import docx
import re

doc = docx.Document('project/shared/RSL_Sergio_Rupay.docx')

triggers = [
    r'\byo\b', r'\bme\b', r'\bmi\b', r'\bmis\b', r'\bmío\b', r'\bmía\b',
    r'\btú\b', r'\btu\b', r'\btus\b', r'\bte\b', r'\bti\b',
    r'\busted\b', r'\bustedes\b',
    r'\bdiapositiva\b', r'\bppt\b', r'\bpresentaci[oó]n\b',
    r'\bsemana\b', r'\bclase\b', r'\bsesi[oó]n\b', r'\bchat\b',
    r'\bprompt\b', r'según tu', r'tu modelo', r'mi modelo'
]

compiled = re.compile('|'.join(triggers), re.IGNORECASE)

print("=== CHECKING TABLES FOR 1ST/2ND PERSON & META WORDS ===")
table_hits = 0
for t_idx, t in enumerate(doc.tables):
    for r_idx, row in enumerate(t.rows):
        for c_idx, cell in enumerate(row.cells):
            matches = list(compiled.finditer(cell.text))
            for m in matches:
                table_hits += 1
                word = m.group(0).lower()
                start = max(0, m.start() - 25)
                end = min(len(cell.text), m.end() + 25)
                snippet = cell.text[start:end].replace('\n', ' ')
                print(f"Table {t_idx} R{r_idx}C{c_idx} [Trigger: {word}]: ...{snippet}...")

if table_hits == 0:
    print("ZERO triggers found in any table!")

