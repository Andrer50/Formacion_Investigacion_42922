import docx

def surgical_repair(doc_path):
    print(f"\n==========================================")
    print(f"SURGICAL REPAIR ON: {doc_path}")
    print(f"==========================================")
    doc = docx.Document(doc_path)

    # 1. Section I-B (Planteamiento del Problema) -> Point 3
    for p in doc.paragraphs:
        if p.text.startswith("3) Aislamiento Transaccional") or p.text.startswith("3) Brecha de Integración Transaccional"):
            p.text = ""
            r0 = p.add_run("3) Brecha de Integración Transaccional con Sistemas ERP/CRM: ")
            r0.bold = True
            r1 = p.add_run("La mayoría de las propuestas algorítmicas limita su alcance a la extracción visual de entidades en formatos intermedios (JSON/CSV) en entornos aislados de laboratorio, careciendo de conectores transaccionales activos, validación fiscal de tres vías (Three-Way Matching) y mecanismos de control de alucinaciones contables requeridos por sistemas ERP productivos como SAP S/4HANA, Oracle Financials o Microsoft Dynamics [28], [64], [112], [127].")
            r1.bold = False
            print("[PASS] 1. Sec I-B Point 3 updated.")
            break

    # 2. Section III-F (PI1)
    for i, p in enumerate(doc.paragraphs):
        # We find PI1's TABLA XVII footer, Fig 6, 1) Apertura, 2.1
        if "Partición temática unívoca auditada y verificada" in p.text or ("TABLA XVII" not in p.text and p.text.startswith("Fuente: elaboración propia a partir del corpus primario [3]–[133]. Síntesis temática")):
            p.text = "Fuente: elaboración propia a partir del corpus primario [3]–[133]. Síntesis temática según Thomas & Harden [134] y Cruzes & Dybå [135]. Acuerdo inter-evaluador κ = 0,88. Nota: Las listas completas de estudios por familia algorítmica se documentan en el Material Suplementario (Apéndice)."
            print("[PASS] 2. TABLA XVII footer updated.")
        elif p.text.startswith("Fig. 6."):
            p.text = "Fig. 6. Distribución de estudios por familia algorítmica de IA en procesamiento documental (Síntesis Temática, PI1, n = 105)."
            print("[PASS] 2. Fig. 6 caption updated.")
        elif p.text.startswith("1) Apertura: Ciento cinco estudios primarios"):
            p.text = ""
            r0 = p.add_run("1) Apertura: ")
            r0.bold = True
            r1 = p.add_run("Ciento cinco estudios primarios (80,2 % del corpus; TABLA XVII, Fig. 6) especificaron arquitecturas algorítmicas reproducibles de IA para el procesamiento de documentos empresariales (PI1), estructurándose en cuatro familias tecnológicas principales.")
            r1.bold = False
            print("[PASS] 2. PI1 1) Apertura updated.")
        elif p.text.startswith("2.1. Canalizaciones Híbridas"):
            p.text = ""
            r0 = p.add_run("2.1. Canalizaciones Híbridas (Pipelines) CNN-RNN y Segmentación Clásica con OCR: ")
            r0.bold = True
            r1 = p.add_run("Constituye la familia predominante del corpus con el 53,3 % de las implementaciones (56 de 105 estudios; Tabla XVII). Combina redes convolucionales (ResNet, VGG, YOLO, Mask R-CNN) para la detección espacial de regiones y tablas con redes recurrentes (BiLSTM) y motores OCR para la transcripción secuencial de texto [5], [10], [11], [59], [71], [103]. Su vigencia responde a su bajo costo computacional en CPU y alta interpretabilidad modular.")
            r1.bold = False
            print("[PASS] 2. PI1 2.1 updated.")

    # 3. Section III-G (PI2) 2.4
    for p in doc.paragraphs:
        if p.text.startswith("2.4. Flujos Corporativos Integrados"):
            p.text = ""
            r0 = p.add_run("2.4. Flujos Corporativos Integrados y Lotes Heterogéneos: ")
            r0.bold = True
            r1 = p.add_run("Comprende el subconjunto de 6 estudios (5,1 % de PI2; Tabla XVIII) que evaluaron canalizaciones completas sobre lotes continuos de documentos empresariales multiformato, alcanzando una mediana de exactitud/F1 del 90,1 % (rango: 82,0 % – 94,5 %) con latencias de inferencia de 300 ms a 1 800 ms por página [32], [78], [85], [93], [110], [111].")
            r1.bold = False
            print("[PASS] 3. PI2 2.4 updated.")
            break

    # 4. Section III-H (PI3) 2.1
    for p in doc.paragraphs:
        if p.text.startswith("2.1. Reducción del Tiempo") or p.text.startswith("2.1. Aceleración Operativa"):
            p.text = ""
            r0 = p.add_run("2.1. Aceleración Operativa y Reducción del Tiempo de Ciclo (Mejora Favorable +1): ")
            r0.bold = True
            r1 = p.add_run("Agrupa los 71 estudios (86,6 % de la evidencia comparativa; Tabla XIX, Fig. 8) donde las arquitecturas de IA superaron contundentemente al ingreso manual y al OCR basado en reglas, logrando una reducción mediana del 82,4 % en el tiempo de procesamiento documental (rango empírico: 60,0 % a 95,0 %) y disminuyendo drásticamente la tasa de retrabajo humano ante variaciones de diseño [3]–[7], [44], [55], [103], [127].")
            r1.bold = False
            print("[PASS] 4. PI3 2.1 updated.")
            break

    # 5. Section III-I (PI4)
    for i, p in enumerate(doc.paragraphs):
        if p.text.startswith("I. Mapeo de Tipologías Documentales") or p.text.startswith("I. Tipologías Documentales"):
            p.text = "I. Tipologías Documentales y Validación en Sistemas ERP/CRM (PI4: ¿En qué tipologías documentales y sistemas empresariales ERP/CRM se han validado empíricamente los modelos?)"
            print("[PASS] 5A. PI4 Heading updated.")
            # Intro paragraph is next
            if i + 1 < len(doc.paragraphs):
                doc.paragraphs[i+1].text = "Para determinar la aplicabilidad corporativa real de los modelos (PI4), se clasificó el universo completo del corpus (N = 131) cruzando las cuatro tipologías documentales de negocio frente a su nivel de integración técnica con plataformas empresariales ERP, CRM y DMS. La distribución cuantitativa se detalla en la Tabla XX y se representa en la matriz de calor de la Fig. 9."
                print("[PASS] 5A. PI4 Intro paragraph updated.")
        elif p.text.startswith("Fuente: elaboración propia a partir del corpus primario [3]–[133]. *Nota: De los 59") or p.text.startswith("*Nota: La columna de sistema corporativo"):
            p.text = "*Nota: La columna de sistema corporativo describe el mapeo funcional conceptual hacia el que se orienta cada tipología. Nivel de integración real del corpus (N = 131): 103 estudios (78,6 %) evalúan modelos en entornos aislados sin conectores empresariales; 20 estudios (15,3 %) generan salidas estructuradas intermedias (JSON/CSV/XML) listas para ingesta; y únicamente 8 estudios (6,1 %; [28], [44], [54], [62], [64], [97], [127], [133]) validan integración transaccional activa con sistemas ERP/contables productivos."
            print("[PASS] 5B. TABLA XX footer updated.")
        elif p.text.startswith("Fig. 9."):
            p.text = "Fig. 9. Matriz de calor (heatmap) de tipologías documentales empresariales frente al nivel de integración en sistemas ERP/CRM/DMS (PI4, N = 131)."
            print("[PASS] 5B. Fig. 9 caption updated.")
        elif p.text.startswith("1) Apertura: Ciento treinta y un"):
            p.text = ""
            r0 = p.add_run("1) Apertura: ")
            r0.bold = True
            r1 = p.add_run("Ciento treinta y un estudios (100,0 % del corpus; TABLA XX, Fig. 9) se mapearon en torno a las tipologías documentales corporativas y su integración sistémica (PI4). El núcleo contable conformado por balances/tablas matriciales (45,0 %, n = 59) y facturas comerciales (26,0 %, n = 34) concentra el 71,0 % de la investigación global (58,0 % estricto al considerar únicamente las 42 tablas financieras específicas más las 34 facturas). No obstante, se evidencia una marcada asimetría entre el reconocimiento documental y el despliegue en ingeniería de software: mientras que en PD3 se identificaron 8 casos de estudio corporativos a nivel de diseño metodológico ([64], [70], [75], [84], [103], [117], [127], [131]), en PI4 solo 8 investigaciones implementaron integración técnica transaccional activa con plataformas ERP ([28], [44], [54], [62], [64], [97], [127], [133]), convergiendo ambas dimensiones exclusivamente en dos estudios ([64], [127]).")
            r1.bold = False
            print("[PASS] 5B. PI4 1) Apertura updated.")

    # 6. Section IV (DISCUSIÓN) Subapartado B
    for i, p in enumerate(doc.paragraphs):
        if p.text.startswith("B. Brecha de Transferencia"):
            p.text = "B. Brecha de Transferencia Industrial y Desconexión Transaccional con Sistemas ERP"
            print("[PASS] 6. Sec IV Subapartado B Heading updated.")
            if i + 1 < len(doc.paragraphs):
                doc.paragraphs[i+1].text = "Un segundo hallazgo estructural de esta revisión es la desconexión entre la investigación en visión computacional y la ingeniería de sistemas empresariales. Aunque el 71,0 % del corpus aborda documentos contables críticos orientados conceptualmente a módulos financieros y de cuentas por pagar (Tabla XX), el 78,6 % de los estudios (103 de 131) finaliza su flujo experimental en la predicción de etiquetas o archivos JSON locales, sin abordar la interoperabilidad transaccional. Como demostró el cruce entre el mapeo de Petersen (PD3) y el análisis de integración técnica (PI4), solo 8 estudios validaron conectores activos con sistemas ERP ([28], [44], [54], [62], [64], [97], [127], [133]) y únicamente dos investigaciones ([64], [127]) articularon simultáneamente un diseño de caso de estudio corporativo real con integración productiva en el ERP. Esto confirma que la principal barrera para la adopción industrial del IDP ya no radica en el reconocimiento óptico aislado, sino en la orquestación de reglas de negocio, conciliación tributaria de tres vías (Three-Way Matching), gobernanza de privacidad on-premise ([116], [127]) y mitigación de alucinaciones numéricas antes del asiento contable definitivo ([4], [37])."
                print("[PASS] 6. Sec IV Subapartado B text updated.")
            break

    doc.save(doc_path)
    print(f"[SAVED] {doc_path} successfully saved.")

if __name__ == '__main__':
    surgical_repair('project/shared/RSL_Sergio_Rupay.docx')
    surgical_repair('project/resultados/Articulo_RSL_Resultados_Completo_IEEE.docx')

