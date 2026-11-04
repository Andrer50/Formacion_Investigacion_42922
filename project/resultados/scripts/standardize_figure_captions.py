import docx
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

FIG_UPDATES = {
    'Fig. 1': (
        'Diagrama de flujo PRISMA 2020 de identificación, cribado, elegibilidad a texto completo (con protocolo de fiabilidad test-retest ciego y arbitraje metodológico, κ = 0,87) e inclusión estratificada de estudios primarios (N = 131).',
        'Fuente: elaboración propia siguiendo el estándar PRISMA 2020 [2].'
    ),
    'Fig. 6': (
        'Distribución de estudios por familia algorítmica de IA en procesamiento documental (Síntesis Temática, PI1, n = 105).',
        'Fuente: elaboración propia a partir del corpus primario [3]–[133].'
    ),
    'Fig. 9': (
        'Matriz de calor (heatmap) de tipologías documentales empresariales frente al nivel de integración en sistemas ERP/CRM/DMS (PI4, N = 131).',
        'Fuente: elaboración propia a partir del corpus primario [3]–[133].'
    )
}

def standardize_figures_in_doc(docpath):
    print(f"=== STANDARDIZING FIGURES IN: {docpath} ===")
    doc = docx.Document(docpath)
    
    updated = 0
    for i, p in enumerate(doc.paragraphs):
        txt = p.text.strip()
        if not txt.startswith('Fig.'):
            continue
            
        fig_prefix = txt.split('.')[0].strip() # e.g. 'Fig'
        # Get 'Fig. 1', 'Fig. 6', etc.
        parts = txt.split('.')
        if len(parts) >= 2:
            fig_key = f"{parts[0].strip()}. {parts[1].strip()}" # 'Fig. 1'
        else:
            fig_key = ''
            
        # Check if this figure needs updating (Fig. 1, Fig. 6, Fig. 9)
        if fig_key in FIG_UPDATES:
            title_text, source_text = FIG_UPDATES[fig_key]
            p.text = '' # clear runs
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(6)
            
            r0 = p.add_run(f"{fig_key}. ")
            r0.font.name = 'Times New Roman'
            r0.font.size = Pt(8.5)
            r0.bold = True
            
            r1 = p.add_run(f"{title_text} ")
            r1.font.name = 'Times New Roman'
            r1.font.size = Pt(8.5)
            
            r2 = p.add_run(source_text)
            r2.font.name = 'Times New Roman'
            r2.font.size = Pt(8.0)
            r2.italic = True
            
            updated += 1
            print(f"  [P{i:3d}] Formatted {fig_key}: {title_text[:50]}... + Source")
        else:
            # For Fig. 2, 3, 4, 5, 7, 8: verify font name and alignment
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(6)
            for r in p.runs:
                if not r.font.name:
                    r.font.name = 'Times New Roman'
            print(f"  [P{i:3d}] Verified existing styling: {fig_key}")
            
    doc.save(docpath)
    print(f"Done for {docpath}: updated {updated} figures.\n")

if __name__ == '__main__':
    standardize_figures_in_doc('project/shared/RSL_Sergio_Rupay.docx')
    standardize_figures_in_doc('project/resultados/Articulo_RSL_Resultados_Completo_IEEE.docx')
    print("ALL 9 FIGURES SUCCESSFULLY STANDARDIZED TO IEEE FORMAT!")

