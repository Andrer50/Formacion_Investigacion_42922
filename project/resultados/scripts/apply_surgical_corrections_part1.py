import docx
from docx.shared import Pt
import re

def update_rupay_docx(file_path):
    print(f"\n--- Modificando {file_path} ---")
    doc = docx.Document(file_path)

    # 1. Sección III-A: Apertura General
    # Target: paragraph 82
    p82 = doc.paragraphs[82]
    assert "La presente sección reporta la evidencia empírica cuantitativa" in p82.text, f"P82 mismatch: {p82.text[:50]}"
    new_text_1 = (
        "La presente sección reporta la evidencia empírica cuantitativa y sistemática extraída del corpus cerrado "
        "de 131 artículos primarios indexados ([3]–[133]), evaluados conforme a las directrices de [1] y los estándares "
        "de [2] (Fig. 1). Los resultados se organizan secuencialmente en cuatro bloques analíticos: (i) la caracterización "
        "bibliométrica y metodológica del corpus (PD1 a PD3 en las Secciones III-B a III-D); (ii) la evaluación de calidad "
        "metodológica (Sección III-E); (iii) la síntesis cuantitativa y temática para las cuatro preguntas de investigación "
        "(PI1 a PI4 en las Secciones III-F a III-I); y (iv) el análisis de sensibilidad global y la calificación de certeza "
        "GRADE-CERQual (Secciones III-J y III-K), siguiendo los criterios definidos en la Sección II-L y la Tabla XI. "
        "Conforme a los estándares de verificabilidad y tratamiento de datos ausentes, no se imputaron valores: PD1–PD3 "
        "y PI4 analizan el universo íntegro (N = 131; 100,0 %), mientras que PI1 (n = 105; 80,2 %), PI2 (n = 117; 89,3 %) "
        "y PI3 (n = 82; 62,6 %) evalúan estrictamente los subconjuntos que reportan arquitecturas reproducibles, pruebas "
        "en benchmarks formales y comparadores explícitos, respectivamente."
    )
    for r in p82._element.xpath('./w:r'):
        p82._element.remove(r)
    r1 = p82.add_run(new_text_1)
    r1.font.name = "Times New Roman"
    r1.font.size = Pt(9.5)
    r1.bold = False
    print("  [1] Sección III-A actualizada.")

    # 2. Sección III-B: 2a y 2c
    # Target: paragraph 91 (2a)
    p91 = doc.paragraphs[91]
    assert "Fase de emergencia y cimientos basados en OCR-CNN" in p91.text, f"P91 mismatch: {p91.text[:50]}"
    prefix_2a = "a) Fase de emergencia y cimientos basados en OCR-CNN (2020–2021): "
    body_2a = (
        "Ciclo inicial caracterizado por propuestas orientadas a mejorar la binarización de escaneos, OCR neuronal con LSTM "
        "y segmentación clásica con Mask R-CNN. Registró un volumen de producción moderado en relación con etapas posteriores (Tabla XIII) "
        "[59], [60], [62]–[64], [111]."
    )
    for r in p91._element.xpath('./w:r'):
        p91._element.remove(r)
    r_pref = p91.add_run(prefix_2a)
    r_pref.font.name = "Times New Roman"
    r_pref.font.size = Pt(9.5)
    r_pref.bold = True
    r_body = p91.add_run(body_2a)
    r_body.font.name = "Times New Roman"
    r_body.font.size = Pt(9.5)
    r_body.bold = False
    print("  [2a] Sección III-B (2a) actualizada con citas [59], [60], [62]–[64], [111].")

    # Target: paragraph 93 (2c)
    p93 = doc.paragraphs[93]
    assert "Fase de aceleración con VLMs y Modelos Generativos" in p93.text, f"P93 mismatch: {p93.text[:50]}"
    prefix_2c = "c) Fase de aceleración con VLMs y Modelos Generativos (2025–2026*): "
    body_2c = (
        "Constituye la etapa más prolífica del corpus, concentrando el volumen cúspide de publicaciones (Tabla XIII). "
        "El factor determinante de esta aceleración fue la incorporación de Vision-Language Models (VLMs), Transformers "
        "generativos con mecanismos de atención visual desacoplada y modelos de lenguaje de gran escala (LLMs) adaptados con "
        "prompt engineering y few-shot learning [3], [4], [6], [7], [19], [32], [82]."
    )
    for r in p93._element.xpath('./w:r'):
        p93._element.remove(r)
    r_pref = p93.add_run(prefix_2c)
    r_pref.font.name = "Times New Roman"
    r_pref.font.size = Pt(9.5)
    r_pref.bold = True
    r_body = p93.add_run(body_2c)
    r_body.font.name = "Times New Roman"
    r_body.font.size = Pt(9.5)
    r_body.bold = False
    print("  [2c] Sección III-B (2c) actualizada con citas [3], [4], [6], [7], [19], [32], [82].")

    # 3. Sección III-B: 3) Contrastes y Debates Temporales
    # Target: paragraph 94
    p94 = doc.paragraphs[94]
    assert "3) Contrastes y Debates Temporales:" in p94.text, f"P94 mismatch: {p94.text[:50]}"
    prefix_3 = "3) Contrastes y Debates Temporales: "
    body_3 = (
        "Mientras que entre 2020 y 2023 el volumen anual creció de forma continua desde 4 hasta 27 estudios (Tabla XIII), "
        "en 2024 se registró un volumen de 16 artículos (12,2 %) enfocados en arquitecturas de grafos y alineación multimodal "
        "[29], [30], [34], [36], [38], previo al ascenso a 53 estudios (40,5 %) en el bienio 2025–2026 impulsado por la publicación "
        "de modelos fundacionales de visión-lenguaje (VLMs) y esquemas zero-shot [3], [4], [6], [22], [32]."
    )
    for r in p94._element.xpath('./w:r'):
        p94._element.remove(r)
    r_pref = p94.add_run(prefix_3)
    r_pref.font.name = "Times New Roman"
    r_pref.font.size = Pt(9.5)
    r_pref.bold = True
    r_body = p94.add_run(body_3)
    r_body.font.name = "Times New Roman"
    r_body.font.size = Pt(9.5)
    r_body.bold = False
    print("  [3] Sección III-B (3) reemplazada completamente (eliminada conjetura y añadidas citas).")

    # 4. Sección III-C: Tabla XIV (España) y Cierre
    # 4a. Tabla XIV (Table 13), Row 10 (España)
    t13 = doc.tables[13]
    row_spain = None
    for r in t13.rows:
        if r.cells[0].text.strip() == "España":
            row_spain = r
            break
    assert row_spain is not None, "No se encontró la fila 'España' en Tabla XIV"
    cell_spain = row_spain.cells[3]
    new_spain_text = (
        "Sin autores con ≥ 3 publicaciones (producción dispersa, ≤ 2 estudios c/u: "
        "Fornés A. (2; [105], [111]), Lladós J. (1; [105]), Sainz-De-Abajo B. (1; [131]))."
    )
    for p in cell_spain.paragraphs:
        for r in p._element.xpath('./w:r'):
            p._element.remove(r)
    r_sp = cell_spain.paragraphs[0].add_run(new_spain_text)
    r_sp.font.name = "Times New Roman"
    r_sp.font.size = Pt(7.5)
    r_sp.bold = False
    print("  [4a] Tabla XIV fila España corregida: Lladós J. (1; [105]), Sainz-De-Abajo B. (1; [131]).")

    # 4b. Cierre y Tendencias (paragraph 108)
    p108 = doc.paragraphs[108]
    assert "4) Cierre y Tendencias: En el plano geográfico regional" in p108.text, f"P108 mismatch: {p108.text[:50]}"
    prefix_4b = "4) Cierre y Tendencias: "
    body_4b = (
        "En el plano geográfico regional, la representación de América Latina en el corpus primario se circunscribe al estudio brasileño "
        "[14] (Gonçalves Lima y Alves Pereira, Universidade Federal de Lavras), el cual introdujo el benchmark UFLA-FORMS para extracción "
        "de entidades en formularios semiestructurados en portugués, sumado a las contribuciones ibéricas en detección tabular y procesamiento "
        "de recibos ([105], [111], [131])."
    )
    for r in p108._element.xpath('./w:r'):
        p108._element.remove(r)
    r_pref = p108.add_run(prefix_4b)
    r_pref.font.name = "Times New Roman"
    r_pref.font.size = Pt(9.5)
    r_pref.bold = True
    r_body = p108.add_run(body_4b)
    r_body.font.name = "Times New Roman"
    r_body.font.size = Pt(9.5)
    r_body.bold = False
    print("  [4b] Sección III-C (4) Cierre recortado exactamente en ([105], [111], [131]).")

    # 5. Sección III-D: 2a, 2b, 2c
    # 5a. paragraph 117 (2a)
    p117 = doc.paragraphs[117]
    assert "a) Predominio del diseño experimental controlado:" in p117.text, f"P117 mismatch: {p117.text[:50]}"
    prefix_5a = "a) Predominio del diseño experimental controlado: "
    body_5a = (
        "La mayor parte del corpus adoptó un diseño experimental formal con modelos baselines bajo condiciones reproducibles de laboratorio "
        "(Tabla XV), apoyándose fundamentalmente en benchmarks públicos abiertos (SROIE, FUNSD, CORD, DocBank). Cabe precisar que la concurrencia "
        "numérica de 82 estudios experimentales y 82 estudios bajo síntesis SWiM en PI3 responde a constructos metodológicos independientes: "
        "62 estudios comparten ambas condiciones (experimentos con comparador frente a métodos tradicionales), mientras que 20 experimentos "
        "controlados contrastaron únicamente modelos neuronales entre sí sin comparador tradicional, y 20 estudios de PI3 provinieron de "
        "desarrollos de artefactos o casos de estudio [3]–[5], [7]–[13], [34], [41]."
    )
    for r in p117._element.xpath('./w:r'):
        p117._element.remove(r)
    r_pref = p117.add_run(prefix_5a)
    r_pref.font.name = "Times New Roman"
    r_pref.font.size = Pt(9.5)
    r_pref.bold = True
    r_body = p117.add_run(body_5a)
    r_body.font.name = "Times New Roman"
    r_body.font.size = Pt(9.5)
    r_body.bold = False
    print("  [5a] Sección III-D (2a) actualizada con citas [3]–[5], [7]–[13], [34], [41].")

    # 5b. paragraph 118 (2b)
    p118 = doc.paragraphs[118]
    assert "b) Desarrollo de artefactos y pruebas de concepto (PoC):" in p118.text, f"P118 mismatch: {p118.text[:50]}"
    prefix_5b = "b) Desarrollo de artefactos y pruebas de concepto (PoC): "
    body_5b = (
        "Constituye la segunda modalidad metodológica predominante (Tabla XV), enfocada en diseñar prototipos o arquitecturas especializadas "
        "validadas de forma acotada, donde una fracción se apoyó en datos privados propietarios sin someter el artefacto a estrés transaccional "
        "continuo [54], [58], [59], [95], [125], [129]."
    )
    for r in p118._element.xpath('./w:r'):
        p118._element.remove(r)
    r_pref = p118.add_run(prefix_5b)
    r_pref.font.name = "Times New Roman"
    r_pref.font.size = Pt(9.5)
    r_pref.bold = True
    r_body = p118.add_run(body_5b)
    r_body.font.name = "Times New Roman"
    r_body.font.size = Pt(9.5)
    r_body.bold = False
    print("  [5b] Sección III-D (2b) actualizada con citas [54], [58], [59], [95], [125], [129].")

    # 5c. paragraph 119 (2c)
    p119 = doc.paragraphs[119]
    assert "c) Validación en conjuntos de datos corporativos y mixtos:" in p119.text, f"P119 mismatch: {p119.text[:50]}"
    prefix_5c = "c) Validación en conjuntos de datos corporativos y mixtos: "
    body_5c = (
        "Cerca de la mitad de las investigaciones recurrió a datos privados de empresas o esquemas híbridos que combinan preentrenamiento "
        "en bancos abiertos con ajuste fino y validación final sobre documentos reales de organizaciones (Tabla XV) "
        "[6], [14], [28], [32], [44], [64], [112]."
    )
    for r in p119._element.xpath('./w:r'):
        p119._element.remove(r)
    r_pref = p119.add_run(prefix_5c)
    r_pref.font.name = "Times New Roman"
    r_pref.font.size = Pt(9.5)
    r_pref.bold = True
    r_body = p119.add_run(body_5c)
    r_body.font.name = "Times New Roman"
    r_body.font.size = Pt(9.5)
    r_body.bold = False
    print("  [5c] Sección III-D (2c) actualizada con citas [6], [14], [28], [32], [44], [64], [112].")

    doc.save(file_path)
    print(f"Guardado exitoso de {file_path}")

def update_resultados_docx(file_path):
    print(f"\n--- Modificando {file_path} ---")
    doc = docx.Document(file_path)

    # 1. Sección III-A: P4
    p4 = doc.paragraphs[4]
    assert "La presente sección reporta la evidencia empírica cuantitativa" in p4.text
    new_text_1 = (
        "La presente sección reporta la evidencia empírica cuantitativa y sistemática extraída del corpus cerrado "
        "de 131 artículos primarios indexados ([3]–[133]), evaluados conforme a las directrices de [1] y los estándares "
        "de [2] (Fig. 1). Los resultados se organizan secuencialmente en cuatro bloques analíticos: (i) la caracterización "
        "bibliométrica y metodológica del corpus (PD1 a PD3 en las Secciones III-B a III-D); (ii) la evaluación de calidad "
        "metodológica (Sección III-E); (iii) la síntesis cuantitativa y temática para las cuatro preguntas de investigación "
        "(PI1 a PI4 en las Secciones III-F a III-I); y (iv) el análisis de sensibilidad global y la calificación de certeza "
        "GRADE-CERQual (Secciones III-J y III-K), siguiendo los criterios definidos en la Sección II-L y la Tabla XI. "
        "Conforme a los estándares de verificabilidad y tratamiento de datos ausentes, no se imputaron valores: PD1–PD3 "
        "y PI4 analizan el universo íntegro (N = 131; 100,0 %), mientras que PI1 (n = 105; 80,2 %), PI2 (n = 117; 89,3 %) "
        "y PI3 (n = 82; 62,6 %) evalúan estrictamente los subconjuntos que reportan arquitecturas reproducibles, pruebas "
        "en benchmarks formales y comparadores explícitos, respectivamente."
    )
    for r in p4._element.xpath('./w:r'):
        p4._element.remove(r)
    r1 = p4.add_run(new_text_1)
    r1.font.name = "Times New Roman"
    r1.font.size = Pt(10)
    print("  [1] Sección III-A actualizada en doc_res.")

    # 2. Sección III-B: P13 (2a) y P15 (2c)
    p13 = doc.paragraphs[13]
    prefix_2a = "a) Fase de emergencia y cimientos basados en OCR-CNN (2020–2021): "
    body_2a = (
        "Ciclo inicial caracterizado por propuestas orientadas a mejorar la binarización de escaneos, OCR neuronal con LSTM "
        "y segmentación clásica con Mask R-CNN. Registró un volumen de producción moderado en relación con etapas posteriores (Tabla XIII) "
        "[59], [60], [62]–[64], [111]."
    )
    for r in p13._element.xpath('./w:r'):
        p13._element.remove(r)
    r_pref = p13.add_run(prefix_2a)
    r_pref.font.name = "Times New Roman"
    r_pref.font.size = Pt(10)
    r_pref.bold = True
    r_body = p13.add_run(body_2a)
    r_body.font.name = "Times New Roman"
    r_body.font.size = Pt(10)
    print("  [2a] P13 actualizado en doc_res.")

    p15 = doc.paragraphs[15]
    prefix_2c = "c) Fase de aceleración con VLMs y Modelos Generativos (2025–2026*): "
    body_2c = (
        "Constituye la etapa más prolífica del corpus, concentrando el volumen cúspide de publicaciones (Tabla XIII). "
        "El factor determinante de esta aceleración fue la incorporación de Vision-Language Models (VLMs), Transformers "
        "generativos con mecanismos de atención visual desacoplada y modelos de lenguaje de gran escala (LLMs) adaptados con "
        "prompt engineering y few-shot learning [3], [4], [6], [7], [19], [32], [82]."
    )
    for r in p15._element.xpath('./w:r'):
        p15._element.remove(r)
    r_pref = p15.add_run(prefix_2c)
    r_pref.font.name = "Times New Roman"
    r_pref.font.size = Pt(10)
    r_pref.bold = True
    r_body = p15.add_run(body_2c)
    r_body.font.name = "Times New Roman"
    r_body.font.size = Pt(10)
    print("  [2c] P15 actualizado en doc_res.")

    # 3. Sección III-B: P16 (3)
    p16 = doc.paragraphs[16]
    prefix_3 = "3) Contrastes y Debates Temporales: "
    body_3 = (
        "Mientras que entre 2020 y 2023 el volumen anual creció de forma continua desde 4 hasta 27 estudios (Tabla XIII), "
        "en 2024 se registró un volumen de 16 artículos (12,2 %) enfocados en arquitecturas de grafos y alineación multimodal "
        "[29], [30], [34], [36], [38], previo al ascenso a 53 estudios (40,5 %) en el bienio 2025–2026 impulsado por la publicación "
        "de modelos fundacionales de visión-lenguaje (VLMs) y esquemas zero-shot [3], [4], [6], [22], [32]."
    )
    for r in p16._element.xpath('./w:r'):
        p16._element.remove(r)
    r_pref = p16.add_run(prefix_3)
    r_pref.font.name = "Times New Roman"
    r_pref.font.size = Pt(10)
    r_pref.bold = True
    r_body = p16.add_run(body_3)
    r_body.font.name = "Times New Roman"
    r_body.font.size = Pt(10)
    print("  [3] P16 actualizado en doc_res.")

    # 4. Sección III-C: Tabla 1 Row 10 (España) y P30 (4)
    t1 = doc.tables[1]
    row_spain = None
    for r in t1.rows:
        if r.cells[0].text.strip() == "España":
            row_spain = r
            break
    assert row_spain is not None
    new_spain_text = (
        "Sin autores con ≥ 3 publicaciones (producción dispersa, ≤ 2 estudios c/u: "
        "Fornés A. (2; [105], [111]), Lladós J. (1; [105]), Sainz-De-Abajo B. (1; [131]))."
    )
    for p in row_spain.cells[3].paragraphs:
        for r in p._element.xpath('./w:r'):
            p._element.remove(r)
    r_sp = row_spain.cells[3].paragraphs[0].add_run(new_spain_text)
    r_sp.font.name = "Times New Roman"
    r_sp.font.size = Pt(8.0)
    print("  [4a] Tabla 1 España actualizada en doc_res.")

    p30 = doc.paragraphs[30]
    prefix_4b = "4) Cierre y Tendencias: "
    body_4b = (
        "En el plano geográfico regional, la representación de América Latina en el corpus primario se circunscribe al estudio brasileño "
        "[14] (Gonçalves Lima y Alves Pereira, Universidade Federal de Lavras), el cual introdujo el benchmark UFLA-FORMS para extracción "
        "de entidades en formularios semiestructurados en portugués, sumado a las contribuciones ibéricas en detección tabular y procesamiento "
        "de recibos ([105], [111], [131])."
    )
    for r in p30._element.xpath('./w:r'):
        p30._element.remove(r)
    r_pref = p30.add_run(prefix_4b)
    r_pref.font.name = "Times New Roman"
    r_pref.font.size = Pt(10)
    r_pref.bold = True
    r_body = p30.add_run(body_4b)
    r_body.font.name = "Times New Roman"
    r_body.font.size = Pt(10)
    print("  [4b] P30 actualizado en doc_res.")

    # 5. Sección III-D: P38
    p38 = doc.paragraphs[38]
    # In doc_res, P38 contains 2), a), b), c) joined by \n
    new_p38_text = (
        "2) Desarrollo por Categoría y Cruce Matricial: La matriz cruzada evidencia tres núcleos metodológicos de trabajo (Tabla XV, Fig. 4):\n"
        "a) Predominio del diseño experimental controlado: La mayor parte del corpus adoptó un diseño experimental formal con modelos baselines bajo condiciones reproducibles de laboratorio (Tabla XV), apoyándose fundamentalmente en benchmarks públicos abiertos (SROIE, FUNSD, CORD, DocBank). Cabe precisar que la concurrencia numérica de 82 estudios experimentales y 82 estudios bajo síntesis SWiM en PI3 responde a constructos metodológicos independientes: 62 estudios comparten ambas condiciones (experimentos con comparador frente a métodos tradicionales), mientras que 20 experimentos controlados contrastaron únicamente modelos neuronales entre sí sin comparador tradicional, y 20 estudios de PI3 provinieron de desarrollos de artefactos o casos de estudio [3]–[5], [7]–[13], [34], [41].\n"
        "b) Desarrollo de artefactos y pruebas de concepto (PoC): Constituye la segunda modalidad metodológica predominante (Tabla XV), enfocada en diseñar prototipos o arquitecturas especializadas validadas de forma acotada, donde una fracción se apoyó en datos privados propietarios sin someter el artefacto a estrés transaccional continuo [54], [58], [59], [95], [125], [129].\n"
        "c) Validación en conjuntos de datos corporativos y mixtos: Cerca de la mitad de las investigaciones recurrió a datos privados de empresas o esquemas híbridos que combinan preentrenamiento en bancos abiertos con ajuste fino y validación final sobre documentos reales de organizaciones (Tabla XV) [6], [14], [28], [32], [44], [64], [112]."
    )
    for r in p38._element.xpath('./w:r'):
        p38._element.remove(r)
    r_p38 = p38.add_run(new_p38_text)
    r_p38.font.name = "Times New Roman"
    r_p38.font.size = Pt(10)
    print("  [5] P38 actualizado en doc_res.")

    doc.save(file_path)
    print(f"Guardado exitoso de {file_path}")

def update_main_md(file_path):
    print(f"\n--- Modificando {file_path} ---")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Sección III-A: Apertura General
    old_sec_1 = (
        "La presente sección reporta la evidencia empírica cuantitativa y sistemática extraída del corpus cerrado "
        "de **131 artículos primarios indexados** ([3]–[133]), evaluados críticamente conforme a las directrices de [1] "
        "y los estándares de calidad metodológica de [2]. Los resultados se estructuran siguiendo el esquema analítico "
        "y los criterios de certeza definidos en la Sección II-L y la Tabla XI."
    )
    # Also check if it was already updated or has slightly different bolding
    new_sec_1 = (
        "La presente sección reporta la evidencia empírica cuantitativa y sistemática extraída del corpus cerrado "
        "de 131 artículos primarios indexados ([3]–[133]), evaluados conforme a las directrices de [1] y los estándares "
        "de [2] (Fig. 1). Los resultados se organizan secuencialmente en cuatro bloques analíticos: (i) la caracterización "
        "bibliométrica y metodológica del corpus (PD1 a PD3 en las Secciones III-B a III-D); (ii) la evaluación de calidad "
        "metodológica (Sección III-E); (iii) la síntesis cuantitativa y temática para las cuatro preguntas de investigación "
        "(PI1 a PI4 en las Secciones III-F a III-I); y (iv) el análisis de sensibilidad global y la calificación de certeza "
        "GRADE-CERQual (Secciones III-J y III-K), siguiendo los criterios definidos en la Sección II-L y la Tabla XI. "
        "Conforme a los estándares de verificabilidad y tratamiento de datos ausentes, no se imputaron valores: PD1–PD3 "
        "y PI4 analizan el universo íntegro (N = 131; 100,0 %), mientras que PI1 (n = 105; 80,2 %), PI2 (n = 117; 89,3 %) "
        "y PI3 (n = 82; 62,6 %) evalúan estrictamente los subconjuntos que reportan arquitecturas reproducibles, pruebas "
        "en benchmarks formales y comparadores explícitos, respectivamente."
    )
    if old_sec_1 in content:
        content = content.replace(old_sec_1, new_sec_1)
        print("  [1] Sección III-A actualizada en main.md.")
    else:
        # Search flexibly
        pattern = r"La presente sección reporta la evidencia empírica cuantitativa y sistemática extraída del corpus cerrado.*?Tabla XI\."
        match = re.search(pattern, content, re.DOTALL)
        if match:
            content = content[:match.start()] + new_sec_1 + content[match.end():]
            print("  [1] Sección III-A actualizada flexiblemente en main.md.")
        else:
            print("  [1] WARNING: No se encontró patrón para Sección III-A en main.md!")

    # 2a. Fase de emergencia (Tabla XIII) -> (Tabla XIII) [59], [60], [62]–[64], [111].
    old_2a = "etapas posteriores (Tabla XIII)."
    new_2a = "etapas posteriores (Tabla XIII) [59], [60], [62]–[64], [111]."
    if old_2a in content:
        content = content.replace(old_2a, new_2a, 1)
        print("  [2a] Fase de emergencia actualizada en main.md.")

    # 2c. few-shot learning. -> few-shot learning [3], [4], [6], [7], [19], [32], [82].
    old_2c = "prompt engineering y few-shot learning."
    new_2c = "prompt engineering y few-shot learning [3], [4], [6], [7], [19], [32], [82]."
    if old_2c in content:
        content = content.replace(old_2c, new_2c, 1)
        print("  [2c] Fase de aceleración actualizada en main.md.")

    # 3. Contrastes y Debates Temporales
    old_3_start = content.find("#### Bloque 3 — Contrastes y Debates Temporales")
    if old_3_start != -1:
        end_3 = content.find("#### Bloque 4", old_3_start)
        new_3 = (
            "#### Bloque 3 — Contrastes y Debates Temporales\n"
            "3) Contrastes y Debates Temporales: Mientras que entre 2020 y 2023 el volumen anual creció de forma continua "
            "desde 4 hasta 27 estudios (Tabla XIII), en 2024 se registró un volumen de 16 artículos (12,2 %) enfocados en "
            "arquitecturas de grafos y alineación multimodal [29], [30], [34], [36], [38], previo al ascenso a 53 estudios "
            "(40,5 %) en el bienio 2025–2026 impulsado por la publicación de modelos fundacionales de visión-lenguaje (VLMs) "
            "y esquemas zero-shot [3], [4], [6], [22], [32].\n\n"
        )
        content = content[:old_3_start] + new_3 + content[end_3:]
        print("  [3] Bloque 3 de PD1 reemplazado en main.md.")

    # 4a. Tabla XIV España: Fornés A. (2; [105], [111]), Lladós J. (1; [105]), Sainz-De-Abajo B. (1; [131])
    old_spain_md = "Fornés A. (2; [105], [111]), Lladós J. (2; [105], [116])"
    new_spain_md = "Fornés A. (2; [105], [111]), Lladós J. (1; [105]), Sainz-De-Abajo B. (1; [131])"
    if old_spain_md in content:
        content = content.replace(old_spain_md, new_spain_md)
        print("  [4a] Tabla XIV España actualizada en main.md.")

    # 4b. Cierre y Tendencias (eliminar oración final)
    old_cierre_part = (
        "sumado a las contribuciones ibéricas en detección tabular y procesamiento de recibos ([105], [111], [131]). "
        "Esta reducida frecuencia de publicaciones latinoamericanas en revistas Q1–Q3 no refleja necesariamente una ausencia de investigación aplicada en la región, sino las fronteras de cobertura del protocolo de búsqueda (restricción a Scopus/WoS en inglés/español y exclusión sistemática de actas de congresos regionales como CLEI o simposios locales, donde se concentra parte del desarrollo tributario corporativo)."
    )
    new_cierre_part = "sumado a las contribuciones ibéricas en detección tabular y procesamiento de recibos ([105], [111], [131])."
    if old_cierre_part in content:
        content = content.replace(old_cierre_part, new_cierre_part)
        print("  [4b] Cierre y Tendencias recortado en main.md.")

    # 5a. Predominio del diseño experimental controlado
    old_5a = "o casos de estudio."
    new_5a = "o casos de estudio [3]–[5], [7]–[13], [34], [41]."
    if old_5a in content:
        content = content.replace(old_5a, new_5a, 1)
        print("  [5a] Predominio diseño experimental actualizado en main.md.")

    # 5b. Desarrollo de artefactos y pruebas de concepto (PoC)
    old_5b = "estrés transaccional continuo."
    new_5b = "estrés transaccional continuo [54], [58], [59], [95], [125], [129]."
    if old_5b in content:
        content = content.replace(old_5b, new_5b, 1)
        print("  [5b] Desarrollo de artefactos actualizado en main.md.")

    # 5c. Validación en conjuntos de datos corporativos y mixtos
    old_5c = "organizaciones (Tabla XV)."
    new_5c = "organizaciones (Tabla XV) [6], [14], [28], [32], [44], [64], [112]."
    if old_5c in content:
        content = content.replace(old_5c, new_5c, 1)
        print("  [5c] Validación corporativa actualizada en main.md.")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Guardado exitoso de {file_path}")

if __name__ == '__main__':
    update_rupay_docx('project/shared/RSL_Sergio_Rupay.docx')
    update_resultados_docx('project/resultados/Articulo_RSL_Resultados_Completo_IEEE.docx')
    update_main_md('project/resultados/main.md')

