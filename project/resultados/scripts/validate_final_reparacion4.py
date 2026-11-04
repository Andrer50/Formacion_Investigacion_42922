import docx

def validate_full_manuscript(docx_path):
    print("=" * 70)
    print(f"VALIDACIÓN OBLIGATORIA SOBRE MANUSCRITO COMPLETO: {docx_path}")
    print("=" * 70)
    
    doc = docx.Document(docx_path)
    paragraphs = [p.text for p in doc.paragraphs]
    doc_text = "\n".join(paragraphs)
    
    # Extract Section VII (Referencias Bibliográficas)
    sec_vii_idx = -1
    for i, p in enumerate(doc.paragraphs):
        if "VII. REFERENCIAS BIBLIOGRÁFICAS" in p.text:
            sec_vii_idx = i
            break
            
    assert sec_vii_idx != -1, "No se encontró el encabezado 'VII. REFERENCIAS BIBLIOGRÁFICAS'"
    
    appendix_idx = len(doc.paragraphs)
    for i in range(sec_vii_idx + 1, len(doc.paragraphs)):
        if "APÉNDICE" in doc.paragraphs[i].text.upper() or "MATERIAL SUPLEMENTARIO" in doc.paragraphs[i].text.upper():
            appendix_idx = i
            break
            
    seccion_vii_text = "\n".join([p.text for p in doc.paragraphs[sec_vii_idx:appendix_idx]])
    
    # ASSERT 1: doc_text.count("Ciento treinta y un estudios (100,0 % del corpus; TABLA XX, Fig. 9)") == 1
    c1 = doc_text.count("Ciento treinta y un estudios (100,0 % del corpus; TABLA XX, Fig. 9)")
    print(f"[ASSERT 1] doc_text.count('Ciento treinta y un estudios (100,0 % del corpus; TABLA XX, Fig. 9)') == {c1}")
    assert c1 == 1, f"Fallo en ASSERT 1: Aparece {c1} veces (debe ser 1)."
    print("  -> PASÓ: Apertura de PI4 única y sin triplicación en PD1-PD3.")

    # ASSERT 2: doc_text.count("La columna de sistema corporativo describe el mapeo funcional conceptual") == 1
    c2 = doc_text.count("La columna de sistema corporativo describe el mapeo funcional conceptual")
    print(f"[ASSERT 2] doc_text.count('La columna de sistema corporativo describe el mapeo funcional conceptual') == {c2}")
    assert c2 == 1, f"Fallo en ASSERT 2: Aparece {c2} veces (debe ser 1)."
    print("  -> PASÓ: Nota de TABLA XX única y sin repetición en TABLAS XXI, XXII y S1.")

    # ASSERT 3: "2) Sesgos y Desconexión de los Bancos de Pruebas" in doc_text
    c3 = "2) Sesgos y Desconexión de los Bancos de Pruebas" in doc_text
    print(f"[ASSERT 3] '2) Sesgos y Desconexión de los Bancos de Pruebas' in doc_text == {c3}")
    assert c3, "Fallo en ASSERT 3: No se encontró la brecha 2 en Sección I-B."
    print("  -> PASÓ: Párrafo 2) de brechas presente en Sección I-B.")

    # ASSERT 4: all(f"[{i}]" in seccion_vii_text for i in range(1, 146))
    c4 = all(f"[{i}]" in seccion_vii_text for i in range(1, 146))
    print(f"[ASSERT 4] all(f'[{{i}}]' in seccion_vii_text for i in range(1, 146)) == {c4}")
    assert c4, "Fallo en ASSERT 4: Faltan números de referencia en Sección VII."
    print("  -> PASÓ: 145/145 referencias presentes del [1] al [145] continuas y sin saltos.")

    print("\n" + "=" * 70)
    print(">>> 100 % DE LOS ASSERTS OBLIGATORIOS PASARON SATISFACTORIAMENTE <<<")
    print("=" * 70 + "\n")

if __name__ == "__main__":
    validate_full_manuscript("project/shared/RSL_Sergio_Rupay.docx")
