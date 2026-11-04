import docx

def repair_step_1():
    docx_path = 'project/shared/RSL_Sergio_Rupay.docx'
    doc = docx.Document(docx_path)
    
    idx_p1 = -1
    idx_p3 = -1
    
    for i, p in enumerate(doc.paragraphs):
        if '1) Fragilidad Operativa de Enfoques Tradicionales:' in p.text:
            idx_p1 = i
        if '3) Brecha de Integración Transaccional con Sistemas ERP/CRM:' in p.text:
            idx_p3 = i
            
    print(f"Found 1) at index {idx_p1}")
    print(f"Found 3) at index {idx_p3}")
    
    assert idx_p1 != -1, "No se encontró el párrafo 1) Fragilidad Operativa"
    assert idx_p3 != -1, "No se encontró el párrafo 3) Brecha de Integración"
    assert idx_p3 >= idx_p1 + 1, "Inconsistencia en el orden de los párrafos 1) y 3)"
    
    target_text_2 = (
        "2) Sesgos y Desconexión de los Bancos de Pruebas (Benchmarks): "
        "Gran parte de los modelos del estado del arte se entrena y evalúa exclusivamente "
        "sobre conjuntos de datos públicos estáticos de tamaño reducido y condiciones controladas "
        "(SROIE, CORD, FUNSD), los cuales no reflejan la severa degradación física, pliegues, "
        "sellos superpuestos, tintas térmicas desvanecidas ni la complejidad tabular de los flujos "
        "documentales reales en las empresas [14], [30], [39], [60], [100]."
    )
    
    if idx_p3 == idx_p1 + 1:
        # Párrafo 2 no existía en absoluto entre 1 y 3; insertamos antes de 3
        p3 = doc.paragraphs[idx_p3]
        new_p = p3.insert_paragraph_before(target_text_2)
        print("Párrafo 2 insertado antes de 3).")
    else:
        # Párrafo 2 está en idx_p1 + 1
        p2 = doc.paragraphs[idx_p1 + 1]
        p2.text = target_text_2
        print(f"Párrafo 2 actualizado en índice {idx_p1 + 1}.")
        
    doc.save(docx_path)
    print("Guardado exitosamente en project/shared/RSL_Sergio_Rupay.docx")

if __name__ == '__main__':
    repair_step_1()

