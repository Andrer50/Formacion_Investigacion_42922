import os
import docx
from docx import Document
from docx.shared import Inches, Pt, Mm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.enum.section import WD_SECTION_START
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_margins(cell, top=60, bottom=60, left=80, right=80):
    """Set compact inner margins for IEEE table cell (in twips, 20 twips = 1 pt)."""
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_ieee_table_borders(table):
    """
    Apply standard IEEE table borders:
    - Top border: 0.75 pt (sz 8)
    - Bottom border: 0.75 pt (sz 8)
    - Inside horizontal header border: 0.5 pt (sz 4)
    - No vertical borders
    """
    tblPr = table._tbl.tblPr
    borders_xml = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>\n'
        f'  <w:top w:val="single" w:sz="8" w:space="0" w:color="000000"/>\n'
        f'  <w:left w:val="none"/>\n'
        f'  <w:bottom w:val="single" w:sz="8" w:space="0" w:color="000000"/>\n'
        f'  <w:right w:val="none"/>\n'
        f'  <w:insideH w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>\n'
        f'  <w:insideV w:val="none"/>\n'
        f'</w:tblBorders>'
    )
    tblPr.append(borders_xml)

def set_cell_shading(cell, color_hex="F2F2F2"):
    """Set subtle cell background shading."""
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

def configure_section_margins(section, top_mm=19.0, bottom_mm=25.4, left_mm=17.3, right_mm=17.3):
    section.top_margin = Mm(top_mm)
    section.bottom_margin = Mm(bottom_mm)
    section.left_margin = Mm(left_mm)
    section.right_margin = Mm(right_mm)
    section.page_width = Mm(215.9)   # 8.5 inches (US Letter)
    section.page_height = Mm(279.4)  # 11.0 inches (US Letter)
    
    # Remove headers and footers per IEEE spec (III.F)
    header = section.header
    header.is_linked_to_previous = False
    for p in header.paragraphs:
        p.text = ""
    footer = section.footer
    footer.is_linked_to_previous = False
    for p in footer.paragraphs:
        p.text = ""

def set_section_columns(section, num_cols=2, space_twips=240):
    """Configure number of columns and spacing (240 twips = 0.17 in = 4.23 mm)."""
    sectPr = section._sectPr
    cols = sectPr.xpath('./w:cols')
    if cols:
        col = cols[0]
    else:
        col = OxmlElement('w:cols')
        sectPr.append(col)
    col.set(qn('w:num'), str(num_cols))
    col.set(qn('w:space'), str(space_twips))

def generate_ieee_word_document(output_path):
    doc = Document()

    # ==========================================
    # SECTION 1: HEADER / TITLE (1 COLUMN)
    # ==========================================
    sec1 = doc.sections[0]
    configure_section_margins(sec1)
    set_section_columns(sec1, num_cols=1)

    # Configure Normal Style
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Times New Roman'
    normal_style.font.size = Pt(10)
    normal_style.font.color.rgb = RGBColor(0, 0, 0)
    normal_style.paragraph_format.line_spacing = 1.0
    normal_style.paragraph_format.space_before = Pt(0)
    normal_style.paragraph_format.space_after = Pt(0)
    normal_style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    # 1. Institutional Context / Header (Centered)
    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_inst.paragraph_format.space_before = Pt(0)
    p_inst.paragraph_format.space_after = Pt(2)
    r_inst = p_inst.add_run("UNIVERSIDAD TECNOLÓGICA DEL PERÚ\nFACULTAD DE INGENIERÍA DE SISTEMAS Y ELECTRÓNICA")
    r_inst.font.name = 'Times New Roman'
    r_inst.font.size = Pt(10)
    r_inst.bold = True

    # 2. Main Title in IEEE format: 24 pt, Centered, Title Case
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(12)
    p_title.paragraph_format.space_after = Pt(8)
    r_title = p_title.add_run("Metodología de la Revisión Sistemática de Literatura (RSL): Inteligencia Artificial para la Automatización del Registro y Validación de Documentos Empresariales")
    r_title.font.name = 'Times New Roman'
    r_title.font.size = Pt(24)
    r_title.bold = True

    # 3. Authors / Course / Metadata: 11 pt & 9.5 pt, Centered
    p_authors = doc.add_paragraph()
    p_authors.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_authors.paragraph_format.space_before = Pt(4)
    p_authors.paragraph_format.space_after = Pt(2)
    r_auth = p_authors.add_run("Formación para la Investigación (2026-1)")
    r_auth.font.name = 'Times New Roman'
    r_auth.font.size = Pt(11)
    r_auth.bold = True

    p_affil = doc.add_paragraph()
    p_affil.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_affil.paragraph_format.space_before = Pt(0)
    p_affil.paragraph_format.space_after = Pt(14)
    r_aff = p_affil.add_run("Facultad de Ingeniería de Sistemas y Electrónica, Universidad Tecnológica del Perú, Lima, Perú\nDocente Asesor: Jimmy Sánchez Portugal | Fecha de consultas: 21 de septiembre de 2026 | Corpus final: N = 110 estudios primarios (4 estudios nucleares)")
    r_aff.font.name = 'Times New Roman'
    r_aff.font.size = Pt(9.5)
    r_aff.italic = True

    # ==========================================
    # SECTION 2: BODY TEXT (2 COLUMNS)
    # ==========================================
    sec2 = doc.add_section(WD_SECTION_START.CONTINUOUS)
    configure_section_margins(sec2)
    set_section_columns(sec2, num_cols=2, space_twips=240)

    # Helper Functions for Typography
    def add_p(text, bold_prefix="", italic_prefix="", italic_text=False, first_line_indent=Pt(10), space_before=Pt(0), space_after=Pt(0), align=WD_ALIGN_PARAGRAPH.JUSTIFY):
        p = doc.add_paragraph()
        p.alignment = align
        p.paragraph_format.line_spacing = 1.0
        p.paragraph_format.space_before = space_before
        p.paragraph_format.space_after = space_after
        p.paragraph_format.first_line_indent = first_line_indent
        
        if bold_prefix:
            r_b = p.add_run(bold_prefix)
            r_b.font.name = 'Times New Roman'
            r_b.font.size = Pt(10)
            r_b.bold = True
        if italic_prefix:
            r_i = p.add_run(italic_prefix)
            r_i.font.name = 'Times New Roman'
            r_i.font.size = Pt(10)
            r_i.italic = True
        r_t = p.add_run(text)
        r_t.font.name = 'Times New Roman'
        r_t.font.size = Pt(10)
        r_t.italic = italic_text
        return p

    def add_heading_1(text):
        """Level 1 Heading: Roman numeral, centered, uppercase/small caps, 10 pt."""
        p = doc.add_paragraph()
        p.paragraph_format.keep_with_next = True
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.first_line_indent = Pt(0)
        run = p.add_run(text)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(10)
        run.bold = True
        return p

    def add_heading_2(text):
        """Level 2 Heading: Capital letter + period, left-aligned, 10 pt Italic."""
        p = doc.add_paragraph()
        p.paragraph_format.keep_with_next = True
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.first_line_indent = Pt(0)
        run = p.add_run(text)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(10)
        run.italic = True
        return p

    def add_heading_3_inline(title, body_text):
        """Level 3 Heading: Arabic numeral + parenthesis, 10 pt Italic, run-in head."""
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.line_spacing = 1.0
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.first_line_indent = Pt(10)
        
        r_title = p.add_run(title + " ")
        r_title.font.name = 'Times New Roman'
        r_title.font.size = Pt(10)
        r_title.italic = True
        
        r_body = p.add_run(body_text)
        r_body.font.name = 'Times New Roman'
        r_body.font.size = Pt(10)
        return p

    def add_table_title(table_num_str, table_title_str):
        p_num = doc.add_paragraph()
        p_num.paragraph_format.keep_with_next = True
        p_num.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_num.paragraph_format.space_before = Pt(8)
        p_num.paragraph_format.space_after = Pt(1)
        p_num.paragraph_format.first_line_indent = Pt(0)
        r_n = p_num.add_run(table_num_str)
        r_n.font.name = 'Times New Roman'
        r_n.font.size = Pt(8)
        r_n.bold = True

        p_tit = doc.add_paragraph()
        p_tit.paragraph_format.keep_with_next = True
        p_tit.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_tit.paragraph_format.space_before = Pt(0)
        p_tit.paragraph_format.space_after = Pt(4)
        p_tit.paragraph_format.first_line_indent = Pt(0)
        r_t = p_tit.add_run(table_title_str)
        r_t.font.name = 'Times New Roman'
        r_t.font.size = Pt(8)
        r_t.bold = True

    def style_ieee_table(table, col_widths=None, header_bg="F2F2F2"):
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        set_ieee_table_borders(table)
        
        # Style Header Row
        for cell in table.rows[0].cells:
            set_cell_margins(cell, top=60, bottom=60, left=60, right=60)
            set_cell_shading(cell, header_bg)
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            for p in cell.paragraphs:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p.paragraph_format.space_before = Pt(0)
                p.paragraph_format.space_after = Pt(0)
                p.paragraph_format.line_spacing = 1.0
                p.paragraph_format.first_line_indent = Pt(0)
                for run in p.runs:
                    run.font.name = 'Times New Roman'
                    run.font.size = Pt(8)
                    run.bold = True
                    
        # Style Data Rows
        for r_idx, row in enumerate(table.rows[1:], start=1):
            bg = "FFFFFF" if r_idx % 2 != 0 else "FAFAFA"
            for cell in row.cells:
                set_cell_margins(cell, top=40, bottom=40, left=60, right=60)
                set_cell_shading(cell, bg)
                cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
                for p in cell.paragraphs:
                    p.paragraph_format.space_before = Pt(0)
                    p.paragraph_format.space_after = Pt(0)
                    p.paragraph_format.line_spacing = 1.0
                    p.paragraph_format.first_line_indent = Pt(0)
                    for run in p.runs:
                        run.font.name = 'Times New Roman'
                        run.font.size = Pt(8)
                        
        if col_widths:
            for row in table.rows:
                for idx, width in enumerate(col_widths):
                    if idx < len(row.cells):
                        row.cells[idx].width = width

    def add_figure_caption(fig_num_str, fig_text_str):
        p = doc.add_paragraph()
        p.paragraph_format.keep_with_next = False
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(4)
        p.paragraph_format.space_after = Pt(8)
        p.paragraph_format.first_line_indent = Pt(0)
        
        r_n = p.add_run(fig_num_str + " ")
        r_n.font.name = 'Times New Roman'
        r_n.font.size = Pt(8)
        r_n.bold = True
        
        r_t = p.add_run(fig_text_str)
        r_t.font.name = 'Times New Roman'
        r_t.font.size = Pt(8)
        return p

    # ==========================================
    # I. PASO 0: ENCUADRE METODOLÓGICO
    # ==========================================
    add_heading_1("I. PASO 0: ENCUADRE METODOLÓGICO Y ESTÁNDARES DE INVESTIGACIÓN")
    add_p(
        "La presente Revisión Sistemática de Literatura (RSL) se diseña, conduce y valida rigurosamente bajo las directrices metodológicas de Kitchenham & Charters (2007) para la ingeniería de software y sistemas de información, y se reporta conforme al estándar internacional de la declaración PRISMA 2020 (Preferred Reporting Items for Systematic Reviews and Meta-Analyses)."
    )
    add_p(
        "Para garantizar la máxima objetividad, la total reproducibilidad y la mitigación de sesgos de selección o confirmación, el protocolo de investigación (definición de preguntas de investigación, marco PICOC, criterios de elegibilidad, ecuaciones de búsqueda booleanas y formulario de extracción de datos) fue formulado y registrado a priori, previo a la ejecución de las consultas definitivas en los motores de búsqueda indexados."
    )

    # ==========================================
    # II. PASO 1: TEMA DE PARTIDA Y DELIMITACIÓN
    # ==========================================
    add_heading_1("II. PASO 1: TEMA DE PARTIDA Y DELIMITACIÓN DEL ESTUDIO")
    add_p(
        "El estudio aborda la aplicación de la Inteligencia Artificial (IA) y el Procesamiento Inteligente de Documentos (IDP / Intelligent Document Processing) en la automatización del registro y la validación de documentos en entornos empresariales."
    )
    add_heading_3_inline(
        "1) Delimitación Positiva:",
        "Sistemas de información empresariales (Enterprise Resource Planning - ERP, Customer Relationship Management - CRM, Document Management Systems - DMS) y flujos internos de validación contable, financiera y operativa estrictamente corporativos."
    )
    add_heading_3_inline(
        "2) Delimitación Negativa:",
        "Se excluyen expresamente los sistemas de administración pública y gubernamental, servicios de atención ciudadana y registros médicos/clínicos no equiparables a flujos empresariales, debido a que obedecen a marcos regulatorios, tipologías documentales y volumetrías operativas sustancialmente distintas."
    )

    # ==========================================
    # III. PASO 2: COMPONENTES PICOC
    # ==========================================
    add_heading_1("III. PASO 2: DELIMITACIÓN DE LOS COMPONENTES PICOC")
    add_p(
        "Para estructurar la búsqueda sistemática y garantizar la cobertura exhaustiva y auditable de los elementos constitutivos del problema, se implementa el marco metodológico extendido PICOC (Población, Intervención, Comparación, Outcome/Resultado y Contexto), detallado en la Tabla I:"
    )

    add_table_title("TABLA I", "COMPONENTES DEL MARCO PICOC Y DEFINICIÓN OPERATIVA")
    t_picoc = doc.add_table(rows=6, cols=3)
    hdr = t_picoc.rows[0].cells
    hdr[0].paragraphs[0].text = "Componente"
    hdr[1].paragraphs[0].text = "Definición Operativa en este Estudio"
    hdr[2].paragraphs[0].text = "Justificación Metodológica"
    
    picoc_data = [
        ("P — Población / Problema", "Sistemas de información empresariales (ERP, CRM, DMS) y flujos internos de registro y validación documental.", "Representa el entorno operativo y tecnológico donde se generan cuellos de botella por el ingreso manual y la heterogeneidad de formatos."),
        ("I — Intervención", "Arquitecturas de Inteligencia Artificial para IDP (IA-OCR, KIE, modelos basados en secuencias, grafos, transformers multimodales y LLMs).", "Constituye la tecnología y enfoque algorítmico cuyo impacto y eficacia se analizan en la literatura."),
        ("C — Comparación", "Ingreso manual de datos o procesamiento convencional basado en reglas y plantillas rígidas.", "Establece la línea base convencional frente a la cual se contrasta la ganancia en precisión, tiempo y costos."),
        ("O — Resultado / Outcome", "Grado de automatización, reducción de la carga operativa, precisión en la extracción (F1-score, exactitud) y velocidad/tiempo de respuesta.", "Variables cuantitativas y métricas de rendimiento clave para evaluar la viabilidad y el retorno operativo."),
        ("C — Contexto", "Entornos corporativos privados y ventana temporal 2020–2025.", "Delimita el dominio de aplicación y el período de maduración de los modelos de aprendizaje profundo y multimodales.")
    ]
    for idx, (c, d, j) in enumerate(picoc_data, start=1):
        cells = t_picoc.rows[idx].cells
        cells[0].paragraphs[0].text = c
        cells[1].paragraphs[0].text = d
        cells[2].paragraphs[0].text = j
    style_ieee_table(t_picoc, col_widths=[Inches(1.0), Inches(1.3), Inches(1.1)])

    # ==========================================
    # IV. PASO 3: PREGUNTA MAESTRA
    # ==========================================
    add_heading_1("IV. PASO 3: PREGUNTA MAESTRA DE INVESTIGACIÓN")
    add_p(
        "La formulación de la pregunta maestra se rige bajo el criterio FINER (Factible, Interesante, Novedosa, Ética y Relevante) y sintetiza los cinco componentes del marco PICOC en una única formulación integral:"
    )
    add_p(
        "«¿Cuál es el impacto de las arquitecturas de Inteligencia Artificial y Procesamiento Inteligente de Documentos (IDP), frente al ingreso manual y enfoques basados en reglas, sobre la precisión, la velocidad y la reducción de la carga operativa en el registro y validación documental dentro de sistemas empresariales, entre 2020 y 2025?»",
        bold_prefix="",
        italic_text=True
    )

    # ==========================================
    # V. PASO 4: PREGUNTAS DE INVESTIGACIÓN (PI)
    # ==========================================
    add_heading_1("V. PASO 4: DESCOMPOSICIÓN EN PREGUNTAS DE INVESTIGACIÓN (PI)")
    add_p(
        "A partir de los componentes PICOC, la pregunta maestra se descompone en cuatro Preguntas de Investigación (PI) temáticas que guían la extracción empírica y la síntesis técnica de la literatura (ver Tabla II):"
    )

    add_table_title("TABLA II", "PREGUNTAS DE INVESTIGACIÓN TEMÁTICAS (PI)")
    t_pi = doc.add_table(rows=5, cols=3)
    hdr_pi = t_pi.rows[0].cells
    hdr_pi[0].paragraphs[0].text = "Código"
    hdr_pi[1].paragraphs[0].text = "Pregunta de Investigación Temática"
    hdr_pi[2].paragraphs[0].text = "PICOC"

    pi_data = [
        ("PI1", "¿Qué arquitecturas y enfoques algorítmicos de IA/IDP (secuencias, grafos, modelos generativos multimodales) se han implementado en el procesamiento de documentos empresariales?", "Intervención (I)"),
        ("PI2", "¿Qué niveles de precisión (F1-score, exactitud) y velocidad/tiempo de resolución alcanzan estas arquitecturas en tareas de extracción de datos semiestructurados?", "Intervención + Outcome (I + O)"),
        ("PI3", "¿Qué diferencias de desempeño, escalabilidad y costo operativo se reportan entre las soluciones basadas en IA y los métodos tradicionales o manuales?", "Intervención vs. Comparación (I vs. C)"),
        ("PI4", "¿En qué tipologías documentales (facturas, recibos, formularios, contratos) y arquitecturas de sistemas empresariales (ERP/CRM) se han validado estas propuestas?", "Población / Contexto (P / C)")
    ]
    for idx, (cod, preg, comp) in enumerate(pi_data, start=1):
        cells = t_pi.rows[idx].cells
        cells[0].paragraphs[0].text = cod
        cells[1].paragraphs[0].text = preg
        cells[2].paragraphs[0].text = comp
    style_ieee_table(t_pi, col_widths=[Inches(0.4), Inches(2.3), Inches(0.7)])

    # ==========================================
    # VI. PASO 5: PREGUNTAS DESCRIPTIVAS (PD)
    # ==========================================
    add_heading_1("VI. PASO 5: PREGUNTAS DESCRIPTIVAS O BIBLIOMÉTRICAS (PD)")
    add_p(
        "Con el propósito de caracterizar cuantitativamente el estado del arte y la evolución de la producción científica en el dominio evaluado, se formulan tres Preguntas Descriptivas (PD), presentadas en la Tabla III:"
    )

    add_table_title("TABLA III", "PREGUNTAS DESCRIPTIVAS O BIBLIOMÉTRICAS (PD)")
    t_pd = doc.add_table(rows=4, cols=3)
    hdr_pd = t_pd.rows[0].cells
    hdr_pd[0].paragraphs[0].text = "Código"
    hdr_pd[1].paragraphs[0].text = "Pregunta Descriptiva / Bibliométrica"
    hdr_pd[2].paragraphs[0].text = "Propósito en la RSL"

    pd_data = [
        ("PD1", "¿Cómo ha evolucionado el volumen de producción científica anual sobre IA aplicada a documentos empresariales entre 2020 y 2025?", "Identificar tendencias de publicación y puntos de inflexión temporal en el área."),
        ("PD2", "¿Qué autores, revistas/conferencias indexadas y países concentran la mayor productividad e impacto académico?", "Mapear los núcleos de investigación y los canales de difusión de mayor relevancia."),
        ("PD3", "¿Qué tipos de diseño metodológico (estudios de caso, experimentos controlados, benchmarks) y datasets (públicos vs. privados) predominan en el corpus?", "Evaluar el nivel de madurez empírica y la transferibilidad de las soluciones al entorno industrial.")
    ]
    for idx, (cod, preg, prop) in enumerate(pd_data, start=1):
        cells = t_pd.rows[idx].cells
        cells[0].paragraphs[0].text = cod
        cells[1].paragraphs[0].text = preg
        cells[2].paragraphs[0].text = prop
    style_ieee_table(t_pd, col_widths=[Inches(0.4), Inches(1.8), Inches(1.2)])

    # ==========================================
    # VII. PASO 6: TÉRMINOS Y ECUACIONES DE BÚSQUEDA
    # ==========================================
    add_heading_1("VII. PASO 6: TÉRMINOS DE BÚSQUEDA, MATRIZ DE DESCRIPTORES Y ECUACIONES LÓGICAS")
    
    add_heading_2("A. Matriz de Descriptores y Palabras Clave")
    add_p(
        "A partir de los componentes PICOC, se derivaron sistemáticamente los términos clave, descriptores y sinónimos técnicos en inglés. Se estructuraron bloques conceptuales mediante el operador OR interno, aplicando comodines de truncamiento (*) para capturar variaciones gramaticales, y conectando los bloques principales mediante el operador booleano AND (ver Tabla IV)."
    )

    add_table_title("TABLA IV", "MATRIZ DE DESCRIPTORES Y PALABRAS CLAVE")
    t_desc = doc.add_table(rows=4, cols=3)
    hdr_d = t_desc.rows[0].cells
    hdr_d[0].paragraphs[0].text = "Bloque"
    hdr_d[1].paragraphs[0].text = "Concepto Base"
    hdr_d[2].paragraphs[0].text = "Descriptores en Inglés (con sinónimos y comodines)"

    desc_data = [
        ("P", "Sistemas empresariales y documentos", '"business document*" OR "financial document*" OR "administrative document*" OR "invoice*" OR "receipt*" OR "document management" OR "business workflow*" OR "ERP" OR "enterprise system*"'),
        ("I", "Inteligencia Artificial y Procesamiento de Documentos", '"intelligent document processing" OR "IDP" OR "document AI" OR "document understanding" OR "key information extraction" OR "KIE" OR "LayoutLM*" OR "optical character recognition" OR "OCR" OR "information extraction"'),
        ("O / C", "Automatización, validación y desempeño", '"automat*" OR "validat*" OR "extract*" OR "recognition" OR "accuracy" OR "efficiency" OR "workload"')
    ]
    for idx, (bloq, conc, desc_txt) in enumerate(desc_data, start=1):
        cells = t_desc.rows[idx].cells
        cells[0].paragraphs[0].text = bloq
        cells[1].paragraphs[0].text = conc
        cells[2].paragraphs[0].text = desc_txt
    style_ieee_table(t_desc, col_widths=[Inches(0.4), Inches(1.1), Inches(1.9)])

    add_heading_2("B. Ecuación Booleana Principal Calibrada")
    add_p(
        '("business document*" OR "financial document*" OR "administrative document*" OR "invoice*" OR "receipt*" OR "document management" OR "business workflow*" OR "ERP" OR "enterprise system*") AND ("intelligent document processing" OR "IDP" OR "document AI" OR "document understanding" OR "key information extraction" OR "KIE" OR "LayoutLM*" OR "optical character recognition" OR "OCR" OR "information extraction") AND ("automat*" OR "validat*" OR "extract*" OR "recognition" OR "accuracy" OR "efficiency" OR "workload")',
        italic_text=True
    )

    add_heading_2("C. Adaptación Sintáctica por Base de Datos Indexada")
    add_heading_3_inline(
        "1) Sintaxis en Scopus (TITLE-ABS-KEY):",
        'TITLE-ABS-KEY(("business document*" OR "financial document*" OR "administrative document*" OR "invoice*" OR "receipt*" OR "document management" OR "business workflow*" OR "ERP" OR "enterprise system*") AND ("intelligent document processing" OR "IDP" OR "document AI" OR "document understanding" OR "key information extraction" OR "KIE" OR "LayoutLM*" OR "optical character recognition" OR "OCR" OR "information extraction") AND ("automat*" OR "validat*" OR "extract*" OR "recognition" OR "accuracy" OR "efficiency" OR "workload"))'
    )
    add_heading_3_inline(
        "2) Sintaxis en Web of Science (TS / Topic):",
        'TS=(("business document*" OR "financial document*" OR "administrative document*" OR "invoice*" OR "receipt*" OR "document management" OR "business workflow*" OR "ERP" OR "enterprise system*") AND ("intelligent document processing" OR "IDP" OR "document AI" OR "document understanding" OR "key information extraction" OR "KIE" OR "LayoutLM*" OR "optical character recognition" OR "OCR" OR "information extraction" OR "NLP" OR "deep learning" OR "machine learning") AND ("automat*" OR "validat*" OR "extract*" OR "recognition" OR "accuracy" OR "efficiency" OR "workload"))'
    )

    add_heading_2("D. Registro de Ecuaciones Ejecutadas por Iteración")
    add_heading_3_inline(
        "1) [EQ-IT1-SCOPUS] Iteración 1 — Scopus (Exploratoria / Restrictiva):",
        'TITLE-ABS-KEY(("enterprise information systems" OR "document management" OR "business workflows" OR "ERP" OR "invoice processing" OR "receipt processing") AND ("intelligent document processing" OR "IDP" OR "optical character recognition" OR "OCR" OR "information extraction" OR "key information extraction" OR "document AI" OR "LayoutLM") AND ("manual data entry" OR "manual processing" OR "traditional processing" OR "rule-based" OR "automation" OR "workload reduction" OR "efficiency" OR "accuracy"))'
    )
    add_heading_3_inline(
        "2) [EQ-IT2-SCOPUS] Iteración 2 — Scopus (Calibrada Definitiva):",
        'TITLE-ABS-KEY(("business document*" OR "financial document*" OR "administrative document*" OR "invoice*" OR "receipt*" OR "document management" OR "business workflow*" OR "ERP" OR "enterprise system*") AND ("intelligent document processing" OR "IDP" OR "document AI" OR "document understanding" OR "key information extraction" OR "KIE" OR "LayoutLM*" OR "optical character recognition" OR "OCR" OR "information extraction") AND ("automat*" OR "validat*" OR "extract*" OR "recognition" OR "accuracy" OR "efficiency" OR "workload"))'
    )
    add_heading_3_inline(
        "3) [EQ-IT1-WOS] Iteración 1 — Web of Science (Exploratoria / Restrictiva):",
        'TS=(("business document*" OR "financial document*" OR "administrative document*" OR "invoice*" OR "receipt*" OR "document management" OR "business workflow*" OR "ERP" OR "enterprise system*") AND ("intelligent document processing" OR "IDP" OR "document AI" OR "document understanding" OR "key information extraction" OR "KIE" OR "LayoutLM*" OR "optical character recognition" OR "OCR" OR "information extraction") AND ("automat*" OR "validat*" OR "extract*" OR "recognition" OR "accuracy" OR "efficiency" OR "workload"))'
    )
    add_heading_3_inline(
        "4) [EQ-IT2-WOS] Iteración 2 — Web of Science (Calibrada Definitiva):",
        'TS=(("business document*" OR "financial document*" OR "administrative document*" OR "invoice*" OR "receipt*" OR "document management" OR "business workflow*" OR "ERP" OR "enterprise system*") AND ("intelligent document processing" OR "IDP" OR "document AI" OR "document understanding" OR "key information extraction" OR "KIE" OR "LayoutLM*" OR "optical character recognition" OR "OCR" OR "information extraction" OR "NLP" OR "deep learning" OR "machine learning") AND ("automat*" OR "validat*" OR "extract*" OR "recognition" OR "accuracy" OR "efficiency" OR "workload"))'
    )

    add_heading_2("E. Trazabilidad de Iteraciones y Calibración Metodológica")
    add_p(
        "Para calibrar la ecuación de búsqueda se ejecutaron dos iteraciones controladas, registrando los resultados brutos y el diagnóstico de exhaustividad (ver Tabla V):"
    )

    add_table_title("TABLA V", "TRAZABILIDAD DE ITERACIONES Y CALIBRACIÓN DE BÚSQUEDA")
    t_it = doc.add_table(rows=5, cols=6)
    hdr_it = t_it.rows[0].cells
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
        cells = t_it.rows[idx].cells
        cells[0].paragraphs[0].text = b
        cells[1].paragraphs[0].text = it
        cells[2].paragraphs[0].text = eq_c
        cells[3].paragraphs[0].text = br
        cells[4].paragraphs[0].text = diag
        cells[5].paragraphs[0].text = dec
    style_ieee_table(t_it, col_widths=[Inches(0.5), Inches(0.5), Inches(0.7), Inches(0.4), Inches(0.9), Inches(0.4)])

    # ==========================================
    # VIII. PASO 7: CRITERIOS DE INCLUSIÓN Y EXCLUSIÓN
    # ==========================================
    add_heading_1("VIII. PASO 7: CRITERIOS DE INCLUSIÓN Y EXCLUSIÓN CODIFICADOS")
    add_p(
        "Los criterios de elegibilidad se codificaron formalmente para garantizar la trazabilidad individual de cada exclusión e inclusión documental. Durante el flujo de trabajo, se aplican primero los filtros bibliométricos gruesos (año, tipo de documento, idioma) y posteriormente la elegibilidad temática a texto completo (ver Tabla VI)."
    )

    add_table_title("TABLA VI", "CRITERIOS DE INCLUSIÓN Y EXCLUSIÓN CODIFICADOS")
    t_cie = doc.add_table(rows=10, cols=4)
    hdr_c = t_cie.rows[0].cells
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
        cells = t_cie.rows[idx].cells
        cells[0].paragraphs[0].text = cod
        cells[1].paragraphs[0].text = tip
        cells[2].paragraphs[0].text = crit
        cells[3].paragraphs[0].text = ver
    style_ieee_table(t_cie, col_widths=[Inches(0.4), Inches(0.6), Inches(1.5), Inches(0.9)])

    # ==========================================
    # IX. PASO 8: BITÁCORA DE BÚSQUEDA Y REDUCCIÓN
    # ==========================================
    add_heading_1("IX. PASO 8: BITÁCORA DE REDUCCIÓN DEL CORPUS Y EVIDENCIAS DE BÚSQUEDA")
    
    add_heading_2("A. Registro Maestro Consolidado por Base Indexada")
    add_p(
        "Para asegurar la reproducibilidad temporal estricta exigida por PRISMA 2020, las consultas finales en ambas bases de datos se ejecutaron en una única fecha calendario: 21 de septiembre de 2026 (ver Tabla VII)."
    )

    add_table_title("TABLA VII", "REGISTRO MAESTRO CONSOLIDADO POR BASE INDEXADA")
    t_reg = doc.add_table(rows=4, cols=6)
    hdr_r = t_reg.rows[0].cells
    hdr_r[0].paragraphs[0].text = "Base de Datos"
    hdr_r[1].paragraphs[0].text = "Fecha"
    hdr_r[2].paragraphs[0].text = "Ecuación Aplicada"
    hdr_r[3].paragraphs[0].text = "Brutos (n)"
    hdr_r[4].paragraphs[0].text = "Filtros (n)"
    hdr_r[5].paragraphs[0].text = "Archivo Exportado"

    reg_data = [
        ("Scopus", "21/09/2026", "[EQ-IT2-SCOPUS] en TITLE-ABS-KEY", "863", "458", "scopus_export_it2.csv"),
        ("Web of Science", "21/09/2026", "[EQ-IT2-WOS] en TS", "730", "502", "wos_export_it2.xls"),
        ("Total Consolidado", "21/09/2026", "Ecuaciones calibradas", "1,593", "960", "Archivos en inputs/")
    ]
    for idx, (b, f, eq_a, br, tf, ar) in enumerate(reg_data, start=1):
        cells = t_reg.rows[idx].cells
        cells[0].paragraphs[0].text = b
        cells[1].paragraphs[0].text = f
        cells[2].paragraphs[0].text = eq_a
        cells[3].paragraphs[0].text = br
        cells[4].paragraphs[0].text = tf
        cells[5].paragraphs[0].text = ar
    style_ieee_table(t_reg, col_widths=[Inches(0.6), Inches(0.5), Inches(0.9), Inches(0.4), Inches(0.4), Inches(0.6)])

    add_heading_2("B. Bitácora de Filtros Nativos Paso a Paso en Scopus")
    add_p(
        "La secuencia progresiva de reducción en Scopus se detalla en la Tabla VIII:"
    )

    add_table_title("TABLA VIII", "BITÁCORA DE FILTROS NATIVOS EN SCOPUS")
    t_sc = doc.add_table(rows=5, cols=4)
    hdr_sc = t_sc.rows[0].cells
    hdr_sc[0].paragraphs[0].text = "Paso / Filtro"
    hdr_sc[1].paragraphs[0].text = "Criterio"
    hdr_sc[2].paragraphs[0].text = "Detalle del Filtro en Scopus"
    hdr_sc[3].paragraphs[0].text = "Restantes (n)"

    sc_data = [
        ("Búsqueda inicial bruta", "Iteración 2", "Ecuación calibrada sin filtros aplicados", "863"),
        ("1. Rango temporal", "IN1", "Años de publicación: 2020–2025", "492"),
        ("2. Tipo de documento", "IN2 / EX3", "Articles (109) + Conference Papers (349)", "458"),
        ("3. Idioma y Colección", "IN3 / EX1", "English y Spanish / Scopus Core Elsevier", "458 (Exportados)")
    ]
    for idx, (pf, ca, df, rr) in enumerate(sc_data, start=1):
        cells = t_sc.rows[idx].cells
        cells[0].paragraphs[0].text = pf
        cells[1].paragraphs[0].text = ca
        cells[2].paragraphs[0].text = df
        cells[3].paragraphs[0].text = rr
    style_ieee_table(t_sc, col_widths=[Inches(0.9), Inches(0.5), Inches(1.5), Inches(0.5)])

    add_heading_2("C. Bitácora de Filtros Nativos Paso a Paso en Web of Science")
    add_p(
        "La secuencia progresiva de reducción en Web of Science se documenta en la Tabla IX:"
    )

    add_table_title("TABLA IX", "BITÁCORA DE FILTROS NATIVOS EN WEB OF SCIENCE")
    t_ws = doc.add_table(rows=5, cols=4)
    hdr_ws = t_ws.rows[0].cells
    hdr_ws[0].paragraphs[0].text = "Paso / Filtro"
    hdr_ws[1].paragraphs[0].text = "Criterio"
    hdr_ws[2].paragraphs[0].text = "Detalle del Filtro en WoS"
    hdr_ws[3].paragraphs[0].text = "Restantes (n)"

    ws_data = [
        ("Búsqueda inicial bruta", "Iteración 2", "Ecuación calibrada sin filtros aplicados", "730"),
        ("1. Rango temporal", "IN1", "Años de publicación: 2020–2025", "536"),
        ("2. Tipo de documento", "IN2 / EX3", "Articles indexados (502)", "502"),
        ("3. Indexación", "IN3", "Web of Science Core Collection", "502 (Exportados)")
    ]
    for idx, (pf, ca, df, rr) in enumerate(ws_data, start=1):
        cells = t_ws.rows[idx].cells
        cells[0].paragraphs[0].text = pf
        cells[1].paragraphs[0].text = ca
        cells[2].paragraphs[0].text = df
        cells[3].paragraphs[0].text = rr
    style_ieee_table(t_ws, col_widths=[Inches(0.9), Inches(0.5), Inches(1.5), Inches(0.5)])

    # ==========================================
    # X. PASO 9: FLUJO PRISMA 2020, CRIBADO Y QA
    # ==========================================
    add_heading_1("X. PASO 9: FLUJO DE SELECCIÓN PRISMA 2020, CRIBADO Y EVALUACIÓN DE CALIDAD (QA)")
    
    add_heading_2("A. Fases del Flujo de Selección PRISMA 2020")
    add_p(
        "El proceso de reducción cuantitativa se estructuró en las cuatro fases del estándar PRISMA 2020, garantizando una consistencia matemática estricta en cada transición (ver Tabla X y Fig. 1):"
    )

    add_table_title("TABLA X", "CUATRO FASES DEL FLUJO DE SELECCIÓN PRISMA 2020")
    t_prisma = doc.add_table(rows=5, cols=6)
    hdr_pr = t_prisma.rows[0].cells
    hdr_pr[0].paragraphs[0].text = "Fase PRISMA"
    hdr_pr[1].paragraphs[0].text = "Entrada (n)"
    hdr_pr[2].paragraphs[0].text = "Operación Metodológica"
    hdr_pr[3].paragraphs[0].text = "Criterios"
    hdr_pr[4].paragraphs[0].text = "Excluidos (n)"
    hdr_pr[5].paragraphs[0].text = "Salida (n)"

    prisma_data = [
        ("Fase 1: Identificación", "1,593 brutos", "Filtros nativos + Deduplicación cruzada (DOI y Levenshtein >= 95%)", "IN1–IN3", "-85 duplicados", "875 únicos"),
        ("Fase 2: Cribado", "875 únicos", "Cribado por Título, Resumen y Palabras Clave", "EX4 y EX-n", "-745 excluidos (680 EX4 + 65 EX-n)", "130 elegibles"),
        ("Fase 3: Elegibilidad", "130 elegibles", "Lectura de Texto Completo y Evaluación QA (QA >= 3.0)", "EX3, EX-n, EX2", "-20 excluidos (8 EX3 + 7 EX-n + 5 EX2)", "110 admitidos"),
        ("Fase 4: Inclusión", "110 admitidos", "Categorización y Mapeo Sistemático de Preguntas PI1–PI4", "Matriz PI", "0", "110 incluidos (Corpus Final)")
    ]
    for idx, (f, ent, op, cr, ex, sal) in enumerate(prisma_data, start=1):
        cells = t_prisma.rows[idx].cells
        cells[0].paragraphs[0].text = f
        cells[1].paragraphs[0].text = ent
        cells[2].paragraphs[0].text = op
        cells[3].paragraphs[0].text = cr
        cells[4].paragraphs[0].text = ex
        cells[5].paragraphs[0].text = sal
    style_ieee_table(t_prisma, col_widths=[Inches(0.6), Inches(0.5), Inches(0.9), Inches(0.5), Inches(0.5), Inches(0.4)])

    # Add Figure 1 (PRISMA flow chart)
    prisma_img_path = r"c:\Users\HP\Desktop\ESCRITORIO\PROYECTOS UNIVERSIDAD\Formacion_Investigacion_42922\project\metodologia\evidencias\diagrama_flujo_prisma_2020.png"
    if os.path.exists(prisma_img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(6)
        p_img.paragraph_format.space_after = Pt(2)
        p_img.paragraph_format.first_line_indent = Pt(0)
        run_img = p_img.add_run()
        run_img.add_picture(prisma_img_path, width=Inches(3.3))
        add_figure_caption("Fig. 1.", "Flujo de selección y reducción del corpus documental según el estándar PRISMA 2020 (Fases 1 a 4).")

    add_heading_2("B. Protocolo de Cribado en Doble Ciego y Concordancia Inter-Evaluador")
    add_heading_3_inline(
        "1) Deduplicación Automatizada:",
        "Se eliminaron 85 registros duplicados entre Scopus y Web of Science mediante coincidencia unívoca de DOI y distancia de Levenshtein normalizada (≥ 95%) sobre el título."
    )
    add_heading_3_inline(
        "2) Evaluación en Doble Ciego:",
        "El cribado de los 875 títulos/resúmenes (Fase 2) y de los 130 textos completos (Fase 3) fue conducido en paralelo por dos revisores independientes bajo estricta aplicación de los criterios codificados."
    )
    add_heading_3_inline(
        "3) Concordancia Inter-Evaluador (Kappa de Cohen):",
        "Las discrepancias se dirimieron mediante sesiones de consenso estructurado sobre el manuscrito original. La concordancia inter-evaluador previa a la reconciliación arrojó un coeficiente Kappa de Cohen κ = 0.86 en Fase 2 y κ = 0.91 en Fase 3, lo que califica como concordancia casi perfecta (> 0.80) según la escala estándar de Landis & Koch."
    )

    add_heading_2("C. Instrumento de Evaluación de Calidad Metodológica (QA)")
    add_p(
        "Se diseñó y aplicó un instrumento de evaluación de calidad de 5 ítems basado en Kitchenham (QA1 a QA5). Cada artículo fue puntuado bajo una escala tripartita: Sí = 1.0 punto, Parcial = 0.5 puntos, No = 0.0 puntos (Puntuación máxima = 5.0 puntos; Umbral mínimo de admisión: QA ≥ 3.0 puntos), detallado en la Tabla XI:"
    )

    add_table_title("TABLA XI", "INSTRUMENTO DE EVALUACIÓN DE CALIDAD METODOLÓGICA (QA)")
    t_qa = doc.add_table(rows=6, cols=3)
    hdr_qa = t_qa.rows[0].cells
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
        cells = t_qa.rows[idx].cells
        cells[0].paragraphs[0].text = cod
        cells[1].paragraphs[0].text = preg
        cells[2].paragraphs[0].text = crit
    style_ieee_table(t_qa, col_widths=[Inches(0.4), Inches(1.8), Inches(1.2)])

    add_heading_2("D. Resultados del Control de Calidad Metodológica")
    add_p(
        "La media general de QA para los 110 estudios primarios incluidos fue de 4.12 / 5.0 (Mediana = 4.0; Mínimo = 3.0; Máximo = 5.0). Los 4 estudios nucleares alcanzaron la calificación máxima perfecta de 5.0 / 5.0. Los 20 manuscritos excluidos en Fase 3 no alcanzaron el umbral mínimo (< 3.0) o presentaron causales de exclusión formal directa (EX2, EX3, EX-n)."
    )

    # ==========================================
    # XI. PASO 10: MATRIZ DE MAPEO Y ALERTA DE INEDITUD
    # ==========================================
    add_heading_1("XI. PASO 10: MATRIZ DE MAPEO ARTÍCULO × PREGUNTA DE INVESTIGACIÓN Y ALERTA DE INEDITUD")
    
    add_heading_2("A. Clasificación del Corpus Incluido (N = 110)")
    add_p(
        "Los 110 estudios primarios incluidos fueron clasificados según su cobertura de las cuatro Preguntas de Investigación temáticas (PI1–PI4):"
    )
    add_heading_3_inline(
        "1) Estudios Nucleares (4/4 PIs — n = 4, 3.6%):",
        "Estudios que resuelven simultáneamente las cuatro preguntas temáticas (PI1, PI2, PI3 y PI4). Representan el núcleo de evidencia comparativa y cuantitativa de la revisión."
    )
    add_heading_3_inline(
        "2) Estudios de Soporte Temático Avanzado (3/4 PIs — n = 32, 29.1%):",
        "Estudios que aportan evidencia empírica rigurosa en tres de las cuatro preguntas clave (ej. arquitectura + métricas + flujos de facturación)."
    )
    add_heading_3_inline(
        "3) Estudios de Soporte Algorítmico y Rendimiento (2/4 PIs — n = 48, 43.6%):",
        "Estudios focalizados en el diseño de modelos neuronales (PI1+PI2) o en la integración en plataformas empresariales ERP/CRM (PI1+PI4)."
    )
    add_heading_3_inline(
        "4) Estudios de Caracterización y Contexto (1/4 PIs — n = 26, 23.6%):",
        "Estudios que aportan caracterización de tipologías documentales o benchmarks de plataformas."
    )

    add_heading_2("B. Muestra Representativa de la Matriz de Mapeo")
    add_p(
        "La Tabla XII resume la cobertura de las preguntas de investigación para los estudios nucleares y una muestra representativa del corpus:"
    )

    add_table_title("TABLA XII", "MUESTRA REPRESENTATIVA DE LA MATRIZ DE MAPEO DEL CORPUS")
    t_map = doc.add_table(rows=13, cols=8)
    hdr_m = t_map.rows[0].cells
    hdr_m[0].paragraphs[0].text = "ID"
    hdr_m[1].paragraphs[0].text = "Referencia Bibliográfica"
    hdr_m[2].paragraphs[0].text = "PI1"
    hdr_m[3].paragraphs[0].text = "PI2"
    hdr_m[4].paragraphs[0].text = "PI3"
    hdr_m[5].paragraphs[0].text = "PI4"
    hdr_m[6].paragraphs[0].text = "Tot."
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
        ("[S050]", "Lee et al. (2024)", "Sí", "—", "—", "Sí", "2/4", "Soporte ERP/Valid."),
        ("[S085]", "Alla (2025)", "—", "—", "—", "Sí", "1/4", "Caracteriz./ERP"),
        ("[S090]", "Cho et al. (2023)", "—", "Sí", "—", "—", "1/4", "Caracteriz. Métr.")
    ]
    for idx, (cid, ref, p1, p2, p3, p4, tot, clas) in enumerate(map_data, start=1):
        cells = t_map.rows[idx].cells
        cells[0].paragraphs[0].text = cid
        cells[1].paragraphs[0].text = ref
        cells[2].paragraphs[0].text = p1
        cells[3].paragraphs[0].text = p2
        cells[4].paragraphs[0].text = p3
        cells[5].paragraphs[0].text = p4
        cells[6].paragraphs[0].text = tot
        cells[7].paragraphs[0].text = clas
    style_ieee_table(t_map, col_widths=[Inches(0.4), Inches(1.1), Inches(0.2), Inches(0.2), Inches(0.2), Inches(0.2), Inches(0.3), Inches(0.8)])

    add_heading_2("C. Protocolo ante la Alerta de Ineditud")
    add_p(
        "Si durante la evaluación se identifica un documento que responda íntegramente a las cuatro preguntas de investigación:"
    )
    add_heading_3_inline(
        "1) Si es un estudio primario empírico:",
        "Se valida y cataloga como estudio primario nuclear (los 4 estudios nucleares identificados son estudios primarios empíricos que proponen arquitecturas y validaciones experimentales concretas)."
    )
    add_heading_3_inline(
        "2) Si es una revisión sistemática previa (RSL o Survey):",
        "Se activa la alerta de ineditud, analizando su ventana temporal y taxonomía para diferenciar explícitamente la presente RSL como una contribución original que aborda brechas no resueltas (ej. modelos multimodales recientes post-2023 y foco estricto en flujos ERP/CRM privados)."
    )

    # ==========================================
    # XII. PASO 11: ENLACE CON RESULTADOS
    # ==========================================
    add_heading_1("XII. PASO 11: ENLACE DE PREGUNTAS CON LA SECCIÓN DE RESULTADOS")
    add_p(
        "Para asegurar una rigurosa trazabilidad y coherencia interna, cada una de las siete preguntas formuladas (PD1–PD3 y PI1–PI4) se responde en la sección de Resultados mediante una tabla de evidencia empírica y un gráfico cuantitativo asignado (ver Tabla XIII):"
    )

    add_table_title("TABLA XIII", "MATRIZ DE ENLACE ENTRE PREGUNTAS, TABLAS Y GRÁFICOS DE RESULTADOS")
    t_res = doc.add_table(rows=8, cols=4)
    hdr_rs = t_res.rows[0].cells
    hdr_rs[0].paragraphs[0].text = "Pregunta"
    hdr_rs[1].paragraphs[0].text = "Contenido Temático a Responder"
    hdr_rs[2].paragraphs[0].text = "Tabla de Evidencia Asignada"
    hdr_rs[3].paragraphs[0].text = "Gráfico Asignado"

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
        cells = t_res.rows[idx].cells
        cells[0].paragraphs[0].text = prg
        cells[1].paragraphs[0].text = cont
        cells[2].paragraphs[0].text = tab
        cells[3].paragraphs[0].text = grf
    style_ieee_table(t_res, col_widths=[Inches(0.4), Inches(1.1), Inches(1.0), Inches(0.9)])

    # ==========================================
    # XIII. PASO 12: ESTRATEGIA DE SÍNTESIS
    # ==========================================
    add_heading_1("XIII. PASO 12: ESTRATEGIA DE SÍNTESIS DE LA INFORMACIÓN")
    add_p(
        "Debido a la heterogeneidad metodológica y contextual de los estudios primarios recuperados (variedad de arquitecturas neuronales, métricas disímiles como F1-score por entidad, exactitud global, WER o tiempo de inferencia, y el uso combinado de datasets públicos de benchmark con datasets corporativos privados protegidos por acuerdos de confidencialidad), no resulta metodológicamente viable ni estadísticamente apropiado realizar un metaanálisis cuantitativo tradicional con estimación de tamaño de efecto combinado."
    )
    add_p(
        "En su lugar, se adopta una estrategia de síntesis narrativa temática y cuantitativa descriptiva estructurada en tres fases:"
    )
    add_heading_3_inline(
        "1) Agrupación y Tabulación Descriptiva:",
        "Consolidación de frecuencias absolutas y relativas para responder las preguntas bibliométricas (PD1–PD3)."
    )
    add_heading_3_inline(
        "2) Síntesis Taxonómica por Ejes Técnicos:",
        "Categorización de enfoques algorítmicos, modalidades de entrada (visión, texto, diseño espacial) y tipologías documentales (PI1 y PI4)."
    )
    add_heading_3_inline(
        "3) Análisis Comparativo de Rendimiento Empírico:",
        "Cálculo de rangos, medianas y dispersión de métricas de precisión y eficiencia operativa (PI2 y PI3), profundizando en los hallazgos de los 4 estudios nucleares."
    )

    # ==========================================
    # XIV. PASO 13: AMENAZAS A LA VALIDEZ
    # ==========================================
    add_heading_1("XIV. PASO 13: AMENAZAS A LA VALIDEZ Y ESTRATEGIAS DE MITIGACIÓN")
    add_p(
        "Siguiendo las recomendaciones de Kitchenham & Charters (2007) y Wohlin et al. (2012), se identifican cuatro fuentes principales de sesgo y las acciones sistemáticas implementadas para su mitigación (ver Tabla XIV):"
    )

    add_table_title("TABLA XIV", "MATRIZ DE AMENAZAS A LA VALIDEZ Y ESTRATEGIAS DE MITIGACIÓN")
    t_am = doc.add_table(rows=5, cols=3)
    hdr_a = t_am.rows[0].cells
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
        cells = t_am.rows[idx].cells
        cells[0].paragraphs[0].text = dim
        cells[1].paragraphs[0].text = rsg
        cells[2].paragraphs[0].text = mit
    style_ieee_table(t_am, col_widths=[Inches(0.9), Inches(1.0), Inches(1.5)])

    # ==========================================
    # XV. PASO 14: CONCLUSIONES Y TRAZABILIDAD
    # ==========================================
    add_heading_1("XV. PASO 14: CONCLUSIONES Y CADENA DE TRAZABILIDAD METODOLÓGICA")
    
    add_heading_2("A. Análisis Conclusivo de los Estudios Nucleares")
    add_p(
        "Tras haber analizado detalladamente los 4 estudios nucleares identificados ([S001] Wei et al., 2020; [S002] Hwang et al., 2021; [S003] Devadarshini & Karthikeyan, 2025; [S004] Kirsch et al., 2025), se ha identificado que ninguno de ellos por sí solo responde de forma integral a nuestra pregunta maestra de investigación. Cada uno de estos trabajos aborda aspectos específicos y altamente valiosos (por ejemplo, arquitecturas basadas en grafos, modelos de dependencia espacial o pipelines híbridos OCR-deep learning), pero presentan delimitaciones respecto al rango temporal completo, la cobertura multimodelo comparativa o la integración específica en flujos ERP corporativos privados bajo el enfoque global planteado. Por consiguiente, estos 4 estudios primarios serán tomados como núcleo de referencia fundamental y base empírica de contrastación técnica para el desarrollo de la presente RSL."
    )

    add_heading_2("B. Cadena de Trazabilidad Metodológica Completa")
    add_p(
        "El andamiaje metodológico desarrollado garantiza que cada decisión, cifra y resultado sea completamente auditable bajo una secuencia lógica continua y sin rupturas:"
    )
    add_p(
        "Tema Delimitado → Marco PICOC → Pregunta Maestra (FINER) → Preguntas (PI + PD) → Ecuación Booleana Calibrada → Criterios IN/EX Codificados → Bitácora de Búsqueda (21/09/2026) → Flujo PRISMA 2020 (4 Fases) → Control de Calidad QA + Doble Ciego (Kappa) → Matriz de Mapeo (N = 110) → Estrategia de Síntesis y Resultados Vinculados",
        bold_prefix="",
        italic_text=True
    )

    add_heading_2("C. Conformidad y Robustez Metodológica")
    add_p(
        "Este diseño metodológico asegura la total solidez científica y la plena conformidad con los estándares de investigación y reporte vigentes para revisiones sistemáticas de literatura en ingeniería de software y sistemas de información."
    )

    # Save Document
    doc.save(output_path)
    print(f"IEEE Document successfully generated at: {output_path}")

if __name__ == "__main__":
    out_dir = r"c:\Users\HP\Desktop\ESCRITORIO\PROYECTOS UNIVERSIDAD\Formacion_Investigacion_42922\project\metodologia"
    out_file1 = os.path.join(out_dir, "Metodologia_RSL_Paso_a_Paso_IEEE.docx")
    out_file2 = os.path.join(out_dir, "Metodologia_RSL_Formato_IEEE.docx")
    
    generate_ieee_word_document(out_file1)
    try:
        generate_ieee_word_document(out_file2)
    except PermissionError:
        print("Note: Metodologia_RSL_Formato_IEEE.docx is open in Word, generated Metodologia_RSL_Paso_a_Paso_IEEE.docx successfully.")

