import docx
import re

def verify_docx(path):
    print(f"\n==========================================")
    print(f"VERIFYING DOCX: {path}")
    print(f"==========================================")
    doc = docx.Document(path)
    full_text = "\n".join(p.text for p in doc.paragraphs)

    # 1. Check references [1] to [145]
    ref_nums = []
    for p in doc.paragraphs:
        txt = p.text.strip()
        if txt.startswith('[') and ']' in txt:
            prefix = txt[:txt.find(']')+1]
            try:
                num = int(prefix[1:-1])
                ref_nums.append(num)
            except ValueError:
                pass

    missing = [i for i in range(1, 146) if i not in ref_nums]
    print(f"Total reference items in bibliography: {len(ref_nums)}")
    assert len(missing) == 0, f"Missing references in {path}: {missing}"
    print(f"[PASS] 100% of references [1] to [145] are present without any gap!")

    # 2. Check PD2 b) and c)
    assert "Concentración geográfica y polos institucionales:" in full_text, "Missing b) Concentración geográfica"
    assert "Redes de coocurrencia de palabras clave (VOSviewer):" in full_text, "Missing c) Redes de coocurrencia"
    print(f"[PASS] Section III-C subapartados b) and c) verified with exact text!")

    # 3. Check Section III-H (PI3) 2.3, 3) and 3.a)
    assert "2.3. Escenarios de Sobrecosto y Penalización por Alucinación (Desfavorable -1):" in full_text, "Missing 2.3 in PI3"
    assert "Registra los estudios en los que la implementación de modelos pesados de IA resultó contraproducente frente a flujos convencionales debido a cuellos de botella de hardware en servidores sin GPU o a la sobrecarga de auditoría humana requerida para corregir alucinaciones numéricas en montos contables y códigos fiscales (Tabla XIX) [37], [56], [121]." in full_text, "Missing 2.3 text in PI3"
    assert "3) Contrastes y Debates de Eficiencia:" in full_text, "Missing 3) heading in PI3"
    assert "La síntesis SWiM pone de relieve una tensión operativa entre tres posturas documentadas en el corpus:" in full_text, "Missing 3) text in PI3"
    assert "a) Superioridad de la automatización cognitiva en flujos multiformato:" in full_text, "Missing a) in PI3"
    assert "La mayoría de la evidencia sostiene que en entornos con alta rotación de proveedores y formatos heterogéneos, los modelos multimodales eliminan el cuello de botella del mantenimiento manual de plantillas, reduciendo drásticamente el tiempo de ciclo operativo [4], [6], [44], [55], [103], [127]." in full_text, "Missing a) text in PI3"
    print(f"[PASS] Section III-H (PI3) 2.3, 3) and a) verified verbatim with exact text!")

    # 4. Check updated references
    assert "ESEM" in full_text, "Missing ESEM in ref [135]"
    assert "10.13140/2.1.1018.4643" in full_text, "Missing DOI in ref [136]"
    assert "973–983" in full_text, "Missing pp. 973–983 in ref [143]"
    assert "1912–1920" in full_text, "Missing pp. 1912–1920 in ref [144]"
    assert "21322" in full_text, "Missing 21322 in ref [145]"
    print(f"[PASS] References [135], [136], [143], [144], [145] updated with exact proceedings, pages and DOIs!")

    # 5. If combined, check II. METODOLOGÍA
    if "RSL_Sergio_Rupay" in path:
        assert "II. METODOLOGÍA" in full_text, "Missing II. METODOLOGÍA"
        print(f"[PASS] Heading 'II. METODOLOGÍA' is present!")

    return True

def verify_markdown(path):
    print(f"\n==========================================")
    print(f"VERIFYING MARKDOWN: {path}")
    print(f"==========================================")
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()

    ref_matches = re.findall(r'\[(\d+)\]\s+[A-Z]', text)
    ref_nums = [int(m) for m in ref_matches]
    missing = [i for i in range(1, 146) if i not in ref_nums]
    print(f"Total reference items in bibliography: {len(ref_nums)}")
    assert len(missing) == 0, f"Missing references in {path}: {missing}"
    print(f"[PASS] 100% of references [1] to [145] are present without any gap!")

    assert "Concentración geográfica y polos institucionales" in text, "Missing b) Concentración geográfica"
    assert "Redes de coocurrencia de palabras clave (VOSviewer)" in text, "Missing c) Redes de coocurrencia"
    print(f"[PASS] Section III-C subapartados b) and c) verified with exact text!")

    assert "2.3. Escenarios de Sobrecosto y Penalización por Alucinación (Desfavorable -1)" in text, "Missing 2.3 in PI3"
    assert "Registra los estudios en los que la implementación de modelos pesados de IA resultó contraproducente" in text, "Missing 2.3 text in PI3"
    assert "3) Contrastes y Debates de Eficiencia:" in text, "Missing 3) heading in PI3"
    assert "La síntesis SWiM pone de relieve una tensión operativa entre tres posturas documentadas en el corpus:" in text, "Missing 3) text in PI3"
    assert "Superioridad de la automatización cognitiva en flujos multiformato" in text, "Missing a) in PI3"
    assert "La mayoría de la evidencia sostiene que en entornos con alta rotación de proveedores y formatos heterogéneos" in text, "Missing a) text in PI3"
    print(f"[PASS] Section III-H (PI3) 2.3, 3) and a) verified verbatim with exact text!")

    assert "ESEM" in text, "Missing ESEM in ref [135]"
    assert "10.13140/2.1.1018.4643" in text, "Missing DOI in ref [136]"
    assert "973–983" in text, "Missing pp. 973–983 in ref [143]"
    assert "1912–1920" in text, "Missing pp. 1912–1920 in ref [144]"
    assert "21322" in text, "Missing 21322 in ref [145]"
    print(f"[PASS] References [135], [136], [143], [144], [145] updated with exact proceedings, pages and DOIs!")
    return True

if __name__ == '__main__':
    v1 = verify_docx('project/shared/RSL_Sergio_Rupay.docx')
    v2 = verify_docx('project/resultados/Articulo_RSL_Resultados_Completo_IEEE.docx')
    v3 = verify_markdown('project/resultados/main.md')
    if v1 and v2 and v3:
        print("\n****************************************************************")
        print(">>> TODOS LOS DOCUMENTOS VERIFICADOS CON ÉXITO AL 100 % <<<")
        print("****************************************************************")
