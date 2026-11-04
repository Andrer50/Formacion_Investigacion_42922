import docx
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

def standardize_document_table_notes(docpath):
    print(f"=== STANDARDIZING TABLE NOTES IN: {docpath} ===")
    doc = docx.Document(docpath)
    
    modified_count = 0
    for i, p in enumerate(doc.paragraphs):
        txt = p.text.strip()
        # Check if paragraph is a table note/footnote
        is_table_note = False
        if txt.startswith(('Fuente:', '*Fuente:', 'Nota:', '*Nota:', '* Nota:', '*Nota metodológica:')):
            is_table_note = True
        elif txt.startswith('Nota de alcance sobre Población y Contexto:'):
            is_table_note = True
            
        if is_table_note:
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(6)
            for r in p.runs:
                r.font.name = 'Times New Roman'
                r.font.size = Pt(8.0)
                r.italic = True
            modified_count += 1
            print(f"  [P{i:3d}] Formatted: {txt[:65]}...")
            
    doc.save(docpath)
    print(f"Total notes formatted in {docpath}: {modified_count}\n")

if __name__ == '__main__':
    standardize_document_table_notes('project/shared/RSL_Sergio_Rupay.docx')
    standardize_document_table_notes('project/resultados/Articulo_RSL_Resultados_Completo_IEEE.docx')
    print("SUCCESS: All table notes standardized to Times New Roman, 8.0 pt, Italic=True.")

