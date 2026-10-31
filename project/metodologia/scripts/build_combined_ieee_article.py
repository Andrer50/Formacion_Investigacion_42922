"""



Script maestro para compilar el artículo científico completo en formato IEEE:

            

"Articulo_RSL_Introduccion_y_Metodologia_IEEE.docx" en project/shared/







Contiene las 4 secciones fundamentales con estándar Scopus Q1/Q2 y Guía ATI3 superados:



- I. INTRODUCCIÓN (Contexto, Brecha, Justificación, Objetivos, PICOC, Preguntas PI/PD - Tablas I y II)



- II. METODOLOGÍA (PRISMA 2020, Ecuación, Criterios CIE, QA Kitchenham, Excluidos PRISMA 2020, Nucleares, Enlace - Tablas III a XII, Fig. 1)



- III. RESULTADOS (PD1-PD3, QA Paso 6, PI1-PI4 en 4 bloques normativos, Sensibilidad Paso 8, GRADE-CERQual SoF Paso 9 - Tablas XIII a XXIII, Figs. 2 a 9)



- IV. REFERENCIAS BIBLIOGRÁFICAS (140 referencias rigurosas IEEE [1] a [140] en 2 columnas)



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
    "3,701 registros en Scopus y Web of Science, consolidando tras cribado formal un corpus primario de N = 131 artículos "
    "de revista revisados por pares. Los resultados indican que los transformers multimodales y Vision-Language Models "
    "alcanzan puntajes F1 entre 72.1 % y 98.7 % (mediana de 95.2 % en comprobantes estructurados y 84.5 % en formularios "
    "degradados). La síntesis por conteo de votos (SWiM) ratifica la superioridad de la IA sobre los métodos tradicionales "
    "en 71 de 82 estudios comparativos (86.6 %), con una reducción media de tiempo de procesamiento del 82.4 % (rango: "
    "60.0 % a 95.0 %); no obstante, se registraron 8 casos de paridad y 3 desfavorables por costos de GPU y alucinaciones. "
    "Finalmente, se constata una brecha de adopción crítica: solo el 6.1 % del corpus (8 estudios) validó soluciones "
    "integradas en producción corporativa real."
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
    "En la era de la transformación digital, las organizaciones empresariales procesan diariamente volúmenes ingentes "
    "de documentos semiestructurados y no estructurados, tales como facturas de proveedores, recibos de caja, notas de crédito, "
    "órdenes de compra y extractos bancarios. Históricamente, la captura, transcripción y verificación de estos comprobantes ha "
    "dependido de la intervención manual humana o de sistemas tradicionales de Reconocimiento Óptico de Caracteres (OCR) basados "
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
    "ricos (Visually Rich Documents - VRD), alcanzando puntajes F1 y exactitudes que oscilan entre 72.1 % y 98.7 % en benchmarks públicos estandarizados [3], [4], [6]."
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



    bold_prefix="2) Sesgos y Desconexión de los Benchmarks: "



)



add_p(



    "A diferencia de las revisiones secundarias previas identificadas en la literatura (compiladas en la Tabla VIII), las cuales se restringen a "



    "taxonomías teóricas o panoramas cualitativos sobre bancos de prueba aislados, existe una marcada escasez de estudios primarios que aborden "



    "la integración transaccional de extremo a extremo entre los pipelines de IDP y los sistemas empresariales corporativos (ERP, CRM y DMS). "



    "La literatura tiende a dar por sentada la interoperabilidad de datos, omitiendo la evaluación concurrente de latencia en tiempo real, "



    "consumo de recursos (GPU vs. CPU) y protocolos de arbitraje humano en el bucle (Human-in-the-Loop) en entornos operativos reales [70], [84], [127].",



    bold_prefix="3) Aislamiento Transaccional con Sistemas ERP: "



)







add_heading_2("C. Motivación, Pregunta Maestra y Objetivos")



add_p(



    "La rápida evolución tecnológica acumulada entre 2020 y 2025 exige una consolidación metodológica rigurosa que sirva de guía a "



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



    "2) Cuantificar el desempeño empírico alcanzado en benchmarks públicos y privados según las métricas estándar de extracción y reconocimiento (PI2).\n"



    "3) Evaluar comparativamente el grado de mejora y eficiencia de los modelos de IA frente al OCR convencional y métodos basados en reglas (PI3).\n"



    "4) Clasificar las tipologías documentales empresariales y evaluar su grado de validación e integración en plataformas ERP/CRM corporativas (PI4)."



)







add_heading_2("D. Estructura del Documento")



add_p(



    "El artículo se estructura de la siguiente manera: la Sección II detalla la Metodología de la Revisión Sistemática (protocolo, marco PICOC, "



    "estrategia de búsqueda calibrada, criterios de inclusión/exclusión, flujo PRISMA 2020, control de calidad Kitchenham, matriz de exclusión PRISMA 2020 y mapeo de síntesis); "



    "la Sección III expone los Resultados empíricos estructurados en cuatro bloques analíticos en respuesta a las preguntas directas e indirectas de investigación; "



    "la Declaración Ética formaliza el uso responsable de tecnologías de IA generativa y la disponibilidad de datos; y la Sección IV compendia las Referencias Bibliográficas en formato IEEE estricto."



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



    "delimitando el dominio a sistemas empresariales corporativos estrictamente privados (ERP, CRM, DMS), excluyendo expedientes clínicos "



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



    ("PD3", "¿Qué diseños metodológicos y tipologías de datasets (públicos vs. privados) predominan en la literatura?", "Madurez empírica y reproducibilidad")



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



    "descartada por dos deficiencias metodológicas críticas: (a) un 28.5 % de contaminación semántica en la muestra piloto (75 de los 263 registros "



    "brutos correspondían a estudios neurofisiológicos de potenciales evocados en electroencefalogramas, EEG) y (b) la omisión inadvertida de la literatura moderna "



    "de KIE, modelos de visión-lenguaje y comprensión de documentos visualmente ricos (VRD). Para subsanar esto, se diseñó la Iteración 2 (calibrada definitiva, archivada en "



    "el repositorio metodológico auditable de datos primarios), la cual expandió los términos a expresiones compuestas ('enterprise resource planning' OR 'ERP system*'), "



    "incorporó operadores booleanos para modelos de visión-lenguaje y limitó la tipología documental estrictamente a artículos de revista arbitrados "



    "(Document Type = Article). Esta calibración recuperó 3,270 registros brutos en Scopus y 431 en WoS (3,701 brutos), que tras filtros nativos de plataforma "



    "se redujeron a 311 y 266 registros respectivamente (total n = 577), optimizando la especificidad temático-empresarial y la exhaustividad del rastreo.",



    bold_prefix="Evolución y Calibración Metodológica de Ecuaciones (Iteración 1 vs. Iteración 2): "



)







add_p(



    "Dentro del corpus primario se identifican tres artículos ([3] Wei et al., [65] Giovannini et al., y [66] Raja et al.) cuya fecha de "



    "asignación formal a volumen de revista impresa figura con año 2026. Se precisa que dichos registros fueron publicados oficialmente "



    "en línea en modalidad Early Access / Advance Online Publication entre agosto y diciembre de 2025; por consiguiente, tanto Scopus como "



    "Web of Science Core Collection los indexaron legítimamente dentro del período de rastreo, cumpliendo estrictamente con el criterio de inclusión "



    "IN1 (publicación en línea 2020–2025) y los estándares de reporte de PRISMA 2020 [2].",



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



    "ecuaciones fueron estrictamente simétricas en su arquitectura booleana y conceptual, se constató una notable disparidad en los volúmenes brutos "



    "iniciales (3,270 en Scopus frente a 431 en WoS). Esta asimetría en las tasas de reducción (-90.5 % en Scopus frente a -38.3 % en WoS) responde a "



    "las marcadas diferencias estructurales de indexación: Scopus indexa una masiva literatura de actas de congresos (Conference Proceedings de IEEE, "



    "ACM y Springer LNCS) y series monográficas previas a 2020 que saturan los resultados de IA documental; al aplicar los filtros nativos de tipo documental "



    "(Document Type = Article) y ventana temporal 2020–2025, se depuraron 2,938 publicaciones de actas y años previos, quedando 332 registros y "



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



hdr[2].paragraphs[0].text = "Años + Doc."



hdr[3].paragraphs[0].text = "Idioma"



hdr[4].paragraphs[0].text = "Exportado"



hdr[5].paragraphs[0].text = "Reducción"







reg_data = [



    ("Scopus (TITLE-ABS-KEY)", "3,270", "332", "311", "311", "-90.5 %"),



    ("WoS Core Coll. (TS)*", "431", "386", "266", "266", "-38.3 %"),



    ("Total Consolidado", "3,701", "718", "577", "577", "-84.4 %")



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



    "*Nota metodológica: En WoS el filtro temporal arrojó 386 registros, reduciéndose a 266 tras aplicar simultáneamente tipo Article e idioma inglés/español. "



    "Los 577 registros consolidados se encuentran archivados en scopus_export_it2.csv (n = 311) y wos_export_it2.xls (n = 266).",



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



    ("IN1", "Inclusión", "Ventana temporal de publicación en línea comprendida entre 2020 y 2025 (incluye artículos Early Access publicados en línea en 2025 con volumen asignado a 2026).", "Filtros nativos en Scopus y Web of Science."),



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



    "Los procesos de cribado, evaluación y extracción fueron conducidos por el autor principal aplicando un protocolo estandarizado de "



    "fiabilidad intra-evaluador test-retest a ciegas (con un intervalo de separación temporal de tres semanas entre la primera y segunda evaluación), "



    "conforme a las directrices metodológicas de Kitchenham & Charters [1] y los estándares de reporte de PRISMA 2020 [2]. "



    "Para la fase de cribado por título y resumen se evaluó una muestra de n = 27 registros (8.0 % de los 338 registros únicos, incluyendo estudios incluidos y excluidos), "



    "alcanzando una proporción de acuerdo observado Po = 92.6 % (25 de 27 acuerdos) y un coeficiente de fiabilidad Kappa de Cohen κ = 0.81 "



    "(IC95%: [0.55, 1.00], clasificado como casi perfecto al ser κ ≥ 0.81). En la fase de elegibilidad a texto completo (n = 27, 9.1 % de los 297 textos completos), se obtuvo "



    "Po = 96.3 % (26 de 27 acuerdos) y un κ = 0.87 (IC95%: [0.61, 1.00]), ratificando una estabilidad casi perfecta. "



    "En la extracción de variables sobre el corpus final (n = 27, 20.6 % de N = 131), la fiabilidad test-retest alcanzó κ = 0.89 en familias algorítmicas (PI1) "



    "y κ = 0.80 en dirección de efecto SWiM (PI3). Las discrepancias marginales (7.4 % en cribado [2 de 27] y 3.7 % en elegibilidad [1 de 27]) fueron resueltas y dirimidas "



    "en sesiones de arbitraje metodológico supervisadas por el docente asesor experto (Mg. Jimmy Sánchez Portugal), mitigando el sesgo del evaluador único; "



    "no obstante, se declara explícitamente como limitación metodológica del estudio la no realización de un doble cribado independiente en paralelo.",



    bold_prefix="Protocolo de Fiabilidad Intra-Evaluador y Arbitraje Metodológico: "



)



add_p(



    "1) Fase 1 (Identificación): Se identificaron inicialmente 3,701 registros brutos en Scopus (3,270) y WoS (431). "



    "Tras aplicar filtros automatizados de plataforma (tipo de documento artículo y cobertura 2020–2026), se retuvieron "



    "577 artículos de revista (311 en Scopus y 266 en WoS). Posteriormente, el algoritmo de deduplicación "



    "por DOI estandarizado y título normalizado eliminó 239 duplicados (238 inter-base y 1 intra-WoS), ingresando 338 registros únicos a cribado."



)



add_p(



    "2) Fase 2 (Cribado): Bajo protocolo de fiabilidad intra-evaluador test-retest ciego (κ = 0.81, IC95%: [0.55, 1.00]), se excluyeron 41 registros por ruido temático (35 por ámbito clínico/histórico "



    "EX4 y 6 sin reporte de métricas empíricas EX-n), pasando 297 estudios a evaluación a texto completo."



)



add_p(



    "3) Fase 3 (Elegibilidad): Se examinaron los 297 textos completos aplicando los criterios de elegibilidad y el instrumento QA (Kitchenham), "



    "con fiabilidad test-retest κ = 0.87 (IC95%: [0.61, 1.00]) y arbitraje docente. Se excluyeron 166 registros: 20 estudios candidatos con justificación "



    "individual detallada bajo el ítem 16b de PRISMA 2020 [2] (ver Tabla VIII) y 146 registros descartados bajo la causal operativa IN4 / EX-n "



    "(investigaciones de OCR genérico de caracteres o visión por computadora sin validación en flujos documentales empresariales, cuyo inventario "



    "completo se encuentra depositado en el repositorio auditable del estudio). El QA operó como instrumento de caracterización y estratificación, "



    "constatándose que todos los estudios que satisficieron los criterios temáticos superaron holgadamente el umbral formal de QA >= 3.0 / 5.0."



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



    ("1. Identificación", "3,701 brutos", "Filtros nativos de plataforma (artículo, 2020–2026)", "-3,124 no elegibles", "577 exportados"),



    ("2. Deduplicación", "577 exportados", "Cruce determinista por DOI y título normalizado", "-239 dupl.", "338 únicos"),



    ("3. Cribado", "338 únicos", "Evaluación de título/resumen con test-retest (κ = 0.81)", "-41 temáticos", "297 elegibles"),



    ("4. Elegibilidad", "297 texto compl.", "Lectura de texto completo y control QA (κ = 0.87)", "-166 estudios", "131 incluidos"),



    ("5. Inclusión", "131 primarios", "Mapeo semántico frente a PI1–PI4 y extracción", "0", "N = 131 final"),



    ("Corpus Total", "3,701 brutos", "Embudo metodológico PRISMA 2020 reproducible", "-3,570 excluidos", "N = 131 final")



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



        "(con protocolo de fiabilidad test-retest ciego y arbitraje metodológico, κ = 0.87) e inclusión estratificada de estudios primarios (N = 131)."



    )



    r_cap_txt.font.size = Pt(8)







add_heading_2("H. Evaluación de Calidad Metodológica (QA)")



add_p(



    "Siguiendo las pautas de Kitchenham & Charters (2007) [1], se formuló un instrumento de calidad metodológica compuesto por cinco "



    "preguntas críticas (QA1 a QA5), evaluadas bajo una escala tricotómica objetiva (1.0 = Sí, 0.5 = Parcial, 0.0 = No) con un umbral "



    "mínimo de protocolo fijado a priori en QA >= 3.0 / 5.0 (ver Tabla VII). Dicho instrumento no operó como un filtro de exclusión fáctico "



    "(dado que la totalidad de los estudios que satisficieron los criterios temáticos superaron holgadamente el corte, con un puntaje mínimo observado "



    "de 3.50), sino como una herramienta de caracterización descriptiva, estratificación de evidencia y base para el análisis de sensibilidad. "



    "El corpus primario alcanzó una media de calidad metodológica de 4.61 / 5.0 (DE = ±0.41), con los cuatro estudios nucleares obteniendo la "



    "calificación máxima de 5.0 / 5.0."



)







add_table_title("TABLA VII", "PREGUNTAS DEL INSTRUMENTO DE CALIDAD METODOLÓGICA (QA)")



t_qa = doc.add_table(rows=6, cols=3)



hdr = t_qa.rows[0].cells



hdr[0].paragraphs[0].text = "Cód."



hdr[1].paragraphs[0].text = "Pregunta de Control de Calidad Metodológica"



hdr[2].paragraphs[0].text = "Criterio de Calificación Tricotómica"







qa_data = [



    ("QA1", "¿El estudio define explícitamente los objetivos, el problema documental y la tipología de documentos de negocio?", "1.0: Objetivos y tipología explícitos; 0.5: Genéricos; 0.0: No definidos."),



    ("QA2", "¿Se describe detalladamente el dataset (volumen, partición train/test, idioma y condiciones de escaneo)?", "1.0: Dataset y partición explícitos; 0.5: Parcial; 0.0: No describe dataset."),



    ("QA3", "¿Se documenta con suficiente claridad la arquitectura neuronal de IA o el pipeline de IDP implementado?", "1.0: Arquitectura completa y reproducible; 0.5: Superficial; 0.0: Enfoque caja negra."),



    ("QA4", "¿Se reportan métricas cuantitativas formales de rendimiento (F1-score, exactitud, latencia, throughput)?", "1.0: Métricas formales reportadas; 0.5: Métricas parciales; 0.0: Solo cualitativo."),



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



    "En estricto cumplimiento del ítem 16b de la declaración PRISMA 2020 [2], de los 166 registros descartados en la fase de elegibilidad a texto completo, "



    "la Tabla VIII lista individualmente los 20 estudios candidatos que a priori abordaban la problemática pero no satisficieron los requerimientos de "



    "elegibilidad primaria (8 revisiones secundarias EX3, 7 sin métricas cuantitativas empíricas EX-n y 5 sin acceso a texto completo EX2), "



    "consignando sus autores completos, base de origen, código y justificación técnica sin truncamientos. Los 146 registros restantes fueron excluidos "



    "bajo el criterio IN4 / EX-n por corresponder a modelos de OCR genérico a nivel de carácter o visión artificial sin validación en tipologías "



    "documentales de negocio (facturas, recibos, formularios o balances); su catálogo bibliográfico auditable completo (corpus_eligibility_excluded_146.csv) "



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
    "máxima (QA = 5.0 / 5.0) y cobertura integral de las cuatro preguntas temáticas (PI1 a PI4). Para conformar un núcleo de referencia "
    "cualitativa profunda y calibración analítica sin incurrir en redundancias, se aplicó un embudo operativo sistemático basado en "
    "muestreo de máxima variación (Maximum Variation Sampling) bajo cinco criterios sucesivos: (i) calidad metodológica máxima "
    "(QA = 5.0 / 5.0); (ii) cobertura temática integral estricta de las cuatro preguntas formuladas (4/4 PIs); (iii) pertenencia a la "
    "frontera temporal más reciente del corpus (bienio 2025–2026, subconjunto de 25 estudios); (iv) indexación en revistas Q1/Q2 "
    "en Scopus / Web of Science; y (v) representatividad disjunta sobre las cuatro tipologías documentales cardinales de negocio y familias "
    "algorítmicas de PI1. Siguiendo este protocolo se seleccionaron cuatro estudios nucleares ([3], [4], [5], [6]). Respecto al estudio [3] (Wei et al.), "
    "se aclara que su selección obedece a la necesidad metodológica de modelar la tipología de gráficos analíticos, diagramas estadísticos y tablas complejas "
    "embebidas en memorias financieras y reportes corporativos de negocio, donde la comprensión documental excede el texto lineal y exige "
    "razonamiento visual multimodal. Esta tipología se complementa armónicamente con órdenes y comprobantes de compra B2B ([4]), balances "
    "financieros tabulares heterogéneos ([5]) y recibos comerciales transaccionales B2C ([6]) (ver Tabla IX). Por su parte, las redes neuronales de grafos (GNN), "
    "al no contar con un estudio primario en la frontera 2025–2026 con QA = 5.0 que cubriera simultáneamente las 4 PIs, se analizan exhaustivamente dentro "
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



    ("[S001]", "[3]", "Wei et al. (2026/2025)", "Pattern Recognition (Elsevier, Q1)", "10.1016/j.patcog.2025.112348", "VLM multimodal para QA visual sobre gráficos analíticos y tablas complejas en reportes corporativos, superando baselines de OCR tradicional."),



    ("[S002]", "[4]", "Chen et al. (2025)", "Electronics (MDPI, Q2)", "10.3390/electronics14112145", "Evaluación rigurosa de LLMs e ingeniería de prompts en extracción de información documental frente a reglas fijas."),



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



    "distinguiéndose conceptualmente de la calidad metodológica (QA de Kitchenham), en la cual 108 estudios alcanzaron calidad alta (QA >= 4.5 pts). "



    "La relación biunívoca matemática entre el identificador del corpus [Sxxx] y la cita IEEE [n] está regida estrictamente por "



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



    "[3]–[133] se estructuran y consolidan mediante métodos rigurosos y formalizados según la naturaleza de cada interrogante: "



    "Síntesis Temática (Thomas & Harden [134]; Cruzes & Dybå [135]) para la taxonomía algorítmica y tipologías documentales (PI1, PI4); "



    "Síntesis Narrativa Estructurada (Popay et al. [136]) con reporte de rangos empíricos [mín, máx] y dispersión por benchmark para el rendimiento "



    "técnico (PI2); Síntesis sin metaanálisis (SWiM, Campbell et al. [137]) con conteo de votos de dirección del efecto y barras divergentes para la "



    "comparativa de eficiencia frente a métodos tradicionales (PI3); Mapeo Sistemático con gráficos de burbujas (Petersen et al. [138]) para el cruce "



    "de diseños y datasets (PD3); análisis cienciométrico con mapas de coocurrencia de palabras clave en VOSviewer (van Eck & Waltman [139]) para redes de "



    "investigación (PD2); y calificación formal de la certeza de la evidencia mediante el marco GRADE-CERQual (Lewin et al. [140]). "



    "Se descarta formalmente la ejecución de un metaanálisis estadístico de efectos fijos o aleatorios debido a la profunda heterogeneidad técnica, "



    "métrica y contextual del dominio de Information Extraction en documentos empresariales: (a) heterogeneidad métrica: los estudios evalúan el "



    "rendimiento a niveles de granularidad conceptualmente incompatibles (exactitud de OCR a nivel de carácter/token mediante CER/WER frente a KIE a "



    "nivel de entidad semántica completa mediante F1-score estricto vs. relajado y ANLS en preguntas y respuestas visuales); (b) heterogeneidad de "



    "entornos de ejecución: las latencias y velocidades de inferencia reportadas (ms/página) dependen de infraestructuras de hardware dispares "



    "(desde clústeres NVIDIA A100/H100 hasta servidores locales sin GPU acelerada), imposibilitando un pool homogéneo de tiempos; y (c) disparidad de "



    "corpus de validación: mientras una fracción de autores evalúa sobre benchmarks públicos (SROIE, CORD, FUNSD), una porción sustancial valida sus "



    "arquitecturas en datasets corporativos cerrados y propietarios no estandarizados, los cuales no reportan intervalos de confianza ni desviaciones "



    "estándar requeridas para un modelo metaanalítico combinado. En consecuencia, la síntesis estructurada por preguntas de investigación "



    "constituye el enfoque epistemológicamente riguroso y apropiado.",



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



    ("Sesgo de Selección", "Omisión de literatura relevante o sesgo por formato de publicación.", "Búsqueda simétrica en Scopus y Web of Science. Restricción estricta a artículos de revista científica arbitrados (Journal Articles) conforme a las directrices de investigación institucional para garantizar rigor y madurez metodológica. Se declara explícitamente como una limitación mayor el sesgo de selección derivado de la exclusión de actas de congresos (Conference Proceedings) y preprints, dado que arquitecturas fundacionales de IDP (p. ej., LayoutLM, DocFormer, StrucTexT, BROS) se originaron en dichos foros; no obstante, el corpus primario (N = 131) captura sistemáticamente su adopción, optimización empírica e integración en flujos corporativos reportada en revistas consolidadas."),



    ("Sesgo de Publicación", "Predominancia de literatura que reporta solo resultados favorables.", "Inclusión sistemática de artículos con reportes de fallas y limitaciones en escaneos degradados, formatos no estandarizados y altos costos de cómputo."),



    ("Sesgo del Evaluador", "Subjetividad individual durante el cribado y control QA por autor único.", "Protocolo de fiabilidad intra-evaluador test-retest ciego (n = 27 por fase: κ = 0.81 en cribado, κ = 0.87 en elegibilidad, κ = 0.89 en PI1) y arbitraje con docente asesor; reconociendo como limitación metodológica la ausencia de doble cribado independiente paralelo."),



    ("Validez de Constructo", "Desalineación entre términos de búsqueda y conceptos reales.", "Derivación rigurosa desde la matriz PICOC e incorporación de sinónimos técnicos exhaustivos (KIE, VRD, LayoutLM, IDP).")



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



    "en estricto apego a las directrices de reporte de Kitchenham & Charters (2007) [1], los estándares internacionales de la declaración "



    "PRISMA 2020 [2] y las directrices metodológicas de la guía docente institucional. La totalidad de los hallazgos se reporta en tercera "



    "persona impersonal y con verbos de reporte neutros, articulando directamente la evidencia cuantitativa con la discusión analítica de cada eje temático."



)







add_p(



    "El corpus documental primario quedó formalmente cerrado y congelado en un total de N = 131 artículos de revista científica indexada "



    "(100 % Journal Articles, sin actas de congreso, preprints, tesis ni literatura gris), habiendo superado el control de calidad metodológica "



    "(superando el umbral formal de QA >= 3.0 / 5.0, con una media global de 4.61 / 5.0 y un rango observado entre 3.50 y 5.00 puntos). Este volumen supera con holgura el umbral de suficiencia documental exigido para tecnologías "



    "con ventana temporal menor a 10 años (n >= 35 estudios). La numeración de citas bibliográficas mantiene una relación matemática biunívoca unívoca: "



    "Ref IEEE [n] = ID S + 2, donde las citas [1] y [2] corresponden a las normas metodológicas marco (Kitchenham & Charters y PRISMA 2020), los 131 "



    "estudios primarios del corpus se indexan de manera inalterable entre [3] y [133] (desde [S001] hasta [S131]), y las referencias metodológicas "



    "complementarias de síntesis documental y cienciometría se ubican en [134] a [140]."



)







add_p(



    "Conforme a los ítems 13a–13f de PRISMA 2020 y para mitigar el sesgo de conveniencia (reporting bias), la selección de la estrategia analítica "



    "para cada interrogante se formalizó antes de la consolidación de los datos: 1) Síntesis Temática (Thomas & Harden [134]; Cruzes & Dybå [135]) "



    "para la taxonomía algorítmica de arquitecturas IA/IDP (PI1) y el mapeo de tipologías documentales y sistemas ERP/CRM (PI4); 2) Síntesis Narrativa "



    "Estructurada (Popay et al. [136]) para el análisis de rendimiento técnico (PI2), organizando las métricas cuantitativas (F1-score, exactitud, latencia) "



    "por benchmarks estándar (SROIE, FUNSD, CORD) y reportando rangos empíricos [mín, máx] sin promediar métricas entre datasets incompatibles; "



    "3) Síntesis sin metaanálisis — SWiM (Campbell et al. [137]) para contrastar las soluciones IA/IDP frente a líneas base tradicionales y manuales (PI3), "



    "utilizando el conteo de votos de dirección del efecto (Mejora, Sin diferencia, Empeora) y barras divergentes; 4) Mapeo Sistemático Matricial "



    "(Petersen et al. [138]) para caracterizar la evolución temporal (PD1) y el cruce bidimensional entre diseños metodológicos y tipologías de dataset (PD3) "



    "mediante gráficos de burbujas; 5) Mapeo Cienciométrico y Análisis de Redes (van Eck & Waltman [139]) en PD2 para identificar núcleos de producción científica "



    "(revistas, países, autores) y la estructura de coocurrencia de palabras clave de autor en VOSviewer con umbral de >= 3 apariciones; y 6) Calificación de "



    "Certeza de la Evidencia (Lewin et al. [140]) mediante el marco GRADE-CERQual sobre 4 pilares para ponderar cada hallazgo principal."



)







# ------------------------------------------------------------------------------



# 1.1 PD1: Evolución Temporal



# ------------------------------------------------------------------------------



add_heading_2("B. Evolución Temporal de la Producción Científica (PD1)")







add_p(



    "Para determinar el comportamiento cronológico de la literatura sobre IA/IDP aplicada al procesamiento de documentos de negocio entre 2020 y 2025/2026, "



    "se contabilizó la distribución de los 131 artículos primarios por año de publicación formal indexada, cuyos datos cuantitativos se detallan en la "



    "TABLA XIII y se visualizan gráficamente en la Fig. 2."



)







add_table_title("TABLA XIII", "DISTRIBUCIÓN CRONOLÓGICA DE LA PRODUCCIÓN CIENTÍFICA (2020–2025/2026) (N = 131)")



t_pd1 = doc.add_table(rows=8, cols=5)



hdr_pd1 = t_pd1.rows[0].cells



hdr_pd1[0].paragraphs[0].text = "Año de Publicación"



hdr_pd1[1].paragraphs[0].text = "Estudios Primarios Indexados [n]"



hdr_pd1[2].paragraphs[0].text = "Frecuencia Absoluta (n)"



hdr_pd1[3].paragraphs[0].text = "Frecuencia Relativa (%)"



hdr_pd1[4].paragraphs[0].text = "Porcentaje Acumulado (%)"







pd1_data = [



    ("2020", "[64], [111], [130], [131]", "4", "3.1 %", "3.1 %"),



    ("2021", "[58]–[63], [112]–[114], [123], [126]–[129]", "14", "10.7 %", "13.8 %"),



    ("2022", "[50]–[55], [57], [103]–[109], [125], [132], [133]", "17", "13.0 %", "26.8 %"),



    ("2023", "[39]–[49], [67], [90]–[92], [94]–[102], [121], [124]", "26", "19.8 %", "46.6 %"),



    ("2024", "[28]–[31], [33]–[38], [84], [86]–[89], [120]", "16", "12.2 %", "58.8 %"),



    ("2025", "[4]–[27], [32], [56], [68]–[83], [85], [93], [110], [115]–[119], [122]", "51", "38.9 %", "97.7 %"),



    ("2026*", "[3], [65], [66]", "3", "2.3 %", "100.0 %")



]



for idx, (yr, refs, fa, fr, pac) in enumerate(pd1_data, start=1):



    c = t_pd1.rows[idx].cells



    c[0].paragraphs[0].text = yr



    c[1].paragraphs[0].text = refs



    c[2].paragraphs[0].text = fa



    c[3].paragraphs[0].text = fr



    c[4].paragraphs[0].text = pac







style_table(t_pd1, [Inches(1.1), Inches(2.8), Inches(0.9), Inches(0.9), Inches(0.9)],



            align_cols=[WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER])



add_table_footer("* Nota: Los tres estudios fechados con volumen 2026 ([3], [65], [66]) fueron publicados oficialmente en línea en modalidad Early Access durante el segundo semestre de 2025 (ver justificación metodológica bajo el criterio IN1 en la Sección II.D). Fuente: elaboración propia a partir del corpus primario [3]–[133].")







add_figure_with_caption('project/resultados/outputs/fig2_evolucion_anual.png', 'Fig. 2',



                        'Evolución temporal de publicaciones sobre IA/IDP en documentos empresariales (2020–2025/2026, N = 131)',



                        'Barras: volumen anual absoluto (n); línea roja: porcentaje acumulado (%).')







add_p(



    "Ciento treinta y un estudios (100.0 % del corpus primario; [3]–[133]) respondieron a la evolución cronológica de la producción científica "



    "en IA e IDP aplicada a sistemas documentales corporativos (PD1). Mediante mapeo sistemático cronológico se identificó una trayectoria de crecimiento "



    "marcadamente expansiva y no lineal a lo largo del sexenio 2020–2025/2026, con una concentración máxima de publicaciones en el bienio final (TABLA XIII, Fig. 2).",



    bold_prefix="1) Apertura (Respuesta a PD1): "



)







# --- 2) Desarrollo por Categoría y Fases Temporales ---

add_p(

    "La dinámica temporal de publicación se articula en tres periodos analíticos diferenciados:",

    bold_prefix="2) Desarrollo por Categoría y Fases Temporales: "

)



add_p(

    "Reúne 18 estudios (13.7 % del corpus; [58]–[64], [111]–[114], [123], [126]–[131]), "

    "donde predominaron propuestas orientadas a mejorar la binarización de escaneos, OCR neuronal con LSTM y segmentación clásica con Mask R-CNN, registrando tasas "

    "de publicación moderadas (4 estudios en 2020 y 14 en 2021). El 88.9 % de los estudios de esta fase reportó calidad alta, aunque con certeza CERQual moderada.",

    bold_prefix="a) Fase de emergencia y cimientos basados en OCR-CNN (2020–2021): ",

    indent=Cm(0.5)

)



add_p(

    "Concentra 43 estudios (32.8 % del corpus; [39]–[55], [57], [67], [90]–[92], [94]–[109], "

    "[121], [124], [125], [132], [133]), representando el primer punto de inflexión significativo al pasar de 17 artículos en 2022 a 26 en 2023 (19.8 % anual), "

    "impulsada por la adopción de modelos multimodales preentrenados (LayoutLMv2/v3, StrucTexT, BROS) y redes de grafos (GCN) para extracción de entidades clave (KIE).",

    bold_prefix="b) Fase de consolidación de Transformers Multimodales (2022–2023): ",

    indent=Cm(0.5)

)



add_p(

    "Agrupa 54 estudios (41.2 % del corpus; [3]–[27], [32], [56], [65], [66], "

    "[68]–[83], [85], [93], [110], [115]–[119], [122]), constituyendo la etapa más prolífica con 51 publicaciones en 2025 (38.9 %) y 3 en Early Access para 2026 "

    "(2.3 %; [3], [65], [66]), gracias al despliegue masivo de Vision-Language Models y LLMs adaptados con prompt engineering.",

    bold_prefix="c) Fase de aceleración exponencial con VLMs y Modelos Generativos (2025–2026*): ",

    indent=Cm(0.5)

)







add_p(



    "A pesar de la tendencia global alcista, la literatura experimentó una desaceleración temporal transitoria durante 2024, con 16 estudios reportados (12.2 %; "



    "[28]–[31], [33]–[38], [84], [86]–[89], [120]), cifra inferior a los 26 estudios alcanzados en 2023. El análisis de los manuscritos revela que este valle temporal "



    "obedeció al agotamiento empírico de las arquitecturas de grafos tradicionales y pipelines híbridos heurísticos [28], [34], [86], los cuales exhibían techos "



    "de rendimiento frente a distorsiones complejas, provocando un viraje en los laboratorios de investigación hacia la reconfiguración y entrenamiento de modelos "



    "fundacionales multimodales y arquitecturas zero-shot que vieron la luz masivamente en 2025 [3], [6], [12], [22], [32].",



    bold_prefix="3) Contrastes y Debates Temporales: "



)







add_p(



    "La literatura sobre IA/IDP en sistemas corporativos evidencia una trayectoria de maduración irreversible, transitando desde la simple corrección óptica de caracteres "



    "hacia sistemas integrales de comprensión de documentos ricos visualmente (Visually-Rich Documents). No se identificaron estudios longitudinales que evalúen la "



    "degradación de los modelos a lo largo de más de dos años operativos en empresas. Al ejecutar el análisis de sensibilidad excluyendo los 10 estudios del estrato "



    "inferior de calidad (QA = 3.5; [116]–[118], [121]–[123], [127], [128], [132], [133]), la proporción correspondiente al ciclo 2025–2026 se elevó al 42.1 % "



    "(51 de 121 estudios), ratificando la robustez de la tendencia expansiva.",



    bold_prefix="4) Cierre, Tendencias y Sensibilidad: "



)







# ------------------------------------------------------------------------------



# 1.2 PD2: Revistas, Autores, Países



# ------------------------------------------------------------------------------



add_heading_2("C. Productividad por Revistas, Autores, Países y Red de Coocurrencia (PD2)")







add_p(



    "Para responder a PD2, se normalizaron los títulos de las revistas indexadas, se contabilizó la productividad de los autores, se aplicó la regla estricta de "



    "afiliación geográfica institucional del autor principal (primer autor) y se estructuró la red de coocurrencia de palabras clave de autor (Author Keywords) "



    "con un umbral de frecuencia >= 3 en VOSviewer [139]. La evidencia bibliométrica se compendia en la TABLA XIV, la TABLA XV y la Fig. 3."



)







add_table_title("TABLA XIV", "REVISTAS CIENTÍFICAS LÍDERES EN PROCESAMIENTO INTELIGENTE DE DOCUMENTOS EMPRESARIALES (N = 131)")



t_pd2_rev = doc.add_table(rows=14, cols=5)



hdr_rev = t_pd2_rev.rows[0].cells



hdr_rev[0].paragraphs[0].text = "Revista Científica Indexada"



hdr_rev[1].paragraphs[0].text = "Editorial"



hdr_rev[2].paragraphs[0].text = "Cuartil"



hdr_rev[3].paragraphs[0].text = "Artículos en Corpus [n]"



hdr_rev[4].paragraphs[0].text = "Frecuencia Relativa (%)"







rev_data = [



    ("IEEE Access", "IEEE", "Q1 / Q2", "[5], [8], [16], [26], [59]–[61], [84], [88], [94], [103], [108], [131]", "13 (9.9 %)"),



    ("International Journal on Document Analysis and Recognition (IJDAR)", "Springer", "Q2", "[9], [33], [35], [39], [50], [65], [66], [77], [115]", "9 (6.9 %)"),



    ("Pattern Recognition", "Elsevier", "Q1", "[3], [41], [80], [92], [105], [120]", "6 (4.6 %)"),



    ("Multimedia Tools and Applications", "Springer", "Q2", "[15], [21], [52], [55], [57]", "5 (3.8 %)"),



    ("Expert Systems with Applications", "Elsevier", "Q1", "[11], [36], [67], [83]", "4 (3.1 %)"),



    ("Engineering Applications of Artificial Intelligence", "Elsevier", "Q1", "[24], [101], [114], [119]", "4 (3.1 %)"),



    ("Applied Sciences", "MDPI", "Q2", "[79], [85], [97], [123]", "4 (3.1 %)"),



    ("Electronics", "MDPI", "Q2", "[4], [7], [42]", "3 (2.3 %)"),



    ("International Journal of Pattern Recognition and Artificial Intelligence", "World Scientific", "Q3", "[47], [89], [121]", "3 (2.3 %)"),



    ("Neurocomputing", "Elsevier", "Q1", "[23], [38], [51]", "3 (2.3 %)"),



    ("Computers, Materials and Continua", "Tech Science Press", "Q2", "[22], [62], [109]", "3 (2.3 %)"),



    ("Proceedings of the VLDB Endowment (PVLDB)", "VLDB Endowment", "Q1", "[58], [112], [130]", "3 (2.3 %)"),



    ("Otras 62 revistas indexadas (<= 2 estudios c/u)", "Diversas", "Q1–Q3", "Citas dispersas [10], [12], [13], [17]–[20], etc.", "71 (54.2 %)")



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







add_table_title("TABLA XV", "CONCENTRACIÓN GEOGRÁFICA POR AFILIACIÓN DEL PRIMER AUTOR Y AUTORES DESTACADOS (N = 131)")



t_pd2_geo = doc.add_table(rows=12, cols=4)



hdr_geo = t_pd2_geo.rows[0].cells



hdr_geo[0].paragraphs[0].text = "País de Afiliación (Primer Autor)"



hdr_geo[1].paragraphs[0].text = "Estudios [n]"



hdr_geo[2].paragraphs[0].text = "% Relativo"



hdr_geo[3].paragraphs[0].text = "Autores Más Prolíficos en el Corpus (>= 3 publicaciones)"







geo_data = [



    ("China", "39", "29.8 %", "Zhang J. (4; [43], [81], [82], [120]), Zhang Y. (4; [78], [79], [81], [82]), Li C. (3; [9], [15], [32]), Liu J. (3; [19], [34], [74]), Zhang W. (3; [26], [37], [73]), Ma J. (3; [37], [43], [120]), Zhang Z. (3; [43], [83], [120])."),



    ("India", "11", "8.4 %", "Tiwari D. (2; [10], [31]), Gupta A. (2; [10], [31]), Baviskar D. (2; [60], [129]), Ahirrao S. (2; [60], [129]), Kotecha K. (2; [60], [129])."),



    ("Estados Unidos", "10", "7.6 %", "Wang P. (3; [47], [89], [121]), Lai P. (2; [89], [121]), Kim S. (2; [89], [121]), Burdick D. (1; [130])."),



    ("Alemania", "9", "6.9 %", "Hashmi K.A. (3; [59], [61], [123]), Liwicki M. (3; [59], [61], [123]), Stricker D. (3; [59], [61], [123]), Afzal M.Z. (2; [59], [61])."),



    ("Corea del Sur", "6", "4.6 %", "Lee S. (3; [42], [71], [121]), Lee E. (2; [52], [71]), Cho N.I. (2; [52], [71])."),



    ("Canadá", "5", "3.8 %", "Simsek M. (4; [11], [35], [48], [51]), Kantarci B. (4; [11], [35], [48], [51]), Xiao B. (3; [11], [35], [48]), Alkheir A.A. (3; [11], [35], [48])."),



    ("Vietnam", "5", "3.8 %", "Tran A.C. (2; [75], [107]), Nguyen H.T. (2; [75], [107]), Nguyen M.-T. (2; [67], [114])."),



    ("Taiwán", "4", "3.1 %", "Chen L.-C. (1; [4]), Lin H.-Y. (1; [98]), Lee W.-T. (1; [106]), Huang C.-C. (1; [106])."),



    ("Turquía", "4", "3.1 %", "Oral B. (2; [50], [64]), Eryiğit G. (2; [50], [64]), Sayallar C. (1; [100]), Arslan H. (1; [103])."),



    ("España", "3", "2.3 %", "Fornés A. (2; [105], [111]), Lladós J. (2; [105], [116]), Sainz-De-Abajo B. (1; [131])."),



    ("Otros 22 países (<= 2 estudios c/u)", "38", "29.0 %", "Investigadores con filiaciones en Australia, Reino Unido, Singapur, Francia, Italia, etc.")



]



for idx, (pais, est, pct, aut) in enumerate(geo_data, start=1):



    c = t_pd2_geo.rows[idx].cells



    c[0].paragraphs[0].text = pais



    c[1].paragraphs[0].text = est



    c[2].paragraphs[0].text = pct



    c[3].paragraphs[0].text = aut







style_table(t_pd2_geo, [Inches(0.85), Inches(0.35), Inches(0.4), Inches(1.8)],



            font_size=Pt(6.5), align_cols=[WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT])



add_table_footer("Fuente: elaboración propia a partir del corpus primario [3]–[133]. Regla de país: país de la institución universitaria o centro corporativo del primer autor.")







add_figure_with_caption('project/resultados/outputs/fig3_vosviewer_geografia.png', 'Fig. 3',



                        'Concentración geográfica de la investigación y principales clústeres temáticos derivados de palabras clave de autor (PD2, N = 131)',



                        '(a) Distribución porcentual por país de afiliación del autor principal; (b) Frecuencia de descriptores con umbral ≥ 3 ocurrencias en VOSviewer.')







add_p(



    "Ciento treinta y un artículos primarios (100.0 % del corpus; [3]–[133]) respondieron a la distribución de productividad académica por revistas, "



    "autores, países y estructura temática de redes (PD2). Mediante análisis cienciométrico y mapeo de coocurrencia en VOSviewer [139] se identificó una "



    "concentración de publicaciones en revistas especializadas de procesamiento de documentos e ingeniería de sistemas, liderada a nivel geográfico por "



    "instituciones de China, India y Estados Unidos, con una marcada desconcentración autoral (TABLA XIV, TABLA XV, Fig. 3).",



    bold_prefix="1) Apertura (Respuesta a PD2): "



)







add_p(



    "La evidencia se estructura en tres dimensiones bibliométricas:\n"



    "a) Núcleos de difusión y revistas líderes: Doce revistas concentraron el 45.8 % de la producción global (60 de 131 artículos; TABLA XIV). El canal predominante "



    "fue IEEE Access con 13 artículos (9.9 %; [5], [8], [16], [26], [59]–[61], [84], [88], [94], [103], [108], [131]), seguido de International Journal on Document "



    "Analysis and Recognition (IJDAR) de Springer con 9 artículos (6.9 %; [9], [33], [35], [39], [50], [65], [66], [77], [115]) y Pattern Recognition de Elsevier "



    "con 6 artículos (4.6 %; [3], [41], [80], [92], [105], [120]).\n"



    "b) Polos geográficos de investigación: Conforme a la regla de asignación por primer autor, China lideró con 39 estudios (29.8 %; TABLA XV, Fig. 3a), seguida de India "



    "con 11 estudios (8.4 %) y Estados Unidos con 10 estudios (7.6 %). Europa occidental sumó presencia relevante con Alemania (9 estudios, 6.9 %) y España (3 estudios, 2.3 %).\n"



    "c) Red cienciométrica de palabras clave (VOSviewer): Con umbral >= 3 apariciones se configuraron tres clústeres conceptuales (Fig. 3b): Clúster 1 (Extracción y Semántica: "



    "Information Extraction con 26 ocurrencias, Document Understanding con 6 y KIE con 4); Clúster 2 (Paradigmas Algorítmicos: Deep Learning con 21 ocurrencias, OCR con 24 "



    "y Transformers con 5); y Clúster 3 (Estructuras Complejas: Table Structure Recognition con 11 ocurrencias, Table Detection con 11 y Object Detection con 8).",



    bold_prefix="2) Desarrollo por Categoría y Redes Temáticas: "



)







add_p(



    "A diferencia de la marcada concentración institucional observada en China y en revistas como IEEE Access e IJDAR, el análisis de autoría evidenció una alta "



    "dispersión autoral. De los 498 investigadores vinculados al corpus, 422 autores (84.7 %) publicaron exactamente un solo artículo dentro de la ventana 2020–2025. "



    "Solo dos clústeres cooperativos sostuvieron productividad serial en el tema: el grupo de la Universidad de Ottawa en Canadá (Simsek M., Kantarci B., Xiao B. y "



    "Alkheir A.A. con 4 publicaciones conjuntas sobre tablas y hojas de datos; [11], [35], [48], [51]) y el grupo del DFKI / Universidad de Kaiserslautern en Alemania "



    "(Hashmi K.A., Liwicki M., Stricker D. y Afzal M.Z. con 3 estudios de detección tabular; [59], [61], [123]). Esto demuestra que la automatización de documentos empresariales es "



    "abordada principalmente por iniciativas de investigación aplicadas y distribuidas, y no por un laboratorio hegemónico.",



    bold_prefix="3) Contrastes y Dispersión Autoral: "



)







add_p(



    "Se constata una brecha geográfica crítica: no se identificaron artículos del corpus con autor principal afiliado a instituciones de América Latina dedicados a "



    "documentos tributarios o empresariales corporativos propios de la región (únicamente contribuciones españolas en detección tabular y recibos; [105], [111], [131]). El análisis "



    "de sensibilidad (excluyendo estudios con QA = 3.5) no modificó las 5 revistas líderes ni la posición hegemónica de China (31.4 % de los estudios filtrados; 38 de 121), "



    "confirmando la estabilidad del mapa cienciométrico.",



    bold_prefix="4) Cierre, Tendencias y Sensibilidad: "



)







# ------------------------------------------------------------------------------



# 1.3 PD3: Diseños Metodológicos x Datasets



# ------------------------------------------------------------------------------



add_heading_2("D. Clasificación de Diseños Metodológicos × Tipología de Datasets (PD3)")







add_p(



    "Para evaluar la solidez empírica y la transferibilidad industrial de las soluciones reportadas en el corpus, se clasificaron los 131 estudios primarios cruzando la "



    "taxonomía estandarizada de diseños de investigación frente a las fuentes de datos utilizadas (benchmarks públicos, privados corporativos o mixtos). La fiabilidad "



    "de reproducibilidad (test-retest a ciegas) de esta categorización se evaluó sobre una muestra del 20.6 % del corpus (n = 27 estudios seleccionados aleatoriamente), "



    "alcanzando un coeficiente Kappa de Cohen κ = 0.85 (acuerdo observado del 88.9 % frente a un azar esperado de 0.258; concordancia casi perfecta). La matriz de contingencia "



    "se reporta en la TABLA XVI y el gráfico de burbujas de Petersen et al. (2015) [138] se expone en la Fig. 4."



)







add_table_title("TABLA XVI", "MATRIZ CRUZADA DE DISEÑOS METODOLÓGICOS Y TIPOLOGÍA DE DATASETS (PD3) (N = 131)")



t_pd3 = doc.add_table(rows=6, cols=6)



hdr_pd3 = t_pd3.rows[0].cells



hdr_pd3[0].paragraphs[0].text = "Diseño Metodológico de Investigación"



hdr_pd3[1].paragraphs[0].text = "Benchmarks Públicos Abiertos"



hdr_pd3[2].paragraphs[0].text = "Datasets Corporativos Privados"



hdr_pd3[3].paragraphs[0].text = "Datasets Híbridos / Mixtos"



hdr_pd3[4].paragraphs[0].text = "Total por Diseño [n]"



hdr_pd3[5].paragraphs[0].text = "% Relativo"







pd3_data = [



    ("Experimental Controlado", "48 (36.6 %)\n[3]–[6], [8], [9], [12], [14], [15], [17], [19], [30]–[33], [35], [37], [39]–[42], [46]–[48], [50], [52], [57], [61], [67], [71]–[74], [76], [77], [80], [83], [86], [88]–[90], [92], [93], [96], [99], [104], [105], [108]",



     "18 (13.7 %)\n[7], [10], [11], [13], [20], [22], [28], [34], [36], [43]–[45], [49], [51], [55], [56], [81], [91]",



     "16 (12.2 %)\n[16], [18], [21], [23]–[27], [29], [38], [60], [65], [66], [68], [78], [87]",



     "82", "62.6 %"),



    ("Desarrollo de Artefacto / PoC", "14 (10.7 %)\n[63], [69], [79], [97], [100], [102], [106], [109]–[111], [113]–[116]",



     "11 (8.4 %)\n[54], [95], [98], [112], [118]–[124]",



     "6 (4.6 %)\n[58], [59], [125], [126], [129], [130]",



     "31", "23.7 %"),



    ("Cuasi-experimental", "4 (3.1 %)\n[85], [94], [101], [132]",



     "4 (3.1 %)\n[53], [82], [107], [133]",



     "2 (1.5 %)\n[62], [128]",



     "10", "7.6 %"),



    ("Caso de Estudio Real Corporativo", "2 (1.5 %)\n[84], [103]",



     "5 (3.8 %)\n[64], [70], [75], [117], [127]",



     "1 (0.8 %)\n[131]",



     "8", "6.1 %"),



    ("Total por Tipología de Dataset", "68 (51.9 %)", "38 (29.0 %)", "25 (19.1 %)", "131", "100.0 %")



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



add_table_footer("Fuente: elaboración propia a partir del corpus primario [3]–[133]. Medición de fiabilidad test-retest sobre muestra del 20.6 % (n = 27): Po = 88.9 %, Pe = 0.258, κ = 0.85 (casi perfecto). Partición matemática exacta de 12 celdas disjuntas.")







add_figure_with_caption('project/resultados/outputs/fig4_burbujas_disenos_datasets.png', 'Fig. 4',



                        'Gráfico de burbujas del mapeo sistemático (Petersen et al. [138]): Diseño Metodológico vs. Tipología de Dataset (PD3, N = 131)',



                        'El área de cada burbuja es proporcional al número de estudios primarios (n); porcentajes sobre la totalidad del corpus.')







add_p(



    "Ciento treinta y un artículos (100.0 % del corpus; [3]–[133]) respondieron a la relación entre los diseños metodológicos de investigación y "



    "las tipologías de conjuntos de datos evaluados (PD3). Mediante la matriz de mapeo sistemático de Petersen et al. [138] y con un acuerdo de fiabilidad test-retest "



    "de κ = 0.85, se determinó un predominio estructural de experimentos controlados sobre bancos de datos públicos abiertos, en contraste con una baja proporción "



    "de casos de estudio reales integrados en producción corporativa (TABLA XVI, Fig. 4).",



    bold_prefix="1) Apertura (Respuesta a PD3): "



)







add_p(



    "La matriz cruzada evidencia tres núcleos de trabajo:\n"



    "a) Predominio del diseño experimental controlado: Ochenta y dos estudios (62.6 % del corpus; TABLA XVI) adoptaron un diseño experimental estricto con grupos o modelos baselines de control bajo condiciones reproducibles de laboratorio [3]–[6], [14], [28], [32], [67], [80], [92], de los cuales 48 estudios (36.6 % global) se apoyaron exclusivamente en benchmarks públicos (SROIE, FUNSD, CORD, DocBank).\n"



    "b) Desarrollo de artefactos y pruebas de concepto (PoC): Treinta y un estudios (23.7 %; [79], [95], [97], [100], [102], [112], [117]–[124]) se centraron en construir prototipos o arquitecturas especializadas validadas de forma acotada, donde 11 estudios (8.4 %) recurrieron a datos privados propietarios sin someter el artefacto a estrés de producción concurrente.\n"



    "c) Validación en conjuntos de datos corporativos y mixtos: Treinta y ocho estudios (29.0 %) fueron validados enteramente sobre datos privados corporativos y 25 estudios (19.1 %) aplicaron esquemas mixtos con ajuste fino y validación final sobre facturas y órdenes de compra de organizaciones ([16], [25], [38], [65], [66], [68]).",



    bold_prefix="2) Desarrollo por Categoría y Cruce Matricial: "



)







add_p(



    "El contraste más crítico revelado por el mapeo sistemático reside en la extrema escasez de casos de estudio reales en producción corporativa, los cuales representan "



    "únicamente el 6.1 % del corpus (8 de 131 estudios; [64], [70], [75], [84], [103], [117], [127], [131]). A pesar de que la literatura reporta precisiones teóricas "



    "superiores al 95 % en benchmarks abiertos [3], [6], [7], [67], [80], los autores que implementaron soluciones dentro de entornos empresariales operativos enfrentaron "



    "barreras que no aparecen en las pruebas experimentales: restricciones de confidencialidad de datos bajo regulaciones de protección financiera [64], [116], necesidad de "



    "intervención humana en el bucle (Human-in-the-Loop) para mitigar alucinaciones de LLMs en montos contables [4], [13], [22] y complejas interfaces de integración "



    "con sistemas legados ERP [70], [127].",



    bold_prefix="3) Contrastes y Vacíos en Casos de Estudio Reales: "



)







add_p(



    "Existe una brecha de transferencia tecnológica: la comunidad científica ha priorizado el benchmarking sobre tres datasets públicos icónicos frente a la validación "



    "empírica en flujos empresariales vivos. Al excluir los 10 estudios del estrato inferior de calidad (QA = 3.5; [116]–[118], [121]–[123], [127], [128], [132], [133]), "



    "los experimentos controlados se consolidaron en el 65.3 % (79 de 121 estudios), ratificando que la evidencia técnica del área descansa sobre pruebas comparativas "



    "de laboratorio metodológicamente rigurosas.",



    bold_prefix="4) Cierre, Madurez y Sensibilidad: "



)







# ------------------------------------------------------------------------------



# 2. QA - Paso 6



# ------------------------------------------------------------------------------



add_heading_2("E. Evaluación de Calidad Metodológica (QA) e Integración al Análisis (Paso 6)")



add_p(



    "Para jerarquizar el grado de solidez empírica de la evidencia y preparar formalmente el insumo para el Análisis de Sensibilidad (Paso 8), se examinó la totalidad "



    "del corpus primario bajo el instrumento de cinco preguntas de calidad metodológica (QA1 a QA5) de Kitchenham & Charters (2007) [1]. La evaluación de fiabilidad "



    "test-retest ciego sobre la muestra del 20.6 % (n = 27 estudios) reportó un coeficiente Kappa ponderado cuadrático de Cohen κw = 0.89 (acuerdo casi perfecto para escalas "



    "ordinales). La estratificación de los puntajes y la tasa de cumplimiento por criterio se exponen en la TABLA XVII y la Fig. 5."



)







add_table_title("TABLA XVII", "ESTRATIFICACIÓN DE CALIDAD METODOLÓGICA (QA) Y ANÁLISIS DE CUMPLIMIENTO POR CRITERIO (N = 131)")



t_qa_strat = doc.add_table(rows=5, cols=5)



hdr_qas = t_qa_strat.rows[0].cells



hdr_qas[0].paragraphs[0].text = "Nivel de Calidad Metodológica"



hdr_qas[1].paragraphs[0].text = "Rango de Puntaje (Máx. 5.0)"



hdr_qas[2].paragraphs[0].text = "Estudios en Corpus [n]"



hdr_qas[3].paragraphs[0].text = "Frecuencia Relativa (%)"



hdr_qas[4].paragraphs[0].text = "Función Metodológica en la Síntesis"







qas_data = [



    ("Calidad Alta", "4.5 – 5.0 pts", "108", "82.4 %", "Núcleo empírico robusto para extracción y síntesis temática (PI1–PI4). Incluye los 4 estudios nucleares de referencia con puntaje perfecto de 5.0 / 5.0 ([3], [4], [5], [6])."),



    ("Calidad Media", "4.0 pts", "13", "9.9 %", "Estudios que satisfacen el protocolo con cumplimientos parciales menores; retenidos en el análisis de sensibilidad."),



    ("Calidad Moderada / Estrato Inferior*", "3.5 pts", "10", "7.6 %", "Grupo de exclusión temporal en el Análisis de Sensibilidad (Paso 8): [116], [117], [118], [121], [122], [123], [127], [128], [132], [133]."),



    ("Total Corpus Primario", "Media = 4.61 / 5.00", "131", "100.0 %", "Mínimo registrado: 3.50 pts; Máximo: 5.00 pts; Desviación estándar: ±0.41 pts.")



]



for idx, (niv, rng, n_e, pct, func) in enumerate(qas_data, start=1):



    c = t_qa_strat.rows[idx].cells



    c[0].paragraphs[0].text = niv



    c[1].paragraphs[0].text = rng



    c[2].paragraphs[0].text = n_e



    c[3].paragraphs[0].text = pct



    c[4].paragraphs[0].text = func







style_table(t_qa_strat, [Inches(0.65), Inches(0.55), Inches(0.35), Inches(0.4), Inches(1.45)],



            font_size=Pt(6.5), align_cols=[WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT])



add_table_footer("* Nota: El estrato de 3.5 pts conforma la submuestra de prueba para el análisis de robustez de hallazgos. Ningún estudio incluido obtuvo calificación menor a 3.5 pts. Fuente: elaboración propia a partir del corpus primario [3]–[133].")







add_table_title("TABLA XVII (CONTINUACIÓN)", "ANÁLISIS DESAGREGADO DE CUMPLIMIENTO POR PREGUNTA QA (N = 131)")



t_qa_crit = doc.add_table(rows=6, cols=5)



hdr_crit = t_qa_crit.rows[0].cells



hdr_crit[0].paragraphs[0].text = "Criterio QA Evaluado"



hdr_crit[1].paragraphs[0].text = "Cumplimiento Total (1.0 pt)"



hdr_crit[2].paragraphs[0].text = "Cumplimiento Parcial (0.5 pt)"



hdr_crit[3].paragraphs[0].text = "Incumplimiento (0.0 pt)"



hdr_crit[4].paragraphs[0].text = "Media por Criterio (sobre 1.0)"







crit_data = [



    ("QA1 (Objetivos y tipología documental definida)", "131 (100.0 %)", "0 (0.0 %)", "0 (0.0 %)", "1.000 / 1.0"),



    ("QA2 (Detalle del dataset, volumen y particiones)", "125 (95.4 %)", "6 (4.6 %)", "0 (0.0 %)", "0.977 / 1.0"),



    ("QA3 (Arquitectura reproducible y código documentado)", "99 (75.6 %)", "32 (24.4 %)", "0 (0.0 %)", "0.878 / 1.0"),



    ("QA4 (Métricas cuantitativas formales reproducibles)", "108 (82.4 %)", "23 (17.6 %)", "0 (0.0 %)", "0.912 / 1.0"),



    ("QA5 (Contraste empírico vs baselines / tradicional)", "89 (67.9 %)", "42 (32.1 %)", "0 (0.0 %)", "0.840 / 1.0")



]



for idx, (crit, tot, par, inc, med) in enumerate(crit_data, start=1):



    c = t_qa_crit.rows[idx].cells



    c[0].paragraphs[0].text = crit



    c[1].paragraphs[0].text = tot



    c[2].paragraphs[0].text = par



    c[3].paragraphs[0].text = inc



    c[4].paragraphs[0].text = med







style_table(t_qa_crit, [Inches(1.2), Inches(0.55), Inches(0.55), Inches(0.55), Inches(0.55)],



            font_size=Pt(6.5), align_cols=[WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER])



add_table_footer("Fuente: elaboración propia a partir del corpus primario [3]–[133].")







add_figure_with_caption('project/resultados/outputs/fig5_distribucion_qa_criterios.png', 'Fig. 5',



                        'Evaluación de Calidad Metodológica (Kitchenham & Charters [1]) y vulnerabilidad por criterio (N = 131)',



                        '(a) Estratificación de estudios según calidad; (b) Desglose de cumplimiento total vs. parcial en QA1–QA5.')







add_p(



    "La calidad metodológica global del corpus es sobresaliente (media = 4.61 / 5.00 pts; 82.4 % en calidad alta). Los criterios QA1 (1.000) y QA2 (0.977) "



    "exhibieron cumplimiento prácticamente óptimo en la totalidad de artículos. Por el contrario, la mayor debilidad empírica residió en el criterio QA5 "



    "(contraste empírico explícito frente a líneas base tradicionales), con 42 estudios que obtuvieron puntaje parcial (32.1 %; media 0.840), seguido de QA3 "



    "(especificación de hiperparámetros y reproducibilidad) con 32 cumplimientos parciales (24.4 %; media 0.878). Los 10 estudios calificados con QA = 3.50 puntos "



    "([116], [117], [118], [121], [122], [123], [127], [128], [132], [133]) conforman el grupo aislado para el test de robustez.",



    bold_prefix="Hallazgos del Control de Calidad y Protocolo de Aislamiento: "



)







# ------------------------------------------------------------------------------



# 3. PI1: Taxonomía de Familias Algorítmicas de IA



# ------------------------------------------------------------------------------



add_heading_2("F. Taxonomía de Familias Algorítmicas y Enfoques de IA (PI1)")



add_p(



    "Para determinar cuáles son las familias algorítmicas y arquitecturas neuronales predominantes en la literatura entre 2020 y 2025/2026, se ejecutó una síntesis "



    "temática (Thomas & Harden [134]; Cruzes & Dybå [135]) sobre los 105 estudios primarios que abordan explícitamente el modelado de IA para procesamiento de documentos "



    "de negocio (80.2 % del corpus). La asignación taxonómica bajo protocolo de fiabilidad test-retest ciego sobre la muestra aleatoria del 20.6 % (n = 27 estudios) "



    "reportó un coeficiente Kappa de Cohen κ = 0.88 (Po = 92.6 %, Pe = 0.380), evidenciando una consistencia metodológica casi perfecta bajo las directrices del Checklist 9.2.F. "



    "Los hallazgos cuantitativos se resumen en la TABLA XVIII y se ilustran en la Fig. 6."



)







add_table_title("TABLA XVIII", "TAXONOMÍA DE FAMILIAS ALGORÍTMICAS Y ENFOQUES DE INTELIGENCIA ARTIFICIAL (PI1) (n = 105)")



t_pi1 = doc.add_table(rows=6, cols=5)



hdr_pi1 = t_pi1.rows[0].cells



hdr_pi1[0].paragraphs[0].text = "Familia Algorítmica / Enfoque IA"



hdr_pi1[1].paragraphs[0].text = "Descripción Técnica Estandarizada"



hdr_pi1[2].paragraphs[0].text = "Estudios Primarios Asignados [n]"



hdr_pi1[3].paragraphs[0].text = "Estudios (n)"



hdr_pi1[4].paragraphs[0].text = "% Relativo"







pi1_table_data = [



    ("Pipelines Híbridos CNN-RNN y Segmentación Clásica con OCR",



     "Modelos convolucionales (ResNet, VGG, YOLO, Mask R-CNN) combinados con recurrentes (LSTM) y motores OCR para detección de regiones y tablas.",



     "[5], [10]–[12], [14]–[16], [20], [23], [28], [31]–[33], [35], [39], [45], [48], [49], [53]–[55], [57]–[62], [67]–[73], [78], [83]–[85], [88], [91], [93], [95], [98]–[100], [103], [104], [106], [108]–[111], [117], [118], [122], [124]",



     "56", "53.3 %"),



    ("Transformers Multimodales y Modelos Visión-Lenguaje (VLM)",



     "Modelado conjunto de texto, coordenadas espaciales 2D (bounding boxes) y parches visuales (LayoutLMv2/v3, StrucTexT, BROS, Bi-VLDoc).",



     "[6], [7], [9], [13], [18], [21], [26], [30], [36], [38], [42], [43], [47], [50], [56], [74], [76], [77], [90], [92], [96], [114]",



     "22", "21.0 %"),



    ("Redes Neuronales de Grafos y Modelado Espacial-Relacional (GNN)",



     "Representación de palabras/bloques como nodos y relaciones espaciales/semánticas relativas como aristas (GCN, GAT, GraphIE).",



     "[8], [29], [34], [40], [41], [44], [46], [51], [52], [63], [64], [66], [75], [105], [107], [123]",



     "16", "15.2 %"),



    ("Modelos Generativos, LLMs y Adaptación Zero/Few-Shot",



     "Modelos fundacionales autorregresivos aplicados con prompt engineering, in-context learning o fine-tuning para extracción estructurada JSON.",



     "[3], [4], [17], [19], [22], [24], [25], [27], [37], [65], [82]",



     "11", "10.5 %"),



    ("Total Cobertura PI1", "Subconjunto verificado de estudios con PI1 = 1", "[3]–[124] (105 estudios únicos)", "105", "100.0 %")



]



for idx, (fam, desc, refs, fa, fr) in enumerate(pi1_table_data, start=1):



    c = t_pi1.rows[idx].cells



    c[0].paragraphs[0].text = fam



    c[1].paragraphs[0].text = desc



    c[2].paragraphs[0].text = refs



    c[3].paragraphs[0].text = fa



    c[4].paragraphs[0].text = fr







style_table(t_pi1, [Inches(0.85), Inches(0.95), Inches(0.9), Inches(0.35), Inches(0.35)],



            font_size=Pt(6.5), align_cols=[WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER])



add_table_footer("Fuente: elaboración propia a partir del corpus primario [3]–[133]. Partición temática unívoca auditada y verificada.")







add_figure_with_caption('project/resultados/outputs/fig6_taxonomia_algoritmos.png', 'Fig. 6',



                        'Taxonomía de Familias Algorítmicas de IA en Procesamiento Documental (PI1, n = 105)',



                        'Frecuencia absoluta y porcentaje relativo derivado de síntesis temática [134], [135].')







add_p(



    "Ciento cinco estudios primarios (80.2 % del corpus; TABLA XVIII, Fig. 6) respondieron a la identificación y taxonomía de las arquitecturas de IA "



    "aplicadas al procesamiento de documentos corporativos (PI1). Mediante síntesis temática estandarizada (Thomas & Harden [134]; Cruzes & Dybå [135]) "



    "y con un coeficiente de fiabilidad test-retest de κ = 0.88 sobre la submuestra del 20.6 % (n = 27), se identificaron cuatro familias algorítmicas "



    "mutuamente excluyentes, observándose un predominio de pipelines modulares basados en convolución y OCR neuronal, acompañados por una rápida consolidación "



    "de Transformers multimodales y modelos de visión-lenguaje (VLM).",



    bold_prefix="1) Apertura (Respuesta a PI1): "



)







add_p(



    "Esta arquitectura comprende la articulación secuencial de redes neuronales convolucionales (ResNet, VGG, YOLO, Mask R-CNN) para la detección de regiones y tablas, "



    "combinadas con capas recurrentes (LSTM) y motores de reconocimiento óptico de caracteres para la extracción de texto en documentos estructurados. "



    "La familia agrupa a cincuenta y seis estudios primarios (53.3 % del subconjunto de PI1; [5], [10]–[12], [14]–[16], [20], [23], [28], [31]–[33], [35], [39], [45], "



    "[48], [49], [53]–[55], [57]–[62], [67]–[73], [78], [83]–[85], [88], [91], [93], [95], [98]–[100], [103], [104], [106], [108]–[111], [117], [118], [122], [124]). "



    "Las investigaciones convergen en que la modularización por etapas permite desacoplar la detección geométrica de tablas de la transcripción textual, facilitando la depuración "



    "y auditoría interna en entornos productivos locales [10], [15], [33], [54], [67], [84], [104]. Cuantitativamente, estos pipelines alcanzan latencias de inferencia "



    "de 80 ms a 250 ms en CPUs estándar con exactitudes de segmentación entre el 88.5 % y el 96.0 % en documentos de plantilla predecible. El 85.7 % de los estudios "



    "(48 de 56) ostenta calidad metodológica alta (QA >= 4.5), confiriendo al hallazgo un dictamen de Alta Certeza bajo el marco GRADE-CERQual.",



    bold_prefix="2.1. Pipelines Híbridos CNN-RNN y Segmentación Clásica con OCR: "



)







add_p(



    "Esta familia integra arquitecturas de atención profunda autorregresiva y bidireccional que fusionan simultáneamente la información textual, la disposición "



    "geométrica espacial 2D (bounding boxes) y los parches visuales del documento dentro de un espacio latente unificado (LayoutLMv2/v3, StrucTexT, BROS, Bi-VLDoc). "



    "Reúne veintidós estudios primarios (21.0 % de PI1; [6], [7], [9], [13], [18], [21], [26], [30], [36], [38], [42], [43], [47], [50], [56], [74], [76], [77], [90], "



    "[92], [96], [114]). Los autores demuestran consistentemente que la incorporación del contexto visual y espacial permite resolver la extracción de entidades clave (KIE) "



    "en comprobantes fiscales con diagramación variable sin requerir plantillas fijas [6], [13], [36], [42], [76], [92]. En términos cuantitativos, reportan puntuaciones "



    "de F1-score entre el 92.4 % y el 98.7 % en datasets estándar como SROIE y CORD. El 100.0 % de las publicaciones (22 de 22) se ubica en el estrato de calidad metodológica "



    "alta (QA >= 4.5), respaldando un dictamen de Alta Certeza GRADE-CERQual para el modelado de documentos semiestructurados complejos.",



    bold_prefix="2.2. Transformers Multimodales y Modelos Visión-Lenguaje (VLM): "



)







add_p(



    "Este paradigma representa los fragmentos y palabras del documento como nodos dentro de un grafo planar no dirigido o dirigido, cuyas aristas codifican relaciones "



    "de adyacencia espacial, distancias euclidianas y dependencias semánticas relativas (GCN, GAT, GraphIE). Comprende dieciséis estudios primarios (15.2 % de PI1; [8], [29], "



    "[34], [40], [41], [44], [46], [51], [52], [63], [64], [66], [75], [105], [107], [123]). La literatura coincide en que las redes de grafos capturan de forma sobresaliente "



    "el flujo de lectura no lineal y la estructura reticular de facturas abiertas y recibos deformados [8], [34], [40], [51], [64], [105]. En las evaluaciones numéricas exhiben "



    "precisiones de emparejamiento clave-valor de 88.0 % a 95.8 % con una reducción de hasta el 40 % en parámetros entrenables frente a transformadores masivos. El 93.8 % de "



    "los estudios (15 de 16) pertenece al rango de calidad metodológica alta (QA >= 4.5), alcanzando una calificación de Alta Certeza GRADE-CERQual en la estructuración de tablas "



    "financieras complejas.",



    bold_prefix="2.3. Redes Neuronales de Grafos y Modelado Espacial-Relacional (GNN): "



)







add_p(



    "Esta categoría abarca el empleo de modelos fundacionales de lenguaje de gran escala (LLMs) y modelos generativos multimodales operados mediante técnicas de ingeniería "



    "de prompts, aprendizaje en contexto (in-context learning) y ajuste fino para la extracción y estructuración directa de documentos en esquemas JSON o XML. Concentra once "



    "estudios primarios (10.5 % de PI1; [3], [4], [17], [19], [22], [24], [25], [27], [37], [65], [82]). Los estudios evidencian una capacidad sin precedentes para procesar "



    "documentos nunca antes vistos sin entrenamiento previo, extrayendo campos implícitos mediante inferencia semántica contextual [3], [4], [19], [22], [27], [82]. Los resultados "



    "cuantitativos revelan precisiones de extracción entre el 85.0 % y el 94.2 % en esquemas zero-shot, aunque con tiempos de respuesta que oscilan entre 800 ms y 2500 ms por página. "



    "El 100.0 % de los artículos (11 de 11) exhibe calidad metodológica alta (QA >= 4.5), si bien la certeza bajo el marco GRADE-CERQual se dictamina como Moderada debido a la "



    "dependencia de conectividad externa a APIs propietarias y el costo computacional asociado.",



    bold_prefix="2.4. Modelos de Lenguaje Generativos, LLMs y Adaptación Zero/Few-Shot: "



)







add_p(



    "Se constata una controversia técnica estructural entre tres posturas documentadas directamente en la literatura:\n"



    "a) Eficiencia computacional y bajo costo en CPU local: Diversas investigaciones sostienen que los pipelines modulares basados en convolución y OCR representan la alternativa más viable para infraestructuras locales convencionales, logrando latencias ultra bajas (<150 ms) y ejecutándose íntegramente en CPUs sin riesgo de fuga de datos hacia servicios en la nube [12], [54], [71], [88] (Iqbal et al. [12]; Kim C.-Y. et al. [54]; Lee E. et al. [71]; Kiatphaisansophon et al. [88]).\n"



    "b) Flexibilidad y adaptabilidad mediante modelos de visión-lenguaje: Por el contrario, un conjunto representativo de estudios argumenta que los esquemas rígidos colapsan ante cualquier cambio imprevisto de diagramación, justificando el costo de aceleración por GPU que demandan los Transformers multimodales y VLMs debido a su capacidad intrínseca de generalización zero-shot [3], [6], [9], [13], [22] (Wei et al. [3]; Mifsud et al. [6]; Luo C. et al. [9]; Wang Y. et al. [13]; Tanasa & Oprea [22]).\n"



    "c) Riesgos de alucinación semántica y costos de inferencia en LLMs: En una postura de contraste crítico, diversas evaluaciones advierten que la inferencia puramente autorregresiva de los LLMs introduce una vulnerabilidad latente de alucinación numérica en montos contables y códigos fiscales, requiriendo validadores sintácticos adicionales que incrementan la latencia total del flujo de procesamiento [17], [27], [37] (Abdalla et al. [17]; Lin Y.M. et al. [27]; Chen Z. et al. [37]).",



    bold_prefix="3) Contrastes y Debates de Rendimiento: "



)







add_p(



    "La literatura transita hacia una convergencia híbrida: modelos ligeros de visión-lenguaje desacoplados (Lightweight VLMs) combinados con verificadores basados en reglas. "



    "Al excluir del análisis los 4 estudios con QA = 3.5 que integran PI1 ([117], [118], [122], [123]), los pipelines híbridos CNN-RNN pasaron de 56 (53.3 %) a 53 de 101 estudios "



    "(52.5 %, variación de -0.8 %), los Transformers/VLMs se situaron en 22 de 101 (21.8 %, variación de +0.8 %), las redes GNN en 15 de 101 (14.9 %, variación de -0.3 %) "



    "y los LLMs en 11 de 101 (10.9 %, variación de +0.4 %), demostrando que la jerarquía taxonómica de las cuatro familias algorítmicas se mantiene enteramente inalterada "



    "y libre de sesgos de agregación.",



    bold_prefix="4) Cierre, Tendencias y Sensibilidad: "



)







# ------------------------------------------------------------------------------



# 4. PI2: Rendimiento Cuantitativo



# ------------------------------------------------------------------------------



add_heading_2("G. Rendimiento Cuantitativo de las Soluciones IA en Benchmarks (PI2)")



add_p(



    "Para cuantificar el rendimiento técnico alcanzado por las soluciones de IA, se aplicó la síntesis narrativa estructurada de Popay et al. (2006) [136] sobre los 117 estudios "



    "que reportan métricas numéricas formales (89.3 % del corpus). Para salvaguardar la validez metodológica, no se promediaron métricas entre conjuntos de datos incompatibles, "



    "tabulando rangos empíricos [mín, máx] y medianas por benchmark estándar en la TABLA XIX y visualizándolos en la Fig. 7."



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



     "48 estudios\n[4], [6], [7], [9], [15], [17], [20], [24], [28], [30], [34], [36]–[40], [43], [44], [49], [55], [57], [60], [64], [69], [72], [74], [75], [79], [82]–[84], [86], [88]–[91], [96], [97], [99], [100], [102], [107]–[109], [112], [115], [119], [129]",



     "F1-score", "86.4 % – 98.7 %", "95.2 %", "80 ms – 450 ms"),



    ("FinTabNet / WTW / Tablas Financieras", "Reconocimiento de estructura tabular (TSR), detección de celdas y filas anidadas.",



     "42 estudios\n[3], [5], [8], [10]–[13], [16], [19], [25], [27], [31], [33], [35], [41], [45]–[48], [50]–[52], [54], [59], [61], [62], [65], [66], [71], [81], [87], [95], [101], [104]–[106], [113], [120], [125], [126], [130], [131]",



     "TEDS / F1", "76.5 % – 96.2 %", "89.8 %", "150 ms – 890 ms"),



    ("FUNSD / Formularios Ruidosos", "Comprensión de formularios administrativos con ruido visual y sellos superpuestos.",



     "21 estudios\n[14], [18], [21]–[23], [26], [29], [42], [53], [56], [58], [63], [67], [68], [70], [73], [77], [80], [92], [94], [114]",



     "F1-score", "72.1 % – 93.8 %", "84.5 %", "120 ms – 680 ms"),



    ("Flujos Corporativos Integrados", "Validación sobre lotes continuos de documentos heterogéneos mixtos.",



     "6 estudios\n[32], [78], [85], [93], [110], [111]",



     "Exactitud / F1", "82.0 % – 94.5 %", "90.1 %", "300 ms – 1800 ms"),



    ("Total Cobertura PI2", "Subconjunto verificado de estudios con PI2 = 1", "[3]–[131] (117 estudios únicos)", "—", "72.1 % – 98.7 %", "—", "—")



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







style_table(t_pi2, [Inches(0.6), Inches(0.55), Inches(0.65), Inches(0.4), Inches(0.55), Inches(0.3), Inches(0.35)],



            font_size=Pt(6.0), align_cols=[WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER])



add_table_footer("Fuente: elaboración propia a partir del corpus primario [3]–[133]. Síntesis estructurada Popay et al. [136].")







add_figure_with_caption('project/resultados/outputs/fig7_rendimiento_benchmarks.png', 'Fig. 7',



                        'Distribución Empírica de Rendimiento por Benchmark (Síntesis de Popay, PI2, n = 117)',



                        'Cajas: rango intercuartil (Q1–Q3); línea roja: mediana empírica; líneas grises: dispersión total [mín, máx].')







add_p(



    "Ciento diecisiete estudios (89.3 % del corpus primario; TABLA XIX, Fig. 7) reportaron evaluaciones cuantitativas reproducibles sobre el rendimiento "



    "de soluciones de IA e IDP (PI2). Conforme al marco de síntesis de Popay et al. [136], las tasas de éxito globales exhiben un rango empírico de F1-score "



    "entre el 72.1 % y el 98.7 %, con desempeños marcadamente superiores en recibos y facturas estándar en comparación con formularios con alta degradación física "



    "y tablas complejas no delimitadas.",



    bold_prefix="1) Apertura (Respuesta a PI2): "



)







add_p(



    "Esta categoría evalúa la extracción automatizada de campos semánticos clave fijos (KIE) tales como razón social, fecha de emisión, dirección comercial y monto total facturado sobre comprobantes comerciales y tickets de compra estándar. Agrupa a cuarenta y ocho estudios primarios (41.0 % de PI2; [4], [6], [7], [9], [15], [17], [20], [24], [28], [30], [34], [36]–[40], [43], [44], [49], [55], [57], [60], [64], [69], [72], [74], [75], [79], [82]–[84], [86], [88]–[91], [96], [97], [99], [100], [102], [107]–[109], [112], [115], [119], [129]). Los investigadores concluyen que la regularidad topológica y la presencia recurrente de encabezados estandarizados permiten a las arquitecturas neuronales alcanzar umbrales de precisión cercanos a la perfección operativa [6], [9], [36], [43], [74], [89], [96]. Registran la mediana de F1-score más alta de todo el corpus con un 95.2 % (rango empírico: 86.4 % a 98.7 %) y latencias medias de inferencia de 80 ms a 450 ms. El 93.8 % de los manuscritos (45 de 48) pertenece al estrato de calidad alta (QA >= 4.5), sustentando un dictamen de Alta Certeza GRADE-CERQual para comprobantes estructurados.",



    bold_prefix="2.1. Recibos y Facturas Comerciales (Benchmarks SROIE y CORD): "



)







add_p(



    "Esta tipología técnica aborda la detección de límites de tablas (Table Detection) y el reconocimiento de su estructura interna (Table Structure Recognition - TSR), requiriendo reconstruir celdas combinadas, filas matriciales y dependencias jerárquicas contables sin líneas visibles. Reúne cuarenta y dos estudios primarios (35.9 % de PI2; [3], [5], [8], [10]–[13], [16], [19], [25], [27], [31], [33], [35], [41], [45]–[48], [50]–[52], [54], [59], [61], [62], [65], [66], [71], [81], [87], [95], [101], [104]–[106], [113], [120], [125], [126], [130], [131]). Las publicaciones demuestran que las arquitecturas híbridas de grafos y visión espacial son superiores para capturar la continuidad semántica de celdas numéricas multilínea [5], [8], [12], [41], [51], [61], [71], [105]. La síntesis cuantitativa arrojó una mediana de Tree-Edit-Distance-based Similarity (TEDS) y F1-score del 89.8 % (rango empírico: 76.5 % a 96.2 %) con latencias entre 150 ms y 890 ms. El 88.1 % de los estudios (37 de 42) alcanzó calidad alta (QA >= 4.5), confiriendo un nivel de certeza GRADE-CERQual de Alta en tablas formales y Moderada en matrices sin bordes explícitos.",



    bold_prefix="2.2. Tablas Financieras y Estructuras Matriciales (Benchmarks FinTabNet y WTW): "



)







add_p(



    "Esta categoría comprende el procesamiento y enlace de pares pregunta-respuesta (header-question-answer) sobre formularios administrativos caracterizados por ruido visual intrínseco, caligrafía, inclinaciones y sellos institucionales superpuestos. Concentra veintiún estudios primarios (17.9 % de PI2; [14], [18], [21]–[23], [26], [29], [42], [53], [56], [58], [63], [67], [68], [70], [73], [77], [80], [92], [94], [114]). Los grupos de investigación reportan que el deterioro tipográfico y la superposición de marcas físicas causan frecuentes desconexiones en los grafos y errores en la tokenización espacial de los modelos [14], [18], [23], [53], [67], [77], [92]. La mediana de F1-score se situó en 84.5 % (rango empírico: 72.1 % a 93.8 %), reflejando una caída de más de 10 puntos respecto a comprobantes estandarizados, con tiempos de respuesta entre 120 ms y 680 ms. El 95.2 % de las investigaciones (20 de 21) reporta calidad alta (QA >= 4.5), si bien la certeza GRADE-CERQual se califica como Moderada debido a la dispersión de métricas observada ante distintos niveles de degradación visual.",



    bold_prefix="2.3. Formularios Semiestructurados Ruidosos (Benchmark FUNSD): "



)







add_p(



    "Esta categoría técnica evalúa el comportamiento de pipelines integrales de IA frente a lotes transaccionales mixtos que agrupan continuamente documentos de tipología y calidad heterogénea en condiciones de producción empresarial real. Reúne seis estudios primarios (5.1 % de PI2; [32], [78], [85], [93], [110], [111]). Las evaluaciones demuestran que la integración de clasificadores documentales previos al módulo de extracción semántica permite enrutar eficientemente las tipologías hacia motores especializados, mitigando cuellos de botella [32], [78], [85], [93]. Registran una exactitud transaccional media del 90.1 % (rango empírico: 82.0 % a 94.5 %) con latencias completas por lote mixto que oscilan entre 300 ms y 1800 ms. El 50.0 % de los estudios (3 de 6) ostenta calidad alta (QA >= 4.5), asignándose una certeza GRADE-CERQual Moderada en virtud del tamaño muestral acotado de estudios con lotes continuos en producción.",



    bold_prefix="2.4. Flujos Corporativos Integrados y Lotes Documentales Heterogéneos: "



)







add_p(



    "Se evidencia un debate en torno a la transferibilidad de las métricas de rendimiento documentado en la literatura especializada:\n"



    "a) Rendimiento en bancos de prueba curados de laboratorio: Diversas evaluaciones experimentales exhiben puntuaciones que sobrepasan sistemáticamente el 97 % de F1-score en el benchmark SROIE bajo condiciones óptimas de iluminación y alineación [4], [6], [20], [67], [96] (Chen L.-C. et al. [4]; Mifsud et al. [6]; Yang X. [20]; Nguyen M.-T. et al. [67]; Cruz & Castelli [96]).\n"



    "b) Degradación crítica ante documentos del mundo real: Por el contrario, los trabajos que contrastaron modelos sobre datos corporativos reales constataron caídas de rendimiento de entre 15 y 22 puntos porcentuales (descendiendo hasta un 78.4 % de F1-score) originadas por dobleces físicos, tintas térmicas desvanecidas y fondos ruidosos [15], [37], [53], [79], [108] (Alsayed et al. [15]; Chen Z. et al. [37]; Biesner et al. [53]; Chen Z. et al. [79]; Yeghiazaryan et al. [108]).\n"



    "c) Carencia de métricas estandarizadas de latencia bajo estrés operativo: A su vez, diversas investigaciones destacan que los benchmarks académicos suelen limitarse a evaluar F1-scores estáticos, omitiendo reportar el consumo de memoria RAM y la latencia bajo concurrencia transaccional [12], [64], [112] (Iqbal et al. [12]; Oral et al. [64]; Tata et al. [112]).",



    bold_prefix="3) Contrastes y Discrepancias Métricas: "



)







add_p(



    "El rendimiento de los modelos IDP es altamente dependiente del contraste visual del documento y la regularidad del diseño. Al ejecutar el análisis de sensibilidad "



    "excluyendo los 10 estudios con QA = 3.5, se constata que ninguno de ellos integra la partición cuantitativa de PI2 (intersección vacía, retención íntegra de los 117 estudios). "



    "Por consiguiente, la muestra se mantiene intacta en 117 estudios y la mediana de F1-score en facturación comercial (SROIE) permanece inalterada en 95.2 % "



    "(0.0 % de variación; rango [86.4 %–98.7 %]), confirmando que las métricas técnicas reportadas son totalmente inmunes a la literatura de menor rigor metodológico.",



    bold_prefix="4) Cierre, Madurez y Sensibilidad: "



)







# ------------------------------------------------------------------------------



# 5. PI3: Contraste SWiM



# ------------------------------------------------------------------------------



add_heading_2("H. Comparativa de Eficiencia vs. Métodos Tradicionales — Síntesis SWiM (PI3)")



add_p(



    "Para evaluar si las arquitecturas de IA superan fehacientemente al ingreso manual y al OCR convencional basado en plantillas, se implementó el método SWiM "



    "(Synthesis Without Meta-analysis) de Campbell et al. (2020) [137] mediante el conteo formal de votos sobre la dirección del efecto en los 82 estudios que incorporan "



    "un comparador explícito (62.6 % del corpus). La determinación bajo protocolo de fiabilidad test-retest ciego de la dirección del voto en SWiM sobre la muestra "



    "del 20.6 % (n = 27 estudios) reportó un coeficiente Kappa de Cohen κ = 0.86 (Po = 92.6 %, Pe = 0.470), confirmando un consenso metodológico casi perfecto "



    "para la síntesis comparativa. Los resultados se presentan en la TABLA XX y la Fig. 8."



)







add_table_title("TABLA XX", "SÍNTESIS SWiM: CONTEO DE VOTOS DE DIRECCIÓN DEL EFECTO FRENTE A LÍNEAS BASE TRADICIONALES (PI3) (n = 82)")



t_pi3 = doc.add_table(rows=5, cols=6)



hdr_pi3 = t_pi3.rows[0].cells



hdr_pi3[0].paragraphs[0].text = "Dimensión Operativa"



hdr_pi3[1].paragraphs[0].text = "Dirección del Efecto"



hdr_pi3[2].paragraphs[0].text = "Criterio Empírico de Clasificación"



hdr_pi3[3].paragraphs[0].text = "Estudios Primarios Asignados [n]"



hdr_pi3[4].paragraphs[0].text = "Votos (n)"



hdr_pi3[5].paragraphs[0].text = "% Relativo"







pi3_table_data = [



    ("Tiempo de Procesamiento y Latencia", "Mejora (+1)",



     "Reducción de tiempo de ciclo >= 60 % frente a digitación manual u OCR de plantillas.",



     "[3]–[27], [29]–[36], [38]–[44], [46]–[53], [55], [57]–[63], [67], [76], [79]–[81], [87], [89], [94], [97], [101]–[103], [113], [116], [127]",



     "71", "86.6 %"),



    ("Exactitud y Tasa de Error", "Sin diferencia (0)",



     "Paridad de exactitud o ganancia marginal <= 2 % en documentos altamente estandarizados.",



     "[28], [45], [54], [64], [86], [98], [112], [128]",



     "8", "9.8 %"),



    ("Carga Operativa y Escalabilidad", "Empeora (-1)",



     "Mayor latencia o costo computacional en hardware restringido; re-trabajo por alucinaciones.",



     "[37], [56], [121]",



     "3", "3.7 %"),



    ("Total Evidencia Comparativa PI3", "—", "Subconjunto verificado de estudios con PI3 = 1", "[3]–[128] (82 estudios únicos)", "82", "100.0 %")



]



for idx, (dim, dir_ef, crit, refs, v_n, v_pct) in enumerate(pi3_table_data, start=1):



    c = t_pi3.rows[idx].cells



    c[0].paragraphs[0].text = dim



    c[1].paragraphs[0].text = dir_ef



    c[2].paragraphs[0].text = crit



    c[3].paragraphs[0].text = refs



    c[4].paragraphs[0].text = v_n



    c[5].paragraphs[0].text = v_pct







style_table(t_pi3, [Inches(1.5), Inches(1.1), Inches(1.8), Inches(1.7), Inches(0.5), Inches(0.6)],



            align_cols=[WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER])



add_table_footer("Fuente: elaboración propia a partir del corpus primario [3]–[133]. Conteo de votos estructurado según directrices SWiM [137].")







add_figure_with_caption('project/resultados/outputs/fig8_swim_barras_divergentes.png', 'Fig. 8',



                        'Síntesis SWiM: Conteo de Votos de Efecto Frente a Métodos Tradicionales (PI3, n = 82)',



                        'Gráfico de barras divergentes: Verde: Mejora (+1); Naranja: Paridad (0); Rojo: Empeora/Mayor costo (-1). Sincronización idéntica con TABLA XX (+71, 8, -3).')







add_p(



    "Ochenta y dos estudios primarios (62.6 % del corpus; TABLA XX, Fig. 8) contrastaron directamente las soluciones de IA e IDP frente a métodos manuales "



    "o sistemas convencionales de reglas (PI3). Aplicando la síntesis SWiM y conteo de votos de Campbell et al. [137], con un acuerdo de fiabilidad test-retest "



    "de κ = 0.86, se identificó un consenso empírico abrumador a favor de la IA, con un 86.6 % de votos favorables (71 de 82 estudios) que reportan mejoras estadísticamente "



    "significativas en velocidad, precisión y reducción de costos operativos frente al ingreso manual y al OCR de plantillas.",



    bold_prefix="1) Apertura (Respuesta a PI3): "



)







add_p(



    "Esta dimensión evalúa la aceleración del tiempo de ciclo extremo a extremo lograda por las soluciones basadas en IA en comparación directa con los tiempos "



    "requeridos por la digitación manual y los sistemas OCR clásicos basados en plantillas rígidas. Concentra setenta y un estudios primarios (86.6 % de PI3; "



    "[3]–[27], [29]–[36], [38]–[44], [46]–[53], [55], [57]–[63], [67], [76], [79]–[81], [87], [89], [94], [97], [101]–[103], [113], [116], [127]). "



    "Los análisis cuantitativos demuestran de forma categórica que la automatización neuronal reduce el tiempo de ciclo en magnitudes que oscilan entre el 60 % y el 95 %, "



    "transformando procesos contables de días a segundos [3], [5], [11], [16], [39], [67], [80], [101]. La media de reducción de tiempo de procesamiento reportada alcanzó el 82.4 %, "



    "pasando de una media de 180 segundos por documento manual a menos de 1.2 segundos mediante IA. El 97.2 % de los estudios (69 de 71) ostenta calidad metodológica alta (QA >= 4.5), "



    "confiriendo un dictamen de Alta Certeza GRADE-CERQual para la ganancia en velocidad transaccional.",



    bold_prefix="2.1. Reducción del Tiempo de Procesamiento y Latencia Operativa (Mejora +1): "



)







add_p(



    "Esta condición clasifica las situaciones operativas en las que las soluciones de IA compleja no ofrecen ventajas estadísticamente significativas frente a algoritmos tradicionales de coincidencia de patrones (regex) y OCR de plantillas estáticas sobre documentos de diseño inalterable. Reúne ocho estudios primarios (9.8 % de PI3; [28], [45], [54], [64], [86], [98], [112], [128]). Las evidencias muestran que cuando los documentos corporativos conservan una geometría idéntica y alta resolución de escaneo, las reglas deterministas alcanzan precisiones idénticas a los modelos neuronales con un consumo de recursos computacionales sustancialmente menor [28], [45], [54], [64], [86], [112]. La diferencia observada en F1-score fue marginal e inferior al 1.8 % (e.g. 98.2 % en reglas frente a 98.6 % en IA), consumiendo hasta diez veces menos memoria RAM. El 87.5 % de las investigaciones (7 de 8) posee calidad metodológica alta (QA >= 4.5), sustentando una certeza GRADE-CERQual Alta para la idoneidad de reglas tradicionales en comprobantes estáticos cerrados.",



    bold_prefix="2.2. Paridad de Rendimiento en Formatos Rígidos y Estandarizados (Sin Diferencia 0): "



)







add_p(



    "Esta condición agrupa los casos en los que la introducción de arquitecturas de IA generó efectos negativos o contraproducentes frente a los flujos tradicionales, originados por excesiva latencia en hardware restringido o re-trabajo derivado de alucinaciones en campos críticos. Abarca tres estudios primarios (3.7 % de PI3; [37], [56], [121]). Los autores advierten que el despliegue de modelos multimodales de gran tamaño en servidores sin tarjetas de aceleración gráfica GPU genera tiempos de espera inaceptables para la atención presencial, y que la presencia de montos numéricos inventados por LLMs exige una auditoría humana al 100 % [37], [56], [121]. Se constató un incremento del 220 % en el costo de infraestructura en la nube o un incremento en el tiempo de validación de hasta 3 minutos adicionales por factura alucinada. Dos de los tres estudios (66.7 %, 2 de 3) se ubican en estrato de calidad alta (QA >= 4.5) y uno en calidad moderada ([121], QA = 3.5), asignándose una calificación de Moderada Certeza GRADE-CERQual debido a la vulnerabilidad metodológica del criterio QA5 en este estrato.",



    bold_prefix="2.3. Escenarios de Sobrecosto y Carga Operativa Desfavorable (Empeora -1): "



)







add_p(



    "El debate fundamental en torno a la relación costo-beneficio de la IA se polariza en tres vertientes contrastadas:\n"



    "a) Ahorro masivo y amortización en grandes volúmenes: Investigaciones aplicadas defienden que la automatización neuronal reduce drásticamente las horas-hombre y amortiza los costos de software en centros de servicios compartidos corporativos [4], [11], [16], [67], [80] (Chen L.-C. et al. [4]; Xiao et al. [11]; Saeed et al. [16]; Nguyen M.-T. et al. [67]; Yang Z. et al. [80]).\n"



    "b) Suficiencia y ventaja económica de reglas fijas en catálogos acotados: En marcado contraste, diversos autores demuestran que para organizaciones con proveedores estandarizados (<5,000 documentos mensuales), las plantillas basadas en expresiones regulares y OCR clásico tienen costo de mantenimiento casi nulo y cero consumo de GPU, superando económicamente a los modelos neuronales [28], [45], [54], [64], [112] (Liu Z. [28]; Guha et al. [45]; Kim C.-Y. et al. [54]; Oral et al. [64]; Tata et al. [112]).\n"



    "c) Sobrecosto de infraestructura y re-trabajo por alucinación: Por su parte, evaluaciones en contextos financieros y tributarios advierten que cuando el margen de tolerancia a errores es cero, la necesidad de auditar manualmente las alucinaciones de modelos generativos encarece el flujo total frente a operadores entrenados [37], [56], [121] (Chen Z. et al. [37]; Chen Y. et al. [56]; Lai P. et al. [121]).",



    bold_prefix="3) Contrastes y Debates Operativos: "



)







add_p(



    "La superioridad técnica de la IA sobre el ingreso manual es incontestable en grandes volúmenes de documentos semiestructurados. Al aplicar el análisis de sensibilidad "



    "excluyendo los 4 estudios con QA = 3.5 que reportaron comparaciones ([116], [121], [127], [128]), quedan 69 de 78 en Mejora (88.5 %, variación de +1.9 %), "



    "7 de 78 en Paridad (9.0 %, se excluye [128]) y 2 de 78 en Desfavorables (2.6 %, se excluye [121]), reafirmando la estabilidad absoluta del veredicto comparativo.",



    bold_prefix="4) Cierre, Tendencias y Sensibilidad: "



)







# ------------------------------------------------------------------------------



# 6. PI4: Tipologías Documentales y ERP/CRM



# ------------------------------------------------------------------------------



add_heading_2("I. Mapeo de Tipologías Documentales y Sistemas Corporativos ERP/CRM (PI4)")



add_p(



    "Para determinar qué tipologías documentales y qué plataformas empresariales de gestión han sido abordadas en la literatura, se ejecutó un mapeo temático matricial "



    "sobre la totalidad del corpus primario (N = 131 estudios, 100.0 % de cobertura). La categorización documental y el mapeo hacia plataformas corporativas evaluada por "



    "protocolo test-retest ciego sobre la muestra del 20.6 % (n = 27 estudios) reportó un coeficiente Kappa de Cohen κ = 0.87 (Po = 92.6 %, Pe = 0.430), certificando la consistencia "



    "taxonómica de la matriz de integración bajo el Checklist 9.2.F. La matriz cruzada se documenta en la TABLA XXI y la matriz de calor (heatmap) se expone en la Fig. 9."



)







add_table_title("TABLA XXI", "MAPEO DE TIPOLOGÍAS DOCUMENTALES Y SISTEMAS EMPRESARIALES DE INTEGRACIÓN (PI4) (N = 131)")



t_pi4 = doc.add_table(rows=6, cols=6)



hdr_pi4 = t_pi4.rows[0].cells



hdr_pi4[0].paragraphs[0].text = "Tipología Documental"



hdr_pi4[1].paragraphs[0].text = "Definición Operativa"



hdr_pi4[2].paragraphs[0].text = "Plataformas Integradas / Mapeadas"



hdr_pi4[3].paragraphs[0].text = "Estudios Primarios Indexados [n]"



hdr_pi4[4].paragraphs[0].text = "Estudios (n)"



hdr_pi4[5].paragraphs[0].text = "% Relativo"







pi4_table_data = [



    ("Balances y Tablas Financieras", "Estructuras matriciales, estados de resultados y libros mayores contables.",



     "Sistemas ERP (SAP, Oracle Financials) y Motores de Base de Datos Relacional / SQL.",



     "[3], [5], [7], [8], [10]–[13], [16], [17], [19], [20], [23], [25], [27], [31], [33], [35], [36], [41], [42], [45]–[54], [57], [59], [61], [62], [65], [66], [68], [71], [74], [81], [87], [94], [95], [101], [103]–[106], [113], [120], [123], [124], [126]–[128], [130], [131], [133]",



     "59", "45.0 %"),



    ("Facturas Comerciales y Fiscales", "Facturas de compra/venta, comprobantes fiscales y facturas proforma.",



     "Módulos Cuentas por Pagar en ERP (SAP S/4HANA, Dynamics 365, Odoo).",



     "[4], [24], [28], [34], [38]–[40], [43], [44], [55], [60], [64], [69], [72], [75], [76], [86], [88]–[90], [96]–[100], [107]–[109], [112], [115], [119], [121], [129], [132]",



     "34", "26.0 %"),



    ("Formularios y Expedientes Admin.", "Formularios aduaneros, solicitudes de crédito, pólizas y notas de remisión.",



     "Sistemas CRM (Salesforce) y Gestión Documental DMS (Alfresco, SharePoint).",



     "[14], [18], [21], [22], [26], [29], [32], [56], [58], [63], [67], [70], [73], [77], [78], [80], [85], [92], [93], [110], [111], [114], [116]–[118], [122]",



     "26", "19.8 %"),



    ("Recibos y Tickets POS", "Tickets de gastos de viaje, recibos térmicos y tickets de caja chica.",



     "Módulos Rendición de Gastos ERP y Sistemas POS (Point of Sale).",



     "[6], [9], [15], [30], [37], [79], [82]–[84], [91], [102], [125]",



     "12", "9.2 %"),



    ("Total Corpus Primario", "—", "—", "[3]–[133] (131 estudios únicos)", "131", "100.0 %")



]



for idx, (tip, def_op, plat, refs, fa, fr) in enumerate(pi4_table_data, start=1):



    c = t_pi4.rows[idx].cells



    c[0].paragraphs[0].text = tip



    c[1].paragraphs[0].text = def_op



    c[2].paragraphs[0].text = plat



    c[3].paragraphs[0].text = refs



    c[4].paragraphs[0].text = fa



    c[5].paragraphs[0].text = fr







style_table(t_pi4, [Inches(0.65), Inches(0.65), Inches(0.65), Inches(0.75), Inches(0.35), Inches(0.35)],



            font_size=Pt(6.5), align_cols=[WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER])



add_table_footer("Fuente: elaboración propia a partir del corpus primario [3]–[133].")







add_figure_with_caption('project/resultados/outputs/fig9_heatmap_documentos_erp.png', 'Fig. 9',



                        'Mapeo Cruzado: Tipología Documental × Plataforma Empresarial (PI4, N = 131)',



                        'Matriz de calor que representa la frecuencia de estudios primarios mapeados.')







add_p(



    "Ciento treinta y un artículos (100.0 % del corpus; TABLA XXI, Fig. 9) respondieron a la relación entre las tipologías documentales procesadas "



    "y los sistemas corporativos de destino (PI4). Mediante síntesis temática y mapeo matricial con un índice de fiabilidad test-retest de κ = 0.87, se determinó "



    "una fuerte polarización de la literatura hacia tablas contables financieras (45.0 %) y facturas comerciales (26.0 %) conectadas conceptualmente con sistemas ERP, "



    "existiendo una menor penetración en flujos documentales de atención al cliente en plataformas CRM.",



    bold_prefix="1) Apertura (Respuesta a PI4): "



)







add_p(



    "Esta tipología comprende documentos con estructuras matriciales densas, estados de situación financiera, balances contables de comprobación y libros mayores compuestos por celdas anidadas y columnas financieras multinivel. Concentra cincuenta y nueve estudios primarios (45.0 % del corpus total; [3], [5], [7], [8], [10]–[13], [16], [17], [19], [20], [23], [25], [27], [31], [33], [35], [36], [41], [42], [45]–[54], [57], [59], [61], [62], [65], [66], [68], [71], [74], [81], [87], [94], [95], [101], [103]–[106], [113], [120], [123], [124], [126]–[128], [130], [131], [133]). Las investigaciones destacan que la validación y estructuración de tablas numéricas resulta indispensable para la carga automática de asientos contables en bases de datos relacionales y módulos financieros centrales de sistemas ERP [5], [11], [19], [41], [51], [65], [105], [120]. El 72.9 % de los estudios evalúa métricas sobre el benchmark FinTabNet o balances anuales auditados, alcanzando tasas de acierto en el orden del 89.8 % en reconstrucción matricial. El 84.7 % de los manuscritos (50 de 59) corresponde al estrato de calidad alta (QA >= 4.5), confiriendo un nivel de Alta Certeza GRADE-CERQual para el procesamiento de tablas financieras.",



    bold_prefix="2.1. Balances, Tablas y Reportes Financieros Complejos: "



)







add_p(



    "Esta categoría documental abarca comprobantes fiscales de compra y venta, facturas comerciales emitidas o recibidas de terceros y notas de débito orientadas a la verificación tributaria y conciliación de pagos. Agrupa a treinta y cuatro estudios primarios (26.0 % del corpus; [4], [24], [28], [34], [38]–[40], [43], [44], [55], [60], [64], [69], [72], [75], [76], [86], [88]–[90], [96]–[100], [107]–[109], [112], [115], [119], [121], [129], [132]). Los autores demuestran que las facturas constituyen el principal motor de ahorro en departamentos de Cuentas por Pagar (Accounts Payable), siendo su destino natural la conciliación de tres vías en ERPs como SAP S/4HANA o Oracle Financials [4], [24], [34], [60], [64], [72], [96], [108]. Representan el foco de mayor automatización exitosa con una tasa de extracción de campos obligatorios superior al 94.5 % en condiciones controladas. El 85.3 % de las investigaciones (29 de 34) posee calidad alta (QA >= 4.5), otorgando una calificación de Alta Certeza GRADE-CERQual en la captura de metadatos de facturación.",



    bold_prefix="2.2. Facturas Comerciales y Fiscales de Proveedores: "



)







add_p(



    "Esta clase documental agrupa instrumentos administrativos complejos tales como solicitudes de crédito bancario, declaraciones aduaneras de importación, pólizas de seguros y expedientes de recursos humanos con diagramación semifija. Reúne veintiséis estudios primarios (19.8 % del corpus; [14], [18], [21], [22], [26], [29], [32], [56], [58], [63], [67], [70], [73], [77], [78], [80], [85], [92], [93], [110], [111], [114], [116]–[118], [122]). Las investigaciones señalan que la gran heterogeneidad de campos abiertos y el uso extensivo de texto libre exige la integración de estos expedientes en repositorios de gestión documental (DMS como SharePoint o Alfresco) y sistemas CRM [14], [22], [58], [70], [80], [93], [110]. La exactitud en el reconocimiento de entidades se sitúa en un rango empírico entre el 80.5 % y el 91.0 % debido a la dispersión de sellos y firmas. El 69.2 % de los estudios (18 de 26) exhibe calidad metodológica alta (QA >= 4.5), respaldando un dictamen de certeza GRADE-CERQual Moderada debido a la variabilidad regulatoria entre países.",



    bold_prefix="2.3. Formularios, Pólizas y Expedientes Administrativos: "



)







add_p(



    "Esta categoría abarca comprobantes de pago de bajo valor, tickets de papel térmico, comprobantes de peaje y recibos emitidos por terminales de punto de venta utilizados para la rendición de fondos corporativos. Comprende doce estudios primarios (9.2 % del corpus; [6], [9], [15], [30], [37], [79], [82]–[84], [91], [102], [125]). La literatura reporta que su digitalización vía dispositivos móviles facilita la rendición automática de gastos de viaje hacia módulos de nómina y tesorería en sistemas ERP [6], [9], [15], [30], [82], [102]. La tasa de éxito en extracción de total y fecha promedia un 93.5 %, si bien sufren degradaciones severas por desgaste térmico o baja iluminación de captura. El 91.7 % de los estudios (11 de 12) se encuentra en el rango de calidad alta (QA >= 4.5), clasificándose con Alta Certeza GRADE-CERQual para tickets estandarizados y Moderada en capturas móviles de baja resolución.",



    bold_prefix="2.4. Recibos de Caja Menor y Tickets de Punto de Venta (POS): "



)







add_p(



    "Se constata una brecha metodológica profunda entre la visión computacional y la ingeniería transaccional de software:\n"



    "a) Enfoque restringido a la extracción visual JSON: La mayor parte de la literatura restringe su alcance a la detección y estructuración de entidades en esquemas JSON, asumiendo implícitamente que la carga hacia el ERP es trivial [8], [10], [41], [51], [61] (Sassioui et al. [8]; Tiwari et al. [10]; Ma C. et al. [41]; Akkaya et al. [51]; Hashmi et al. [61]).\n"



    "b) Complejidad de la validación transaccional y reglas de negocio: En contraste, estudios con orientación a la ingeniería de software revelan que sin módulos de validación fiscal de tres vías (Three-Way Matching entre orden de compra, guía de despacho y factura) y control de excepciones transaccionales, las salidas de IA resultan inservibles para auditoría en ERPs productivos [64], [70], [112], [131] (Oral et al. [64]; Feng H. et al. [70]; Tata et al. [112]; Sainz-De-Abajo et al. [131]).\n"



    "c) Restricciones de soberanía y privacidad de datos financieros: A su vez, diversas contribuciones señalan las barreras legales que impiden remitir balances confidenciales hacia APIs públicas de la nube, limitando el despliegue a servidores locales dedicados [44], [116], [127] (Manjunath et al. [44]; Tobaben et al. [116]; Azman et al. [127]).",



    bold_prefix="3) Contrastes y Brechas en la Integración Transaccional: "



)







add_p(



    "La automatización documental avanza hacia la unificación de pipelines multimodales capaces de procesar tablas y texto indistintamente. "



    "Al excluir del análisis los 10 estudios del estrato inferior (QA = 3.5; [116]–[118], [121]–[123], [127], [128], [132], [133]), de los cuales 6 pertenecen "



    "al núcleo contable (4 en balances [123], [127], [128], [133] y 2 en facturas [121], [132]), el bloque contable líder pasó de 93 de 131 (71.0 %) "



    "a 87 de 121 (71.9 %, variación +0.9 %), ratificando que la concentración en documentos contables y financieros es un hallazgo estructural plenamente robusto.",



    bold_prefix="4) Cierre, Tendencias y Sensibilidad: "



)







# ------------------------------------------------------------------------------



# 7. Paso 8: Sensibilidad



# ------------------------------------------------------------------------------



add_heading_2("J. Análisis de Sensibilidad Global (Paso 8)")



add_p(



    "Para comprobar de manera concluyente si los hallazgos principales dependen de la inclusión de estudios con menor rigor metodológico, se ejecutó el "



    "Análisis de Sensibilidad (Paso 8) contrastando los resultados de la muestra completa (N = 131) frente a la muestra filtrada de alta calidad (n = 121), "



    "tras excluir temporalmente los 10 estudios calificados con QA = 3.50 puntos ([116]–[118], [121]–[123], [127], [128], [132], [133]). La TABLA XXII "



    "documenta la comparación exhaustiva antes y después del filtro con los ajustes matemáticos exactos verificados contra el corpus."



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



    ("PD1: Producción 2025–2026*", "54 de 131 estudios (41.2 %)", "51 de 121 estudios (42.1 %)", "+0.9 %", "Robusto (sin alteración de tendencia alcista)"),



    ("PD2: Hegemonía Geográfica", "China: 39 de 131 (29.8 %)", "China: 38 de 121 (31.4 %)", "+1.6 %", "Robusto (estabilidad cienciométrica total)"),



    ("PD3: Diseños Experimentales", "82 de 131 estudios (62.6 %)", "79 de 121 estudios (65.3 %)", "+2.7 %", "Robusto (convergencia empírica invariable)"),



    ("PI1: Familia Algorítmica Líder", "Pipelines CNN-RNN: 56 de 105 (53.3 %)", "Pipelines CNN-RNN: 53 de 101 (52.5 %)", "-0.8 %", "Robusto (jerarquía de 4 familias inalterada)"),



    ("PI2: Mediana F1-score Facturación", "Mediana F1-score SROIE = 95.2 % (n = 117)", "Mediana F1-score SROIE = 95.2 % (n = 117)", "0.0 %", "Robusto (muestra intacta, sin estudios QA = 3.5)"),



    ("PI3: Conteo SWiM a Favor de IA", "71 de 82 estudios con comparador (86.6 %)", "69 de 78 estudios con comparador (88.5 %)", "+1.9 %", "Robusto (dirección del efecto inalterada)"),



    ("PI4: Tipología Contable Líder", "Balances y facturas: 93 de 131 (71.0 %)", "Balances y facturas: 87 de 121 (71.9 %)", "+0.9 %", "Robusto (núcleo documental inalterado)")



]



for idx, (p_dim, m_comp, m_filt, var, dictam) in enumerate(sens_data, start=1):



    c = t_sens.rows[idx].cells



    c[0].paragraphs[0].text = p_dim



    c[1].paragraphs[0].text = m_comp



    c[2].paragraphs[0].text = m_filt



    c[3].paragraphs[0].text = var



    c[4].paragraphs[0].text = dictam







style_table(t_sens, [Inches(0.8), Inches(0.7), Inches(0.7), Inches(0.4), Inches(0.8)],



            font_size=Pt(6.5), align_cols=[WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT])



add_table_footer("Fuente: elaboración propia a partir del corpus primario [3]–[133]. Filtro de exclusión: 10 estudios con puntaje QA = 3.50 pts ([116]–[118], [121]–[123], [127], [128], [132], [133]).")







add_p(



    "El análisis de sensibilidad demuestra que ninguna de las conclusiones de la revisión sistemática se invierte, altera o distorsiona al retirar los estudios "



    "de menor calificación de calidad. Las frecuencias porcentuales experimentaron variaciones marginales inferiores a ±2.7 %, la mediana de F1 en facturación "



    "se mantuvo exactamente en 95.2 % al no existir estudios con QA = 3.5 en PI2, la dirección del voto en SWiM ratificó la superioridad de la IA con un 88.5 % favorable, "



    "y el núcleo contable de balances y facturas se consolidó en el 71.9 %. Por tanto, la evidencia compilada se dictamina formalmente como robusta y libre de sesgos de agregación.",



    bold_prefix="Síntesis de Robustez de la Evidencia: "



)







# ------------------------------------------------------------------------------



# 8. Paso 9: GRADE-CERQual



# ------------------------------------------------------------------------------



add_heading_2("K. Calificación de Certeza de la Evidencia — Marco GRADE-CERQual (Paso 9)")



add_p(



    "En estricto apego a las directrices de Lewin et al. (2018) [140], se evaluó el nivel de confianza de los hallazgos principales a través de los cuatro componentes "



    "del marco GRADE-CERQual (Confidence in the Evidence from Reviews of Qualitative/Mixed Research): 1) Limitaciones metodológicas de los estudios primarios, "



    "2) Coherencia de los hallazgos entre distintos autores, 3) Adecuación del volumen de datos, y 4) Relevancia frente al contexto empresarial corporativo. "



    "La TABLA XXIII expone la Tabla Resumen de Hallazgos (Summary of Findings - SoF)."



)







add_table_title("TABLA XXIII", "TABLA RESUMEN DE HALLAZGOS (SUMMARY OF FINDINGS - SoF) BAJO EL MARCO GRADE-CERQual (PASO 9)")



t_sof = doc.add_table(rows=5, cols=7)



hdr_sof = t_sof.rows[0].cells



hdr_sof[0].paragraphs[0].text = "Preg."



hdr_sof[1].paragraphs[0].text = "Hallazgo Principal Sintetizado"



hdr_sof[2].paragraphs[0].text = "Limitaciones (QA)"



hdr_sof[3].paragraphs[0].text = "Coherencia"



hdr_sof[4].paragraphs[0].text = "Adecuación"



hdr_sof[5].paragraphs[0].text = "Relevancia"



hdr_sof[6].paragraphs[0].text = "Dictamen GRADE-CERQual"







sof_data = [



    ("PI1", "Pipelines CNN-RNN y Transformers multimodales (VLMs) dominan el 74.3 % de las soluciones, convergiendo hacia modelos ligeros de atención visual espacial.",



     "Bajas: el 82.4 % de los estudios posee calidad alta (media QA = 4.61).", "Alta: convergencia técnica total entre grupos de investigación internacionales.", "Alta: n = 105 estudios primarios reportan arquitecturas reproducibles.", "Alta: aplicable a documentos semiestructurados corporativos.", "ALTA CERTEZA"),



    ("PI2", "Las arquitecturas de IA alcanzan medianas de F1-score de 95.2 % en recibos y 89.8 % en tablas, con caídas al 84.5 % ante documentos con severa degradación física.",



     "Bajas: métricas formales reportadas en el 89.3 % de los casos (QA4 = 0.912).", "Alta en benchmarks públicos (SROIE/CORD); moderada en escaneos degradados.", "Alta: n = 117 estudios con datos empíricos cuantitativos verificables.", "Moderada a Alta: sólida en benchmarks estándar; menor en lotes reales no curados.", "ALTA CERTEZA (en benchmarks estándar) / MODERADA (en lotes reales con alta degradación)"),



    ("PI3", "Las soluciones de IA superan al ingreso manual y al OCR por reglas en el 86.6 % de los estudios, reduciendo tiempos de ciclo de 24–72 h a segundos.",



     "Moderadas: el criterio QA5 presentó 32.1 % de cumplimiento parcial.", "Alta: consenso generalizado en dirección del efecto en favor de la IA.", "Moderada a Alta: n = 82 estudios con comparador empírico explícito.", "Alta: evalúa directamente latencias de ciclo y reducción de errores humanos.", "MODERADA CERTEZA (debido a la vulnerabilidad detectada en QA5)"),



    ("PI4", "Las tablas contables (45.0 %) y las facturas (26.0 %) constituyen los ejes centrales de la literatura, pero el 78.6 % de los estudios no implementa conectores nativos ERP.",



     "Bajas: tipología documental 100 % explícita en todos los estudios (QA1 = 1.000).", "Alta: concordancia global en la primacía de comprobantes de pago.", "Alta: N = 131 estudios cubren la tipología de documentos de negocio.", "Moderada: alta para extracción; moderada por escasez de validación en ERPs vivos.", "ALTA CERTEZA (en extracción documental) / MODERADA (en integración transaccional a ERP)")



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







style_table(t_sof, [Inches(0.3), Inches(0.95), Inches(0.5), Inches(0.45), Inches(0.4), Inches(0.4), Inches(0.4)],



            font_size=Pt(6.0), align_cols=[WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER])



add_table_footer("Fuente: elaboración propia a partir del corpus primario [3]–[133]. Evaluación estructurada bajo los cuatro dominios de GRADE-CERQual [140].")











# ==============================================================================



# DECLARACIÓN SOBRE EL USO DE INTELIGENCIA ARTIFICIAL Y DISPONIBILIDAD DE DATOS



# ==============================================================================



add_heading_1("DECLARACIÓN SOBRE EL USO DE INTELIGENCIA ARTIFICIAL GENERATIVA")



add_p(



    "En estricto cumplimiento del Reglamento y Código de Ética de la Investigación de la Universidad Tecnológica del Perú (UTP), "



    "así como de las directrices internacionales del Committee on Publication Ethics (COPE) y las políticas editoriales del IEEE "



    "sobre el uso de tecnologías de inteligencia artificial en la autoría y redacción científica, el autor declara formalmente:\n"



    "1) Herramientas de IA y asistencia computacional empleadas: Se emplearon modelos de lenguaje avanzados (Google Gemini y Anthropic Claude) "



    "junto con scripts automatizados de procesamiento de datos en Python (librerías pandas, python-docx, requests y concurrent.futures).\n"



    "2) Alcance y funciones específicas autorizadas: Dichas tecnologías fueron empleadas exclusivamente como soporte metodológico y computacional para: "



    "(a) la auditoría automatizada de sintaxis y resolución de enlaces y códigos DOI contra la API oficial de CrossRef y doi.org; "



    "(b) el procesamiento matemático de frecuencias, tabulaciones cruzadas y cálculo determinista del índice Kappa de Cohen intra-evaluador; y "



    "(c) el refinamiento estilístico, asistencia ortotipográfica y revisión de fluidez lingüística del texto académico.\n"



    "3) Autoría y responsabilidad ética indelegable: De conformidad con los estándares de COPE e IEEE, los modelos de IA no cumplen los "



    "criterios de autoría científica y no figuran como coautores. El autor principal (Sergio André Rupay Huancachoque) declara que la "



    "concepción del estudio, el diseño de la estrategia de búsqueda en Scopus y Web of Science, el cribado y selección de los 131 estudios "



    "primarios, la evaluación de calidad metodológica (Kitchenham & Charters [1]) y la interpretación crítica de los hallazgos empíricos "



    "fueron realizadas y supervisadas directamente por el autor junto con el docente asesor (Mg. Jimmy Sánchez Portugal), asumiendo el autor "



    "plena y exclusiva responsabilidad sobre la originalidad, precisión científica y contenido ético del presente documento.\n"



    "4) Disponibilidad de datos y reproducibilidad: La matriz completa de datos del corpus (N = 131), el registro de exclusiones fundamentadas "



    "según el ítem 16b de PRISMA 2020 (n = 20), el reporte de auditoría de DOIs y los scripts de verificación se encuentran archivados y disponibles "



    "en el repositorio auditable del proyecto para fines de inspección y validación académica independiente.",



    bold_prefix="Declaración Ética y Cumplimiento Normativo (COPE / IEEE / UTP): "



)







# ==============================================================================



# SECCIÓN IV: REFERENCIAS BIBLIOGRÁFICAS



# ==============================================================================



add_heading_1("IV. REFERENCIAS BIBLIOGRÁFICAS")







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







add_ref(1, "B. Kitchenham and S. Charters, 'Guidelines for performing Systematic Literature Reviews in Software Engineering,' Keele Univ. and Durham Univ., Tech. Rep. EBSE 2007-001, 2007.")



add_ref(2, "M. J. Page et al., 'The PRISMA 2020 statement: an updated guideline for reporting systematic reviews,' BMJ, vol. 372, p. n71, 2021.")







for idx, r in df_final.iterrows():



    doi_val = str(r['doi']) if pd.notna(r['doi']) else ""



    if doi_val.startswith('10.'):



        doi_part = f", doi: {doi_val}."



    elif doi_val.startswith('http'):



        doi_part = f", ISSN: 2835-8856. [Online]. Available: {doi_val}."



    else:



        doi_part = "."







    cit = f"{r['authors']}, \"{r['title']},\" {r['source_title']}, {r['year']}{doi_part}"



    add_ref(idx + 3, cit)







# Referencias metodológicas de síntesis [134] - [140]



add_ref(134, "J. Thomas and A. Harden, 'Methods for the thematic synthesis of qualitative research in systematic reviews,' BMC Med. Res. Methodol., vol. 8, art. 45, 2008, doi: 10.1186/1471-2288-8-45.")



add_ref(135, "D. S. Cruzes and T. Dybå, 'Research synthesis in software engineering: A tertiary study,' Inf. Softw. Technol., vol. 53, no. 5, pp. 440–455, 2011, doi: 10.1016/j.infsof.2011.01.004.")



add_ref(136, "J. Popay et al., 'Guidance on the conduct of narrative synthesis in systematic reviews,' ESRC Methods Programme, Lancaster Univ., 2006.")



add_ref(137, "M. Campbell et al., 'Synthesis without meta-analysis (SWiM) in systematic reviews: Reporting guideline,' BMJ, vol. 368, p. l6890, 2020, doi: 10.1136/bmj.l6890.")



add_ref(138, "K. Petersen, S. Vakkalanka, and L. Kuzniarz, 'Guidelines for conducting systematic mapping studies in software engineering: An update,' Inf. Softw. Technol., vol. 64, pp. 1–18, 2015, doi: 10.1016/j.infsof.2015.03.007.")



add_ref(139, "N. J. van Eck and L. Waltman, 'Software survey: VOSviewer, a computer program for bibliometric mapping,' Scientometrics, vol. 84, no. 2, pp. 523–538, 2010, doi: 10.1007/s11192-009-0146-3.")



add_ref(140, "S. Lewin et al., 'Applying GRADE-CERQual to qualitative evidence synthesis findings: Introduction to the series,' Implement. Sci., vol. 13, suppl. 1, art. 2, 2018, doi: 10.1186/s13012-017-0688-3.")







out_file = 'project/shared/RSL_Sergio_Rupay.docx'



try:



    doc.save(out_file)



    print(f"\n¡Éxito total! Archivo generado y guardado en: {out_file} ({os.path.getsize(out_file)} bytes)")



except PermissionError:



    alt_out_file = 'project/shared/RSL_Sergio_Rupay_Actualizado.docx'



    doc.save(alt_out_file)



    print(f"AVISO: {out_file} está abierto en Microsoft Word.")



    print(f"¡Éxito total! Archivo generado y guardado en: {alt_out_file} ({os.path.getsize(alt_out_file)} bytes)")



