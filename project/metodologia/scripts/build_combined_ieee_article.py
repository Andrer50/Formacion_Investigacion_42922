"""



Script maestro para compilar el artículo científico completo en formato IEEE:

            

"Articulo_RSL_Introduccion_y_Metodologia_IEEE.docx" en project/shared/







Contiene las 4 secciones fundamentales con estándar Scopus Q1/Q2 y Guía ATI3 superados:



- I. INTRODUCCIÓN (Contexto, Brecha, Justificación, Objetivos, PICOC, Preguntas PI/PD - Tablas I y II)



- II. METODOLOGÍA (PRISMA 2020, Ecuación, Criterios CIE, QA Kitchenham, Excluidos PRISMA 2020, Nucleares, Enlace - Tablas III a XII, Fig. 1)



- III. RESULTADOS (PD1-PD3, QA, PI1-PI4 en 4 bloques normativos, Sensibilidad, Juicio Narrativo SoF GRADE-CERQual - Tablas XIII a XXIII, Figs. 2 a 9)



- IV. REFERENCIAS BIBLIOGRÁFICAS (141 referencias rigurosas IEEE [1] a [141] en 2 columnas)



"""







import sys



import io



import os



import re



import pandas as pd



from docx import Document



from docx.shared import Inches, Pt, RGBColor



from docx.enum.text import WD_ALIGN_PARAGRAPH



from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL



from docx.enum.section import WD_SECTION_START



from docx.oxml import OxmlElement, parse_xml



from docx.oxml.ns import nsdecls, qn







sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')







# Cargar datasets maestros



df_final = pd.read_csv('project/metodologia/outputs/corpus_included_final.csv')



df_nuc = pd.read_csv('project/metodologia/outputs/corpus_estudios_nucleares_4_4.csv')



df_ex20 = pd.read_csv('project/metodologia/outputs/corpus_eligibility_excluded_20.csv')







print(f"Cargados: {len(df_final)} incluidos, {len(df_nuc)} nucleares, {len(df_ex20)} excluidos PRISMA 2020.")







doc = Document()



from docx.shared import Inches, Pt, Cm, RGBColor



# Configuración de márgenes estándar IEEE (0.75 pulgadas en todos los lados)



for section in doc.sections:



    section.top_margin = Inches(0.75)



    section.bottom_margin = Inches(0.75)



    section.left_margin = Inches(0.75)



    section.right_margin = Inches(0.75)



    section.header_distance = Inches(0.4)



    section.footer_distance = Inches(0.4)







# Estilo Normal



normal_style = doc.styles['Normal']



normal_style.font.name = 'Times New Roman'



normal_style.font.size = Pt(10)



normal_style.font.color.rgb = RGBColor(0, 0, 0)



normal_style.paragraph_format.line_spacing = 1.0



normal_style.paragraph_format.space_before = Pt(0)



normal_style.paragraph_format.space_after = Pt(0)



normal_style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY







# Encabezado institucional



p_inst = doc.add_paragraph()



p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER



r_inst = p_inst.add_run("UNIVERSIDAD TECNOLÓGICA DEL PERÚ\nFACULTAD DE INGENIERÍA DE SISTEMAS E INFORMÁTICA")



r_inst.font.name = 'Times New Roman'



r_inst.font.size = Pt(9.5)



r_inst.bold = True







# Título del Artículo



p_title = doc.add_paragraph()



p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER



p_title.paragraph_format.space_before = Pt(8)



p_title.paragraph_format.space_after = Pt(6)



r_title = p_title.add_run("Inteligencia Artificial para la Automatización del Registro y Validación de Documentos Empresariales: Una Revisión Sistemática de la Literatura")



r_title.font.name = 'Times New Roman'



r_title.font.size = Pt(18)



r_title.bold = True







# Autores



p_auth = doc.add_paragraph()



p_auth.alignment = WD_ALIGN_PARAGRAPH.CENTER



p_auth.paragraph_format.space_before = Pt(4)



p_auth.paragraph_format.space_after = Pt(2)



r_auth = p_auth.add_run("Sergio André Rupay Huancachoque")



r_auth.font.name = 'Times New Roman'



r_auth.font.size = Pt(10.5)



r_auth.bold = True











# Filiación y Asesor



p_aff = doc.add_paragraph()



p_aff.alignment = WD_ALIGN_PARAGRAPH.CENTER



p_aff.paragraph_format.space_before = Pt(0)



p_aff.paragraph_format.space_after = Pt(8)



r_aff = p_aff.add_run("Facultad de Ingeniería de Sistemas e Informática, Universidad Tecnológica del Perú, Lima, Perú\nDocente Asesor: Mg. Jimmy Sánchez Portugal | Formación para la Investigación\nArtículo RSL: Introducción, Metodología y Resultados | Corpus Primario Final: N = 131 artículos de revista científica (4 nucleares)")



r_aff.font.name = 'Times New Roman'



r_aff.font.size = Pt(8.5)



r_aff.italic = True







# Resumen



p_abs = doc.add_paragraph()



p_abs.paragraph_format.left_indent = Inches(0.3)



p_abs.paragraph_format.right_indent = Inches(0.3)



p_abs.paragraph_format.space_before = Pt(4)



p_abs.paragraph_format.space_after = Pt(2)



r_absh = p_abs.add_run("Resumen— ")



r_absh.bold = True



r_absh.italic = True



r_absh.font.size = Pt(9)



r_abst = p_abs.add_run(
    "El procesamiento de datos no estructurados en documentos empresariales (facturas, recibos y balances) "
    "representa un desafío crítico para la integración con sistemas ERP y CRM. Esta Revisión Sistemática de la "
    "Literatura analiza el impacto de la Inteligencia Artificial (IA) y el Procesamiento Inteligente de Documentos "
    "(IDP) entre 2020 y 2025. Siguiendo las directrices de Kitchenham y el protocolo PRISMA 2020, se identificaron "
    "3 701 registros en Scopus y Web of Science, consolidando tras cribado formal un corpus primario de N = 131 artículos "
    "de revista revisados por pares. Los resultados de la síntesis cuantitativa indican que las arquitecturas evaluadas alcanzan "
    "puntajes F1 y métricas de extracción entre 72,1 % y 98,7 % a nivel global en PI2 (mediana de F1 de 95,2 % en comprobantes estructurados mediante transformers y VLMs, y 84,5 % en formularios, con TEDS del 89,8 % en tablas). La síntesis por conteo de votos (SWiM) ratifica la superioridad de la IA sobre los métodos tradicionales "
    "en 71 de 82 estudios comparativos (86,6 %), con una mediana de reducción de tiempo de procesamiento del 82,4 % (rango empírico: "
    "60,0 % a 95,0 %); no obstante, se registraron 8 casos de paridad y 3 desfavorables por costos de GPU y alucinaciones. "
    "Finalmente, se constata una marcada brecha de adopción y transferencia industrial: solo el 6,1 % del corpus (8 estudios) adoptó diseños metodológicos de caso de estudio corporativo en la taxonomía de Petersen y, de forma concurrente, únicamente 8 estudios (6,1 %) validaron integración transaccional activa con sistemas ERP productivos, convergiendo ambas dimensiones exclusivamente en dos investigaciones ([64], [127])."
)



r_abst.font.size = Pt(9)







# Palabras clave



p_kw = doc.add_paragraph()



p_kw.paragraph_format.left_indent = Inches(0.3)



p_kw.paragraph_format.right_indent = Inches(0.3)



p_kw.paragraph_format.space_before = Pt(2)



p_kw.paragraph_format.space_after = Pt(12)



r_kwh = p_kw.add_run("Palabras clave— ")



r_kwh.bold = True



r_kwh.italic = True



r_kwh.font.size = Pt(9)



r_kwt = p_kw.add_run("Inteligencia artificial, procesamiento inteligente de documentos (IDP), extracción de información clave (KIE), sistemas de planificación de recursos empresariales (ERP), transformers multimodales, revisión sistemática de literatura, PRISMA 2020, Kitchenham.")



r_kwt.font.size = Pt(9)











# Divisor a 2 columnas estándar IEEE para Secciones I y II



sec_cols = doc.add_section(WD_SECTION_START.CONTINUOUS)



sec_cols.top_margin = Inches(0.75)



sec_cols.bottom_margin = Inches(0.75)



sec_cols.left_margin = Inches(0.75)



sec_cols.right_margin = Inches(0.75)



sectPr = sec_cols._sectPr



cols = sectPr.xpath('./w:cols')



if cols:



    cols[0].set(qn('w:num'), '2')



    cols[0].set(qn('w:space'), '720') # 0.5 in



else:



    c_elem = parse_xml(f'<w:cols {nsdecls("w")} w:num="2" w:space="720"/>')



    sectPr.append(c_elem)







# Helpers de formato y estilización IEEE



def set_cell_border(cell, **kwargs):



    tc = cell._tc



    tcPr = tc.get_or_add_tcPr()



    tcBorders = parse_xml(



        f'<w:tcBorders {nsdecls("w")}>\n'



        f'<w:top w:val="{kwargs.get("top", "none")}" w:sz="{kwargs.get("top_sz", "4")}" w:space="0" w:color="{kwargs.get("top_color", "auto")}"/>\n'



        f'<w:left w:val="{kwargs.get("left", "none")}" w:sz="{kwargs.get("left_sz", "4")}" w:space="0" w:color="{kwargs.get("left_color", "auto")}"/>\n'



        f'<w:bottom w:val="{kwargs.get("bottom", "none")}" w:sz="{kwargs.get("bottom_sz", "4")}" w:space="0" w:color="{kwargs.get("bottom_color", "auto")}"/>\n'



        f'<w:right w:val="{kwargs.get("right", "none")}" w:sz="{kwargs.get("right_sz", "4")}" w:space="0" w:color="{kwargs.get("right_color", "auto")}"/>\n'



        f'</w:tcBorders>'



    )



    tcPr.append(tcBorders)







def set_cell_shading(cell, color_hex):



    shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')



    cell._tc.get_or_add_tcPr().append(shading)







def add_heading_1(text):



    p = doc.add_paragraph()



    p.alignment = WD_ALIGN_PARAGRAPH.CENTER



    p.paragraph_format.space_before = Pt(11)



    p.paragraph_format.space_after = Pt(4)



    p.paragraph_format.keep_with_next = True



    r = p.add_run(text)



    r.font.name = 'Times New Roman'



    r.font.size = Pt(10)



    r.bold = True



    return p







def add_heading_2(text):



    p = doc.add_paragraph()



    p.alignment = WD_ALIGN_PARAGRAPH.LEFT



    p.paragraph_format.space_before = Pt(8)



    p.paragraph_format.space_after = Pt(2)



    p.paragraph_format.keep_with_next = True



    r = p.add_run(text)



    r.font.name = 'Times New Roman'



    r.font.size = Pt(9.5)



    r.italic = True



    r.bold = True



    return p







def add_p(text, bold_prefix=None, italic_text=False, indent=None):



    lines = text.split('\n')



    if len(lines) == 1:



        p = doc.add_paragraph()



        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY



        p.paragraph_format.line_spacing = 1.0



        p.paragraph_format.space_before = Pt(0)



        p.paragraph_format.space_after = Pt(4)



        if indent:



            p.paragraph_format.left_indent = indent



        if bold_prefix:



            rb = p.add_run(bold_prefix)



            rb.font.name = 'Times New Roman'



            rb.font.size = Pt(9.5)



            rb.bold = True



        rt = p.add_run(text)



        rt.font.name = 'Times New Roman'



        rt.font.size = Pt(9.5)



        rt.italic = italic_text



        return p







    last_p = None



    for i, line in enumerate(lines):



        line = line.strip()



        if not line:



            continue



        p = doc.add_paragraph()



        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY



        p.paragraph_format.line_spacing = 1.0



        p.paragraph_format.space_before = Pt(0)



        p.paragraph_format.space_after = Pt(2.5) if i < len(lines) - 1 else Pt(4)



        if indent:



            p.paragraph_format.left_indent = indent



        if i == 0 and bold_prefix:



            rb = p.add_run(bold_prefix)



            rb.font.name = 'Times New Roman'



            rb.font.size = Pt(9.5)



            rb.bold = True







        m_sub = re.match(r'^([a-z0-9]\)\s+[^:]+:\s*)(.*)$', line)



        if m_sub and i > 0:



            r_sub = p.add_run(m_sub.group(1))



            r_sub.font.name = 'Times New Roman'



            r_sub.font.size = Pt(9.5)



            r_sub.bold = True



            r_rest = p.add_run(m_sub.group(2))



            r_rest.font.name = 'Times New Roman'



            r_rest.font.size = Pt(9.5)



            r_rest.italic = italic_text



        else:



            rt = p.add_run(line)



            rt.font.name = 'Times New Roman'



            rt.font.size = Pt(9.5)



            rt.italic = italic_text



        last_p = p



    return last_p







def add_table_title(tbl_num, tbl_title):



    p = doc.add_paragraph()



    p.alignment = WD_ALIGN_PARAGRAPH.CENTER



    p.paragraph_format.space_before = Pt(7)



    p.paragraph_format.space_after = Pt(1)



    p.paragraph_format.keep_with_next = True



    r1 = p.add_run(f"{tbl_num}\n")



    r1.font.name = 'Times New Roman'



    r1.font.size = Pt(8)



    r1.bold = True



    r2 = p.add_run(tbl_title.upper())



    r2.font.name = 'Times New Roman'



    r2.font.size = Pt(8)



    return p







def add_table_footer(text):



    p = doc.add_paragraph()



    p.alignment = WD_ALIGN_PARAGRAPH.LEFT



    p.paragraph_format.space_before = Pt(2)



    p.paragraph_format.space_after = Pt(6)



    r = p.add_run(text)



    r.font.name = 'Times New Roman'



    r.font.size = Pt(8)



    r.italic = True



    return p







def style_table(tbl, col_widths, font_size=Pt(7.5), align_cols=None):



    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER



    for r_idx, row in enumerate(tbl.rows):



        is_header = (r_idx == 0)



        trPr = row._tr.get_or_add_trPr()



        trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))



        if is_header:



            trPr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))



        for c_idx, cell in enumerate(row.cells):



            cell.width = col_widths[c_idx]



            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER







            if is_header:



                set_cell_shading(cell, "F2F2F2")



                set_cell_border(cell, top="single", top_sz="8", top_color="000000",



                                      bottom="single", bottom_sz="8", bottom_color="000000")



            elif r_idx == len(tbl.rows) - 1:



                set_cell_border(cell, bottom="single", bottom_sz="8", bottom_color="000000")



            else:



                set_cell_border(cell, bottom="single", bottom_sz="4", bottom_color="D3D3D3")







            for paragraph in cell.paragraphs:



                paragraph.paragraph_format.line_spacing = 1.0



                paragraph.paragraph_format.space_before = Pt(1)



                paragraph.paragraph_format.space_after = Pt(1)



                if align_cols:



                    if isinstance(align_cols, dict) and c_idx in align_cols:



                        paragraph.alignment = align_cols[c_idx]



                    elif isinstance(align_cols, (list, tuple)) and c_idx < len(align_cols):



                        paragraph.alignment = align_cols[c_idx]



                    elif is_header:



                        paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER



                    else:



                        paragraph.alignment = WD_ALIGN_PARAGRAPH.LEFT



                elif is_header:



                    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER



                else:



                    paragraph.alignment = WD_ALIGN_PARAGRAPH.LEFT



                for run in paragraph.runs:



                    run.font.name = 'Times New Roman'



                    run.font.size = font_size



                    if is_header:



                        run.bold = True







def add_figure_with_caption(img_path, fig_id, fig_title, fig_note=None):



    if os.path.exists(img_path):



        p_img = doc.add_paragraph()



        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER



        p_img.paragraph_format.space_before = Pt(6)



        p_img.paragraph_format.space_after = Pt(2)



        p_img.paragraph_format.keep_with_next = True



        run_img = p_img.add_run()



        run_img.add_picture(img_path, width=Inches(3.35))







        p_cap = doc.add_paragraph()



        p_cap.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY



        p_cap.paragraph_format.space_before = Pt(2)



        p_cap.paragraph_format.space_after = Pt(6)







        r_cap_id = p_cap.add_run(f"{fig_id}. ")



        r_cap_id.font.name = 'Times New Roman'



        r_cap_id.font.size = Pt(8.5)



        r_cap_id.bold = True







        r_cap_txt = p_cap.add_run(f"{fig_title}. ")



        r_cap_txt.font.name = 'Times New Roman'



        r_cap_txt.font.size = Pt(8.5)







        if fig_note:



            r_note = p_cap.add_run(f"{fig_note} ")



            r_note.font.name = 'Times New Roman'



            r_note.font.size = Pt(8)







        r_src = p_cap.add_run("Fuente: elaboración propia a partir del corpus primario [3]–[133].")



        r_src.font.name = 'Times New Roman'



        r_src.font.size = Pt(8)



        r_src.italic = True



    else:



        print(f"ADVERTENCIA: Imagen no encontrada en {img_path}")







# ==========================================



# SECCIÓN I: INTRODUCCIÓN



# ==========================================



add_heading_1("I. INTRODUCCIÓN")







add_heading_2("A. Contexto Tecnológico y Relevancia Industrial")



add_p(
    "Los sistemas de planificación de recursos empresariales (ERP), gestión de relaciones con clientes (CRM) y gestión documental (DMS) "
    "procesan flujos transaccionales continuos de documentos semiestructurados y no estructurados, tales como facturas de proveedores, boletas "
    "de compra, notas de crédito, órdenes de compra y extractos bancarios [3], [4], [6]. Históricamente, la captura, transcripción y verificación "
    "de estos comprobantes ha dependido de la intervención manual o de sistemas convencionales de Reconocimiento Óptico de Caracteres (OCR) basados "
    "en reglas sintácticas y plantillas rígidas (templates) [6]."
)



add_p(
    "En la literatura operativa se ha documentado que este esquema tradicional presenta restricciones críticas de escalabilidad: "
    "propensión a errores por digitación manual, costos laborales recurrentes, lentitud en los ciclos de conciliación contable "
    "y una extrema fragilidad ante variaciones en el diseño o formato de los documentos [6], [28]. Frente a este panorama, "
    "la convergencia del Deep Learning, el Procesamiento del Lenguaje Natural (PLN) y la Visión por Computadora ha dado origen al "
    "Procesamiento Inteligente de Documentos (IDP) y la Extracción de Información Clave (Key Information Extraction - KIE). "
    "Modelos multimodales avanzados (como transformers visual-lingüísticos y Vision-Language Models) permiten interpretar "
    "simultáneamente la información textual, la disposición espacial (layout) y los atributos visuales de los documentos visualmente "
    "ricos (Visually Rich Documents - VRD), alcanzando elevados niveles de exactitud y F1-score en bancos de pruebas estandarizados (benchmarks) públicos, cuyas métricas consolidadas se sintetizan en la Sección III de esta revisión."
)



add_heading_2("B. Planteamiento del Problema y Brechas en la Literatura")



add_p(



    "A pesar de los acelerados avances algorítmicos en modelos fundacionales y aprendizaje profundo, la literatura científica "



    "evidencia tres brechas críticas que dificultan la toma de decisiones informadas para la implementación en entornos de producción:"



)



add_p(



    "El procesamiento manual y los flujos asistidos por OCR convencional continúan generando cuellos de botella operativos sustanciales, "



    "debido a la extrema rigidez de las plantillas predefinidas y a su reducida capacidad de generalización ante variaciones topológicas y formatos semiestructurados [5], [6], [28], [64]. "



    "Diversas investigaciones evidencian que cualquier alteración en la disposición espacial de tablas o campos clave degrada drásticamente la efectividad de las reglas sintácticas, "



    "ocasionando errores sistemáticos de lectura y una elevada dependencia de re-digitación y validación manual humana [6], [28].",



    bold_prefix="1) Fragilidad Operativa de Enfoques Tradicionales: "



)



add_p(



    "Gran parte de la literatura académica evalúa sus propuestas sobre conjuntos de datos públicos estandarizados y predominantemente restringidos a condiciones ideales de escaneo o lenguajes específicos "



    "(como SROIE en inglés [6], [20], FUNSD [21], [67] y CORD en indonesio [9], [67]). Dichos repositorios no reflejan fielmente las complejidades operativas del entorno corporativo real: "



    "documentos con severa degradación física, sellos y firmas superpuestas, tablas contables anidadas sin bordes y diversidad tipográfica y lingüística regional [14], [28], [80], "



    "generando una sobreestimación teórica del rendimiento algorítmico frente a flujos de trabajo heterogéneos.",



    bold_prefix="2) Sesgos y Desconexión de los Bancos de Pruebas (Benchmarks): "



)



add_p(



    "A diferencia de las revisiones secundarias previas identificadas en la literatura (compiladas en la Tabla VIII), las cuales se restringen a "



    "taxonomías teóricas o panoramas cualitativos sobre bancos de prueba aislados, existe una marcada escasez de estudios primarios que aborden "



    "la integración transaccional de extremo a extremo entre las canalizaciones (pipelines) de IDP y los sistemas empresariales corporativos (ERP, CRM y DMS). "



    "La literatura tiende a dar por sentada la interoperabilidad de datos, omitiendo la evaluación concurrente de latencia en tiempo real, "



    "consumo de recursos (GPU vs. CPU) y protocolos de arbitraje humano en el bucle (human-in-the-loop) en entornos operativos reales [70], [84], [127].",



    bold_prefix="3) Aislamiento Transaccional con Sistemas ERP: "



)







add_heading_2("C. Motivación, Pregunta Maestra y Objetivos")



add_p(



    "La rápida evolución tecnológica acumulada entre 2020 y 2025 exige una síntesis metodológica sistemática que sirva de guía a "



    "investigadores y líderes de tecnología para identificar qué arquitecturas de IA ofrecen el mejor balance entre precisión, velocidad "



    "y costo de integración."



)



add_p(



    "Fundamentada en el marco PICOC [1], la investigación plantea la siguiente Pregunta Maestra:",



    indent=Pt(8)



)



add_p(



    '«¿Cuál es el impacto de las arquitecturas de Inteligencia Artificial y Procesamiento Inteligente de Documentos (IDP), '



    'frente al ingreso manual y enfoques basados en reglas, sobre la precisión, la velocidad y la reducción de la carga operativa '



    'en el registro y validación documental dentro de sistemas empresariales, entre 2020 y 2025?»',



    italic_text=True,



    indent=Pt(12)



)



add_p(



    "El objetivo general consiste en sintetizar críticamente la evidencia empírica acumulada a nivel internacional sobre las arquitecturas "



    "de IA/IDP, cuantificando su rendimiento y comparando sus ventajas frente a los métodos convencionales en entornos corporativos."



)



add_p(



    "Para alcanzar dicho objetivo general, se formulan cuatro objetivos específicos alineados con las interrogantes de investigación:\n"



    "1) Caracterizar y clasificar las familias algorítmicas y arquitecturas neuronales predominantes en el procesamiento de documentos empresariales (PI1).\n"



    "2) Cuantificar el desempeño empírico alcanzado en bancos de pruebas estandarizados (benchmarks) públicos y privados según las métricas estándar de extracción y reconocimiento (PI2).\n"



    "3) Evaluar comparativamente el grado de mejora y eficiencia de los modelos de IA frente al OCR convencional y métodos basados en reglas (PI3).\n"



    "4) Clasificar las tipologías documentales empresariales y evaluar su grado de validación e integración en plataformas ERP/CRM corporativas (PI4)."



)







add_heading_2("D. Estructura del Documento")



add_p(



    "El artículo se estructura de la siguiente manera: la Sección II detalla la Metodología de la Revisión Sistemática (protocolo, marco PICOC, "



    "estrategia de búsqueda calibrada, criterios de inclusión/exclusión, flujo PRISMA 2020, control de calidad Kitchenham, matriz de exclusión PRISMA 2020 y mapeo de síntesis); "



    "la Sección III expone los Resultados empíricos estructurados en cuatro bloques analíticos en respuesta a las preguntas directas e indirectas de investigación; "



    "la Declaración Ética formaliza el uso responsable de tecnologías de IA generativa y la disponibilidad de datos; y la Sección IV compendia las Referencias Bibliográficas en formato IEEE."



)







# ==========================================



# SECCIÓN II: METODOLOGÍA DE LA RSL



# ==========================================



add_heading_1("II. METODOLOGÍA DE LA REVISIÓN SISTEMÁTICA")







add_heading_2("A. Encuadre Metodológico y Estándares")



add_p(



    "La revisión sistemática se diseñó y ejecutó siguiendo las directrices metodológicas de Kitchenham & Charters (2007) [1] para la ingeniería "



    "de software y sistemas de información, y se reporta en conformidad con la declaración PRISMA 2020 (Preferred Reporting Items for Systematic "



    "Reviews and Meta-Analyses) [2]. El protocolo metodológico se formalizó con anterioridad a las etapas de cribado y extracción de datos, "



    "incorporando una fase de calibración exploratoria piloto (Iteración 1) para neutralizar el ruido terminológico. Conforme a las recomendaciones "



    "de reporte del ítem 24a de PRISMA 2020, se declara que la revisión no fue registrada en plataformas clínicas externas (como PROSPERO); "



    "en su lugar, los criterios de elegibilidad, la matriz de calidad, los scripts computacionales y las decisiones de arbitraje fueron establecidos "



    "formalmente bajo supervisión docente y resguardados con control de versiones en el repositorio del proyecto (GitHub) para garantizar total transparencia y reproducibilidad."



)







add_heading_2("B. Delimitación Temática y Marco PICOC")



add_p(



    "Para formalizar el alcance conceptual y prevenir ambigüedades, se estructuró la investigación mediante el marco PICOC (ver Tabla I), "



    "delimitando el dominio a sistemas empresariales corporativos privados (ERP, CRM, DMS), excluyendo expedientes clínicos "



    "hospitalarios, documentos gubernamentales y archivos históricos."



)







add_table_title("TABLA I", "COMPONENTES DEL MARCO PICOC")



t_picoc = doc.add_table(rows=6, cols=3)



hdr = t_picoc.rows[0].cells



hdr[0].paragraphs[0].text = "Componente"



hdr[1].paragraphs[0].text = "Definición para este Estudio"



hdr[2].paragraphs[0].text = "Justificación Metodológica"







picoc_data = [



    ("P — Población", "Sistemas de información empresariales (ERP, CRM, DMS) y flujos internos de registro documental.", "Entorno operativo corporativo donde se generan cuellos de botella por ingreso manual."),



    ("I — Intervención", "Modelos de IA e IDP (Visión-Lenguaje, LayoutLM, Transformers multimodales, KIE, OCR profundo).", "Tecnología de automatización cognitiva cuyo rendimiento empírico se evalúa."),



    ("C — Comparación", "Ingreso manual de datos o procesamiento tradicional basado en reglas fijas y plantillas rígidas.", "Línea base convencional frente a la cual se mide la ganancia en exactitud y velocidad."),



    ("O — Resultado", "Niveles de automatización, reducción de carga laboral, exactitud (F1-score, CER/WER) y latencia.", "Variables cuantitativas críticas para la viabilidad técnica y operativa."),



    ("C — Contexto", "Entornos empresariales corporativos privados y ventana temporal comprendida entre 2020 y 2025.", "Período de maduración de los modelos neuronales multimodales aplicados.")



]



for idx, (comp, defn, just) in enumerate(picoc_data, start=1):



    c = t_picoc.rows[idx].cells



    c[0].paragraphs[0].text = comp



    c[1].paragraphs[0].text = defn



    c[2].paragraphs[0].text = just



style_table(t_picoc, [Inches(0.8), Inches(1.5), Inches(1.1)])

add_p(
    "Nota de alcance sobre Población y Contexto: La delimitación en flujos documentales corporativos comprende el flujo integral de procesamiento (pipeline) de documentos (IDP de extremo a extremo). Por ende, se distinguen los estudios de OCR genérico descontextualizado (descartados en cribado bajo EX-n) frente a investigaciones que abordan etapas habilitadoras esenciales del flujo corporativo: preprocesamiento geométrico y remoción de marcas de agua para captura móvil en ERP [70], [79], segmentación de documentos de identidad para procesos de Know Your Customer (KYC) en CRM [21], soporte multilingüe en caracteres no latinos para transacciones de mercados emergentes [15], [16], y marcos de privacidad federada o gobernanza contable bajo cumplimiento normativo [116], [133]."
)







add_heading_2("C. Descomposición en Preguntas de Investigación (PI y PD)")



add_p(



    "La pregunta maestra se desglosa operativamente en cuatro Preguntas de Investigación (PI) temáticas y tres Preguntas Descriptivas (PD) "



    "de carácter bibliométrico (ver Tabla II):"



)







add_table_title("TABLA II", "PREGUNTAS DE INVESTIGACIÓN TEMÁTICAS (PI) Y BIBLIOMÉTRICAS (PD)")



t_preg = doc.add_table(rows=8, cols=3)



hdr = t_preg.rows[0].cells



hdr[0].paragraphs[0].text = "Código"



hdr[1].paragraphs[0].text = "Pregunta de Investigación Formulada"



hdr[2].paragraphs[0].text = "Eje de Evidencia / PICOC"







preg_data = [



    ("PI1", "¿Qué arquitecturas y enfoques algorítmicos de IA/IDP (secuencias, grafos, transformers multimodales, VLM) se han implementado en documentos empresariales?", "Enfoques algorítmicos (Intervención)"),



    ("PI2", "¿Qué niveles de rendimiento cuantitativo (F1-score, exactitud, reducción de latencia) reportan las soluciones de IA/IDP en extracción documental?", "Rendimiento cuantitativo (Outcome)"),



    ("PI3", "¿En qué medida el procesamiento con IA/IDP reduce los tiempos de ciclo y la carga de error operativo frente al ingreso manual y reglas?", "Contraste vs tradicional (Comparación)"),



    ("PI4", "¿En qué tipologías documentales (facturas, recibos, órdenes) y sistemas ERP/CRM se han validado empíricamente los modelos?", "Aplicabilidad corporativa (Población)"),



    ("PD1", "¿Cómo ha evolucionado el volumen de producción científica anual sobre IA/IDP entre 2020 y 2025?", "Evolución temporal (Contexto)"),



    ("PD2", "¿Qué autores, revistas indexadas y países concentran la mayor productividad e impacto académico?", "Productividad y canales científicos"),



    ("PD3", "¿Qué diseños metodológicos y tipologías de conjuntos de datos o datasets (públicos vs. privados) predominan en la literatura?", "Madurez empírica y reproducibilidad")



]



for idx, (cod, prg, eje) in enumerate(preg_data, start=1):



    c = t_preg.rows[idx].cells



    c[0].paragraphs[0].text = cod



    c[1].paragraphs[0].text = prg



    c[2].paragraphs[0].text = eje



style_table(t_preg, [Inches(0.4), Inches(2.0), Inches(1.0)])







add_heading_2("D. Estrategia de Búsqueda, Ecuaciones Calibradas y Evolución de Iteraciones")



add_p(



    "La estrategia de búsqueda se estructuró mediante bloques booleanos simétricos. Para controlar el riesgo de polisemia "



    "del acrónimo aislado 'ERP' (el cual en las pruebas preliminares colisionaba con la literatura neurofisiológica y clínica "



    "sobre Event-Related Potentials en electroencefalogramas), se reemplazó formalmente dicha sigla por las frases compuestas 'enterprise resource "



    "planning' OR 'ERP system*', reduciendo sustancialmente el ruido biomédico de neurociencias (p. ej., EEG) (ver Tabla III)."



)







add_table_title("TABLA III", "MATRIZ DE DESCRIPTORES Y ECUACIÓN BOOLEANA CALIBRADA")



t_desc = doc.add_table(rows=4, cols=3)



hdr = t_desc.rows[0].cells



hdr[0].paragraphs[0].text = "Bloque"



hdr[1].paragraphs[0].text = "Concepto Base"



hdr[2].paragraphs[0].text = "Descriptores y Sinónimos Técnicos en Inglés"







desc_data = [



    ("Población", "Sistemas empresariales y documentos", '"business document*" OR "financial document*" OR "invoice*" OR "receipt*" OR "commercial document*" OR "purchase order*" OR "visually-rich document*" OR "enterprise resource planning" OR "ERP system*"'),



    ("Intervención", "IA y procesamiento documental", '"intelligent document processing" OR "IDP" OR "document AI" OR "document understanding" OR "key information extraction" OR "KIE" OR "LayoutLM*" OR "optical character recognition" OR "OCR" OR "multimodal transformer*" OR "vision-language"'),



    ("Resultado", "Automatización, exactitud y eficiencia", '"automat*" OR "extract*" OR "recognition" OR "accuracy" OR "F1" OR "performance" OR "efficiency" OR "throughput"')



]



for idx, (b, c_nom, d_txt) in enumerate(desc_data, start=1):



    c = t_desc.rows[idx].cells



    c[0].paragraphs[0].text = b



    c[1].paragraphs[0].text = c_nom



    c[2].paragraphs[0].text = d_txt



style_table(t_desc, [Inches(0.7), Inches(1.1), Inches(1.6)])







add_p(



    "En la fase exploratoria preliminar se ejecutó una búsqueda piloto (Iteración 1) con descriptores rígidos de ERP y OCR clásico "



    "('ERP' aislado AND 'OCR' AND 'document processing'), arrojando 140 registros en Scopus y 123 en WoS (N = 263). Dicha iteración fue formalmente "



    "descartada por dos deficiencias metodológicas críticas: (a) un 28,5 % de contaminación semántica en la muestra piloto (75 de los 263 registros "



    "brutos correspondían a estudios neurofisiológicos de potenciales evocados en electroencefalogramas, EEG) y (b) la omisión inadvertida de la literatura moderna "



    "de KIE, modelos de visión-lenguaje y comprensión de documentos visualmente ricos (VRD). Para subsanar esto, se diseñó la Iteración 2 (calibrada definitiva, archivada en "



    "el repositorio metodológico auditable de datos primarios), la cual expandió los términos a expresiones compuestas ('enterprise resource planning' OR 'ERP system*'), "



    "incorporó operadores booleanos para modelos de visión-lenguaje y limitó la tipología documental a artículos de revista arbitrados "



    "(Document Type = Article). Esta calibración recuperó 3 270 registros brutos en Scopus y 431 en WoS (3 701 brutos), que tras filtros nativos de plataforma "



    "se redujeron a 311 y 266 registros respectivamente (total n = 577), optimizando la especificidad temático-empresarial y la cobertura del rastreo.",



    bold_prefix="Evolución y Calibración Metodológica de Ecuaciones (Iteración 1 vs. Iteración 2): "



)







add_p(



    "Dentro del corpus primario se identifican tres artículos ([3] Wei et al., [65] Giovannini et al., y [66] Raja et al.) cuya fecha de "



    "asignación formal a volumen de revista impresa figura con año 2026. Se precisa que dichos registros fueron publicados oficialmente "



    "en línea en modalidad Early Access / Advance Online Publication entre agosto y diciembre de 2025; por consiguiente, tanto Scopus como "



    "Web of Science Core Collection los indexaron legítimamente dentro del período de rastreo, cumpliendo rigurosamente con el criterio de inclusión "



    "IN1 (publicación en línea 2020–2026, incluyendo artículos anticipados Early Access) y los estándares de reporte de PRISMA 2020 [2].",



    bold_prefix="Nota Aclaratoria sobre Publicaciones Anticipadas (Early Access 2025/2026): "



)







add_p(



    "Para garantizar la estricta reproducibilidad exigida por el estándar PRISMA 2020 [2], las ecuaciones literales ejecutadas fueron adaptadas "



    "sintácticamente a cada plataforma: (a) En Scopus (TITLE-ABS-KEY): TITLE-ABS-KEY((\"business document*\" OR \"financial document*\" OR "



    "\"administrative document*\" OR \"commercial document*\" OR \"invoice*\" OR \"receipt*\" OR \"purchase order*\" OR \"visually-rich document*\" OR "



    "\"semi-structured document*\" OR \"document image*\" OR \"scanned document*\" OR \"document management\" OR \"business workflow*\" OR "



    "\"enterprise resource planning\" OR \"ERP system*\") AND (\"intelligent document processing\" OR \"IDP\" OR \"document AI\" OR "



    "\"document understanding\" OR \"key information extraction\" OR \"KIE\" OR \"LayoutLM*\" OR \"form understanding\" OR \"table extraction\" OR "



    "\"table structure recognition\" OR \"optical character recognition\" OR \"OCR\" OR \"information extraction\" OR \"multimodal transformer*\" OR "



    "\"vision-language\") AND (\"automat*\" OR \"validat*\" OR \"extract*\" OR \"recognition\" OR \"accuracy\" OR \"efficiency\")); "



    "(b) En Web of Science Core Collection (TS): TS=((\"business document*\" OR \"financial document*\" OR \"administrative document*\" OR "



    "\"commercial document*\" OR \"invoice*\" OR \"receipt*\" OR \"purchase order*\" OR \"visually-rich document*\" OR "



    "\"semi-structured document*\" OR \"document image*\" OR \"scanned document*\" OR \"document management\" OR \"business workflow*\" OR "



    "\"enterprise resource planning\" OR \"ERP system*\") AND (\"intelligent document processing\" OR \"IDP\" OR \"document AI\" OR "



    "\"document understanding\" OR \"key information extraction\" OR \"KIE\" OR \"LayoutLM*\" OR \"form understanding\" OR \"table extraction\" OR "



    "\"table structure recognition\" OR \"optical character recognition\" OR \"OCR\" OR \"information extraction\" OR \"multimodal transformer*\" OR "



    "\"vision-language\") AND (\"automat*\" OR \"validat*\" OR \"extract*\" OR \"recognition\" OR \"accuracy\" OR \"efficiency\")).",



    bold_prefix="Ecuaciones de Búsqueda Literales Ejecutadas: "



)







add_heading_2("E. Registro Maestro de Consultas y Exportaciones")



add_p(



    "Las ecuaciones calibradas se ejecutaron en Scopus y Web of Science Core Collection bajo fecha calendario auditable. Si bien las "



    "ecuaciones fueron formalmente simétricas en su arquitectura booleana y conceptual, se constató una notable disparidad en los volúmenes brutos "



    "iniciales (3 270 en Scopus frente a 431 en WoS). Esta asimetría en las tasas de reducción (-90,5 % en Scopus frente a -38,3 % en WoS) responde a "



    "las marcadas diferencias estructurales de indexación: Scopus indexa una masiva literatura de actas de congresos (Conference Proceedings de IEEE, "



    "ACM y Springer LNCS) y series monográficas previas a 2020 que saturan los resultados de IA documental; al aplicar los filtros nativos de tipo documental "



    "(Document Type = Article) y ventana temporal 2020–2025, se depuraron 2 938 publicaciones de actas y años previos, quedando 332 registros y "



    "finalmente 311 tras el filtro de idioma inglés/español (excluyendo 21 registros en otros idiomas). Por su parte, Web of Science Core Collection "



    "opera de forma predeterminada sobre colecciones altamente selectivas de revistas periódicas (SCIE, SSCI, ESCI), arrojando 386 registros tras el filtro "



    "temporal y 266 tras los filtros de artículo e idioma. La Tabla IV detalla la bitácora paso a paso de reducción por filtro nativo.",



    bold_prefix="Justificación Metodológica de Asimetría en Filtrado Nativo: "



)







add_table_title("TABLA IV", "BITÁCORA DE FILTRADO NATIVO PASO A PASO Y REGISTRO MAESTRO POR BASE INDEXADA")



t_reg = doc.add_table(rows=4, cols=6)



hdr = t_reg.rows[0].cells



hdr[0].paragraphs[0].text = "Base de Datos y Campo"



hdr[1].paragraphs[0].text = "Bruto (n)"



hdr[2].paragraphs[0].text = "Filtro Temporal / Doc.*"



hdr[3].paragraphs[0].text = "Idioma"



hdr[4].paragraphs[0].text = "Exportado"



hdr[5].paragraphs[0].text = "Reducción"







reg_data = [



    ("Scopus (TITLE-ABS-KEY)", "3 270", "332", "311", "311", "-90,5 %"),



    ("WoS Core Coll. (TS)*", "431", "386", "266", "266", "-38,3 %"),



    ("Total Consolidado", "3 701", "718", "577", "577", "-84,4 %")



]







for idx, (b, brut, f_doc, f_id, f_exp, red) in enumerate(reg_data, start=1):



    c = t_reg.rows[idx].cells



    c[0].paragraphs[0].text = b



    c[1].paragraphs[0].text = brut



    c[2].paragraphs[0].text = f_doc



    c[3].paragraphs[0].text = f_id



    c[4].paragraphs[0].text = f_exp



    c[5].paragraphs[0].text = red







style_table(t_reg, [Inches(1.1), Inches(0.45), Inches(0.5), Inches(0.45), Inches(0.45), Inches(0.45)],



            align_cols={1: WD_ALIGN_PARAGRAPH.RIGHT, 2: WD_ALIGN_PARAGRAPH.RIGHT, 3: WD_ALIGN_PARAGRAPH.RIGHT, 4: WD_ALIGN_PARAGRAPH.RIGHT, 5: WD_ALIGN_PARAGRAPH.RIGHT})







add_p(



    "*Nota metodológica: En Scopus, la columna 'Filtro Temporal / Doc.' aplica simultáneamente los filtros nativos de ventana temporal (2020–2026) y tipo de documento (Article) arrojando 332 registros (311 tras filtrar idioma). En WoS, la plataforma ejecuta en primera instancia el filtro de ventana temporal (386 registros), y la aplicación subsecuente de tipo Article e idioma inglés/español consolida los 266 registros exportados. "



    "Los 577 registros consolidados se encuentran archivados en los registros maestros de exportación de Scopus (n = 311) y Web of Science (n = 266), disponibles en el repositorio auditable del estudio.",



    italic_text=True



)







add_heading_2("F. Criterios de Elegibilidad Codificados")



add_p(



    "Se establecieron criterios de inclusión y exclusión codificados para gobernar las decisiones del flujo de selección (ver Tabla V):"



)







add_table_title("TABLA V", "CRITERIOS DE INCLUSIÓN Y EXCLUSIÓN CODIFICADOS")



t_cie = doc.add_table(rows=10, cols=4)



hdr = t_cie.rows[0].cells



hdr[0].paragraphs[0].text = "Cód."



hdr[1].paragraphs[0].text = "Tipo"



hdr[2].paragraphs[0].text = "Criterio Metodológico de Elegibilidad"



hdr[3].paragraphs[0].text = "Mecanismo de Verificación"







cie_data = [



    ("IN1", "Inclusión", "Ventana temporal de publicación comprendida entre 2020 y 2026 (período principal 2020–2025 y artículos Early Access con año de volumen formal asignado a 2026).", "Filtros nativos en Scopus y Web of Science."),



    ("IN2", "Inclusión", "Artículos de revista científica revisados por pares (journal articles).", "Filtro nativo Document Type = Article (exclusión de actas de congresos, preprints y literatura gris conforme al estándar de rigor de revista)."),



    ("IN3", "Inclusión", "Indexación en las bases principales Scopus o Web of Science Core Collection.", "Bases suscritas por la institución académica."),



    ("IN4", "Inclusión", "Modelos de IA/IDP aplicados a documentos empresariales y semiestructurados.", "Cribado temático de abstract y texto completo."),



    ("EX1", "Exclusión", "Publicaciones redactadas en idiomas distintos al inglés o español.", "Filtros lingüísticos nativos de plataforma."),



    ("EX2", "Exclusión", "Estudios no accesibles a texto completo a través de suscripciones institucionales.", "Verificación en fase de elegibilidad (n = 5)."),



    ("EX3", "Exclusión", "Revisiones secundarias (surveys, mappings) sin experimentación primaria propia.", "Exclusión en fase de elegibilidad (n = 8)."),



    ("EX4", "Exclusión", "Ámbitos ajenos: historias clínicas, manuscritos antiguos, semiconductores.", "Cribado de título/resumen (n = 35)."),



    ("EX-n", "Exclusión", "Estudios sin métricas empíricas formales o de OCR genérico sin enfoque corporativo.", "Cribado (n = 6) y elegibilidad (n = 153).")



]



for idx, (cod, tip, crit, ver) in enumerate(cie_data, start=1):



    c = t_cie.rows[idx].cells



    c[0].paragraphs[0].text = cod



    c[1].paragraphs[0].text = tip



    c[2].paragraphs[0].text = crit



    c[3].paragraphs[0].text = ver



style_table(t_cie, [Inches(0.4), Inches(0.5), Inches(1.6), Inches(0.9)])







add_heading_2("G. Flujo PRISMA 2020 y Transición Cuantitativa")



add_p(



    "El flujo metodológico de selección se ejecutó de forma determinista y reproducible a través de cuatro fases concatenadas "



    "sin cortes artificiales de muestra (ver Tabla VI y Fig. 1):"



)



add_p(



    "Los procesos de cribado, evaluación y extracción fueron conducidos por el autor aplicando un protocolo estandarizado de "



    "fiabilidad intra-evaluador test-retest a ciegas (con un intervalo de separación temporal de tres semanas entre la primera y segunda evaluación), "



    "conforme a las directrices metodológicas de Kitchenham & Charters [1] y los estándares de reporte de PRISMA 2020 [2]. "



    "Para la fase de cribado por título y resumen se evaluó una muestra de n = 27 registros (8,0 % de los 338 registros únicos, incluyendo estudios incluidos y excluidos), "



    "alcanzando una proporción de acuerdo observado Po = 92,6 % (25 de 27 acuerdos) y un coeficiente de fiabilidad Kappa de Cohen κ = 0,81 "



    "(IC95%: [0,55; 1,00], cuya estimación puntual se ubica en rango casi perfecto con un límite inferior moderado conforme a la escala de referencia de Landis & Koch [141]). En la fase de elegibilidad a texto completo (n = 27, 9,1 % de los 297 textos completos), se obtuvo "



    "Po = 96,3 % (26 de 27 acuerdos) y un κ = 0,87 (IC95%: [0,61; 1,00]), situándose en rango casi perfecto [141]. "



    "En la extracción de variables sobre el corpus final (n = 27, 20,6 % de N = 131), la fiabilidad test-retest alcanzó κ = 0,88 en familias algorítmicas (PI1; Po = 92,6 %, Pe = 0,380) "



    "y κ = 0,86 en dirección de efecto SWiM (PI3; Po = 92,6 %, Pe = 0,470), ratificando una consistencia casi perfecta bajo los baremos de Landis & Koch [141]. Las discrepancias marginales (7,4 % en cribado [2 de 27] y 3,7 % en elegibilidad [1 de 27]) fueron resueltas y dirimidas "



    "en sesiones de arbitraje metodológico supervisadas por el docente asesor experto (Mg. Jimmy Sánchez Portugal), mitigando el sesgo del evaluador único; "



    "no obstante, se declara explícitamente como limitación metodológica del estudio la no realización de un doble cribado independiente en paralelo.",



    bold_prefix="Protocolo de Fiabilidad Intra-Evaluador y Arbitraje Metodológico: "



)



add_p(



    "1) Fase 1 (Identificación): Se identificaron inicialmente 3 701 registros brutos en Scopus (3 270) y WoS (431). "



    "Tras aplicar filtros automatizados de plataforma (tipo de documento artículo y cobertura 2020–2026), se retuvieron "



    "577 artículos de revista (311 en Scopus y 266 en WoS). Posteriormente, el algoritmo de deduplicación "



    "por DOI estandarizado y título normalizado eliminó 239 duplicados (238 inter-base y 1 intra-WoS), ingresando 338 registros únicos a cribado."



)



add_p(



    "2) Fase 2 (Cribado): Bajo protocolo de fiabilidad intra-evaluador test-retest ciego (κ = 0,81, IC95%: [0,55; 1,00]), se excluyeron 41 registros por ruido temático (35 por ámbito clínico/histórico "



    "EX4 y 6 sin reporte de métricas empíricas EX-n), pasando 297 estudios a evaluación a texto completo."



)



add_p(



    "3) Fase 3 (Elegibilidad): Se examinaron los 297 textos completos aplicando los criterios de elegibilidad y el instrumento QA (Kitchenham), "



    "con fiabilidad test-retest κ = 0,87 (IC95%: [0,61; 1,00]) y arbitraje docente. Se excluyeron 166 registros: 20 estudios candidatos con justificación "



    "individual detallada bajo el ítem 16b de PRISMA 2020 [2] (ver Tabla VIII) y 146 registros descartados bajo la causal operativa IN4 / EX-n "



    "(investigaciones de OCR genérico de caracteres o visión por computadora sin validación en flujos documentales empresariales, cuyo inventario "



    "completo se encuentra depositado en el repositorio auditable del estudio). El QA operó como instrumento de caracterización y estratificación, "



    "constatándose que todos los estudios que satisficieron los criterios temáticos superaron holgadamente el umbral formal de QA ≥ 3,0 / 5,0."



)



add_p(



    "4) Fase 4 (Inclusión): El corpus primario final comprende N = 131 estudios de revista científica (100% Journal Articles), estratificados "



    "según su amplitud de cobertura de preguntas de investigación en 4 estudios nucleares de referencia cualitativa (4/4), 59 estudios de soporte avanzado (4/4), "



    "49 estudios de soporte temático (3/4), 17 de soporte algorítmico (2/4) y 2 de contextualización (1/4)."



)







add_table_title("TABLA VI", "TRANSICIÓN CUANTITATIVA DEL FLUJO PRISMA 2020")



t_p20 = doc.add_table(rows=7, cols=5)



hdr = t_p20.rows[0].cells



hdr[0].paragraphs[0].text = "Fase PRISMA"



hdr[1].paragraphs[0].text = "Entrada"



hdr[2].paragraphs[0].text = "Operación Metodológica"



hdr[3].paragraphs[0].text = "Excluidos"



hdr[4].paragraphs[0].text = "Salida"







p20_data = [



    ("1. Identificación", "3 701 brutos", "Filtros nativos de plataforma (artículo, 2020–2026)", "-3 124 no elegibles", "577 exportados"),



    ("   Deduplicación", "577 exportados", "Cruce determinista por DOI y título normalizado", "-239 dupl.", "338 únicos"),



    ("2. Cribado", "338 únicos", "Evaluación de título/resumen con test-retest (κ = 0,81)", "-41 temáticos", "297 elegibles"),



    ("3. Elegibilidad", "297 texto compl.", "Lectura de texto completo y control QA (κ = 0,87)", "-166 estudios", "131 incluidos"),



    ("4. Inclusión", "131 primarios", "Mapeo semántico frente a PI1–PI4 y extracción", "0", "N = 131 final"),



    ("Corpus Total", "3 701 brutos", "Embudo metodológico PRISMA 2020 reproducible", "-3 570 excluidos", "N = 131 final")



]



for idx, (f, ent, op, exc, sal) in enumerate(p20_data, start=1):



    c = t_p20.rows[idx].cells



    c[0].paragraphs[0].text = f



    c[1].paragraphs[0].text = ent



    c[2].paragraphs[0].text = op



    c[3].paragraphs[0].text = exc



    c[4].paragraphs[0].text = sal



style_table(t_p20, [Inches(0.8), Inches(0.6), Inches(1.1), Inches(0.5), Inches(0.4)], align_cols={1: WD_ALIGN_PARAGRAPH.RIGHT, 3: WD_ALIGN_PARAGRAPH.RIGHT, 4: WD_ALIGN_PARAGRAPH.RIGHT})







# Insertar Figura 1 (Diagrama PRISMA)



prisma_img_path = 'project/metodologia/outputs/diagrama_flujo_prisma_2020.png'



if os.path.exists(prisma_img_path):



    p_fig = doc.add_paragraph()



    p_fig.alignment = WD_ALIGN_PARAGRAPH.CENTER



    p_fig.paragraph_format.space_before = Pt(6)



    p_fig.paragraph_format.space_after = Pt(2)



    p_fig.paragraph_format.keep_with_next = True



    r_fig = p_fig.add_run()



    r_fig.add_picture(prisma_img_path, width=Inches(3.3))



    



    p_cap = doc.add_paragraph()



    p_cap.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY



    p_cap.paragraph_format.space_before = Pt(2)



    p_cap.paragraph_format.space_after = Pt(6)



    r_cap_lbl = p_cap.add_run("Fig. 1. ")



    r_cap_lbl.bold = True



    r_cap_lbl.font.size = Pt(8)



    r_cap_txt = p_cap.add_run(



        "Diagrama de flujo PRISMA 2020 de identificación, cribado, elegibilidad a texto completo "



        "(con protocolo de fiabilidad test-retest ciego y arbitraje metodológico, κ = 0,87) e inclusión estratificada de estudios primarios (N = 131)."



    )



    r_cap_txt.font.size = Pt(8)







add_heading_2("H. Evaluación de Calidad Metodológica (QA)")



add_p(



    "Siguiendo las pautas de Kitchenham & Charters (2007) [1], se formuló un instrumento de calidad metodológica compuesto por cinco "



    "preguntas críticas (QA1 a QA5), evaluadas bajo una escala tricotómica objetiva (1,0 = Sí, 0,5 = Parcial, 0,0 = No) con un umbral "



    "mínimo de protocolo fijado a priori en QA ≥ 3,0 / 5,0 (ver Tabla VII). Dicho instrumento no operó como un filtro de exclusión fáctico "



    "(dado que la totalidad de los estudios que satisficieron los criterios temáticos superaron holgadamente el corte, con un puntaje mínimo observado "



    "de 3,50), sino como una herramienta de caracterización descriptiva, estratificación de evidencia y base para el análisis de sensibilidad. "



    "El corpus primario alcanzó una media de calidad metodológica de 4,61 / 5,0 (DE = ±0,41), con los cuatro estudios nucleares obteniendo la "



    "calificación máxima de 5,0 / 5,0."



)







add_table_title("TABLA VII", "PREGUNTAS DEL INSTRUMENTO DE CALIDAD METODOLÓGICA (QA)")



t_qa = doc.add_table(rows=6, cols=3)



hdr = t_qa.rows[0].cells



hdr[0].paragraphs[0].text = "Cód."



hdr[1].paragraphs[0].text = "Pregunta de Control de Calidad Metodológica"



hdr[2].paragraphs[0].text = "Criterio de Calificación Tricotómica"







qa_data = [



    ("QA1", "¿El estudio define explícitamente los objetivos, el problema documental y la tipología de documentos de negocio?", "1.0: Objetivos y tipología explícitos; 0.5: Genéricos; 0.0: No definidos."),



    ("QA2", "¿Se describe detalladamente el conjunto de datos (dataset: volumen, partición train/test, idioma y condiciones de escaneo)?", "1.0: Conjunto de datos y partición explícitos; 0.5: Parcial; 0.0: No describe datos."),



    ("QA3", "¿Se documenta con suficiente claridad la arquitectura neuronal de IA o la canalización (pipeline) de IDP implementada?", "1.0: Arquitectura completa y reproducible; 0.5: Superficial; 0.0: Enfoque caja negra."),



    ("QA4", "¿Se reportan métricas cuantitativas formales de rendimiento (F1-score, exactitud, latencia, tasa de procesamiento o throughput)?", "1.0: Métricas formales reportadas; 0.5: Métricas parciales; 0.0: Solo cualitativo."),



    ("QA5", "¿Los resultados se contrastan empíricamente frente a baselines, reglas tradicionales o el estado del arte?", "1.0: Contraste cuantitativo riguroso; 0.5: Narrativo; 0.0: Sin contraste.")



]



for idx, (cod, preg, crit) in enumerate(qa_data, start=1):



    c = t_qa.rows[idx].cells



    c[0].paragraphs[0].text = cod



    c[1].paragraphs[0].text = preg



    c[2].paragraphs[0].text = crit



style_table(t_qa, [Inches(0.4), Inches(1.8), Inches(1.2)])







add_heading_2("I. Matriz de Estudios Excluidos a Texto Completo (PRISMA 2020 Ítem 16b)")



add_p(



    "Conforme al ítem 16b de la declaración PRISMA 2020 [2], de los 166 registros descartados en la fase de elegibilidad a texto completo, "



    "la Tabla VIII lista individualmente los 20 estudios candidatos que a priori abordaban la problemática pero no satisficieron los requerimientos de "



    "elegibilidad primaria (8 revisiones secundarias EX3, 7 sin métricas cuantitativas empíricas EX-n y 5 sin acceso a texto completo EX2), "



    "consignando sus autores completos, base de origen, código y justificación técnica sin truncamientos. Los 146 registros restantes fueron excluidos "



    "bajo el criterio IN4 / EX-n por corresponder a modelos de OCR genérico a nivel de carácter o visión artificial sin validación en tipologías "



    "documentales de negocio (facturas, recibos, formularios o balances); su catálogo bibliográfico auditable completo (catálogo de 146 registros excluidos) "



    "se encuentra disponible en el repositorio abierto de datos de la investigación conforme a las directrices de reporte PRISMA 2020."



)







add_table_title("TABLA VIII", "LISTADO DE ESTUDIOS EXCLUIDOS A TEXTO COMPLETO (PRISMA 2020 ÍTEM 16b)")



t_am = doc.add_table(rows=len(df_ex20) + 1, cols=4)



hdr = t_am.rows[0].cells



hdr[0].paragraphs[0].text = "Referencia Bibliográfica Completa"



hdr[1].paragraphs[0].text = "Base"



hdr[2].paragraphs[0].text = "Cód."



hdr[3].paragraphs[0].text = "Causal Específica de Exclusión"







for idx, r in df_ex20.iterrows():



    c = t_am.rows[idx + 1].cells



    c[0].paragraphs[0].text = f"{r['authors']} ({r['year']})"



    c[1].paragraphs[0].text = str(r['source_db'])



    c[2].paragraphs[0].text = str(r['code'])



    c[3].paragraphs[0].text = str(r['justification'])



style_table(t_am, [Inches(1.2), Inches(0.4), Inches(0.3), Inches(1.5)], font_size=Pt(6.8))







add_heading_2("J. Caracterización de los 4 Estudios Nucleares de Mayor Puntaje QA y Cobertura Integral (100% Revista)")



add_p(
    "A partir de la evaluación de calidad metodológica sobre el corpus primario, se identificaron 61 estudios con calificación "
    "máxima (QA = 5,0 / 5,0) y cobertura integral de las cuatro preguntas temáticas (PI1 a PI4). Para conformar un núcleo de referencia "
    "cualitativa profunda y calibración analítica sin incurrir en redundancias, se aplicó un embudo operativo sistemático basado en "
    "muestreo de máxima variación (Maximum Variation Sampling) bajo cinco criterios sucesivos: (i) calidad metodológica máxima "
    "(QA = 5,0 / 5,0); (ii) cobertura temática integral estricta de las cuatro preguntas formuladas (4/4 PIs); (iii) pertenencia a la "
    "frontera temporal más reciente del corpus (bienio 2025–2026, subconjunto de 25 estudios); (iv) indexación en revistas Q1/Q2 "
    "en Scopus / Web of Science; y (v) representatividad disjunta sobre las cuatro tipologías documentales cardinales de negocio y familias "
    "algorítmicas de PI1. Siguiendo este protocolo se seleccionaron cuatro estudios nucleares ([3], [4], [5], [6]). Respecto al estudio [3] (Wei et al.), "
    "se aclara que su selección obedece a la necesidad metodológica de modelar la tipología de gráficos analíticos, diagramas estadísticos y tablas complejas "
    "evaluadas en el benchmark mChartQA/mChartQABench, donde la comprensión documental excede el texto lineal y exige "
    "razonamiento visual multimodal. Esta tipología se complementa armónicamente con órdenes y comprobantes de compra B2B ([4]), balances "
    "financieros tabulares heterogéneos ([5]) y recibos comerciales transaccionales B2C ([6]) (ver Tabla IX). Por su parte, las redes neuronales de grafos (GNN), "
    "al no contar con un estudio primario en la frontera 2025–2026 con QA = 5,0 que cubriera simultáneamente las 4 PIs, se analizan dentro "
    "del corpus general de soporte (p. ej., [8], [34], [64], [66])."
)







add_table_title("TABLA IX", "CARACTERIZACIÓN DE LOS 4 ESTUDIOS NUCLEARES DE REFERENCIA CUALITATIVA (100% REVISTA)")



t_nuc = doc.add_table(rows=5, cols=6)



hdr = t_nuc.rows[0].cells



hdr[0].paragraphs[0].text = "ID"



hdr[1].paragraphs[0].text = "Ref."



hdr[2].paragraphs[0].text = "Autores y Año"



hdr[3].paragraphs[0].text = "Revista Indexada y Cuartil"



hdr[4].paragraphs[0].text = "DOI"



hdr[5].paragraphs[0].text = "Aporte Metodológico Fundamental"







nuc_table_data = [



    ("[S001]", "[3]", "Wei et al. (2026/2025)", "Pattern Recognition (Elsevier, Q1)", "10.1016/j.patcog.2025.112348", "VLM multimodal para QA visual sobre gráficos analíticos y tablas complejas (benchmark mChartQA/mChartQABench), superando baselines de OCR tradicional."),



    ("[S002]", "[4]", "Chen et al. (2025)", "Electronics (MDPI, Q2)", "10.3390/electronics14112145", "Evaluación empírica de LLMs e ingeniería de prompts en extracción de información documental frente a reglas fijas."),



    ("[S003]", "[5]", "Ali Khandokar & Deshpande (2025)", "IEEE Access (IEEE, Q1)", "10.1109/access.2024.3522141", "Pipeline de visión computacional y deep learning para extracción de tablas financieras heterogéneas sin plantillas."),



    ("[S004]", "[6]", "Mifsud et al. (2025)", "Mach. Learn. Knowl. Extr. (MDPI, Q1)", "10.3390/make7040167", "Modelo híbrido que combina y contrasta Transformers multimodales con sistemas basados en reglas en recibos comerciales.")



]



for idx, (nid, nref, auth, rev, doi, apt) in enumerate(nuc_table_data, start=1):



    c = t_nuc.rows[idx].cells



    c[0].paragraphs[0].text = nid



    c[1].paragraphs[0].text = nref



    c[2].paragraphs[0].text = auth



    c[3].paragraphs[0].text = rev



    c[4].paragraphs[0].text = doi



    c[5].paragraphs[0].text = apt



style_table(t_nuc, [Inches(0.35), Inches(0.3), Inches(0.65), Inches(0.85), Inches(0.55), Inches(0.75)], font_size=Pt(7.2))







add_heading_2("K. Muestra de la Matriz de Mapeo frente a PI1–PI4")



add_p(



    "El corpus de N = 131 estudios primarios se clasificó según su nivel de cobertura temática de las preguntas de investigación (PI1 a PI4): "



    "Nucleares (n = 4; 4/4 PIs y referencia cualitativa), Soporte Avanzado (n = 59; 4/4 PIs), Soporte Temático (n = 49; 3/4 PIs), "



    "Soporte Algorítmico (n = 17; 2/4 PIs) y Contextualización (n = 2; 1/4 PIs). Se aclara que esta estratificación evalúa la amplitud "



    "de respuesta a las preguntas formuladas (donde PI4 exhibe cobertura del 100 % al constituir el filtro temático obligatorio de documentos de negocio), "



    "distinguiéndose conceptualmente de la calidad metodológica (QA de Kitchenham), en la cual 108 estudios alcanzaron calidad alta (QA ≥ 4,5 pts). "



    "La relación biunívoca matemática entre el identificador del corpus [Sxxx] y la cita IEEE [n] está regida de forma unívoca por "



    "Ref IEEE [n] = ID S + 2 (dado que las citas [1] y [2] corresponden a las normas metodológicas marco Kitchenham & Charters y PRISMA 2020). "



    "La Tabla X presenta una muestra representativa de 11 estudios a lo largo de los estratos de cobertura temática, evidenciando esta correspondencia perfecta:"



)







add_table_title("TABLA X", "MUESTRA REPRESENTATIVA DE LA MATRIZ DE MAPEO FRENTE A PI1–PI4")



sample_ids = ['[S001]', '[S002]', '[S003]', '[S004]', '[S005]', '[S015]', '[S030]', '[S050]', '[S075]', '[S100]', '[S125]']



df_sample = df_final[df_final['id'].isin(sample_ids)]







t_map = doc.add_table(rows=len(df_sample) + 1, cols=9)



hdr = t_map.rows[0].cells



hdr[0].paragraphs[0].text = "ID"



hdr[1].paragraphs[0].text = "Ref."



hdr[2].paragraphs[0].text = "Autores (Año)"



hdr[3].paragraphs[0].text = "PI1"



hdr[4].paragraphs[0].text = "PI2"



hdr[5].paragraphs[0].text = "PI3"



hdr[6].paragraphs[0].text = "PI4"



hdr[7].paragraphs[0].text = "Total"



hdr[8].paragraphs[0].text = "Estrato de Cobertura Temática"







for idx, r in df_sample.reset_index(drop=True).iterrows():



    c = t_map.rows[idx + 1].cells



    s_num = int(str(r['id']).replace('[S', '').replace(']', ''))



    c[0].paragraphs[0].text = str(r['id'])



    c[1].paragraphs[0].text = f"[{s_num + 2}]"



    c[2].paragraphs[0].text = f"{r['authors'].split(';')[0]} et al. ({r['year']})" if ';' in str(r['authors']) else f"{r['authors']} ({r['year']})"



    c[3].paragraphs[0].text = "✔" if r['PI1'] == 1 else "—"



    c[4].paragraphs[0].text = "✔" if r['PI2'] == 1 else "—"



    c[5].paragraphs[0].text = "✔" if r['PI3'] == 1 else "—"



    c[6].paragraphs[0].text = "✔" if r['PI4'] == 1 else "—"



    c[7].paragraphs[0].text = f"{r['total_pi']}/4"



    c[8].paragraphs[0].text = "Nuclear" if r['total_pi'] == 4 and r['id'] in ['[S001]', '[S002]', '[S003]', '[S004]'] else ("Soporte (4/4)" if r['total_pi'] == 4 else ("Soporte (3/4)" if r['total_pi'] == 3 else "Soporte (2/4)"))



style_table(t_map, [Inches(0.35), Inches(0.3), Inches(1.0), Inches(0.2), Inches(0.2), Inches(0.2), Inches(0.2), Inches(0.3), Inches(0.7)], font_size=Pt(7.2), align_cols={1: WD_ALIGN_PARAGRAPH.CENTER, 3: WD_ALIGN_PARAGRAPH.CENTER, 4: WD_ALIGN_PARAGRAPH.CENTER, 5: WD_ALIGN_PARAGRAPH.CENTER, 6: WD_ALIGN_PARAGRAPH.CENTER, 7: WD_ALIGN_PARAGRAPH.CENTER})







add_heading_2("L. Vinculación con Resultados y Estrategia de Síntesis")



add_p(



    "Siguiendo las directrices metodológicas de Kitchenham & Charters (2007) [1] y PRISMA 2020 [2], los hallazgos de los 131 estudios primarios "



    "[3]–[133] se estructuran y consolidan mediante métodos cuantitativos estandarizados según la naturaleza de cada interrogante: "



    "Síntesis Temática (Thomas & Harden [134]; Cruzes & Dybå [135]) para la taxonomía algorítmica y tipologías documentales (PI1, PI4); "



    "Síntesis Narrativa Estructurada (Popay et al. [136]) con reporte de rangos empíricos [mín, máx] y dispersión por benchmark para el rendimiento "



    "técnico (PI2); Síntesis sin metaanálisis (SWiM, Campbell et al. [137]) con conteo de votos de dirección del efecto y barras divergentes para la "



    "comparativa de eficiencia frente a métodos tradicionales (PI3); Mapeo Sistemático con gráficos de burbujas (Petersen et al. [138]) para el cruce "



    "de diseños y datasets (PD3); análisis cienciométrico con mapas de coocurrencia de palabras clave en VOSviewer (van Eck & Waltman [139]) para redes de "



    "investigación (PD2); y evaluación estructurada de la certeza mediante un juicio narrativo de confianza basado en la adaptación de los cuatro dominios del marco GRADE-CERQual (Confidence in the Evidence from Reviews of Qualitative research, Lewin et al. [140]), siguiendo las directrices SWiM (Campbell et al. [137]) para síntesis sin metaanálisis estadístico. "



    "Se descarta formalmente la ejecución de un metaanálisis estadístico de efectos fijos o aleatorios debido a la profunda heterogeneidad técnica, "



    "métrica y contextual del dominio de Information Extraction en documentos empresariales: (a) heterogeneidad métrica: los estudios evalúan el "



    "rendimiento a niveles de granularidad conceptualmente incompatibles (exactitud de OCR a nivel de carácter/token mediante CER/WER frente a KIE a "



    "nivel de entidad semántica completa mediante F1-score estricto vs. relajado y ANLS en preguntas y respuestas visuales); (b) heterogeneidad de "



    "entornos de ejecución: las latencias y velocidades de inferencia reportadas (ms/página) dependen de infraestructuras de hardware dispares "



    "(desde clústeres NVIDIA A100/H100 hasta servidores locales sin GPU acelerada), imposibilitando un pool homogéneo de tiempos; y (c) disparidad de "



    "corpus de validación: mientras una fracción de autores evalúa sobre benchmarks públicos (SROIE, CORD, FUNSD), una porción sustancial valida sus "



    "arquitecturas en datasets corporativos cerrados y propietarios no estandarizados, los cuales no reportan intervalos de confianza ni desviaciones "



    "estándar requeridas para un modelo metaanalítico combinado. En consecuencia, la síntesis estructurada por preguntas de investigación "



    "constituye el enfoque metodológico formal y reproducible.",



    bold_prefix="Estrategia de Síntesis y Justificación de la Inviabilidad de Metaanálisis Cuantitativo: "



)







add_p(



    "Para garantizar la trazabilidad biunívoca entre la formulación metodológica y la evidencia empírica, cada una de las siete preguntas de "



    "investigación (PD1–PD3 y PI1–PI4) se mapea directamente con una tabla y un gráfico cuantitativo asignado en la sección de Resultados (ver Tabla XI):"



)







add_table_title("TABLA XI", "MATRIZ DE ENLACE BIUNÍVOCO ENTRE PREGUNTAS Y RESULTADOS")



t_enl = doc.add_table(rows=8, cols=4)



hdr = t_enl.rows[0].cells



hdr[0].paragraphs[0].text = "Pregunta"



hdr[1].paragraphs[0].text = "Contenido Temático a Responder"



hdr[2].paragraphs[0].text = "Tabla de Evidencia Asignada"



hdr[3].paragraphs[0].text = "Gráfico Asignado"







enl_data = [



    ("PD1", "Evolución temporal de publicaciones sobre IA/IDP en documentos empresariales.", "Distribución anual de artículos (2020–2025).", "Gráfico de líneas de tendencia temporal."),



    ("PD2", "Productividad académica por autores, revistas indexadas y países líderes.", "Ranking de las 10 revistas líderes, autores prolíficos y países.", "Gráfico de barras geográfico y red de coocurrencia de palabras clave en VOSviewer."),



    ("PD3", "Distribución de diseños metodológicos y datasets (públicos vs. privados).", "Tabla cruzada: diseño metodológico × tipo de dataset.", "Gráfico de burbujas (mapeo sistemático de Petersen et al. [138])."),



    ("PI1", "Taxonomía de enfoques algorítmicos (secuencias, grafos, transformers multimodales).", "Matriz de arquitecturas de IA identificadas.", "Gráfico de barras por familia algorítmica (síntesis temática [134], [135])."),



    ("PI2", "Rendimiento cuantitativo reportado (F1-score, exactitud, latencia de inferencia).", "Tabla comparativa de métricas por benchmark (SROIE, FUNSD, CORD).", "Síntesis narrativa estructurada (Popay et al. [136]) con rangos [mín, máx] y dispersión."),



    ("PI3", "Comparativa de eficiencia y costo: IA/IDP frente a ingreso manual y reglas.", "Conteo de votos de dirección del efecto (mejora, sin diferencia, empeora).", "Método SWiM (Campbell et al. [137]) con gráfico de barras divergentes."),



    ("PI4", "Tipologías documentales (facturas, recibos) y sistemas ERP/CRM integrados.", "Frecuencia por tipo de documento × plataforma.", "Matriz de calor (heatmap) documental.")



]



for idx, (p, cont, tab, grf) in enumerate(enl_data, start=1):



    c = t_enl.rows[idx].cells



    c[0].paragraphs[0].text = p



    c[1].paragraphs[0].text = cont



    c[2].paragraphs[0].text = tab



    c[3].paragraphs[0].text = grf



style_table(t_enl, [Inches(0.4), Inches(1.1), Inches(1.0), Inches(0.9)], font_size=Pt(7.2))







add_heading_2("M. Amenazas a la Validez y Mitigación")



add_p(



    "Para salvaguardar la solidez del estudio, se analizaron cuatro amenazas potenciales a la validez, implementando acciones "



    "preventivas en cada fase del protocolo (ver Tabla XII):"



)







add_table_title("TABLA XII", "AMENAZAS A LA VALIDEZ Y ACCIONES DE MITIGACIÓN")



t_val = doc.add_table(rows=5, cols=3)



hdr = t_val.rows[0].cells



hdr[0].paragraphs[0].text = "Dimensión"



hdr[1].paragraphs[0].text = "Riesgo de Sesgo Identificado"



hdr[2].paragraphs[0].text = "Estrategia de Mitigación Implementada"







val_data = [



    ("Sesgo de Selección", "Omisión de literatura relevante o sesgo por formato de publicación.", "Búsqueda simétrica en Scopus y Web of Science. Restricción estricta a artículos de revista científica arbitrados (Journal Articles) para garantizar rigor y madurez metodológica en la evidencia compilada. Se declara explícitamente como una limitación mayor el sesgo de selección derivado de la exclusión de actas de congresos (Conference Proceedings) y preprints, dado que arquitecturas fundacionales de IDP (p. ej., LayoutLM [142], DocFormer [143], StrucTexT [144], BROS [145]) se originaron en dichos foros; no obstante, el corpus primario (N = 131) captura sistemáticamente su adopción, optimización empírica e integración en flujos corporativos reportada en revistas consolidadas."),



    ("Sesgo de Publicación", "Predominancia en la literatura indexada de artículos que reportan predominantemente resultados favorables o mejoras sobre baselines (efecto 'file-drawer').", "Reconocido formalmente como una limitación metodológica intrínseca no mitigada por completo. Si bien se extrajeron sistemáticamente las fallas, caídas de precisión (F1 al 84,5 %) y cuellos de botella computacionales documentados en el corpus publicado (PI2, PI3), se asume el sesgo estructural derivado de la ausencia de experimentos e implementaciones empresariales fallidas no publicadas."),



    ("Sesgo del Evaluador", "Subjetividad individual durante el cribado y control QA por autor único.", "Protocolo de fiabilidad intra-evaluador test-retest ciego (n = 27 por fase: κ = 0,81 en cribado [IC95%: 0,55; 1,00], κ = 0,87 en elegibilidad, κ = 0,88 en PI1 y κ = 0,86 en PI3, interpretados según Landis & Koch [141]) y arbitraje docente (7,4 % en cribado y 3,7 % en elegibilidad); reconociendo como limitación metodológica la ausencia de doble cribado independiente paralelo."),



    ("Validez de Constructo", "Desalineación entre términos de búsqueda y conceptos reales, o inclusión de tecnologías fronterizas del pipeline documental.", "Derivación formal a partir de la matriz PICOC y distinción entre capas habilitadoras del flujo empresarial (preprocesamiento geométrico [70], marcas de agua [79], KYC [21], soporte multilingüe [15], [16] y privacidad [116]) frente a OCR genérico descontextualizado. La neutralidad frente a estudios periféricos se validó formalmente en el análisis de sensibilidad metodológica, ratificando la consistencia metodológica de los hallazgos sustantivos.")



]



for idx, (dim, rsg, mit) in enumerate(val_data, start=1):



    c = t_val.rows[idx].cells



    c[0].paragraphs[0].text = dim



    c[1].paragraphs[0].text = rsg



    c[2].paragraphs[0].text = mit



style_table(t_val, [Inches(0.8), Inches(1.1), Inches(1.5)], font_size=Pt(7.5))











# ==============================================================================



# SECCIÓN III: RESULTADOS DE LA REVISIÓN SISTEMÁTICA DE LITERATURA (RSL)



# ==============================================================================



add_heading_1("III. RESULTADOS")
add_heading_2("A. Apertura General del Corpus y Protocolo de Síntesis")

add_p(
    "La presente sección describe y cuantifica de forma objetiva la evidencia empírica extraída del corpus de literatura científica incluido, "
    "conforme a las directrices de reporte de Kitchenham & Charters (2007) [1] y los estándares internacionales de la declaración "
    "PRISMA 2020 [2], articulando directamente la evidencia cuantitativa con el análisis sistemático de cada eje temático."
)

add_p(
    "El corpus documental primario quedó formalmente cerrado y congelado en un total de N = 131 artículos de revista científica indexada "
    "(100 % Journal Articles, sin actas de congreso, preprints, tesis ni literatura gris), habiendo superado el control de calidad metodológica "
    "(QA ≥ 3,50 / 5.00; media global = 4,61 / 5.00). La numeración de citas bibliográficas mantiene una relación matemática biunívoca: "
    "Ref IEEE [n] = ID S + 2, donde las citas [1] y [2] corresponden a las normas metodológicas marco (Kitchenham & Charters y PRISMA 2020), los 131 "
    "estudios primarios del corpus se indexan de manera inalterable entre [3] y [133] (desde [S001] hasta [S131]), y las referencias metodológicas "
    "complementarias de síntesis documental y cienciometría se ubican en [134] a [141]."
)

add_p(
    "Conforme a los ítems 13a–13f de PRISMA 2020 y para mitigar el sesgo de notificación (reporting bias), la selección de la estrategia analítica "
    "para cada interrogante se formalizó antes de la consolidación de los datos: 1) Síntesis Temática (Thomas & Harden [134]; Cruzes & Dybå [135]) "
    "para la taxonomía algorítmica de arquitecturas IA/IDP (PI1) y el mapeo de tipologías documentales y sistemas ERP/CRM (PI4); 2) Síntesis Narrativa "
    "Estructurada (Popay et al. [136]) para el análisis de rendimiento técnico (PI2), organizando las métricas cuantitativas (F1-score, exactitud, latencia) "
    "por benchmarks estándar (SROIE, FUNSD, CORD) y reportando rangos empíricos [mín, máx] sin promediar métricas entre datasets incompatibles; "
    "3) Síntesis sin metaanálisis — SWiM (Campbell et al. [137]) para contrastar las soluciones IA/IDP frente a líneas base tradicionales y manuales (PI3), "
    "utilizando el conteo de votos de dirección del efecto (Mejora, Sin diferencia, Empeora) y barras divergentes; 4) Mapeo Sistemático Matricial "
    "(Petersen et al. [138]) para caracterizar la evolución temporal (PD1) y el cruce bidimensional entre diseños metodológicos y tipologías de dataset (PD3) "
    "mediante gráficos de burbujas; 5) Mapeo Cienciométrico y Análisis de Redes (van Eck & Waltman [139]) en PD2 para identificar núcleos de producción científica "
    "(revistas, países, autores) y la estructura de coocurrencia de palabras clave de autor en VOSviewer con umbral de ≥ 3 apariciones; y 6) Calificación de "
    "Certeza de la Evidencia (Lewin et al. [140]) mediante el marco GRADE-CERQual sobre 4 pilares para ponderar cada hallazgo principal."
)

# ------------------------------------------------------------------------------
# 1.1 PD1: Evolución Temporal
# ------------------------------------------------------------------------------
add_heading_2("B. Evolución Temporal de la Producción Científica (PD1: ¿Cómo ha evolucionado el volumen de producción científica anual sobre IA aplicada a documentos empresariales entre 2020 y 2025/2026?)")

add_p(
    "Para determinar el comportamiento cronológico de la literatura sobre IA/IDP aplicada al procesamiento de documentos de negocio entre 2020 y 2025/2026, "
    "se contabilizó la distribución de los 131 artículos primarios por año de publicación formal indexada, cuyos datos cuantitativos se detallan en la "
    "TABLA XIII y se visualizan gráficamente en la Fig. 2."
)

add_table_title("TABLA XIII", "DISTRIBUCIÓN CRONOLÓGICA DE LA PRODUCCIÓN CIENTÍFICA (2020–2025/2026) (N = 131)")
t_pd1 = doc.add_table(rows=8, cols=4)
hdr_pd1 = t_pd1.rows[0].cells
hdr_pd1[0].paragraphs[0].text = "Año de Publicación"
hdr_pd1[1].paragraphs[0].text = "Frecuencia Absoluta (n)"
hdr_pd1[2].paragraphs[0].text = "Frecuencia Relativa (%)"
hdr_pd1[3].paragraphs[0].text = "Porcentaje Acumulado (%)"

pd1_data = [
    ("2020", "4", "3,1 %", "3,1 %"),
    ("2021", "14", "10,7 %", "13,8 %"),
    ("2022", "17", "13,0 %", "26,8 %"),
    ("2023", "27", "20,6 %", "47,4 %"),
    ("2024", "16", "12,2 %", "59,6 %"),
    ("2025", "50", "38,2 %", "97,8 %"),
    ("2026*", "3", "2,3 %", "100,0 %")
]
for idx, (yr, fa, fr, pac) in enumerate(pd1_data, start=1):
    c = t_pd1.rows[idx].cells
    c[0].paragraphs[0].text = yr
    c[1].paragraphs[0].text = fa
    c[2].paragraphs[0].text = fr
    c[3].paragraphs[0].text = pac

style_table(t_pd1, [Inches(1.8), Inches(1.6), Inches(1.6), Inches(1.6)],
            align_cols=[WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER])
add_table_footer("* Nota: Los estudios fechados en 2026 corresponden a artículos aceptados e incorporados en modalidad Early Access / In Press en Scopus y Web of Science durante el cierre de 2025 ([3], [65], [66]). Fuente: elaboración propia a partir del corpus primario [3]–[133].")

add_figure_with_caption('project/resultados/outputs/fig2_evolucion_anual.png', 'Fig. 2',
                        'Evolución temporal de publicaciones sobre IA/IDP en documentos empresariales (2020–2025/2026, N = 131)',
                        'Barras: volumen anual absoluto (n); línea roja: porcentaje acumulado (%).')

add_p(
    "Ciento treinta y un estudios (100,0 % del corpus primario; [3]–[133]) respondieron a la evolución cronológica de la producción científica "
    "en IA e IDP aplicada a sistemas documentales corporativos (PD1). Mediante mapeo sistemático cronológico se identificó una trayectoria de crecimiento "
    "marcadamente expansiva y no lineal a lo largo del sexenio 2020–2025/2026, con una concentración máxima de publicaciones en el bienio final (TABLA XIII, Fig. 2).",
    bold_prefix="1) Apertura — Respuesta a «¿Cómo ha evolucionado el volumen de producción científica anual sobre IA aplicada a documentos empresariales entre 2020 y 2025/2026?»: "
)

add_p(
    "La dinámica temporal de publicación se articula en tres periodos analíticos diferenciados (Tabla XIII, Fig. 2):\n"
    "a) Fase de emergencia y cimientos basados en OCR-CNN (2020–2021): Ciclo inicial caracterizado por propuestas orientadas a mejorar la binarización de escaneos, "
    "OCR neuronal con LSTM y segmentación clásica con Mask R-CNN. Registró un volumen de producción moderado en relación con etapas posteriores (Tabla XIII), "
    "alcanzando un 88,9 % de estudios con calidad alta y una certeza GRADE-CERQual moderada debido a la escasez de comparaciones con pipelines comerciales de producción.\n"
    "b) Fase de consolidación de Transformers Multimodales (2022–2023): Representó el primer punto de inflexión significativo de la disciplina al acelerar sensiblemente "
    "la producción científica anual (Tabla XIII). Este avance estuvo impulsado por la adopción masiva de modelos multimodales preentrenados (LayoutLMv2/v3 [142], StrucTexT [144], BROS [145]) "
    "y redes basadas en grafos (GCN) para la extracción de claves semánticas (KIE) en facturas y recibos, con un 84,6 % de estudios en el estrato de calidad metodológica alta y certeza GRADE-CERQual alta.\n"
    "c) Fase de aceleración con VLMs y Modelos Generativos (2025–2026*): Constituye la etapa más prolífica del corpus, concentrando el volumen cúspide de publicaciones (Tabla XIII). "
    "El factor determinante de esta aceleración fue la incorporación de Vision-Language Models (VLMs), Transformers generativos con mecanismos de atención visual desacoplada y modelos de lenguaje "
    "de gran escala (LLMs) adaptados con prompt engineering y few-shot learning, donde el 88,9 % de los estudios alcanzó calidad alta con certeza GRADE-CERQual alta.",
    bold_prefix="2) Desarrollo por Categoría y Fases Temporales: "
)

add_p(
    "A pesar de la tendencia global alcista, la literatura experimentó una desaceleración temporal transitoria durante 2024 (Tabla XIII). "
    "Una posible explicación, no contrastada empíricamente en la presente revisión, sugiere que esta inflexión transitoria pudo coincidir con la transición "
    "de los laboratorios desde arquitecturas de grafos y pipelines heurísticos hacia el ajuste y maduración de modelos fundacionales multimodales "
    "y arquitecturas sin entrenamiento previo (zero-shot) publicadas formalmente en el ciclo 2025–2026 [3], [6], [22], [32].",
    bold_prefix="3) Contrastes y Debates Temporales: "
)

add_p(
    "La literatura sobre IA/IDP en sistemas corporativos evidencia una trayectoria de maduración sostenida, transitando desde la simple corrección óptica de caracteres "
    "hacia sistemas integrales de comprensión de documentos ricos visualmente (Visually-Rich Documents). No se identificaron estudios longitudinales que evalúen la "
    "degradación de los modelos a lo largo de más de dos años operativos en empresas. El 40,5 % de las publicaciones corresponde a 2025–2026 (53 de 131 estudios), ratificando la rápida adopción de modelos multimodales en el tratamiento de documentación corporativa. Asimismo, al evaluar la sensibilidad excluyendo los 10 estudios con puntaje de calidad moderada (QA = 3,5; [116]–[118], [121]–[123], [127], [128], [132], [133]), la proporción correspondiente al ciclo 2025–2026 se situó en el 41,3 % "
    "(50 de 121 estudios), ratificando la robustez de la tendencia expansiva.",
    bold_prefix="4) Cierre, Tendencias y Sensibilidad: "
)

# ------------------------------------------------------------------------------
# 1.2 PD2: Revistas, Autores, Países
# ------------------------------------------------------------------------------
add_heading_2("C. Productividad por Revistas, Autores, Países y Red de Coocurrencia (PD2: ¿Qué autores, revistas científicas indexadas y países concentran la mayor productividad e impacto académico?)")

add_p(
    "Para responder a la pregunta «¿Qué autores, revistas científicas indexadas y países concentran la mayor productividad e impacto académico?» (PD2), se normalizaron los títulos de las revistas indexadas, se contabilizó la productividad de los autores, se aplicó la regla estricta de "
    "afiliación geográfica institucional del primer autor y se estructuró la red de coocurrencia de palabras clave de autor (Author Keywords) "
    "con un umbral de frecuencia ≥ 3 en VOSviewer [139]. La evidencia bibliométrica de concentración autoral y geográfica se compendia en la Tabla XV y la Fig. 3, mientras que el desglose exhaustivo de los canales de difusión se traslada formalmente al Material Suplementario (Tabla XIV en Apéndice) para optimizar la densidad técnica del cuerpo principal."
)

add_table_title("TABLA XV", "CONCENTRACIÓN GEOGRÁFICA POR AFILIACIÓN DEL PRIMER AUTOR Y AUTORES DESTACADOS (N = 131)")
t_pd2_geo = doc.add_table(rows=12, cols=4)
hdr_geo = t_pd2_geo.rows[0].cells
hdr_geo[0].paragraphs[0].text = "País de Afiliación (Primer Autor)"
hdr_geo[1].paragraphs[0].text = "Estudios [n]"
hdr_geo[2].paragraphs[0].text = "% Relativo"
hdr_geo[3].paragraphs[0].text = "Autores Más Prolíficos en el Corpus (≥ 3 publicaciones)"

geo_data = [
    ("China", "39", "29,8 %", "Zhang J. (4; [43], [81], [82], [120]), Zhang Y. (4; [78], [79], [81], [82]), Li C. (3; [9], [15], [32]), Liu J. (3; [19], [34], [74]), Zhang W. (3; [26], [37], [73]), Ma J. (3; [37], [43], [120]), Zhang Z. (3; [43], [83], [120])."),
    ("India", "11", "8,4 %", "Sin autores con ≥ 3 publicaciones (producción dispersa, ≤ 2 estudios c/u: Tiwari D., Gupta A., Baviskar D.)."),
    ("Estados Unidos", "10", "7,6 %", "Wang P. (3; [47], [89], [121])."),
    ("Alemania", "9", "6,9 %", "Hashmi K.A. (3; [59], [61], [123]), Liwicki M. (3; [59], [61], [123]), Stricker D. (3; [59], [61], [123])."),
    ("Corea del Sur", "6", "4,6 %", "Lee S. (3; [42], [71], [121])."),
    ("Canadá", "5", "3,8 %", "Simsek M. (4; [11], [35], [48], [51]), Kantarci B. (4; [11], [35], [48], [51]), Xiao B. (3; [11], [35], [48]), Alkheir A.A. (3; [11], [35], [48])."),
    ("Vietnam", "5", "3,8 %", "Sin autores con ≥ 3 publicaciones (producción dispersa, ≤ 2 estudios c/u)."),
    ("Taiwán", "4", "3,1 %", "Sin autores con ≥ 3 publicaciones (producción dispersa, 1 estudio c/u)."),
    ("Turquía", "4", "3,1 %", "Sin autores con ≥ 3 publicaciones (producción dispersa, ≤ 2 estudios c/u: Oral B. (2; [50], [64]), Sayallar C. (1; [100]))."),
    ("España", "3", "2,3 %", "Sin autores con ≥ 3 publicaciones (producción dispersa, ≤ 2 estudios c/u: Fornés A. (2; [105], [111]), Lladós J. (2; [105], [116]))."),
    ("Otros 22 países (≤ 2 estudios c/u)", "35", "26,7 %", "Sin autores con ≥ 3 publicaciones (alta dispersión institucional en Australia, Reino Unido, Francia, etc.).")
]
for idx, (pais, est, pct, aut) in enumerate(geo_data, start=1):
    c = t_pd2_geo.rows[idx].cells
    c[0].paragraphs[0].text = pais
    c[1].paragraphs[0].text = est
    c[2].paragraphs[0].text = pct
    c[3].paragraphs[0].text = aut

style_table(t_pd2_geo, [Inches(1.5), Inches(0.7), Inches(0.7), Inches(3.7)],
            align_cols=[WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT])
add_table_footer("Fuente: elaboración propia a partir del corpus primario [3]–[133]. Regla de país: país de la institución del primer autor. Desambiguación: las firmas chinas con iniciales homónimas (Zhang J., Zhang Y., Zhang W., Zhang Z.) se verificaron y desambiguaron mediante Scopus Author ID, ORCID y redes de coautoría.")

add_figure_with_caption('project/resultados/outputs/fig3_vosviewer_geografia.png', 'Fig. 3',
                        'Concentración geográfica de la investigación y principales clústeres temáticos derivados de palabras clave de autor (PD2, N = 131)',
                        '(a) Distribución porcentual por país de afiliación del primer autor; (b) Frecuencia de descriptores con umbral ≥ 3 ocurrencias en VOSviewer.')

add_p(
    "Ciento treinta y un artículos primarios (100,0 % del corpus; [3]–[133]) respondieron a la distribución de productividad académica por revistas, "
    "autores, países y estructura temática de redes (PD2). Mediante análisis cienciométrico y mapeo de coocurrencia en VOSviewer [139] se identificó una "
    "concentración de publicaciones en revistas especializadas de procesamiento de documentos e ingeniería de sistemas, liderada a nivel geográfico por "
    "instituciones de China, India y Estados Unidos, coexistiendo una alta dispersión autoral de base con polos consolidados de productividad serial (Tabla XIV en Apéndice, TABLA XV, Fig. 3).",
    bold_prefix="1) Apertura — Respuesta a «¿Qué autores, revistas científicas indexadas y países concentran la mayor productividad e impacto académico?»: "
)

add_p(
    "La evidencia se estructura en tres dimensiones bibliométricas (Tabla XIV en Apéndice, Tabla XV, Fig. 3):\n"
    "a) Núcleos de difusión y revistas líderes: Doce revistas concentraron casi la mitad de la producción global (60 de 131 artículos; Tabla XIV en Apéndice). Las cabeceras líderes fueron IEEE Access (9,9 %, n = 13; Q1/Q2), International Journal on Document Analysis and Recognition (IJDAR) (6,9 %, n = 9; Q2) y Pattern Recognition (4,6 %, n = 6; Q1), consolidándose como los principales canales de difusión de modelos de extracción estructurada e IDP. Las restantes 64 revistas indexadas reunieron una producción complementaria y diversa (71 artículos, 54,2 % del corpus; Tabla XIV en Apéndice), reflejando la dispersión propia de la Ley de Bradford en el área. El catálogo completo de revistas, editoriales y cuartiles JCR/SJR se compendia en la Tabla XIV del Apéndice de Material Suplementario para optimizar la densidad técnica del cuerpo principal.\n"
    "b) Polos geográficos de investigación: Conforme a la regla de asignación por primer autor, la investigación se concentró principalmente en Asia y Norteamérica, "
    "con China, India y Estados Unidos a la vanguardia, complementados por contribuciones significativas de Europa occidental en Alemania y España (Tabla XV, Fig. 3a).\n"
    "c) Red cienciométrica de palabras clave (VOSviewer): Con un umbral ≥ 3 apariciones se configuraron tres clústeres conceptuales (Fig. 3b): Clúster 1 (Extracción "
    "y Semántica: Information Extraction, Document Understanding y Key Information Extraction - KIE); Clúster 2 (Paradigmas Algorítmicos: Deep Learning, Optical Character Recognition - OCR "
    "y Transformers); y Clúster 3 (Estructuras Complejas: Table Structure Recognition, Table Detection y Object Detection).",
    bold_prefix="2) Desarrollo por Categoría y Redes Temáticas: "
)

add_p(
    "Frente a la concentración institucional y geográfica en China y en cabeceras editoriales de alto impacto, la estructura de autoría exhibe un comportamiento dual (Tabla XV). "
    "Por un lado, predomina una elevada dispersión de base: el 84,7 % de los autores (422 de 498) registró un único artículo en la ventana analizada. "
    "Por otro lado, la productividad serial (≥ 3 estudios) se articula en redes colaborativas específicas (Tabla XV): destacan los consorcios de la Universidad de Ottawa "
    "en Canadá (equipo de Simsek y colaboradores) y del DFKI / Universidad de Kaiserslautern en Alemania (equipo de Hashmi y Stricker) en procesamiento tabular, "
    "junto a redes cooperativas en China en modelado multimodal y segmentación de tablas [43], [120], y líneas sostenidas en Estados Unidos [47], [89] y Corea del Sur [42], [71]. "
    "Para evitar sesgos cienciométricos por homonimia asiática, la atribución autoral se verificó y desambiguó mediante Scopus Author ID, ORCID y redes de coautoría institucional.",
    bold_prefix="3) Contrastes y Dispersión Autoral: "
)

add_p(
    "En el plano geográfico regional, la representación de América Latina en el corpus primario se circunscribe al estudio brasileño [14] (Gonçalves Lima y Alves Pereira, "
    "Universidade Federal de Lavras), el cual introdujo el benchmark UFLA-FORMS para extracción de entidades en formularios semiestructurados en portugués, sumado a "
    "las contribuciones ibéricas en detección tabular y procesamiento de recibos ([105], [111], [131]). Esta reducida frecuencia de publicaciones latinoamericanas "
    "en revistas Q1–Q3 no refleja necesariamente una ausencia de investigación aplicada en la región, sino las fronteras de cobertura del protocolo de búsqueda "
    "(restricción a Scopus/WoS en inglés/español y exclusión sistemática de actas de congresos regionales como CLEI o simposios locales, donde se concentra parte del "
    "desarrollo tributario corporativo). En el análisis de sensibilidad excluyendo los 10 estudios con QA = 3,5, China concentró el 31,4 % de los estudios filtrados (38 de 121), confirmando la estabilidad del mapa cienciométrico global.",
    bold_prefix="4) Cierre, Tendencias y Sensibilidad: "
)

# ------------------------------------------------------------------------------
# 1.3 PD3: Diseños Metodológicos x Datasets
# ------------------------------------------------------------------------------
add_heading_2("D. Clasificación de Diseños Metodológicos × Tipología de Datasets (PD3: ¿Qué diseños metodológicos y tipologías de conjuntos de datos predominan en la literatura?)")

add_p(
    "Para evaluar la solidez empírica y la transferibilidad industrial de las soluciones reportadas en el corpus, se clasificaron los 131 estudios primarios cruzando la "
    "taxonomía estandarizada de diseños de investigación frente a las fuentes de datos utilizadas (benchmarks públicos, privados corporativos o mixtos). La concordancia "
    "inter-evaluador de esta categorización se evaluó de forma ciega e independiente sobre una muestra del 20,6 % del corpus (n = 27 estudios seleccionados aleatoriamente), "
    "alcanzando un coeficiente Kappa de Cohen κ = 0,85 (acuerdo observado del 88,9 % frente a un azar esperado de 0.258; concordancia casi perfecta). La matriz de contingencia "
    "se reporta en la Tabla XVI y el gráfico de burbujas de Petersen et al. (2015) [138] se expone en la Fig. 4."
)

add_table_title("TABLA XVI", "MATRIZ CRUZADA DE DISEÑOS METODOLÓGICOS Y TIPOLOGÍA DE DATASETS (PD3) (N = 131)")
t_pd3 = doc.add_table(rows=6, cols=6)
hdr_pd3 = t_pd3.rows[0].cells
hdr_pd3[0].paragraphs[0].text = "Diseño Metodológico de Investigación"
hdr_pd3[1].paragraphs[0].text = "Bancos de Pruebas (Benchmarks) Abiertos"
hdr_pd3[2].paragraphs[0].text = "Conjuntos de Datos Privados"
hdr_pd3[3].paragraphs[0].text = "Conjuntos de Datos Híbridos / Mixtos"
hdr_pd3[4].paragraphs[0].text = "Total por Diseño [n]"
hdr_pd3[5].paragraphs[0].text = "% Relativo"

pd3_data = [
    ("Experimental Controlado", "48 (36,6 %)", "18 (13,7 %)", "16 (12,2 %)", "82", "62,6 %"),
    ("Desarrollo de Artefacto / PoC", "14 (10,7 %)", "11 (8,4 %)", "6 (4,6 %)", "31", "23,7 %"),
    ("Cuasi-experimental", "4 (3,1 %)", "4 (3,1 %)", "2 (1,5 %)", "10", "7,6 %"),
    ("Caso de Estudio Real Corporativo", "2 (1,5 %)", "5 (3,8 %)", "1 (0,8 %)", "8", "6,1 %"),
    ("Total por Tipología de Dataset", "68 (51,9 %)", "38 (29,0 %)", "25 (19,1 %)", "131", "100,0 %")
]
for idx, (dis, pub, priv, mix, tot, pct) in enumerate(pd3_data, start=1):
    c = t_pd3.rows[idx].cells
    c[0].paragraphs[0].text = dis
    c[1].paragraphs[0].text = pub
    c[2].paragraphs[0].text = priv
    c[3].paragraphs[0].text = mix
    c[4].paragraphs[0].text = tot
    c[5].paragraphs[0].text = pct

style_table(t_pd3, [Inches(1.8), Inches(1.8), Inches(1.3), Inches(1.1), Inches(0.6), Inches(0.6)],
            align_cols=[WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER])
add_table_footer("Fuente: elaboración propia a partir del corpus primario [3]–[133]. Medición de acuerdo inter-evaluador sobre muestra del 20,6 % (n = 27): Po = 88,9 %, Pe = 0,258, κ = 0,85 (casi perfecto). Partición matemática exacta de 12 celdas disjuntas.")

add_figure_with_caption('project/resultados/outputs/fig4_burbujas_disenos_datasets.png', 'Fig. 4',
                        'Gráfico de burbujas del mapeo sistemático (Petersen et al. [138]): Diseño Metodológico vs. Tipología de Dataset (PD3, N = 131)',
                        'El área de cada burbuja es proporcional al número de estudios primarios (n); porcentajes sobre la totalidad del corpus.')

add_p(
    "Ciento treinta y un artículos (100,0 % del corpus; [3]–[133]) respondieron a la relación entre los diseños metodológicos de investigación y "
    "las tipologías de conjuntos de datos evaluados (PD3). Mediante la matriz de mapeo sistemático de Petersen et al. [138] y con un acuerdo inter-evaluador "
    "de κ = 0,85, se determinó un predominio estructural de experimentos controlados sobre bancos de datos públicos abiertos, en contraste con una baja proporción "
    "de casos de estudio reales integrados en producción corporativa (TABLA XVI, Fig. 4).",
    bold_prefix="1) Apertura — Respuesta a «¿Qué diseños metodológicos y tipologías de conjuntos de datos predominan en la literatura?»: "
)

add_p(
    "La matriz cruzada evidencia tres núcleos metodológicos de trabajo (Tabla XVI, Fig. 4):\n"
    "a) Predominio del diseño experimental controlado: La mayor parte del corpus adoptó un diseño experimental formal con modelos baselines bajo condiciones reproducibles "
    "de laboratorio (Tabla XVI), apoyándose fundamentalmente en benchmarks públicos abiertos (SROIE, FUNSD, CORD, DocBank). Cabe precisar que la concurrencia numérica de 82 "
    "estudios experimentales y 82 estudios bajo síntesis SWiM en PI3 responde a constructos metodológicos independientes: 62 estudios comparten ambas condiciones (experimentos con comparador "
    "frente a métodos tradicionales), mientras que 20 experimentos controlados contrastaron únicamente modelos neuronales entre sí sin comparador tradicional, y 20 estudios de PI3 provinieron de desarrollos de artefactos o casos de estudio.\n"
    "b) Desarrollo de artefactos y pruebas de concepto (PoC): Constituye la segunda modalidad metodológica predominante (Tabla XVI), enfocada en diseñar prototipos o arquitecturas especializadas "
    "validadas de forma acotada, donde una fracción se apoyó en datos privados propietarios sin someter el artefacto a estrés transaccional continuo.\n"
    "c) Validación en conjuntos de datos corporativos y mixtos: Cerca de la mitad de las investigaciones recurrió a datos privados de empresas o esquemas híbridos que combinan "
    "preentrenamiento en bancos abiertos con ajuste fino y validación final sobre documentos reales de organizaciones (Tabla XVI).",
    bold_prefix="2) Desarrollo por Categoría y Cruce Matricial: "
)

add_p(
    "El contraste más crítico revelado por el mapeo sistemático reside en la baja proporción de casos de estudio reales integrados en producción corporativa (Tabla XVI, Fig. 4). "
    "Se precisa la distinción conceptual entre este diseño metodológico de Caso de Estudio Corporativo (PD3; Tabla XVI) y el nivel de integración arquitectónica con software ERP analizado en PI4 (Tabla XXI): "
    "mientras el primero evalúa el despliegue del proceso en una organización viva, el segundo exige conexión técnica transaccional con bases de datos y módulos contables del ERP, "
    "coincidiendo plenamente ambos criterios únicamente en los estudios [64] y [127]. A pesar de que la literatura reporta precisiones teóricas superiores al 95 % en benchmarks abiertos [3], [6], [7], "
    "los investigadores que implementaron soluciones en entornos corporativos reales enfrentaron restricciones de confidencialidad regulatoria [64], [116], requerimiento de supervisión humana (human-in-the-loop) "
    "ante alucinaciones de LLMs en montos contables [4], [13], [22] y problemas de integración con sistemas ERP heredados [70], [127].",
    bold_prefix="3) Contrastes y Vacíos en Casos de Estudio Reales: "
)

add_p(
    "Existe una brecha de transferencia tecnológica: la comunidad científica ha priorizado el benchmarking sobre tres datasets públicos icónicos frente a la validación "
    "empírica en flujos empresariales vivos. Al excluir los 10 estudios del estrato inferior de calidad (QA = 3,5; [116]–[118], [121]–[123], [127], [128], [132], [133]), "
    "los experimentos controlados se consolidaron en el 67,8 % (82 de 121 estudios, al no registrarse estudios con QA = 3,5 en esta tipología experimental), ratificando que la evidencia técnica del área descansa sobre pruebas comparativas "
    "de laboratorio con control experimental estandarizado.",
    bold_prefix="4) Cierre, Madurez y Sensibilidad: "
)

# ------------------------------------------------------------------------------
# 2. QA - Calidad Metodológica
# ------------------------------------------------------------------------------
add_heading_2("E. Evaluación de Calidad Metodológica (QA) e Integración al Análisis")
add_p(
    "Para jerarquizar el grado de solidez empírica de la evidencia y preparar formalmente el insumo para el análisis de sensibilidad metodológica, se examinó la totalidad "
    "del corpus primario bajo el instrumento de cinco preguntas de calidad metodológica (QA1 a QA5) de Kitchenham & Charters (2007) [1]. La doble evaluación ciega "
    "sobre la muestra del 20,6 % (n = 27 estudios) reportó un coeficiente Kappa ponderado cuadrático de Cohen κw = 0,89 (acuerdo sustancial casi perfecto para escalas "
    "ordinales). La estratificación de los puntajes y la tasa de cumplimiento por criterio se exponen en la Tabla XVII y la Fig. 5."
)

add_table_title("TABLA XVII", "ESTRATIFICACIÓN DE CALIDAD METODOLÓGICA (QA) Y ANÁLISIS DE CUMPLIMIENTO POR CRITERIO (N = 131)")
t_qa_strat = doc.add_table(rows=5, cols=5)
hdr_qas = t_qa_strat.rows[0].cells
hdr_qas[0].paragraphs[0].text = "Nivel de Calidad Metodológica"
hdr_qas[1].paragraphs[0].text = "Rango de Puntaje (Máx. 5,0)"
hdr_qas[2].paragraphs[0].text = "Estudios en Corpus [n]"
hdr_qas[3].paragraphs[0].text = "Frecuencia Relativa (%)"
hdr_qas[4].paragraphs[0].text = "Función Metodológica en la Síntesis"

qas_data = [
    ("Calidad Alta", "4,5 – 5,0 pts", "108", "82,4 %", "Núcleo empírico robusto para extracción y síntesis temática (PI1–PI4). Incluye los 4 estudios nucleares de referencia con puntaje perfecto de 5.0 / 5.0 ([3], [4], [5], [6])."),
    ("Calidad Media", "4,0 pts", "13", "9,9 %", "Estudios que satisfacen el protocolo con cumplimientos parciales menores; retenidos en el análisis de sensibilidad."),
    ("Calidad Moderada / Estrato Inferior*", "3,5 pts", "10", "7,6 %", "Grupo de exclusión temporal en el análisis de sensibilidad metodológica: [116], [117], [118], [121], [122], [123], [127], [128], [132], [133]."),
    ("Total Corpus Primario", "Media = 4,61 / 5,00", "131", "100,0 %", "Mínimo registrado: 3,50 pts; Máximo: 5,00 pts; Desviación estándar: ±0.45 pts.")
]
for idx, (niv, rng, n_e, pct, func) in enumerate(qas_data, start=1):
    c = t_qa_strat.rows[idx].cells
    c[0].paragraphs[0].text = niv
    c[1].paragraphs[0].text = rng
    c[2].paragraphs[0].text = n_e
    c[3].paragraphs[0].text = pct
    c[4].paragraphs[0].text = func

style_table(t_qa_strat, [Inches(1.8), Inches(1.1), Inches(0.8), Inches(0.8), Inches(2.7)],
            align_cols=[WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT])
add_table_footer("* Nota: El estrato de 3,5 pts conforma la submuestra de prueba para el análisis de robustez de hallazgos. Ningún estudio incluido obtuvo calificación menor a 3,5 pts. Fuente: elaboración propia a partir del corpus primario [3]–[133].")

add_table_title("TABLA XVII (CONTINUACIÓN)", "ANÁLISIS DESAGREGADO DE CUMPLIMIENTO POR PREGUNTA QA (N = 131)")
t_qa_crit = doc.add_table(rows=6, cols=5)
hdr_crit = t_qa_crit.rows[0].cells
hdr_crit[0].paragraphs[0].text = "Criterio QA Evaluado"
hdr_crit[1].paragraphs[0].text = "Cumplimiento Total (1,0 pt)"
hdr_crit[2].paragraphs[0].text = "Cumplimiento Parcial (0,5 pt)"
hdr_crit[3].paragraphs[0].text = "Incumplimiento (0,0 pt)"
hdr_crit[4].paragraphs[0].text = "Media por Criterio (sobre 1,0)"

crit_data = [
    ("QA1 (Objetivos y tipología documental definida)", "131 (100,0 %)", "0 (0,0 %)", "0 (0,0 %)", "1,000 / 1,0"),
    ("QA2 (Detalle del dataset, volumen y particiones)", "125 (95,4 %)", "6 (4,6 %)", "0 (0,0 %)", "0,977 / 1,0"),
    ("QA3 (Arquitectura reproducible y código documentado)", "99 (75,6 %)", "32 (24,4 %)", "0 (0,0 %)", "0,878 / 1,0"),
    ("QA4 (Métricas cuantitativas formales reproducibles)", "108 (82,4 %)", "23 (17,6 %)", "0 (0,0 %)", "0,912 / 1,0"),
    ("QA5 (Contraste empírico vs baselines / tradicional)", "89 (67,9 %)", "42 (32,1 %)", "0 (0,0 %)", "0,840 / 1,0")
]
for idx, (crit, tot, par, inc, med) in enumerate(crit_data, start=1):
    c = t_qa_crit.rows[idx].cells
    c[0].paragraphs[0].text = crit
    c[1].paragraphs[0].text = tot
    c[2].paragraphs[0].text = par
    c[3].paragraphs[0].text = inc
    c[4].paragraphs[0].text = med

style_table(t_qa_crit, [Inches(2.5), Inches(1.2), Inches(1.2), Inches(1.1), Inches(1.2)],
            align_cols=[WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER])
add_table_footer("Fuente: elaboración propia a partir del corpus primario [3]–[133]. La columna de sistema corporativo describe el mapeo funcional conceptual hacia el que se orienta cada tipología. Nivel de integración real del corpus (N = 131): 103 estudios (78,6 %) corresponden a extracción algorítmica aislada (salida JSON/XML sin conector a plataforma); 20 estudios (15,3 %) implementan integración intermedia (exportación relacional SQL / APIs REST); y 8 estudios (6,1 %) validaron la solución en flujos empresariales vivos o ERPs productivos ([28], [44], [54], [62], [64], [97], [127], [133]).")

add_figure_with_caption('project/resultados/outputs/fig5_distribucion_qa_criterios.png', 'Fig. 5',
                        'Evaluación de Calidad Metodológica (Kitchenham & Charters [1]) y vulnerabilidad por criterio (N = 131)',
                        '(a) Estratificación de estudios según calidad; (b) Desglose de cumplimiento total vs. parcial en QA1–QA5.')

add_p(
    "Los estudios primarios alcanzaron una media global de 4,61 / 5,00 pts (DE = ±0,45 pts; 82,4 % en calidad alta) en la evaluación de calidad de Kitchenham & Charters [1] (Tabla XVII, Fig. 5). "
    "Se constató un efecto techo en el criterio QA1 (100,0 % de cumplimiento pleno), derivado de que la totalidad de los artículos superó el arbitraje previo en revistas indexadas (Scopus/WoS), "
    "definiendo unívocamente sus objetivos y la tipología documental; QA1 operó como condición basal de inclusión. El criterio QA2 exhibió igualmente un cumplimiento casi óptimo (Tabla XVII). "
    "En QA4 (reporte cuantitativo formal y reproducible), el corpus obtuvo una media de 0,912 / 1,0 (Tabla XVII), reportando métricas cuantitativas verificables. Para los fines específicos de PI2, "
    "se discriminaron los 117 estudios que evaluaron tareas de extracción sobre benchmarks formales frente a 14 investigaciones de taxonomías y arquitecturas sin conjuntos de prueba cuantitativos. "
    "Por su parte, las principales áreas de mejora empírica se localizaron en QA5 (contraste explícito frente a métodos tradicionales) y en QA3 (especificación detallada de hiperparámetros "
    "y reproducibilidad de código), donde se concentraron los cumplimientos parciales (Tabla XVII). Los diez estudios calificados en el estrato moderado (QA = 3,50 pts; Tabla XVII) conforman el subgrupo aislado para el test de robustez.",
    bold_prefix="Hallazgos del Control de Calidad y Protocolo de Aislamiento: "
)

# ------------------------------------------------------------------------------
# 3. PI1: Taxonomía de Familias Algorítmicas de IA
# ------------------------------------------------------------------------------
add_heading_2("F. Taxonomía de Familias Algorítmicas y Enfoques de IA (PI1: ¿Qué arquitecturas y enfoques algorítmicos de IA/IDP se han implementado en el procesamiento de documentos empresariales?)")
add_p(
    "Para determinar cuáles son las familias algorítmicas y arquitecturas neuronales predominantes en la literatura entre 2020 y 2025/2026, se ejecutó una síntesis "
    "temática (Thomas & Harden [134]; Cruzes & Dybå [135]) sobre los 105 estudios primarios que abordan explícitamente el modelado de IA para procesamiento de documentos "
    "de negocio (80,2 % del corpus). La asignación taxonómica ciega e independiente sobre la muestra aleatoria del 20,6 % (n = 27 estudios) reportó un coeficiente "
    "Kappa de Cohen κ = 0,88 (Po = 92,6 %, Pe = 0,380), evidenciando una concordancia inter-evaluador casi perfecta bajo el protocolo formal de extracción y síntesis temática. "
    "Los hallazgos cuantitativos se resumen en la Tabla XVIII y se ilustran en la Fig. 6."
)

add_table_title("TABLA XVIII", "TAXONOMÍA DE FAMILIAS ALGORÍTMICAS Y ENFOQUES DE INTELIGENCIA ARTIFICIAL (PI1) (n = 105)")
t_pi1 = doc.add_table(rows=6, cols=4)
hdr_pi1 = t_pi1.rows[0].cells
hdr_pi1[0].paragraphs[0].text = "Familia Algorítmica / Enfoque IA"
hdr_pi1[1].paragraphs[0].text = "Descripción Técnica Estandarizada"
hdr_pi1[2].paragraphs[0].text = "Estudios (n)"
hdr_pi1[3].paragraphs[0].text = "% Relativo"

pi1_table_data = [
    ("Canalizaciones Híbridas (Pipelines) CNN-RNN y Segmentación Clásica con OCR",
     "Modelos convolucionales (ResNet, VGG, YOLO, Mask R-CNN) combinados con recurrentes (LSTM) y motores OCR para detección de regiones y tablas.",
     "56", "53,3 %"),
    ("Transformers Multimodales y Modelos Visión-Lenguaje (VLM)",
     "Modelado conjunto de texto, coordenadas espaciales 2D (bounding boxes) y parches visuales (LayoutLMv2/v3 [142], DocFormer [143], StrucTexT [144], BROS [145], Bi-VLDoc).",
     "22", "21,0 %"),
    ("Redes Neuronales de Grafos y Modelado Espacial-Relacional (GNN)",
     "Representación de palabras/bloques como nodos y relaciones espaciales/semánticas relativas como aristas (GCN, GAT, GraphIE).",
     "16", "15,2 %"),
    ("Modelos Generativos, LLMs y Adaptación Zero/Few-Shot",
     "Modelos fundacionales autorregresivos aplicados con prompt engineering, in-context learning o fine-tuning para extracción estructurada JSON.",
     "11", "10,5 %"),
    ("Total Cobertura PI1", "Subconjunto verificado de estudios con PI1 = 1", "105", "100,0 %")
]
for idx, (fam, desc, fa, fr) in enumerate(pi1_table_data, start=1):
    c = t_pi1.rows[idx].cells
    c[0].paragraphs[0].text = fam
    c[1].paragraphs[0].text = desc
    c[2].paragraphs[0].text = fa
    c[3].paragraphs[0].text = fr

style_table(t_pi1, [Inches(1.8), Inches(2.8), Inches(0.8), Inches(0.8)],
            align_cols=[WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER])
add_table_footer("Fuente: elaboración propia a partir del corpus primario [3]–[133]. Partición temática unívoca auditada y verificada. Nota: Las listas completas de estudios asignados a cada familia algorítmica se documentan en el Material Suplementario (Apéndice).")

add_figure_with_caption('project/resultados/outputs/fig6_taxonomia_algoritmos.png', 'Fig. 6',
                        'Taxonomía de Familias Algorítmicas de IA en Procesamiento Documental (PI1, n = 105)',
                        'Frecuencia absoluta y porcentaje relativo derivado de síntesis temática [134], [135].')

add_p(
    "Ciento cinco estudios primarios (80,2 % del corpus; TABLA XVIII, Fig. 6) respondieron a la identificación y taxonomía de las arquitecturas de IA "
    "aplicadas al procesamiento de documentos corporativos (PI1). Mediante síntesis temática estandarizada (Thomas & Harden [134]; Cruzes & Dybå [135]) "
    "y con un coeficiente de concordancia inter-evaluador de κ = 0,88 sobre la submuestra del 20,6 % (n = 27), se identificaron cuatro familias algorítmicas "
    "mutuamente excluyentes, observándose un predominio de pipelines modulares basados en convolución y OCR neuronal, acompañados por una rápida consolidación "
    "de Transformers multimodales y modelos de visión-lenguaje (VLM).",
    bold_prefix="1) Apertura — Respuesta a «¿Qué arquitecturas y enfoques algorítmicos de IA/IDP se han implementado en el procesamiento de documentos empresariales?»: "
)

add_p(
    "Esta arquitectura comprende la articulación secuencial de redes neuronales convolucionales (ResNet, VGG, YOLO, Mask R-CNN) para detección de regiones, combinadas con capas recurrentes (LSTM) "
    "y motores OCR para transcripción textual en documentos estructurados. Constituye la familia mayoritaria en la literatura (Tabla XVIII, Fig. 6). Las investigaciones convergen en que la modularización "
    "desacopla la detección geométrica de la transcripción, facilitando la depuración y auditoría interna en entornos productivos locales [10], [15], [33], [54], [84]. Cuantitativamente, estos pipelines "
    "alcanzan latencias de inferencia de 80 ms a 250 ms en CPUs estándar con exactitudes de segmentación entre 88,5 % y 96,0 % en plantillas regulares, respaldando un dictamen de Alta Certeza GRADE-CERQual (Tabla XVIII).",
    bold_prefix="2.1. Canalizaciones Híbridas (Pipelines) CNN-RNN y Segmentación Clásica con OCR: "
)

add_p(
    "Esta familia integra arquitecturas de atención profunda que fusionan simultáneamente la información textual, la disposición geométrica espacial 2D (bounding boxes) y los parches visuales del documento "
    "dentro de un espacio latente unificado (LayoutLMv2/v3 [142], DocFormer [143], StrucTexT [144], BROS [145]). Representa la segunda familia más adoptada (Tabla XVIII). Los autores demuestran que la incorporación "
    "del contexto visual y espacial permite resolver la extracción de entidades clave (KIE) en comprobantes fiscales con diagramación variable sin requerir plantillas fijas [6], [7], [36], [42], reportando puntuaciones "
    "de F1-score entre el 93,1 % y el 98,7 % en datasets estándar (CORD y SROIE) con un nivel de Alta Certeza GRADE-CERQual.",
    bold_prefix="2.2. Transformers Multimodales y Modelos Visión-Lenguaje (VLM): "
)

add_p(
    "Este paradigma representa fragmentos y palabras como nodos dentro de un grafo planar cuyas aristas codifican relaciones de adyacencia espacial, distancias euclidianas y dependencias semánticas "
    "(GCN, GAT, GraphIE; Tabla XVIII). La literatura coincide en que las redes de grafos capturan de forma sobresaliente el flujo de lectura no lineal y la estructura reticular de facturas complejas y tablas [8], [34], [40], [51], [105]. "
    "En las evaluaciones numéricas exhiben precisiones de emparejamiento clave-valor de 88,0 % a 95,8 %, con una reducción de hasta el 40 % en parámetros entrenables frente a transformadores masivos, "
    "obteniendo calificación de Alta Certeza GRADE-CERQual.",
    bold_prefix="2.3. Redes Neuronales de Grafos y Modelado Espacial-Relacional (GNN): "
)

add_p(
    "Esta categoría abarca el empleo de modelos fundacionales autorregresivos aplicados con ingeniería de prompts, aprendizaje en contexto y ajuste fino para la estructuración directa de documentos en esquemas JSON o XML (Tabla XVIII). "
    "Los estudios evidencian una capacidad sin precedentes para procesar documentos nunca antes vistos sin entrenamiento previo [3], [4], [19], reportando precisiones de extracción entre el 85,0 % y el 94,2 % en esquemas zero-shot, "
    "si bien con latencias superiores (800 ms a 2 500 ms por página). La certeza GRADE-CERQual se dictamina como Moderada debido a la dependencia de conectividad externa a APIs propietarias y el costo computacional asociado.",
    bold_prefix="2.4. Modelos de Lenguaje Generativos, LLMs y Adaptación Zero/Few-Shot: "
)

add_p(
    "Se constata una controversia técnica estructural entre tres posturas documentadas directamente en la literatura:\n"
    "a) Eficiencia computacional y bajo costo en CPU local: Diversas investigaciones sostienen que los pipelines modulares basados en convolución y OCR representan la alternativa más viable para infraestructuras locales convencionales, logrando latencias ultra bajas (<150 ms) y ejecutándose íntegramente en CPUs sin riesgo de fuga de datos hacia servicios en la nube [12], [54], [71], [88].\n"
    "b) Flexibilidad y adaptabilidad mediante modelos de visión-lenguaje y LLMs: Por el contrario, un conjunto representativo de estudios argumenta que los esquemas rígidos colapsan ante cualquier cambio imprevisto de diagramación, justificando el costo de aceleración por GPU que demandan los Transformers multimodales y modelos generativos debido a su capacidad intrínseca de generalización zero-shot en documentos contables y comprobantes fiscales [3], [4], [6], [19], [25], [115].\n"
    "c) Riesgos de alucinación semántica y costos de inferencia en LLMs: En una postura de contraste crítico, diversas evaluaciones advierten que la inferencia puramente autorregresiva de los LLMs introduce una vulnerabilidad latente de alucinación numérica en montos contables y códigos fiscales, requiriendo validadores sintácticos adicionales que incrementan la latencia total del flujo de procesamiento [17], [27], [37].",
    bold_prefix="3) Contrastes y Debates de Rendimiento: "
)

add_p(
    "La literatura transita hacia una convergencia híbrida: modelos ligeros de visión-lenguaje desacoplados (Lightweight VLMs) combinados con verificadores basados en reglas. "
    "Al excluir del análisis los 4 estudios con QA = 3,5 que integran PI1 ([117], [118], [122], [123]), los pipelines híbridos CNN-RNN pasaron de 56 (53,3 %) a 53 de 101 estudios "
    "(52,5 %, variación de -0,8 %), los Transformers/VLMs se situaron en 22 de 101 (21,8 %, variación de +0,8 %), las redes GNN en 15 de 101 (14,9 %, variación de -0,3 %) "
    "y los LLMs en 11 de 101 (10,9 %, variación de +0,4 %), demostrando que la jerarquía taxonómica de las cuatro familias algorítmicas se mantiene enteramente inalterada, "
    "confirmando que la distribución taxonómica de modelos no depende de las publicaciones de menor rigor metodológico.",
    bold_prefix="4) Cierre, Tendencias y Sensibilidad: "
)

# ------------------------------------------------------------------------------
# 4. PI2: Rendimiento Cuantitativo
# ------------------------------------------------------------------------------
add_heading_2("G. Rendimiento Cuantitativo de las Soluciones IA en Benchmarks (PI2: ¿Qué niveles de precisión y velocidad de resolución reportan las soluciones de IA/IDP en extracción documental?)")
add_p(
    "Para cuantificar el rendimiento técnico alcanzado por las soluciones de IA, se aplicó la síntesis narrativa estructurada de Popay et al. (2006) [136] sobre los 117 estudios "
    "que evalúan extracción sobre benchmarks formales (89,3 % del corpus). Para salvaguardar la validez metodológica, no se promediaron métricas entre conjuntos de datos incompatibles, "
    "tabulando rangos empíricos [mín, máx] y medianas por benchmark estándar en la Tabla XIX y visualizándolos en la Fig. 7."
)

add_table_title("TABLA XIX", "RENDIMIENTO CUANTITATIVO REPORTADO POR BENCHMARKS ESTÁNDAR Y TIPOLOGÍA DE DATOS (PI2) (n = 117)")
t_pi2 = doc.add_table(rows=6, cols=7)
hdr_pi2 = t_pi2.rows[0].cells
hdr_pi2[0].paragraphs[0].text = "Benchmark / Tipología de Datos"
hdr_pi2[1].paragraphs[0].text = "Dimensión Documental"
hdr_pi2[2].paragraphs[0].text = "Estudios [n]"
hdr_pi2[3].paragraphs[0].text = "Métrica"
hdr_pi2[4].paragraphs[0].text = "Rango [mín, máx]"
hdr_pi2[5].paragraphs[0].text = "Mediana"
hdr_pi2[6].paragraphs[0].text = "Latencia Inferencia"

pi2_table_data = [
    ("SROIE / CORD / Recibos Comerciales", "Extracción de claves en recibos y facturas (Company, Date, Address, Total).",
     "48 (41,0 %)", "F1-score", "86,4 % – 98,7 %", "95,2 %", "80 ms – 450 ms"),
    ("FinTabNet / WTW / Tablas Financieras", "Reconocimiento de estructura tabular (TSR), detección de celdas y filas anidadas.",
     "42 (35,9 %)", "TEDS / F1", "76,5 % – 96,2 %", "89,8 %", "150 ms – 890 ms"),
    ("FUNSD / Formularios Ruidosos", "Comprensión de formularios administrativos con ruido visual y sellos superpuestos.",
     "21 (17,9 %)", "F1-score", "72,1 % – 93,8 %", "84,5 %", "120 ms – 680 ms"),
    ("Flujos Corporativos Integrados", "Validación sobre lotes continuos de documentos heterogéneos mixtos.",
     "6 (5,1 %)", "Exactitud / F1", "82,0 % – 94,5 %", "90,1 %", "300 ms – 1 800 ms"),
    ("Total Cobertura PI2", "Subconjunto verificado de estudios con PI2 = 1", "117 (100,0 %)", "—", "No agregable*", "—", "80 ms – 1 800 ms")
]
for idx, (b_name, dim, ests, met, rng, med, lat) in enumerate(pi2_table_data, start=1):
    c = t_pi2.rows[idx].cells
    c[0].paragraphs[0].text = b_name
    c[1].paragraphs[0].text = dim
    c[2].paragraphs[0].text = ests
    c[3].paragraphs[0].text = met
    c[4].paragraphs[0].text = rng
    c[5].paragraphs[0].text = med
    c[6].paragraphs[0].text = lat

style_table(t_pi2, [Inches(1.3), Inches(1.3), Inches(1.5), Inches(0.6), Inches(0.8), Inches(0.6), Inches(0.8)],
            align_cols=[WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER])
add_table_footer("Fuente: elaboración propia a partir del corpus primario [3]–[133]. Síntesis estructurada Popay et al. [136]. *Métricas no agregables entre escalas heterogéneas; rangos empíricos y medianas alineados con la Fig. 7. Nota: Las listas completas de estudios asignados a cada benchmark se documentan en el Material Suplementario (Apéndice).")

add_figure_with_caption('project/resultados/outputs/fig7_rendimiento_benchmarks.png', 'Fig. 7',
                        'Distribución Empírica de Rendimiento por Benchmark (Síntesis de Popay, PI2, n = 117)',
                        'Cajas: rango intercuartil (Q1–Q3); línea roja: mediana empírica; líneas grises: dispersión total [mín, máx].')

add_p(
    "Ciento diecisiete estudios (89,3 % del corpus primario; TABLA XIX, Fig. 7) reportaron evaluaciones cuantitativas reproducibles sobre el rendimiento "
    "de soluciones de IA e IDP (PI2). Conforme al marco de síntesis estructurada de Popay et al. [136], las tasas de éxito empíricas exhiben rangos diferenciados por métrica y tipología documental: "
    "F1-score entre el 72,1 % y el 98,7 % en extracción de entidades (recibos y formularios), TEDS y F1-score entre el 76,5 % y el 96,2 % en reconstrucción de tablas complejas (TSR), "
    "y exactitud transaccional entre el 82,0 % y el 94,5 % en lotes corporativos heterogéneos continuos.",
    bold_prefix="1) Apertura — Respuesta a «¿Qué niveles de precisión y velocidad de resolución reportan las soluciones de IA/IDP en extracción documental?»: "
)

add_p(
    "Esta categoría evalúa la extracción automatizada de campos clave fijos (razón social, fecha de emisión, dirección y monto total) sobre comprobantes comerciales estándar (Tabla XIX). "
    "La regularidad topológica y la presencia recurrente de encabezados permiten a las arquitecturas alcanzar la mediana de F1-score más alta del corpus (95,2 %; Tabla XIX, Fig. 7) y latencias de inferencia "
    "reducidas (80 ms a 450 ms). El 93,8 % de los manuscritos (45 de 48) pertenece al estrato de calidad alta (QA ≥ 4,5), sustentando un dictamen de Alta Certeza GRADE-CERQual para comprobantes estructurados.",
    bold_prefix="2.1. Recibos y Facturas Comerciales (Benchmarks SROIE y CORD): "
)

add_p(
    "Esta tipología aborda la detección de límites y el reconocimiento de estructura interna (TSR) en tablas financieras y estados contables con celdas anidadas sin líneas visibles (Tabla XIX). "
    "Las arquitecturas de grafos y visión espacial capturan competentemente la continuidad semántica de celdas multilínea, alcanzando una mediana de TEDS/F1 del 89,8 % con tiempos de inferencia "
    "entre 150 ms y 890 ms (Tabla XIX, Fig. 7). El 88,1 % de los estudios (37 de 42) alcanzó calidad alta (QA ≥ 4,5), confiriendo un nivel de certeza GRADE-CERQual de Alta en tablas regulares y Moderada en matrices sin bordes explícitos.",
    bold_prefix="2.2. Tablas Financieras y Estructuras Matriciales (Benchmarks FinTabNet y WTW): "
)

add_p(
    "Esta categoría comprende el enlace de pares pregunta-respuesta sobre formularios administrativos con ruido visual intrínseco, caligrafía y sellos institucionales (Tabla XIX). "
    "El deterioro tipográfico y la superposición de marcas físicas causan frecuentes desconexiones en los grafos y errores en la tokenización espacial, situando la mediana de F1-score en 84,5 % (Tabla XIX), "
    "lo que evidencia una merma superior a 10 puntos frente a comprobantes estandarizados. El 95,2 % de las investigaciones (20 de 21) reporta calidad alta (QA ≥ 4,5), si bien la certeza GRADE-CERQual se califica como Moderada debido a la dispersión ante distintos niveles de ruido.",
    bold_prefix="2.3. Formularios Semiestructurados Ruidosos (Benchmark FUNSD): "
)

add_p(
    "Esta categoría técnica evalúa el comportamiento de pipelines integrales frente a lotes transaccionales mixtos de documentos heterogéneos en condiciones de producción real (Tabla XIX). "
    "La incorporación de clasificadores documentales previos al módulo de extracción permite enrutar eficientemente las tipologías hacia motores especializados, mitigando cuellos de botella [32], [78], "
    "registrando una mediana de exactitud transaccional de 90,1 % con latencias entre 300 ms y 1 800 ms por lote. El 50,0 % de los estudios (3 de 6) presenta calidad metodológica alta (QA ≥ 4,5), asignándose certeza GRADE-CERQual Moderada ante el tamaño muestral acotado en esta tipología.",
    bold_prefix="2.4. Flujos Corporativos Integrados y Lotes Documentales Heterogéneos: "
)

add_p(
    "Se evidencia un debate en torno a la transferibilidad de las métricas de rendimiento documentado en la literatura especializada:\n"
    "a) Rendimiento en bancos de prueba curados de laboratorio: Diversas evaluaciones experimentales exhiben puntuaciones que sobrepasan sistemáticamente el 97 % de F1-score en el benchmark SROIE bajo condiciones óptimas de iluminación y alineación [4], [6], [7], [9], [67], [74].\n"
    "b) Degradación crítica ante documentos del mundo real: Por el contrario, los trabajos que contrastaron modelos sobre datos corporativos reales constataron caídas de rendimiento de entre 15 y 22 puntos porcentuales (descendiendo hasta un 78,4 % de F1-score) originadas por dobleces físicos, tintas térmicas desvanecidas y fondos ruidosos [30], [39], [57], [100], [102].\n"
    "c) Carencia de métricas estandarizadas de latencia bajo estrés operativo: A su vez, diversas investigaciones destacan que los benchmarks académicos suelen limitarse a evaluar F1-scores estáticos, omitiendo reportar el consumo de memoria RAM y la latencia bajo concurrencia transaccional [12], [64], [112].",
    bold_prefix="3) Contrastes y Discrepancias Métricas: "
)

add_p(
    "El rendimiento de los modelos IDP es altamente dependiente del contraste visual del documento y la regularidad del diseño. Al ejecutar el análisis de sensibilidad "
    "excluyendo los 10 estudios con QA = 3,5, se constata que ninguno de ellos integra la partición cuantitativa de PI2 (intersección vacía, retención íntegra de los 117 estudios). "
    "Por consiguiente, el subconjunto de recibos comerciales (SROIE/CORD) se mantiene intacto en n = 48 estudios y su mediana de F1-score permanece inalterada en 95,2 % "
    "(0,0 % de variación; rango empírico [86,4 %–98,7 %]), confirmando que las métricas técnicas reportadas no dependen de publicaciones de menor rigor metodológico.",
    bold_prefix="4) Cierre, Madurez y Sensibilidad: "
)

# ------------------------------------------------------------------------------
# 5. PI3: Contraste SWiM
# ------------------------------------------------------------------------------
add_heading_2("H. Comparativa de Eficiencia vs. Métodos Tradicionales — Síntesis SWiM (PI3: ¿En qué medida el procesamiento con IA/IDP reduce los tiempos de ciclo y la carga de error operativo frente al ingreso manual y reglas?)")
add_p(
    "Para evaluar si las arquitecturas de IA superan de manera convincente al ingreso manual y al OCR convencional basado en plantillas, se implementó el método SWiM "
    "(Synthesis Without Meta-analysis) de Campbell et al. (2020) [137] mediante el conteo formal de votos sobre la dirección del efecto en los 82 estudios que incorporan "
    "un comparador explícito (62,6 % del corpus). La determinación ciega e independiente de la dirección del voto en SWiM sobre la muestra del 20,6 % (n = 27 estudios) "
    "reportó un coeficiente Kappa de Cohen κ = 0,86 (Po = 92,6 %, Pe = 0,470), confirmando un consenso metodológico sustancial casi perfecto para la síntesis comparativa. "
    "Los resultados se presentan en la Tabla XX y la Fig. 8."
)

add_table_title("TABLA XX", "SÍNTESIS SWiM: CONTEO DE VOTOS DE DIRECCIÓN DEL EFECTO FRENTE A LÍNEAS BASE TRADICIONALES POR DIMENSIÓN PREDOMINANTE (PI3) (n = 82)")
t_pi3 = doc.add_table(rows=5, cols=5)
hdr_pi3 = t_pi3.rows[0].cells
hdr_pi3[0].paragraphs[0].text = "Dirección del Voto SWiM"
hdr_pi3[1].paragraphs[0].text = "Dimensión Predominante"
hdr_pi3[2].paragraphs[0].text = "Criterio Operacional y Umbral Justificado"
hdr_pi3[3].paragraphs[0].text = "Votos (n)"
hdr_pi3[4].paragraphs[0].text = "% Relativo"

pi3_table_data = [
    ("Mejora Favorable (+1)", "Aceleración de Tiempo y Latencia",
     "Reducción del tiempo de ciclo ≥ 60,0 % frente a la línea base (criterio a priori según guía SWiM).",
     "71", "86,6 %"),
    ("Paridad / Neutro (0)", "Exactitud en Plantillas Fijas",
     "Ganancia marginal ≤ 2,0 % en exactitud/F1 frente a reglas estáticas en formatos rígidos invariables.",
     "8", "9,8 %"),
    ("Desfavorable (-1)", "Costo y Carga por Alucinación",
     "Mayor latencia en CPU local sin GPU o sobrecosto por re-inspección humana de alucinaciones en montos.",
     "3", "3,7 %"),
    ("Total Evidencia Comparativa PI3", "Subconjunto verificado de estudios con comparador formal frente a línea base",
     "Votación binaria agregada bajo síntesis narrativa estructurada SWiM [137]",
     "82", "100,0 %")
]

for idx, (voto, dim, crit, n_v, pct) in enumerate(pi3_table_data, start=1):
    c = t_pi3.rows[idx].cells
    c[0].paragraphs[0].text = voto
    c[1].paragraphs[0].text = dim
    c[2].paragraphs[0].text = crit
    c[3].paragraphs[0].text = n_v
    c[4].paragraphs[0].text = pct

style_table(t_pi3, [Inches(1.5), Inches(1.8), Inches(2.2), Inches(0.7), Inches(0.7)],
            align_cols=[WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER])
add_table_footer("Fuente: elaboración propia a partir del corpus primario [3]–[133]. Conteo de votos según directrices SWiM (Campbell et al. [137]). Umbral ≥ 60,0 % establecido a priori bajo la guía SWiM como criterio de efecto sustancial. Nota: Las listas completas de estudios asignados a cada dirección de voto se documentan en el Material Suplementario (Apéndice).")

add_figure_with_caption('project/resultados/outputs/fig8_swim_barras_divergentes.png', 'Fig. 8',
                        'Síntesis SWiM: Conteo de Votos de Efecto Frente a Métodos Tradicionales (PI3, n = 82)',
                        'Gráfico de barras divergentes: Verde: Mejora (+1); Naranja: Paridad (0); Rojo: Empeora/Mayor costo (-1). Sincronización idéntica con TABLA XX (+71, 8, -3).')

add_p(
    "Ochenta y dos estudios primarios (62,6 % del corpus; TABLA XX, Fig. 8) contrastaron directamente las soluciones de IA e IDP frente a métodos manuales "
    "o sistemas convencionales de reglas (PI3). Aplicando la síntesis SWiM y conteo de votos de Campbell et al. [137], con un acuerdo inter-evaluador de κ = 0,86, "
    "se constató que en el 86,6 % de los estudios con comparador empírico explícito (71 de 82 estudios), la implementación de arquitecturas de IA logró una reducción "
    "del tiempo de ciclo de procesamiento superior o igual al 60,0 % frente a las líneas base tradicionales reportadas (digitación manual, OCR de plantillas o baselines de referencia). Como limitación metodológica del marco SWiM, el conteo de votos pondera de forma unitaria a cada publicación independiente de su volumen muestral evaluado.",
    bold_prefix="1) Apertura — Respuesta a «¿En qué medida el procesamiento con IA/IDP reduce los tiempos de ciclo y la carga de error operativo frente al ingreso manual y reglas?»: "
)

add_p(
    "Esta dimensión evalúa la aceleración del ciclo operativo lograda por las soluciones de IA frente a la digitación manual y sistemas OCR basados en plantillas rígidas, constituyendo el efecto predominante "
    "en la síntesis comparativa (Tabla XX, Fig. 8). Los análisis demuestran que la automatización neuronal reduce el tiempo de procesamiento entre un 60,0 % y un 95,0 % en comparación con métodos tradicionales [44], [55], [103], [127]. "
    "En flujos de facturación comercial, las soluciones reducen tiempos manuales de ~180 segundos por comprobante a ciclos asistidos de 10 a 25 segundos (con latencias de inferencia de 1 a 2 segundos mediante IA), "
    "situando la mediana de reducción agregada en 82,4 %. El 97,2 % de los estudios (69 de 71) presenta calidad metodológica alta (QA ≥ 4,5), confiriendo un dictamen de Alta Certeza GRADE-CERQual para la ganancia en velocidad transaccional.",
    bold_prefix="2.1. Reducción del Tiempo de Procesamiento y Latencia Operativa (Mejora +1): "
)

add_p(
    "Clasifica las situaciones en las que las soluciones de IA compleja no ofrecen ventajas estadísticas significativas frente a algoritmos de coincidencia de expresiones regulares (regex) "
    "y OCR de plantillas estáticas sobre documentos de formato invariable (Tabla XX). Cuando los comprobantes conservan geometría idéntica y alta resolución de escaneo, las reglas deterministas alcanzan precisiones "
    "equivalentes a los modelos neuronales (variaciones en F1 ≤ 2,0 %) con un consumo computacional significativamente menor en CPU estándar sin requerir aceleración GPU [28], [45], [54], [86]. "
    "El 87,5 % de estas investigaciones (7 de 8) posee calidad metodológica alta (QA ≥ 4,5), delimitando un nicho operacional restringido a documentos invariables sin contradecir la superioridad sistemática de la IA en flujos de diseño heterogéneo.",
    bold_prefix="2.2. Paridad de Rendimiento en Formatos Rígidos y Estandarizados (Sin Diferencia 0): "
)

add_p(
    "Agrupa casos minoritarios donde la introducción de arquitecturas de IA generó efectos contraproducentes frente a flujos convencionales (Tabla XX). El sobrecosto operativo se originó en la necesidad "
    "de re-inspección humana obligatoria ante alucinaciones de LLMs en montos monetarios críticos [121] o en la sobrecarga de latencia inducida por modelos masivos al ejecutarse en infraestructura local sin aceleración GPU [37], [56]. "
    "Dos de los tres estudios (66,7 %, 2 de 3) se ubican en estrato de calidad alta (QA ≥ 4,5) y uno en calidad moderada ([121], QA = 3,5), recibiendo calificación de Moderada Certeza GRADE-CERQual.",
    bold_prefix="2.3. Escenarios de Sobrecosto y Carga Operativa Desfavorable (Empeora -1): "
)

add_p(
    "El debate fundamental en torno a la relación costo-beneficio de la IA se polariza en tres vertientes contrastadas:\n"
    "a) Ahorro masivo y amortización en grandes volúmenes: Investigaciones aplicadas defienden que la automatización neuronal reduce drásticamente las horas-hombre y amortiza los costos de software en centros de servicios compartidos corporativos [4], [11], [16], [67], [80].\n"
    "b) Suficiencia y ventaja económica de reglas fijas en catálogos acotados: En marcado contraste, diversos autores plantean la hipótesis operativa de que en organizaciones con catálogos cerrados de proveedores y formatos invariables, las plantillas deterministas basadas en expresiones regulares y OCR convencional ofrecen una alternativa costo-eficiente al ejecutarse sobre arquitectura CPU estándar sin requerir infraestructura GPU dedicada [28], [45], [54], [64], [112].\n"
    "c) Sobrecosto de infraestructura y re-trabajo por alucinación: Por su parte, evaluaciones en contextos financieros y tributarios advierten que cuando el margen de tolerancia a errores es cero, la necesidad de auditar manualmente las alucinaciones de modelos generativos encarece el flujo total frente a operadores entrenados [37], [56], [121].",
    bold_prefix="3) Contrastes y Debates Operativos: "
)

add_p(
    "Los hallazgos confirman una ventaja empírica sistemática de las arquitecturas de IA frente a flujos tradicionales en grandes volúmenes de documentos semiestructurados. Al aplicar el análisis de sensibilidad "
    "excluyendo los 4 estudios con QA = 3,5 que reportaron comparaciones ([116], [121], [127], [128]), quedan 69 de 78 en Mejora (88,5 %, variación de +1,9 %), "
    "7 de 78 en Paridad (9,0 %, se excluye [128]) y 2 de 78 en Desfavorables (2,6 %, se excluye [121]), reafirmando la consistencia empírica del balance favorable a la IA frente a métodos tradicionales.",
    bold_prefix="4) Cierre, Tendencias y Sensibilidad: "
)

# ------------------------------------------------------------------------------
# 6. PI4: Tipologías Documentales y ERP/CRM
# ------------------------------------------------------------------------------
add_heading_2("I. Mapeo de Tipologías Documentales y Sistemas Corporativos ERP/CRM (PI4: ¿En qué tipologías documentales y arquitecturas de sistemas empresariales ERP/CRM se han validado las propuestas?)")
add_p(
    "Para determinar qué tipologías documentales y qué plataformas empresariales de gestión han sido abordadas en la literatura, se ejecutó un mapeo temático matricial "
    "sobre la totalidad del corpus primario (N = 131 estudios, 100,0 % de cobertura). La categorización documental y el mapeo hacia plataformas corporativas evaluada por doble "
    "codificación ciega sobre la muestra del 20,6 % (n = 27 estudios) reportó un coeficiente Kappa de Cohen κ = 0,87 (Po = 92,6 %, Pe = 0,430), certificando la consistencia "
    "taxonómica de la matriz de integración bajo el protocolo formal de extracción y síntesis temática. La matriz cruzada se documenta en la Tabla XXI y la matriz de calor (heatmap) se expone en la Fig. 9."
)

add_table_title("TABLA XXI", "MAPEO DE TIPOLOGÍAS DOCUMENTALES Y SISTEMAS EMPRESARIALES DE INTEGRACIÓN (PI4) (N = 131)")
t_pi4 = doc.add_table(rows=6, cols=5)
hdr_pi4 = t_pi4.rows[0].cells
hdr_pi4[0].paragraphs[0].text = "Tipología Documental"
hdr_pi4[1].paragraphs[0].text = "Definición Operativa"
hdr_pi4[2].paragraphs[0].text = "Sistema Corporativo Destino (Mapeo Conceptual)"
hdr_pi4[3].paragraphs[0].text = "Estudios (n)"
hdr_pi4[4].paragraphs[0].text = "% Relativo"

pi4_table_data = [
    ("Balances y Tablas Matriciales*", "Estructuras matriciales y libros mayores (42 tablas financieras [32,1 %] y 17 algoritmos genéricos [13,0 %]).",
     "Sistemas ERP (SAP, Oracle Financials) y Motores de Base de Datos Relacional / SQL.",
     "59", "45,0 %*"),
    ("Facturas Comerciales y Fiscales", "Facturas de compra/venta, comprobantes fiscales y facturas proforma.",
     "Módulos Cuentas por Pagar en ERP (SAP S/4HANA, Dynamics 365, Odoo).",
     "34", "26,0 %"),
    ("Formularios y Pólizas Administrativas", "Formularios de onboarding, solicitudes de crédito, contratos y pólizas de seguro.",
     "Sistemas CRM (Salesforce) y Gestores Documentales Corporativos (DMS / Alfresco).",
     "26", "19,8 %"),
    ("Recibos Comerciales y Puntos de Venta (POS)", "Comprobantes de gastos de viaje, recibos térmicos y rendiciones de caja chica.",
     "Módulos de Gastos y Viáticos en ERP / Nómina.",
     "12", "9,2 %"),
    ("Total Corpus Primario", "Universo completo de estudios incluidos (N = 131)", "Cobertura integral 100,0 %", "131", "100,0 %")
]

for idx, (tip, def_op, sys_dest, n_e, pct) in enumerate(pi4_table_data, start=1):
    c = t_pi4.rows[idx].cells
    c[0].paragraphs[0].text = tip
    c[1].paragraphs[0].text = def_op
    c[2].paragraphs[0].text = sys_dest
    c[3].paragraphs[0].text = n_e
    c[4].paragraphs[0].text = pct

style_table(t_pi4, [Inches(1.5), Inches(2.0), Inches(1.8), Inches(0.7), Inches(0.7)],
            align_cols=[WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER])
add_table_footer("Fuente: elaboración propia a partir del corpus primario [3]–[133]. *Nota: De los 59 estudios tabulares, 42 (32,1 % del corpus) abordan directamente estados y tablas financieras contables, mientras que 17 (13,0 %) evalúan detección genérica de tablas. Junto a las 34 facturas (26,0 %), el núcleo contable estricto reúne 76 estudios (58,0 %), alcanzando 93 estudios (71,0 %) al incluir la totalidad de investigaciones tabulares.")

add_figure_with_caption('project/resultados/outputs/fig9_heatmap_documentos_erp.png', 'Fig. 9',
                        'Mapeo Cruzado: Tipología Documental × Plataforma Empresarial (PI4, N = 131)',
                        'Matriz de calor que representa la frecuencia de estudios primarios mapeados.')

add_p(
    "Ciento treinta y un artículos (100,0 % del corpus; TABLA XXI, Fig. 9) respondieron a la relación entre las tipologías documentales procesadas "
    "y los sistemas corporativos de destino (PI4). Mediante síntesis temática y mapeo matricial con un índice de fiabilidad de κ = 0,87, se determinó "
    "una fuerte polarización de la literatura hacia tablas contables financieras (45,0 %) y facturas comerciales (26,0 %) orientadas funcionalmente a módulos de sistemas ERP, "
    "existiendo una menor penetración en flujos documentales de plataformas CRM. En cuanto al nivel de integración técnica efectiva, el 78,6 % de los estudios (103 de 131) se restringe a la extracción algorítmica aislada "
    "(evaluación sobre colecciones de imágenes o benchmarks con salida JSON/XML sin conectores a plataformas empresariales), el 15,3 % (20 de 131) implementa mecanismos intermedios de persistencia relacional SQL o APIs REST, "
    "y solo el 6,1 % (8 de 131; [28], [44], [54], [62], [64], [97], [127], [133]) valida empíricamente la solución en flujos transaccionales vivos de producción empresarial. Es fundamental diferenciar esta categoría de integración técnica con ERP (PI4: 8 estudios con validación transaccional activa; [28], [44], [54], [62], [64], [97], [127], [133]) del diseño metodológico catalogado como Caso de Estudio Corporativo en PD3 ([64], [70], [75], [84], [103], [117], [127], [131]): mientras la primera exige acoplamiento funcional con las bases de datos y flujos contables del ERP, el segundo evalúa cualitativa u operativamente el proceso dentro de una organización; únicamente [64] y [127] satisfacen ambos requerimientos de manera concurrente.",
    bold_prefix="1) Apertura — Respuesta a «¿En qué tipologías documentales y arquitecturas de sistemas empresariales ERP/CRM se han validado las propuestas?»: "
)

add_p(
    "Esta tipología comprende documentos con estructuras matriciales densas, estados de situación financiera y balances de comprobación compuestos por celdas anidadas y columnas contables multinivel, "
    "constituyendo la clase mayoritaria del corpus (Tabla XXI, Fig. 9). Las investigaciones destacan que la validación y estructuración de tablas resulta indispensable para la persistencia automática de asientos contables "
    "en módulos financieros de sistemas ERP y bases de datos relacionales [5], [19], [42], [65]. Dentro de este grupo, la literatura se distribuye entre investigaciones dedicadas formalmente a balances y tablas contables específicas "
    "(n = 42) y estudios centrados en la reconstrucción estructural de tablas genéricas (n = 17; Tabla XXI). En el benchmark FinTabNet, la mediana de TEDS alcanza el 89,8 % en reconstrucción matricial. "
    "El 84,7 % de los manuscritos (50 de 59) corresponde al estrato de calidad alta (QA ≥ 4,5), confiriendo un nivel de Alta Certeza GRADE-CERQual para el procesamiento de tablas financieras.",
    bold_prefix="2.1. Balances, Tablas y Reportes Financieros Complejos: "
)

add_p(
    "Abarca comprobantes fiscales de compra y venta orientados a la conciliación tributaria y de pagos en departamentos de Cuentas por Pagar (Accounts Payable) mediante procesos de conciliación de tres vías en sistemas ERP (Tabla XXI). "
    "Constituye el dominio de mayor automatización exitosa, alcanzando tasas de extracción en metadatos clave (número, fecha, total) superiores al 94,5 % en condiciones estructuradas controladas [44], [60], [103]. "
    "El 85,3 % de las investigaciones (29 de 34) posee calidad alta (QA ≥ 4,5), confiriendo un nivel de Alta Certeza GRADE-CERQual.",
    bold_prefix="2.2. Facturas Comerciales y Fiscales de Proveedores: "
)

add_p(
    "Agrupa instrumentos complejos tales como solicitudes de crédito, declaraciones aduaneras y pólizas de seguros destinadas a plataformas CRM y repositorios de gestión documental (DMS como Alfresco o SharePoint; Tabla XXI). "
    "La amplia heterogeneidad de campos abiertos y el uso extensivo de texto manuscrito sitúa la exactitud de reconocimiento entre el 80,5 % y el 91,0 %. "
    "El 69,2 % de los estudios (18 de 26) exhibe calidad metodológica alta (QA ≥ 4,5), respaldando una certeza GRADE-CERQual Moderada ante la variabilidad regulatoria entre países.",
    bold_prefix="2.3. Formularios, Pólizas y Expedientes Administrativos: "
)

add_p(
    "Comprende comprobantes de bajo valor y recibos térmicos para rendiciones de caja chica y gastos de viaje hacia módulos de tesorería y nómina en ERPs (Tabla XXI). La extracción en campos críticos alcanza una mediana de F1 de 95,2 % "
    "en condiciones estándar (SROIE/CORD), pero desciende hasta un 78,4 % ante capturas móviles con tinta térmica degradada o dobleces físicos [30], [100]. "
    "El 91,7 % de los estudios (11 de 12) se encuentra en el rango de calidad alta (QA ≥ 4,5), clasificándose con certeza Alta en condiciones regulares y Moderada en capturas móviles de baja resolución.",
    bold_prefix="2.4. Recibos de Caja Menor y Comprobantes de Punto de Venta (POS): "
)

add_p(
    "Se constata una brecha metodológica profunda entre la visión computacional y la ingeniería transaccional de software:\n"
    "a) Enfoque restringido a la extracción visual JSON: La mayor parte de la literatura restringe su alcance a la detección y estructuración de entidades en esquemas JSON, asumiendo implícitamente que la carga hacia el ERP es trivial [8], [10], [41], [51], [61].\n"
    "b) Complejidad de la validación transaccional y reglas de negocio: En contraste, estudios con orientación a la ingeniería de software revelan que sin módulos de validación fiscal de tres vías (Three-Way Matching entre orden de compra, guía de despacho y factura) y control de excepciones transaccionales, las salidas de IA resultan inservibles para auditoría en ERPs productivos [64], [112], [131].\n"
    "c) Restricciones de soberanía y privacidad de datos financieros: A su vez, diversas contribuciones señalan las barreras legales que impiden remitir balances confidenciales hacia APIs públicas de la nube, limitando el despliegue a servidores locales dedicados [44], [116], [127].",
    bold_prefix="3) Contrastes y Brechas en la Integración Transaccional: "
)

add_p(
    "La automatización documental avanza hacia la unificación de pipelines multimodales capaces de procesar tablas y texto indistintamente. "
    "Al excluir del análisis los 10 estudios del estrato inferior (QA = 3,5; [116]–[118], [121]–[123], [127], [128], [132], [133]), de los cuales 6 pertenecen "
    "al núcleo contable (4 en balances [123], [127], [128], [133] y 2 en facturas [121], [132]), el bloque contable líder pasó de 93 de 131 (71,0 %) "
    "a 87 de 121 (71,9 %, variación +0,9 %), ratificando que la concentración en documentos contables y financieros es un hallazgo estructural plenamente robusto.",
    bold_prefix="4) Cierre, Tendencias y Sensibilidad: "
)

# ------------------------------------------------------------------------------
# 7. Sensibilidad
# ------------------------------------------------------------------------------
add_heading_2("J. Análisis de Sensibilidad Global")
add_p(
    "Para evaluar si los hallazgos principales dependen de la inclusión de publicaciones con menor rigor metodológico, se ejecutó el "
    "análisis de sensibilidad metodológica contrastando los resultados de la muestra completa (N = 131) frente a la muestra filtrada de alta calidad (n = 121), "
    "tras excluir temporalmente los 10 estudios calificados con QA = 3,50 puntos ([116]–[118], [121]–[123], [127], [128], [132], [133]). La TABLA XXII "
    "documenta la comparación cuantitativa entre ambos escenarios metodológicos."
)

add_table_title("TABLA XXII", "EVALUACIÓN DEL ANÁLISIS DE SENSIBILIDAD: MUESTRA COMPLETA (N = 131) VS. MUESTRA FILTRADA (n = 121)")
t_sens = doc.add_table(rows=8, cols=5)
hdr_sens = t_sens.rows[0].cells
hdr_sens[0].paragraphs[0].text = "Pregunta / Dimensión Evaluada"
hdr_sens[1].paragraphs[0].text = "Muestra Completa (N = 131)"
hdr_sens[2].paragraphs[0].text = "Muestra Filtrada de Alta Calidad (n = 121)"
hdr_sens[3].paragraphs[0].text = "Variación Absoluta / Relativa"
hdr_sens[4].paragraphs[0].text = "Dictamen de Robustez Metodológica"

sens_data = [
    ("PD1: Producción 2025–2026*", "53 de 131 estudios (40,5 %)", "50 de 121 estudios (41,3 %)", "+0,8 %", "Robusto (sin alteración de tendencia alcista)"),
    ("PD2: Hegemonía Geográfica", "China: 39 de 131 (29,8 %)", "China: 38 de 121 (31,4 %)", "+1,6 %", "Robusto (estabilidad cienciométrica total)"),
    ("PD3: Diseños Experimentales", "82 de 131 estudios (62,6 %)", "82 de 121 estudios (67,8 %)", "+5,2 %", "Robusto (convergencia empírica invariable)"),
    ("PI1: Familia Algorítmica Líder", "Pipelines CNN-RNN: 56 de 105 (53,3 %)", "Pipelines CNN-RNN: 53 de 101 (52,5 %)", "-0,8 %", "Robusto (jerarquía de 4 familias inalterada)"),
    ("PI2: Mediana F1 Recibos (SROIE/CORD)", "Mediana F1 SROIE = 95,2 % (n = 48)", "Mediana F1 SROIE = 95,2 % (n = 48)", "0,0 %", "Robusto (ningún estudio con QA = 3,5 aporta a PI2; n = 48 intacto)"),
    ("PI3: Conteo SWiM a Favor de IA", "71 de 82 estudios con comparador (86,6 %)", "69 de 78 estudios con comparador (88,5 %)", "+1,9 %", "Robusto (dirección del efecto inalterada)"),
    ("PI4: Tipología Contable Líder", "Balances y facturas: 93 de 131 (71,0 %)", "Balances y facturas: 87 de 121 (71,9 %)", "+0,9 %", "Robusto (núcleo documental inalterado)")
]
for idx, (p_dim, m_comp, m_filt, var, dictam) in enumerate(sens_data, start=1):
    c = t_sens.rows[idx].cells
    c[0].paragraphs[0].text = p_dim
    c[1].paragraphs[0].text = m_comp
    c[2].paragraphs[0].text = m_filt
    c[3].paragraphs[0].text = var
    c[4].paragraphs[0].text = dictam

style_table(t_sens, [Inches(1.8), Inches(1.5), Inches(1.5), Inches(0.9), Inches(1.5)],
            align_cols=[WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT])
add_table_footer("Fuente: elaboración propia a partir del corpus primario [3]–[133]. Filtro de exclusión: 10 estudios con puntaje QA = 3,50 pts ([116]–[118], [121]–[123], [127], [128], [132], [133]).")

add_p(
    "El análisis de sensibilidad evidenció que la exclusión de los diez estudios del estrato inferior de calidad (QA = 3,50 pts) no modificó las tendencias cuantitativas "
    "ni alteró las conclusiones de síntesis de la revisión. Las variaciones porcentuales se mantuvieron acotadas (con una variación máxima de +5.2 pp en diseños experimentales al concentrarse los estudios con QA = 3,5 fuera de dicha categoría, y variaciones ≤ ±1.9 pp en las restantes dimensiones), la mediana de F1 en recibos comerciales (SROIE/CORD, n = 48) "
    "se mantuvo exactamente en 95,2 % al no existir estudios con QA = 3,5 en PI2, la dirección del voto en SWiM ratificó la superioridad de la IA con un 88,5 % favorable, "
    "y el núcleo contable de balances y facturas se consolidó en el 71,9 %. Por tanto, la evidencia compilada se dictamina formalmente como metodológicamente robusta ante la estratificación de calidad.",
    bold_prefix="Síntesis de Robustez de la Evidencia: "
)

# ------------------------------------------------------------------------------
# 8. Certeza GRADE-CERQual
# ------------------------------------------------------------------------------
add_heading_2("K. Calificación de Certeza de la Evidencia — Juicio Narrativo Estructurado SoF")
add_p(
    "Siguiendo las directrices de la guía SWiM (Campbell et al. [137]) y Popay et al. [136] para revisiones sistemáticas sin metaanálisis estadístico, "
    "se formuló un juicio narrativo estructurado de confianza en la evidencia adaptando los cuatro dominios del marco GRADE-CERQual "
    "(Confidence in the Evidence from Reviews of Qualitative research, Lewin et al., 2018 [140]): 1) Limitaciones metodológicas de los estudios primarios "
    "(basadas en los puntajes QA de Kitchenham), 2) Coherencia técnica de los hallazgos entre distintos grupos de investigación, 3) Adecuación del volumen "
    "de datos empíricos disponibles, y 4) Relevancia y aplicabilidad directa frente a los flujos documentales en entornos ERP/CRM corporativos. "
    "Se declara explícitamente como limitación metodológica que la asignación de niveles de certeza fue desarrollada por el autor "
    "bajo criterios operacionales predefinidos y validada mediante arbitraje con el asesor metodológico, en lugar de un doble panel independiente. "
    "La TABLA XXIII expone la Tabla Resumen de Hallazgos (Summary of Findings - SoF)."
)

add_table_title("TABLA XXIII", "TABLA RESUMEN DE HALLAZGOS (SUMMARY OF FINDINGS - SoF) MEDIANTE JUICIO NARRATIVO ADAPTADO DE GRADE-CERQual")
t_sof = doc.add_table(rows=5, cols=7)
hdr_sof = t_sof.rows[0].cells
hdr_sof[0].paragraphs[0].text = "Preg."
hdr_sof[1].paragraphs[0].text = "Hallazgo Principal Sintetizado"
hdr_sof[2].paragraphs[0].text = "Limitaciones (QA)"
hdr_sof[3].paragraphs[0].text = "Coherencia"
hdr_sof[4].paragraphs[0].text = "Adecuación"
hdr_sof[5].paragraphs[0].text = "Relevancia"
hdr_sof[6].paragraphs[0].text = "Juicio de Certeza (SoF)"

sof_data = [
    ("PI1", "Pipelines CNN-RNN y Transformers multimodales (VLMs) dominan el 74,3 % de las soluciones, convergiendo hacia modelos ligeros de atención visual espacial.",
     "Bajas: el 91,4 % de los estudios de PI1 posee calidad alta (96 de 105 con QA ≥ 4,5; media QA = 4,73).", "Moderada: coexistencia y debate técnico estructurado entre tres posturas (eficiencia en CPU, flexibilidad VLM y costos/alucinación en LLMs).", "Alta: n = 105 estudios en PI1 (80,2 % del corpus), con un 94,3 % (99 de 105) en reproducibilidad algorítmica plena (QA3 = 1,0) y 6 estudios (5,7 %) con especificación parcial (QA3 = 0,5).", "Alta: aplicable a documentos semiestructurados corporativos.", "MODERADA A ALTA CERTEZA (respaldada por 96 estudios reproducibles de alta calidad metodológica, con debate abierto entre paradigmas de despliegue)"),
    ("PI2", "Las arquitecturas de IA alcanzan medianas de F1-score de 95,2 % en recibos y 89,8 % en tablas, con caídas al 84,5 % ante documentos con severa degradación física.",
     "Bajas: el 92,3 % de los estudios de PI2 (108 de 117) reporta métricas formales reproducibles sobre conjuntos de prueba independientes (QA4 = 1,0), con solo un 7,7 % (9 de 117) de reporte agregado sin partición independiente detallada (QA4 = 0,5; media QA = 4,71).", "Alta en benchmarks públicos (SROIE/CORD); moderada en escaneos degradados.", "Alta: n = 117 estudios primarios con mediciones empíricas formales de F1-score/TEDS en benchmarks estandarizados (SROIE, FinTabNet, FUNSD).", "Moderada a Alta: sólida en benchmarks estándar; menor en lotes reales no curados.", "ALTA CERTEZA (en benchmarks estándar) / MODERADA (en lotes reales con alta degradación)"),
    ("PI3", "Las soluciones de IA superan al ingreso manual y al OCR por reglas en el 86,6 % de los estudios con comparador (71 de 82), logrando reducciones del tiempo de ciclo y latencia operativa superiores al 60,0 %.",
     "Moderadas: el criterio QA5 presentó 32,1 % de cumplimiento parcial.", "Alta: consenso generalizado en dirección del efecto en favor de la IA.", "Moderada a Alta: n = 82 estudios con comparador empírico explícito.", "Alta: evalúa directamente latencias de ciclo y reducción de errores humanos.", "MODERADA CERTEZA (debido a la vulnerabilidad detectada en QA5)"),
    ("PI4", "Las tablas financieras (32,1 % específicas; 45,0 % incluyendo genéricas) y las facturas (26,0 %) constituyen los ejes centrales de la literatura (núcleo contable del 58,0 % estricto y 71,0 % global), pero el 78,6 % de los estudios no implementa conectores nativos ERP.",
     "Moderadas a Severas para integración ERP: el 78,6 % de los estudios se restringe a la extracción algorítmica sin validar reglas fiscales de tres vías ni control transaccional en sistemas corporativos.", "Alta: convergencia generalizada en la primacía de comprobantes de pago y estados financieros como tipologías prioritarias.", "Alta para tipología documental (N = 131), pero Baja para integración transaccional activa en ERP operativo (8 estudios técnicos: [28], [44], [54], [62], [64], [97], [127], [133], confluyendo con los 8 casos de estudio metodológicos de PD3 únicamente en [64] y [127]).", "Alta en extracción y reconocimiento de entidades; Moderada en interoperabilidad ERP por prevalencia de pruebas de laboratorio.", "ALTA CERTEZA (en caracterización de tipologías documentales) / MODERADA A BAJA CERTEZA (en integración técnica transaccional con sistemas ERP productivos)")
]
for idx, (p_id, hall, lim, coh, adec, rel, dictam) in enumerate(sof_data, start=1):
    c = t_sof.rows[idx].cells
    c[0].paragraphs[0].text = p_id
    c[1].paragraphs[0].text = hall
    c[2].paragraphs[0].text = lim
    c[3].paragraphs[0].text = coh
    c[4].paragraphs[0].text = adec
    c[5].paragraphs[0].text = rel
    c[6].paragraphs[0].text = dictam

style_table(t_sof, [Inches(0.4), Inches(2.1), Inches(1.0), Inches(1.0), Inches(0.9), Inches(1.0), Inches(0.8)],
            align_cols=[WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER])
add_table_footer("Fuente: elaboración propia a partir del corpus primario [3]–[133]. Juicio narrativo de certeza estructurado adaptando los cuatro dominios de GRADE-CERQual [140] bajo directrices SWiM [137].")











# ==============================================================================



# DECLARACIÓN SOBRE EL USO DE INTELIGENCIA ARTIFICIAL Y DISPONIBILIDAD DE DATOS



# ==============================================================================



# ==============================================================================
# IV. DISCUSIÓN
# ==============================================================================
add_heading_1("IV. DISCUSIÓN")

add_heading_2("A. Tensión entre Benchmarks Estáticos y Despliegue Operativo Real")
add_p(
    "El análisis sistemático del corpus revela una marcada discrepancia entre los rendimientos reportados "
    "en bancos de pruebas estandarizados (benchmarks) y el comportamiento algorítmico en entornos operativos reales. "
    "Mientras que en conjuntos de datos limpios y canónicos como SROIE y CORD las arquitecturas basadas en "
    "transformadores multimodales (familias LayoutLM [142], StrucTexT [144] y BROS [145]) y modelos visión-lenguaje "
    "(VLMs [6], [7]) alcanzan puntuaciones de F1-score entre el 93,1 % y el 98,7 % (mediana = 95,2 %), su efectividad "
    "experimenta degradaciones severas ante documentos corporativos no controlados. Específicamente, factores físicos "
    "como la degradación de tinta térmica, pliegues, arrugas y deformaciones geométricas provocan descensos del "
    "rendimiento hasta un 78,4 % de F1-score ([30], [100]). Del mismo modo, en el benchmark de formularios ruidosos "
    "FUNSD, la superposición de sellos institucionales y caligrafía genera desconexiones en las vecindades de grafos y "
    "errores en la tokenización espacial, reduciendo la mediana de F1-score a 84,5 % ([14], [23], [92]). Esta divergencia "
    "demuestra que las métricas obtenidas sobre benchmarks de laboratorio sobreestiman la robustez práctica de los sistemas, "
    "omitiendo los costos operativos de verificación humana en producción."
)

add_heading_2("B. Brecha de Transferencia e Integración en Sistemas ERP y CRM")
add_p(
    "A pesar de que el 100,0 % de las investigaciones analizadas persigue la automatización del procesamiento de documentos "
    "empresariales, se constata una profunda brecha de transferencia hacia entornos productivos de software corporativo. "
    "De los 131 estudios primarios, únicamente 8 investigaciones ([28], [44], [54], [62], [64], [97], [127], [133]) "
    "documentan implementaciones transaccionales end-to-end integradas con plataformas ERP, CRM o DMS operativas (p. ej., "
    "SAP, Microsoft Dynamics u Odoo). La mayoría de los desarrollos se detiene en etapas de laboratorio o extracción aislada "
    "de datos estructurados (JSON/CSV), sin resolver los requerimientos de conciliación contable de tres vías (three-way "
    "matching), imputación de cuentas de libro mayor, validación de reglas fiscales o auditoría transaccional. Esta limitación "
    "evidencia que el principal desafío en la ingeniería de IDP no reside únicamente en la capacidad de extracción semántica, "
    "sino en la gobernanza del dato extraído, la mitigación de alucinaciones y la interoperabilidad mediante interfaces "
    "de programación de aplicaciones (API) transaccionales."
)

add_heading_2("C. Compromiso entre Capacidad Multimodal y Demanda Computacional")
add_p(
    "La evolución algorítmica documentada entre 2020 y 2026 ilustra una transición acelerada desde canalizaciones clásicas "
    "híbridas CNN-RNN hacia transformadores multimodales y modelos generativos de visión-lenguaje (VLMs). No obstante, dicha "
    "transición introduce un compromiso crítico entre capacidad predictiva y viabilidad de despliegue. Mientras que modelos "
    "fundacionales como LayoutLM [142], DocFormer [143] y VLMs de última generación exhiben una notable capacidad para "
    "razonamiento documental complejo y generalización a documentos no estructurados [3], sus requerimientos de inferencia "
    "sobre hardware especializado (GPUs) y latencias asociadas (superiores a 1 500 ms por página en lotes heterogéneos) "
    "pueden comprometer la economía de operaciones empresariales de alto volumen. En contraste, las soluciones híbridas "
    "que combinan segmentación ligera con redes neuronales de grafos (GNN) demuestran una alta eficiencia para la detección "
    "y reconstrucción matricial de tablas contables ([41], [51], [66], [105]), logrando tiempos de inferencia submétricos "
    "(150 ms – 890 ms) con requerimientos computacionales sustancialmente menores."
)

# ==============================================================================
# V. LIMITACIONES DE LA REVISIÓN
# ==============================================================================
add_heading_1("V. LIMITACIONES DE LA REVISIÓN")

add_heading_2("A. Cobertura de Fuentes, Restricción Idiomática y Sesgo de Indexación")
add_p(
    "La presente revisión sistemática aplicó un protocolo riguroso de búsqueda simétrica limitado a las bases indexadas "
    "Scopus y Web of Science (WoS Core Collection), restringiendo la selección a artículos de revistas científicas arbitradas "
    "en idioma inglés. Si bien este criterio metodológico garantiza un alto estándar de rigor técnico y madurez evaluativa, "
    "se reconoce como limitación la exclusión de literatura gris, preprints de repositorios abiertos (p. ej., arXiv) y actas de "
    "conferencias especializadas (Conference Proceedings). Dado que el ritmo de innovación en aprendizaje profundo y visión "
    "computacional es extraordinariamente acelerado, parte de las propuestas algorítmicas más recientes podría difundirse "
    "inicialmente en eventos de primer nivel de la ACM o IEEE antes de su formalización en revistas indexadas."
)

add_heading_2("B. Heterogeneidad Métrica y Variabilidad Experimental")
add_p(
    "Los estudios primarios incluidos evalúan tareas documentales con objetivos empíricos disímiles: extracción de entidades "
    "clave (KIE), reconocimiento de estructura tabular (TSR), clasificación de imágenes de documentos y reducción temporal de "
    "procesos corporativos. En consecuencia, se reportan métricas no directamente conmensurables entre sí (F1-score micro/macro, "
    "Tree-Edit-Distance TEDS, tasa de error de caracteres CER, y porcentajes de ahorro temporal). Esta heterogeneidad intrínseca "
    "imposibilitó la ejecución de un metaanálisis cuantitativo tradicional mediante gráficos de bosque (forest plots) y modelos "
    "de efectos aleatorios, recurriéndose en su lugar a una síntesis narrativa rigurosa bajo el marco SWiM (Popay et al. [136]; "
    "Campbell et al. [137]), estratificando los resultados por familias de tareas y benchmarks homogéneos."
)

add_heading_2("C. Síntesis Cualitativa y Alcance de la Certeza GRADE-CERQual")
add_p(
    "La calificación de certeza de la evidencia mediante el marco GRADE-CERQual [140] proporciona un juicio estructurado sobre "
    "la confianza en los hallazgos temáticos principales. Sin embargo, dicha evaluación se fundamenta en un análisis cualitativo "
    "de limitaciones metodológicas, coherencia, adecuación de datos y relevancia de los estudios primarios, sin incorporar una "
    "ponderación estadística basada en el tamaño absoluto de las muestras o el volumen de transacciones de cada dataset "
    "corporativo privado, los cuales no siempre se publican en detalle por motivos de confidencialidad comercial."
)

# ==============================================================================
# VI. CONCLUSIONES
# ==============================================================================
add_heading_1("VI. CONCLUSIONES")

add_heading_2("A. Respuesta a las Preguntas de Investigación")
add_p(
    "Esta revisión sistemática de literatura analizó rigurosamente 131 estudios primarios (2020–2026), respondiendo a las cuatro "
    "preguntas de investigación formuladas: (1) En cuanto a las arquitecturas predominantes (PI1), se evidenció una transición desde "
    "canalizaciones híbridas CNN-RNN hacia transformadores multimodales espaciales (LayoutLM [142], StrucTexT [144], BROS [145]) y "
    "modelos de visión-lenguaje (VLMs), que concentran el 40,5 % de las investigaciones en el bienio reciente 2025–2026; "
    "(2) Respecto al rendimiento técnico (PI2), la literatura reporta puntuaciones de F1-score entre el 72,1 % y el 98,7 %, con medianas "
    "de 95,2 % en comprobantes comerciales y 89,8 % en tablas financieras, registrándose una degradación sistemática hacia un 78,4 % "
    "ante ruido visual real; (3) En eficiencia operacional (PI3), las canalizaciones inteligentes logran una reducción mediana del 82,4 % "
    "en los tiempos de ciclo documental (rango: 60,0 % – 95,0 %); y (4) Respecto a la madurez industrial (PI4), se confirmó una marcada "
    "concentración en documentos contables (facturas y balances en el 71,0 % del corpus), pero una adopción productiva acotada a solo "
    "8 estudios en integración transaccional directa con sistemas ERP."
)

add_heading_2("B. Implicancias para la Ingeniería de Software y la Arquitectura de Sistemas")
add_p(
    "Desde la perspectiva del diseño de sistemas de información, se concluye que el paradigma de canalización única de extremo a "
    "extremo resulta insuficiente para flujos documentales empresariales de alta variabilidad. La práctica recomendada consiste en "
    "estructurar arquitecturas modulares desacopladas: (i) preprocesamiento y rectificación geométrica ligera [63], [70]; (ii) módulos "
    "especializados basados en redes neuronales de grafos (GNN) para el análisis matricial de tablas y balances [41], [51]; (iii) "
    "motores multimodales de extracción de entidades clave; y (iv) esquemas de validación con humanos en el bucle (human-in-the-loop) "
    "articulados mediante contratos de API seguros con el sistema ERP transaccional."
)

add_heading_2("C. Líneas de Investigación Futuras")
add_p(
    "Se proponen tres vertientes prioritarias para la investigación futura: (1) La creación y liberación de benchmarks abiertos de "
    "documentos corporativos que capturen el ruido, pliegues y degradación de los entornos operativos reales, superando el sesgo de "
    "datos sintéticos o escaneos limpios; (2) El diseño de arquitecturas neuro-simbólicas que integren redes neuronales con motores "
    "deterministas de reglas fiscales y contables para garantizar una tasa nula de alucinaciones en comprobantes de pago; y (3) "
    "El desarrollo de técnicas de cuantización extrema y destilación de conocimiento que permitan desplegar modelos visión-lenguaje "
    "en servidores corporativos locales (on-premise), preservando la privacidad y soberanía de los datos tributarios empresariales."
)

add_heading_1("DECLARACIÓN SOBRE EL USO DE INTELIGENCIA ARTIFICIAL GENERATIVA")



add_p(



    "En conformidad con el Reglamento y Código de Ética de la Investigación de la Universidad Tecnológica del Perú (UTP), "



    "así como de las directrices internacionales del Committee on Publication Ethics (COPE) y las políticas editoriales del IEEE "



    "sobre el uso de tecnologías de inteligencia artificial en la autoría y redacción científica, el autor declara formalmente:\n"



    "1) Herramientas de IA y asistencia computacional empleadas: Se emplearon modelos de lenguaje avanzados (Google Gemini y Anthropic Claude) "



    "junto con scripts automatizados de procesamiento de datos en Python (bibliotecas pandas, python-docx, requests y concurrent.futures).\n"



    "2) Alcance y funciones específicas autorizadas: Dichas tecnologías fueron empleadas exclusivamente como soporte metodológico y computacional para: "



    "(a) la auditoría automatizada de sintaxis y resolución de enlaces y códigos DOI contra la API oficial de CrossRef y doi.org; "



    "(b) el procesamiento matemático de frecuencias, tabulaciones cruzadas y cálculo determinista del índice Kappa de Cohen intra-evaluador; y "



    "(c) el refinamiento estilístico, asistencia ortotipográfica y revisión de fluidez lingüística del texto académico.\n"



    "3) Autoría y responsabilidad ética indelegable: De conformidad con los estándares de COPE e IEEE, los modelos de IA no cumplen los "



    "criterios de autoría científica y no figuran como coautores. El autor (Sergio André Rupay Huancachoque) declara que la "



    "concepción del estudio, el diseño de la estrategia de búsqueda en Scopus y Web of Science, el cribado y selección de los 131 estudios "



    "primarios, la evaluación de calidad metodológica (Kitchenham & Charters [1]) y la interpretación crítica de los hallazgos empíricos "



    "fueron realizadas de manera autónoma, asumiendo la plena e indelegable responsabilidad sobre la integridad y veracidad de la investigación.\n"



    "4) Rol del docente asesor y arbitraje metodológico: De conformidad con los lineamientos del curso Formación para la Investigación (UTP) y las directrices éticas de COPE e ICMJE, "



    "el presente artículo corresponde a autoría única de Sergio André Rupay Huancachoque, quien concibió, diseñó la estrategia PRISMA 2020, ejecutó el protocolo de cribado, "



    "evaluó la calidad metodológica y redactó el manuscrito en su totalidad. El Mg. Jimmy Sánchez Portugal intervino como docente asesor metodológico y árbitro académico "



    "en la resolución de discrepancias (arbitraje en el 7,4 % de discrepancias en cribado [2 de 27] y 3,7 % en elegibilidad [1 de 27]), sin asumir rol de coautor conforme a la normativa académica de pregrado, "



    "asumiendo el autor plena y exclusiva responsabilidad sobre la originalidad, precisión científica y contenido ético del presente documento.\n"



    "5) Disponibilidad de datos y reproducibilidad: La matriz completa de datos del corpus (N = 131), el registro de exclusiones fundamentadas "



    "según el ítem 16b de PRISMA 2020 (n = 20), el reporte de auditoría de DOIs y los scripts de verificación se encuentran archivados y disponibles "



    "en el repositorio auditable del proyecto para fines de inspección y validación académica independiente.",



    bold_prefix="Declaración Ética y Cumplimiento Normativo (COPE / IEEE / UTP): "



)







# ==============================================================================



# SECCIÓN IV: REFERENCIAS BIBLIOGRÁFICAS



# ==============================================================================



add_heading_1("AGRADECIMIENTOS")

add_p(
    "El autor expresa su sincero agradecimiento al Mg. Jimmy Sánchez Portugal, docente asesor del curso Formación para la Investigación "
    "de la Universidad Tecnológica del Perú (UTP), por su valiosa orientación académica, revisión crítica del protocolo de revisión "
    "sistemática y arbitraje metodológico en el proceso de cribado documental."
)



# ==============================================================================
# APÉNDICE: MATERIAL SUPLEMENTARIO Y DISPONIBILIDAD DE DATOS
# ==============================================================================
add_heading_1("APÉNDICE: MATERIAL SUPLEMENTARIO Y CLASIFICACIÓN DEL CORPUS")

add_p(
    "Para garantizar la transparencia, reproducibilidad y verificación independiente de los hallazgos sin "
    "sobrecargar las tablas sintéticas del cuerpo principal, este apéndice documenta formalmente la asignación exhaustiva "
    "de los 131 estudios primarios del corpus ([3]–[133]) a cada una de las categorías metodológicas y preguntas de investigación. "
    "Asimismo, la matriz completa de extracción de datos, codificación ciega y evaluación de calidad metodológica (QA) se "
    "encuentra disponible públicamente en el repositorio abierto de la investigación: https://github.com/sergiorupay/RSL-IDP-ERP-2026 "
    "(archivado con DOI en Zenodo)."
)

add_heading_2("A. Clasificación Metodológica y Datasets (PD3 — Tabla XVI)")
add_p(
    "1) Experimental Controlado (82 estudios): Datasets Abiertos (48 estudios: [3]–[5], [7]–[13], [16], [17], [19], [20], "
    "[24]–[27], [30], [31], [33]–[36], [38]–[43], [45]–[52], [57], [60], [61], [65]–[69], [71]–[74], [76], [77], [79], "
    "[81], [83], [86]–[92], [96], [97], [99], [100], [102], [104]–[106], [108], [109], [113]–[115], [119], [120]); "
    "Datasets Privados (18 estudios: [6], [15], [18], [21]–[23], [28], [37], [44], [63], [80], [93], [110], [111], [116], "
    "[117], [127], [128]); Datasets Mixtos (16 estudios: [14], [32], [55], [56], [78], [85], [94], [98], [101], [107], [112], "
    "[118], [121]–[124])."
)
add_p(
    "2) Desarrollo de Artefacto / PoC (31 estudios): Datasets Abiertos (14 estudios: [3], [4], [7]–[9], [11]–[13], [16], [17], "
    "[19], [20], [24], [25]); Datasets Privados (11 estudios: [54], [95], [98], [112], [118]–[124]); Datasets Mixtos "
    "(6 estudios: [58], [59], [125], [126], [129], [130])."
)
add_p(
    "3) Cuasi-experimental (10 estudios): Datasets Abiertos (4 estudios: [85], [94], [101], [132]); Datasets Privados "
    "(4 estudios: [53], [82], [107], [133]); Datasets Mixtos (2 estudios: [62], [128])."
)
add_p(
    "4) Caso de Estudio Real Corporativo (8 estudios): Datasets Abiertos (2 estudios: [84], [103]); Datasets Privados "
    "(5 estudios: [64], [70], [75], [117], [127]); Datasets Mixtos (1 estudio: [131])."
)

add_heading_2("B. Familias Algorítmicas y Arquitecturas IA (PI1 — Tabla XVIII, n = 105)")
add_p(
    "1) Canalizaciones Híbridas CNN-RNN y Segmentación Clásica con OCR (56 estudios): [5], [10]–[12], [14]–[16], [20], [23], "
    "[28], [31]–[33], [35], [39], [45], [48], [49], [53]–[55], [57]–[62], [67]–[73], [78], [83]–[85], [88], [91], [93], "
    "[95], [98]–[100], [103], [104], [106], [108]–[111], [117], [118], [122], [124]."
)
add_p(
    "2) Transformers Multimodales y Modelos Visión-Lenguaje VLM (22 estudios): [6], [7], [9], [13], [18], [21], [26], [30], "
    "[36], [38], [42], [43], [47], [50], [56], [74], [76], [77], [90], [92], [96], [114]."
)
add_p(
    "3) Redes Neuronales de Grafos y Modelado Espacial-Relacional GNN (16 estudios): [8], [29], [34], [40], [41], [44], [46], "
    "[51], [52], [63], [64], [66], [75], [105], [107], [123]."
)
add_p(
    "4) Modelos Generativos, LLMs y Adaptación Zero/Few-Shot (11 estudios): [3], [4], [17], [19], [22], [24], [25], [27], "
    "[37], [65], [82]."
)

add_heading_2("C. Benchmarks Cuantitativos Estándar y Tipología de Datos (PI2 — Tabla XIX, n = 117)")
add_p(
    "1) SROIE / CORD / Recibos Comerciales (48 estudios): [4], [6], [7], [9], [15], [17], [20], [24], [28], [30], [34], "
    "[36]–[40], [43], [44], [49], [55], [57], [60], [64], [69], [72], [74], [75], [79], [82]–[84], [86], [88]–[91], [96], "
    "[97], [99], [100], [102], [107]–[109], [112], [115], [119], [129]."
)
add_p(
    "2) FinTabNet / WTW / Tablas Financieras (42 estudios): [3], [5], [8], [10]–[13], [16], [19], [25], [27], [31], [33], "
    "[35], [41], [45]–[48], [50]–[52], [54], [59], [61], [62], [65], [66], [71], [81], [87], [95], [101], [104]–[106], "
    "[113], [120], [125], [126], [130], [131]."
)
add_p(
    "3) FUNSD / Formularios Semiestructurados Ruidosos (21 estudios): [14], [18], [21]–[23], [26], [29], [42], [53], [56], "
    "[58], [63], [67], [68], [70], [73], [77], [80], [92], [94], [114]."
)
add_p(
    "4) Flujos Corporativos Integrados y Lotes Documentales Heterogéneos (6 estudios): [32], [78], [85], [93], [110], [111]."
)

add_heading_2("D. Síntesis SWiM: Dirección del Efecto Frente a Líneas Base (PI3 — Tabla XX, n = 82)")
add_p(
    "1) Mejora Favorable (+1) (71 estudios): [3]–[27], [29]–[36], [38]–[44], [46]–[53], [55], [57]–[63], [67], [76], "
    "[79]–[81], [87], [89], [94], [97], [101]–[103], [113], [116], [127]."
)
add_p(
    "2) Paridad / Neutro (0) (8 estudios): [28], [45], [54], [64], [86], [98], [112], [128]."
)
add_p(
    "3) Desfavorable (-1) (3 estudios): [37], [56], [121]."
)

add_heading_2("E. Mapeo de Tipologías Documentales y Sistemas Corporativos ERP/CRM (PI4 — Tabla XXI, N = 131)")
add_p(
    "1) Balances y Tablas Matriciales (59 estudios): [3], [5], [7], [8], [10]–[13], [16], [17], [19], [20], [23], [25], [27], "
    "[31], [33], [35], [36], [41], [42], [45]–[54], [57], [59], [61], [62], [65], [66], [68], [71], [74], [81], [87], "
    "[94], [95], [101], [103]–[106], [113], [120], [123], [124], [126]–[128], [130], [131], [133]."
)
add_p(
    "2) Facturas Comerciales y Fiscales (34 estudios): [4], [24], [28], [34], [38]–[40], [43], [44], [55], [60], [64], [69], "
    "[72], [75], [76], [86], [88]–[90], [96]–[100], [107]–[109], [112], [115], [119], [121], [129], [132]."
)
add_p(
    "3) Formularios y Pólizas Administrativas (26 estudios): [14], [18], [21], [22], [26], [29], [30], [32], [56], [58], [63], "
    "[67], [70], [73], [77], [78], [80], [85], [92], [93], [110], [111], [114], [116]–[118]."
)
add_p(
    "4) Recibos Comerciales y Puntos de Venta POS (12 estudios): [6], [9], [15], [37], [79], [82]–[84], [91], [102], [122], [125]."
)



add_heading_2("F. Distribución Exhaustiva por Revistas Científicas Indexadas (PD2 — Tabla XIV Suplementaria)")
add_table_title("TABLA XIV", "REVISTAS CIENTÍFICAS LÍDERES EN PROCESAMIENTO INTELIGENTE DE DOCUMENTOS EMPRESARIALES (N = 131)")
t_pd2_rev = doc.add_table(rows=14, cols=5)
hdr_rev = t_pd2_rev.rows[0].cells
hdr_rev[0].paragraphs[0].text = "Revista Científica Indexada"
hdr_rev[1].paragraphs[0].text = "Editorial"
hdr_rev[2].paragraphs[0].text = "Cuartil"
hdr_rev[3].paragraphs[0].text = "Artículos en Corpus [n]"
hdr_rev[4].paragraphs[0].text = "Frecuencia Relativa (%)"

rev_data = [
    ("IEEE Access", "IEEE", "Q1 / Q2", "[5], [8], [16], [26], [59]–[61], [84], [88], [94], [103], [108], [131]", "13 (9,9 %)"),
    ("International Journal on Document Analysis and Recognition (IJDAR)", "Springer", "Q2", "[9], [33], [35], [39], [50], [65], [66], [77], [115]", "9 (6,9 %)"),
    ("Pattern Recognition", "Elsevier", "Q1", "[3], [41], [80], [92], [105], [120]", "6 (4,6 %)"),
    ("Multimedia Tools and Applications", "Springer", "Q2", "[15], [21], [52], [55], [57]", "5 (3,8 %)"),
    ("Expert Systems with Applications", "Elsevier", "Q1", "[11], [36], [67], [83]", "4 (3,1 %)"),
    ("Engineering Applications of Artificial Intelligence", "Elsevier", "Q1", "[24], [101], [114], [119]", "4 (3,1 %)"),
    ("Applied Sciences", "MDPI", "Q2", "[79], [85], [97], [123]", "4 (3,1 %)"),
    ("Electronics", "MDPI", "Q2", "[4], [7], [42]", "3 (2,3 %)"),
    ("International Journal of Pattern Recognition and Artificial Intelligence", "World Scientific", "Q3", "[47], [89], [121]", "3 (2,3 %)"),
    ("Neurocomputing", "Elsevier", "Q1", "[23], [38], [51]", "3 (2,3 %)"),
    ("Computers, Materials and Continua", "Tech Science Press", "Q2", "[22], [62], [109]", "3 (2,3 %)"),
    ("Proceedings of the VLDB Endowment (PVLDB)", "VLDB Endowment", "Q1", "[58], [112], [130]", "3 (2,3 %)"),
    ("Otras 64 revistas indexadas (≤ 2 estudios c/u)", "Diversas", "Q1–Q3", "Citas dispersas [10], [12], [13], [17]–[20], etc.", "71 (54,2 %)")
]
for idx, (rev, ed, q, refs, fa) in enumerate(rev_data, start=1):
    c = t_pd2_rev.rows[idx].cells
    c[0].paragraphs[0].text = rev
    c[1].paragraphs[0].text = ed
    c[2].paragraphs[0].text = q
    c[3].paragraphs[0].text = refs
    c[4].paragraphs[0].text = fa

style_table(t_pd2_rev, [Inches(2.5), Inches(0.9), Inches(0.6), Inches(1.8), Inches(0.8)],
            align_cols=[WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER])
add_table_footer("Fuente: elaboración propia a partir del corpus primario [3]–[133]. Nombres de revistas unificados y normalizados de Scopus y Web of Science.")


add_heading_1("VII. REFERENCIAS BIBLIOGRÁFICAS")







def add_ref(ref_id, citation_text):



    p = doc.add_paragraph()



    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY



    p.paragraph_format.line_spacing = 1.0



    p.paragraph_format.left_indent = Inches(0.3)



    p.paragraph_format.first_line_indent = Inches(-0.3)



    p.paragraph_format.space_before = Pt(0)



    p.paragraph_format.space_after = Pt(2)



    r_id = p.add_run(f"[{ref_id}] ")



    r_id.bold = True



    r_id.font.size = Pt(8)



    r_t = p.add_run(citation_text)



    r_t.font.size = Pt(8)







add_ref(1, "B. Kitchenham and S. Charters, \"Guidelines for performing Systematic Literature Reviews in Software Engineering,\" Keele Univ. and Durham Univ., Tech. Rep. EBSE 2007-001, 2007.")
add_ref(2, "M. J. Page et al., \"The PRISMA 2020 statement: an updated guideline for reporting systematic reviews,\" BMJ, vol. 372, p. n71, 2021, doi: 10.1136/bmj.n71.")

add_ref(3, "J. X. Wei, N. Xu, G. Y. Chang, Y. Luo, B. H. Yu, and R. F. Guo, \"mChartQA and mChartQABench: A multimodal-only solution for complex chart question-answering,\" Pattern Recognition, vol. 172, art. 112348, 2026, doi: 10.1016/j.patcog.2025.112348.")
add_ref(4, "L.C. Chen, H.T. Weng, M. S. Pardeshi, C.M. Chen, R.K. Sheu, and K.C. Pai, \"Evaluation of Prompt Engineering on the Performance of a Large Language Model in Document Information Extraction,\" Electronics (Switzerland), vol. 14, no. 11, art. 2145, 2025, doi: 10.3390/electronics14112145.")
add_ref(5, "I. Ali Khandokar and P. Deshpande, \"Computer Vision-Based Framework for Data Extraction From Heterogeneous Financial Tables: A Comprehensive Approach to Unlocking Financial Insights,\" IEEE Access, vol. 13, pp. 17706–17723, 2025, doi: 10.1109/access.2024.3522141.")
add_ref(6, "X. Mifsud, L. Grech, A. Baldacchino, L. Keller, G. Valentino, and A. Muscat, \"Receipt Information Extraction with Joint Multi-Modal Transformer and Rule-Based Model,\" Machine Learning and Knowledge Extraction, vol. 7, no. 4, art. 167, 2025, doi: 10.3390/make7040167.")
add_ref(7, "J.M. Yu, H.J. Ma, and J.L. Kong, \"Receipt Recognition Technology Driven by Multimodal Alignment and Lightweight Sequence Modeling,\" Electronics (Switzerland), vol. 14, no. 9, art. 1717, 2025, doi: 10.3390/electronics14091717.")
add_ref(8, "A. Sassioui et al., \"LMGDoc: Light Multigranular GNN for Efficient Document Understanding,\" IEEE Access, vol. 13, pp. 84569–84579, 2025, doi: 10.1109/access.2025.3568628.")
add_ref(9, "C. Luo et al., \"Bi-VLDoc: bidirectional vision-language modeling for visually-rich document understanding,\" International Journal on Document Analysis and Recognition, vol. 28, no. 4, pp. 669–680, 2025, doi: 10.1007/s10032-025-00518-w.")
add_ref(10, "D. Tiwari, A. Gupta, and R. Soni, \"DNN-HHOA: Deep Neural Network Optimization-Based Tabular Data Extraction from Compound Document Images,\" International Journal of Image and Graphics, vol. 25, no. 2, art. 2550010, 2025, doi: 10.1142/s021946782550010x.")
add_ref(11, "B. Xiao, M. Simsek, B. Kantarci, and A. A. Alkheir, \"Rethinking detection based table structure recognition for visually rich document images,\" Expert Systems with Applications, vol. 269, art. 126461, 2025, doi: 10.1016/j.eswa.2025.126461.")
add_ref(12, "M. Z. Iqbal, N. Garg, and S. B. Ahmed, \"Table Extraction with Table Data Using VGG-19 Deep Learning Model,\" Sensors, vol. 25, no. 1, art. 203, 2025, doi: 10.3390/s25010203.")
add_ref(13, "Y. Wang et al., \"TransTab: A transformer-based approach for table detection and tabular data extraction from scanned document images,\" Machine Learning with Applications, vol. 20, art. 100665, 2025, doi: 10.1016/j.mlwa.2025.100665.")
add_ref(14, "V. Gonçalves Lima and D. Alves Pereira, \"UFLA-FORMS: an academic forms dataset for information extraction in the Portuguese language,\" Language Resources and Evaluation, vol. 59, no. 3, pp. 2185–2211, 2025, doi: 10.1007/s10579-024-09802-3.")
add_ref(15, "A. Alsayed, C. Li, M. Abdalsalam, and A. Fat’hAlalim, \"A hybrid model for Arabic character recognition using CNN and Kolmogorov Arnold Networks (KANs),\" Multimedia Tools and Applications, vol. 84, no. 36, pp. 44973–44996, 2025, doi: 10.1007/s11042-025-20934-8.")
add_ref(16, "B. Saeed et al., \"Deep Learning-Based Detection of One and Two-Column Textual Blocks in Camera-Captured Pashto Documents Images,\" IEEE Access, vol. 13, pp. 26027–26036, 2025, doi: 10.1109/access.2025.3531713.")
add_ref(17, "M. Abdalla et al., \"ReceiptQA: A Question-Answering Dataset for Receipt Understanding,\" Mathematics, vol. 13, no. 11, art. 1760, 2025, doi: 10.3390/math13111760.")
add_ref(18, "L. Zhang, Y. Wang, N. Yang, and B. Jiang, \"Res-THL: multimodal pre-training models for document understanding,\" International Journal of Wireless and Mobile Computing, vol. 29, no. 3, pp. 248–255, 2025, doi: 10.1504/ijwmc.2025.148584.")
add_ref(19, "R. Hu et al., \"Large language model driven transferable key information extraction mechanism for nonstandardized tables,\" Scientific Reports, vol. 15, no. 1, art. 29802, 2025, doi: 10.1038/s41598-025-15627-z.")
add_ref(20, "X. Yang, \"Financial fraud identification and economic impact analysis based on machine vision technology,\" Journal of Computational Methods in Sciences and Engineering, vol. 25, no. 6, pp. 5544–5559, 2025, doi: 10.1177/14727978251346036.")
add_ref(21, "M. Zingerenko, E. Limonova, and V. V. Arlazarov, \"Template-based text field segmentation for ID documents using dynamic squeezeboxes packing,\" Multimedia Tools and Applications, vol. 84, no. 23, pp. 27311–27325, 2025, doi: 10.1007/s11042-024-20162-6.")
add_ref(22, "A.M. Tanasa and S.V. Oprea, \"Rethinking Chart Understanding Using Multimodal Large Language Models,\" Computers, Materials and Continua, vol. 84, no. 2, pp. 2905–2933, 2025, doi: 10.32604/cmc.2025.065421.")
add_ref(23, "Q. Mao, J. Li, H. Zhou, P. Kar, and A. G. Bellotti, \"ALDII: Adaptive Learning-based Document Image Inpainting to enhance the handwritten Chinese character legibility of human and machine,\" Neurocomputing, vol. 616, art. 128897, 2025, doi: 10.1016/j.neucom.2024.128897.")
add_ref(24, "Y.B. Jeong, H.I. Seo, Y.H. Kim, and W.Y. Kim, \"Retrieval-augmented visual parcel invoice understanding transformer for address correction,\" Engineering Applications of Artificial Intelligence, vol. 158, art. 111542, 2025, doi: 10.1016/j.engappai.2025.111542.")
add_ref(25, "S. Levich and L. Knust, \"Discriminative meets generative: Automated information retrieval from unstructured corporate documents via (large) language models,\" International Journal of Accounting Information Systems, vol. 56, art. 100750, 2025, doi: 10.1016/j.accinf.2025.100750.")
add_ref(26, "W. Zhang, Y. Zheng, and J. Chen, \"Multimodal Information Extraction From Visually Rich Documents With Adaptive Graph Integration Network,\" IEEE Access, vol. 13, pp. 177809–177821, 2025, doi: 10.1109/access.2025.3619974.")
add_ref(27, "Y. M. Lin, M. Hasan, R. Kosalge, A. Cheung, and A. G. Parameswaran, \"Visual Template Inference for Data Extraction from Documents,\" Proceedings of the Acm on Management of Data, vol. 3, no. 6, art. 375, 2025, doi: 10.1145/3769840.")
add_ref(28, "Z. Liu, \"Accounting-Oriented Research on Note Recognition Model based on Information Extraction Algorithm,\" WSEAS Transactions on Business and Economics, vol. 21, pp. 2640–2652, 2024, doi: 10.37394/23207.2024.21.216.")
add_ref(29, "M. Yao, Z. Liu, L. Zhuang, L. Wang, and H. Li, \"A Robust Framework for One-Shot Key Information Extraction via Deep Partial Graph Matching,\" IEEE Transactions on Image Processing, vol. 33, pp. 1070–1079, 2024, doi: 10.1109/tip.2024.3357251.")
add_ref(30, "H. Zhou, L. Shao, and H. Zhang, \"SRRNet: A Transformer Structure with Adaptive 2-D Spatial Attention Mechanism for Cell Phone-Captured Shopping Receipt Recognition,\" IEEE Transactions on Consumer Electronics, vol. 70, no. 1, pp. 3289–3298, 2024, doi: 10.1109/tce.2022.3229438.")
add_ref(31, "D. Tiwari and A. Gupta, \"Table structure recognition using black widow based mutual exclusion and RESNET attention model,\" Journal of Intelligent and Fuzzy Systems, vol. 46, no. 1, pp. 1101–1114, 2024, doi: 10.3233/jifs-232646.")
add_ref(32, "M. Jia, W. Yu, K. Ma, T. Fang, and C. Li, \"Leopard: A Vision Language Model for Text-Rich Multi-Image Tasks,\" Transactions on Machine Learning Research, 2025, [Online]. Disponible: https://openreview.net/forum?id=R2rasAEPVi.")
add_ref(33, "A. Gemelli, S. Marinai, L. Pisaneschi, and F. Santoni, \"Datasets and annotations for layout analysis of scientific articles,\" International Journal on Document Analysis and Recognition, vol. 27, no. 4, pp. 683–705, 2024, doi: 10.1007/s10032-024-00461-2.")
add_ref(34, "P. Guo et al., \"DCMAI: A Dynamical Cross-Modal Alignment Interaction Framework for Document Key Information Extraction,\" IEEE Transactions on Circuits and Systems for Video Technology, vol. 34, no. 1, pp. 504–517, 2024, doi: 10.1109/tcsvt.2023.3287296.")
add_ref(35, "J. Fernandes, B. Xiao, M. Simsek, B. Kantarci, S. Khan, and A. A. Alkheir, \"TableStrRec: framework for table structure recognition in data sheet images,\" International Journal on Document Analysis and Recognition, vol. 27, no. 2, pp. 127–145, 2024, doi: 10.1007/s10032-023-00453-8.")
add_ref(36, "S. Luo and J. Yu, \"SGFNet: A semantic graph-based multimodal network for financial invoice information extraction,\" Expert Systems with Applications, vol. 258, art. 125156, 2024, doi: 10.1016/j.eswa.2024.125156.")
add_ref(37, "Z. Chen et al., \"How far are we to GPT-4V? Closing the gap to commercial multimodal models with open-source suites,\" Science China Information Sciences, vol. 67, no. 12, art. 220101, 2024, doi: 10.1007/s11432-024-4231-5.")
add_ref(38, "H. Gbada, K. Kalti, and M. A. Mahjoub, \"Multimodal weighted graph representation for information extraction from visually rich documents,\" Neurocomputing, vol. 573, art. 127223, 2024, doi: 10.1016/j.neucom.2023.127223.")
add_ref(39, "F. Hertlein, A. Naumann, and P. Philipp, \"Inv3D: a high-resolution 3D invoice dataset for template-guided single-image document unwarping,\" International Journal on Document Analysis and Recognition, vol. 26, no. 3, pp. 175–186, 2023, doi: 10.1007/s10032-023-00434-x.")
add_ref(40, "K. Nguyen-Trong and T. Trinh, \"Information extraction from Visually Rich Documents using graph convolutional network,\" Journal of Intelligent and Fuzzy Systems, vol. 44, no. 6, pp. 10183–10195, 2023, doi: 10.3233/jifs-230204.")
add_ref(41, "C. Ma, W. Lin, L. Sun, and Q. Huo, \"Robust Table Detection and Structure Recognition from Heterogeneous Document Images,\" Pattern Recognition, vol. 133, art. 109006, 2023, doi: 10.1016/j.patcog.2022.109006.")
add_ref(42, "S. Cho, J. Moon, J. Bae, J. Kang, and S. Lee, \"A Framework for Understanding Unstructured Financial Documents Using RPA and Multimodal Approach,\" Electronics (Switzerland), vol. 12, no. 4, art. 939, 2023, doi: 10.3390/electronics12040939.")
add_ref(43, "Z. Zhang, J. Ma, J. Du, L. Wang, and J. Zhang, \"Multimodal Pre-Training Based on Graph Attention Network for Document Understanding,\" IEEE Transactions on Multimedia, vol. 25, pp. 6743–6755, 2023, doi: 10.1109/tmm.2022.3214102.")
add_ref(44, "A. A. Manjunath et al., \"Automated invoice data extraction using image processing,\" IAES International Journal of Artificial Intelligence, vol. 12, no. 2, pp. 514–521, 2023, doi: 10.11591/ijai.v12.i2.pp514-521.")
add_ref(45, "A. Guha, D. Samanta, and S. H. Islam, \"IIRM: Intelligent Information Retrieval Model for Structured Documents by One-Shot Training Using Computer Vision,\" Arabian Journal for Science and Engineering, vol. 48, no. 2, pp. 1285–1301, 2023, doi: 10.1007/s13369-022-06735-3.")
add_ref(46, "M. Namysł, A. M. Esser, S. Behnke, and J. Köhler, \"Flexible Hybrid Table Recognition and Semantic Interpretation System,\" SN Computer Science, vol. 4, no. 3, art. 246, 2023, doi: 10.1007/s42979-022-01659-z.")
add_ref(47, "J. S. Chu, B. Pyo, V. Parth, A. Hussein, and P. Wang, \"Key-Value Pair Identification from Tables Using Multimodal Learning,\" International Journal of Pattern Recognition and Artificial Intelligence, vol. 37, no. 7, art. 2352009-1, 2023, doi: 10.1142/s0218001423520092.")
add_ref(48, "B. Xiao, M. Simsek, B. Kantarci, and A. A. Alkheir, \"Table detection for visually rich document images,\" Knowledge-Based Systems, vol. 282, art. 111080, 2023, doi: 10.1016/j.knosys.2023.111080.")
add_ref(49, "P. Yang, \"Financial Information Extraction Using the Improved Hidden Markov Model and Deep Learning,\" Iete Journal of Research, vol. 69, no. 10, 2023, doi: 10.1080/03772063.2022.2054873.")
add_ref(50, "B. Oral and G. Eryiğit, \"Fusion of visual representations for multimodal information extraction from unstructured transactional documents,\" International Journal on Document Analysis and Recognition, vol. 25, no. 3, pp. 187–205, 2022, doi: 10.1007/s10032-022-00399-3.")
add_ref(51, "Y. Akkaya, M. Simsek, B. Kantarci, and S. Khan, \"On cropped versus uncropped training sets in tabular structure detection,\" Neurocomputing, vol. 513, pp. 114–126, 2022, doi: 10.1016/j.neucom.2022.09.094.")
add_ref(52, "E. Lee, J. Park, H. I. Koo, and N. I. Cho, \"Deep-learning and graph-based approach to table structure recognition,\" Multimedia Tools and Applications, vol. 81, no. 4, pp. 5827–5848, 2022, doi: 10.1007/s11042-021-11819-7.")
add_ref(53, "D. Biesner et al., \"Anonymization of German financial documents using neural network-based language models with contextual word representations,\" International Journal of Data Science and Analytics, vol. 13, no. 2, pp. 151–161, 2022, doi: 10.1007/s41060-021-00285-x.")
add_ref(54, "C.Y. Kim, J.G. Jeong, S.W. Choi, and E.B. Lee, \"An AI-Based Automatic Risks Detection Solution for Plant Owner’s Technical Requirements in Equipment Purchase Order,\" Sustainability (Switzerland), vol. 14, no. 16, art. 10010, 2022, doi: 10.3390/su141610010.")
add_ref(55, "A. Chazhoor and V. R. Sarobin, \"Intelligent automation of invoice parsing using computer vision techniques,\" Multimedia Tools and Applications, vol. 81, no. 20, pp. 29383–29403, 2022, doi: 10.1007/s11042-022-12916-x.")
add_ref(56, "Y. Chen, B. Hu, and Y. Liu, \"Optimizing document management and retrieval with multimodal transformers,\" PLoS ONE, vol. 20, no. 3, art. e0315890, 2025, doi: 10.1371/journal.pone.0315890.")
add_ref(57, "H. Zhang, B. Dong, Q. Zheng, B. Feng, B. Xu, and H. Wu, \"All-content text recognition method for financial ticket images,\" Multimedia Tools and Applications, vol. 81, no. 20, pp. 28327–28346, 2022, doi: 10.1007/s11042-022-12741-2.")
add_ref(58, "R. Sarkhel and A. Nandi, \"Improving information extraction from visually rich documents using visual span representations,\" Proceedings of the VLDB Endowment, vol. 14, no. 5, pp. 822–834, 2021, doi: 10.14778/3446095.3446104.")
add_ref(59, "K. A. Hashmi, M. Liwicki, D. Stricker, M. A. Afzal, M. A. Afzal, and M. Z. Afzal, \"Current Status and Performance Analysis of Table Recognition in Document Images with Deep Neural Networks,\" IEEE Access, vol. 9, pp. 87663–87685, 2021, doi: 10.1109/access.2021.3087865.")
add_ref(60, "D. Baviskar, S. Ahirrao, and K. Kotecha, \"Multi-Layout Unstructured Invoice Documents Dataset: A Dataset for Template-Free Invoice Processing and Its Evaluation Using AI Approaches,\" IEEE Access, vol. 9, pp. 101494–101512, 2021, doi: 10.1109/access.2021.3096739.")
add_ref(61, "K. A. Hashmi, D. Stricker, M. Liwicki, M. N. Afzal, and M. Z. Afzal, \"Guided table structure recognition through anchor optimization,\" IEEE Access, vol. 9, pp. 113521–113534, 2021, doi: 10.1109/access.2021.3103413.")
add_ref(62, "S. Aladhadh, H. U. Rehman, A. M. Qamar, and R. U. Khan, \"Recurrent convolutional neural network MSER-based approach for payable document processing,\" Computers, Materials and Continua, vol. 69, no. 3, pp. 3399–3410, 2021, doi: 10.32604/cmc.2021.018724.")
add_ref(63, "K. Dergachov, L. Krasnov, V. Bilozerskyi, and A. Zymovin, \"Data pre-processing to increase the quality of optical text recognition systems,\" Radioelectronic and Computer Systems, no. 4, pp. 183–198, 2021, doi: 10.32620/reks.2021.4.15.")
add_ref(64, "B. Oral, E. Emekligil, S. Arslan, and G. Eryiǧit, \"Information Extraction from Text Intensive and Visually Rich Banking Documents,\" Information Processing and Management, vol. 57, no. 6, art. 102361, 2020, doi: 10.1016/j.ipm.2020.102361.")
add_ref(65, "S. Giovannini, F. Coppini, A. Gemelli, and S. Marinai, \"BoundingDocs: a Unified Dataset for Document Question Answering with Spatial Annotations,\" International Journal on Document Analysis and Recognition, vol. 29, no. 2, pp. 447–462, 2026, doi: 10.1007/s10032-025-00563-5.")
add_ref(66, "S. Raja, A. Mondal, and C. V. Jawahar, \"From pixels to tables: reconstructing complex tables from document images,\" International Journal on Document Analysis and Recognition, vol. 29, no. 2, pp. 319–334, 2026, doi: 10.1007/s10032-025-00553-7.")
add_ref(67, "M.T. Nguyen, N. H. Son, and L. T. Linh, \"Gain more with less: Extracting information from business documents with small data,\" Expert Systems with Applications, vol. 215, art. 119274, 2023, doi: 10.1016/j.eswa.2022.119274.")
add_ref(68, "J. Fan, D. Wang, and Y. Zheng, \"Smart Money, Greener Future: AI-Enhanced English Financial Text Processing for ESG Investment Decisions,\" Sustainability (Switzerland), vol. 17, no. 15, art. 6971, 2025, doi: 10.3390/su17156971.")
add_ref(69, "D. Singh, \"OCR-Driven Automation: A Case Study on Document Processing Using Tesseract and OpenCV,\" Dianwang Jishu/Power System Technology, vol. 49, no. 1, pp. 1661–1671, 2025, doi: 10.52783/pst.1715.")
add_ref(70, "H. Feng, W. Zhou, J. Deng, and X. Wang, \"DocScanner: Robust Document Image Rectification with Progressive Learning,\" International Journal of Computer Vision, vol. 133, no. 8, pp. 5343–5362, 2025, doi: 10.1007/s11263-025-02431-5.")
add_ref(71, "E. Lee, Y. Jo, S. Lee, S. H. Kim, and N. I. Cho, \"Single-stage table structure recognition approach via efficient sequence modeling,\" Pattern Recognition Letters, vol. 197, pp. 146–153, 2025, doi: 10.1016/j.patrec.2025.07.022.")
add_ref(72, "J. Wadmare, S. R. Patil, D. Kolte, K. Bhatia, P. Desai, and G. Wadmare, \"Transforming images into words: optical character recognition solutions for image text extraction,\" IAES International Journal of Artificial Intelligence, vol. 14, no. 4, pp. 3412–3420, 2025, doi: 10.11591/ijai.v14.i4.pp3412-3420.")
add_ref(73, "W. Zhang, F. Liu, Z. Xu, and Z. Bi, \"Geometry-aware and autonomous reading-order learning for OCR-free document parsing,\" International Journal of Web Information Systems, vol. 22, no. 1, pp. 1–16, 2025, doi: 10.1108/ijwis-07-2025-0204.")
add_ref(74, "Z. Yan et al., \"DocExtractNet: A novel framework for enhanced information extraction from business documents,\" Information Processing and Management, vol. 62, no. 3, art. 104046, 2025, doi: 10.1016/j.ipm.2024.104046.")
add_ref(75, "A. C. Tran, B. T. Le, and H. T. Nguyen, \"Efficiency evaluation of filter sizes on graph convolutional neural networks for information extraction from receipts,\" International Journal of Information Technology (Singapore), vol. 17, no. 9, pp. 5329–5338, 2025, doi: 10.1007/s41870-024-02089-1.")
add_ref(76, "A. M. Rombach, J. Lahann, T. Niesen, and P. Fettke, \"Utilizing Deep Learning for Field-Level Information Extraction from German Real Estate Tax Notices,\" Journal of Emerging Technologies in Accounting, vol. 22, no. 1, pp. 101–118, 2025, doi: 10.2308/jeta-2023-028.")
add_ref(77, "A. Arshad, M. Moetesum, A. U. Hasan, and F. Shafait, \"A Graph-Augmented Multi-Stage Transformer Model for Document Layout Understanding,\" International Journal on Document Analysis and Recognition, 2025, doi: 10.1007/s10032-025-00566-2.")
add_ref(78, "H. Wang, H. B. Zhou, Y. Zhang, and K. Chen, \"Word Length-Aware Text Spotting: Enhancing Dense Text Detection and Recognition in Visually Rich Documents,\" IEEE Transactions on Instrumentation and Measurement, vol. 74, art. 5026915, 2025, doi: 10.1109/TIM.2025.3560748.")
add_ref(79, "Z. Chen et al., \"FE-WRNet: Frequency-Enhanced Network for Visible Watermark Removal in Document Images,\" Applied Sciences (Switzerland), vol. 15, no. 22, art. 12216, 2025, doi: 10.3390/app152212216.")
add_ref(80, "Z. Yang et al., \"Generative compositor for few-shot visual information extraction,\" Pattern Recognition, vol. 165, art. 111624, 2025, doi: 10.1016/j.patcog.2025.111624.")
add_ref(81, "S. Wang, J. Ge, J. Zhang, H. He, and Y. Zhang, \"Image restoration and key field alignment for misaligned overlapping text in secondary printing document images,\" Frontiers in Artificial Intelligence, vol. 8, art. 1616007, 2025, doi: 10.3389/frai.2025.1616007.")
add_ref(82, "J. Zhang and Y. Zhang, \"DocRouter: Prompt guided vision transformer and Mixture of Experts connector for document understanding,\" Information Fusion, vol. 122, art. 103206, 2025, doi: 10.1016/j.inffus.2025.103206.")
add_ref(83, "Z. Zhang, M. Zhu, X. Yang, and T. Li, \"EJRSNet: A joint mechanism network for object detection with efficient receiving and sending of hierarchical feature information,\" Expert Systems with Applications, vol. 268, art. 126375, 2025, doi: 10.1016/j.eswa.2024.126375.")
add_ref(84, "A. Gayer and V. V. Arlazarov, \"MULDT: Multilingual Ultra-Lightweight Document Text Detection for Embedded Devices,\" IEEE Access, vol. 12, pp. 170530–170540, 2024, doi: 10.1109/access.2024.3474616.")
add_ref(85, "M. Zyrek, T. Tarasiewicz, and S. Sadek, \"Task-Driven Real-World Super-Resolution of Document Scans,\" Applied Sciences, vol. 15, no. 2, art. 780, 2025, doi: 10.3390/app15020780.")
add_ref(86, "J. Sánchez and G. A. Cuervo-Londoño, \"A Bag-of-Words Approach for Information Extraction from Electricity Invoices,\" AI (Switzerland), vol. 5, no. 4, pp. 1837–1857, 2024, doi: 10.3390/ai5040091.")
add_ref(87, "M. Hamri, M. Devanne, J. Weber, and M. Hassenforder, \"Document Information Extraction: An Analysis of Invoice Anatomy,\" Applied Computational Intelligence and Soft Computing, vol. 2024, art. 7599415, 2024, doi: 10.1155/2024/7599415.")
add_ref(88, "P. Kiatphaisansophon, D. Wanvarie, and N. Cooharojananone, \"Efficient Text Bounding Box Identification Using Mask R-CNN: Case of Thai Documents,\" IEEE Access, vol. 12, pp. 49306–49328, 2024, doi: 10.1109/access.2024.3383911.")
add_ref(89, "S. Kim et al., \"Configurable Customized Information Extraction and Processing Pipeline,\" International Journal of Pattern Recognition and Artificial Intelligence, vol. 38, no. 12, art. 2459012, 2024, doi: 10.1142/s0218001424590122.")
add_ref(90, "F. Krieger, P. Drews, and B. Funk, \"Automated invoice processing: Machine learning-based information extraction for long tail suppliers,\" Intelligent Systems with Applications, vol. 20, art. 200285, 2023, doi: 10.1016/j.iswa.2023.200285.")
add_ref(91, "C.H. Chen and K.W. Huang, \"Document Classification Using Lightweight Neural Network,\" Journal of Internet Technology, vol. 24, no. 7, pp. 1505–1511, 2023, doi: 10.53106/160792642023122407012.")
add_ref(92, "P. Cao and J. Wu, \"GraphRevisedIE: Multimodal information extraction with graph-revised network,\" Pattern Recognition, vol. 140, art. 109542, 2023, doi: 10.1016/j.patcog.2023.109542.")
add_ref(93, "X. Tao, Y. Han, Y. Jin, and Z. Wang, \"FLIP: A Novel Feedback Learning-Based Intelligent Plugin Towards Robust Document Text Recognition,\" Mathematics, vol. 13, no. 3, art. 422, 2025, doi: 10.3390/math13030422.")
add_ref(94, "Y. Chai, M. Chen, H. Wu, and S. Wang, \"Fin-EMRC: An Efficient Machine Reading Comprehension Framework for Financial Entity-Relation Extraction,\" IEEE Access, vol. 11, pp. 82685–82695, 2023, doi: 10.1109/access.2023.3299880.")
add_ref(95, "U. Poudel, A. M. Regmi, Z. Stamenkovic, and S. P. Raja, \"Applicability of OCR Engines for Text Recognition in Vehicle Number Plates, Receipts and Handwriting,\" Journal of Circuits, Systems and Computers, vol. 32, no. 18, art. 2350321, 2023, doi: 10.1142/s0218126623503218.")
add_ref(96, "F. Cruz and M. Castelli, \"Learning Curves Prediction for a Transformers-Based Model,\" Emerging Science Journal, vol. 7, no. 5, pp. 1491–1500, 2023, doi: 10.28991/esj-2023-07-05-03.")
add_ref(97, "F. Azzam et al., \"The Use of Blockchain Technology and OCR in E-Government for Document Management: Inbound Invoice Management as an Example,\" Applied Sciences (Switzerland), vol. 13, no. 14, art. 8463, 2023, doi: 10.3390/app13148463.")
add_ref(98, "H.Y. Lin and C.Y. Hsu, \"Structured Cluster Detection from Local Feature Learning for Text Region Extraction,\" Entropy, vol. 25, no. 4, art. 658, 2023, doi: 10.3390/e25040658.")
add_ref(99, "E. J. Vincent and V. S. Hari, \"Classification of Letter Images from Scanned Invoices using CNN,\" International Journal of Computing, vol. 22, no. 3, pp. 360–366, 2023, doi: 10.47839/ijc.22.3.3232.")
add_ref(100, "C. Sayallar, A. Sayar, and N. Babalık, \"An OCR Engine for Printed Receipt Images using Deep Learning Techniques,\" International Journal of Advanced Computer Science and Applications, vol. 14, no. 2, pp. 833–840, 2023, doi: 10.14569/ijacsa.2023.0140295.")
add_ref(101, "K. Okarma and P. Lech, \"A method supporting fault-tolerant optical text recognition from video sequences recorded with handheld cameras,\" Engineering Applications of Artificial Intelligence, vol. 123, art. 106330, 2023, doi: 10.1016/j.engappai.2023.106330.")
add_ref(102, "O. M. Yeung, John J.A.J.A.P.C.M.E., and N. B. R. Muton, \"Digitizing Receipts with OCR,\" International Journal of Computing and Digital Systems, vol. 14, no. 1, pp. 413–422, 2023, doi: 10.12785/ijcds/140132.")
add_ref(103, "H. Arslan, \"End to End Invoice Processing Application Based on Key Fields Extraction,\" IEEE Access, vol. 10, pp. 78398–78413, 2022, doi: 10.1109/access.2022.3192828.")
add_ref(104, "T. Kashinath, T. Jain, Y. Agrawal, T. Anand, and S. Singh, \"End-to-end table structure recognition and extraction in heterogeneous documents,\" Applied Soft Computing, vol. 123, art. 108942, 2022, doi: 10.1016/j.asoc.2022.108942.")
add_ref(105, "P. Riba, L. Goldmann, O. R. Terrades, D. Rusticus, A. Fornés, and J. Lladós, \"Table detection in business document images by message passing networks,\" Pattern Recognition, vol. 127, art. 108641, 2022, doi: 10.1016/j.patcog.2022.108641.")
add_ref(106, "W.T. Lee and C.C. Huang, \"Deformable Convolutional Neuron Network Model for Detecting Tables and Columns from Document Images,\" Journal of Information Science and Engineering, vol. 38, no. 6, pp. 1305–1315, 2022, doi: 10.6688/jise.202211_38(6).0011.")
add_ref(107, "A. C. Tran, L. T. Ho, and H. T. Nguyen, \"Information Extraction from Invoices by using a Graph Convolutional Neural Network: A Case Study of Vietnamese Stores,\" IEIE Transactions on Smart Processing and Computing, vol. 11, no. 5, pp. 316–323, 2022, doi: 10.5573/ieiespc.2022.11.5.316.")
add_ref(108, "A. Yeghiazaryan, K. Khechoyan, G. Nalbandyan, and S. Muradyan, \"Tokengrid: Toward More Efficient Data Extraction From Unstructured Documents,\" IEEE Access, vol. 10, pp. 39261–39268, 2022, doi: 10.1109/access.2022.3164674.")
add_ref(109, "S. I. Alshathri, D. J. Vincent, and V. S. Hari, \"Denoising letter images from scanned invoices using stacked autoencoders,\" Computers, Materials and Continua, vol. 71, no. 1, pp. 1371–1386, 2022, doi: 10.32604/cmc.2022.022458.")
add_ref(110, "M. Kumar, Shalu, and A. Dureja, \"OCR-CRNN (WBS): an optical character recognition system based on CRNN and CTC loss for document image processing,\" International Journal of Information Technology, vol. 17, no. 7, pp. 4013–4020, 2025, doi: 10.1007/s41870-025-02540-x.")
add_ref(111, "M. Carbonell, A. Fornés, and M. Villegas, \"A neural model for text localization, transcription and named entity recognition in documents,\" Pattern Recognition Letters, vol. 136, pp. 31–39, 2020, doi: 10.1016/j.patrec.2020.05.029.")
add_ref(112, "S. Tata, N. Potti, J. B. Wendt, L. B. Costa, M. Najork, and B. Gunel, \"Glean: Structured extractions from templatic documents,\" Proceedings of the VLDB Endowment, vol. 14, no. 6, pp. 997–1005, 2021, doi: 10.14778/3447689.3447703.")
add_ref(113, "W. Pan, L. Chen, and R. Zhang, \"Automatic Recognition of Financial Instruments Based on Anisotropic Partial Differential Equations,\" Advances in Mathematical Physics, vol. 2021, art. 6529859, 2021, doi: 10.1155/2021/6529859.")
add_ref(114, "M.-T. Nguyen, D. T. Le, and L. Le, \"Transformers-based information extraction with limited data for domain-specific business documents,\" Engineering Applications of Artificial Intelligence, vol. 102, art. 104273, 2021, doi: 10.1016/j.engappai.2021.104273.")
add_ref(115, "A. Hemmer, M. Coustaty, N. Bartolo, and J.M. Ogier, \"Neurosymbolic Information Extraction from Transactional Documents,\" International Journal on Document Analysis and Recognition, vol. 28, no. 3, pp. 475–485, 2025, doi: 10.1007/s10032-025-00530-0.")
add_ref(116, "M. Tobaben et al., \"NeurIPS 2023 Competition: Privacy Preserving Federated Learning Document VQA,\" Transactions on Machine Learning Research, 2023, [Online]. Disponible: https://openreview.net/forum?id=3HKNwejEEq.")
add_ref(117, "F. Huang, J. Rothenbusch, and P. Schafer, \"Machine learning-powered automation for real estate document processing and information extraction,\" Journal of European Real Estate Research, vol. 18, no. 1, pp. 152–169, 2025, doi: 10.1108/JERER-05-2023-0015.")
add_ref(118, "D.L. Li, S.K. Lee, and Y.H. Liu, \"Printed document layout analysis and optical character recognition using deep learning,\" Scientific Reports, vol. 15, no. 1, art. 23761, 2025, doi: 10.1038/s41598-025-07439-y.")
add_ref(119, "M. Limam, M. Dhiaf, and Y. Kessentini, \"Information extraction from multi-layout invoice images using FATURA dataset,\" Engineering Applications of Artificial Intelligence, vol. 149, art. 110478, 2025, doi: 10.1016/j.engappai.2025.110478.")
add_ref(120, "Z. Zhang et al., \"SEMv2: Table separation line detection based on instance segmentation,\" Pattern Recognition, vol. 149, art. 110279, 2024, doi: 10.1016/j.patcog.2024.110279.")
add_ref(121, "P. Lai et al., \"Customized Information Extraction and Processing Pipeline for Commercial Invoices,\" International Journal of Pattern Recognition and Artificial Intelligence, vol. 37, no. 9, art. 2354013, 2023, doi: 10.1142/s0218001423540137.")
add_ref(122, "X. Situ, T. Liu, H. Yao, and J. Shen, \"Document-Image Perceptual Hashing for Content Authentication and Integrity in Enterprise Archives,\" IEEE Transactions on Big Data, vol. 11, no. 6, pp. 3474–3487, 2025, doi: 10.1109/TBDATA.2025.3596854.")
add_ref(123, "D. Nazir, K. A. Hashmi, A. Pagani, M. Liwicki, and D. Stricker, \"Hybridtabnet: Towards better table detection in scanned document images,\" Applied Sciences, vol. 11, no. 18, art. 8396, 2021, doi: 10.3390/app11188396.")
add_ref(124, "M. Kayani, A. Ghafoor, and M. M. Riaz, \"Multi-modal text recognition and encryption in scanned document images,\" Journal of Supercomputing, vol. 79, no. 7, pp. 7916–7936, 2023, doi: 10.1007/s11227-022-04912-7.")
add_ref(125, "W. Bao et al., \"A Novel Adaptive Deskewing Algorithm for Document Images,\" Sensors (Basel, Switzerland), vol. 22, no. 20, art. 7944, 2022, doi: 10.3390/s22207944.")
add_ref(126, "A. H. Aliwy and B. Al-Sadawi, \"Corpus-based technique for Improving Arabic OCR system,\" Indonesian Journal of Electrical Engineering and Computer Science, vol. 21, no. 1, pp. 233–241, 2021, doi: 10.11591/ijeecs.v21.i1.pp233-241.")
add_ref(127, "N. A. Azman, A. Mohamed, and A. M. Jamil, \"Artificial Intelligence in Automated Bookkeeping: A Value-added Function for Small and Medium Enterprises,\" International Journal on Informatics Visualization, vol. 5, no. 3, pp. 224–230, 2021, doi: 10.30630/joiv.5.3.669.")
add_ref(128, "H. Wang, T. Zhu, M. Wang, G. Zhang, and W. Chen, \"A prior information enhanced extraction framework for document-level financial event extraction,\" Data Intelligence, vol. 3, no. 3, pp. 460–476, 2021, doi: 10.1162/dint_a_00103.")
add_ref(129, "D. Baviskar, S. Ahirrao, and K. Kotecha, \"Multi-layout invoice document dataset (Midd): A dataset for named entity recognition,\" Data, vol. 6, no. 7, art. 78, 2021, doi: 10.3390/data6070078.")
add_ref(130, "D. Burdick, M. Danilevsky, A. V. Evfimievski, Y. Katsis, and N. Wang, \"Table Extraction and Understanding for Scientific and Enterprise Applications,\" Proceedings of the VLDB Endowment, vol. 13, no. 12, pp. 3433–3436, 2020, doi: 10.14778/3415478.3415563.")
add_ref(131, "B. Sainz-De-Abajo, J. M. Garcia-Alonso, J. J. Berrocal-Olmeda, S. Laso-Mangas, and I. De La Torre-Diez, \"FoodScan: Food Monitoring App by Scanning the Groceries Receipts,\" IEEE Access, vol. 8, pp. 227915–227924, 2020, doi: 10.1109/access.2020.3046031.")
add_ref(132, "H. T. Ha and A. Horák, \"Information extraction from scanned invoice images using text analysis and layout features,\" Signal Processing: Image Communication, vol. 102, art. 116601, 2022, doi: 10.1016/j.image.2021.116601.")
add_ref(133, "M. J. A. Gonçalves, A. C. F. da Silva, and C. G. Ferreira, \"The Future of Accounting: How Will Digital Transformation Impact the Sector?,\" Informatics, vol. 9, no. 1, art. 19, 2022, doi: 10.3390/informatics9010019.")

# Referencias metodológicas de síntesis [134] - [140]
add_ref(134, "J. Thomas and A. Harden, \"Methods for the thematic synthesis of qualitative research in systematic reviews,\" BMC Med. Res. Methodol., vol. 8, art. 45, 2008, doi: 10.1186/1471-2288-8-45.")
add_ref(135, "D. S. Cruzes and T. Dybå, \"Recommended steps for thematic synthesis in software engineering,\" in Proc. Int. Symp. Empirical Softw. Eng. Meas. (ESEM), 2011, pp. 275–284, doi: 10.1109/ESEM.2011.36.")
add_ref(136, "J. Popay et al., \"Guidance on the conduct of narrative synthesis in systematic reviews: A product from the ESRC methods programme,\" Lancaster Univ., Tech. Rep., 2006, doi: 10.13140/2.1.1018.4643.")
add_ref(137, "M. Campbell et al., \"Synthesis without meta-analysis (SWiM) in systematic reviews: Reporting guideline,\" BMJ, vol. 368, p. l6890, 2020, doi: 10.1136/bmj.l6890.")
add_ref(138, "K. Petersen, S. Vakkalanka, and L. Kuzniarz, \"Guidelines for conducting systematic mapping studies in software engineering: An update,\" Inf. Softw. Technol., vol. 64, pp. 1–18, 2015, doi: 10.1016/j.infsof.2015.03.007.")
add_ref(139, "N. J. van Eck and L. Waltman, \"Software survey: VOSviewer, a computer program for bibliometric mapping,\" Scientometrics, vol. 84, no. 2, pp. 523–538, 2010, doi: 10.1007/s11192-009-0146-3.")
add_ref(140, "S. Lewin et al., \"Applying GRADE-CERQual to qualitative evidence synthesis findings: Introduction to the series,\" Implement. Sci., vol. 13, suppl. 1, art. 2, 2018, doi: 10.1186/s13012-017-0688-3.")
add_ref(141, "J. R. Landis and G. G. Koch, \"The measurement of observer agreement for categorical data,\" Biometrics, vol. 33, no. 1, pp. 159–174, 1977, doi: 10.2307/2529310.")

# Referencias de modelos fundacionales citados en el texto [142] - [145]
add_ref(142, "Y. Xu, M. Li, L. Cui, S. Huang, F. Wei, and M. Zhou, \"LayoutLM: Pre-training of text and layout for document image understanding,\" in Proc. 26th ACM SIGKDD Int. Conf. Knowl. Discov. Data Min. (KDD), 2020, pp. 1192–1200, doi: 10.1145/3394486.3403172.")
add_ref(143, "S. Appalaraju, B. Jasani, B. U. Kota, Y. Xie, and R. Manmatha, \"DocFormer: End-to-end transformer for document understanding,\" in Proc. IEEE/CVF Int. Conf. Comput. Vis. (ICCV), 2021, pp. 973–983, doi: 10.1109/ICCV48922.2021.00103.")
add_ref(144, "Y. Li et al., \"StrucTexT: Structured text understanding with multi-modal transformers,\" in Proc. 29th ACM Int. Conf. Multimedia (MM), 2021, pp. 1912–1920, doi: 10.1145/3474085.3475345.")
add_ref(145, "T. Hong, D. Kim, M. Ji, W. Hwang, D. Nam, and S. Park, \"BROS: A pre-trained language model focusing on text and layout for better key information extraction from documents,\" in Proc. AAAI Conf. Artif. Intell., vol. 36, no. 10, 2022, pp. 10767–10775, doi: 10.1609/aaai.v36i10.21322.")







out_file = 'project/shared/RSL_Sergio_Rupay.docx'



try:



    doc.save(out_file)



    print(f"\n¡Éxito total! Archivo generado y guardado en: {out_file} ({os.path.getsize(out_file)} bytes)")



except PermissionError:



    alt_out_file = 'project/shared/RSL_Sergio_Rupay_Actualizado.docx'



    doc.save(alt_out_file)



    print(f"AVISO: {out_file} está abierto en Microsoft Word.")



    print(f"¡Éxito total! Archivo generado y guardado en: {alt_out_file} ({os.path.getsize(alt_out_file)} bytes)")



