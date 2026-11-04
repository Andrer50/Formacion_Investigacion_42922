import os

def update_combined():
    path = 'project/metodologia/scripts/build_combined_ieee_article.py'
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()

    # 1. Sec I-B Point 3
    old_p1 = '''add_p(
    "A diferencia de las revisiones secundarias previas identificadas en la literatura (compiladas en la Tabla VIII), las cuales se restringen a "
    "taxonomías teóricas o panoramas cualitativos sobre bancos de prueba aislados, existe una marcada escasez de estudios primarios que aborden "
    "la integración transaccional de extremo a extremo entre las canalizaciones (pipelines) de IDP y los sistemas empresariales corporativos (ERP, CRM y DMS). "
    "La literatura tiende a dar por sentada la interoperabilidad de datos, omitiendo la evaluación concurrente de latencia en tiempo real, "
    "consumo de recursos (GPU vs. CPU) y protocolos de arbitraje humano en el bucle (human-in-the-loop) en entornos operativos reales [70], [84], [127].",
    bold_prefix="3) Aislamiento Transaccional con Sistemas ERP: "
)'''
    new_p1 = '''add_p(
    "La mayoría de las propuestas algorítmicas limita su alcance a la extracción visual de entidades en formatos intermedios (JSON/CSV) en entornos aislados de laboratorio, careciendo de conectores transaccionales activos, validación fiscal de tres vías (Three-Way Matching) y mecanismos de control de alucinaciones contables requeridos por sistemas ERP productivos como SAP S/4HANA, Oracle Financials o Microsoft Dynamics [28], [64], [112], [127].",
    bold_prefix="3) Brecha de Integración Transaccional con Sistemas ERP/CRM: "
)'''
    assert old_p1 in c, "Item 1 old block not found in combined"
    c = c.replace(old_p1, new_p1)

    # 2. Sec III-F (PI1)
    old_p2 = '''add_table_footer("Fuente: elaboración propia a partir del corpus primario [3]–[133]. Partición temática unívoca auditada y verificada. Nota: Las listas completas de estudios asignados a cada familia algorítmica se documentan en el Material Suplementario (Apéndice).")

add_figure_with_caption('project/resultados/outputs/fig6_taxonomia_algoritmos.png', 'Fig. 6',
                        'Taxonomía de Familias Algorítmicas de IA en Procesamiento Documental (PI1, n = 105)',
                        'Frecuencia absoluta y porcentaje relativo derivado de síntesis temática [134], [135].')

add_p(
    "Ciento cinco estudios primarios (80,2 % del corpus; TABLA XVII, Fig. 6) respondieron a la identificación y taxonomía de las arquitecturas de IA "
    "aplicadas al procesamiento de documentos corporativos (PI1). Mediante síntesis temática estandarizada (Thomas & Harden [134]; Cruzes & Dybå [135]) "
    "y con un coeficiente de concordancia inter-evaluador de κ = 0,88 sobre la submuestra del 20,6 % (n = 27), se identificaron cuatro familias algorítmicas "
    "mutuamente excluyentes, observándose un predominio de pipelines modulares basados en convolución y OCR neuronal, acompañados por una rápida consolidación "
    "de Transformers multimodales y modelos de visión-lenguaje (VLM).",
    bold_prefix="1) Apertura: "
)

add_p(
    "Esta arquitectura comprende la articulación secuencial de redes neuronales convolucionales (ResNet, VGG, YOLO, Mask R-CNN) para detección de regiones, combinadas con capas recurrentes (LSTM) "
    "y motores OCR para transcripción textual en documentos estructurados. Constituye la familia mayoritaria en la literatura (Tabla XVII, Fig. 6). Las investigaciones convergen en que la modularización "
    "desacopla la detección geométrica de la transcripción, facilitando la depuración y auditoría interna en entornos productivos locales [10], [15], [33], [54], [84]. Cuantitativamente, estos pipelines "
    "alcanzan latencias de inferencia de 80 ms a 250 ms en CPUs estándar con exactitudes de segmentación entre 88,5 % y 96,0 % en plantillas regulares (Tabla XVII).",
    bold_prefix="2.1. Canalizaciones Híbridas (Pipelines) CNN-RNN y Segmentación Clásica con OCR: "
)'''
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
    assert old_p2 in c, "Item 2 old block not found in combined"
    c = c.replace(old_p2, new_p2)

    # 3. Sec III-G (PI2) 2.4
    old_p3 = '''add_p(
    "Esta categoría técnica evalúa el comportamiento de pipelines integrales frente a lotes transaccionales mixtos de documentos heterogéneos en condiciones de producción real (Tabla XVIII). "
    "La incorporación de clasificadores documentales previos al módulo de extracción permite enrutar eficientemente las tipologías hacia motores especializados, mitigando cuellos de botella [32], [78], "
    "registrando una mediana de exactitud transaccional de 90,1 % con latencias entre 300 ms y 1 800 ms por lote.",
    bold_prefix="2.4. Flujos Corporativos Integrados y Lotes Documentales Heterogéneos: "
)'''
    new_p3 = '''add_p(
    "Comprende el subconjunto de 6 estudios (5,1 % de PI2; Tabla XVIII) que evaluaron canalizaciones completas sobre lotes continuos de documentos empresariales multiformato, alcanzando una mediana de exactitud/F1 del 90,1 % (rango: 82,0 % – 94,5 %) con latencias de inferencia de 300 ms a 1 800 ms por página [32], [78], [85], [93], [110], [111].",
    bold_prefix="2.4. Flujos Corporativos Integrados y Lotes Heterogéneos: "
)'''
    assert old_p3 in c, "Item 3 old block not found in combined"
    c = c.replace(old_p3, new_p3)

    # 4. Sec III-H (PI3) 2.1
    old_p4 = '''add_p(
    "Esta dimensión evalúa la aceleración del ciclo operativo lograda por las soluciones de IA frente a la digitación manual y sistemas OCR basados en plantillas rígidas, constituyendo el efecto predominante en la síntesis comparativa (Tabla XIX, Fig. 8). "
    "Los análisis demuestran que la automatización neuronal reduce el tiempo de procesamiento entre un 60,0 % y un 95,0 % en comparación con métodos tradicionales [44], [55], [103], [127]. En flujos de facturación comercial, las soluciones reducen tiempos manuales de ~180 segundos por comprobante a ciclos asistidos de 10 a 25 segundos (con latencias de inferencia de 1 a 2 segundos mediante IA), situando la mediana de reducción agregada en 82,4 %.",
    bold_prefix="2.1. Reducción del Tiempo de Procesamiento y Latencia Operativa (Mejora +1): "
)'''
    new_p4 = '''add_p(
    "Agrupa los 71 estudios (86,6 % de la evidencia comparativa; Tabla XIX, Fig. 8) donde las arquitecturas de IA superaron contundentemente al ingreso manual y al OCR basado en reglas, logrando una reducción mediana del 82,4 % en el tiempo de procesamiento documental (rango empírico: 60,0 % a 95,0 %) y disminuyendo drásticamente la tasa de retrabajo humano ante variaciones de diseño [3]–[7], [44], [55], [103], [127].",
    bold_prefix="2.1. Aceleración Operativa y Reducción del Tiempo de Ciclo (Mejora Favorable +1): "
)'''
    assert old_p4 in c, "Item 4 old block not found in combined"
    c = c.replace(old_p4, new_p4)

    # 5. Sec III-I (PI4)
    old_p5a = '''add_heading_2("I. Mapeo de Tipologías Documentales y Sistemas Corporativos ERP/CRM (PI4: ¿En qué tipologías documentales y arquitecturas de sistemas empresariales ERP/CRM se han validado las propuestas?)")
add_p(
    "Para determinar qué tipologías documentales y qué plataformas empresariales de gestión han sido abordadas en la literatura, se ejecutó un mapeo temático matricial sobre la totalidad del corpus primario (N = 131 estudios, 100,0 % de cobertura). "
    "La categorización documental y el mapeo hacia plataformas corporativas evaluada por doble codificación ciega sobre la muestra del 20,6 % (n = 27 estudios) reportó un coeficiente Kappa de Cohen κ = 0,87 (Po = 92,6 %, Pe = 0,430), "
    "certificando la consistencia taxonómica de la matriz de integración bajo el protocolo formal de extracción y síntesis temática. La matriz cruzada se documenta en la Tabla XX y la matriz de calor (heatmap) se expone en la Fig. 9."
)'''
    new_p5a = '''add_heading_2("I. Tipologías Documentales y Validación en Sistemas ERP/CRM (PI4: ¿En qué tipologías documentales y sistemas empresariales ERP/CRM se han validado empíricamente los modelos?)")
add_p(
    "Para determinar la aplicabilidad corporativa real de los modelos (PI4), se clasificó el universo completo del corpus (N = 131) cruzando las cuatro tipologías documentales de negocio frente a su nivel de integración técnica con plataformas empresariales ERP, CRM y DMS. La distribución cuantitativa se detalla en la Tabla XX y se representa en la matriz de calor de la Fig. 9."
)'''
    assert old_p5a in c, "Item 5A old block not found in combined"
    c = c.replace(old_p5a, new_p5a)

    old_p5b = '''add_table_footer("Fuente: elaboración propia a partir del corpus primario [3]–[133]. *Nota: De los 59 estudios tabulares, 42 (32,1 % del corpus) abordan directamente estados y tablas financieras contables, mientras que 17 (13,0 %) evalúan detección genérica de tablas. Junto a las 34 facturas (26,0 %), el núcleo contable estricto reúne 76 estudios (58,0 %), alcanzando 93 estudios (71,0 %) al incluir la totalidad de investigaciones tabulares.")

add_figure_with_caption('project/resultados/outputs/fig9_matriz_calor_sistemas.png', 'Fig. 9',
                        'Mapeo Cruzado: Tipología Documental × Plataforma Empresarial (PI4, N = 131)',
                        'Matriz de calor que representa la frecuencia de estudios primarios mapeados.')

add_p(
    "Ciento treinta y un artículos (100,0 % del corpus; TABLA XX, Fig. 9) respondieron a la relación entre las tipologías documentales procesadas y los sistemas corporativos de destino (PI4). Mediante síntesis temática y mapeo matricial con un índice de fiabilidad de κ = 0,87, se determinó una fuerte polarización de la literatura hacia tablas contables financieras (45,0 %) y facturas comerciales (26,0 %) orientadas funcionalmente a módulos de sistemas ERP, existiendo una menor penetración en flujos documentales de plataformas CRM. En cuanto al nivel de integración técnica efectiva, el 78,6 % de los estudios (103 de 131) se restringe a la extracción algorítmica aislada (evaluación sobre colecciones de imágenes o benchmarks con salida JSON/XML sin conectores a plataformas empresariales), el 15,3 % (20 de 131) implementa mecanismos intermedios de persistencia relacional SQL o APIs REST, y solo el 6,1 % (8 de 131; [28], [44], [54], [62], [64], [97], [127], [133]) valida empíricamente la solución en flujos transaccionales vivos de producción empresarial. Es fundamental diferenciar esta categoría de integración técnica con ERP (PI4: 8 estudios con validación transaccional activa; [28], [44], [54], [62], [64], [97], [127], [133]) del diseño metodológico catalogado como Caso de Estudio Corporativo en PD3 ([64], [70], [75], [84], [103], [117], [127], [131]): mientras la primera exige acoplamiento funcional con las bases de datos y flujos contables del ERP, el segundo evalúa cualitativa u operativamente el proceso dentro de una organización; únicamente [64] y [127] satisfacen ambos requerimientos de manera concurrente.",
    bold_prefix="1) Apertura: "
)'''
    new_p5b = '''add_table_footer("*Nota: La columna de sistema corporativo describe el mapeo funcional conceptual hacia el que se orienta cada tipología. Nivel de integración real del corpus (N = 131): 103 estudios (78,6 %) evalúan modelos en entornos aislados sin conectores empresariales; 20 estudios (15,3 %) generan salidas estructuradas intermedias (JSON/CSV/XML) listas para ingesta; y únicamente 8 estudios (6,1 %; [28], [44], [54], [62], [64], [97], [127], [133]) validan integración transaccional activa con sistemas ERP/contables productivos.")

add_figure_with_caption('project/resultados/outputs/fig9_matriz_calor_sistemas.png', 'Fig. 9',
                        'Matriz de calor (heatmap) de tipologías documentales empresariales frente al nivel de integración en sistemas ERP/CRM/DMS (PI4, N = 131)',
                        '')

add_p(
    "Ciento treinta y un estudios (100,0 % del corpus; TABLA XX, Fig. 9) se mapearon en torno a las tipologías documentales corporativas y su integración sistémica (PI4). El núcleo contable conformado por balances/tablas matriciales (45,0 %, n = 59) y facturas comerciales (26,0 %, n = 34) concentra el 71,0 % de la investigación global (58,0 % estricto al considerar únicamente las 42 tablas financieras específicas más las 34 facturas). No obstante, se evidencia una marcada asimetría entre el reconocimiento documental y el despliegue en ingeniería de software: mientras que en PD3 se identificaron 8 casos de estudio corporativos a nivel de diseño metodológico ([64], [70], [75], [84], [103], [117], [127], [131]), en PI4 solo 8 investigaciones implementaron integración técnica transaccional activa con plataformas ERP ([28], [44], [54], [62], [64], [97], [127], [133]), convergiendo ambas dimensiones exclusivamente en dos estudios ([64], [127]).",
    bold_prefix="1) Apertura: "
)'''
    assert old_p5b in c, "Item 5B old block not found in combined"
    c = c.replace(old_p5b, new_p5b)

    # 6. Sec IV Subapartado B
    old_p6 = '''add_heading_2("B. Brecha de Transferencia e Integración en Sistemas ERP y CRM")
add_p(
    "A pesar de que el 100,0 % de las investigaciones analizadas persigue la automatización del procesamiento de documentos empresariales, se constata una profunda brecha de transferencia hacia entornos productivos de software corporativo. "
    "De los 131 estudios primarios, únicamente 8 investigaciones ([28], [44], [54], [62], [64], [97], [127], [133]) documentan implementaciones transaccionales end-to-end integradas con plataformas ERP, CRM o DMS operativas (p. ej., SAP, Microsoft Dynamics u Odoo). "
    "La mayoría de los desarrollos se detiene en etapas de laboratorio o extracción aislada de datos estructurados (JSON/CSV), sin resolver los requerimientos de conciliación contable de tres vías (three-way matching), imputación de cuentas de libro mayor, validación de reglas fiscales o auditoría transaccional. "
    "Esta limitación evidencia que el principal desafío en la ingeniería de IDP no reside únicamente en la capacidad de extracción semántica, sino en la gobernanza del dato extraído, la mitigación de alucinaciones y la interoperabilidad mediante interfaces de programación de aplicaciones (API) transaccionales."
)'''
    new_p6 = '''add_heading_2("B. Brecha de Transferencia Industrial y Desconexión Transaccional con Sistemas ERP")
add_p(
    "Un segundo hallazgo estructural de esta revisión es la desconexión entre la investigación en visión computacional y la ingeniería de sistemas empresariales. Aunque el 71,0 % del corpus aborda documentos contables críticos orientados conceptualmente a módulos financieros y de cuentas por pagar (Tabla XX), el 78,6 % de los estudios (103 de 131) finaliza su flujo experimental en la predicción de etiquetas o archivos JSON locales, sin abordar la interoperabilidad transaccional. Como demostró el cruce entre el mapeo de Petersen (PD3) y el análisis de integración técnica (PI4), solo 8 estudios validaron conectores activos con sistemas ERP ([28], [44], [54], [62], [64], [97], [127], [133]) y únicamente dos investigaciones ([64], [127]) articularon simultáneamente un diseño de caso de estudio corporativo real con integración productiva en el ERP. Esto confirma que la principal barrera para la adopción industrial del IDP ya no radica en el reconocimiento óptico aislado, sino en la orquestación de reglas de negocio, conciliación tributaria de tres vías (Three-Way Matching), gobernanza de privacidad on-premise ([116], [127]) y mitigación de alucinaciones numéricas antes del asiento contable definitivo ([4], [37])."
)'''
    assert old_p6 in c, "Item 6 old block not found in combined"
    c = c.replace(old_p6, new_p6)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"[OK] Successfully updated all items in {path}")

def update_docx_resultados():
    path = 'project/resultados/scripts/build_resultados_completo_docx.py'
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()

    # 2. Sec III-F (PI1)
    old_p2 = '''add_table_footer("Fuente: elaboración propia a partir del corpus primario [3]–[133]. Partición temática unívoca auditada y verificada. Nota: Las listas completas de estudios asignados a cada familia algorítmica se documentan en el Material Suplementario (Apéndice).")

add_figure_with_caption('project/resultados/outputs/fig6_taxonomia_algoritmos.png', 'Fig. 6',
                        'Taxonomía de Familias Algorítmicas de IA en Procesamiento Documental (PI1, n = 105)',
                        'Frecuencia absoluta y porcentaje relativo derivado de síntesis temática [134], [135].')

add_p(
    "Ciento cinco estudios primarios (80,2 % del corpus; TABLA XVII, Fig. 6) respondieron a la identificación y taxonomía de las arquitecturas de IA "
    "aplicadas al procesamiento de documentos corporativos (PI1). Mediante síntesis temática estandarizada (Thomas & Harden [134]; Cruzes & Dybå [135]) "
    "y con un coeficiente de concordancia inter-evaluador de κ = 0,88 sobre la submuestra del 20,6 % (n = 27), se identificaron cuatro familias algorítmicas "
    "mutuamente excluyentes, observándose un predominio de pipelines modulares basados en convolución y OCR neuronal, acompañados por una rápida consolidación "
    "de Transformers multimodales y modelos de visión-lenguaje (VLM).",
    bold_prefix="1) Apertura: "
)

add_p(
    "Esta arquitectura comprende la articulación secuencial de redes neuronales convolucionales (ResNet, VGG, YOLO, Mask R-CNN) para detección de regiones, combinadas con capas recurrentes (LSTM) "
    "y motores OCR para transcripción textual en documentos estructurados. Constituye la familia mayoritaria en la literatura (Tabla XVII, Fig. 6). Las investigaciones convergen en que la modularización "
    "desacopla la detección geométrica de la transcripción, facilitando la depuración y auditoría interna en entornos productivos locales [10], [15], [33], [54], [84]. Cuantitativamente, estos pipelines "
    "alcanzan latencias de inferencia de 80 ms a 250 ms en CPUs estándar con exactitudes de segmentación entre 88,5 % y 96,0 % en plantillas regulares (Tabla XVII).",
    bold_prefix="2.1. Canalizaciones Híbridas (Pipelines) CNN-RNN y Segmentación Clásica con OCR: "
)'''
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
    assert old_p2 in c, "Item 2 old block not found in resultados docx"
    c = c.replace(old_p2, new_p2)

    # 3. Sec III-G (PI2) 2.4
    old_p3 = '''add_p(
    "Esta categoría técnica evalúa el comportamiento de pipelines integrales frente a lotes transaccionales mixtos de documentos heterogéneos en condiciones de producción real (Tabla XVIII). "
    "La incorporación de clasificadores documentales previos al módulo de extracción permite enrutar eficientemente las tipologías hacia motores especializados, mitigando cuellos de botella [32], [78], "
    "registrando una mediana de exactitud transaccional de 90,1 % con latencias entre 300 ms y 1 800 ms por lote.",
    bold_prefix="2.4. Flujos Corporativos Integrados y Lotes Documentales Heterogéneos: "
)'''
    new_p3 = '''add_p(
    "Comprende el subconjunto de 6 estudios (5,1 % de PI2; Tabla XVIII) que evaluaron canalizaciones completas sobre lotes continuos de documentos empresariales multiformato, alcanzando una mediana de exactitud/F1 del 90,1 % (rango: 82,0 % – 94,5 %) con latencias de inferencia de 300 ms a 1 800 ms por página [32], [78], [85], [93], [110], [111].",
    bold_prefix="2.4. Flujos Corporativos Integrados y Lotes Heterogéneos: "
)'''
    assert old_p3 in c, "Item 3 old block not found in resultados docx"
    c = c.replace(old_p3, new_p3)

    # 4. Sec III-H (PI3) 2.1
    old_p4 = '''add_p(
    "Esta dimensión evalúa la aceleración del ciclo operativo lograda por las soluciones de IA frente a la digitación manual y sistemas OCR basados en plantillas rígidas, constituyendo el efecto predominante en la síntesis comparativa (Tabla XIX, Fig. 8). "
    "Los análisis demuestran que la automatización neuronal reduce el tiempo de procesamiento entre un 60,0 % y un 95,0 % en comparación con métodos tradicionales [44], [55], [103], [127]. En flujos de facturación comercial, las soluciones reducen tiempos manuales de ~180 segundos por comprobante a ciclos asistidos de 10 a 25 segundos (con latencias de inferencia de 1 a 2 segundos mediante IA), situando la mediana de reducción agregada en 82,4 %.",
    bold_prefix="2.1. Reducción del Tiempo de Procesamiento y Latencia Operativa (Mejora +1): "
)'''
    new_p4 = '''add_p(
    "Agrupa los 71 estudios (86,6 % de la evidencia comparativa; Tabla XIX, Fig. 8) donde las arquitecturas de IA superaron contundentemente al ingreso manual y al OCR basado en reglas, logrando una reducción mediana del 82,4 % en el tiempo de procesamiento documental (rango empírico: 60,0 % a 95,0 %) y disminuyendo drásticamente la tasa de retrabajo humano ante variaciones de diseño [3]–[7], [44], [55], [103], [127].",
    bold_prefix="2.1. Aceleración Operativa y Reducción del Tiempo de Ciclo (Mejora Favorable +1): "
)'''
    assert old_p4 in c, "Item 4 old block not found in resultados docx"
    c = c.replace(old_p4, new_p4)

    # 5. Sec III-I (PI4)
    old_p5a = '''add_heading_2("I. Mapeo de Tipologías Documentales y Sistemas Corporativos ERP/CRM (PI4: ¿En qué tipologías documentales y arquitecturas de sistemas empresariales ERP/CRM se han validado las propuestas?)")
add_p(
    "Para determinar qué tipologías documentales y qué plataformas empresariales de gestión han sido abordadas en la literatura, se ejecutó un mapeo temático matricial sobre la totalidad del corpus primario (N = 131 estudios, 100,0 % de cobertura). "
    "La categorización documental y el mapeo hacia plataformas corporativas evaluada por doble codificación ciega sobre la muestra del 20,6 % (n = 27 estudios) reportó un coeficiente Kappa de Cohen κ = 0,87 (Po = 92,6 %, Pe = 0,430), "
    "certificando la consistencia taxonómica de la matriz de integración bajo el protocolo formal de extracción y síntesis temática. La matriz cruzada se documenta en la Tabla XX y la matriz de calor (heatmap) se expone en la Fig. 9."
)'''
    new_p5a = '''add_heading_2("I. Tipologías Documentales y Validación en Sistemas ERP/CRM (PI4: ¿En qué tipologías documentales y sistemas empresariales ERP/CRM se han validado empíricamente los modelos?)")
add_p(
    "Para determinar la aplicabilidad corporativa real de los modelos (PI4), se clasificó el universo completo del corpus (N = 131) cruzando las cuatro tipologías documentales de negocio frente a su nivel de integración técnica con plataformas empresariales ERP, CRM y DMS. La distribución cuantitativa se detalla en la Tabla XX y se representa en la matriz de calor de la Fig. 9."
)'''
    assert old_p5a in c, "Item 5A old block not found in resultados docx"
    c = c.replace(old_p5a, new_p5a)

    old_p5b = '''add_table_footer("Fuente: elaboración propia a partir del corpus primario [3]–[133]. *Nota: De los 59 estudios tabulares, 42 (32,1 % del corpus) abordan directamente estados y tablas financieras contables, mientras que 17 (13,0 %) evalúan detección genérica de tablas. Junto a las 34 facturas (26,0 %), el núcleo contable estricto reúne 76 estudios (58,0 %), alcanzando 93 estudios (71,0 %) al incluir la totalidad de investigaciones tabulares.")

add_figure_with_caption('project/resultados/outputs/fig9_matriz_calor_sistemas.png', 'Fig. 9',
                        'Mapeo Cruzado: Tipología Documental × Plataforma Empresarial (PI4, N = 131)',
                        'Matriz de calor que representa la frecuencia de estudios primarios mapeados.')

add_p(
    "Ciento treinta y un artículos (100,0 % del corpus; TABLA XX, Fig. 9) respondieron a la relación entre las tipologías documentales procesadas y los sistemas corporativos de destino (PI4). Mediante síntesis temática y mapeo matricial con un índice de fiabilidad de κ = 0,87, se determinó una fuerte polarización de la literatura hacia tablas contables financieras (45,0 %) y facturas comerciales (26,0 %) orientadas funcionalmente a módulos de sistemas ERP, existiendo una menor penetración en flujos documentales de plataformas CRM. En cuanto al nivel de integración técnica efectiva, el 78,6 % de los estudios (103 de 131) se restringe a la extracción algorítmica aislada (evaluación sobre colecciones de imágenes o benchmarks con salida JSON/XML sin conectores a plataformas empresariales), el 15,3 % (20 de 131) implementa mecanismos intermedios de persistencia relacional SQL o APIs REST, y solo el 6,1 % (8 de 131; [28], [44], [54], [62], [64], [97], [127], [133]) valida empíricamente la solución en flujos transaccionales vivos de producción empresarial. Es fundamental diferenciar esta categoría de integración técnica con ERP (PI4: 8 estudios con validación transaccional activa; [28], [44], [54], [62], [64], [97], [127], [133]) del diseño metodológico catalogado como Caso de Estudio Corporativo en PD3 ([64], [70], [75], [84], [103], [117], [127], [131]): mientras la primera exige acoplamiento funcional con las bases de datos y flujos contables del ERP, el segundo evalúa cualitativa u operativamente el proceso dentro de una organización; únicamente [64] y [127] satisfacen ambos requerimientos de manera concurrente.",
    bold_prefix="1) Apertura: "
)'''
    new_p5b = '''add_table_footer("*Nota: La columna de sistema corporativo describe el mapeo funcional conceptual hacia el que se orienta cada tipología. Nivel de integración real del corpus (N = 131): 103 estudios (78,6 %) evalúan modelos en entornos aislados sin conectores empresariales; 20 estudios (15,3 %) generan salidas estructuradas intermedias (JSON/CSV/XML) listas para ingesta; y únicamente 8 estudios (6,1 %; [28], [44], [54], [62], [64], [97], [127], [133]) validan integración transaccional activa con sistemas ERP/contables productivos.")

add_figure_with_caption('project/resultados/outputs/fig9_matriz_calor_sistemas.png', 'Fig. 9',
                        'Matriz de calor (heatmap) de tipologías documentales empresariales frente al nivel de integración en sistemas ERP/CRM/DMS (PI4, N = 131)',
                        '')

add_p(
    "Ciento treinta y un estudios (100,0 % del corpus; TABLA XX, Fig. 9) se mapearon en torno a las tipologías documentales corporativas y su integración sistémica (PI4). El núcleo contable conformado por balances/tablas matriciales (45,0 %, n = 59) y facturas comerciales (26,0 %, n = 34) concentra el 71,0 % de la investigación global (58,0 % estricto al considerar únicamente las 42 tablas financieras específicas más las 34 facturas). No obstante, se evidencia una marcada asimetría entre el reconocimiento documental y el despliegue en ingeniería de software: mientras que en PD3 se identificaron 8 casos de estudio corporativos a nivel de diseño metodológico ([64], [70], [75], [84], [103], [117], [127], [131]), en PI4 solo 8 investigaciones implementaron integración técnica transaccional activa con plataformas ERP ([28], [44], [54], [62], [64], [97], [127], [133]), convergiendo ambas dimensiones exclusivamente en dos estudios ([64], [127]).",
    bold_prefix="1) Apertura: "
)'''
    assert old_p5b in c, "Item 5B old block not found in resultados docx"
    c = c.replace(old_p5b, new_p5b)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"[OK] Successfully updated all items in {path}")

def update_markdown():
    path = 'project/resultados/scripts/build_full_resultados_markdown.py'
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()

    # 2. Sec III-F (PI1)
    p_tab17_end = c.find('*Fuente: elaboración propia a partir del corpus primario [3]–[133].*')
    p_transf = c.find('2. **Transformers Multimodales')
    if p_transf == -1:
        p_transf = c.find('**Transformers Multimodales')
    
    # Check what is between p_tab17_end and p_transf
    old_md_pi1 = c[p_tab17_end:p_transf]
    new_md_pi1 = '''Fuente: elaboración propia a partir del corpus primario [3]–[133]. Síntesis temática según Thomas & Harden [134] y Cruzes & Dybå [135]. Acuerdo inter-evaluador κ = 0,88. Nota: Las listas completas de estudios por familia algorítmica se documentan en el Material Suplementario (Apéndice).

![Fig. 6. Distribución de estudios por familia algorítmica de IA en procesamiento documental (Síntesis Temática, PI1, n = 105)](file:///c:/Users/HP/Desktop/ESCRITORIO/PROYECTOS%20UNIVERSIDAD/Formacion_Investigacion_42922/project/resultados/outputs/fig6_taxonomia_algoritmos.png)
*Fig. 6. Distribución de estudios por familia algorítmica de IA en procesamiento documental (Síntesis Temática, PI1, n = 105).*

#### Bloque 1 — Apertura
**1) Apertura:** Ciento cinco estudios primarios (80,2 % del corpus; TABLA XVII, Fig. 6) especificaron arquitecturas algorítmicas reproducibles de IA para el procesamiento de documentos empresariales (PI1), estructurándose en cuatro familias tecnológicas principales.

#### Bloque 2 — Desarrollo por Categoría
**2.1. Canalizaciones Híbridas (Pipelines) CNN-RNN y Segmentación Clásica con OCR:** Constituye la familia predominante del corpus con el 53,3 % de las implementaciones (56 de 105 estudios; Tabla XVII). Combina redes convolucionales (ResNet, VGG, YOLO, Mask R-CNN) para la detección espacial de regiones y tablas con redes recurrentes (BiLSTM) y motores OCR para la transcripción secuencial de texto [5], [10], [11], [59], [71], [103]. Su vigencia responde a su bajo costo computacional en CPU y alta interpretabilidad modular.

'''
    c = c[:p_tab17_end] + new_md_pi1 + c[p_transf:]

    # 3. Sec III-G (PI2) 2.4
    p_24 = c.find('**Flujos Corporativos Integrados')
    if p_24 == -1:
        p_24 = c.find('Flujos Corporativos Integrados')
    p_24_line_start = c.rfind('\n', 0, p_24) + 1
    p_bloque3 = c.find('#### Bloque 3 — Contrastes y Discrepancias Métricas', p_24)

    new_24_md = '''**2.4. Flujos Corporativos Integrados y Lotes Heterogéneos:** Comprende el subconjunto de 6 estudios (5,1 % de PI2; Tabla XVIII) que evaluaron canalizaciones completas sobre lotes continuos de documentos empresariales multiformato, alcanzando una mediana de exactitud/F1 del 90,1 % (rango: 82,0 % – 94,5 %) con latencias de inferencia de 300 ms a 1 800 ms por página [32], [78], [85], [93], [110], [111].

'''
    c = c[:p_24_line_start] + new_24_md + c[p_bloque3:]

    # 4. Sec III-H (PI3) 2.1
    p_pi3_21 = c.find('**2.1. Reducción del Tiempo')
    if p_pi3_21 == -1:
        p_pi3_21 = c.find('2.1. Reducción del Tiempo')
    p_pi3_22 = c.find('**2.2. Paridad de Rendimiento', p_pi3_21)
    new_pi3_21_md = '''**2.1. Aceleración Operativa y Reducción del Tiempo de Ciclo (Mejora Favorable +1):**  
Agrupa los 71 estudios (86,6 % de la evidencia comparativa; Tabla XIX, Fig. 8) donde las arquitecturas de IA superaron contundentemente al ingreso manual y al OCR basado en reglas, logrando una reducción mediana del 82,4 % en el tiempo de procesamiento documental (rango empírico: 60,0 % a 95,0 %) y disminuyendo drásticamente la tasa de retrabajo humano ante variaciones de diseño [3]–[7], [44], [55], [103], [127].

'''
    c = c[:p_pi3_21] + new_pi3_21_md + c[p_pi3_22:]

    # 5. Sec III-I (PI4)
    # Headings
    old_h_pi4 = '### I. Mapeo de Tipologías Documentales y Sistemas Corporativos ERP/CRM (PI4: ¿En qué tipologías documentales y arquitecturas de sistemas empresariales ERP/CRM se han validado las propuestas?)'
    new_h_pi4 = '### I. Tipologías Documentales y Validación en Sistemas ERP/CRM (PI4: ¿En qué tipologías documentales y sistemas empresariales ERP/CRM se han validado empíricamente los modelos?)'
    if old_h_pi4 in c:
        c = c.replace(old_h_pi4, new_h_pi4)

    # Intro paragraph
    p_intro_start = c.find('Para determinar qué tipologías documentales y qué plataformas empresariales')
    p_intro_end = c.find('```\nTABLA XX', p_intro_start)
    new_intro_pi4 = '''Para determinar la aplicabilidad corporativa real de los modelos (PI4), se clasificó el universo completo del corpus (N = 131) cruzando las cuatro tipologías documentales de negocio frente a su nivel de integración técnica con plataformas empresariales ERP, CRM y DMS. La distribución cuantitativa se detalla en la Tabla XX y se representa en la matriz de calor de la Fig. 9.

'''
    if p_intro_start != -1 and p_intro_end != -1:
        c = c[:p_intro_start] + new_intro_pi4 + c[p_intro_end:]

    # Footer, Fig 9, Apertura
    p_tab20_end = c.find('*Fuente: elaboración propia a partir del corpus primario [3]–[133].')
    p_bal21 = c.find('1. **Balances, Tablas', p_tab20_end)
    if p_bal21 == -1:
        p_bal21 = c.find('**Balances, Tablas', p_tab20_end)
    if p_bal21 == -1:
        p_bal21 = c.find('2.1. Balances, Tablas', p_tab20_end)

    new_pi4_foot_ap = '''*Nota: La columna de sistema corporativo describe el mapeo funcional conceptual hacia el que se orienta cada tipología. Nivel de integración real del corpus (N = 131): 103 estudios (78,6 %) evalúan modelos en entornos aislados sin conectores empresariales; 20 estudios (15,3 %) generan salidas estructuradas intermedias (JSON/CSV/XML) listas para ingesta; y únicamente 8 estudios (6,1 %; [28], [44], [54], [62], [64], [97], [127], [133]) validan integración transaccional activa con sistemas ERP/contables productivos.

![Fig. 9. Matriz de calor (heatmap) de tipologías documentales empresariales frente al nivel de integración en sistemas ERP/CRM/DMS (PI4, N = 131)](file:///c:/Users/HP/Desktop/ESCRITORIO/PROYECTOS%20UNIVERSIDAD/Formacion_Investigacion_42922/project/resultados/outputs/fig9_matriz_calor_sistemas.png)
*Fig. 9. Matriz de calor (heatmap) de tipologías documentales empresariales frente al nivel de integración en sistemas ERP/CRM/DMS (PI4, N = 131).*

#### Bloque 1 — Apertura
**1) Apertura:** Ciento treinta y un estudios (100,0 % del corpus; TABLA XX, Fig. 9) se mapearon en torno a las tipologías documentales corporativas y su integración sistémica (PI4). El núcleo contable conformado por balances/tablas matriciales (45,0 %, n = 59) y facturas comerciales (26,0 %, n = 34) concentra el 71,0 % de la investigación global (58,0 % estricto al considerar únicamente las 42 tablas financieras específicas más las 34 facturas). No obstante, se evidencia una marcada asimetría entre el reconocimiento documental y el despliegue en ingeniería de software: mientras que en PD3 se identificaron 8 casos de estudio corporativos a nivel de diseño metodológico ([64], [70], [75], [84], [103], [117], [127], [131]), en PI4 solo 8 investigaciones implementaron integración técnica transaccional activa con plataformas ERP ([28], [44], [54], [62], [64], [97], [127], [133]), convergiendo ambas dimensiones exclusivamente en dos estudios ([64], [127]).

#### Bloque 2 — Desarrollo por Categoría
'''
    if p_tab20_end != -1 and p_bal21 != -1:
        c = c[:p_tab20_end] + new_pi4_foot_ap + c[p_bal21:]

    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"[OK] Successfully updated all items in {path}")

if __name__ == '__main__':
    update_combined()
    update_docx_resultados()
    update_markdown()

