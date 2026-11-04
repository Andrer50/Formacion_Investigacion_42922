import re

def sync_markdown():
    path = 'project/resultados/main.md'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. PI1 Footer of Table XVII
    old_t17_footer = '*Fuente: elaboración propia a partir del corpus primario [3]–[133].*'
    new_t17_footer = '*Fuente: elaboración propia a partir del corpus primario [3]–[133]. Síntesis temática según Thomas & Harden [134] y Cruzes & Dybå [135]. Acuerdo inter-evaluador κ = 0,88. Nota: Las listas completas de estudios por familia algorítmica se documentan en el Material Suplementario (Apéndice).*'
    
    # We replace only in the context of Table XVII
    if old_t17_footer in content:
        # replace the one after TABLA XVII
        t17_pos = content.find('TABLA XVII')
        if t17_pos != -1:
            next_foot = content.find(old_t17_footer, t17_pos)
            if next_foot != -1 and next_foot < t17_pos + 1500:
                content = content[:next_foot] + new_t17_footer + content[next_foot + len(old_t17_footer):]
                print("Updated Table XVII footer in main.md")

    # 2. PI1 Fig 6 caption
    old_fig6 = '*Fig. 6. Taxonomía de familias algorítmicas de IA en procesamiento documental empresarial (PI1, n = 105). Frecuencia absoluta y porcentaje relativo derivado de síntesis temática [134], [135]. Fuente: elaboración propia a partir del corpus primario [3]–[133].*'
    new_fig6 = '*Fig. 6. Distribución de estudios por familia algorítmica de IA en procesamiento documental (Síntesis Temática, PI1, n = 105).*'
    if old_fig6 in content:
        content = content.replace(old_fig6, new_fig6)
        print("Updated Fig 6 caption in main.md")

    # 3. PI1 Bloque 1 - Apertura
    old_pi1_apertura = '#### Bloque 1 — Apertura\nCiento cinco estudios primarios (80,2 % del corpus; TABLA XVII, Fig. 6) aportan evidencia para responder a la pregunta sobre la taxonomía de arquitecturas de IA aplicadas al procesamiento de documentos corporativos (PI1). Mediante síntesis temática estandarizada (*Thomas & Harden [134]; Cruzes & Dybå [135]*) y con un coeficiente de concordancia inter-evaluador de $\\kappa = 0,88$ sobre la submuestra del 20,6 % ($n = 27$), se identificaron cuatro familias algorítmicas mutuamente excluyentes, observándose un predominio de pipelines modulares basados en convolución y OCR neuronal, acompañados por una rápida consolidación de Transformers multimodales y modelos de visión-lenguaje (VLM).'
    new_pi1_apertura = '#### Bloque 1 — Apertura\n1) Apertura: Ciento cinco estudios primarios (80,2 % del corpus; TABLA XVII, Fig. 6) especificaron arquitecturas algorítmicas reproducibles de IA para el procesamiento de documentos empresariales (PI1), estructurándose en cuatro familias tecnológicas principales.'
    if old_pi1_apertura in content:
        content = content.replace(old_pi1_apertura, new_pi1_apertura)
        print("Updated PI1 Apertura in main.md")

    # 4. PI1 Subapartado 2.1
    old_pi1_21 = '**1. Canalizaciones Híbridas (*Pipelines*) CNN-RNN y Segmentación Clásica con OCR:**  \nEsta arquitectura comprende la articulación secuencial de redes neuronales convolucionales (ResNet, VGG, YOLO, Mask R-CNN) para detección de regiones, combinadas con capas recurrentes (LSTM) y motores OCR para transcripción textual en documentos estructurados. Constituye la familia mayoritaria en la literatura (Tabla XVII, Fig. 6). Las investigaciones convergen en que la modularización desacopla la detección geométrica de la transcripción, facilitando la depuración y auditoría interna en entornos productivos locales [10], [15], [33], [54], [84]. Cuantitativamente, estos pipelines alcanzan latencias de inferencia de 80 ms a 250 ms en CPUs estándar con exactitudes de segmentación entre 88,5 % y 96,0 % en plantillas regulares (Tabla XVII).'
    new_pi1_21 = '2.1. Canalizaciones Híbridas (Pipelines) CNN-RNN y Segmentación Clásica con OCR: Constituye la familia predominante del corpus con el 53,3 % de las implementaciones (56 de 105 estudios; Tabla XVII). Combina redes convolucionales (ResNet, VGG, YOLO, Mask R-CNN) para la detección espacial de regiones y tablas con redes recurrentes (BiLSTM) y motores OCR para la transcripción secuencial de texto [5], [10], [11], [59], [71], [103]. Su vigencia responde a su bajo costo computacional en CPU y alta interpretabilidad modular.'
    if old_pi1_21 in content:
        content = content.replace(old_pi1_21, new_pi1_21)
        print("Updated PI1 2.1 in main.md")

    # 5. PI2 Subapartado 2.4
    old_pi2_24 = '**4. Flujos Corporativos Integrados y Lotes Documentales Heterogéneos:**  \nEsta categoría técnica evalúa el comportamiento de pipelines integrales frente a lotes transaccionales mixtos de documentos heterogéneos en condiciones de producción real (Tabla XVIII). La incorporación de clasificadores documentales previos al módulo de extracción permite enrutar eficientemente las tipologías hacia motores especializados, mitigando cuellos de botella [32], [78], registrando una mediana de exactitud transaccional de 90,1 % con latencias entre 300 ms y 1 800 ms por lote.'
    new_pi2_24 = '2.4. Flujos Corporativos Integrados y Lotes Heterogéneos: Comprende el subconjunto de 6 estudios (5,1 % de PI2; Tabla XVIII) que evaluaron canalizaciones completas sobre lotes continuos de documentos empresariales multiformato, alcanzando una mediana de exactitud/F1 del 90,1 % (rango: 82,0 % – 94,5 %) con latencias de inferencia de 300 ms a 1 800 ms por página [32], [78], [85], [93], [110], [111].'
    if old_pi2_24 in content:
        content = content.replace(old_pi2_24, new_pi2_24)
        print("Updated PI2 2.4 in main.md")

    # 6. PI3 Subapartado 2.1
    old_pi3_21 = '**2.1. Reducción del Tiempo de Procesamiento y Latencia Operativa (Mejora +1):**  \nEsta dimensión evalúa la aceleración del ciclo operativo lograda por las soluciones de IA frente a la digitación manual y sistemas OCR basados en plantillas rígidas, constituyendo el efecto predominante en 71 de los 82 estudios con comparador (86,6 %; Tabla XIX, Fig. 8). Los análisis demuestran que la automatización neuronal reduce el tiempo de procesamiento entre un 60,0 % y un 95,0 % en comparación con métodos tradicionales [44], [55], [103], [127]. En flujos de facturación comercial, las soluciones reducen tiempos manuales de ~180 segundos por comprobante a ciclos asistidos de 10 a 25 segundos (con latencias de inferencia de 1 a 2 segundos mediante IA), situando la mediana de reducción agregada en 82,4 %.'
    new_pi3_21 = '2.1. Aceleración Operativa y Reducción del Tiempo de Ciclo (Mejora Favorable +1): Agrupa los 71 estudios (86,6 % de la evidencia comparativa; Tabla XIX, Fig. 8) donde las arquitecturas de IA superaron contundentemente al ingreso manual y al OCR basado en reglas, logrando una reducción mediana del 82,4 % en el tiempo de procesamiento documental (rango empírico: 60,0 % a 95,0 %) y disminuyendo drásticamente la tasa de retrabajo humano ante variaciones de diseño [3]–[7], [44], [55], [103], [127].'
    if old_pi3_21 in content:
        content = content.replace(old_pi3_21, new_pi3_21)
        print("Updated PI3 2.1 in main.md")

    # 7. PI4 Header
    old_pi4_hdr = '## 6. Mapeo de Tipologías Documentales y Sistemas Corporativos ERP/CRM (PI4: ¿En qué tipologías documentales y arquitecturas de sistemas empresariales ERP/CRM se han validado las propuestas?)'
    new_pi4_hdr = '## 6. I. Tipologías Documentales y Validación en Sistemas ERP/CRM (PI4: ¿En qué tipologías documentales y sistemas empresariales ERP/CRM se han validado empíricamente los modelos?)'
    if old_pi4_hdr in content:
        content = content.replace(old_pi4_hdr, new_pi4_hdr)
        print("Updated PI4 Header in main.md")

    # 8. PI4 Opening paragraph
    old_pi4_open = 'Para determinar qué tipologías documentales y qué plataformas empresariales de gestión han sido abordadas en la literatura, se ejecutó un mapeo temático matricial sobre la totalidad del corpus primario (**$N = 131$ estudios**, 100,0 % de cobertura). La categorización documental y el mapeo hacia plataformas corporativas evaluada por doble codificación ciega sobre la muestra del 20,6 % ($n = 27$ estudios) reportó un coeficiente Kappa de Cohen **$\\kappa = 0,87$** ($P_o = 92.6\\,\\%$, $P_e = 0,430$), certificando la consistencia taxonómica de la matriz de integración bajo el protocolo formal de extracción y síntesis temática. La matriz cruzada se documenta en la Tabla XX y la matriz de calor (heatmap) se expone en la Fig. 9.'
    new_pi4_open = 'Para determinar la aplicabilidad corporativa real de los modelos (PI4), se clasificó el universo completo del corpus (N = 131) cruzando las cuatro tipologías documentales de negocio frente a su nivel de integración técnica con plataformas empresariales ERP, CRM y DMS. La distribución cuantitativa se detalla en la Tabla XX y se representa en la matriz de calor de la Fig. 9.'
    if old_pi4_open in content:
        content = content.replace(old_pi4_open, new_pi4_open)
        print("Updated PI4 Opening paragraph in main.md")

    # 9. PI4 Table XX Footer
    old_t20_footer_part = 'Nivel de integración real del corpus ($N = 131$): 103 estudios ($78.6\,\%$) corresponden a extracción algorítmica aislada'
    new_t20_footer = '*Nota: La columna de sistema corporativo describe el mapeo funcional conceptual hacia el que se orienta cada tipología. Nivel de integración real del corpus (N = 131): 103 estudios (78,6 %) evalúan modelos en entornos aislados sin conectores empresariales; 20 estudios (15,3 %) generan salidas estructuradas intermedias (JSON/CSV/XML) listas para ingesta; y únicamente 8 estudios (6,1 %; [28], [44], [54], [62], [64], [97], [127], [133]) validan integración transaccional activa con sistemas ERP/contables productivos.*'
    
    t20_pos = content.find('TABLA XX')
    if t20_pos != -1:
        f_start = content.find('*Fuente: elaboración propia', t20_pos)
        f_end = content.find('![Fig. 9', f_start)
        if f_start != -1 and f_end != -1:
            content = content[:f_start] + new_t20_footer + '\n\n' + content[f_end:]
            print("Updated Table XX footer in main.md")

    # 10. PI4 Fig 9 caption
    old_fig9 = '*Fig. 9. Mapeo cruzado de tipologías documentales frente a sistemas corporativos destino (PI4, N = 131). Intensidad de color proporcional al número de estudios mapeados. Fuente: elaboración propia a partir del corpus primario [3]–[133].*'
    new_fig9 = '*Fig. 9. Matriz de calor (heatmap) de tipologías documentales empresariales frente al nivel de integración en sistemas ERP/CRM/DMS (PI4, N = 131).*'
    if old_fig9 in content:
        content = content.replace(old_fig9, new_fig9)
        print("Updated Fig 9 caption in main.md")

    # 11. PI4 Bloque 1 - Apertura
    old_pi4_apertura_start = content.find('#### Bloque 1 — Apertura\nCiento treinta y un artículos (100,0 % del corpus; TABLA XX, Fig. 9)')
    if old_pi4_apertura_start != -1:
        end_pi4_apertura = content.find('#### Bloque 2', old_pi4_apertura_start)
        new_pi4_apertura = '#### Bloque 1 — Apertura\n1) Apertura: Ciento treinta y un estudios (100,0 % del corpus; TABLA XX, Fig. 9) se mapearon en torno a las tipologías documentales corporativas y su integración sistémica (PI4). El núcleo contable conformado por balances/tablas matriciales (45,0 %, n = 59) y facturas comerciales (26,0 %, n = 34) concentra el 71,0 % de la investigación global (58,0 % estricto al considerar únicamente las 42 tablas financieras específicas más las 34 facturas). No obstante, se evidencia una marcada asimetría entre el reconocimiento documental y el despliegue en ingeniería de software: mientras que en PD3 se identificaron 8 casos de estudio corporativos a nivel de diseño metodológico ([64], [70], [75], [84], [103], [117], [127], [131]), en PI4 solo 8 investigaciones implementaron integración técnica transaccional activa con plataformas ERP ([28], [44], [54], [62], [64], [97], [127], [133]), convergiendo ambas dimensiones exclusivamente en dos estudios ([64], [127]).\n\n'
        content = content[:old_pi4_apertura_start] + new_pi4_apertura + content[end_pi4_apertura:]
        print("Updated PI4 Apertura in main.md")

    # Clean up duplicate appendix at the end if present
    dup_app = '## Apéndice: Material Suplementario y Clasificación del Corpus\n\n### A. Clasificación Metodológica y Datasets (PD3 — Tabla XV)'
    if dup_app in content:
        dup_idx = content.find(dup_app)
        content = content[:dup_idx].rstrip() + '\n'
        print("Removed duplicate appendix block at end of main.md")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Saved main.md successfully.")

if __name__ == '__main__':
    sync_markdown()

