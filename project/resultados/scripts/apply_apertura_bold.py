"""
Script para asegurar que '1) Apertura: ' esté en negrita (bold=True)
en todos los bloques de resultados (PD1, PD2, PD3, PI1, PI2, PI3, PI4).
Aplica a:
1. project/shared/RSL_Sergio_Rupay.docx
2. project/resultados/Articulo_RSL_Resultados_Completo_IEEE.docx
3. project/resultados/main.md
"""

import docx
from docx.shared import Pt

PREFIX = "1) Apertura: "

def update_docx(docx_path):
    print(f"=== Procesando {docx_path} ===")
    doc = docx.Document(docx_path)
    count = 0
    
    for i, p in enumerate(doc.paragraphs):
        txt = p.text.strip()
        if txt.startswith("1) Apertura:"):
            # Comprobar si el primer run ya es '1) Apertura: ' con bold=True
            already_bold = False
            for r in p.runs:
                if "1) Apertura:" in r.text and r.bold is True:
                    already_bold = True
                    break
            
            if not already_bold:
                full_text = p.text
                idx = full_text.find("1) Apertura:")
                prefix = full_text[:idx + len(PREFIX)]
                rest = full_text[idx + len(PREFIX):]
                
                # Limpiar runs existentes
                for r in list(p.runs):
                    p._element.remove(r._r)
                    
                # Crear run en negrita para '1) Apertura: '
                r0 = p.add_run(prefix)
                r0.bold = True
                r0.font.name = 'Times New Roman'
                r0.font.size = Pt(9.5)
                
                # Crear run normal para el texto restante
                r1 = p.add_run(rest)
                r1.bold = False
                r1.font.name = 'Times New Roman'
                r1.font.size = Pt(9.5)
                
                count += 1
                print(f"  [P{i:3d}] Aplicada negrita a '{prefix.strip()}'")
            else:
                print(f"  [P{i:3d}] Ya tenía negrita en '1) Apertura:'.")
                
    doc.save(docx_path)
    print(f"Guardado exitosamente {docx_path} con {count} párrafos actualizados.\n")

def update_markdown(md_path):
    print(f"=== Procesando {md_path} ===")
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Reemplazar '1) Apertura:' cuando no esté ya en negrita
    import re
    # Match 1) Apertura: not preceded by **
    new_content, count = re.subn(r'(?<!\*\*)1\) Apertura:', r'**1) Apertura:**', content)
    
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"Guardado {md_path} con {count} reemplazos en Markdown.\n")

if __name__ == '__main__':
    update_docx('project/shared/RSL_Sergio_Rupay.docx')
    update_docx('project/resultados/Articulo_RSL_Resultados_Completo_IEEE.docx')
    update_markdown('project/resultados/main.md')
    print("¡Proceso de negrita para Apertura completado exitosamente!")

