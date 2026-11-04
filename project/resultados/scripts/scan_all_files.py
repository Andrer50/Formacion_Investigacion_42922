import docx
import os
import re

files_to_scan = [
    r'.\README.md',
    r'.\project\introduccion\Introduccion_RSL.docx',
    r'.\project\metodologia\main.md',
    r'.\project\metodologia\Metodologia_RSL_IEEE.docx',
    r'.\project\metodologia\outputs\reporte_prisma_paso_a_paso.md',
    r'.\project\resultados\Articulo_RSL_Resultados_Completo_IEEE.docx',
    r'.\project\resultados\main.md',
    r'.\project\shared\RSL_Sergio_Rupay.docx'
]

patterns = [
    r'\btu\b', r'\btus\b', r'\bti\b', r'\busted\b',
    r'seg[uú]n tu', r'tu modelo', r'mi modelo', r'nuestro modelo',
    r'modelo que us', r'modelo propuesto',
    r'esta semana', r'la semana', r'de esta semana',
    r'presentaci[oó]n de esta', r'para la presentaci',
    r'como mencion', r'como pedist', r'como solicit',
    r'aquí tienes', r'a continuación te', r'adjunto',
    r'entregable', r'r[uú]brica'
]

compiled = re.compile('|'.join(patterns), re.IGNORECASE)

for fpath in files_to_scan:
    if not os.path.exists(fpath):
        continue
    print(f"\n==================== SCANNING: {fpath} ====================")
    text_items = []
    if fpath.endswith('.docx'):
        doc = docx.Document(fpath)
        for i, p in enumerate(doc.paragraphs):
            text_items.append((f"P{i}", p.text))
        for t_idx, t in enumerate(doc.tables):
            for r_idx, row in enumerate(t.rows):
                for c_idx, cell in enumerate(row.cells):
                    text_items.append((f"T{t_idx}R{r_idx}C{c_idx}", cell.text))
    else:
        with open(fpath, 'r', encoding='utf-8') as f:
            for l_idx, line in enumerate(f.readlines()):
                text_items.append((f"Line {l_idx+1}", line.strip()))
                
    hits = 0
    for loc, text in text_items:
        matches = compiled.findall(text)
        if matches:
            # filter out purely false positives if needed, but let's print
            for m in set(matches):
                # find context
                for f in re.finditer(re.escape(m), text, re.IGNORECASE):
                    start = max(0, f.start() - 35)
                    end = min(len(text), f.end() + 35)
                    print(f"  [{loc}] ({m}): ...{repr(text[start:end])}...")
                    hits += 1
    if hits == 0:
        print("  -> ZERO hits found.")

