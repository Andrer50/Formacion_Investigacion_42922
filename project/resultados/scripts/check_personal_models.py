import docx
import re

doc = docx.Document('project/shared/RSL_Sergio_Rupay.docx')

print("=== CHECKING FOR PERSONAL MODEL REFERENCES ===")
model_triggers = [
    r'\bnuestr[oa]s?\s+modelo',
    r'\bmi\s+modelo',
    r'\btu\s+modelo',
    r'\bsu\s+modelo',
    r'modelo\s+propuesto',
    r'modelo\s+desarrollado',
    r'modelo\s+que\s+us',
    r'modelo\s+utilizado\s+por\s+nosotros',
    r'nuestra\s+propuesta',
    r'nuestro\s+sistema',
    r'nuestro\s+enfoque',
    r'nuestro\s+experimento',
    r'mi\s+investigaci[oó]n',
    r'tu\s+investigaci[oó]n',
    r'según\s+tu',
    r'según\s+el\s+modelo\s+que',
    r'presentaci[oó]n\s+de\s+esta\s+semana',
    r'esta\s+semana',
    r'para\s+esta\s+semana',
    r'para\s+la\s+presentaci[oó]n',
    r'entregable',
    r'r[uú]brica',
    r'tarea',
    r'semana\s*\d+',
    r'avance\s*\d+'
]

pattern = re.compile('|'.join(model_triggers), re.IGNORECASE)

found_any = False
for i, p in enumerate(doc.paragraphs):
    m = pattern.findall(p.text)
    if m:
        found_any = True
        print(f"P{i}: Match {m}")
        for match in set(m):
            for f in re.finditer(re.escape(match), p.text, re.IGNORECASE):
                start = max(0, f.start() - 40)
                end = min(len(p.text), f.end() + 40)
                print(f"   Snippet: {repr(p.text[start:end])}")

for t_idx, t in enumerate(doc.tables):
    for r_idx, row in enumerate(t.rows):
        for c_idx, cell in enumerate(row.cells):
            m = pattern.findall(cell.text)
            if m:
                found_any = True
                print(f"Table {t_idx} R{r_idx}C{c_idx}: Match {m}")
                print(f"   Snippet: {repr(cell.text[:100])}")

if not found_any:
    print("NO matches found for personal model triggers!")

