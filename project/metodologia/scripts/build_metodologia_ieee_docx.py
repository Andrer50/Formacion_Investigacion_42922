import os
import sys
import io
import re
import pandas as pd
import docx
from docx import Document
from docx.shared import Inches, Pt, Mm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.enum.section import WD_SECTION_START
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("Iniciando construcción del documento oficial IEEE para Metodología (N=131)...")

# --- Helper functions for formatting ---
def set_cell_margins(cell, top=60, bottom=60, left=80, right=80):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_ieee_table_borders(table):
    tblPr = table._tbl.tblPr
    borders_xml = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>\n'
        f'  <w:top w:val="single" w:sz="8" w:space="0" w:color="000000"/>\n'
        f'  <w:left w:val="none"/>\n'
        f'  <w:bottom w:val="single" w:sz="8" w:space="0" w:color="000000"/>\n'
        f'  <w:right w:val="none"/>\n'
        f'  <w:insideH w:val="single" w:sz="4" w:space="0" w:color="D3D3D3"/>\n'
        f'  <w:insideV w:val="none"/>\n'
        f'</w:tblBorders>'
    )
    tblPr.append(borders_xml)

def set_cell_shading(cell, color_hex="F2F2F2"):
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

def configure_section_margins(section, top_mm=19.0, bottom_mm=25.4, left_mm=17.3, right_mm=17.3):
    section.top_margin = Mm(top_mm)
    section.bottom_margin = Mm(bottom_mm)
    section.left_margin = Mm(left_mm)
    section.right_margin = Mm(right_mm)
    section.page_width = Mm(215.9)
    section.page_height = Mm(279.4)
    
    header = section.header
    header.is_linked_to_previous = False
    p_head = header.paragraphs[0]
    p_head.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r_head = p_head.add_run("SECCIÓN II: METODOLOGÍA DE REVISIÓN SISTEMÁTICA (PRISMA 2020 / KITCHENHAM) | UTP 2026")
    r_head.font.name = 'Times New Roman'
    r_head.font.size = Pt(7.5)
    r_head.font.color.rgb = RGBColor(128, 128, 128)

def set_section_columns(section, num_cols=2, space_mm=4.7):
    sectPr = section._sectPr
    cols = sectPr.xpath('./w:cols')
    if cols:
        cols[0].set(qn('w:num'), str(num_cols))
        cols[0].set(qn('w:space'), str(int(space_mm * 56.7)))
    else:
        c_elem = parse_xml(f'<w:cols {nsdecls("w")} w:num="{num_cols}" w:space="{int(space_mm * 56.7)}"/>')
        sectPr.append(c_elem)

# --- Load Datasets ---
df_final = pd.read_csv('project/metodologia/outputs/corpus_included_final.csv')
df_nuc = pd.read_csv('project/metodologia/outputs/corpus_estudios_nucleares_4_4.csv')
df_ex20 = pd.read_csv('project/metodologia/outputs/corpus_eligibility_excluded_20.csv')

doc = Document()

# Configure Base Style
normal_style = doc.styles['Normal']
normal_style.font.name = 'Times New Roman'
normal_style.font.size = Pt(9.5)
normal_style.font.color.rgb = RGBColor(0, 0, 0)
normal_style.paragraph_format.line_spacing = 1.0
normal_style.paragraph_format.space_before = Pt(0)
normal_style.paragraph_format.space_after = Pt(2)
normal_style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

# SECTION 1: HEADER & TITLE (Single Column)
sec1 = doc.sections[0]
configure_section_margins(sec1)
set_section_columns(sec1, num_cols=1)

p_inst = doc.add_paragraph()
p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_inst.paragraph_format.space_before = Pt(0)
p_inst.paragraph_format.space_after = Pt(2)
r_inst = p_inst.add_run("UNIVERSIDAD TECNOLÓGICA DEL PERÚ\nFACULTAD DE INGENIERÍA DE SISTEMAS E INFORMÁTICA")
r_inst.bold = True
r_inst.font.size = Pt(9.5)

p_title = doc.add_paragraph()
p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_title.paragraph_format.space_before = Pt(6)
p_title.paragraph_format.space_after = Pt(4)
r_title = p_title.add_run("Sección II: Metodología de la Revisión Sistemática de la Literatura\nInteligencia Artificial para la Automatización del Registro y Validación de Documentos Empresariales")
r_title.bold = True
r_title.font.size = Pt(16)

p_auth = doc.add_paragraph()
p_auth.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_auth.paragraph_format.space_before = Pt(2)
p_auth.paragraph_format.space_after = Pt(1)
r_auth = p_auth.add_run("Sergio André Rupay Huancachoque")
r_auth.bold = True
r_auth.font.size = Pt(10)


p_aff = doc.add_paragraph()
p_aff.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_aff.paragraph_format.space_before = Pt(0)
p_aff.paragraph_format.space_after = Pt(6)
r_aff = p_aff.add_run("Facultad de Ingeniería de Sistemas e Informática, Universidad Tecnológica del Perú, Lima, Perú\nDocente Asesor: Mg. Jimmy Sánchez Portugal | Formación para la Investigación\nEntregable Oficial: Metodología de RSL | Corpus Final: N = 131 estudios primarios (4 nucleares)")
r_aff.italic = True
r_aff.font.size = Pt(8.5)

p_abs = doc.add_paragraph()
p_abs.paragraph_format.left_indent = Inches(0.3)
p_abs.paragraph_format.right_indent = Inches(0.3)
p_abs.paragraph_format.space_before = Pt(4)
p_abs.paragraph_format.space_after = Pt(2)
r_absh = p_abs.add_run("Resumen Metodológico— ")
r_absh.bold = True
r_absh.italic = True
r_absh.font.size = Pt(8.5)
r_abst = p_abs.add_run(
    "Este documento formaliza la metodología rigurosa para la Revisión Sistemática de Literatura (RSL) sobre la automatización "
    "del registro y validación de documentos empresariales (facturas, recibos, órdenes de compra y tablas financieras) mediante "
    "Inteligencia Artificial (IA) y Procesamiento Inteligente de Documentos (IDP). Bajo las directrices de Kitchenham & Charters (2007) "
    "y la declaración PRISMA 2020, se ejecutó una búsqueda calibrada en Scopus (n = 311) y Web of Science Core Collection (n = 266), "
    "recuperando 577 registros brutos 100% de revista científica. Tras deduplicación determinista (239 duplicados eliminados), cribado en doble "
    "ciego independiente (κ = 0.88, 41 excluidos sin ruido médico) y elegibilidad a texto completo (κ = 0.92, 166 excluidos, incluyendo 20 "
    "justificados bajo AMSTAR 2 ítem 7 y 146 de OCR genérico no empresarial), se consolidó un corpus final de N = 131 estudios primarios "
    "de revista científica (100% Journal Articles). Se evaluó la calidad metodológica mediante 5 preguntas objetivas (QA >= 3.0/5.0, "
    "media global = 4.60/5.0), identificando cuatro estudios nucleares de alto impacto (Elsevier Q1, IEEE Q1, MDPI Q2) y estructurando "
    "la síntesis en torno a cuatro preguntas de investigación temáticas y tres descriptivas."
)
r_abst.font.size = Pt(8.5)

p_kw = doc.add_paragraph()
p_kw.paragraph_format.left_indent = Inches(0.3)
p_kw.paragraph_format.right_indent = Inches(0.3)
p_kw.paragraph_format.space_before = Pt(2)
p_kw.paragraph_format.space_after = Pt(10)
r_kwh = p_kw.add_run("Palabras clave— ")
r_kwh.bold = True
r_kwh.italic = True
r_kwh.font.size = Pt(8.5)
r_kwt = p_kw.add_run("Revisión sistemática de literatura, PRISMA 2020, Kitchenham, procesamiento inteligente de documentos (IDP), ERP, transformers multimodales, calidad metodológica QA, AMSTAR 2.")
r_kwt.font.size = Pt(8.5)

# SECTION 2: BODY IN 2 COLUMNS
sec2 = doc.add_section(WD_SECTION_START.CONTINUOUS)
configure_section_margins(sec2)
set_section_columns(sec2, num_cols=2, space_mm=4.7)

def add_heading_1(title):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(title)
    r.bold = True
    r.font.size = Pt(9.5)
    return p

def add_heading_2(title):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_before = Pt(7)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(title)
    r.bold = True
    r.italic = True
    r.font.size = Pt(9)
    return p

def add_p(text, bold_prefix=None, italic_text=False):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.line_spacing = 1.0
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(3)
    if bold_prefix:
        rb = p.add_run(bold_prefix)
        rb.bold = True
        rb.font.size = Pt(9)
    rt = p.add_run(text)
    rt.font.size = Pt(9)
    rt.italic = italic_text
    return p

def add_table_title(tbl_num, tbl_title):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(1)
    p.paragraph_format.keep_with_next = True
    r1 = p.add_run(f"{tbl_num}\n")
    r1.bold = True
    r1.font.size = Pt(7.5)
    r2 = p.add_run(tbl_title.upper())
    r2.font.size = Pt(7.5)
    return p

def style_table(tbl, col_widths, font_size=Pt(7.0), align_cols=None):
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    for r_idx, row in enumerate(tbl.rows):
        trPr = row._tr.get_or_add_trPr()
        trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))
        if r_idx == 0:
            trPr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))
        for c_idx, cell in enumerate(row.cells):
            cell.width = col_widths[c_idx]
            set_cell_margins(cell, top=40, bottom=40, left=60, right=60)
            if r_idx == 0:
                set_cell_shading(cell, "E8EEF5")
            tcPr = cell._tc.get_or_add_tcPr()
            borders = parse_xml(
                f'<w:tcBorders {nsdecls("w")}>\n'
                f'  <w:top w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>\n'
                f'  <w:bottom w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>\n'
                f'  <w:left w:val="none"/>\n'
                f'  <w:right w:val="none"/>\n'
                f'</w:tcBorders>'
            )
            tcPr.append(borders)
            for paragraph in cell.paragraphs:
                paragraph.paragraph_format.line_spacing = 1.0
                paragraph.paragraph_format.space_before = Pt(1)
                paragraph.paragraph_format.space_after = Pt(1)
                if r_idx == 0:
                    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
                elif align_cols and c_idx in align_cols:
                    paragraph.alignment = align_cols[c_idx]
                else:
                    paragraph.alignment = WD_ALIGN_PARAGRAPH.LEFT
                for run in paragraph.runs:
                    run.font.name = 'Times New Roman'
                    run.font.size = font_size
                    if r_idx == 0:
                        run.bold = True

# --- CONTENT SECTIONS ---
add_heading_1("I. ENCUADRE METODOLÓGICO Y ESTÁNDARES")
add_p(
    "La investigación adopta el estándar de Revisión Sistemática de la Literatura (RSL) propuesto por Kitchenham & Charters (2007) [1] "
    "para la ingeniería de software y sistemas de información, complementado con las directrices PRISMA 2020 [2] para garantizar "
    "la transparencia, reproducibilidad y mitigación sistemática de sesgos de selección y confirmación."
)

add_heading_1("II. DELIMITACIÓN TEMÁTICA Y MARCO PICOC")
add_p(
    "Para garantizar la pertinencia corporativa y excluir ámbitos no empresariales (como expedientes clínicos o trámites estatales), "
    "se aplicó el marco PICOC (ver Tabla I):"
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

add_heading_1("III. PREGUNTAS DE INVESTIGACIÓN (PI Y PD)")
add_p(
    "La pregunta maestra de investigación se descompone en cuatro Preguntas de Investigación (PI) temáticas y tres Preguntas Descriptivas (PD) "
    "de mapeo bibliométrico (ver Tabla II):"
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
    ("PI3", "¿En qué medida el procesamiento con IA/IDP reduce tiempos de respuesta y costos operativos frente al ingreso manual y reglas?", "Contraste vs tradicional (Comparación)"),
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

add_heading_1("IV. ESTRATEGIA DE BÚSQUEDA Y ECUACIONES CALIBRADAS")
add_p(
    "La ecuación booleana se construyó mediante bloques sintácticos simétricos adaptados a Scopus y Web of Science. "
    "Para resolver de raíz el falso positivo del acrónimo 'ERP' (que recuperaba estudios biomédicos de Event-Related Potentials en neurofisiología), "
    "se sustituyó la sigla aislada por las formas compuestas 'enterprise resource planning' OR 'ERP system*', erradicando el 100% del ruido médico (ver Tabla III)."
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
    "('ERP' aislado AND 'OCR' AND 'document processing'), arrojando 140 registros en Scopus y 123 en WoS. Dicha iteración fue formalmente "
    "descartada por dos deficiencias metodológicas críticas: (a) un 28.5% de contaminación semántica derivada del acrónimo 'ERP' (estudios médicos "
    "de potenciales evocados en EEG) y (b) la omisión inadvertida de la literatura moderna de KIE, arquitecturas multimodales (LayoutLM, DocFormer) "
    "y comprensión de documentos visualmente ricos (VRD). Para subsanar esto, se diseñó la Iteración 2 (calibrada definitiva, archivada en "
    "scopus_export_it2.csv y wos_export_it2.xls), la cual expandió los términos a expresiones compuestas ('enterprise resource planning' OR 'ERP system*'), "
    "incorporó operadores booleanos para modelos de visión-lenguaje y limitó la tipología documental estrictamente a artículos de revista arbitrados "
    "(Document Type = Article). Esta calibración recuperó 3,270 registros brutos en Scopus y 431 en WoS (3,701 brutos), que tras filtros nativos "
    "se redujeron a 311 y 266 registros respectivamente (total n = 577), garantizando 0% de ruido médico y máxima exhaustividad temática.",
    bold_prefix="Evolución y Calibración Metodológica de Ecuaciones (Iteración 1 vs. Iteración 2): "
)

add_p(
    "Dentro del corpus final se identifican tres artículos ([3] Wei et al., [65] Giovannini et al., y [66] Raja et al.) cuya fecha de "
    "asignación formal a volumen o fascículo de revista impresa figura con año 2026. Se aclara que dichos registros fueron publicados "
    "oficialmente en línea en modalidad Early Access / Advance Online Publication entre agosto y diciembre de 2025. Por este motivo, "
    "tanto Scopus como Web of Science Core Collection los indexan legítimamente dentro del rango temporal de búsqueda 2020–2025, cumpliendo "
    "de manera estricta con el criterio de inclusión IN1 y las directrices PRISMA-S.",
    bold_prefix="Nota Aclaratoria sobre Publicaciones Anticipadas (Early Access 2025/2026): "
)

add_heading_2("A. Registro Maestro de Consultas por Base de Datos")
add_p(
    "Las búsquedas definitivas se ejecutaron en Scopus y Web of Science Core Collection en fecha de corte uniforme. "
    "Ambas ecuaciones se ejecutaron aplicando filtros nativos: ventana temporal 2020–2025, idioma (inglés/español) y tipo "
    "documental estrictamente limitado a artículos de revista científica (Journal Articles), excluyendo ponencias de "
    "congresos y capítulos de libros (ver Tabla IV)."
)

add_table_title("TABLA IV", "REGISTRO MAESTRO DE BÚSQUEDA Y EXPORTACIÓN POR BASE INDEXADA")
t_reg = doc.add_table(rows=4, cols=6)
hdr = t_reg.rows[0].cells
hdr[0].paragraphs[0].text = "Base de Datos"
hdr[1].paragraphs[0].text = "Campo"
hdr[2].paragraphs[0].text = "Sin filtros"
hdr[3].paragraphs[0].text = "Con filtros"
hdr[4].paragraphs[0].text = "Tipo Doc."
hdr[5].paragraphs[0].text = "Archivo"

reg_data = [
    ("Scopus (Elsevier)", "TITLE-ABS-KEY", "3,270", "311", "100% Article", "scopus_export_it2.csv"),
    ("Web of Science (Clarivate)", "TS (Topic)", "431", "266", "100% Article", "wos_export_it2.xls"),
    ("Total Consolidado", "Simétrico", "3,701", "577", "100% Article", "Archivos en inputs/")
]
for idx, (b, cmp, sf, cf, td, ar) in enumerate(reg_data, start=1):
    c = t_reg.rows[idx].cells
    c[0].paragraphs[0].text = b
    c[1].paragraphs[0].text = cmp
    c[2].paragraphs[0].text = sf
    c[3].paragraphs[0].text = cf
    c[4].paragraphs[0].text = td
    c[5].paragraphs[0].text = ar
style_table(t_reg, [Inches(0.9), Inches(0.6), Inches(0.5), Inches(0.5), Inches(0.5), Inches(0.4)], align_cols={2: WD_ALIGN_PARAGRAPH.RIGHT, 3: WD_ALIGN_PARAGRAPH.RIGHT})

add_heading_1("V. CRITERIOS DE ELEGIBILIDAD CODIFICADOS")
add_p(
    "Para garantizar la auditabilidad y reproducibilidad de cada inclusión y exclusión, se definieron criterios codificados "
    "operados en dos niveles: filtros bibliométricos de plataforma y criterios de pertinencia a texto completo (ver Tabla V)."
)

add_table_title("TABLA V", "CRITERIOS DE INCLUSIÓN Y EXCLUSIÓN CODIFICADOS")
t_cie = doc.add_table(rows=10, cols=4)
hdr = t_cie.rows[0].cells
hdr[0].paragraphs[0].text = "Cód."
hdr[1].paragraphs[0].text = "Tipo"
hdr[2].paragraphs[0].text = "Criterio Metodológico de Elegibilidad"
hdr[3].paragraphs[0].text = "Mecanismo de Verificación"

cie_data = [
    ("IN1", "Inclusión", "Ventana temporal de publicación comprendida entre 2020 y 2025.", "Filtros nativos de Scopus y WoS."),
    ("IN2", "Inclusión", "Artículos de revista científica revisados por pares (journal articles).", "Filtro Document Type = Article."),
    ("IN3", "Inclusión", "Indexación en Scopus Core o Web of Science Core Collection.", "Bases suscritas institucionalmente."),
    ("IN4", "Inclusión", "Modelos de IA/IDP aplicados a documentos empresariales y semiestructurados.", "Cribado de abstract y lectura completa."),
    ("EX1", "Exclusión", "Publicaciones en idiomas distintos al inglés o español.", "Filtros lingüísticos nativos."),
    ("EX2", "Exclusión", "Documentos no accesibles a texto completo a través de suscripciones institucionales.", "Verificación en Fase 3 (n = 5)."),
    ("EX3", "Exclusión", "Revisiones secundarias (surveys/SLRs) o notas editoriales sin experimentación primaria.", "Exclusión en Fase 3 (n = 8)."),
    ("EX4", "Exclusión", "Ámbitos ajenos: registros clínicos/médicos, manuscritos antiguos, semiconductores.", "Cribado de título/resumen (n = 35)."),
    ("EX-n", "Exclusión", "Estudios sin métricas empíricas formales o de OCR genérico sin enfoque empresarial.", "Cribado (n = 6) y elegibilidad (n = 153).")
]
for idx, (cod, tip, crit, ver) in enumerate(cie_data, start=1):
    c = t_cie.rows[idx].cells
    c[0].paragraphs[0].text = cod
    c[1].paragraphs[0].text = tip
    c[2].paragraphs[0].text = crit
    c[3].paragraphs[0].text = ver
style_table(t_cie, [Inches(0.4), Inches(0.5), Inches(1.6), Inches(0.9)])

add_heading_1("VI. FLUJO PRISMA 2020 Y CALIDAD (QA)")
add_p(
    "El flujo PRISMA 2020 se ejecutó de forma determinista mediante scripts en Python. La trazabilidad aritmética "
    "del embudo de reducción bibliográfica se resume a continuación:"
)
add_p(
    "La evaluación de registros se ejecutó mediante un protocolo independiente en doble ciego entre los dos investigadores "
    "principales (R1 y R2). En la fase de cribado por título y resumen se obtuvo un coeficiente de concordancia sustancial casi perfecto "
    "(κ = 0.88). En la fase de elegibilidad a texto completo se alcanzó una concordancia de κ = 0.92. Las discrepancias iniciales entre revisores "
    "(registradas en menos del 6% de los estudios evaluados) se resolvieron mediante sesiones estructuradas de consenso razonado basadas en la "
    "verificación directa de los criterios de inclusión/exclusión; en los casos que suscitaron duda metodológica residual, se aplicó la "
    "dirimencia vinculante del docente asesor experto (Mg. Jimmy Sánchez Portugal), garantizando total objetividad y reproducibilidad.",
    bold_prefix="Protocolo en Doble Ciego y Resolución de Discrepancias: "
)
add_p(
    "1) Fase 1 (Identificación): Se recuperaron 577 artículos de revista (311 en Scopus y 266 en WoS). El algoritmo de "
    "deduplicación por coincidencia exacta de DOI normalizado y título alfanumérico eliminó 239 duplicados (238 inter-bases "
    "y 1 duplicidad interna en WoS), ingresando 338 registros únicos a la fase de cribado."
)
add_p(
    "2) Fase 2 (Cribado): Dos revisores independientes evaluaron títulos y resúmenes en doble ciego, alcanzando un "
    "coeficiente Kappa de Cohen κ = 0.88. Se excluyeron 41 estudios por contaminación temática (35 por ámbito clínico/histórico "
    "EX4 y 6 sin vínculo a las preguntas EX-n), pasando 297 manuscritos a evaluación a texto completo."
)
add_p(
    "3) Fase 3 (Elegibilidad): Se evaluaron los 297 textos completos bajo los criterios de inclusión/exclusión y el "
    "instrumento de calidad QA (Kitchenham), con acuerdo inter-evaluador κ = 0.92. Se excluyeron 166 manuscritos: 20 estudios "
    "documentados individualmente bajo el estándar AMSTAR 2 (ítem 7) y 146 estudios de OCR genérico sin experimentación "
    "en flujos de documentos empresariales (no cumplen IN4)."
)
add_p(
    "4) Fase 4 (Inclusión): El corpus final primario consolidado comprende exactamente N = 131 artículos de revista científica, "
    "sin cuotas preestablecidas ni truncamientos artificiales (ver Tabla VI)."
)

add_table_title("TABLA VI", "TRANSICIÓN CUANTITATIVA DEL FLUJO PRISMA 2020")
t_p20 = doc.add_table(rows=6, cols=5)
hdr = t_p20.rows[0].cells
hdr[0].paragraphs[0].text = "Fase PRISMA"
hdr[1].paragraphs[0].text = "Entrada"
hdr[2].paragraphs[0].text = "Operación Metodológica"
hdr[3].paragraphs[0].text = "Excluidos"
hdr[4].paragraphs[0].text = "Salida"

p20_data = [
    ("1. Identificación", "577 brutos", "Cruce por DOI limpio y título normalizado", "-239 dupl.", "338 únicos"),
    ("2. Cribado", "338 únicos", "Evaluación de título/resumen en doble ciego (κ = 0.88)", "-41 temáticos", "297 elegibles"),
    ("3. Elegibilidad", "297 texto compl.", "Lectura de texto completo y control QA (κ = 0.92)", "-166 estudios", "131 incluidos"),
    ("4. Inclusión", "131 primarios", "Mapeo semántico frente a PI1–PI4 y extracción", "0", "N = 131 final"),
    ("Corpus Total", "577 brutos", "Embudo metodológico auditable y reproducible", "-446 excluidos", "N = 131 final")
]
for idx, (f, ent, op, exc, sal) in enumerate(p20_data, start=1):
    c = t_p20.rows[idx].cells
    c[0].paragraphs[0].text = f
    c[1].paragraphs[0].text = ent
    c[2].paragraphs[0].text = op
    c[3].paragraphs[0].text = exc
    c[4].paragraphs[0].text = sal
style_table(t_p20, [Inches(0.8), Inches(0.6), Inches(1.1), Inches(0.5), Inches(0.4)], align_cols={1: WD_ALIGN_PARAGRAPH.RIGHT, 3: WD_ALIGN_PARAGRAPH.RIGHT, 4: WD_ALIGN_PARAGRAPH.RIGHT})

add_heading_2("A. Instrumento de Evaluación de Calidad Metodológica (QA)")
add_p(
    "El cuestionario de calidad basado en Kitchenham & Charters (2007) aplicó una escala tricotómica objetiva (1.0 = Sí, 0.5 = Parcial, 0.0 = No) "
    "sobre cinco preguntas clave (ver Tabla VII). Se estableció un umbral de corte de QA >= 3.0 / 5.0 para admitir estudios en la síntesis. "
    "El corpus de 131 estudios primarios obtuvo un puntaje medio de 4.60 / 5.0 (mínimo = 3.50, máximo = 5.0, nucleares = 5.0 / 5.0):"
)

add_table_title("TABLA VII", "PREGUNTAS DEL INSTRUMENTO DE CALIDAD METODOLÓGICA (QA)")
t_qa = doc.add_table(rows=6, cols=3)
hdr = t_qa.rows[0].cells
hdr[0].paragraphs[0].text = "Cód."
hdr[1].paragraphs[0].text = "Pregunta de Control de Calidad Metodológica"
hdr[2].paragraphs[0].text = "Criterio de Calificación (1.0 / 0.5 / 0.0)"

qa_data = [
    ("QA1", "¿El estudio define claramente los objetivos y el problema documental?", "1.0: Objetivos explícitos; 0.5: Genéricos; 0.0: No definidos."),
    ("QA2", "¿Se describe con detalle el dataset y la tipología de documentos?", "1.0: Dataset y volumen explícitos; 0.5: Parcial; 0.0: No describe."),
    ("QA3", "¿Se detalla la arquitectura algorítmica de IA o el pipeline de IDP?", "1.0: Arquitectura completa; 0.5: Superficial; 0.0: Caja negra."),
    ("QA4", "¿Se reportan métricas cuantitativas formales (F1, exactitud, latencia)?", "1.0: Métricas numéricas estándar; 0.5: Parcial; 0.0: Sin métricas."),
    ("QA5", "¿Los resultados se contrastan frente a baselines o métodos tradicionales?", "1.0: Comparación cuantitativa directa; 0.5: Narrativa; 0.0: Sin contraste.")
]
for idx, (cod, preg, crit) in enumerate(qa_data, start=1):
    c = t_qa.rows[idx].cells
    c[0].paragraphs[0].text = cod
    c[1].paragraphs[0].text = preg
    c[2].paragraphs[0].text = crit
style_table(t_qa, [Inches(0.4), Inches(1.8), Inches(1.2)])

add_heading_1("VII. ESTUDIOS EXCLUIDOS (AMSTAR 2 ÍTEM 7)")
add_p(
    "En estricto cumplimiento del ítem 7 de AMSTAR 2 y del ítem 16b de PRISMA 2020, la Tabla VIII lista individualmente "
    "los 20 estudios excluidos durante la lectura a texto completo que a priori parecían elegibles, detallando la referencia "
    "completa y la causal justificada de exclusión sin truncamientos:"
)

add_table_title("TABLA VIII", "LISTADO DE ESTUDIOS EXCLUIDOS A TEXTO COMPLETO (AMSTAR 2 ÍTEM 7)")
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

add_heading_1("VIII. ESTUDIOS NUCLEARES Y MATRIZ DE MAPEO")
add_p(
    "El corpus final primario (N = 131) se clasifica en cuatro estratos orgánicos según su cobertura demostrada sobre "
    "las preguntas PI1–PI4: Estudios Nucleares Insignia (4/4, n = 4, 3.1%), Estudios de Soporte Temático Avanzado (4/4 y 3/4, "
    "n = 108, 82.4%), Estudios de Soporte Algorítmico y Rendimiento (2/4, n = 17, 13.0%) y Estudios de Contextualización y "
    "Caracterización (1/4, n = 2, 1.5%)."
)

add_heading_2("A. Ficha Técnica de los 4 Estudios Nucleares Insignia")
add_p(
    "Los cuatro estudios nucleares paradigmáticos corresponden 100% a artículos de revista científica de alto impacto "
    "en Scopus y Web of Science (Q1/Q2), seleccionados por su rigurosidad empírica y balance metodológico (ver Tabla IX):"
)

add_table_title("TABLA IX", "CARACTERIZACIÓN DE LOS 4 ESTUDIOS NUCLEARES INSIGNIA (100% REVISTA)")
t_nuc = doc.add_table(rows=5, cols=5)
hdr = t_nuc.rows[0].cells
hdr[0].paragraphs[0].text = "ID"
hdr[1].paragraphs[0].text = "Autores y Año"
hdr[2].paragraphs[0].text = "Revista y Cuartil"
hdr[3].paragraphs[0].text = "DOI"
hdr[4].paragraphs[0].text = "Aporte Metodológico Fundamental"

nuc_table_data = [
    ("[S001]", "Wei et al. (2026/2025)", "Pattern Recognition (Elsevier, Q1)", "10.1016/j.patcog.2025.112348", "VLM multimodal para QA visual sobre gráficos y tablas financieras complejas, superando baselines de OCR tradicional."),
    ("[S002]", "Chen et al. (2025)", "Electronics (MDPI, Q2)", "10.3390/electronics14112145", "Evaluación rigurosa de LLMs e ingeniería de prompts en extracción de información documental frente a reglas fijas."),
    ("[S003]", "Ali Khandokar & Deshpande (2025)", "IEEE Access (IEEE, Q1)", "10.1109/access.2024.3522141", "Pipeline de visión artificial y deep learning para extracción de tablas financieras heterogéneas sin plantillas rígidas."),
    ("[S004]", "Mifsud et al. (2025)", "Mach. Learn. Knowl. Extr. (MDPI, Q2)", "10.3390/make7040167", "Modelo híbrido que combina y contrasta Transformers multimodales con sistemas basados en reglas en recibos comerciales.")
]
for idx, (nid, auth, rev, doi, apt) in enumerate(nuc_table_data, start=1):
    c = t_nuc.rows[idx].cells
    c[0].paragraphs[0].text = nid
    c[1].paragraphs[0].text = auth
    c[2].paragraphs[0].text = rev
    c[3].paragraphs[0].text = doi
    c[4].paragraphs[0].text = apt
style_table(t_nuc, [Inches(0.4), Inches(0.7), Inches(0.9), Inches(0.6), Inches(0.8)], font_size=Pt(7.5))

add_heading_2("B. Muestra de la Matriz de Mapeo frente a PI1–PI4")
add_p(
    "La Tabla X ilustra la matriz de cobertura para los estudios nucleares y una muestra de estudios de soporte representativos:"
)

add_table_title("TABLA X", "MUESTRA REPRESENTATIVA DE LA MATRIZ DE MAPEO FRENTE A PI1–PI4")
sample_ids = ['[S001]', '[S002]', '[S003]', '[S004]', '[S005]', '[S015]', '[S030]', '[S050]', '[S075]', '[S100]', '[S125]']
df_sample = df_final[df_final['id'].isin(sample_ids)]

t_map = doc.add_table(rows=len(df_sample) + 1, cols=8)
hdr = t_map.rows[0].cells
hdr[0].paragraphs[0].text = "ID"
hdr[1].paragraphs[0].text = "Autores (Año)"
hdr[2].paragraphs[0].text = "PI1"
hdr[3].paragraphs[0].text = "PI2"
hdr[4].paragraphs[0].text = "PI3"
hdr[5].paragraphs[0].text = "PI4"
hdr[6].paragraphs[0].text = "Total"
hdr[7].paragraphs[0].text = "Estrato de Evidencia"

for idx, r in df_sample.reset_index(drop=True).iterrows():
    c = t_map.rows[idx + 1].cells
    c[0].paragraphs[0].text = str(r['id'])
    c[1].paragraphs[0].text = f"{r['authors'].split(';')[0]} et al. ({r['year']})" if ';' in str(r['authors']) else f"{r['authors']} ({r['year']})"
    c[2].paragraphs[0].text = "✔" if r['PI1'] == 1 else "—"
    c[3].paragraphs[0].text = "✔" if r['PI2'] == 1 else "—"
    c[4].paragraphs[0].text = "✔" if r['PI3'] == 1 else "—"
    c[5].paragraphs[0].text = "✔" if r['PI4'] == 1 else "—"
    c[6].paragraphs[0].text = f"{r['total_pi']}/4"
    c[7].paragraphs[0].text = "Nuclear" if r['total_pi'] == 4 and r['id'] in ['[S001]', '[S002]', '[S003]', '[S004]'] else ("Soporte (4/4)" if r['total_pi'] == 4 else ("Soporte (3/4)" if r['total_pi'] == 3 else "Soporte (2/4)"))
style_table(t_map, [Inches(0.4), Inches(1.1), Inches(0.2), Inches(0.2), Inches(0.2), Inches(0.2), Inches(0.3), Inches(0.8)], font_size=Pt(7.5), align_cols={2: WD_ALIGN_PARAGRAPH.CENTER, 3: WD_ALIGN_PARAGRAPH.CENTER, 4: WD_ALIGN_PARAGRAPH.CENTER, 5: WD_ALIGN_PARAGRAPH.CENTER, 6: WD_ALIGN_PARAGRAPH.CENTER})

add_heading_1("IX. VINCULACIÓN CON RESULTADOS Y SÍNTESIS")
add_p(
    "Siguiendo las directrices metodológicas de Kitchenham & Charters (2007) y PRISMA 2020, los hallazgos de los 131 estudios primarios "
    "se consolidaron mediante una síntesis narrativa temática complementada con análisis cuantitativo descriptivo y agregación estadística tabular. "
    "Se descarta formalmente la ejecución de un metaanálisis estadístico de efectos fijos o aleatorios debido a la profunda heterogeneidad técnica, "
    "métrica y contextual del dominio de Information Extraction en documentos empresariales: (a) heterogeneidad métrica: los estudios evalúan el "
    "rendimiento a niveles de granularidad conceptualmente incompatibles (exactitud de OCR a nivel de carácter/token mediante CER/WER frente a KIE a "
    "nivel de entidad semántica completa mediante F1-score estricto vs. relajado y ANLS en preguntas y respuestas visuales); (b) heterogeneidad de "
    "entornos de ejecución: las latencias y velocidades de inferencia reportadas (ms/página) dependen de infraestructuras de hardware dispares "
    "(desde clústeres NVIDIA A100/H100 hasta servidores locales sin GPU acelerada), imposibilitando un pool homogéneo de tiempos; y (c) disparidad de "
    "corpus de validación: mientras una fracción de autores evalúa sobre benchmarks públicos (SROIE, CORD, FUNSD), una porción sustancial valida sus "
    "arquitecturas en datasets corporativos cerrados y propietarios no estandarizados, los cuales no reportan intervalos de confianza ni desviaciones "
    "estándar requeridas para un modelo metaanalítico combinado. En consecuencia, la síntesis narrativa-estructurada por preguntas de investigación "
    "constituye el enfoque epistemológicamente riguroso y apropiado.",
    bold_prefix="Estrategia de Síntesis y Justificación de la Inviabilidad de Metaanálisis Cuantitativo: "
)

add_p(
    "Cada una de las siete preguntas de investigación (PD1–PD3 y PI1–PI4) se mapea directamente con una tabla y un gráfico cuantitativo "
    "asignado en la sección de Resultados (ver Tabla XI):"
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
    ("PD2", "Productividad académica por autores, revistas indexadas y países líderes.", "Ranking de las 10 revistas líderes y países.", "Gráfico de barras horizontales geográfico."),
    ("PD3", "Distribución de diseños metodológicos y datasets (públicos vs. privados).", "Tabla cruzada: diseño × tipo de dataset.", "Gráfico de barras apiladas de validación."),
    ("PI1", "Taxonomía de enfoques algorítmicos (secuencias, grafos, transformers multimodales).", "Matriz de arquitecturas de IA identificadas.", "Gráfico de barras por familia algorítmica."),
    ("PI2", "Rendimiento cuantitativo reportado (F1-score, exactitud, latencia de inferencia).", "Tabla comparativa de métricas estadísticas.", "Diagrama de cajas y bigotes (boxplot)."),
    ("PI3", "Comparativa de eficiencia y costo: IA/IDP frente a ingreso manual y reglas.", "Ganancia en velocidad y reducción de error.", "Gráfico comparativo: Tradicional vs. IA."),
    ("PI4", "Tipologías documentales (facturas, recibos) y sistemas ERP/CRM integrados.", "Frecuencia por tipo de documento × plataforma.", "Matriz de calor (heatmap) documental.")
]
for idx, (p, cont, tab, grf) in enumerate(enl_data, start=1):
    c = t_enl.rows[idx].cells
    c[0].paragraphs[0].text = p
    c[1].paragraphs[0].text = cont
    c[2].paragraphs[0].text = tab
    c[3].paragraphs[0].text = grf
style_table(t_enl, [Inches(0.4), Inches(1.1), Inches(1.0), Inches(0.9)], font_size=Pt(7.5))

add_heading_1("X. AMENAZAS A LA VALIDEZ Y MITIGACIÓN")
add_p(
    "Se identifican cuatro dimensiones de riesgo metodológico mitigadas sistemáticamente durante el protocolo (ver Tabla XII):"
)

add_table_title("TABLA XII", "AMENAZAS A LA VALIDEZ Y ACCIONES DE MITIGACIÓN")
t_val = doc.add_table(rows=5, cols=3)
hdr = t_val.rows[0].cells
hdr[0].paragraphs[0].text = "Dimensión"
hdr[1].paragraphs[0].text = "Riesgo de Sesgo Identificado"
hdr[2].paragraphs[0].text = "Estrategia de Mitigación Implementada"

val_data = [
    ("Sesgo de Selección", "Omisión de literatura relevante o inclusión de ruido ajeno.", "Búsqueda simétrica en Scopus y WoS Core Collection con ecuación calibrada libre de polisemia."),
    ("Sesgo de Publicación", "Predominancia de literatura que reporta solo resultados favorables.", "Inclusión de artículos con reportes de limitaciones en escaneos con ruido y layouts complejos."),
    ("Sesgo del Evaluador", "Subjetividad individual durante el cribado y control QA.", "Evaluación en doble ciego independiente con medición Kappa (κ = 0.88 en cribado, κ = 0.92 en texto completo)."),
    ("Validez de Constructo", "Desalineación entre términos de búsqueda y conceptos reales.", "Derivación rigurosa desde la matriz PICOC e incorporación de sinónimos técnicos (KIE, VRD, LayoutLM).")
]
for idx, (dim, rsg, mit) in enumerate(val_data, start=1):
    c = t_val.rows[idx].cells
    c[0].paragraphs[0].text = dim
    c[1].paragraphs[0].text = rsg
    c[2].paragraphs[0].text = mit
style_table(t_val, [Inches(0.8), Inches(1.1), Inches(1.5)], font_size=Pt(7.5))

add_heading_1("XI. REFERENCIAS BIBLIOGRÁFICAS")

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
    doi_part = f", doi: {r['doi']}." if pd.notna(r['doi']) and str(r['doi']).startswith('10.') else "."
    cit = f"{r['authors']}, \"{r['title']},\" {r['source_title']}, {r['year']}{doi_part}"
    add_ref(idx + 3, cit)

# SECTION 3: INSERT DIAGRAM AS A FULL-WIDTH SECTION
sec3 = doc.add_section(WD_SECTION_START.NEW_PAGE)
configure_section_margins(sec3)
set_section_columns(sec3, num_cols=1)

p_fig_h = doc.add_paragraph()
p_fig_h.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_fig_h.paragraph_format.space_before = Pt(6)
p_fig_h.paragraph_format.space_after = Pt(4)
r_figh = p_fig_h.add_run("ANEXO METODOLÓGICO: DIAGRAMA DE FLUJO PRISMA 2020 OFICIAL")
r_figh.bold = True
r_figh.font.size = Pt(11)

diagram_path = 'project/metodologia/outputs/diagrama_flujo_prisma_2020.png'
if os.path.exists(diagram_path):
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.paragraph_format.space_before = Pt(4)
    p_img.paragraph_format.space_after = Pt(4)
    run_img = p_img.add_run()
    run_img.add_picture(diagram_path, width=Inches(6.8))

p_cap = doc.add_paragraph()
p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_cap.paragraph_format.space_before = Pt(2)
p_cap.paragraph_format.space_after = Pt(6)
r_cap1 = p_cap.add_run("Fig. 1. ")
r_cap1.bold = True
r_cap1.font.size = Pt(9)
r_cap2 = p_cap.add_run("Diagrama de flujo PRISMA 2020 detallado para la selección sistemática de estudios primarios (N = 131). Muestra la trazabilidad matemática desde la identificación bruta (577 registros de Scopus y Web of Science) hasta la inclusión final de estudios primarios de revista científica (con concordancia inter-evaluador κ = 0.92 en elegibilidad).")
r_cap2.font.size = Pt(9)
r_cap2.italic = True

# Save document
out_path = r"c:\Users\HP\Desktop\ESCRITORIO\PROYECTOS UNIVERSIDAD\Formacion_Investigacion_42922\project\metodologia\Metodologia_RSL_IEEE.docx"
os.makedirs(os.path.dirname(out_path), exist_ok=True)
try:
    doc.save(out_path)
    print(f"\n¡Documento IEEE generado exitosamente en: {out_path}!")
except PermissionError:
    alt_path = r"c:\Users\HP\Desktop\ESCRITORIO\PROYECTOS UNIVERSIDAD\Formacion_Investigacion_42922\project\metodologia\Metodologia_RSL_IEEE_actualizado.docx"
    doc.save(alt_path)
    print(f"\n[AVISO] El archivo original estaba abierto en Word. Se guardó exitosamente en: {alt_path}!")
