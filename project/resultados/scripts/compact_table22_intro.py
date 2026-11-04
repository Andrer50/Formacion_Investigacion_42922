"""
Script para parafrasear y compactar la introducción de la TABLA XXII (Sección III-K).
Reduce ~434 caracteres (~6 líneas) para asegurar que el texto quepa íntegramente
en la página anterior y la TABLA XXII comience limpia al inicio de una sola página.
"""

import docx
from docx.shared import Pt

TARGET_SUBSTRING = "adaptando los cuatro dominios del marco GRADE-CERQual (Confidence in the Evidence"

COMPACT_TEXT = (
    "Conforme a las directrices SWiM (Campbell et al. [137]) y Popay et al. [136], "
    "se estructuró un juicio narrativo de confianza adaptando los cuatro dominios de "
    "GRADE-CERQual (Lewin et al. [140]): 1) limitaciones metodológicas (QA de [1]), "
    "2) coherencia técnica de hallazgos, 3) adecuación de datos empíricos, y "
    "4) relevancia en flujos ERP/CRM corporativos. Como limitación metodológica, "
    "los niveles de certeza fueron definidos operacionalmente por el autor y "
    "validados con el asesor metodológico, en lugar de un doble panel independiente (TABLA XXII)."
)

def update_docx(docx_path):
    print(f"=== Procesando {docx_path} ===")
    doc = docx.Document(docx_path)
    updated = False
    
    for i, p in enumerate(doc.paragraphs):
        # Asegurar que sea exclusivamente el párrafo previo a TABLA XXII
        if TARGET_SUBSTRING in p.text and ("III-K" in doc.paragraphs[i-1].text or "K. Calificación" in doc.paragraphs[i-1].text):
            orig_len = len(p.text)
            
            # Limpiar runs
            for r in list(p.runs):
                p._element.remove(r._r)
                
            # Agregar el texto compactado
            r = p.add_run(COMPACT_TEXT)
            r.bold = False
            r.font.name = 'Times New Roman'
            r.font.size = Pt(9.5)
            
            updated = True
            new_len = len(COMPACT_TEXT)
            print(f"  [P{i:3d}] Párrafo compactado: {orig_len} -> {new_len} caracteres (ahorro de {orig_len - new_len} caracteres / ~6 líneas).")
            
    doc.save(docx_path)
    print(f"Guardado exitosamente: {docx_path}\n")

if __name__ == '__main__':
    update_docx('project/shared/RSL_Sergio_Rupay.docx')
    update_docx('project/resultados/Articulo_RSL_Resultados_Completo_IEEE.docx')
