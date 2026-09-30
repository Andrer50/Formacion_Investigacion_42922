import os
import pandas as pd
import docx
from docx import Document
from docx.shared import Inches, Pt, Mm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.enum.section import WD_SECTION_START
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_margins(cell, top=50, bottom=50, left=70, right=70):
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

def format_ieee_authors(auth_str):
    if not isinstance(auth_str, str) or not auth_str.strip():
        return "Anon."
    parts = [p.strip() for p in auth_str.split(";") if p.strip()]
    formatted = []
    for p in parts:
        sub = p.split()
        if len(sub) >= 2:
            last = sub[-1]
            if len(last) <= 3 and last.replace(".", "").isalpha():
                initials = last if last.endswith(".") else last + "."
                surname = " ".join(sub[:-1])
                formatted.append(f"{initials} {surname}")
            else:
                formatted.append(p)
        else:
            formatted.append(p)
    if len(formatted) == 1:
        return formatted[0]
    elif len(formatted) == 2:
        return f"{formatted[0]} and {formatted[1]}"
    elif len(formatted) <= 6:
        join_str = ", ".join(formatted[:-1])
        return f"{join_str}, and {formatted[-1]}"
    else:
        return f"{formatted[0]} et al."

def generate_final_rsl_delivery(output_path, csv_path):
    df_corpus = pd.read_csv(csv_path)
    print(f"Loaded {len(df_corpus)} primary studies from {csv_path}")

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

    # 1. Institutional Header (Centered)
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
    r_title = p_title.add_run("Inteligencia Artificial para la Automatización del Registro y Validación de Documentos Empresariales: Una Revisión Sistemática de la Literatura")
    r_title.font.name = 'Times New Roman'
    r_title.font.size = Pt(24)
    r_title.bold = True

    # 3. Authors & Affiliation: 11 pt & 9.5 pt, Centered
    p_authors = doc.add_paragraph()
    p_authors.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_authors.paragraph_format.space_before = Pt(4)
    p_authors.paragraph_format.space_after = Pt(2)
    r_auth = p_authors.add_run("Sergio André Rupay Huancachoque, Rodrigo Eduardo Gallegos Cartagena")
    r_auth.font.name = 'Times New Roman'
    r_auth.font.size = Pt(11)
    r_auth.bold = True

    p_affil = doc.add_paragraph()
    p_affil.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_affil.paragraph_format.space_before = Pt(0)
    p_affil.paragraph_format.space_after = Pt(14)
    r_aff = p_affil.add_run(
        "Facultad de Ingeniería de Sistemas y Electrónica, Universidad Tecnológica del Perú, Lima, Perú\n"
        "Curso: Formación para la Investigación (2026-1) | Docente Asesor: Jimmy Sánchez Portugal\n"
        "Repositorio del Proyecto: https://github.com/Andrer50/Formacion_Investigacion_42922\n"
        "Corpus Maestro Calibrado: N = 110 estudios primarios ([1]–[110]) | Ventana: 2020–2025"
    )
    r_aff.font.name = 'Times New Roman'
    r_aff.font.size = Pt(9.5)
    r_aff.italic = True

    # ==========================================
    # SECTION 2: BODY TEXT (2 COLUMNS)
    # ==========================================
    sec2 = doc.add_section(WD_SECTION_START.CONTINUOUS)
    configure_section_margins(sec2)
    set_section_columns(sec2, num_cols=2, space_twips=240)

    # Typography Helper Functions
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
        p.paragraph_format.space_before = Pt(12)
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
            set_cell_margins(cell, top=50, bottom=50, left=50, right=50)
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
                set_cell_margins(cell, top=35, bottom=35, left=50, right=50)
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

    def add_reference_entry(ref_num, ref_text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.line_spacing = 1.0
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.left_indent = Inches(0.25)
        p.paragraph_format.first_line_indent = Inches(-0.25)
        
        r_num = p.add_run(ref_num + " ")
        r_num.font.name = 'Times New Roman'
        r_num.font.size = Pt(8)
        
        r_t = p.add_run(ref_text)
        r_t.font.name = 'Times New Roman'
        r_t.font.size = Pt(8)
        return p

    # ==========================================
    # I. INTRODUCCIÓN
    # ==========================================
    add_heading_1("I. INTRODUCCIÓN")
    
    add_heading_2("A. Contexto y Estado de la Problemática")
    add_p(
        "En el ámbito empresarial contemporáneo, el procesamiento de grandes volúmenes de datos no estructurados representa un desafío y una oportunidad crítica para la productividad de las organizaciones. Se estima que aproximadamente el 80% de los datos generados internamente en las organizaciones son de carácter no estructurado, tales como imágenes de documentos, correos electrónicos, contratos, facturas y formularios comerciales."
    )
    add_p(
        "El Procesamiento Inteligente de Documentos (IDP) y el Reconocimiento y Análisis de Documentos (DAR) se han constituido como disciplinas esenciales para convertir esta información en datos estructurados legibles e interpretables por computadoras, facilitando su procesamiento automatizado en plataformas transaccionales."
    )
    add_p(
        "Históricamente, la digitalización dependía de herramientas rígidas de Reconocimiento Óptico de Caracteres (OCR) basadas en plantillas estáticas y reglas predefinidas. Con la maduración de las técnicas de aprendizaje profundo (Deep Learning), Procesamiento de Lenguaje Natural (NLP) y Visión por Computadora (CV), los sistemas actuales logran extraer información clave (KIE / Key Information Extraction) interpretando conjuntamente la semántica textual, el diseño visual (layout) y la información espacial en documentos visualmente ricos (VRDs), permitiendo tareas complejas de inducción libres de plantillas fijas."
    )

    add_heading_2("B. Planteamiento del Problema y Brechas Identificadas")
    add_p(
        "A pesar del auge tecnológico, la transición desde entornos académicos hacia arquitecturas de producción industrial presenta tres brechas críticas:"
    )
    add_heading_3_inline(
        "1) Cuellos de Botella Operativos:",
        "Los métodos manuales y las tecnologías OCR tradicionales continúan generando altos costos, latencia y márgenes de error en el registro documental corporativo."
    )
    add_heading_3_inline(
        "2) Limitaciones de Generalización en Benchmarks:",
        "La literatura reporta discrepancias en la generalización de modelos entrenados en datasets públicos controlados (FUNSD, CORD, SROIE) frente a layouts corporativos reales complejos o degradados."
    )
    add_heading_3_inline(
        "3) Desconexión con Sistemas Transaccionales:",
        "Existe un vacío en la integración de la extracción semántica con la lógica de procesos empresariales (ERP, CRM) y mecanismos de validación y explicabilidad requeridos en sectores regulados."
    )

    add_heading_2("C. Motivación y Formulación de la Pregunta Maestra")
    add_p(
        "La motivación fundamental de esta revisión sistemática radica en la acelerada evolución de modelos de IA multimodal y generativa entre 2020 y 2025. Consolidar esta evidencia científica permite identificar con precisión las arquitecturas algorítmicas óptimas para cada tipología documental, facilitando la transferencia tecnológica hacia implementaciones industriales robustas."
    )
    add_p(
        "El objetivo general del estudio se sintetiza en la siguiente pregunta maestra de investigación:"
    )
    add_p(
        "«¿Cuál es el impacto de las arquitecturas de Inteligencia Artificial y Procesamiento Inteligente de Documentos (IDP), frente al ingreso manual y enfoques basados en reglas, sobre la precisión, la velocidad y la reducción de la carga operativa en el registro y validación documental dentro de sistemas empresariales, entre 2020 y 2025?»",
        bold_prefix="",
        italic_text=True
    )

    add_heading_2("D. Estructura del Artículo")
    add_p(
        "El documento se articula en las siguientes secciones: en la Sección II se detalla la metodología sistemática bajo directrices Kitchenham y PRISMA 2020; en la Sección III se expone la taxonomía y caracterización algorítmica; en la Sección IV se analizan las brechas metodológicas y experimentales; y en la Sección V se abordan las implicaciones prácticas y conclusiones."
    )

    # ==========================================
    # II. METODOLOGÍA
    # ==========================================
    add_heading_1("II. METODOLOGÍA DE LA REVISIÓN SISTEMÁTICA")
    
    add_heading_2("A. Encuadre Metodológico y Estándares")
    add_p(
        "La Revisión Sistemática de Literatura (RSL) se diseñó y condujo bajo las directrices metodológicas de Kitchenham & Charters para la ingeniería de software y sistemas de información, reportándose conforme al estándar PRISMA 2020. El protocolo de investigación fue formalizado a priori para garantizar reproducibilidad y mitigación de sesgos."
    )

    add_heading_2("B. Delimitación del Ámbito de Aplicación")
    add_heading_3_inline(
        "1) Delimitación Positiva:",
        "Sistemas de información empresariales (ERP, CRM, DMS) y flujos internos de registro y validación contable, financiera y operativa corporativos privados."
    )
    add_heading_3_inline(
        "2) Delimitación Negativa:",
        "Se excluyen trámites del sector público, servicios de atención ciudadana y registros clínicos, debido a marcos regulatorios y volumetrías operativas disímiles."
    )

    add_heading_2("C. Descomposición mediante el Marco PICOC")
    add_p(
        "Para estructurar la búsqueda sistemática y garantizar cobertura auditable, se implementó el marco PICOC, cuyos componentes, definiciones operativas y justificaciones se detallan en la Tabla I."
    )

    add_table_title("TABLA I", "COMPONENTES DEL MARCO PICOC Y DEFINICIÓN OPERATIVA")
    t_picoc = doc.add_table(rows=6, cols=3)
    hdr = t_picoc.rows[0].cells
    hdr[0].paragraphs[0].text = "Componente"
    hdr[1].paragraphs[0].text = "Definición Operativa en este Estudio"
    hdr[2].paragraphs[0].text = "Justificación Metodológica"
    
    picoc_data = [
        ("P — Población / Problema", "Sistemas de información empresariales (ERP, CRM, DMS) y flujos internos de registro y validación documental.", "Entorno operativo donde se generan cuellos de botella por ingreso manual y formatos heterogéneos."),
        ("I — Intervención", "Arquitecturas de IA para IDP (IA-OCR, KIE, modelos basados en secuencias, grafos, transformers multimodales y LLMs).", "Tecnología y enfoque algorítmico cuyo impacto y eficacia se analizan en la literatura."),
        ("C — Comparación", "Ingreso manual de datos o procesamiento convencional basado en reglas y plantillas rígidas.", "Línea base convencional frente a la cual se contrasta la ganancia en precisión, tiempo y costos."),
        ("O — Resultado / Outcome", "Grado de automatización, reducción de carga operativa, precisión (F1-score, exactitud) y velocidad de respuesta.", "Variables cuantitativas clave para evaluar la viabilidad y el retorno operativo."),
        ("C — Contexto", "Entornos corporativos privados y ventana temporal 2020–2025.", "Delimita el dominio de aplicación y el periodo de maduración de modelos profundos y multimodales.")
    ]
    for idx, (c, d, j) in enumerate(picoc_data, start=1):
        cells = t_picoc.rows[idx].cells
        cells[0].paragraphs[0].text = c
        cells[1].paragraphs[0].text = d
        cells[2].paragraphs[0].text = j
    style_ieee_table(t_picoc, col_widths=[Inches(1.0), Inches(1.3), Inches(1.1)])

    add_heading_2("D. Preguntas de Investigación Temáticas (PI) y Bibliométricas (PD)")
    add_p(
        "A partir del marco PICOC, la investigación se descompone en cuatro Preguntas de Investigación (PI) temáticas orientadas a la evidencia técnica (Tabla II) y tres Preguntas Descriptivas (PD) orientadas a la caracterización bibliométrica del estado del arte (Tabla III)."
    )

    add_table_title("TABLA II", "PREGUNTAS DE INVESTIGACIÓN TEMÁTICAS (PI)")
    t_pi = doc.add_table(rows=5, cols=3)
    hdr_pi = t_pi.rows[0].cells
    hdr_pi[0].paragraphs[0].text = "Código"
    hdr_pi[1].paragraphs[0].text = "Pregunta de Investigación Temática"
    hdr_pi[2].paragraphs[0].text = "PICOC"

    pi_data = [
        ("PI1", "¿Qué arquitecturas y enfoques algorítmicos de IA/IDP (secuencias, grafos, transformers, LLMs) se han implementado en documentos empresariales?", "Intervención (I)"),
        ("PI2", "¿Qué niveles de precisión (F1-score, exactitud) y velocidad/tiempo de resolución alcanzan estas arquitecturas en extracción semiestructurada?", "Intervención + Outcome (I + O)"),
        ("PI3", "¿Qué diferencias de desempeño, escalabilidad y costo operativo se reportan entre soluciones de IA y métodos tradicionales o manuales?", "Intervención vs. Comparación (I vs. C)"),
        ("PI4", "¿En qué tipologías documentales (facturas, recibos, formularios, contratos) y sistemas empresariales (ERP/CRM) se han validado?", "Población / Contexto (P / C)")
    ]
    for idx, (cod, preg, comp) in enumerate(pi_data, start=1):
        cells = t_pi.rows[idx].cells
        cells[0].paragraphs[0].text = cod
        cells[1].paragraphs[0].text = preg
        cells[2].paragraphs[0].text = comp
    style_ieee_table(t_pi, col_widths=[Inches(0.4), Inches(2.3), Inches(0.7)])

    add_table_title("TABLA III", "PREGUNTAS DESCRIPTIVAS O BIBLIOMÉTRICAS (PD)")
    t_pd = doc.add_table(rows=4, cols=3)
    hdr_pd = t_pd.rows[0].cells
    hdr_pd[0].paragraphs[0].text = "Código"
    hdr_pd[1].paragraphs[0].text = "Pregunta Descriptiva / Bibliométrica"
    hdr_pd[2].paragraphs[0].text = "Propósito en la RSL"

    pd_data = [
        ("PD1", "¿Cómo ha evolucionado el volumen de producción científica anual sobre IA en documentos empresariales entre 2020 y 2025?", "Identificar tendencias de publicación y puntos de inflexión temporal."),
        ("PD2", "¿Qué autores, revistas/conferencias indexadas y países concentran la mayor productividad e impacto académico?", "Mapear los núcleos de investigación y canales de difusión líderes."),
        ("PD3", "¿Qué tipos de diseño metodológico (estudios de caso, experimentos, benchmarks) y datasets (públicos vs. privados) predominan?", "Evaluar el nivel de madurez empírica y transferibilidad industrial.")
    ]
    for idx, (cod, preg, prop) in enumerate(pd_data, start=1):
        cells = t_pd.rows[idx].cells
        cells[0].paragraphs[0].text = cod
        cells[1].paragraphs[0].text = preg
        cells[2].paragraphs[0].text = prop
    style_ieee_table(t_pd, col_widths=[Inches(0.4), Inches(1.8), Inches(1.2)])

    add_heading_2("E. Estrategia de Búsqueda y Ecuaciones Booleanas Calibradas")
    add_p(
        "A partir de los componentes PICOC, se derivaron los descriptores técnicos en inglés (Tabla IV). Las ecuaciones adaptadas a la sintaxis nativa de Scopus y Web of Science se presentan a continuación, junto con la bitácora de calibración en dos iteraciones (Tabla V)."
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

    add_heading_3_inline(
        "1) Sintaxis Calibrada en Scopus (TITLE-ABS-KEY):",
        'TITLE-ABS-KEY(("business document*" OR "financial document*" OR "administrative document*" OR "invoice*" OR "receipt*" OR "document management" OR "business workflow*" OR "ERP" OR "enterprise system*") AND ("intelligent document processing" OR "IDP" OR "document AI" OR "document understanding" OR "key information extraction" OR "KIE" OR "LayoutLM*" OR "optical character recognition" OR "OCR" OR "information extraction") AND ("automat*" OR "validat*" OR "extract*" OR "recognition" OR "accuracy" OR "efficiency" OR "workload"))'
    )
    add_heading_3_inline(
        "2) Sintaxis Calibrada en Web of Science (TS / Topic):",
        'TS=(("business document*" OR "financial document*" OR "administrative document*" OR "invoice*" OR "receipt*" OR "document management" OR "business workflow*" OR "ERP" OR "enterprise system*") AND ("intelligent document processing" OR "IDP" OR "document AI" OR "document understanding" OR "key information extraction" OR "KIE" OR "LayoutLM*" OR "optical character recognition" OR "OCR" OR "information extraction" OR "NLP" OR "deep learning" OR "machine learning") AND ("automat*" OR "validat*" OR "extract*" OR "recognition" OR "accuracy" OR "efficiency" OR "workload"))'
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
        ("Scopus", "Iteración 1", "[EQ-IT1-SCOPUS]", "140", "Sobre-restringida: frases literales cerradas limitaron la recuperación.", "Descartada"),
        ("Scopus", "Iteración 2", "[EQ-IT2-SCOPUS]", "863", "Óptima: uso de comodines (*), descriptores KIE y ampliación morfológica.", "Aprobada"),
        ("WoS", "Iteración 1", "[EQ-IT1-WOS]", "123", "Sobre-restringida: sintaxis de campo TS excesivamente rígida.", "Descartada"),
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

    add_heading_2("F. Criterios de Elegibilidad Codificados")
    add_p(
        "Los criterios de inclusión y exclusión codificados formalmente para la selección documental se presentan en la Tabla VI."
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
        ("IN2", "Inclusión", "Artículos de revista revisados por pares o ponencias en congresos internacionales indexados.", "Filtro por tipo documental en metadatos de las bases."),
        ("IN3", "Inclusión", "Estudios indexados en Scopus (Elsevier) o Web of Science Core Collection.", "Bases de datos indexadas suscritas institucionalmente."),
        ("IN4", "Inclusión", "Artículos que propongan, evalúen o comparen modelos de IA/IDP en documentos empresariales.", "Cribado de título/resumen y evaluación a texto completo."),
        ("EX1", "Exclusión", "Documentos publicados en idiomas distintos al inglés o español.", "Filtros lingüísticos en Scopus y Web of Science."),
        ("EX2", "Exclusión", "Publicaciones no disponibles a texto completo institucionalmente.", "Verificación en Fase 3 de Elegibilidad (n = 5)."),
        ("EX3", "Exclusión", "Literatura gris, preprints sin arbitraje, notas editoriales o revisiones puramente teóricas.", "Descarte en filtros y exclusión en Elegibilidad (n = 8)."),
        ("EX4", "Exclusión", "Estudios enfocados en sector público o registros médicos no equiparables a flujos empresariales.", "Exclusión durante cribado de título/resumen (n = 680)."),
        ("EX-n", "Exclusión", "Documentos que no aportan evidencia técnica a PI1–PI4 o carecen de métricas reproducibles.", "Exclusión en cribado (n = 65) y elegibilidad (n = 7).")
    ]
    for idx, (cod, tip, crit, ver) in enumerate(cie_data, start=1):
        cells = t_cie.rows[idx].cells
        cells[0].paragraphs[0].text = cod
        cells[1].paragraphs[0].text = tip
        cells[2].paragraphs[0].text = crit
        cells[3].paragraphs[0].text = ver
    style_ieee_table(t_cie, col_widths=[Inches(0.4), Inches(0.6), Inches(1.5), Inches(0.9)])

    add_heading_2("G. Bitácora de Búsqueda y Reducción en Bases Indexadas")
    add_p(
        "Las consultas definitivas se ejecutaron en fecha única (21 de septiembre de 2026). En la Tabla VII se resume el registro maestro consolidado, mientras que en la Tabla VIII y Tabla IX se documenta la aplicación progresiva de filtros nativos en Scopus y Web of Science, respectivamente."
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

    add_heading_2("H. Flujo de Selección PRISMA 2020 y Control de Calidad Metodológica (QA)")
    add_p(
        "El proceso de reducción cuantitativa se estructuró en las cuatro fases del estándar PRISMA 2020, sintetizado en la Tabla X y visualizado en la Fig. 1. La evaluación de calidad metodológica se ejecutó mediante el instrumento de 5 criterios de la Tabla XI."
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

    add_heading_3_inline(
        "1) Deduplicación y Doble Ciego:",
        "Se eliminaron 85 registros duplicados mediante cotejo de DOI y distancia de Levenshtein normalizada (≥ 95%). El cribado y la lectura a texto completo se condujeron en doble ciego por dos revisores independientes, alcanzando un coeficiente Kappa de Cohen κ = 0.86 en Fase 2 y κ = 0.91 en Fase 3 (concordancia casi perfecta)."
    )
    add_heading_3_inline(
        "2) Control de Calidad Metodológica (QA):",
        "Se evaluaron 5 dimensiones de rigor científico (QA1 a QA5) con puntaje máximo de 5.0 y umbral de corte QA ≥ 3.0 (Tabla XI). La media general para los 110 estudios incluidos fue de 4.12 / 5.0, alcanzando los 4 estudios nucleares ([1]–[4]) la calificación máxima de 5.0 / 5.0."
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

    add_heading_2("I. Matriz de Mapeo del Corpus y Protocolo de Ineditud")
    add_p(
        "Los 110 estudios primarios admitidos se clasificaron según su nivel de cobertura de las cuatro preguntas de investigación temáticas (PI1–PI4). En la Tabla XII se presenta una muestra representativa del mapeo del corpus, destacando los 4 estudios nucleares de cobertura integral ([1]–[4])."
    )

    add_table_title("TABLA XII", "MUESTRA REPRESENTATIVA DE LA MATRIZ DE MAPEO DEL CORPUS")
    t_map = doc.add_table(rows=13, cols=8)
    hdr_m = t_map.rows[0].cells
    hdr_m[0].paragraphs[0].text = "Ref."
    hdr_m[1].paragraphs[0].text = "Referencia / Autores"
    hdr_m[2].paragraphs[0].text = "PI1"
    hdr_m[3].paragraphs[0].text = "PI2"
    hdr_m[4].paragraphs[0].text = "PI3"
    hdr_m[5].paragraphs[0].text = "PI4"
    hdr_m[6].paragraphs[0].text = "Tot."
    hdr_m[7].paragraphs[0].text = "Clasificación"

    map_sample = [
        ("[1]", "M. Wei et al. (2020) [S001]", "Sí", "Sí", "Sí", "Sí", "4/4", "Nuclear"),
        ("[2]", "W. Hwang et al. (2021) [S002]", "Sí", "Sí", "Sí", "Sí", "4/4", "Nuclear"),
        ("[3]", "M. Devadarshini et al. (2025) [S003]", "Sí", "Sí", "Sí", "Sí", "4/4", "Nuclear"),
        ("[4]", "B. Kirsch et al. (2025) [S004]", "Sí", "Sí", "Sí", "Sí", "4/4", "Nuclear"),
        ("[5]", "W. Rong (2025) [S005]", "Sí", "Sí", "—", "Sí", "3/4", "Soporte Temático"),
        ("[6]", "L.-C. Chen et al. (2025) [S006]", "Sí", "Sí", "—", "Sí", "3/4", "Soporte Temático"),
        ("[7]", "J.-M. Yu et al. (2025) [S007]", "Sí", "Sí", "—", "Sí", "3/4", "Soporte Temático"),
        ("[12]", "S. Jena et al. (2023) [S012]", "Sí", "Sí", "—", "Sí", "3/4", "Soporte Temático"),
        ("[37]", "P. Sara et al. (2022) [S037]", "Sí", "Sí", "—", "—", "2/4", "Soporte Algorítmico"),
        ("[50]", "H. Lee et al. (2024) [S050]", "Sí", "—", "—", "Sí", "2/4", "Soporte ERP/Valid."),
        ("[85]", "K. Alla (2025) [S085]", "—", "—", "—", "Sí", "1/4", "Caracteriz./ERP"),
        ("[90]", "Y. Cho et al. (2023) [S090]", "—", "Sí", "—", "—", "1/4", "Caracteriz. Métr.")
    ]
    for idx, (cid, ref, p1, p2, p3, p4, tot, clas) in enumerate(map_sample, start=1):
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

    add_heading_2("J. Vinculación con Resultados y Estrategia de Síntesis")
    add_p(
        "Cada una de las preguntas formuladas (PD1–PD3 y PI1–PI4) se vincula unívocamente a una tabla de evidencia y un gráfico asignado en los resultados, según se especifica en la Tabla XIII. Se adoptó una estrategia de síntesis narrativa temática y cuantitativa descriptiva en tres fases debido a la heterogeneidad de datasets y métricas reportadas."
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

    add_heading_2("K. Amenazas a la Validez y Estrategias de Mitigación")
    add_p(
        "Se identificaron y mitigaron cuatro fuentes principales de sesgo metodológico (selección, publicación, evaluador y constructo), cuyas estrategias se detallan en la Tabla XIV."
    )

    add_table_title("TABLA XIV", "MATRIZ DE AMENAZAS A LA VALIDEZ Y ESTRATEGIAS DE MITIGACIÓN")
    t_am = doc.add_table(rows=5, cols=3)
    hdr_a = t_am.rows[0].cells
    hdr_a[0].paragraphs[0].text = "Dimensión de Amenaza"
    hdr_a[1].paragraphs[0].text = "Riesgo Identificado"
    hdr_a[2].paragraphs[0].text = "Estrategia de Mitigación Implementada"

    am_data = [
        ("Sesgo de Selección (Selection Bias)", "Posible omisión de literatura relevante o sobre-inclusión de estudios no pertinentes.", "• Consulta simultánea a dos bases primarias de alto impacto (Scopus y Web of Science Core Collection).\n• Calibración booleana mediante dos iteraciones y validación morfológica con comodines (*).\n• Criterios de inclusión/exclusión codificados y operados unívocamente (IN1–IN4, EX1–EX4)."),
        ("Sesgo de Publicación (Publication Bias)", "Tendencia a reportar únicamente resultados positivos o modelos con alto F1-score.", "• Inclusión de ponencias en congresos internacionales indexados además de artículos de revista (IN2).\n• Extracción sistemática no solo de valores pico, sino de limitaciones en layouts complejos o ruido."),
        ("Sesgo del Evaluador / Extracción (Reviewer Bias)", "Subjetividad individual durante el cribado de resúmenes o la asignación de puntajes QA.", "• Proceso de cribado en doble ciego con dos revisores independientes.\n• Medición cuantitativa de concordancia mediante Kappa de Cohen (κ = 0.86 en cribado, κ = 0.91 en texto completo).\n• Resolución de discrepancias mediante consenso estructurado sobre el texto original."),
        ("Validez de Constructo (Construct Validity)", "Desalineación entre los términos de búsqueda empleados y los conceptos reales de la investigación.", "• Derivación formal de palabras clave a partir de la matriz de descomposición PICOC.\n• Incorporación exhaustiva de sinónimos técnicos en inglés (IDP, Document AI, KIE, LayoutLM, OCR).\n• Validación previa con búsqueda exploratoria de calibración.")
    ]
    for idx, (dim, rsg, mit) in enumerate(am_data, start=1):
        cells = t_am.rows[idx].cells
        cells[0].paragraphs[0].text = dim
        cells[1].paragraphs[0].text = rsg
        cells[2].paragraphs[0].text = mit
    style_ieee_table(t_am, col_widths=[Inches(0.9), Inches(1.0), Inches(1.5)])

    add_heading_2("L. Conclusiones Metodológicas y Cadena de Trazabilidad")
    add_p(
        "Tras haber analizado detalladamente los 4 estudios nucleares identificados ([1]–[4]), se ha determinado que ninguno de ellos por sí solo responde de forma integral a la pregunta maestra de investigación. Cada uno de estos trabajos aborda aspectos específicos y altamente valiosos (por ejemplo, arquitecturas basadas en grafos, modelos de dependencia espacial o pipelines híbridos OCR-deep learning), pero presentan delimitaciones respecto al rango temporal completo, la cobertura multimodelo comparativa o la integración específica en flujos ERP corporativos privados bajo el enfoque global planteado. Por consiguiente, estos 4 estudios primarios son tomados como núcleo de referencia fundamental y base empírica de contrastación técnica para el desarrollo y discusión de la presente RSL."
    )
    add_p(
        "El andamiaje metodológico desarrollado garantiza que cada decisión, cifra y resultado sea completamente auditable bajo una secuencia lógica continua y sin rupturas:"
    )
    add_p(
        "Tema Delimitado → Marco PICOC → Pregunta Maestra (FINER) → Preguntas (PI + PD) → Ecuación Booleana Calibrada → Criterios IN/EX Codificados → Bitácora de Búsqueda (21/09/2026) → Flujo PRISMA 2020 (4 Fases) → Control de Calidad QA + Doble Ciego (Kappa) → Matriz de Mapeo (N = 110) → Estrategia de Síntesis y Resultados Vinculados",
        bold_prefix="",
        italic_text=True
    )
    add_p(
        "Este diseño metodológico asegura la total solidez científica y la plena conformidad con los estándares de investigación y reporte vigentes para revisiones sistemáticas de literatura en ingeniería de software y sistemas de información."
    )

    # ==========================================
    # REFERENCIAS (All 110 corpus studies in IEEE format)
    # ==========================================
    p_ref_h = doc.add_paragraph()
    p_ref_h.paragraph_format.keep_with_next = True
    p_ref_h.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_ref_h.paragraph_format.space_before = Pt(14)
    p_ref_h.paragraph_format.space_after = Pt(6)
    p_ref_h.paragraph_format.first_line_indent = Pt(0)
    r_ref_h = p_ref_h.add_run("REFERENCIAS")
    r_ref_h.font.name = 'Times New Roman'
    r_ref_h.font.size = Pt(10)
    r_ref_h.bold = True

    for i, r in df_corpus.iterrows():
        ref_num = f"[{i+1}]"
        auth = format_ieee_authors(r['authors'])
        title = str(r['title']).strip()
        source = str(r['source_title']).strip()
        year = str(r['year']).strip()
        doi = str(r['doi']).strip()
        doi_str = f", doi: {doi}" if doi and doi.lower() != "nan" else ""
        ref_text = f'{auth}, "{title}," {source}, {year}{doi_str}.'
        add_reference_entry(ref_num, ref_text)

    # Save Document
    doc.save(output_path)
    print(f"Final Combined IEEE Article successfully generated at: {output_path}")

if __name__ == "__main__":
    out_dir = r"c:\Users\HP\Desktop\ESCRITORIO\PROYECTOS UNIVERSIDAD\Formacion_Investigacion_42922\project"
    out_file = os.path.join(out_dir, "Articulo_RSL_Introduccion_y_Metodologia_IEEE.docx")
    csv_file = os.path.join(out_dir, "metodologia", "outputs", "corpus_included_final.csv")
    generate_final_rsl_delivery(out_file, csv_file)
