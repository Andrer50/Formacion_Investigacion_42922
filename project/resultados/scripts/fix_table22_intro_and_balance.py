"""
Script para eliminar la frase redundante previa a la TABLA XXII y evitar
la división/balanceo del texto entre dos columnas.
Aplica a:
1. project/shared/RSL_Sergio_Rupay.docx
2. project/resultados/Articulo_RSL_Resultados_Completo_IEEE.docx
3. project/resultados/main.md
"""

import docx
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

TARGET = "en lugar de un doble panel independiente. La TABLA XXII expone la Tabla Resumen de Hallazgos (Summary of Findings - SoF)."
REPLACEMENT = "en lugar de un doble panel independiente (TABLA XXII)."

def update_docx(docx_path):
    print(f"=== Procesando {docx_path} ===")
    doc = docx.Document(docx_path)
    
    # 1. Reemplazar texto en el párrafo previo a Tabla XXII
    modified = False
    for i, p in enumerate(doc.paragraphs):
        if TARGET in p.text:
            for r in p.runs:
                if TARGET in r.text:
                    r.text = r.text.replace(TARGET, REPLACEMENT)
                    modified = True
                    print(f"  [P{i:3d}] Frase redundante reemplazada por '(TABLA XXII)'.")
            if not modified:
                p.text = p.text.replace(TARGET, REPLACEMENT)
                modified = True
                print(f"  [P{i:3d}] Reemplazado a nivel de párrafo.")

    # 2. Configurar compatibilidad dontBalanceSingleOpenSection
    compat = doc.settings._element.find(qn('w:compat'))
    if compat is not None:
        existing = compat.find(qn('w:dontBalanceSingleOpenSection'))
        if existing is None:
            elem = OxmlElement('w:dontBalanceSingleOpenSection')
            compat.append(elem)
            print("  Añadido <w:dontBalanceSingleOpenSection/> a word/settings.xml.")
        else:
            print("  <w:dontBalanceSingleOpenSection/> ya existía.")

    # 3. Ajustar el párrafo del salto de sección previo a Tabla XXII para altura cero
    body = doc._body._element
    for idx, el in enumerate(body):
        if el.tag.endswith('p'):
            sect = el.xpath('.//w:sectPr')
            if sect:
                cols = sect[0].xpath('.//w:cols/@w:num')
                if cols and cols[0] == '2':
                    pPr = el.find(qn('w:pPr'))
                    if pPr is not None:
                        sp = pPr.find(qn('w:spacing'))
                        if sp is None:
                            sp = OxmlElement('w:spacing')
                            pPr.append(sp)
                        sp.set(qn('w:before'), '0')
                        sp.set(qn('w:after'), '0')
                        sp.set(qn('w:line'), '1')
                        sp.set(qn('w:lineRule'), 'exact')
                        print(f"  Salto de sección (elemento body [{idx}]) ajustado a espaciado 0 exacto.")

    doc.save(docx_path)
    print(f"Guardado exitosamente: {docx_path}\n")

def update_markdown(md_path):
    print(f"=== Procesando {md_path} ===")
    with open(md_path, 'r', encoding='utf-8') as f:
        text = f.read()

    target_md = "empresarial corporativo. La TABLA XXII expone la Tabla Resumen de Hallazgos (Summary of Findings - SoF)."
    repl_md = "empresarial corporativo (TABLA XXII)."

    if target_md in text:
        text = text.replace(target_md, repl_md)
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"  Texto actualizado en {md_path}.\n")
    else:
        print(f"  Target no encontrado en {md_path}.\n")

if __name__ == '__main__':
    update_docx('project/shared/RSL_Sergio_Rupay.docx')
    update_docx('project/resultados/Articulo_RSL_Resultados_Completo_IEEE.docx')
    update_markdown('project/resultados/main.md')
    print("¡Ajuste fino de Tabla XXII completado al 100 %!")

