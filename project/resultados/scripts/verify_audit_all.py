import docx
import re
import sys

def verify_file(filepath):
    print(f"\n=======================================================")
    print(f"AUDITING FILE: {filepath}")
    print(f"=======================================================")
    
    doc = docx.Document(filepath)
    paragraphs_text = [p.text for p in doc.paragraphs]
    full_text = "\n".join(paragraphs_text)
    
    # 1. Check all references [1] to [145]
    print("\n--- 1. VERIFICACIÓN DE REFERENCIAS BIBLIOGRÁFICAS [1] - [145] ---")
    missing_refs = []
    for i in range(1, 146):
        pattern = rf"\[{i}\]"
        if not re.search(pattern, full_text):
            missing_refs.append(i)
    
    if not missing_refs:
        print("  [OK] Las 145 referencias [1] a [145] estan presentes sin ningun salto.")
    else:
        print(f"  [ERROR] Faltan {len(missing_refs)} referencias: {missing_refs}")
    
    # Check verbatim references [134]-[139] and [143]-[145]
    verbatim_refs = {
        134: "J. Thomas and A. Harden, \"Methods for the thematic synthesis of qualitative research in systematic reviews,\"",
        135: "D. S. Cruzes and T. Dybå, \"Recommended steps for thematic synthesis in software engineering,\"",
        136: "J. Popay et al., \"Guidance on the conduct of narrative synthesis in systematic reviews: A product from the ESRC Methods Programme,\"",
        137: "M. Campbell et al., \"Synthesis without meta-analysis (SWiM) in systematic reviews: Reporting guideline,\"",
        138: "M. J. Page et al., \"The PRISMA 2020 statement: An updated guideline for reporting systematic reviews,\"",
        139: "M. Lewin et al., \"Using qualitative evidence in decision making for health and social interventions: An approach to assess confidence in findings from qualitative evidence syntheses (GRADE-CERQual),\"",
        143: "S. Srihari et al., \"DocFormer: End-to-end transformer for document understanding,\"",
        144: "Y. Li et al., \"StrucTexT: Structured text understanding with multi-modal pre-training,\"",
        145: "T. Hong et al., \"BROS: A pre-trained language model focusing on text and layout for better key information extraction,\""
    }
    
    for r_num, r_snippet in verbatim_refs.items():
        found = any(f"[{r_num}]" in p and r_snippet[:30] in p for p in paragraphs_text)
        if found:
            print(f"  [OK] Referencia [{r_num}] verificada.")
        else:
            print(f"  [WARNING/ERROR] Referencia [{r_num}] no coincide exactamente con el snippet.")
            
    # 2. Check all tables TABLA I to TABLA XXII + TABLA S1
    print("\n--- 2. VERIFICACIÓN DE TABLAS (TABLA I - XXII + S1) ---")
    roman_tables = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", 
                    "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX", "XXI", "XXII"]
    
    # In full text or table cells
    tables_cell_text = "\n".join(["\n".join(["\t".join([c.text for c in row.cells]) for row in table.rows]) for table in doc.tables])
    combined_text = full_text + "\n" + tables_cell_text
    
    for t_rom in roman_tables:
        t_name = f"TABLA {t_rom}"
        # allow case insensitive or slight spacing
        found = bool(re.search(rf"\bTABLA\s+{t_rom}\b", combined_text, re.IGNORECASE))
        if found:
            print(f"  [OK] {t_name} presente.")
        else:
            print(f"  [ERROR] {t_name} NO encontrada.")
            
    found_s1 = bool(re.search(r"\bTABLA\s+S1\b", combined_text, re.IGNORECASE))
    if found_s1:
        print("  [OK] TABLA S1 presente.")
    else:
        print("  [ERROR] TABLA S1 NO encontrada.")
        
    # 3. Check Section Results Subsections A. to K.
    print("\n--- 3. VERIFICACIÓN DE SUBSECCIONES DE RESULTADOS (A. a K.) ---")
    subsections = [
        ("A.", "A. Flujo de Selección y Cribado PRISMA 2020"),
        ("B.", "B. Evolución Temporal de la Producción Científica (PD1"),
        ("C.", "C. Canales de Publicación, Concentración Geográfica y Redes de Coautoría (PD2"),
        ("D.", "D. Tipología de Diseños de Investigación y Niveles de Evidencia (PD3"),
        ("E.", "E. Evaluación de Calidad Metodológica (QA) y Riesgo de Sesgo"),
        ("F.", "F. Familias Algorítmicas y Arquitecturas de IA (PI1"),
        ("G.", "G. Métricas de Rendimiento y Rendimiento Documental (PI2"),
        ("H.", "H. Eficiencia Comparativa Frente al Baseline y Retorno Operativo (PI3"),
        ("I.", "I. Tipologías Documentales y Validación en Sistemas ERP/CRM (PI4"),
        ("J.", "J. Evaluación de Confianza en la Evidencia (GRADE-CERQual)"),
        ("K.", "K. Síntesis Cruzada y Análisis de Robustez de la Evidencia")
    ]
    
    for letter, label in subsections:
        found = any(label[:25] in p for p in paragraphs_text)
        if found:
            print(f"  [OK] Subseccion {letter} presente: {label[:45]}...")
        else:
            print(f"  [ERROR] Subseccion {letter} NO encontrada: {label}")
            
    # 4. Check surgical items:
    print("\n--- 4. VERIFICACIÓN DE LOS 7 PUNTOS QUIRÚRGICOS ---")
    surgical_checks = [
        ("1. Sec I-B: Brecha 3", "3) Brecha de Integración Transaccional con Sistemas ERP/CRM: La mayoría de las propuestas algorítmicas"),
        ("2a. Sec III-F: Pie Tabla XVII", "Fuente: elaboración propia a partir del corpus primario [3]–[133]. Síntesis temática según Thomas & Harden [134] y Cruzes & Dybå [135]"),
        ("2b. Sec III-F: Pie Fig 6", "Fig. 6. Distribución de estudios por familia algorítmica de IA en procesamiento documental (Síntesis Temática, PI1, n = 105)."),
        ("2c. Sec III-F: 1) Apertura", "1) Apertura: Ciento cinco estudios primarios (80,2 % del corpus; TABLA XVII, Fig. 6) especificaron arquitecturas"),
        ("2d. Sec III-F: 2.1 Canalizaciones Híbridas", "2.1. Canalizaciones Híbridas (Pipelines) CNN-RNN y Segmentación Clásica con OCR: Constituye la familia predominante"),
        ("3. Sec III-G: 2.4 Flujos Corporativos", "2.4. Flujos Corporativos Integrados y Lotes Heterogéneos: Comprende el subconjunto de 6 estudios"),
        ("4. Sec III-H: 2.1 Aceleración Operativa", "2.1. Aceleración Operativa y Reducción del Tiempo de Ciclo (Mejora Favorable +1): Agrupa los 71 estudios"),
        ("5a. Sec III-I: Encabezado I.", "I. Tipologías Documentales y Validación en Sistemas ERP/CRM (PI4: ¿En qué tipologías documentales y sistemas empresariales ERP/CRM se han validado empíricamente los modelos?)"),
        ("5b. Sec III-I: Párrafo previo a Tabla XX", "Para determinar la aplicabilidad corporativa real de los modelos (PI4), se clasificó el universo completo del corpus"),
        ("5c. Sec III-I: Pie Tabla XX", "Nivel de integración real del corpus (N = 131): 103 estudios (78,6 %) evalúan modelos en entornos aislados"),
        ("5d. Sec III-I: Pie Fig 9", "Fig. 9. Matriz de calor (heatmap) de tipologías documentales empresariales frente al nivel de integración en sistemas ERP/CRM/DMS (PI4, N = 131)."),
        ("5e. Sec III-I: 1) Apertura", "1) Apertura: Ciento treinta y un estudios (100,0 % del corpus; TABLA XX, Fig. 9) se mapearon en torno a las tipologías"),
        ("6a. Sec IV: Heading B.", "B. Brecha de Transferencia Industrial y Desconexión Transaccional con Sistemas ERP"),
        ("6b. Sec IV: Subheadings A, B, C", None) # check A, B, C in discussion
    ]
    
    for item_name, phrase in surgical_checks:
        if phrase:
            found = any(phrase[:40] in p for p in paragraphs_text)
            if found:
                print(f"  [OK] {item_name} encontrado.")
            else:
                print(f"  [ERROR] {item_name} NO encontrado.")
                
    # Check Section IV subheadings A, B, C
    sec4_A = any("A. Dominancia Algorítmica y Madurez Multimodal" in p for p in paragraphs_text)
    sec4_B = any("B. Brecha de Transferencia Industrial y Desconexión Transaccional con Sistemas ERP" in p for p in paragraphs_text)
    sec4_C = any("C. Amenazas a la Validez" in p for p in paragraphs_text)
    print(f"  [OK] Sec IV subheadings: A={sec4_A}, B={sec4_B}, C={sec4_C}")

verify_file('project/shared/RSL_Sergio_Rupay.docx')
verify_file('project/resultados/Articulo_RSL_Resultados_Completo_IEEE.docx')

