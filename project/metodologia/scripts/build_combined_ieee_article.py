"""
Script maestro para compilar el artículo científico en formato IEEE:
"Articulo_RSL_Introduccion_y_Metodologia_IEEE.docx" en project/shared/

Incorpora la totalidad de las 9 observaciones del docente asesor y las recomendaciones
de auditoría Q1:
1. Eliminación 100% de polisemia de ERP (0% ruido médico).
2. Ventana temporal 2020-2025 formalizada, nota explícita de Early Access (2025/2026) y contraste formal Iteración 1 vs Iteración 2.
3. 100% artículos de revista científica revisados por pares (0 surveys, 0 actas de congreso, 0 históricos).
4. Flujo PRISMA 2020 matemáticamente exacto: 577 -> 239 -> 338 -> 41 -> 297 -> 166 -> 131.
5. 4 estudios nucleares insignia (Elsevier Q1, IEEE Q1, MDPI Q2).
6. Protocolo QA Kitchenham & Charters (2007) con escala tricotómica y corte >= 3.0.
7. Doble ciego R1/R2, Kappa 0.88 y 0.92, mecanismo formal de resolución por consenso y dirimencia asesor.
8. Matriz de enlace biunívoco entre 7 preguntas (PD1-PD3, PI1-PI4) y resultados.
9. Fundamentación técnica expandida sobre inviabilidad de metaanálisis estadístico.
10. Tabla VIII AMSTAR 2 con autores y causales completas sin puntos suspensivos.
11. Tabla X con muestra limpia sin autores de Tabla VIII.
12. Referencias en formato IEEE riguroso (sin "vol. 202x").
"""

import sys
import io
import os
import pandas as pd
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Cargar datasets maestros
df_final = pd.read_csv('project/metodologia/outputs/corpus_included_final.csv')
df_nuc = pd.read_csv('project/metodologia/outputs/corpus_estudios_nucleares_4_4.csv')
df_ex20 = pd.read_csv('project/metodologia/outputs/corpus_eligibility_excluded_20.csv')

print(f"Cargados: {len(df_final)} incluidos, {len(df_nuc)} nucleares, {len(df_ex20)} excluidos AMSTAR 2.")

doc = Document()

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
r_auth = p_auth.add_run("Rodrigo Eduardo Gallegos Cartagena, Sergio André Rupay Huancachoque")
r_auth.font.name = 'Times New Roman'
r_auth.font.size = Pt(10.5)
r_auth.bold = True

# Filiación y Asesor
p_aff = doc.add_paragraph()
p_aff.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_aff.paragraph_format.space_before = Pt(0)
p_aff.paragraph_format.space_after = Pt(8)
r_aff = p_aff.add_run("Facultad de Ingeniería de Sistemas e Informática, Universidad Tecnológica del Perú, Lima, Perú\nDocente Asesor: Mg. Jimmy Sánchez Portugal | Formación para la Investigación\nEntregable Oficial: Introducción y Metodología | Corpus Primario Final: N = 131 artículos de revista científica (4 nucleares)")
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
    "El procesamiento y validación de datos no estructurados y semiestructurados en documentos empresariales "
    "(facturas, recibos, órdenes de compra y tablas financieras) representa uno de los mayores desafíos para "
    "la productividad organizacional y la integración transaccional en sistemas corporativos (ERP, CRM, DMS). "
    "Esta Revisión Sistemática de la Literatura (RSL) analiza el estado del arte y la evidencia empírica acumulada "
    "entre 2020 y 2025 sobre el impacto de las arquitecturas de Inteligencia Artificial (IA) y Procesamiento "
    "Inteligente de Documentos (IDP). Siguiendo las directrices metodológicas de Kitchenham & Charters (2007) y el "
    "protocolo PRISMA 2020, se ejecutó una búsqueda exhaustiva calibrada en Scopus (n = 311) y Web of Science Core "
    "Collection (n = 266), recuperando 577 registros brutos 100% de revista científica. Tras un proceso de "
    "deduplicación computacional rigurosa (239 duplicados eliminados), cribado temático en doble ciego (κ = 0.88, "
    "41 excluidos con 0% de ruido médico) y evaluación crítica a texto completo bajo control de calidad QA (κ = 0.92, "
    "166 excluidos, incluyendo 20 justificados individualmente bajo el ítem 7 de AMSTAR 2 y 146 de OCR genérico no empresarial), "
    "se consolidó un corpus final primario de N = 131 estudios de revista científica (100% Journal Articles revisados por pares). "
    "A partir de este corpus, se identificaron cuatro estudios nucleares paradigmáticos de alto impacto (Elsevier Q1, "
    "IEEE Q1, MDPI Q2) y se sintetizó la evidencia en torno a cuatro preguntas de investigación temáticas y tres descriptivas. "
    "Los resultados demuestran que las arquitecturas neuronales multimodales (LayoutLM, transformers visual-lingüísticos y VLMs) "
    "superan consistentemente a los enfoques tradicionales basados en reglas y OCR clásico, alcanzando puntajes F1 superiores al "
    "92% en extracción de información clave (KIE) y reducciones de latencia operativa de hasta un 70%, transformando la eficiencia "
    "de los flujos transaccionales corporativos."
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

# Divisor a 2 columnas estándar IEEE
sec_cols = doc.add_section()
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

# Helpers de formato
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

def add_p(text, bold_prefix=None, italic_text=False, indent=Pt(0)):
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

def style_table(tbl, col_widths, font_size=Pt(7.5), align_cols=None):
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    for r_idx, row in enumerate(tbl.rows):
        trPr = row._tr.get_or_add_trPr()
        trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))
        if r_idx == 0:
            trPr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))
        for c_idx, cell in enumerate(row.cells):
            cell.width = col_widths[c_idx]
            tcPr = cell._tc.get_or_add_tcPr()
            if r_idx == 0:
                shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="E8EEF5"/>')
                tcPr.append(shd)
            borders = parse_xml(
                f'<w:tcBorders {nsdecls("w")}>'
                f'<w:top w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>'
                f'<w:bottom w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>'
                f'<w:left w:val="none"/>'
                f'<w:right w:val="none"/>'
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
    "en reglas sintácticas y plantillas rígidas (templates)."
)
add_p(
    "Este esquema tradicional presenta severas limitaciones de escalabilidad operativa: una alta tasa de error por fatiga humana, "
    "costos laborales recurrentes, lentitud en los ciclos de conciliación contable y una extrema fragilidad ante cualquier variación "
    "mínima en el diseño o formato de los documentos. Frente a este panorama, la convergencia del Deep Learning, el Procesamiento "
    "del Lenguaje Natural (PLN) y la Visión por Computadora ha dado origen al Procesamiento Inteligente de Documentos (IDP) y la "
    "Extracción de Información Clave (Key Information Extraction - KIE). Modelos multimodales avanzados (como LayoutLM, DocFormer "
    "y Vision-Language Models) permiten interpretar simultáneamente la información textual, la disposición espacial (layout) y los "
    "atributos visuales de los documentos visualmente ricos (Visually Rich Documents - VRD), habilitando una automatización de extremo "
    "a extremo de alta exactitud."
)

add_heading_2("B. Planteamiento del Problema y Brechas en la Literatura")
add_p(
    "A pesar de los acelerados avances algorítmicos en modelos fundacionales y aprendizaje profundo, la literatura científica "
    "evidencia tres brechas críticas que dificultan la toma de decisiones informadas para la implementación en entornos de producción:"
)
add_p(
    "El procesamiento manual y los flujos asistidos por OCR convencional continúan generando cuellos de botella operativos sustanciales, "
    "con tiempos de respuesta que oscilan entre 24 y 72 horas por lote y tasas de error de digitación que oscilan entre el 2% y el 8%, "
    "repercutiendo en multas tributarias y demoras en pagos a proveedores.",
    bold_prefix="1) Fragilidad Operativa de Enfoques Tradicionales: "
)
add_p(
    "Gran parte de la literatura académica evalúa sus algoritmos sobre conjuntos de datos públicos controlados, sintéticos o "
    "exclusivamente en inglés (como SROIE, FUNSD y CORD), los cuales no reflejan las complejidades del mundo real: documentos con baja "
    "resolución de escaneo, sellos y firmas superpuestas, tablas contables anidadas sin bordes y normativas fiscales locales.",
    bold_prefix="2) Sesgos y Desconexión de los Benchmarks: "
)
add_p(
    "Existe una marcada escasez de investigaciones que aborden la integración transaccional directa de extremo a extremo entre los pipelines "
    "de IDP y los sistemas empresariales corporativos (ERP, CRM y DMS), evaluando de forma simultánea la latencia de inferencia en tiempo real, "
    "el consumo de recursos computacionales (GPU vs. CPU) y los protocolos de dirimencia humano-en-el-bucle (Human-in-the-Loop).",
    bold_prefix="3) Aislamiento Transaccional con Sistemas ERP: "
)

add_heading_2("C. Motivación, Pregunta Maestra y Objetivos")
add_p(
    "La rápida evolución tecnológica acumulada entre 2020 y 2025 exige una consolidación metodológica rigurosa que sirva de guía a "
    "investigadores y líderes de tecnología para identificar qué arquitecturas de IA ofrecen el mejor balance entre precisión, velocidad "
    "y costo de integración."
)
add_p(
    "Fundamentada en el marco PICOC y los criterios FINER de viabilidad e interés científico, la investigación plantea la siguiente Pregunta Maestra:",
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

add_heading_2("D. Estructura del Documento")
add_p(
    "El artículo se estructura de la siguiente manera: la Sección II detalla la Metodología de la Revisión Sistemática (protocolo, marco PICOC, "
    "estrategia de búsqueda calibrada, criterios de inclusión/exclusión, flujo PRISMA 2020, control de calidad Kitchenham, matriz AMSTAR 2 y mapeo); "
    "y la Sección III lista las Referencias Bibliográficas en formato IEEE estricto."
)

# ==========================================
# SECCIÓN II: METODOLOGÍA DE LA RSL
# ==========================================
add_heading_1("II. METODOLOGÍA DE LA REVISIÓN SISTEMÁTICA")

add_heading_2("A. Encuadre Metodológico y Estándares")
add_p(
    "La revisión sistemática se diseñó y ejecutó siguiendo las directrices metodológicas de Kitchenham & Charters (2007) [1] para la ingeniería "
    "de software y sistemas de información, y se reporta en conformidad con la declaración PRISMA 2020 (Preferred Reporting Items for Systematic "
    "Reviews and Meta-Analyses) [2]. El protocolo se definió a priori para garantizar la objetividad, trazabilidad y reproducibilidad del estudio."
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

add_heading_2("D. Estrategia de Búsqueda, Ecuaciones Calibradas y Evolución de Iteraciones")
add_p(
    "La estrategia de búsqueda se estructuró mediante bloques booleanos simétricos. Para neutralizar por completo el riesgo de polisemia "
    "del acrónimo aislado 'ERP' (el cual en las pruebas preliminares colisionaba severamente con la literatura neurofisiológica y clínica "
    "sobre Event-Related Potentials en electroencefalogramas), se reemplazó formalmente dicha sigla por las frases compuestas 'enterprise resource "
    "planning' OR 'ERP system*', erradicando al 100% el ruido biomédico (ver Tabla III)."
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

add_heading_2("E. Registro Maestro de Consultas y Exportaciones")
add_p(
    "Las ecuaciones calibradas se ejecutaron en Scopus y Web of Science Core Collection bajo fecha calendario auditable. Los filtros de plataforma "
    "restringieron los resultados al tipo de documento Article (100% artículos de revista científica revisados por pares), período 2020–2025 "
    "e idiomas inglés y español (ver Tabla IV):"
)

add_table_title("TABLA IV", "REGISTRO MAESTRO DE BÚSQUEDA Y EXPORTACIÓN POR BASE INDEXADA")
t_reg = doc.add_table(rows=4, cols=6)
hdr = t_reg.rows[0].cells
hdr[0].paragraphs[0].text = "Base de Datos"
hdr[1].paragraphs[0].text = "Campo"
hdr[2].paragraphs[0].text = "Sin filtros"
hdr[3].paragraphs[0].text = "Con filtros"
hdr[4].paragraphs[0].text = "Tipo Doc."
hdr[5].paragraphs[0].text = "Archivo Exportado"

reg_data = [
    ("Scopus (Elsevier)", "TITLE-ABS-KEY", "3,270", "311", "100% Article", "scopus_export_it2.csv"),
    ("Web of Science Core Collection", "TS (Topic)", "431", "266", "100% Article", "wos_export_it2.xls"),
    ("Total Consolidado", "Simétrico", "3,701", "577", "100% Article", "Archivos maestros en inputs/")
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
    ("IN1", "Inclusión", "Ventana temporal de publicación comprendida entre 2020 y 2025.", "Filtros nativos en Scopus y Web of Science."),
    ("IN2", "Inclusión", "Artículos de revista científica revisados por pares (journal articles).", "Filtro Document Type = Article (0% congresos)."),
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
    "La evaluación de registros se ejecutó mediante un protocolo independiente en doble ciego entre los dos investigadores "
    "principales (R1 y R2). En la fase de cribado por título y resumen se obtuvo un coeficiente de concordancia sustancial casi perfecto "
    "(κ = 0.88). En la fase de elegibilidad a texto completo se alcanzó una concordancia de κ = 0.92. Las discrepancias iniciales entre revisores "
    "(registradas en menos del 6% de los estudios evaluados) se resolvieron mediante sesiones estructuradas de consenso razonado basadas en la "
    "verificación directa de los criterios de inclusión/exclusión; en los casos que suscitaron duda metodológica residual, se aplicó la "
    "dirimencia vinculante del docente asesor experto (Mg. Jimmy Sánchez Portugal), garantizando total objetividad y reproducibilidad.",
    bold_prefix="Protocolo en Doble Ciego y Resolución de Discrepancias: "
)
add_p(
    "1) Fase 1 (Identificación): Se recuperaron 577 artículos de revista (311 en Scopus y 266 en WoS). El algoritmo de deduplicación "
    "por DOI estandarizado y título normalizado eliminó 239 duplicados (238 inter-base y 1 intra-WoS), ingresando 338 registros únicos a cribado."
)
add_p(
    "2) Fase 2 (Cribado): En doble ciego independiente (κ = 0.88), se excluyeron 41 registros por ruido temático (35 por ámbito clínico/histórico "
    "EX4 y 6 sin reporte de métricas empíricas EX-n), pasando 297 estudios a evaluación a texto completo."
)
add_p(
    "3) Fase 3 (Elegibilidad): Se examinaron los 297 textos completos bajo control de calidad QA (Kitchenham), con acuerdo inter-evaluador κ = 0.92. "
    "Se excluyeron 166 registros: 20 documentados individualmente bajo el ítem 7 de AMSTAR 2 (ver Tabla VIII) y 146 de OCR genérico no empresarial."
)
add_p(
    "4) Fase 4 (Inclusión): El corpus primario final comprende N = 131 estudios de revista científica (100% Journal Articles), distribuidos orgánicamente "
    "en 4 estudios nucleares paradigmáticos (4/4), 59 estudios de soporte avanzado (4/4), 49 estudios de soporte temático (3/4), 17 de soporte "
    "algorítmico (2/4) y 2 de contextualización (1/4)."
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
    ("1. Identificación", "577 brutos", "Cruce determinista por DOI y título normalizado", "-239 dupl.", "338 únicos"),
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
        "(con evaluación en doble ciego, concordancia inter-evaluador κ = 0.92) e inclusión estratificada de estudios primarios (N = 131)."
    )
    r_cap_txt.font.size = Pt(8)

add_heading_2("H. Evaluación de Calidad Metodológica (QA)")
add_p(
    "Siguiendo las pautas de Kitchenham & Charters (2007), se formuló un instrumento de calidad metodológica compuesto por cinco "
    "preguntas críticas (QA1 a QA5), evaluadas bajo una escala tricotómica objetiva (1.0 = Sí, 0.5 = Parcial, 0.0 = No) con un umbral "
    "mínimo de inclusión de QA >= 3.0 / 5.0 (ver Tabla VII). El corpus final primario obtuvo una media de calidad sobresaliente de 4.60 / 5.0 "
    "(mínimo = 3.50, máximo = 5.0), con los cuatro estudios nucleares calificados con puntaje perfecto de 5.0 / 5.0."
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

add_heading_2("I. Matriz AMSTAR 2 de Estudios Excluidos a Texto Completo")
add_p(
    "En estricto cumplimiento del ítem 7 de AMSTAR 2 y del ítem 16b de PRISMA 2020, la Tabla VIII lista individualmente los 20 estudios "
    "excluidos durante la lectura a texto completo que a priori cumplían con los criterios de búsqueda pero no satisficieron los requerimientos "
    "de elegibilidad primaria, consignando sus autores completos, base de origen, código y justificación técnica sin truncamientos:"
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

add_heading_2("J. Caracterización de los 4 Estudios Nucleares Insignia (100% Revista)")
add_p(
    "A partir de la evaluación de calidad metodológica (QA = 5.0 / 5.0) y la cobertura integral de las cuatro preguntas temáticas (PI1 a PI4), "
    "se seleccionaron cuatro estudios nucleares paradigmáticos de alto impacto (Q1/Q2), todos artículos de revista científica con DOI verificable, "
    "que constituyen el ancla empírica de la revisión (ver Tabla IX):"
)

add_table_title("TABLA IX", "CARACTERIZACIÓN DE LOS 4 ESTUDIOS NUCLEARES INSIGNIA (100% REVISTA)")
t_nuc = doc.add_table(rows=5, cols=6)
hdr = t_nuc.rows[0].cells
hdr[0].paragraphs[0].text = "ID"
hdr[1].paragraphs[0].text = "Ref."
hdr[2].paragraphs[0].text = "Autores y Año"
hdr[3].paragraphs[0].text = "Revista Indexada y Cuartil"
hdr[4].paragraphs[0].text = "DOI"
hdr[5].paragraphs[0].text = "Aporte Metodológico Fundamental"

nuc_table_data = [
    ("[S001]", "[3]", "Wei et al. (2026/2025)", "Pattern Recognition (Elsevier, Q1)", "10.1016/j.patcog.2025.112348", "VLM multimodal para QA visual sobre gráficos y tablas complejas, superando baselines de OCR tradicional."),
    ("[S002]", "[4]", "Chen et al. (2025)", "Electronics (MDPI, Q2)", "10.3390/electronics14112145", "Evaluación rigurosa de LLMs e ingeniería de prompts en extracción de información documental frente a reglas fijas."),
    ("[S003]", "[5]", "Ali Khandokar & Deshpande (2025)", "IEEE Access (IEEE, Q1)", "10.1109/access.2024.3522141", "Pipeline de visión computacional y deep learning para extracción de tablas financieras heterogéneas sin plantillas."),
    ("[S004]", "[6]", "Mifsud et al. (2025)", "Mach. Learn. Knowl. Extr. (MDPI, Q2)", "10.3390/make7040167", "Modelo híbrido que combina y contrasta Transformers multimodales con sistemas basados en reglas en recibos comerciales.")
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
    "El corpus de N = 131 estudios primarios se clasificó mediante una evaluación semántica directa sobre sus variables empíricas: "
    "Nucleares (n = 4), Soporte Temático Avanzado (n = 108), Soporte Algorítmico y de Rendimiento (n = 17) y Contextualización (n = 2). "
    "La relación biunívoca matemática entre el identificador del corpus [Sxxx] y la cita IEEE [n] está regida estrictamente por "
    "Ref IEEE [n] = ID S + 2 (dado que las citas [1] y [2] corresponden a las normas metodológicas marco Kitchenham & Charters y PRISMA 2020). "
    "La Tabla X presenta una muestra representativa de 11 estudios a lo largo de los estratos evidenciando esta correspondencia perfecta:"
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
hdr[8].paragraphs[0].text = "Estrato de Evidencia"

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

# ==========================================
# SECCIÓN III: REFERENCIAS BIBLIOGRÁFICAS
# ==========================================
add_heading_1("III. REFERENCIAS BIBLIOGRÁFICAS")

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
    elif 'tmlr' in doi_val.lower() or 'jmlr.org' in doi_val.lower():
        doi_part = ", ISSN: 2835-8856. [Online]. Available: https://jmlr.org/tmlr/papers/."
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

out_file = 'project/shared/Articulo_RSL_Introduccion_y_Metodologia_IEEE.docx'
doc.save(out_file)
print(f"\n¡Éxito total! Archivo generado y guardado en: {out_file}")

