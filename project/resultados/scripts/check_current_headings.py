import docx
import re

doc = docx.Document('project/shared/RSL_Sergio_Rupay.docx')

print("=== CHECKING HEADINGS IN DOCX ===")
headings = [p.text.strip() for p in doc.paragraphs if p.style.name.startswith('Heading') or p.text.startswith(('I.', 'II.', 'III.', 'IV.', 'V.', 'VI.', 'VII.', 'A.', 'B.', 'C.', 'D.', 'E.', 'F.', 'G.', 'H.', 'I.', 'J.', 'K.'))]
for h in headings[:35]:
    print(' ', h)

print("\n=== CHECKING TABLES IN DOCX ===")
tables_found = []
for p in doc.paragraphs:
    t = p.text.strip()
    if t.startswith('TABLA ') or t.startswith('Tabla '):
        tables_found.append(t.split('\n')[0])
for t in tables_found:
    print(' ', t)

