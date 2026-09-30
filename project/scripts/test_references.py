import pandas as pd

df = pd.read_csv(r"c:\Users\HP\Desktop\ESCRITORIO\PROYECTOS UNIVERSIDAD\Formacion_Investigacion_42922\project\metodologia\outputs\corpus_included_final.csv")
print(f"Total articles in corpus: {len(df)}")

def format_ieee_authors(auth_str):
    if not isinstance(auth_str, str) or not auth_str.strip():
        return "Anon."
    parts = [p.strip() for p in auth_str.split(";") if p.strip()]
    formatted = []
    for p in parts:
        sub = p.split()
        if len(sub) >= 2:
            last = sub[-1]
            if len(last) <= 3 and last.replace(".", "").isalpha():
                initials = last if last.endswith(".") else last + "."
                surname = " ".join(sub[:-1])
                formatted.append(f"{initials} {surname}")
            else:
                formatted.append(p)
        else:
            formatted.append(p)
    if len(formatted) == 1:
        return formatted[0]
    elif len(formatted) == 2:
        return f"{formatted[0]} and {formatted[1]}"
    elif len(formatted) <= 6:
        join_str = ", ".join(formatted[:-1])
        return f"{join_str}, and {formatted[-1]}"
    else:
        return f"{formatted[0]} et al."

for i, r in df.head(15).iterrows():
    auth = format_ieee_authors(r['authors'])
    title = str(r['title']).strip()
    source = str(r['source_title']).strip()
    year = str(r['year']).strip()
    doi = str(r['doi']).strip()
    doi_str = f", doi: {doi}" if doi and doi.lower() != "nan" else ""
    print(f"[{i+1}] {auth}, \"{title},\" in {source}, {year}{doi_str}.")
