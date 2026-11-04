import docx
import re

doc = docx.Document('project/shared/RSL_Sergio_Rupay.docx')

keywords = [
    'nota', 'aclaratoria', 'docente', 'asesor', 'jimmy', 'utp',
    'gemini', 'claude', 'chatgpt', 'openai', 'llm', 'curso',
    'formación para', 'ati', 'rúbrica', 'entregable'
]

print("=== CHECKING NOTES, COURSE REFERENCES, AI MENTIONS ===")
for i, p in enumerate(doc.paragraphs):
    text_lower = p.text.lower()
    found = [k for k in keywords if k in text_lower]
    if found:
        # print paragraph index and snippet
        print(f"[P{i}] (keywords: {found}):")
        print(f"   {repr(p.text[:130])}...\n")

for t_idx, t in enumerate(doc.tables):
    for r_idx, row in enumerate(t.rows):
        for c_idx, cell in enumerate(row.cells):
            text_lower = cell.text.lower()
            found = [k for k in keywords if k in text_lower]
            if found:
                print(f"[Table {t_idx} R{r_idx}C{c_idx}] (keywords: {found}):")
                print(f"   {repr(cell.text[:100])}...\n")

