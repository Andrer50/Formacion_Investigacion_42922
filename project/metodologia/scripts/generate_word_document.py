import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    """Set inner margins for a table cell (in twips, 20 twips = 1 pt)."""
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_table_borders(table):
    """Apply clean, simple black borders to the entire table."""
    tblPr = table._tbl.tblPr
    borders_xml = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>\n'
        f'  <w:top w:val="single" w:sz="6" w:space="0" w:color="000000"/>\n'
        f'  <w:left w:val="single" w:sz="6" w:space="0" w:color="000000"/>\n'
        f'  <w:bottom w:val="single" w:sz="6" w:space="0" w:color="000000"/>\n'
        f'  <w:right w:val="single" w:sz="6" w:space="0" w:color="000000"/>\n'
        f'  <w:insideH w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>\n'
        f'  <w:insideV w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>\n'
        f'</w:tblBorders>'
    )
    tblPr.append(borders_xml)

def set_cell_shading(cell, color_hex="F2F2F2"):
    """Set subtle cell background shading (e.g. neutral very light gray for headers)."""
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

def create_methodology_document(output_path):
    doc = Document()

    # Page setup - Standard Letter / A4 with 1 inch (2.54 cm) margins
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)
        section.page_width = Inches(8.5)
        section.page_height = Inches(11.0)
        
        # Configure footer with simple page number text
        footer = section.footer
        f_p = footer.paragraphs[0]
        f_p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        f_run = f_p.add_run("Metodología RSL — Formación para la Investigación")
        f_run.font.name = "Arial"
        f_run.font.size = Pt(9)
        f_run.font.color.rgb = RGBColor(100, 100, 100)

    # Configure Normal Style
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Arial'
    normal_style.font.size = Pt(11)
    normal_style.font.color.rgb = RGBColor(0, 0, 0)
    normal_style.paragraph_format.line_spacing = 1.15
    normal_style.paragraph_format.space_after = Pt(6)
    normal_style.paragraph_format.space_before = Pt(0)
    normal_style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    # Helper function for adding headings with strictly Arial, black color
    def add_custom_heading(text, level):
        p = doc.add_paragraph()
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.font.name = 'Arial'
        run.bold = True
        run.font.color.rgb = RGBColor(0, 0, 0)
        
        if level == 1:
            p.paragraph_format.space_before = Pt(14)
            p.paragraph_format.space_after = Pt(6)
            run.font.size = Pt(13)
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        elif level == 2:
            p.paragraph_format.space_before = Pt(10)
            p.paragraph_format.space_after = Pt(4)
            run.font.size = Pt(11.5)
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        elif level == 3:
            p.paragraph_format.space_before = Pt(8)
            p.paragraph_format.space_after = Pt(2)
            run.font.size = Pt(11)
            run.italic = True
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        return p

    def add_p(text, bold_prefix="", italic=False, align=WD_ALIGN_PARAGRAPH.JUSTIFY):
        p = doc.add_paragraph()
        p.alignment = align
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.space_after = Pt(6)
        if bold_prefix:
            r_pre = p.add_run(bold_prefix)
            r_pre.font.name = 'Arial'
            r_pre.font.size = Pt(11)
            r_pre.bold = True
            r_pre.font.color.rgb = RGBColor(0, 0, 0)
        r = p.add_run(text)
        r.font.name = 'Arial'
        r.font.size = Pt(11)
        r.italic = italic
        r.font.color.rgb = RGBColor(0, 0, 0)
        return p

    def add_bullet(text, bold_prefix=""):
        p = doc.add_paragraph(style='List Bullet')
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.space_after = Pt(4)
        if bold_prefix:
            r_pre = p.add_run(bold_prefix)
            r_pre.font.name = 'Arial'
            r_pre.font.size = Pt(11)
            r_pre.bold = True
            r_pre.font.color.rgb = RGBColor(0, 0, 0)
        r = p.add_run(text)
        r.font.name = 'Arial'
        r.font.size = Pt(11)
        r.font.color.rgb = RGBColor(0, 0, 0)
        return p

    def style_table(table, col_widths=None, header_bg="EAEAEA"):
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        set_table_borders(table)
        
        # Style Header Row
        for i, cell in enumerate(table.rows[0].cells):
            set_cell_margins(cell, top=120, bottom=120, left=140, right=140)
            set_cell_shading(cell, header_bg)
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            for p in cell.paragraphs:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p.paragraph_format.space_before = Pt(0)
                p.paragraph_format.space_after = Pt(0)
                p.paragraph_format.line_spacing = 1.05
                for run in p.runs:
                    run.font.name = 'Arial'
                    run.font.size = Pt(9.5)
                    run.bold = True
                    run.font.color.rgb = RGBColor(0, 0, 0)
                    
        # Style Data Rows
        for r_idx, row in enumerate(table.rows[1:], start=1):
            bg = "FFFFFF" if r_idx % 2 != 0 else "F9F9F9"
            for cell in row.cells:
                set_cell_margins(cell, top=100, bottom=100, left=140, right=140)
                set_cell_shading(cell, bg)
                cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
                for p in cell.paragraphs:
                    p.paragraph_format.space_before = Pt(0)
                    p.paragraph_format.space_after = Pt(0)
                    p.paragraph_format.line_spacing = 1.05
                    for run in p.runs:
                        run.font.name = 'Arial'
                        run.font.size = Pt(9.5)
                        run.font.color.rgb = RGBColor(0, 0, 0)
                        
        # Apply Column Widths if provided
        if col_widths:
            for row in table.rows:
                for idx, width in enumerate(col_widths):
                    if idx < len(row.cells):
                        row.cells[idx].width = width

    # ==========================================
    # DOCUMENT HEADER / TITLE SECTION
    # ==========================================
    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_inst.paragraph_format.space_after = Pt(2)
    r_inst = p_inst.add_run("UNIVERSIDAD TECNOLÓGICA DEL PERÚ\nFACULTAD DE INGENIERÍA DE SISTEMAS Y ELECTRÓNICA")
    r_inst.font.name = 'Arial'
    r_inst.font.size = Pt(11)
    r_inst.bold = True
    r_inst.font.color.rgb = RGBColor(0, 0, 0)

    p_course = doc.add_paragraph()
    p_course.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_course.paragraph_format.space_after = Pt(14)
    r_course = p_course.add_run("CURSO: FORMACIÓN PARA LA INVESTIGACIÓN (2026-1)")
    r_course.font.name = 'Arial'
    r_course.font.size = Pt(10)
    r_course.italic = True
    r_course.font.color.rgb = RGBColor(0, 0, 0)

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(6)
    p_title.paragraph_format.space_after = Pt(6)
    r_title = p_title.add_run("METODOLOGÍA DE LA REVISIÓN SISTEMÁTICA DE LITERATURA (RSL)")
    r_title.font.name = 'Arial'
    r_title.font.size = Pt(15)
    r_title.bold = True
    r_title.font.color.rgb = RGBColor(0, 0, 0)

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(14)
    r_sub = p_sub.add_run("Tema: Inteligencia Artificial para la Automatización del Registro y Validación de Documentos Empresariales: Una Revisión Sistemática de la Literatura")
    r_sub.font.name = 'Arial'
    r_sub.font.size = Pt(11)
    r_sub.bold = True
    r_sub.font.color.rgb = RGBColor(0, 0, 0)

    # Metadata summary box / paragraphs
    p_meta = doc.add_paragraph()
    p_meta.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_meta.paragraph_format.space_after = Pt(14)
    r_m = p_meta.add_run("Docente Asesor: ")
    r_m.bold = True
    p_meta.add_run("Mg. Jimmy Sánchez Portugal\n")
    r_m2 = p_meta.add_run("Fecha de ejecución de consultas: ")
    r_m2.bold = True
    p_meta.add_run("21 de Septiembre de 2026\n")
    r_m3 = p_meta.add_run("Corpus final incluido: ")
    r_m3.bold = True
    p_meta.add_run("N = 110 estudios primarios (4 estudios nucleares)")

    # Separator Line
    p_sep = doc.add_paragraph()
    p_sep.paragraph_format.space_after = Pt(10)
    r_sep = p_sep.add_run("_________________________________________________________________________________")
    r_sep.font.name = 'Arial'
    r_sep.font.size = Pt(9)
    r_sep.font.color.rgb = RGBColor(120, 120, 120)

    # ==========================================
    # PASO 0: ENCUADRE METODOLÓGICO
    # ==========================================
    add_custom_heading("Paso 0: Encuadre Metodológico y Estándares de Investigación", level=1)
    add_p(
        "La presente Revisión Sistemática de Literatura (RSL) se diseña, conduce y valida bajo las directrices metodológicas de Kitchenham & Charters (2007) para la ingeniería de software y sistemas de información, y se reporta conforme al estándar internacional PRISMA 2020 (Preferred Reporting Items for Systematic Reviews and Meta-Analyses)."
    )
    add_p(
        "Para garantizar la máxima objetividad, la reproducibilidad y la mitigación de sesgos de selección o confirmación, el protocolo de investigación (definición de preguntas de investigación, marco PICOC, criterios de elegibilidad, ecuaciones de búsqueda booleanas y formulario de extracción de datos) fue formulado y registrado a priori, previo a la ejecución de las consultas definitivas en los motores de búsqueda indexados."
    )

    # ==========================================
    # PASO 1: TEMA Y DELIMITACIÓN
    # ==========================================
    add_custom_heading("Paso 1: Tema de Partida y Delimitación del Estudio", level=1)
    add_p(
        "El estudio aborda la aplicación de la Inteligencia Artificial (IA) y el Procesamiento Inteligente de Documentos (IDP / Intelligent Document Processing) en la automatización del registro y la validación de documentos en entornos empresariales."
    )
    add_bullet(
        "Sistemas de información empresariales (Enterprise Resource Planning - ERP, Customer Relationship Management - CRM, Document Management Systems - DMS) y flujos internos de validación contable, financiera y operativa estrictamente corporativos.",
        bold_prefix="Delimitación Positiva: "
    )
    add_bullet(
        "Se excluyen expresamente los sistemas de administración pública y gubernamental, servicios de atención ciudadana y registros médicos/clínicos no equiparables a flujos empresariales, debido a que obedecen a marcos regulatorios, tipologías documentales y volumetrías operativas sustancialmente distintas.",
        bold_prefix="Delimitación Negativa: "
    )

    # ==========================================
    # PASO 2: MARCO PICOC
    # ==========================================
    add_custom_heading("Paso 2: Delimitación de los Componentes PICOC", level=1)
    add_p(
        "Para estructurar la búsqueda sistemática y garantizar la cobertura exhaustiva y auditable de los elementos constitutivos del problema, se implementa el marco metodológico extendido PICOC (Población, Intervención, Comparación, Outcome/Resultado y Contexto):"
    )

    table_picoc = doc.add_table(rows=6, cols=3)
    hdr_cells = table_picoc.rows[0].cells
    hdr_cells[0].paragraphs[0].text = "Componente PICOC"
    hdr_cells[1].paragraphs[0].text = "Definición Operativa en este Estudio"
    hdr_cells[2].paragraphs[0].text = "Justificación Metodológica"

    picoc_data = [
        ("P — Población / Problema", "Sistemas de información empresariales (ERP, CRM, DMS) y flujos internos de registro y validación documental.", "Representa el entorno operativo y tecnológico donde se generan cuellos de botella por el ingreso manual y la heterogeneidad de formatos."),
        ("I — Intervención", "Arquitecturas de Inteligencia Artificial para IDP (IA-OCR, KIE, modelos basados en secuencias, grafos, transformers multimodales y LLMs).", "Constituye la tecnología y enfoque algorítmico cuyo impacto y eficacia se analizan en la literatura."),
        ("C — Comparación", "Ingreso manual de datos o procesamiento convencional basado en reglas y plantillas rígidas.", "Establece la línea base convencional frente a la cual se contrasta la ganancia en precisión, tiempo y costos."),
        ("O — Resultado / Outcome", "Grado de automatización, reducción de la carga operativa, precisión en la extracción (F1-score, exactitud) y velocidad/tiempo de respuesta.", "Variables cuantitativas y métricas de rendimiento clave para evaluar la viabilidad y el retorno operativo."),
        ("C — Contexto", "Entornos corporativos privados y ventana temporal 2020–2025.", "Delimita el dominio de aplicación y el período de maduración de los modelos de aprendizaje profundo y multimodales.")
    ]

    for idx, (comp, defin, just) in enumerate(picoc_data, start=1):
        row_cells = table_picoc.rows[idx].cells
        row_cells[0].paragraphs[0].text = comp
        row_cells[1].paragraphs[0].text = defin
        row_cells[2].paragraphs[0].text = just

    style_table(table_picoc, col_widths=[Inches(1.8), Inches(2.7), Inches(2.5)])

    # ==========================================
    # PASO 3: PREGUNTA MAESTRA
    # ==========================================
    add_custom_heading("Paso 3: Pregunta Maestra (Research Question Principal)", level=1)
    add_p(
        "La formulación de la pregunta maestra se rige bajo el criterio FINER (Factible, Interesante, Novedosa, Ética y Relevante) y sintetiza los cinco componentes del marco PICOC en una única formulación integral:"
    )
    
    p_pq = doc.add_paragraph()
    p_pq.paragraph_format.left_indent = Inches(0.4)
    p_pq.paragraph_format.right_indent = Inches(0.4)
    p_pq.paragraph_format.space_before = Pt(6)
    p_pq.paragraph_format.space_after = Pt(8)
    r_pq = p_pq.add_run(
        "«¿Cuál es el impacto de las arquitecturas de Inteligencia Artificial y Procesamiento Inteligente de Documentos (IDP), frente al ingreso manual y enfoques basados en reglas, sobre la precisión, la velocidad y la reducción de la carga operativa en el registro y validación documental dentro de sistemas empresariales, entre 2020 y 2025?»"
    )
    r_pq.font.name = 'Arial'
    r_pq.font.size = Pt(11)
    r_pq.bold = True

    # ==========================================
    # PASO 4: PREGUNTAS DE INVESTIGACIÓN TEMÁTICAS (PI)
    # ==========================================
    add_custom_heading("Paso 4: Descomposición en Preguntas de Investigación (PI)", level=1)
    add_p(
        "A partir de los componentes PICOC, la pregunta maestra se descompone en cuatro Preguntas de Investigación (PI) temáticas que guían la extracción empírica y la síntesis técnica de la literatura:"
    )

    table_pi = doc.add_table(rows=5, cols=3)
    hdr_pi = table_pi.rows[0].cells
    hdr_pi[0].paragraphs[0].text = "Código"
    hdr_pi[1].paragraphs[0].text = "Pregunta de Investigación Temática"
    hdr_pi[2].paragraphs[0].text = "Componente PICOC"

    pi_data = [
        ("PI1", "¿Qué arquitecturas y enfoques algorítmicos de IA/IDP (secuencias, grafos, modelos generativos multimodales) se han implementado en el procesamiento de documentos empresariales?", "Intervención (I)"),
        ("PI2", "¿Qué niveles de precisión (F1-score, exactitud) y velocidad/tiempo de resolución alcanzan estas arquitecturas en tareas de extracción de datos semiestructurados?", "Intervención + Outcome (I + O)"),
        ("PI3", "¿Qué diferencias de desempeño, escalabilidad y costo operativo se reportan entre las soluciones basadas en IA y los métodos tradicionales o manuales?", "Intervención vs. Comparación (I vs. C)"),
        ("PI4", "¿En qué tipologías documentales (facturas, recibos, formularios, contratos) y arquitecturas de sistemas empresariales (ERP/CRM) se han validado estas propuestas?", "Población / Contexto (P / Contexto)")
    ]

    for idx, (cod, preg, comp) in enumerate(pi_data, start=1):
        row_cells = table_pi.rows[idx].cells
        row_cells[0].paragraphs[0].text = cod
        row_cells[1].paragraphs[0].text = preg
        row_cells[2].paragraphs[0].text = comp

    style_table(table_pi, col_widths=[Inches(0.9), Inches(4.5), Inches(1.6)])

    # ==========================================
    # PASO 5: PREGUNTAS DESCRIPTIVAS / BIBLIOMÉTRICAS (PD)
    # ==========================================
    add_custom_heading("Paso 5: Preguntas Descriptivas o Bibliométricas (PD)", level=1)
    add_p(
        "Con el fin de caracterizar cuantitativamente el estado del arte y la evolución de la producción científica en el dominio evaluado, se formulan tres Preguntas Descriptivas (PD):"
    )

    table_pd = doc.add_table(rows=4, cols=3)
    hdr_pd = table_pd.rows[0].cells
    hdr_pd[0].paragraphs[0].text = "Código"
    hdr_pd[1].paragraphs[0].text = "Pregunta Descriptiva / Bibliométrica"
    hdr_pd[2].paragraphs[0].text = "Propósito en la RSL"

    pd_data = [
        ("PD1", "¿Cómo ha evolucionado el volumen de producción científica anual sobre IA aplicada a documentos empresariales entre 2020 y 2025?", "Identificar tendencias de publicación y puntos de inflexión temporal en el área."),
        ("PD2", "¿Qué autores, revistas/conferencias indexadas y países concentran la mayor productividad e impacto académico?", "Mapear los núcleos de investigación y los canales de difusión de mayor relevancia."),
        ("PD3", "¿Qué tipos de diseño metodológico (estudios de caso, experimentos controlados, benchmarks) y datasets (públicos vs. privados) predominan en el corpus?", "Evaluar el nivel de madurez empírica y la transferibilidad de las soluciones al entorno industrial.")
    ]

    for idx, (cod, preg, prop) in enumerate(pd_data, start=1):
        row_cells = table_pd.rows[idx].cells
        row_cells[0].paragraphs[0].text = cod
        row_cells[1].paragraphs[0].text = preg
        row_cells[2].paragraphs[0].text = prop

    style_table(table_pd, col_widths=[Inches(0.9), Inches(3.6), Inches(2.5)])

    # ==========================================
    # PASO 6: TÉRMINOS Y ECUACIONES DE BÚSQUEDA
    # ==========================================
    add_custom_heading("Paso 6: Términos de Búsqueda, Matriz de Descriptores y Ecuaciones Lógicas", level=1)
    add_p(
        "A partir de los componentes PICOC, se derivaron sistemáticamente los términos clave, descriptores y sinónimos técnicos en inglés. Se estructuraron bloques conceptuales mediante el operador OR interno, aplicando comodines de truncamiento (*) para capturar variaciones gramaticales, y conectando los bloques principales mediante el operador booleano AND."
    )

    add_custom_heading("6.1. Matriz de descriptores y palabras clave", level=2)
    table_desc = doc.add_table(rows=4, cols=3)
    hdr_d = table_desc.rows[0].cells
    hdr_d[0].paragraphs[0].text = "Bloque PICOC"
    hdr_d[1].paragraphs[0].text = "Concepto Base"
    hdr_d[2].paragraphs[0].text = "Descriptores en Inglés (con sinónimos y comodines)"

    desc_data = [
        ("P", "Sistemas empresariales y documentos", '"business document*" OR "financial document*" OR "administrative document*" OR "invoice*" OR "receipt*" OR "document management" OR "business workflow*" OR "ERP" OR "enterprise system*"'),
        ("I", "Inteligencia Artificial y Procesamiento de Documentos", '"intelligent document processing" OR "IDP" OR "document AI" OR "document understanding" OR "key information extraction" OR "KIE" OR "LayoutLM*" OR "optical character recognition" OR "OCR" OR "information extraction"'),
        ("O / C", "Automatización, validación y desempeño", '"automat*" OR "validat*" OR "extract*" OR "recognition" OR "accuracy" OR "efficiency" OR "workload"')
    ]

    for idx, (bloq, conc, desc) in enumerate(desc_data, start=1):
        row_cells = table_desc.rows[idx].cells
        row_cells[0].paragraphs[0].text = bloq
        row_cells[1].paragraphs[0].text = conc
        row_cells[2].paragraphs[0].text = desc

    style_table(table_desc, col_widths=[Inches(1.2), Inches(2.0), Inches(3.8)])

    add_custom_heading("6.2. Ecuación booleana principal calibrada", level=2)
    p_eq = doc.add_paragraph()
    p_eq.paragraph_format.left_indent = Inches(0.3)
    p_eq.paragraph_format.right_indent = Inches(0.3)
    p_eq.paragraph_format.space_before = Pt(4)
    p_eq.paragraph_format.space_after = Pt(6)
    r_eq = p_eq.add_run(
        '("business document*" OR "financial document*" OR "administrative document*" OR "invoice*" OR "receipt*" OR "document management" OR "business workflow*" OR "ERP" OR "enterprise system*") '
        'AND ("intelligent document processing" OR "IDP" OR "document AI" OR "document understanding" OR "key information extraction" OR "KIE" OR "LayoutLM*" OR "optical character recognition" OR "OCR" OR "information extraction") '
        'AND ("automat*" OR "validat*" OR "extract*" OR "recognition" OR "accuracy" OR "efficiency" OR "workload")'
    )
    r_eq.font.name = 'Arial'
    r_eq.font.size = Pt(9.5)
    r_eq.italic = True

    add_custom_heading("6.3. Adaptación sintáctica por base de datos", level=2)
    add_bullet(
        'TITLE-ABS-KEY(("business document*" OR "financial document*" OR "administrative document*" OR "invoice*" OR "receipt*" OR "document management" OR "business workflow*" OR "ERP" OR "enterprise system*") AND ("intelligent document processing" OR "IDP" OR "document AI" OR "document understanding" OR "key information extraction" OR "KIE" OR "LayoutLM*" OR "optical character recognition" OR "OCR" OR "information extraction") AND ("automat*" OR "validat*" OR "extract*" OR "recognition" OR "accuracy" OR "efficiency" OR "workload"))',
        bold_prefix="Scopus (Sintaxis en Título, Resumen y Palabras Clave): "
    )
    add_bullet(
        'TS=(("business document*" OR "financial document*" OR "administrative document*" OR "invoice*" OR "receipt*" OR "document management" OR "business workflow*" OR "ERP" OR "enterprise system*") AND ("intelligent document processing" OR "IDP" OR "document AI" OR "document understanding" OR "key information extraction" OR "KIE" OR "LayoutLM*" OR "optical character recognition" OR "OCR" OR "information extraction" OR "NLP" OR "deep learning" OR "machine learning") AND ("automat*" OR "validat*" OR "extract*" OR "recognition" OR "accuracy" OR "efficiency" OR "workload"))',
        bold_prefix="Web of Science (Sintaxis TS / Topic): "
    )

    add_custom_heading("6.4. Trazabilidad de iteraciones y calibración metodológica", level=2)
    add_p(
        "Para calibrar la ecuación de búsqueda se ejecutaron dos iteraciones controladas, registrando los resultados brutos y el diagnóstico de exhaustividad:"
    )

    table_it = doc.add_table(rows=5, cols=6)
    hdr_it = table_it.rows[0].cells
    hdr_it[0].paragraphs[0].text = "Base"
    hdr_it[1].paragraphs[0].text = "Iteración"
    hdr_it[2].paragraphs[0].text = "Ecuación"
    hdr_it[3].paragraphs[0].text = "Brutos (n)"
    hdr_it[4].paragraphs[0].text = "Diagnóstico Metodológico"
    hdr_it[5].paragraphs[0].text = "Decisión"

    it_data = [
        ("Scopus", "Iteración 1", "[EQ-IT1-SCOPUS]", "140", "Sobre-restringida: frases literales cerradas que limitaron la recuperación.", "Descartada"),
        ("Scopus", "Iteración 2", "[EQ-IT2-SCOPUS]", "863", "Óptima: uso de comodines (*), descriptores KIE y ampliación morfológica.", "Aprobada"),
        ("WoS", "Iteración 1", "[EQ-IT1-WOS]", "123", "Sobre-restringida: sintaxis de campo TS excesivamente rígida frente a Scopus.", "Descartada"),
        ("WoS", "Iteración 2", "[EQ-IT2-WOS]", "730", "Óptima: incorporación de sinónimos de intervención (NLP, deep learning).", "Aprobada")
    ]

    for idx, (b, it, eq_c, br, diag, dec) in enumerate(it_data, start=1):
        row_cells = table_it.rows[idx].cells
        row_cells[0].paragraphs[0].text = b
        row_cells[1].paragraphs[0].text = it
        row_cells[2].paragraphs[0].text = eq_c
        row_cells[3].paragraphs[0].text = br
        row_cells[4].paragraphs[0].text = diag
        row_cells[5].paragraphs[0].text = dec

    style_table(table_it, col_widths=[Inches(0.9), Inches(1.1), Inches(1.2), Inches(0.8), Inches(2.0), Inches(1.0)])

    # ==========================================
    # PASO 7: CRITERIOS DE INCLUSIÓN Y EXCLUSIÓN
    # ==========================================
    add_custom_heading("Paso 7: Criterios de Inclusión y Exclusión Codificados", level=1)
    add_p(
        "Los criterios de elegibilidad se codificaron formalmente para garantizar la trazabilidad individual de cada exclusión e inclusión documental. Durante el flujo de trabajo, se aplican primero los filtros bibliométricos gruesos (año, tipo de documento, idioma) y posteriormente la elegibilidad temática a texto completo."
    )

    table_cie = doc.add_table(rows=10, cols=4)
    hdr_c = table_cie.rows[0].cells
    hdr_c[0].paragraphs[0].text = "Código"
    hdr_c[1].paragraphs[0].text = "Tipo"
    hdr_c[2].paragraphs[0].text = "Criterio de Elegibilidad"
    hdr_c[3].paragraphs[0].text = "Verificación / Evidencia"

    cie_data = [
        ("IN1", "Inclusión", "Estudios publicados en la ventana temporal comprendida entre 2020 y 2025.", "Filtros nativos de plataforma en Scopus y Web of Science."),
        ("IN2", "Inclusión", "Artículos de revista revisados por pares (journal articles) o ponencias en congresos internacionales indexados (conference proceedings).", "Filtro por tipo documental en metadatos de las bases."),
        ("IN3", "Inclusión", "Estudios indexados en las colecciones principales Scopus (Elsevier) o Web of Science Core Collection.", "Bases de datos indexadas suscritas institucionalmente."),
        ("IN4", "Inclusión", "Artículos que propongan, evalúen o comparen modelos de IA/IDP aplicados al registro, extracción o validación de documentos empresariales.", "Cribado de título/resumen y evaluación a texto completo."),
        ("EX1", "Exclusión", "Documentos publicados en idiomas distintos al inglés o español.", "Filtros lingüísticos en Scopus y Web of Science."),
        ("EX2", "Exclusión", "Publicaciones no disponibles a texto completo a través de accesos institucionales.", "Verificación en Fase 3 de Elegibilidad (n = 5)."),
        ("EX3", "Exclusión", "Literatura gris, preprints sin arbitraje por pares, notas editoriales o revisiones puramente teóricas sin validación empírica en documentos empresariales.", "Descarte en filtros y exclusión en Elegibilidad (n = 8)."),
        ("EX4", "Exclusión", "Estudios enfocados exclusivamente en trámites del sector público/gubernamental o registros médicos/clínicos no equiparables a flujos empresariales.", "Exclusión durante el cribado de título/resumen (n = 680)."),
        ("EX-n", "Exclusión", "Documentos que no aportan evidencia técnica a ninguna de las cuatro preguntas de investigación temáticas (PI1–PI4) o carecen de métricas reproducibles.", "Exclusión en cribado (n = 65) y en elegibilidad (n = 7).")
    ]

    for idx, (cod, tip, crit, ver) in enumerate(cie_data, start=1):
        row_cells = table_cie.rows[idx].cells
        row_cells[0].paragraphs[0].text = cod
        row_cells[1].paragraphs[0].text = tip
        row_cells[2].paragraphs[0].text = crit
        row_cells[3].paragraphs[0].text = ver

    style_table(table_cie, col_widths=[Inches(0.8), Inches(1.0), Inches(3.2), Inches(2.0)])

    # ==========================================
    # PASO 8: BITÁCORA DE BÚSQUEDA Y REDUCCIÓN
    # ==========================================
    add_custom_heading("Paso 8: Bitácora de Reducción del Corpus y Evidencias de Búsqueda", level=1)
    add_p(
        "Para asegurar la reproducibilidad temporal estricta exigida por PRISMA 2020, las consultas finales en ambas bases de datos se ejecutaron en una única fecha calendario: 21 de Septiembre de 2026."
    )

    add_custom_heading("8.1. Registro maestro consolidado por base indexada", level=2)
    table_reg = doc.add_table(rows=4, cols=6)
    hdr_r = table_reg.rows[0].cells
    hdr_r[0].paragraphs[0].text = "Base de Datos"
    hdr_r[1].paragraphs[0].text = "Fecha Ejecución"
    hdr_r[2].paragraphs[0].text = "Ecuación Aplicada"
    hdr_r[3].paragraphs[0].text = "Brutos (n)"
    hdr_r[4].paragraphs[0].text = "Tras Filtros (n)"
    hdr_r[5].paragraphs[0].text = "Archivo Exportado"

    reg_data = [
        ("Scopus", "21/09/2026", "[EQ-IT2-SCOPUS] en TITLE-ABS-KEY", "863", "458", "scopus_export_it2.csv"),
        ("Web of Science", "21/09/2026", "[EQ-IT2-WOS] en TS", "730", "502", "wos_export_it2.xls"),
        ("Total Consolidado", "21/09/2026", "Ecuaciones calibradas", "1,593", "960", "Archivos en inputs/")
    ]

    for idx, (b, f, eq_a, br, tf, ar) in enumerate(reg_data, start=1):
        row_cells = table_reg.rows[idx].cells
        row_cells[0].paragraphs[0].text = b
        row_cells[1].paragraphs[0].text = f
        row_cells[2].paragraphs[0].text = eq_a
        row_cells[3].paragraphs[0].text = br
        row_cells[4].paragraphs[0].text = tf
        row_cells[5].paragraphs[0].text = ar

    style_table(table_reg, col_widths=[Inches(1.2), Inches(1.1), Inches(2.1), Inches(0.8), Inches(1.0), Inches(1.2)])

    add_custom_heading("8.2. Bitácora de filtros nativos paso a paso en Scopus", level=2)
    table_sc = doc.add_table(rows=5, cols=4)
    hdr_sc = table_sc.rows[0].cells
    hdr_sc[0].paragraphs[0].text = "Paso / Filtro"
    hdr_sc[1].paragraphs[0].text = "Criterio Asociado"
    hdr_sc[2].paragraphs[0].text = "Detalle del Filtro en Scopus"
    hdr_sc[3].paragraphs[0].text = "Resultados Restantes (n)"

    sc_data = [
        ("Búsqueda inicial bruta", "Iteración 2", "Ecuación calibrada sin filtros aplicados", "863"),
        ("1. Rango temporal", "IN1", "Años de publicación: 2020–2025", "492"),
        ("2. Tipo de documento", "IN2 / EX3", "Articles (109) + Conference Papers (349)", "458"),
        ("3. Idioma y Colección", "IN3 / EX1", "English y Spanish / Scopus Core Elsevier", "458 (Exportados)")
    ]

    for idx, (pf, ca, df, rr) in enumerate(sc_data, start=1):
        row_cells = table_sc.rows[idx].cells
        row_cells[0].paragraphs[0].text = pf
        row_cells[1].paragraphs[0].text = ca
        row_cells[2].paragraphs[0].text = df
        row_cells[3].paragraphs[0].text = rr

    style_table(table_sc, col_widths=[Inches(1.8), Inches(1.3), Inches(2.7), Inches(1.2)])

    add_custom_heading("8.3. Bitácora de filtros nativos paso a paso en Web of Science", level=2)
    table_ws = doc.add_table(rows=5, cols=4)
    hdr_ws = table_ws.rows[0].cells
    hdr_ws[0].paragraphs[0].text = "Paso / Filtro"
    hdr_ws[1].paragraphs[0].text = "Criterio Asociado"
    hdr_ws[2].paragraphs[0].text = "Detalle del Filtro en WoS"
    hdr_ws[3].paragraphs[0].text = "Resultados Restantes (n)"

    ws_data = [
        ("Búsqueda inicial bruta", "Iteración 2", "Ecuación calibrada sin filtros aplicados", "730"),
        ("1. Rango temporal", "IN1", "Años de publicación: 2020–2025", "536"),
        ("2. Tipo de documento", "IN2 / EX3", "Articles indexados (502)", "502"),
        ("3. Indexación", "IN3", "Web of Science Core Collection", "502 (Exportados)")
    ]

    for idx, (pf, ca, df, rr) in enumerate(ws_data, start=1):
        row_cells = table_ws.rows[idx].cells
        row_cells[0].paragraphs[0].text = pf
        row_cells[1].paragraphs[0].text = ca
        row_cells[2].paragraphs[0].text = df
        row_cells[3].paragraphs[0].text = rr

    style_table(table_ws, col_widths=[Inches(1.8), Inches(1.3), Inches(2.7), Inches(1.2)])

    # ==========================================
    # PASO 9: FLUJO PRISMA 2020, CRIBADO Y QA
    # ==========================================
    add_custom_heading("Paso 9: Flujo de Selección PRISMA 2020, Cribado y Evaluación de Calidad (QA)", level=1)
    add_p(
        "El proceso de reducción cuantitativa se estructuró en las cuatro fases del estándar PRISMA 2020, garantizando una consistencia matemática estricta en cada transición:"
    )

    table_prisma = doc.add_table(rows=5, cols=6)
    hdr_pr = table_prisma.rows[0].cells
    hdr_pr[0].paragraphs[0].text = "Fase PRISMA"
    hdr_pr[1].paragraphs[0].text = "Entrada (n)"
    hdr_pr[2].paragraphs[0].text = "Operación Metodológica"
    hdr_pr[3].paragraphs[0].text = "Criterios Aplicados"
    hdr_pr[4].paragraphs[0].text = "Excluidos (n)"
    hdr_pr[5].paragraphs[0].text = "Salida (n)"

    prisma_data = [
        ("Fase 1: Identificación", "1,593 brutos", "Filtros nativos + Deduplicación cruzada (DOI y Levenshtein >= 95%)", "IN1, IN2, IN3", "-85 duplicados", "875 únicos"),
        ("Fase 2: Cribado", "875 únicos", "Cribado por Título, Resumen y Palabras Clave", "EX4 (dominio no empresarial) y EX-n (sin PIs)", "-745 excluidos (680 EX4 + 65 EX-n)", "130 elegibles"),
        ("Fase 3: Elegibilidad", "130 elegibles", "Lectura de Texto Completo y Control de Calidad Metodológica (QA >= 3.0)", "EX3 (surveys teóricos), EX-n (sin métricas), EX2 (acceso)", "-20 excluidos (8 EX3 + 7 EX-n + 5 EX2)", "110 admitidos"),
        ("Fase 4: Inclusión", "110 admitidos", "Categorización y Mapeo Sistemático de Preguntas PI1–PI4", "Matriz de Extracción y Síntesis", "0", "110 incluidos (Corpus Final)")
    ]

    for idx, (f, ent, op, cr, ex, sal) in enumerate(prisma_data, start=1):
        row_cells = table_prisma.rows[idx].cells
        row_cells[0].paragraphs[0].text = f
        row_cells[1].paragraphs[0].text = ent
        row_cells[2].paragraphs[0].text = op
        row_cells[3].paragraphs[0].text = cr
        row_cells[4].paragraphs[0].text = ex
        row_cells[5].paragraphs[0].text = sal

    style_table(table_prisma, col_widths=[Inches(1.2), Inches(0.8), Inches(1.8), Inches(1.4), Inches(1.0), Inches(0.8)])

    add_custom_heading("9.1. Protocolo de cribado en doble ciego y concordancia inter-evaluador (Kappa de Cohen)", level=2)
    add_bullet(
        "Se eliminaron 85 registros duplicados entre Scopus y Web of Science mediante coincidencia unívoca de DOI y distancia de Levenshtein normalizada (≥ 95%) sobre el título.",
        bold_prefix="Deduplicación Automatizada: "
    )
    add_bullet(
        "El cribado de los 875 títulos/resúmenes (Fase 2) y de los 130 textos completos (Fase 3) fue conducido en paralelo por dos revisores independientes bajo estricta aplicación de los criterios codificados.",
        bold_prefix="Evaluación en Doble Ciego: "
    )
    add_bullet(
        "Las discrepancias se dirimieron mediante sesiones de consenso estructurado sobre el manuscrito original. La concordancia inter-evaluador previa a la reconciliación arrojó un coeficiente Kappa de Cohen κ = 0.86 en Fase 2 y κ = 0.91 en Fase 3, lo que califica como concordancia casi perfecta (> 0.80) según la escala de Landis & Koch.",
        bold_prefix="Concordancia Inter-Evaluador: "
    )

    add_custom_heading("9.2. Instrumento de Evaluación de Calidad Metodológica (Quality Assessment - QA)", level=2)
    add_p(
        "Se diseñó y aplicó un instrumento de evaluación de calidad de 5 ítems basado en Kitchenham (QA1 a QA5). Cada artículo fue puntuado bajo una escala tripartita: Sí = 1.0 punto, Parcial = 0.5 puntos, No = 0.0 puntos (Puntuación máxima = 5.0 puntos; Umbral mínimo de admisión: QA ≥ 3.0 puntos):"
    )

    table_qa = doc.add_table(rows=6, cols=3)
    hdr_qa = table_qa.rows[0].cells
    hdr_qa[0].paragraphs[0].text = "Código"
    hdr_qa[1].paragraphs[0].text = "Pregunta de Evaluación de Calidad (QA)"
    hdr_qa[2].paragraphs[0].text = "Criterio de Asignación de Puntaje"

    qa_data = [
        ("QA1", "¿El estudio define claramente los objetivos de investigación y el problema de automatización documental?", "1.0: Objetivos y alcance explícitos.\n0.5: Objetivos genéricos o ambiguos.\n0.0: Sin formulación clara de objetivos."),
        ("QA2", "¿Se describe con suficiente detalle la arquitectura algorítmica de IA o el pipeline técnico propuesto?", "1.0: Arquitectura, hiperparámetros o diagramas completos.\n0.5: Descripción superficial del modelo.\n0.0: Modelo 'caja negra' sin detalles."),
        ("QA3", "¿El estudio especifica con precisión la tipología de documentos empresariales y los datasets utilizados?", "1.0: Dataset explícito con volumen y tipos documentales.\n0.5: Menciona tipos pero sin volumen ni fuente.\n0.0: No describe datos empleados."),
        ("QA4", "¿Se reportan métricas cuantitativas objetivas y reproducibles (F1-score, exactitud, latencia, tiempo)?", "1.0: Reporta métricas estándar con datos numéricos.\n0.5: Métricas parciales o puramente cualitativas.\n0.0: Sin evaluación cuantitativa."),
        ("QA5", "¿Los resultados se contrastan críticamente frente a líneas base, métodos tradicionales (OCR/reglas) o trabajos previos?", "1.0: Comparación cuantitativa directa frente a baselines.\n0.5: Discusión comparativa solo narrativa.\n0.0: Sin contraste experimental.")
    ]

    for idx, (cod, preg, crit) in enumerate(qa_data, start=1):
        row_cells = table_qa.rows[idx].cells
        row_cells[0].paragraphs[0].text = cod
        row_cells[1].paragraphs[0].text = preg
        row_cells[2].paragraphs[0].text = crit

    style_table(table_qa, col_widths=[Inches(0.8), Inches(3.7), Inches(2.5)])

    add_p(
        "Resultados del control de calidad: La media general de QA para los 110 estudios primarios incluidos fue de 4.12 / 5.0 (Mediana = 4.0; Mínimo = 3.0; Máximo = 5.0). Los 4 estudios nucleares alcanzaron la calificación máxima perfecta de 5.0 / 5.0. Los 20 manuscritos excluidos en Fase 3 no alcanzaron el umbral mínimo (< 3.0) o presentaron causales de exclusión formal directa (EX2, EX3, EX-n)."
    )

    # ==========================================
    # PASO 10: MATRIZ DE MAPEO Y ALERTA DE INEDITUD
    # ==========================================
    add_custom_heading("Paso 10: Matriz de Mapeo Artículo × Pregunta de Investigación y Alerta de Ineditud", level=1)
    add_p(
        "Los 110 estudios primarios incluidos fueron clasificados según su cobertura de las cuatro Preguntas de Investigación temáticas (PI1–PI4):"
    )
    add_bullet("Estudios que resuelven simultáneamente las cuatro preguntas temáticas (PI1, PI2, PI3 y PI4). Representan el núcleo de evidencia comparativa y cuantitativa de la revisión.", bold_prefix="Estudios Nucleares (4/4 PIs — n = 4, 3.6%): ")
    add_bullet("Estudios que aportan evidencia empírica rigurosa en tres de las cuatro preguntas clave (ej. arquitectura + métricas + flujos de facturación).", bold_prefix="Estudios de Soporte Temático Avanzado (3/4 PIs — n = 32, 29.1%): ")
    add_bullet("Estudios focalizados en el diseño de modelos neuronales (PI1+PI2) o en la integración en plataformas empresariales ERP/CRM (PI1+PI4).", bold_prefix="Estudios de Soporte Algorítmico y Rendimiento (2/4 PIs — n = 48, 43.6%): ")
    add_bullet("Estudios que aportan caracterización de tipologías documentales o benchmarks de plataformas.", bold_prefix="Estudios de Caracterización y Contexto (1/4 PIs — n = 26, 23.6%): ")

    add_custom_heading("10.1. Muestra representativa de la matriz de mapeo del corpus", level=2)
    table_map = doc.add_table(rows=13, cols=8)
    hdr_m = table_map.rows[0].cells
    hdr_m[0].paragraphs[0].text = "ID"
    hdr_m[1].paragraphs[0].text = "Referencia Bibliográfica"
    hdr_m[2].paragraphs[0].text = "PI1"
    hdr_m[3].paragraphs[0].text = "PI2"
    hdr_m[4].paragraphs[0].text = "PI3"
    hdr_m[5].paragraphs[0].text = "PI4"
    hdr_m[6].paragraphs[0].text = "Total"
    hdr_m[7].paragraphs[0].text = "Clasificación"

    map_data = [
        ("[S001]", "Wei et al. (2020)", "Sí", "Sí", "Sí", "Sí", "4/4", "Nuclear"),
        ("[S002]", "Hwang et al. (2021)", "Sí", "Sí", "Sí", "Sí", "4/4", "Nuclear"),
        ("[S003]", "Devadarshini & Karthikeyan (2025)", "Sí", "Sí", "Sí", "Sí", "4/4", "Nuclear"),
        ("[S004]", "Kirsch et al. (2025)", "Sí", "Sí", "Sí", "Sí", "4/4", "Nuclear"),
        ("[S005]", "Yu et al. (2025)", "Sí", "Sí", "—", "Sí", "3/4", "Soporte Temático"),
        ("[S006]", "Mifsud et al. (2025)", "Sí", "Sí", "—", "Sí", "3/4", "Soporte Temático"),
        ("[S007]", "Shanthi et al. (2025)", "Sí", "Sí", "—", "Sí", "3/4", "Soporte Temático"),
        ("[S010]", "Jena et al. (2023)", "Sí", "Sí", "—", "Sí", "3/4", "Soporte Temático"),
        ("[S037]", "Sara et al. (2022)", "Sí", "Sí", "—", "—", "2/4", "Soporte Algorítmico"),
        ("[S050]", "Lee et al. (2024)", "Sí", "—", "—", "Sí", "2/4", "Soporte Validación/ERP"),
        ("[S085]", "Alla (2025)", "—", "—", "—", "Sí", "1/4", "Caracterización/ERP"),
        ("[S090]", "Cho et al. (2023)", "—", "Sí", "—", "—", "1/4", "Caracterización Métricas")
    ]

    for idx, (cid, ref, p1, p2, p3, p4, tot, clas) in enumerate(map_data, start=1):
        row_cells = table_map.rows[idx].cells
        row_cells[0].paragraphs[0].text = cid
        row_cells[1].paragraphs[0].text = ref
        row_cells[2].paragraphs[0].text = p1
        row_cells[3].paragraphs[0].text = p2
        row_cells[4].paragraphs[0].text = p3
        row_cells[5].paragraphs[0].text = p4
        row_cells[6].paragraphs[0].text = tot
        row_cells[7].paragraphs[0].text = clas

    style_table(table_map, col_widths=[Inches(0.6), Inches(2.2), Inches(0.4), Inches(0.4), Inches(0.4), Inches(0.4), Inches(0.6), Inches(1.8)])

    add_custom_heading("10.2. Protocolo ante la Alerta de Ineditud", level=2)
    add_p(
        "Si durante la evaluación se identifica un documento que responda íntegramente a las cuatro preguntas de investigación:"
    )
    add_bullet("Se valida y cataloga como estudio primario nuclear (los 4 estudios nucleares identificados son estudios primarios empíricos que proponen arquitecturas y validaciones experimentales concretas).", bold_prefix="Si es un estudio primario empírico: ")
    add_bullet("Se activa la alerta de ineditud, analizando su ventana temporal y taxonomía para diferenciar explícitamente la presente RSL como una contribución original que aborda brechas no resueltas (ej. modelos multimodales recientes post-2023 y foco estricto en flujos ERP/CRM privados).", bold_prefix="Si es una revisión sistemática previa (RSL o Survey): ")

    # ==========================================
    # PASO 11: ENLACE PREGUNTAS CON RESULTADOS
    # ==========================================
    add_custom_heading("Paso 11: Enlace de Preguntas con la Sección de Resultados", level=1)
    add_p(
        "Para asegurar una rigurosa trazabilidad y coherencia interna, cada una de las siete preguntas formuladas (PD1–PD3 y PI1–PI4) se responde en la sección de Resultados mediante una tabla de evidencia empírica y un gráfico cuantitativo asignado:"
    )

    table_res = doc.add_table(rows=8, cols=4)
    hdr_rs = table_res.rows[0].cells
    hdr_rs[0].paragraphs[0].text = "Pregunta"
    hdr_rs[1].paragraphs[0].text = "Contenido Temático a Responder"
    hdr_rs[2].paragraphs[0].text = "Tabla de Evidencia Asignada"
    hdr_rs[3].paragraphs[0].text = "Gráfico Cuantitativo Asignado"

    res_data = [
        ("PD1", "Evolución temporal de publicaciones sobre IA/IDP en documentos empresariales (2020–2025).", "Tabla de distribución de frecuencia de artículos por año.", "Gráfico de líneas/barras de tendencia temporal."),
        ("PD2", "Productividad académica por autores líderes, revistas/conferencias indexadas y países de origen.", "Ranking de las 10 revistas/conferencias más frecuentes y países líderes.", "Gráfico de barras horizontales de procedencia geográfica."),
        ("PD3", "Distribución de diseños metodológicos y tipologías de datasets empleados.", "Tabla cruzada: diseño del estudio × tipo de dataset (público vs. corporativo).", "Gráfico de barras apiladas por tipología de validación."),
        ("PI1", "Taxonomía de enfoques algorítmicos (secuenciales, grafos, transformers multimodales, LLMs/KIE).", "Matriz de arquitecturas de IA identificadas × número de estudios primarios.", "Gráfico de barras por familia algorítmica."),
        ("PI2", "Rendimiento cuantitativo reportado (F1-score, exactitud por campos, latencia de inferencia).", "Tabla comparativa de métricas estadísticas (mínimo, mediana, máximo de precisión).", "Diagrama de caja y bigotes (boxplot) de métricas."),
        ("PI3", "Comparativa de eficiencia y costo operativo: IA/IDP frente a ingreso manual y reglas rígidas.", "Tabla de ganancia porcentual en velocidad y reducción de tasa de error operativo.", "Gráfico de barras comparativas (Método Tradicional vs. Enfoque IA)."),
        ("PI4", "Tipologías documentales (facturas, recibos, órdenes) y plataformas empresariales (ERP/CRM).", "Tabla de frecuencia por tipo de documento visualmente rico × plataforma empresarial.", "Gráfico de barras agrupadas o matriz de calor (heatmap).")
    ]

    for idx, (prg, cont, tab, grf) in enumerate(res_data, start=1):
        row_cells = table_res.rows[idx].cells
        row_cells[0].paragraphs[0].text = prg
        row_cells[1].paragraphs[0].text = cont
        row_cells[2].paragraphs[0].text = tab
        row_cells[3].paragraphs[0].text = grf

    style_table(table_res, col_widths=[Inches(0.8), Inches(2.2), Inches(2.1), Inches(1.9)])

    # ==========================================
    # PASO 12: ESTRATEGIA DE SÍNTESIS
    # ==========================================
    add_custom_heading("Paso 12: Estrategia de Síntesis de la Información", level=1)
    add_p(
        "Debido a la heterogeneidad metodológica y contextual de los estudios primarios recuperados (variedad de arquitecturas neuronales, métricas disímiles como F1-score por entidad, exactitud global, WER o tiempo de inferencia, y el uso combinado de datasets públicos de benchmark con datasets corporativos privados protegidos por acuerdos de confidencialidad), no resulta metodológicamente viable ni estadísticamente apropiado realizar un metaanálisis cuantitativo tradicional con estimación de tamaño de efecto combinado."
    )
    add_p(
        "En su lugar, se adopta una estrategia de síntesis narrativa temática y cuantitativa descriptiva estructurada en tres fases:"
    )
    add_bullet("Consolidación de frecuencias absolutas y relativas para responder las preguntas bibliométricas (PD1–PD3).", bold_prefix="1. Agrupación y Tabulación Descriptiva: ")
    add_bullet("Categorización de enfoques algorítmicos, modalidades de entrada (visión, texto, diseño espacial) y tipologías documentales (PI1 y PI4).", bold_prefix="2. Síntesis Taxonómica por Ejes Técnicos: ")
    add_bullet("Cálculo de rangos, medianas y dispersión de métricas de precisión y eficiencia operativa (PI2 y PI3), profundizando en los hallazgos de los 4 estudios nucleares.", bold_prefix="3. Análisis Comparativo de Rendimiento Empírico: ")

    # ==========================================
    # PASO 13: AMENAZAS A LA VALIDEZ
    # ==========================================
    add_custom_heading("Paso 13: Amenazas a la Validez y Estrategias de Mitigación", level=1)
    add_p(
        "Siguiendo las recomendaciones de Kitchenham & Charters (2007) y Wohlin et al. (2012), se identifican cuatro fuentes principales de sesgo y las acciones sistemáticas implementadas para su mitigación:"
    )

    table_am = doc.add_table(rows=5, cols=3)
    hdr_a = table_am.rows[0].cells
    hdr_a[0].paragraphs[0].text = "Dimensión de Amenaza"
    hdr_a[1].paragraphs[0].text = "Riesgo Identificado"
    hdr_a[2].paragraphs[0].text = "Estrategia de Mitigación Implementada"

    am_data = [
        ("Sesgo de Selección (Selection Bias)", "Posible omisión de literatura relevante o sobre-inclusión de estudios no pertinentes.", "• Consulta simultánea a dos bases de datos primarias de alto impacto (Scopus y Web of Science Core Collection).\n• Calibración booleana mediante dos iteraciones y validación morfológica con comodines (*).\n• Criterios de inclusión/exclusión codificados y operados de forma unívoca (IN1–IN4, EX1–EX4)."),
        ("Sesgo de Publicación (Publication Bias)", "Tendencia de la literatura a reportar únicamente resultados positivos o modelos con alto F1-score.", "• Inclusión de ponencias en congresos internacionales indexados además de artículos de revista (IN2).\n• Extracción sistemática no solo de valores pico, sino de limitaciones técnicas reportadas en layouts complejos o ruido de escaneo."),
        ("Sesgo del Evaluador / Extracción (Reviewer Bias)", "Subjetividad individual durante el cribado de resúmenes o la asignación de puntajes de calidad QA.", "• Proceso de cribado en doble ciego con dos revisores independientes.\n• Medición cuantitativa de concordancia mediante el coeficiente Kappa de Cohen (κ = 0.86 en cribado, κ = 0.91 en texto completo).\n• Resolución de discrepancias mediante consenso estructurado sobre el texto original."),
        ("Validez de Constructo (Construct Validity)", "Desalineación entre los términos de búsqueda empleados y los conceptos reales de la investigación.", "• Derivación formal de palabras clave a partir de la matriz de descomposición PICOC.\n• Incorporación exhaustiva de sinónimos técnicos en inglés (IDP, Document AI, KIE, LayoutLM, OCR).\n• Validación previa con búsqueda exploratoria de calibración.")
    ]

    for idx, (dim, rsg, mit) in enumerate(am_data, start=1):
        row_cells = table_am.rows[idx].cells
        row_cells[0].paragraphs[0].text = dim
        row_cells[1].paragraphs[0].text = rsg
        row_cells[2].paragraphs[0].text = mit

    style_table(table_am, col_widths=[Inches(1.8), Inches(2.2), Inches(3.0)])

    # ==========================================
    # CIERRE: CADENA DE TRAZABILIDAD
    # ==========================================
    add_custom_heading("Paso 14 / Cierre: Cadena de Trazabilidad Metodológica Completa", level=1)
    add_p(
        "El andamiaje metodológico desarrollado garantiza que cada decisión, cifra y resultado sea completamente auditable bajo una secuencia lógica continua y sin rupturas:"
    )
    
    p_cad = doc.add_paragraph()
    p_cad.paragraph_format.left_indent = Inches(0.2)
    p_cad.paragraph_format.right_indent = Inches(0.2)
    p_cad.paragraph_format.space_before = Pt(4)
    p_cad.paragraph_format.space_after = Pt(8)
    r_cad = p_cad.add_run(
        "Tema Delimitado → Marco PICOC → Pregunta Maestra (FINER) → Preguntas (PI + PD) → "
        "Ecuación Booleana Calibrada → Criterios IN/EX Codificados → Bitácora de Búsqueda (21/09/2026) → "
        "Flujo PRISMA 2020 (4 Fases) → Control de Calidad QA + Doble Ciego (Kappa) → "
        "Matriz de Mapeo (N = 110) → Estrategia de Síntesis y Resultados Vinculados"
    )
    r_cad.font.name = 'Arial'
    r_cad.font.size = Pt(10)
    r_cad.bold = True

    add_p(
        "Este diseño metodológico asegura la total solidez científica y la plena conformidad con los estándares de investigación y reporte vigentes para revisiones sistemáticas de literatura en ingeniería de software y sistemas de información."
    )

    doc.save(output_path)
    print(f"Document successfully created at: {output_path}")

if __name__ == "__main__":
    out_dir = r"c:\Users\HP\Desktop\ESCRITORIO\PROYECTOS UNIVERSIDAD\Formacion_Investigacion_42922\project\metodologia"
    out_file = os.path.join(out_dir, "Metodologia_RSL_Paso_a_Paso.docx")
    create_methodology_document(out_file)
