import docx
from docx.shared import Pt
import re

def update_rupay_docx(file_path):
    print(f"\n--- Modificando {file_path} ---")
    doc = docx.Document(file_path)

    # Helper to set paragraph runs cleanly
    def set_p_runs(p, prefix, body, font_size=9.5):
        for r in p._element.xpath('./w:r'):
            p._element.remove(r)
        if prefix:
            r_pre = p.add_run(prefix)
            r_pre.font.name = "Times New Roman"
            r_pre.font.size = Pt(font_size)
            r_pre.bold = True
        r_bod = p.add_run(body)
        r_bod.font.name = "Times New Roman"
        r_bod.font.size = Pt(font_size)
        r_bod.bold = False

    # 1. Sección III-F (PI1)
    # 1a. P138: 2.1. Canalizaciones Híbridas
    p138 = doc.paragraphs[138]
    assert "2.1. Canalizaciones Híbridas" in p138.text, f"P138 mismatch: {p138.text[:50]}"
    old_end_1a = "alta interpretabilidad modular."
    new_end_1a = "alta interpretabilidad modular [12], [44], [55], [71]."
    assert old_end_1a in p138.text, f"Old end 1a not found in P138: {p138.text[-50:]}"
    full_text_1a = p138.text.replace(old_end_1a, new_end_1a)
    prefix_1a = "2.1. Canalizaciones Híbridas (Pipelines) CNN-RNN y Segmentación Clásica con OCR: "
    body_1a = full_text_1a.replace(prefix_1a, "")
    set_p_runs(p138, prefix_1a, body_1a)
    print("  [1a] III-F (2.1) actualizado con [12], [44], [55], [71].")

    # 1b. P140: 2.3. Redes Neuronales de Grafos
    p140 = doc.paragraphs[140]
    assert "2.3. Redes Neuronales de Grafos" in p140.text, f"P140 mismatch: {p140.text[:50]}"
    old_end_1b = "frente a transformadores masivos."
    new_end_1b = "frente a transformadores masivos [8], [29], [34], [40], [75]."
    assert old_end_1b in p140.text, f"Old end 1b not found in P140: {p140.text[-50:]}"
    full_text_1b = p140.text.replace(old_end_1b, new_end_1b)
    prefix_1b = "2.3. Redes Neuronales de Grafos y Modelado Espacial-Relacional (GNN): "
    body_1b = full_text_1b.replace(prefix_1b, "")
    set_p_runs(p140, prefix_1b, body_1b)
    print("  [1b] III-F (2.3) actualizado con [8], [29], [34], [40], [75].")

    # 1c. P146: 4) Cierre y Tendencias (PI1)
    p146 = doc.paragraphs[146]
    assert "verificadores basados en reglas" in p146.text, f"P146 mismatch: {p146.text[:50]}"
    old_end_1c = "verificadores basados en reglas."
    new_end_1c = "verificadores basados en reglas [6], [7], [82], [115]."
    assert old_end_1c in p146.text
    full_text_1c = p146.text.replace(old_end_1c, new_end_1c)
    prefix_1c = "4) Cierre y Tendencias: "
    body_1c = full_text_1c.replace(prefix_1c, "")
    set_p_runs(p146, prefix_1c, body_1c)
    print("  [1c] III-F (4) Cierre actualizado con [6], [7], [82], [115].")

    # 2. Sección III-G (PI2)
    # 2a. P154: 2.1. Recibos y Facturas Comerciales
    p154 = doc.paragraphs[154]
    assert "2.1. Recibos y Facturas Comerciales" in p154.text, f"P154 mismatch: {p154.text[:50]}"
    prefix_2a = "2.1. Recibos y Facturas Comerciales (Benchmarks SROIE y CORD): "
    body_2a = (
        "Esta categoría evalúa la extracción automatizada de campos clave fijos (razón social, fecha de emisión, "
        "dirección y monto total) sobre comprobantes comerciales estándar (Tabla XVIII). La regularidad topológica "
        "y la presencia recurrente de encabezados permiten a las arquitecturas alcanzar la mediana de F1-score más alta "
        "del corpus (95,2 % global, con mediana de 95,2 % [86,4 % – 98,7 %] en SROIE y 94,1 % [88,0 % – 97,4 %] en CORD; "
        "Tabla XVIII, Fig. 7) y latencias de inferencia reducidas (80 ms a 450 ms) [4], [6], [7], [9], [30], [74]."
    )
    set_p_runs(p154, prefix_2a, body_2a)
    print("  [2a] III-G (2.1) reemplazado con mediana CORD y citas [4], [6], [7], [9], [30], [74].")

    # 2b. P155: 2.2. Tablas Financieras y Estructuras Matriciales
    p155 = doc.paragraphs[155]
    assert "2.2. Tablas Financieras" in p155.text, f"P155 mismatch: {p155.text[:50]}"
    old_end_2b = "(Tabla XVIII, Fig. 7)."
    new_end_2b = "(Tabla XVIII, Fig. 7) [5], [8], [11], [35], [41], [66]."
    assert old_end_2b in p155.text, f"Old end 2b not found in P155: {p155.text[-50:]}"
    full_text_2b = p155.text.replace(old_end_2b, new_end_2b)
    prefix_2b = "2.2. Tablas Financieras y Estructuras Matriciales (Benchmarks FinTabNet y WTW): "
    body_2b = full_text_2b.replace(prefix_2b, "")
    set_p_runs(p155, prefix_2b, body_2b)
    print("  [2b] III-G (2.2) actualizado con [5], [8], [11], [35], [41], [66].")

    # 2c. P156: 2.3. Formularios Semiestructurados Ruidosos
    p156 = doc.paragraphs[156]
    assert "2.3. Formularios Semiestructurados" in p156.text, f"P156 mismatch: {p156.text[:50]}"
    old_end_2c = "frente a comprobantes estandarizados."
    new_end_2c = "frente a comprobantes estandarizados [14], [18], [21], [26], [42], [77], [92]."
    assert old_end_2c in p156.text, f"Old end 2c not found in P156: {p156.text[-50:]}"
    full_text_2c = p156.text.replace(old_end_2c, new_end_2c)
    prefix_2c = "2.3. Formularios Semiestructurados Ruidosos (Benchmark FUNSD): "
    body_2c = full_text_2c.replace(prefix_2c, "")
    set_p_runs(p156, prefix_2c, body_2c)
    print("  [2c] III-G (2.3) actualizado con [14], [18], [21], [26], [42], [77], [92].")

    # 2d. P162: 4) Cierre y Tendencias (PI2)
    p162 = doc.paragraphs[162]
    assert "esquemas de preprocesamiento más robustos" in p162.text, f"P162 mismatch: {p162.text[:50]}"
    old_end_2d = "esquemas de preprocesamiento más robustos."
    new_end_2d = "esquemas de preprocesamiento más robustos [14], [30], [70], [85]."
    assert old_end_2d in p162.text, f"Old end 2d not found in P162: {p162.text[-50:]}"
    full_text_2d = p162.text.replace(old_end_2d, new_end_2d)
    prefix_2d = "4) Cierre y Tendencias: "
    body_2d = full_text_2d.replace(prefix_2d, "")
    set_p_runs(p162, prefix_2d, body_2d)
    print("  [2d] III-G (4) Cierre actualizado con [14], [30], [70], [85].")

    # 3. Sección III-H (PI3)
    # 3a. P177: 4) Cierre y Tendencias (PI3)
    p177 = doc.paragraphs[177]
    assert "comprobantes con geometría fija" in p177.text, f"P177 mismatch: {p177.text[:50]}"
    old_end_3a = "comprobantes con geometría fija."
    new_end_3a = "comprobantes con geometría fija [4], [6], [28], [54], [112]."
    assert old_end_3a in p177.text, f"Old end 3a not found in P177: {p177.text[-50:]}"
    full_text_3a = p177.text.replace(old_end_3a, new_end_3a)
    prefix_3a = "4) Cierre y Tendencias: "
    body_3a = full_text_3a.replace(prefix_3a, "")
    set_p_runs(p177, prefix_3a, body_3a)
    print("  [3] III-H (4) Cierre actualizado con [4], [6], [28], [54], [112].")

    # 4. Sección III-I (PI4)
    # 4a. P185: 2.1. Balances, Tablas y Reportes Financieros Complejos
    p185 = doc.paragraphs[185]
    assert "2.1. Balances, Tablas y Reportes Financieros" in p185.text, f"P185 mismatch: {p185.text[:50]}"
    t_185 = p185.text.strip()
    old_end_4a = "89,8 % en reconstrucción matricial."
    new_end_4a = "89,8 % en reconstrucción matricial [5], [11], [41], [61], [66], [105]."
    assert old_end_4a in t_185, f"Old end 4a not found in P185: {t_185[-50:]}"
    full_text_4a = t_185.replace(old_end_4a, new_end_4a)
    prefix_4a = "2.1. Balances, Tablas y Reportes Financieros Complejos: "
    body_4a = full_text_4a.replace(prefix_4a, "")
    set_p_runs(p185, prefix_4a, body_4a)
    print("  [4a] III-I (2.1) actualizado con [5], [11], [41], [61], [66], [105].")

    # 4b. P187: 2.3. Formularios, Pólizas y Expedientes Administrativos
    p187 = doc.paragraphs[187]
    assert "2.3. Formularios, Pólizas y Expedientes" in p187.text, f"P187 mismatch: {p187.text[:50]}"
    t_187 = p187.text.strip()
    old_end_4b = "entre el 80,5 % y el 91,0 %."
    new_end_4b = "entre el 80,5 % y el 91,0 % [14], [21], [56], [58], [67], [70], [114]."
    assert old_end_4b in t_187, f"Old end 4b not found in P187: {t_187[-50:]}"
    full_text_4b = t_187.replace(old_end_4b, new_end_4b)
    prefix_4b = "2.3. Formularios, Pólizas y Expedientes Administrativos: "
    body_4b = full_text_4b.replace(prefix_4b, "")
    set_p_runs(p187, prefix_4b, body_4b)
    print("  [4b] III-I (2.3) actualizado con [14], [21], [56], [58], [67], [70], [114].")

    # 4c. P193: 4) Cierre y Tendencias (PI4)
    p193 = doc.paragraphs[193]
    assert "sistemas ERP corporativos" in p193.text, f"P193 mismatch: {p193.text[:50]}"
    t_193 = p193.text.strip()
    old_end_4c = "sistemas ERP corporativos."
    new_end_4c = "sistemas ERP corporativos [28], [44], [64], [127], [133]."
    assert old_end_4c in t_193, f"Old end 4c not found in P193: {t_193[-50:]}"
    full_text_4c = t_193.replace(old_end_4c, new_end_4c)
    prefix_4c = "4) Cierre y Tendencias: "
    body_4c = full_text_4c.replace(prefix_4c, "")
    set_p_runs(p193, prefix_4c, body_4c)
    print("  [4c] III-I (4) Cierre actualizado con [28], [44], [64], [127], [133].")

    doc.save(file_path)
    print(f"Guardado exitoso de {file_path}")

def update_resultados_docx(file_path):
    print(f"\n--- Modificando {file_path} ---")
    doc = docx.Document(file_path)

    def set_p_runs(p, prefix, body, font_size=10.0):
        for r in p._element.xpath('./w:r'):
            p._element.remove(r)
        if prefix:
            r_pre = p.add_run(prefix)
            r_pre.font.name = "Times New Roman"
            r_pre.font.size = Pt(font_size)
            r_pre.bold = True
        r_bod = p.add_run(body)
        r_bod.font.name = "Times New Roman"
        r_bod.font.size = Pt(font_size)
        r_bod.bold = False

    # Find paragraphs by unique phrases
    for p in doc.paragraphs:
        t = p.text.strip()
        # 1a. III-F 2.1
        if "alta interpretabilidad modular." in t:
            full_text = t.replace("alta interpretabilidad modular.", "alta interpretabilidad modular [12], [44], [55], [71].")
            prefix = "2.1. Canalizaciones Híbridas (Pipelines) CNN-RNN y Segmentación Clásica con OCR: "
            set_p_runs(p, prefix, full_text.replace(prefix, ""))
            print("  [1a] III-F 2.1 actualizado en doc_res.")
        # 1b. III-F 2.3
        elif "frente a transformadores masivos." in t:
            full_text = t.replace("frente a transformadores masivos.", "frente a transformadores masivos [8], [29], [34], [40], [75].")
            prefix = "2.3. Redes Neuronales de Grafos y Modelado Espacial-Relacional (GNN): "
            set_p_runs(p, prefix, full_text.replace(prefix, ""))
            print("  [1b] III-F 2.3 actualizado en doc_res.")
        # 1c. III-F 4 Cierre
        elif "verificadores basados en reglas." in t:
            full_text = t.replace("verificadores basados en reglas.", "verificadores basados en reglas [6], [7], [82], [115].")
            prefix = "4) Cierre y Tendencias: "
            set_p_runs(p, prefix, full_text.replace(prefix, ""))
            print("  [1c] III-F 4 actualizado en doc_res.")
        # 2a. III-G 2.1
        elif "2.1. Recibos y Facturas Comerciales (Benchmarks SROIE y CORD):" in t:
            prefix = "2.1. Recibos y Facturas Comerciales (Benchmarks SROIE y CORD): "
            body = (
                "Esta categoría evalúa la extracción automatizada de campos clave fijos (razón social, fecha de emisión, "
                "dirección y monto total) sobre comprobantes comerciales estándar (Tabla XVIII). La regularidad topológica "
                "y la presencia recurrente de encabezados permiten a las arquitecturas alcanzar la mediana de F1-score más alta "
                "del corpus (95,2 % global, con mediana de 95,2 % [86,4 % – 98,7 %] en SROIE y 94,1 % [88,0 % – 97,4 %] en CORD; "
                "Tabla XVIII, Fig. 7) y latencias de inferencia reducidas (80 ms a 450 ms) [4], [6], [7], [9], [30], [74]."
            )
            set_p_runs(p, prefix, body)
            print("  [2a] III-G 2.1 actualizado en doc_res.")
        # 2b. III-G 2.2
        elif "(Tabla XVIII, Fig. 7)." in t and "2.2. Tablas Financieras" in t:
            full_text = t.replace("(Tabla XVIII, Fig. 7).", "(Tabla XVIII, Fig. 7) [5], [8], [11], [35], [41], [66].")
            prefix = "2.2. Tablas Financieras y Estructuras Matriciales (Benchmarks FinTabNet y WTW): "
            set_p_runs(p, prefix, full_text.replace(prefix, ""))
            print("  [2b] III-G 2.2 actualizado en doc_res.")
        # 2c. III-G 2.3
        elif "frente a comprobantes estandarizados." in t:
            full_text = t.replace("frente a comprobantes estandarizados.", "frente a comprobantes estandarizados [14], [18], [21], [26], [42], [77], [92].")
            prefix = "2.3. Formularios Semiestructurados Ruidosos (Benchmark FUNSD): "
            set_p_runs(p, prefix, full_text.replace(prefix, ""))
            print("  [2c] III-G 2.3 actualizado en doc_res.")
        # 2d. III-G 4 Cierre
        elif "esquemas de preprocesamiento más robustos." in t:
            full_text = t.replace("esquemas de preprocesamiento más robustos.", "esquemas de preprocesamiento más robustos [14], [30], [70], [85].")
            prefix = "4) Cierre y Tendencias: "
            set_p_runs(p, prefix, full_text.replace(prefix, ""))
            print("  [2d] III-G 4 actualizado en doc_res.")
        # 3. III-H 4 Cierre
        elif "comprobantes con geometría fija." in t:
            full_text = t.replace("comprobantes con geometría fija.", "comprobantes con geometría fija [4], [6], [28], [54], [112].")
            prefix = "4) Cierre y Tendencias: "
            set_p_runs(p, prefix, full_text.replace(prefix, ""))
            print("  [3] III-H 4 actualizado en doc_res.")
        # 4a. III-I 2.1
        elif "89,8 % en reconstrucción matricial." in t:
            full_text = t.replace("89,8 % en reconstrucción matricial.", "89,8 % en reconstrucción matricial [5], [11], [41], [61], [66], [105].")
            prefix = "2.1. Balances, Tablas y Reportes Financieros Complejos: "
            set_p_runs(p, prefix, full_text.replace(prefix, ""))
            print("  [4a] III-I 2.1 actualizado en doc_res.")
        # 4b. III-I 2.3
        elif "entre el 80,5 % y el 91,0 %." in t:
            full_text = t.replace("entre el 80,5 % y el 91,0 %.", "entre el 80,5 % y el 91,0 % [14], [21], [56], [58], [67], [70], [114].")
            prefix = "2.3. Formularios, Pólizas y Expedientes Administrativos: "
            set_p_runs(p, prefix, full_text.replace(prefix, ""))
            print("  [4b] III-I 2.3 actualizado en doc_res.")
        # 4c. III-I 4 Cierre
        elif "sistemas ERP corporativos." in t:
            full_text = t.replace("sistemas ERP corporativos.", "sistemas ERP corporativos [28], [44], [64], [127], [133].")
            prefix = "4) Cierre y Tendencias: "
            set_p_runs(p, prefix, full_text.replace(prefix, ""))
            print("  [4c] III-I 4 actualizado en doc_res.")

    doc.save(file_path)
    print(f"Guardado exitoso de {file_path}")

def update_main_md(file_path):
    print(f"\n--- Modificando {file_path} ---")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    replacements = [
        # 1a
        ("alta interpretabilidad modular.", "alta interpretabilidad modular [12], [44], [55], [71]."),
        # 1b
        ("frente a transformadores masivos.", "frente a transformadores masivos [8], [29], [34], [40], [75]."),
        # 1c
        ("verificadores basados en reglas.", "verificadores basados en reglas [6], [7], [82], [115]."),
        # 2b
        ("(Tabla XVIII, Fig. 7).", "(Tabla XVIII, Fig. 7) [5], [8], [11], [35], [41], [66]."),
        # 2c
        ("frente a comprobantes estandarizados.", "frente a comprobantes estandarizados [14], [18], [21], [26], [42], [77], [92]."),
        # 3
        ("comprobantes con geometría fija.", "comprobantes con geometría fija [4], [6], [28], [54], [112]."),
        # 4a
        ("89,8 % en reconstrucción matricial.", "89,8 % en reconstrucción matricial [5], [11], [41], [61], [66], [105]."),
        # 4b
        ("entre el 80,5 % y el 91,0 %.", "entre el 80,5 % y el 91,0 % [14], [21], [56], [58], [67], [70], [114]."),
        # 4c
        ("sistemas ERP corporativos.", "sistemas ERP corporativos [28], [44], [64], [127], [133].")
    ]

    for old, new in replacements:
        if old in content:
            content = content.replace(old, new, 1)
            print(f"  Reemplazado en main.md: {new[:40]}...")
        else:
            print(f"  WARNING: No encontrado en main.md: {old}")

    # 2a in main.md: Replace paragraph starting with "2.1. Recibos y Facturas Comerciales"
    p2a_old_pattern = r"(\*\*?2\.1\.\s+Recibos y Facturas Comerciales.*?\n)(.*?80\s+ms\s+a\s+450\s+ms\.\)?)"
    new_2a_text = (
        "2.1. Recibos y Facturas Comerciales (Benchmarks SROIE y CORD): Esta categoría evalúa la extracción "
        "automatizada de campos clave fijos (razón social, fecha de emisión, dirección y monto total) sobre "
        "comprobantes comerciales estándar (Tabla XVIII). La regularidad topológica y la presencia recurrente de "
        "encabezados permiten a las arquitecturas alcanzar la mediana de F1-score más alta del corpus (95,2 % global, "
        "con mediana de 95,2 % [86,4 % – 98,7 %] en SROIE y 94,1 % [88,0 % – 97,4 %] en CORD; Tabla XVIII, Fig. 7) "
        "y latencias de inferencia reducidas (80 ms a 450 ms) [4], [6], [7], [9], [30], [74]."
    )
    if "Recibos y Facturas Comerciales (Benchmarks SROIE y CORD)" in content:
        # locate start and end of that section paragraph
        pos_s = content.find("Recibos y Facturas Comerciales (Benchmarks SROIE y CORD)")
        # backtrack to start of line
        line_start = content.rfind("\n", 0, pos_s) + 1
        # find end of paragraph (double newline)
        p_end = content.find("\n\n", pos_s)
        content = content[:line_start] + new_2a_text + content[p_end:]
        print("  [2a] Reemplazado párrafo 2.1 en main.md.")

    # 2d in main.md: Cierre y Tendencias (PI2)
    pos_pi2 = content.find("## 4. Rendimiento Cuantitativo")
    if pos_pi2 != -1:
        pos_cierre_pi2 = content.find("Cierre y Tendencias", pos_pi2)
        pos_next_sec = content.find("## 5. Comparativa", pos_cierre_pi2)
        cierre_pi2_sub = content[pos_cierre_pi2:pos_next_sec]
        old_cierre_end = "más robustos."
        new_cierre_end = "más robustos [14], [30], [70], [85]."
        if old_cierre_end in cierre_pi2_sub:
            cierre_pi2_sub = cierre_pi2_sub.replace(old_cierre_end, new_cierre_end, 1)
            content = content[:pos_cierre_pi2] + cierre_pi2_sub + content[pos_next_sec:]
            print("  [2d] Cierre PI2 actualizado en main.md.")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Guardado exitoso de {file_path}")

if __name__ == '__main__':
    update_rupay_docx('project/shared/RSL_Sergio_Rupay.docx')
    update_resultados_docx('project/resultados/Articulo_RSL_Resultados_Completo_IEEE.docx')
    update_main_md('project/resultados/main.md')

