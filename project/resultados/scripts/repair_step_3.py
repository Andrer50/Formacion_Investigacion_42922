import docx
import re

def repair_table_notes(docx_path):
    print(f"Repairing table notes in {docx_path}...")
    doc = docx.Document(docx_path)
    
    note_t21 = (
        "Fuente: elaboración propia a partir del corpus primario [3]–[133]. "
        "Análisis de sensibilidad metodológica excluyendo los 10 estudios del estrato inferior "
        "(QA = 3,50 pts: [116]–[118], [121]–[123], [127], [128], [132], [133])."
    )
    
    note_t22 = (
        "Fuente: elaboración propia a partir del corpus primario [3]–[133]. "
        "Evaluación estructurada de certeza adaptada de los cuatro dominios GRADE-CERQual "
        "(Lewin et al. [140]) e integrada bajo directrices SWiM (Campbell et al. [137])."
    )
    
    note_ts1 = (
        "Fuente: elaboración propia a partir del corpus primario [3]–[133]. "
        "Cuartiles verificados en Scimago Journal Rank (SJR) y Journal Citation Reports (JCR) "
        "vigentes al período de publicación."
    )
    
    for i, p in enumerate(doc.paragraphs):
        # Look for TABLA XXII first so it doesn't collide with TABLA XXI
        if re.match(r"^TABLA\s+XXII\b", p.text.strip()):
            target_p = doc.paragraphs[i + 1]
            print(f"Found TABLA XXII at {i}. Replacing paragraph {i+1} with note_t22.")
            target_p.text = note_t22
            
        elif re.match(r"^TABLA\s+XXI\b", p.text.strip()):
            target_p = doc.paragraphs[i + 1]
            print(f"Found TABLA XXI at {i}. Replacing paragraph {i+1} with note_t21.")
            target_p.text = note_t21
            
        elif re.match(r"^TABLA\s+S1\b", p.text.strip()):
            target_p = doc.paragraphs[i + 1]
            print(f"Found TABLA S1 at {i}. Replacing paragraph {i+1} with note_ts1.")
            target_p.text = note_ts1
            
    doc.save(docx_path)
    print(f"Saved {docx_path} successfully.\n")

if __name__ == '__main__':
    repair_table_notes('project/shared/RSL_Sergio_Rupay.docx')
    repair_table_notes('project/resultados/Articulo_RSL_Resultados_Completo_IEEE.docx')
