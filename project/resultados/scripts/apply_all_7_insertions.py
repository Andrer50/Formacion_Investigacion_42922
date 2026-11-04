import os

def update_combined():
    path = 'project/metodologia/scripts/build_combined_ieee_article.py'
    with open(path, 'r', encoding='utf-8') as f:
        t = f.read()

    # 1. Sec I-B Point 3
    idx1 = t.find('Aislamiento Transaccional con Sistemas ERP: ')
    assert idx1 != -1, "Target 1 not found"
    # Find start of add_p before idx1
    p_start = t.rfind('add_p(', 0, idx1)
    p_end = t.find(')', idx1) + 1
    new_p1 = '''add_p(
    "La mayoría de las propuestas algorítmicas limita su alcance a la extracción visual de entidades en formatos intermedios (JSON/CSV) en entornos aislados de laboratorio, careciendo de conectores transaccionales activos, validación fiscal de tres vías (Three-Way Matching) y mecanismos de control de alucinaciones contables requeridos por sistemas ERP productivos como SAP S/4HANA, Oracle Financials o Microsoft Dynamics [28], [64], [112], [127].",
    bold_prefix="3) Brecha de Integración Transaccional con Sistemas ERP/CRM: "
)'''
    t = t[:p_start] + new_p1 + t[p_end:]
    print("[OK] Item 1 applied in combined")

    # 2. Sec III-F (PI1)
    idx2 = t.find('Partición temática unívoca auditada y verificada')
    assert idx2 != -1, "Target 2 not found"
    p_start2 = t.rfind('add_table_footer(', 0, idx2)
    # Find end of 2.1
    idx2_end = t.find('2.1. Canalizaciones Híbridas (Pipelines) CNN-RNN y Segmentación Clásica con OCR: ')
    p_end2 = t.find(')', idx2_end) + 1
    new_p2 = '''add_table_footer("Fuente: elaboración propia a partir del corpus primario [3]–[133]. Síntesis temática según Thomas & Harden [134] y Cruzes & Dybå [135]. Acuerdo inter-evaluador κ = 0,88. Nota: Las listas completas de estudios por familia algorítmica se documentan en el Material Suplementario (Apéndice).")

add_figure_with_caption('project/resultados/outputs/fig6_taxonomia_algoritmos.png', 'Fig. 6',
                        'Distribución de estudios por familia algorítmica de IA en procesamiento documental (Síntesis Temática, PI1, n = 105)',
                        '')

add_p(
    "Ciento cinco estudios primarios (80,2 % del corpus; TABLA XVII, Fig. 6) especificaron arquitecturas algorítmicas reproducibles de IA para el procesamiento de documentos empresariales (PI1), estructurándose en cuatro familias tecnológicas principales.",
    bold_prefix="1) Apertura: "
)

add_p(
    "Constituye la familia predominante del corpus con el 53,3 % de las implementaciones (56 de 105 estudios; Tabla XVII). Combina redes convolucionales (ResNet, VGG, YOLO, Mask R-CNN) para la detección espacial de regiones y tablas con redes recurrentes (BiLSTM) y motores OCR para la transcripción secuencial de texto [5], [10], [11], [59], [71], [103]. Su vigencia responde a su bajo costo computacional en CPU y alta interpretabilidad modular.",
    bold_prefix="2.1. Canalizaciones Híbridas (Pipelines) CNN-RNN y Segmentación Clásica con OCR: "
)'''
    t = t[:p_start2] + new_p2 + t[p_end2:]
    print("[OK] Item 2 applied in combined")

    # 3. Sec III-G (PI2) 2.4
    idx3 = t.find('2.4. Flujos Corporativos Integrados y Lotes Documentales Heterogéneos: ')
    assert idx3 != -1, "Target 3 not found"
    p_start3 = t.rfind('add_p(', 0, idx3)
    p_end3 = t.find(')', idx3) + 1
    new_p3 = '''add_p(
    "Comprende el subconjunto de 6 estudios (5,1 % de PI2; Tabla XVIII) que evaluaron canalizaciones completas sobre lotes continuos de documentos empresariales multiformato, alcanzando una mediana de exactitud/F1 del 90,1 % (rango: 82,0 % – 94,5 %) con latencias de inferencia de 300 ms a 1 800 ms por página [32], [78], [85], [93], [110], [111].",
    bold_prefix="2.4. Flujos Corporativos Integrados y Lotes Heterogéneos: "
)'''
    t = t[:p_start3] + new_p3 + t[p_end3:]
    print("[OK] Item 3 applied in combined")

    # 4. Sec III-H (PI3) 2.1
    idx4 = t.find('2.1. Reducción del Tiempo de Procesamiento y Latencia Operativa (Mejora +1): ')
    assert idx4 != -1, "Target 4 not found"
    p_start4 = t.rfind('add_p(', 0, idx4)
    p_end4 = t.find(')', idx4) + 1
    new_p4 = '''add_p(
    "Agrupa los 71 estudios (86,6 % de la evidencia comparativa; Tabla XIX, Fig. 8) donde las arquitecturas de IA superaron contundentemente al ingreso manual y al OCR basado en reglas, logrando una reducción mediana del 82,4 % en el tiempo de procesamiento documental (rango empírico: 60,0 % a 95,0 %) y disminuyendo drásticamente la tasa de retrabajo humano ante variaciones de diseño [3]–[7], [44], [55], [103], [127].",
    bold_prefix="2.1. Aceleración Operativa y Reducción del Tiempo de Ciclo (Mejora Favorable +1): "
)'''
    t = t[:p_start4] + new_p4 + t[p_end4:]
    print("[OK] Item 4 applied in combined")

    # 5. Sec III-I (PI4)
    idx5a = t.find('I. Mapeo de Tipologías Documentales y Sistemas Corporativos ERP/CRM')
    assert idx5a != -1, "Target 5A not found"
    p_start5a = t.rfind('add_heading_2(', 0, idx5a)
    idx5a_intro = t.find('La matriz cruzada se documenta en la Tabla XX y la matriz de calor (heatmap) se expone en la Fig. 9.', idx5a)
    p_end5a = t.find(')', idx5a_intro) + 1
    new_p5a = '''add_heading_2("I. Tipologías Documentales y Validación en Sistemas ERP/CRM (PI4: ¿En qué tipologías documentales y sistemas empresariales ERP/CRM se han validado empíricamente los modelos?)")
add_p(
    "Para determinar la aplicabilidad corporativa real de los modelos (PI4), se clasificó el universo completo del corpus (N = 131) cruzando las cuatro tipologías documentales de negocio frente a su nivel de integración técnica con plataformas empresariales ERP, CRM y DMS. La distribución cuantitativa se detalla en la Tabla XX y se representa en la matriz de calor de la Fig. 9."
)'''
    t = t[:p_start5a] + new_p5a + t[p_end5a:]

    # 5B: Table footer, Fig 9, Apertura
    idx5b = t.find('De los 59 estudios tabulares, 42 (32,1 % del corpus) abordan directamente estados')
    assert idx5b != -1, "Target 5B not found"
    p_start5b = t.rfind('add_table_footer(', 0, idx5b)
    idx5b_ap = t.find('únicamente [64] y [127] satisfacen ambos requerimientos de manera concurrente.', idx5b)
    p_end5b = t.find(')', idx5b_ap) + 1
    new_p5b = '''add_table_footer("*Nota: La columna de sistema corporativo describe el mapeo funcional conceptual hacia el que se orienta cada tipología. Nivel de integración real del corpus (N = 131): 103 estudios (78,6 %) evalúan modelos en entornos aislados sin conectores empresariales; 20 estudios (15,3 %) generan salidas estructuradas intermedias (JSON/CSV/XML) listas para ingesta; y únicamente 8 estudios (6,1 %; [28], [44], [54], [62], [64], [97], [127], [133]) validan integración transaccional activa con sistemas ERP/contables productivos.")

add_figure_with_caption('project/resultados/outputs/fig9_matriz_calor_sistemas.png', 'Fig. 9',
                        'Matriz de calor (heatmap) de tipologías documentales empresariales frente al nivel de integración en sistemas ERP/CRM/DMS (PI4, N = 131)',
                        '')

add_p(
    "Ciento treinta y un estudios (100,0 % del corpus; TABLA XX, Fig. 9) se mapearon en torno a las tipologías documentales corporativas y su integración sistémica (PI4). El núcleo contable conformado por balances/tablas matriciales (45,0 %, n = 59) y facturas comerciales (26,0 %, n = 34) concentra el 71,0 % de la investigación global (58,0 % estricto al considerar únicamente las 42 tablas financieras específicas más las 34 facturas). No obstante, se evidencia una marcada asimetría entre el reconocimiento documental y el despliegue en ingeniería de software: mientras que en PD3 se identificaron 8 casos de estudio corporativos a nivel de diseño metodológico ([64], [70], [75], [84], [103], [117], [127], [131]), en PI4 solo 8 investigaciones implementaron integración técnica transaccional activa con plataformas ERP ([28], [44], [54], [62], [64], [97], [127], [133]), convergiendo ambas dimensiones exclusivamente en dos estudios ([64], [127]).",
    bold_prefix="1) Apertura: "
)'''
    t = t[:p_start5b] + new_p5b + t[p_end5b:]
    print("[OK] Item 5 applied in combined")

    # 6. Sec IV Subapartado B
    idx6 = t.find('B. Brecha de Transferencia e Integración en Sistemas ERP y CRM')
    assert idx6 != -1, "Target 6 not found"
    p_start6 = t.rfind('add_heading_2(', 0, idx6)
    idx6_end = t.find('mediante interfaces de programación de aplicaciones (API) transaccionales.', idx6)
    p_end6 = t.find(')', idx6_end) + 1
    new_p6 = '''add_heading_2("B. Brecha de Transferencia Industrial y Desconexión Transaccional con Sistemas ERP")
add_p(
    "Un segundo hallazgo estructural de esta revisión es la desconexión entre la investigación en visión computacional y la ingeniería de sistemas empresariales. Aunque el 71,0 % del corpus aborda documentos contables críticos orientados conceptualmente a módulos financieros y de cuentas por pagar (Tabla XX), el 78,6 % de los estudios (103 de 131) finaliza su flujo experimental en la predicción de etiquetas o archivos JSON locales, sin abordar la interoperabilidad transaccional. Como demostró el cruce entre el mapeo de Petersen (PD3) y el análisis de integración técnica (PI4), solo 8 estudios validaron conectores activos con sistemas ERP ([28], [44], [54], [62], [64], [97], [127], [133]) y únicamente dos investigaciones ([64], [127]) articularon simultáneamente un diseño de caso de estudio corporativo real con integración productiva en el ERP. Esto confirma que la principal barrera para la adopción industrial del IDP ya no radica en el reconocimiento óptico aislado, sino en la orquestación de reglas de negocio, conciliación tributaria de tres vías (Three-Way Matching), gobernanza de privacidad on-premise ([116], [127]) y mitigación de alucinaciones numéricas antes del asiento contable definitivo ([4], [37])."
)'''
    t = t[:p_start6] + new_p6 + t[p_end6:]
    print("[OK] Item 6 applied in combined")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(t)
    print(f"[SUCCESS] All surgical updates applied to {path}\n")

def update_docx_resultados():
    path = 'project/resultados/scripts/build_resultados_completo_docx.py'
    with open(path, 'r', encoding='utf-8') as f:
        t = f.read()

    # 2. Sec III-F (PI1)
    idx2 = t.find('Partición temática unívoca auditada y verificada')
    assert idx2 != -1, "Target 2 not found in resultados docx"
    p_start2 = t.rfind('add_table_footer(', 0, idx2)
    idx2_end = t.find('2.1. Canalizaciones Híbridas (Pipelines) CNN-RNN y Segmentación Clásica con OCR: ')
    p_end2 = t.find(')', idx2_end) + 1
    new_p2 = '''add_table_footer("Fuente: elaboración propia a partir del corpus primario [3]–[133]. Síntesis temática según Thomas & Harden [134] y Cruzes & Dybå [135]. Acuerdo inter-evaluador κ = 0,88. Nota: Las listas completas de estudios por familia algorítmica se documentan en el Material Suplementario (Apéndice).")

add_figure_with_caption('project/resultados/outputs/fig6_taxonomia_algoritmos.png', 'Fig. 6',
                        'Distribución de estudios por familia algorítmica de IA en procesamiento documental (Síntesis Temática, PI1, n = 105)',
                        '')

add_p(
    "Ciento cinco estudios primarios (80,2 % del corpus; TABLA XVII, Fig. 6) especificaron arquitecturas algorítmicas reproducibles de IA para el procesamiento de documentos empresariales (PI1), estructurándose en cuatro familias tecnológicas principales.",
    bold_prefix="1) Apertura: "
)

add_p(
    "Constituye la familia predominante del corpus con el 53,3 % de las implementaciones (56 de 105 estudios; Tabla XVII). Combina redes convolucionales (ResNet, VGG, YOLO, Mask R-CNN) para la detección espacial de regiones y tablas con redes recurrentes (BiLSTM) y motores OCR para la transcripción secuencial de texto [5], [10], [11], [59], [71], [103]. Su vigencia responde a su bajo costo computacional en CPU y alta interpretabilidad modular.",
    bold_prefix="2.1. Canalizaciones Híbridas (Pipelines) CNN-RNN y Segmentación Clásica con OCR: "
)'''
    t = t[:p_start2] + new_p2 + t[p_end2:]
    print("[OK] Item 2 applied in resultados docx")

    # 3. Sec III-G (PI2) 2.4
    idx3 = t.find('2.4. Flujos Corporativos Integrados y Lotes Documentales Heterogéneos: ')
    assert idx3 != -1, "Target 3 not found in resultados docx"
    p_start3 = t.rfind('add_p(', 0, idx3)
    p_end3 = t.find(')', idx3) + 1
    new_p3 = '''add_p(
    "Comprende el subconjunto de 6 estudios (5,1 % de PI2; Tabla XVIII) que evaluaron canalizaciones completas sobre lotes continuos de documentos empresariales multiformato, alcanzando una mediana de exactitud/F1 del 90,1 % (rango: 82,0 % – 94,5 %) con latencias de inferencia de 300 ms a 1 800 ms por página [32], [78], [85], [93], [110], [111].",
    bold_prefix="2.4. Flujos Corporativos Integrados y Lotes Heterogéneos: "
)'''
    t = t[:p_start3] + new_p3 + t[p_end3:]
    print("[OK] Item 3 applied in resultados docx")

    # 4. Sec III-H (PI3) 2.1
    idx4 = t.find('2.1. Reducción del Tiempo de Procesamiento y Latencia Operativa (Mejora +1): ')
    assert idx4 != -1, "Target 4 not found in resultados docx"
    p_start4 = t.rfind('add_p(', 0, idx4)
    p_end4 = t.find(')', idx4) + 1
    new_p4 = '''add_p(
    "Agrupa los 71 estudios (86,6 % de la evidencia comparativa; Tabla XIX, Fig. 8) donde las arquitecturas de IA superaron contundentemente al ingreso manual y al OCR basado en reglas, logrando una reducción mediana del 82,4 % en el tiempo de procesamiento documental (rango empírico: 60,0 % a 95,0 %) y disminuyendo drásticamente la tasa de retrabajo humano ante variaciones de diseño [3]–[7], [44], [55], [103], [127].",
    bold_prefix="2.1. Aceleración Operativa y Reducción del Tiempo de Ciclo (Mejora Favorable +1): "
)'''
    t = t[:p_start4] + new_p4 + t[p_end4:]
    print("[OK] Item 4 applied in resultados docx")

    # 5. Sec III-I (PI4)
    idx5a = t.find('I. Mapeo de Tipologías Documentales y Sistemas Corporativos ERP/CRM')
    assert idx5a != -1, "Target 5A not found in resultados docx"
    p_start5a = t.rfind('add_heading_2(', 0, idx5a)
    idx5a_intro = t.find('La matriz cruzada se documenta en la Tabla XX y la matriz de calor (heatmap) se expone en la Fig. 9.', idx5a)
    p_end5a = t.find(')', idx5a_intro) + 1
    new_p5a = '''add_heading_2("I. Tipologías Documentales y Validación en Sistemas ERP/CRM (PI4: ¿En qué tipologías documentales y sistemas empresariales ERP/CRM se han validado empíricamente los modelos?)")
add_p(
    "Para determinar la aplicabilidad corporativa real de los modelos (PI4), se clasificó el universo completo del corpus (N = 131) cruzando las cuatro tipologías documentales de negocio frente a su nivel de integración técnica con plataformas empresariales ERP, CRM y DMS. La distribución cuantitativa se detalla en la Tabla XX y se representa en la matriz de calor de la Fig. 9."
)'''
    t = t[:p_start5a] + new_p5a + t[p_end5a:]

    idx5b = t.find('De los 59 estudios tabulares, 42 (32,1 % del corpus) abordan directamente estados')
    assert idx5b != -1, "Target 5B not found in resultados docx"
    p_start5b = t.rfind('add_table_footer(', 0, idx5b)
    idx5b_ap = t.find('únicamente [64] y [127] satisfacen ambos requerimientos de manera concurrente.', idx5b)
    p_end5b = t.find(')', idx5b_ap) + 1
    new_p5b = '''add_table_footer("*Nota: La columna de sistema corporativo describe el mapeo funcional conceptual hacia el que se orienta cada tipología. Nivel de integración real del corpus (N = 131): 103 estudios (78,6 %) evalúan modelos en entornos aislados sin conectores empresariales; 20 estudios (15,3 %) generan salidas estructuradas intermedias (JSON/CSV/XML) listas para ingesta; y únicamente 8 estudios (6,1 %; [28], [44], [54], [62], [64], [97], [127], [133]) validan integración transaccional activa con sistemas ERP/contables productivos.")

add_figure_with_caption('project/resultados/outputs/fig9_matriz_calor_sistemas.png', 'Fig. 9',
                        'Matriz de calor (heatmap) de tipologías documentales empresariales frente al nivel de integración en sistemas ERP/CRM/DMS (PI4, N = 131)',
                        '')

add_p(
    "Ciento treinta y un estudios (100,0 % del corpus; TABLA XX, Fig. 9) se mapearon en torno a las tipologías documentales corporativas y su integración sistémica (PI4). El núcleo contable conformado por balances/tablas matriciales (45,0 %, n = 59) y facturas comerciales (26,0 %, n = 34) concentra el 71,0 % de la investigación global (58,0 % estricto al considerar únicamente las 42 tablas financieras específicas más las 34 facturas). No obstante, se evidencia una marcada asimetría entre el reconocimiento documental y el despliegue en ingeniería de software: mientras que en PD3 se identificaron 8 casos de estudio corporativos a nivel de diseño metodológico ([64], [70], [75], [84], [103], [117], [127], [131]), en PI4 solo 8 investigaciones implementaron integración técnica transaccional activa con plataformas ERP ([28], [44], [54], [62], [64], [97], [127], [133]), convergiendo ambas dimensiones exclusivamente en dos estudios ([64], [127]).",
    bold_prefix="1) Apertura: "
)'''
    t = t[:p_start5b] + new_p5b + t[p_end5b:]
    print("[OK] Item 5 applied in resultados docx")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(t)
    print(f"[SUCCESS] All surgical updates applied to {path}\n")

def update_markdown():
    path = 'project/resultados/scripts/build_full_resultados_markdown.py'
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()

    # 2. Sec III-F (PI1)
    p_tab17_end = c.find('*Fuente: elaboración propia a partir del corpus primario [3]–[133].*')
    p_transf = c.find('2. **Transformers Multimodales')
    if p_transf == -1:
        p_transf = c.find('**Transformers Multimodales')
    if p_tab17_end != -1 and p_transf != -1:
        new_md_pi1 = '''Fuente: elaboración propia a partir del corpus primario [3]–[133]. Síntesis temática según Thomas & Harden [134] y Cruzes & Dybå [135]. Acuerdo inter-evaluador κ = 0,88. Nota: Las listas completas de estudios por familia algorítmica se documentan en el Material Suplementario (Apéndice).

![Fig. 6. Distribución de estudios por familia algorítmica de IA en procesamiento documental (Síntesis Temática, PI1, n = 105)](file:///c:/Users/HP/Desktop/ESCRITORIO/PROYECTOS%20UNIVERSIDAD/Formacion_Investigacion_42922/project/resultados/outputs/fig6_taxonomia_algoritmos.png)
*Fig. 6. Distribución de estudios por familia algorítmica de IA en procesamiento documental (Síntesis Temática, PI1, n = 105).*

#### Bloque 1 — Apertura
**1) Apertura:** Ciento cinco estudios primarios (80,2 % del corpus; TABLA XVII, Fig. 6) especificaron arquitecturas algorítmicas reproducibles de IA para el procesamiento de documentos empresariales (PI1), estructurándose en cuatro familias tecnológicas principales.

#### Bloque 2 — Desarrollo por Categoría
**2.1. Canalizaciones Híbridas (Pipelines) CNN-RNN y Segmentación Clásica con OCR:** Constituye la familia predominante del corpus con el 53,3 % de las implementaciones (56 de 105 estudios; Tabla XVII). Combina redes convolucionales (ResNet, VGG, YOLO, Mask R-CNN) para la detección espacial de regiones y tablas con redes recurrentes (BiLSTM) y motores OCR para la transcripción secuencial de texto [5], [10], [11], [59], [71], [103]. Su vigencia responde a su bajo costo computacional en CPU y alta interpretabilidad modular.

'''
        c = c[:p_tab17_end] + new_md_pi1 + c[p_transf:]
        print("[OK] Item 2 applied in markdown")

    # 3. Sec III-G (PI2) 2.4
    p_funsd = c.find('superposición de marcas físicas causan frecuentes desconexiones')
    if p_funsd != -1:
        p_funsd_end = c.find('\n\n', p_funsd)
        p_bloque3 = c.find('#### Bloque 3 — Contrastes y Discrepancias Métricas', p_funsd)
        new_24_md = '''\n\n**2.4. Flujos Corporativos Integrados y Lotes Heterogéneos:** Comprende el subconjunto de 6 estudios (5,1 % de PI2; Tabla XVIII) que evaluaron canalizaciones completas sobre lotes continuos de documentos empresariales multiformato, alcanzando una mediana de exactitud/F1 del 90,1 % (rango: 82,0 % – 94,5 %) con latencias de inferencia de 300 ms a 1 800 ms por página [32], [78], [85], [93], [110], [111].\n\n'''
        c = c[:p_funsd_end] + new_24_md + c[p_bloque3:]
        print("[OK] Item 3 applied in markdown")

    # 4. Sec III-H (PI3) 2.1
    p_pi3_21 = c.find('**2.1. Reducción del Tiempo')
    if p_pi3_21 != -1:
        p_pi3_22 = c.find('**2.2. Paridad de Rendimiento', p_pi3_21)
        new_pi3_21_md = '''**2.1. Aceleración Operativa y Reducción del Tiempo de Ciclo (Mejora Favorable +1):**  
Agrupa los 71 estudios (86,6 % de la evidencia comparativa; Tabla XIX, Fig. 8) donde las arquitecturas de IA superaron contundentemente al ingreso manual y al OCR basado en reglas, logrando una reducción mediana del 82,4 % en el tiempo de procesamiento documental (rango empírico: 60,0 % a 95,0 %) y disminuyendo drásticamente la tasa de retrabajo humano ante variaciones de diseño [3]–[7], [44], [55], [103], [127].\n\n'''
        c = c[:p_pi3_21] + new_pi3_21_md + c[p_pi3_22:]
        print("[OK] Item 4 applied in markdown")

    # 5. Sec III-I (PI4)
    # Headings
    p_h6 = c.find('## 6. Mapeo de Tipologías Documentales y Sistemas Corporativos ERP/CRM')
    if p_h6 != -1:
        p_h6_end = c.find('\n', p_h6)
        c = c[:p_h6] + '## 6. Tipologías Documentales y Validación en Sistemas ERP/CRM (PI4: ¿En qué tipologías documentales y sistemas empresariales ERP/CRM se han validado empíricamente los modelos?)' + c[p_h6_end:]

    # Intro
    p_intro_s = c.find('Para determinar qué tipologías documentales y qué plataformas empresariales')
    if p_intro_s != -1:
        p_intro_e = c.find('```\nTABLA XX', p_intro_s)
        new_intro = '''Para determinar la aplicabilidad corporativa real de los modelos (PI4), se clasificó el universo completo del corpus (N = 131) cruzando las cuatro tipologías documentales de negocio frente a su nivel de integración técnica con plataformas empresariales ERP, CRM y DMS. La distribución cuantitativa se detalla en la Tabla XX y se representa en la matriz de calor de la Fig. 9.\n\n'''
        c = c[:p_intro_s] + new_intro + c[p_intro_e:]

    # Footer, Fig 9, Apertura
    p_f9 = c.find('*Fuente: elaboración propia a partir del corpus primario [3]–[133].')
    p_ap_end = c.find('1. **Balances, Tablas y Reportes Financieros Complejos:**', p_f9)
    if p_f9 != -1 and p_ap_end != -1:
        new_f9_ap = '''*Nota: La columna de sistema corporativo describe el mapeo funcional conceptual hacia el que se orienta cada tipología. Nivel de integración real del corpus (N = 131): 103 estudios (78,6 %) evalúan modelos en entornos aislados sin conectores empresariales; 20 estudios (15,3 %) generan salidas estructuradas intermedias (JSON/CSV/XML) listas para ingesta; y únicamente 8 estudios (6,1 %; [28], [44], [54], [62], [64], [97], [127], [133]) validan integración transaccional activa con sistemas ERP/contables productivos.

![Fig. 9. Matriz de calor (heatmap) de tipologías documentales empresariales frente al nivel de integración en sistemas ERP/CRM/DMS (PI4, N = 131)](file:///c:/Users/HP/Desktop/ESCRITORIO/PROYECTOS%20UNIVERSIDAD/Formacion_Investigacion_42922/project/resultados/outputs/fig9_matriz_calor_sistemas.png)
*Fig. 9. Matriz de calor (heatmap) de tipologías documentales empresariales frente al nivel de integración en sistemas ERP/CRM/DMS (PI4, N = 131).*

#### Bloque 1 — Apertura
**1) Apertura:** Ciento treinta y un estudios (100,0 % del corpus; TABLA XX, Fig. 9) se mapearon en torno a las tipologías documentales corporativas y su integración sistémica (PI4). El núcleo contable conformado por balances/tablas matriciales (45,0 %, n = 59) y facturas comerciales (26,0 %, n = 34) concentra el 71,0 % de la investigación global (58,0 % estricto al considerar únicamente las 42 tablas financieras específicas más las 34 facturas). No obstante, se evidencia una marcada asimetría entre el reconocimiento documental y el despliegue en ingeniería de software: mientras que en PD3 se identificaron 8 casos de estudio corporativos a nivel de diseño metodológico ([64], [70], [75], [84], [103], [117], [127], [131]), en PI4 solo 8 investigaciones implementaron integración técnica transaccional activa con plataformas ERP ([28], [44], [54], [62], [64], [97], [127], [133]), convergiendo ambas dimensiones exclusivamente en dos estudios ([64], [127]).

#### Bloque 2 — Desarrollo por Categoría
'''
        c = c[:p_f9] + new_f9_ap + c[p_ap_end:]
        print("[OK] Item 5 applied in markdown")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"[SUCCESS] All surgical updates applied to {path}\n")

if __name__ == '__main__':
    update_combined()
    update_docx_resultados()
    update_markdown()

