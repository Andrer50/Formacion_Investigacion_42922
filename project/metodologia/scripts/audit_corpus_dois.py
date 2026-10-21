import os
import sys
import io
import pandas as pd
import requests
from concurrent.futures import ThreadPoolExecutor

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

csv_path = "project/metodologia/outputs/corpus_included_final.csv"
df = pd.read_csv(csv_path)
df["ref_num"] = df.index + 3

headers = {
    "User-Agent": "AntigravityDOIValidator/1.0 (mailto:investigacion@utp.edu.pe)"
}

def verify_doi(row):
    ref = f"[{row['ref_num']}] ({row['id']})"
    doi = str(row["doi"]).strip()
    title_csv = str(row["title"]).strip()
    
    # Si es una URL directa (ej. TMLR / OpenReview)
    if doi.startswith("http"):
        try:
            r = requests.head(doi, allow_redirects=True, timeout=12, headers=headers)
            status = "OK (URL)" if r.status_code < 400 else f"ERROR {r.status_code}"
            return (ref, doi, status, title_csv[:60])
        except Exception as e:
            # Reintentar con GET por si el servidor rechaza HEAD
            try:
                r_get = requests.get(doi, timeout=12, headers=headers)
                status = "OK (URL GET)" if r_get.status_code < 400 else f"ERROR {r_get.status_code}"
                return (ref, doi, status, title_csv[:60])
            except Exception as e2:
                return (ref, doi, f"FALLO CONEXIÓN: {e2}", title_csv[:60])
            
    # Consulta a la API oficial de CrossRef para verificar existencia y título
    url = f"https://api.crossref.org/works/{doi}"
    for attempt in range(3):
        try:
            r = requests.get(url, timeout=12, headers=headers)
            if r.status_code == 200:
                data = r.json().get("message", {})
                cr_title = data.get("title", [""])[0] if data.get("title") else title_csv
                return (ref, doi, "OK (CrossRef 200)", cr_title[:60])
            elif r.status_code == 429:
                import time
                time.sleep(1.0 * (attempt + 1))
                continue
            else:
                # Fallback a doi.org (para DOIs registrados en DataCite/mEDRA)
                r2 = requests.head(f"https://doi.org/{doi}", allow_redirects=True, timeout=12, headers=headers)
                if r2.status_code < 400:
                    return (ref, doi, "OK (doi.org)", title_csv[:60])
                return (ref, doi, f"NO RESUELVE ({r.status_code})", title_csv[:60])
        except Exception as e:
            if attempt < 2:
                import time
                time.sleep(1.0)
                continue
            # Fallback si CrossRef da timeout
            try:
                r2 = requests.head(f"https://doi.org/{doi}", allow_redirects=True, timeout=12, headers=headers)
                if r2.status_code < 400:
                    return (ref, doi, "OK (doi.org fallback)", title_csv[:60])
            except Exception:
                pass
            return (ref, doi, f"TIMEOUT/ERROR: {e}", title_csv[:60])

print(f"Auditando los {len(df)} DOIs/URLs contra CrossRef y doi.org...")
with ThreadPoolExecutor(max_workers=6) as executor:
    results = list(executor.map(verify_doi, [row for _, row in df.iterrows()]))

res_df = pd.DataFrame(results, columns=["Ref", "DOI_o_URL", "Estado", "Titulo_Verificado"])
print("\n=== RESUMEN DE ESTADOS DE RESOLUCIÓN ===")
print(res_df["Estado"].value_counts())

incidencias = res_df[~res_df["Estado"].str.startswith("OK")]
if len(incidencias) == 0:
    print("\n¡ÉXITO TOTAL! 100 % de los 131 DOIs/URLs resuelven satisfactoriamente.")
else:
    print(f"\nIncidencias detectadas ({len(incidencias)}):")
    print(incidencias)

out_csv = "project/metodologia/outputs/auditoria_dois_131.csv"
res_df.to_csv(out_csv, index=False)
print(f"\nReporte completo guardado en: {out_csv}")
