import docx
import os
import re

def scan_docx_thorough(fpath):
    print(f"=== FULL SCAN: {fpath} ===")
    doc = docx.Document(fpath)
    
    all_texts = []
    
    # 1. Paragraphs
    for i, p in enumerate(doc.paragraphs):
        all_texts.append((f"Paragraph {i}", p.text))
        
    # 2. Tables
    for t_idx, t in enumerate(doc.tables):
        for r_idx, row in enumerate(t.rows):
            for c_idx, cell in enumerate(row.cells):
                all_texts.append((f"Table {t_idx} R{r_idx}C{c_idx}", cell.text))
                
    # 3. Headers and footers
    for s_idx, sec in enumerate(doc.sections):
        for p in sec.header.paragraphs:
            all_texts.append((f"Section {s_idx} Header", p.text))
        for p in sec.footer.paragraphs:
            all_texts.append((f"Section {s_idx} Footer", p.text))
            
    # Search patterns
    patterns = [
        (r'\bsemana\b', 'semana'),
        (r'presentaci[oó]n\b', 'presentación'),
        (r'\btu\b', 'tu (2da persona)'),
        (r'\btus\b', 'tus (2da persona)'),
        (r'\busted\b', 'usted'),
        (r'seg[uú]n tu', 'según tu'),
        (r'para la presentaci', 'para la presentación'),
        (r'de esta semana', 'de esta semana'),
        (r'esta semana', 'esta semana'),
        (r'entrega\b', 'entrega'),
        (r'r[uú]brica\b', 'rúbrica'),
        (r'tarea\b', 'tarea'),
        (r'prompt\b', 'prompt'),
        (r'nota del autor', 'nota del autor'),
        (r'nota para', 'nota para'),
        (r'instrucci[oó]n', 'instrucción'),
        (r'como se pidi[oó]', 'como se pidió'),
        (r'como pediste', 'como pediste'),
        (r'como solicitaste', 'como solicitaste'),
        (r'el modelo que us', 'el modelo que use/usaste'),
        (r'tu modelo', 'tu modelo'),
        (r'mi modelo', 'mi modelo'),
        (r'nuestro modelo', 'nuestro modelo')
    ]
    
    hits = []
    for loc, text in all_texts:
        if not text.strip():
            continue
        for pat, label in patterns:
            m = re.findall(pat, text, re.IGNORECASE)
            if m:
                # find context
                for match in re.finditer(pat, text, re.IGNORECASE):
                    start = max(0, match.start() - 40)
                    end = min(len(text), match.end() + 40)
                    hits.append((loc, label, text[start:end].replace('\n', ' ')))
                    
    print(f"Total hits in {fpath}: {len(hits)}")
    for loc, label, snippet in hits:
        print(f"  [{loc}] ({label}): ...{snippet}...")

scan_docx_thorough('project/shared/RSL_Sergio_Rupay.docx')

