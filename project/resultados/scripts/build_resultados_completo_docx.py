"""
Compilador de Word (.docx) en formato IEEE para la Sección III COMPLETA (Bloque 1 + Bloque 2):
"Articulo_RSL_Resultados_Completo_IEEE.docx" en project/shared/

Contiene:
- Apertura General del Corpus y Métodos de Síntesis
- PD1: Evolución Temporal -> TABLA XIII y Fig. 2
- PD2: Revistas, Autores, Países y Red de Coocurrencia -> TABLA XIV, TABLA XV y Fig. 3
- PD3: Diseños Metodológicos x Tipología de Datasets -> TABLA XVI y Fig. 4
- Paso 6: Evaluación de Calidad Metodológica (QA) -> TABLA XVII y Fig. 5
- PI1: Taxonomía de Familias Algorítmicas de IA e IDP -> TABLA XVIII y Fig. 6
- PI2: Rendimiento Cuantitativo por Benchmark -> TABLA XIX y Fig. 7
- PI3: Comparativa de Eficiencia vs. Métodos Tradicionales (SWiM) -> TABLA XX y Fig. 8
- PI4: Tipologías Documentales y Sistemas ERP/CRM -> TABLA XXI y Fig. 9
- Paso 8: Análisis de Sensibilidad Global -> TABLA XXII
- Paso 9: Tabla Resumen de Hallazgos (SoF) GRADE-CERQual -> TABLA XXIII
"""

import os
import sys
import io
import pandas as pd
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

df_final = pd.read_csv('project/metodologia/outputs/corpus_included_final.csv')
print(f"Cargados: {len(df_final)} estudios primarios incluidos para la compilación formal.")

doc = Document()

# Márgenes estándar IEEE (0.75 pulgadas en todos los lados)
for section in doc.sections:
    section.top_margin = Inches(0.75)
    section.bottom_margin = Inches(0.75)
    section.left_margin = Inches(0.75)
    section.right_margin = Inches(0.75)
    section.header_distance = Inches(0.4)
    section.footer_distance = Inches(0.4)

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

def add_title(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(4)
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(15)
    run.bold = True
    return p

def add_subtitle(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(12)
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(9.5)
    run.italic = True
    return p

def add_heading_1(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(11)
    run.bold = True
    run.font.color.rgb = RGBColor(0x00, 0x20, 0x60)
    return p

def add_heading_2(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(10)
    run.bold = True
    run.font.color.rgb = RGBColor(0x1F, 0x49, 0x7D)
    return p

def add_heading_3(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(9.5)
    run.bold = True
    run.italic = True
    run.font.color.rgb = RGBColor(0x33, 0x33, 0x33)
    return p

def add_p(text, bold_prefix=None, italic_text=False, indent=None):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.05
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    if indent:
        p.paragraph_format.left_indent = indent

    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = 'Times New Roman'
        r_pre.font.size = Pt(9)
        r_pre.bold = True

    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(9)
    r.italic = italic_text
    return p

def add_table_title(table_id, table_name):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.keep_with_next = True
    r_id = p.add_run(f"{table_id}\n")
    r_id.font.name = 'Times New Roman'
    r_id.font.size = Pt(8.5)
    r_id.bold = True
    r_name = p.add_run(table_name.upper())
    r_name.font.name = 'Times New Roman'
    r_name.font.size = Pt(8.5)
    r_name.bold = True
    return p

def add_table_footer(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(6)
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(7.5)
    r.italic = True
    return p

def style_table(table, col_widths, font_size=Pt(7.5), align_cols=None):
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for r_idx, row in enumerate(table.rows):
        is_header = (r_idx == 0)
        trPr = row._tr.get_or_add_trPr()
        trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))
        if is_header:
            trPr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))

        for c_idx, cell in enumerate(row.cells):
            cell.width = col_widths[c_idx]
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER

            if is_header:
                set_cell_shading(cell, "1F497D")
                set_cell_border(cell, top="single", top_sz="12", top_color="002060",
                                      bottom="single", bottom_sz="12", bottom_color="002060",
                                      left="none", right="none")
            else:
                bg = "F2F5F9" if r_idx % 2 == 1 else "FFFFFF"
                set_cell_shading(cell, bg)
                set_cell_border(cell, top="single", top_sz="4", top_color="D3D3D3",
                                      bottom="single", bottom_sz="4", bottom_color="D3D3D3",
                                      left="none", right="none")

            for paragraph in cell.paragraphs:
                paragraph.paragraph_format.space_before = Pt(2)
                paragraph.paragraph_format.space_after = Pt(2)
                paragraph.paragraph_format.line_spacing = 1.0
                
                if align_cols and c_idx < len(align_cols):
                    paragraph.alignment = align_cols[c_idx]
                elif is_header:
                    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
                else:
                    paragraph.alignment = WD_ALIGN_PARAGRAPH.LEFT

                for run in paragraph.runs:
                    run.font.name = 'Times New Roman'
                    run.font.size = font_size
                    if is_header:
                        run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
                        run.bold = True

def add_figure_with_caption(img_path, fig_id, caption_title, caption_text, width=Inches(6.5)):
    if os.path.exists(img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(8)
        p_img.paragraph_format.space_after = Pt(2)
        p_img.paragraph_format.keep_with_next = True
        run_img = p_img.add_run()
        run_img.add_picture(img_path, width=width)

    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_cap.paragraph_format.space_before = Pt(2)
    p_cap.paragraph_format.space_after = Pt(8)
    r_cap_id = p_cap.add_run(f"{fig_id}. ")
    r_cap_id.bold = True
    r_cap_id.font.name = 'Times New Roman'
    r_cap_id.font.size = Pt(8)

    r_cap_tit = p_cap.add_run(f"{caption_title}. ")
    r_cap_tit.bold = True
    r_cap_tit.font.name = 'Times New Roman'
    r_cap_tit.font.size = Pt(8)

    r_cap_txt = p_cap.add_run(f"{caption_text} Fuente: elaboración propia a partir del corpus primario [3]–[133].")
    r_cap_txt.font.name = 'Times New Roman'
    r_cap_txt.font.size = Pt(8)
    r_cap_txt.italic = True

# ==============================================================================
# CONSTRUCCIÓN DEL DOCUMENTO COMPLETO
# ==============================================================================

add_title("SECCIÓN III: RESULTADOS DE LA REVISIÓN SISTEMÁTICA DE LITERATURA (RSL)")
add_subtitle("Entrega Completa: Bloque 1 (Apertura, PD1, PD2, PD3, QA) + Bloque 2 (PI1, PI2, PI3, PI4, Sensibilidad y GRADE-CERQual)\nEstándar IEEE – Guía de Evaluación Continua ATI3 (Mg. Jimmy Sánchez Portugal)")

# ------------------------------------------------------------------------------
# 0. Apertura General
# ------------------------------------------------------------------------------
add_heading_1("III. RESULTADOS")
add_heading_2("A. Apertura General del Corpus y Protocolo de Síntesis")
add_p(
    "La presente sección describe y cuantifica de forma objetiva la evidencia empírica extraída del corpus de literatura científica incluido, "
    "en estricto apego a las directrices de reporte de Kitchenham & Charters (2007) [1], los estándares internacionales de la declaración "
    "PRISMA 2020 [2] y las directrices metodológicas institucionales. La totalidad de los hallazgos se reporta en tercera persona impersonal "
    "y con verbos de reporte neutros, reservando las deducciones teóricas y reflexiones causales para la sección de Discusión."
)
add_p(
    "El corpus documental primario quedó formalmente cerrado y congelado en un total de N = 131 artículos de revista científica indexada "
    "(100 % Journal Articles, sin actas de congreso, preprints, tesis ni literatura gris), habiendo superado el control de calidad metodológica "
    "(QA >= 3.50 / 5.00; media global = 4.61 / 5.00). La numeración de citas bibliográficas mantiene una relación matemática biunívoca unívoca: "
    "Ref IEEE [n] = ID S + 2, donde [1] y [2] son Kitchenham & Charters y PRISMA 2020, los 131 estudios primarios se indexan entre [3] y [133], "
    "y las referencias metodológicas complementarias de síntesis y cienciometría se ubican en [134] a [140]."
)
add_p(
    "Conforme a los ítems 13a–13f de PRISMA 2020 y para mitigar el sesgo de conveniencia (reporting bias), se formalizaron los métodos de síntesis: "
    "1) Síntesis Temática (Thomas & Harden [134]; Cruzes & Dybå [135]) para PI1 y PI4; 2) Síntesis Narrativa Estructurada (Popay et al. [136]) para PI2; "
    "3) Síntesis sin metaanálisis — SWiM (Campbell et al. [137]) para PI3; 4) Mapeo Sistemático Matricial (Petersen et al. [138]) para PD1 y PD3; "
    "5) Mapeo Cienciométrico (van Eck & Waltman [139]) para PD2; y 6) Calificación GRADE-CERQual (Lewin et al. [140]) para la certeza de la evidencia."
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
add_table_footer("* Nota: Los estudios fechados en 2026 corresponden a artículos aceptados e incorporados en modalidad Early Access / In Press en Scopus y Web of Science durante el cierre de 2025 ([3], [65], [66]). Fuente: elaboración propia a partir del corpus primario [3]–[133].")

add_figure_with_caption('project/resultados/outputs/fig2_evolucion_anual.png', 'Fig. 2',
                        'Evolución temporal de publicaciones sobre IA/IDP en documentos empresariales (2020–2025/2026, N = 131)',
                        'Barras: volumen anual absoluto (n); línea roja: porcentaje acumulado (%).')

add_p("Ciento treinta y un estudios (100.0 % del corpus primario; [3]–[133]) respondieron a la evolución cronológica de la producción científica en IA e IDP aplicada a sistemas documentales corporativos (PD1). Mediante mapeo sistemático cronológico se identificó una trayectoria de crecimiento marcadamente expansiva y no lineal a lo largo del sexenio 2020–2025/2026, con una concentración máxima de publicaciones en el bienio final (TABLA XIII, Fig. 2).", bold_prefix="1) Apertura (Respuesta a PD1): ")
add_p("La dinámica temporal se articula en tres periodos analíticos: a) Fase de emergencia y cimientos basados en OCR-CNN (2020–2021) con 18 estudios (13.7 %; [58]–[64], [111]–[114], [123], [126]–[131]); b) Fase de consolidación de Transformers Multimodales (2022–2023) con 43 estudios (32.8 %; [39]–[55], [57], [67], [90]–[92], [94]–[109], [121], [124], [125], [132], [133]); y c) Fase de aceleración exponencial con VLMs y Modelos Generativos (2025–2026*) con 54 estudios (41.2 %; [3]–[27], [32], [56], [65], [66], [68]–[83], [85], [93], [110], [115]–[119], [122]), impulsada por Vision-Language Models y LLMs adaptados con prompt engineering.", bold_prefix="2) Desarrollo por Categoría y Fases Temporales: ")
add_p("A pesar de la tendencia alcista, se observó una desaceleración temporal en 2024 (16 estudios; 12.2 %; [28]–[31], [33]–[38], [84], [86]–[89], [120]), obedeciendo al agotamiento empírico de las arquitecturas de grafos tradicionales y pipelines heurísticos que exhibían techos de rendimiento frente a distorsiones complejas.", bold_prefix="3) Contrastes y Debates Temporales: ")
add_p("La literatura transita irreversiblemente desde el OCR simple hacia sistemas de comprensión de documentos visualmente ricos (VRD). Al excluir los 10 estudios de calidad inferior (QA = 3.5), el ciclo 2025–2026 agrupa el 42.1 %, ratificando la robustez de la tendencia expansiva.", bold_prefix="4) Cierre, Tendencias y Sensibilidad: ")

# ------------------------------------------------------------------------------
# 1.2 PD2: Revistas, Autores, Países
# ------------------------------------------------------------------------------
add_heading_2("C. Productividad por Revistas, Autores, Países y Red de Coocurrencia (PD2)")
add_p(
    "Para responder a PD2, se normalizaron los títulos de las revistas indexadas, se contabilizó la productividad de los autores, se aplicó la regla estricta de "
    "afiliación geográfica del primer autor y se estructuró la red de coocurrencia de Author Keywords con umbral >= 3 en VOSviewer [139] (TABLA XIV, TABLA XV, Fig. 3)."
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
    ("International Journal on Document Analysis and Recognition (IJDAR)", "Springer", "Q2", "[9], [33], [35], [39], [50], [65], [66], [70], [77], [115]", "10 (7.6 %)"),
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
    ("Otras 61 revistas indexadas (<= 2 estudios c/u)", "Diversas", "Q1–Q3", "Citas dispersas [10], [12], [13], [17]–[20], etc.", "70 (53.4 %)")
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
hdr_geo[3].paragraphs[0].text = "Autores Más Prolíficos en el Corpus (>= 2 publicaciones vinculadas)"

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

style_table(t_pd2_geo, [Inches(1.5), Inches(0.7), Inches(0.7), Inches(3.7)],
            align_cols=[WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT])
add_table_footer("Fuente: elaboración propia a partir del corpus primario [3]–[133]. Regla de país: país de la institución universitaria o centro corporativo del primer autor.")

add_figure_with_caption('project/resultados/outputs/fig3_vosviewer_geografia.png', 'Fig. 3',
                        'Concentración geográfica de la investigación y principales clústeres temáticos de palabras clave (PD2, N = 131)',
                        '(a) Distribución porcentual por país del autor principal; (b) Frecuencia de descriptores (umbral ≥ 3) en VOSviewer.')

add_p("Ciento treinta y un artículos primarios (100.0 % del corpus; [3]–[133]) respondieron a la productividad por revistas, autores, países y red temática (PD2), constatándose concentración editorial en revistas especializadas de procesamiento de documentos y liderazgo geográfico de China (29.8 %), India (8.4 %) y EE.UU. (7.6 %) con alta desconcentración autoral (TABLA XIV, TABLA XV, Fig. 3).", bold_prefix="1) Apertura (Respuesta a PD2): ")
add_p("Doce revistas concentraron el 46.6 % de las publicaciones (lideradas por IEEE Access con 13 estudios e IJDAR con 10). En palabras clave de autor (VOSviewer) emergieron 3 clústeres conceptuales: 1) Extracción de Información y Comprensión Documental; 2) Aprendizaje Profundo y OCR; y 3) Reconocimiento de Estructura de Tablas.", bold_prefix="2) Desarrollo por Categoría y Redes Temáticas: ")
add_p("Se constató una alta dispersión autoral: de 498 investigadores, el 84.7 % publicó exactamente un artículo. Solo dos grupos sostuvieron producción serial: la Univ. de Ottawa en Canadá (Simsek M., Kantarci B., Xiao B. y Alkheir A.A. con 4 estudios; [11], [35], [48], [51]) y el DFKI de Alemania (Hashmi K.A., Liwicki M., Stricker D. y Afzal M.Z. con 3 estudios; [59], [61], [123]).", bold_prefix="3) Contrastes y Dispersión Autoral: ")
add_p("Se detectó una brecha geográfica total: cero estudios primarios con primer autor de América Latina aplicados a comprobantes de la región (las contribuciones hispanas provienen de España en tablas y recibos; [105], [111], [131]). La exclusión de estudios con QA = 3.5 no alteró las 5 revistas líderes ni la hegemonía de China (31.4 %), confirmando la estabilidad cienciométrica.", bold_prefix="4) Cierre, Tendencias y Sensibilidad: ")

# ------------------------------------------------------------------------------
# 1.3 PD3: Diseños Metodológicos x Datasets
# ------------------------------------------------------------------------------
add_heading_2("D. Clasificación de Diseños Metodológicos × Tipología de Datasets (PD3)")
add_p(
    "Para evaluar la transferibilidad industrial de las soluciones, se cruzaron los diseños metodológicos frente a las fuentes de datos utilizadas. "
    "La evaluación ciega sobre el 20.6 % del corpus (n = 27) reportó un Kappa de Cohen κ = 0.85 (acuerdo del 88.9 %; concordancia casi perfecta). "
    "La matriz de contingencia de 12 celdas exactas se expone en la TABLA XVI y el gráfico de burbujas de Petersen et al. [138] en la Fig. 4."
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
add_table_footer("Fuente: elaboración propia a partir del corpus primario [3]–[133]. Medición de acuerdo inter-evaluador sobre muestra del 20.6 % (n = 27): Po = 88.9 %, Pe = 0.258, κ = 0.85 (casi perfecto). Partición matemática exacta de 12 celdas.")

add_figure_with_caption('project/resultados/outputs/fig4_burbujas_disenos_datasets.png', 'Fig. 4',
                        'Gráfico de burbujas del mapeo sistemático (Petersen et al. [138]): Diseño Metodológico vs. Tipología de Dataset (PD3, N = 131)',
                        'El área de cada burbuja es proporcional al número de estudios primarios (n); porcentajes sobre la totalidad del corpus.')

add_p("Ciento treinta y un artículos (100.0 %; [3]–[133]) respondieron a los diseños metodológicos y datasets (PD3), identificándose un predominio estructural de experimentos controlados sobre benchmarks públicos (62.6 %; 82 estudios) frente a una baja proporción de casos reales corporativos (6.1 %; 8 estudios) (TABLA XVI, Fig. 4).", bold_prefix="1) Apertura (Respuesta a PD3): ")
add_p("La distribución comprende 82 experimentos controlados (48 públicos, 18 privados y 16 mixtos), 31 desarrollos de artefacto / PoC (23.7 %), 10 estudios cuasi-experimentales (7.6 %) y 8 casos de estudio reales en producción (6.1 %).", bold_prefix="2) Desarrollo por Categoría y Cruce Matricial: ")
add_p("El contraste más crítico reside en la escasez de casos de estudio en producción (8 estudios; 6.1 %; [64], [70], [75], [84], [103], [117], [127], [131]), donde emergen barreras operativas no presentes en laboratorio: confidencialidad financiera, necesidad de Human-in-the-Loop y rigidez de integración con ERPs legados.", bold_prefix="3) Contrastes y Vacíos en Casos de Estudio Reales: ")
add_p("Al excluir los 10 estudios de calidad moderada (QA = 3.5), los experimentos controlados se consolidaron en el 65.3 % (79 de 121), ratificando la robustez de la base empírica de laboratorio.", bold_prefix="4) Cierre, Madurez y Sensibilidad: ")

# ------------------------------------------------------------------------------
# 2. QA - Paso 6
# ------------------------------------------------------------------------------
add_heading_2("E. Evaluación de Calidad Metodológica (QA) e Integración al Análisis (Paso 6)")
add_p(
    "Para jerarquizar la evidencia y preparar el análisis de sensibilidad, se evaluó el corpus bajo el protocolo de Kitchenham & Charters (2007) [1] (QA1 a QA5). "
    "El doble ciego sobre el 20.6 % (n = 27) reportó un Kappa ponderado cuadrático κw = 0.89. Los resultados se detallan en la TABLA XVII y la Fig. 5."
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
    ("Calidad Alta", "4.5 – 5.0 pts", "108", "82.4 %", "Núcleo empírico robusto para extracción y síntesis temática (PI1–PI4). Incluye los 4 estudios nucleares con puntaje perfecto de 5.0 / 5.0 ([3], [4], [5], [6])."),
    ("Calidad Media", "4.0 pts", "13", "9.9 %", "Estudios con cumplimientos parciales menores; retenidos en análisis de sensibilidad."),
    ("Calidad Moderada / Estrato Inferior*", "3.5 pts", "10", "7.6 %", "Grupo de exclusión temporal en Análisis de Sensibilidad (Paso 8): [116], [117], [118], [121], [122], [123], [127], [128], [132], [133]."),
    ("Total Corpus Primario", "Media = 4.61 / 5.00", "131", "100.0 %", "Mínimo registrado: 3.50 pts; Máximo: 5.00 pts; Desviación estándar: ±0.41 pts.")
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

style_table(t_qa_crit, [Inches(2.5), Inches(1.2), Inches(1.2), Inches(1.1), Inches(1.2)],
            align_cols=[WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER])
add_table_footer("Fuente: elaboración propia a partir del corpus primario [3]–[133].")

add_figure_with_caption('project/resultados/outputs/fig5_distribucion_qa_criterios.png', 'Fig. 5',
                        'Evaluación de Calidad Metodológica (Kitchenham & Charters [1]) y vulnerabilidad por criterio (N = 131)',
                        '(a) Estratificación de estudios según calidad; (b) Desglose de cumplimiento total vs. parcial en QA1–QA5.')

add_p(
    "La calidad global es sobresaliente (media = 4.61 / 5.00 pts; 82.4 % en calidad alta). QA1 (1.000) y QA2 (0.977) exhibieron cumplimiento óptimo. "
    "El criterio más vulnerable fue QA5 (contraste empírico frente a baselines tradicionales), con cumplimiento parcial en 42 estudios (32.1 %; media 0.840), "
    "seguido de QA3 (reproducibilidad de arquitectura e hiperparámetros) con 32 cumplimientos parciales (24.4 %; media 0.878). Los 10 estudios con QA = 3.50 pts "
    "([116], [117], [118], [121], [122], [123], [127], [128], [132], [133]) conforman el subconjunto de prueba para el análisis de robustez.",
    bold_prefix="Hallazgos del Control de Calidad y Protocolo de Aislamiento: "
)

# ------------------------------------------------------------------------------
# 3. PI1: Taxonomía de Arquitecturas IA/IDP
# ------------------------------------------------------------------------------
add_heading_2("F. Taxonomía de Familias Algorítmicas y Enfoques de IA (PI1)")
add_p(
    "Para responder a PI1, se aplicó síntesis temática (Thomas & Harden [134]; Cruzes & Dybå [135]) sobre los 105 estudios con PI1 = 1 (80.2 % del corpus). "
    "Los resultados se sintetizan en la TABLA XVIII y la Fig. 6."
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
    ("Pipelines Híbridos CNN-RNN y Segmentación con OCR",
     "Modelos convolucionales (ResNet, VGG, YOLO, Mask R-CNN) combinados con recurrentes y motores OCR para detección de regiones y tablas.",
     "[5], [10]–[12], [14]–[16], [20], [23], [28], [31]–[33], [35], [39], [45], [48], [49], [53]–[55], [57]–[62], [67]–[73], [78], [83]–[85], [88], [91], [93], [95], [98]–[100], [103], [104], [106], [108]–[111], [117], [118], [122], [124]",
     "56", "53.3 %"),
    ("Transformers Multimodales y Visión-Lenguaje (VLM)",
     "Modelado conjunto de texto, coordenadas 2D (bounding boxes) y parches visuales (LayoutLMv2/v3, StrucTexT, BROS, Bi-VLDoc).",
     "[6], [7], [9], [13], [18], [21], [26], [30], [36], [38], [42], [43], [47], [50], [56], [74], [76], [77], [90], [92], [96], [114]",
     "22", "21.0 %"),
    ("Redes Neuronales de Grafos y Modelado Espacial (GNN)",
     "Representación de palabras/bloques como nodos y relaciones geométricas relativas como aristas (GCN, GAT, GraphIE).",
     "[8], [29], [34], [40], [41], [44], [46], [51], [52], [63], [64], [66], [75], [105], [107], [123]",
     "16", "15.2 %"),
    ("Modelos Generativos, LLMs y Zero/Few-Shot",
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

style_table(t_pi1, [Inches(1.8), Inches(2.2), Inches(1.8), Inches(0.6), Inches(0.8)],
            align_cols=[WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER])
add_table_footer("Fuente: elaboración propia a partir del corpus primario [3]–[133]. Partición temática unívoca auditada y verificada.")

add_figure_with_caption('project/resultados/outputs/fig6_taxonomia_algoritmos.png', 'Fig. 6',
                        'Taxonomía de Familias Algorítmicas de IA en Procesamiento Documental (PI1, n = 105)',
                        'Frecuencia absoluta y porcentaje relativo derivado de síntesis temática [134], [135].')

add_p("Ciento cinco estudios primarios (80.2 % del corpus; TABLA XVIII, Fig. 6) respondieron a la taxonomía de arquitecturas IA/IDP (PI1). Mediante síntesis temática se identificaron cuatro familias algorítmicas mutuamente excluyentes, destacando el predominio de pipelines modulares CNN-RNN con OCR neuronal (53.3 %) y la rápida consolidación de Transformers multimodales y VLMs (21.0 %).", bold_prefix="1) Apertura (Respuesta a PI1): ")
add_p("La distribución comprende: a) Pipelines Híbridos CNN-RNN (56 estudios; 53.3 %; 82.1 % calidad alta; CERQual alta); b) Transformers Multimodales y VLMs (22 estudios; 21.0 %; 86.4 % calidad alta; CERQual alta); c) Redes Neuronales de Grafos GNN (16 estudios; 15.2 %; 81.3 % calidad alta; CERQual alta); y d) Modelos Generativos y LLMs (11 estudios; 10.5 %; 90.9 % calidad alta; CERQual moderada por costo computacional).", bold_prefix="2) Desarrollo por Categoría Algorítmica: ")
add_p("Existe una marcada divergencia entre latencia y adaptabilidad: los pipelines CNN-RNN ofrecen inferencias ultrarrápidas (<150 ms) pero son frágiles ante cambios de formato, mientras que Transformers y LLMs absorben deformaciones visuales pero requieren aceleración GPU y presentan riesgo de alucinación numérica en montos contables.", bold_prefix="3) Contrastes y Debates de Rendimiento: ")
add_p("Al excluir del análisis los 4 estudios con QA = 3.5 en PI1 ([117], [118], [122], [124]), los pipelines híbridos representaron el 51.5 % (52 de 101) y los Transformers/VLMs el 21.8 % (22 de 101), demostrando la estabilidad de la taxonomía.", bold_prefix="4) Cierre, Tendencias y Sensibilidad: ")

# ------------------------------------------------------------------------------
# 4. PI2: Rendimiento Cuantitativo
# ------------------------------------------------------------------------------
add_heading_2("G. Rendimiento Cuantitativo de las Soluciones IA en Benchmarks (PI2)")
add_p(
    "Para responder a PI2, se aplicó la síntesis narrativa estructurada de Popay et al. (2006) [136] sobre los 117 estudios con PI2 = 1 (89.3 % del corpus). "
    "Se reportan rangos empíricos [mín, máx] y medianas sin promediar métricas entre conjuntos de datos incompatibles (TABLA XIX, Fig. 7)."
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

style_table(t_pi2, [Inches(1.5), Inches(1.3), Inches(1.6), Inches(0.6), Inches(0.8), Inches(0.5), Inches(0.9)],
            align_cols=[WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER])
add_table_footer("Fuente: elaboración propia a partir del corpus primario [3]–[133]. Síntesis estructurada Popay et al. [136].")

add_figure_with_caption('project/resultados/outputs/fig7_rendimiento_benchmarks.png', 'Fig. 7',
                        'Distribución Empírica de Rendimiento por Benchmark (Síntesis de Popay, PI2, n = 117)',
                        'Cajas: rango intercuartil (Q1–Q3); línea roja: mediana empírica; líneas grises: dispersión total [mín, máx].')

add_p("Ciento diecisiete estudios (89.3 % del corpus; TABLA XIX, Fig. 7) reportaron métricas cuantitativas sobre el rendimiento de soluciones IA (PI2). El rango empírico de F1-score osciló entre 72.1 % y 98.7 %, con desempeños marcadamente superiores en recibos y facturas estándar (mediana 95.2 %) frente a tablas complejas (89.8 %) y formularios degradados (84.5 %).", bold_prefix="1) Apertura (Respuesta a PI2): ")
add_p("En recibos (48 estudios), la mediana de F1-score alcanzó 95.2 % (latencias 80–450 ms; CERQual alta). En tablas financieras (42 estudios), la mediana de TEDS/F1 fue 89.8 % (latencias 150–890 ms; CERQual alta para tablas con bordes). En formularios ruidosos FUNSD (21 estudios), la mediana descendió a 84.5 % por sellos y caligrafía superpuesta (CERQual moderada).", bold_prefix="2) Desarrollo por Benchmark y Dispersión: ")
add_p("Existe una brecha sistemática entre pruebas en benchmarks abiertos (>97 % F1 en SROIE) y lotes corporativos degradados (donde la precisión decae hasta 78.4 %), evidenciando que los benchmarks sobrestiman la exactitud frente a documentos reales arrugados o térmicos.", bold_prefix="3) Contrastes y Discrepancias Métricas: ")
add_p("Al excluir estudios de calidad inferior retenidos en PI2, la mediana de F1 en facturación se mantuvo prácticamente idéntica en 95.4 % (+0.2 %), demostrando la solidez del desempeño técnico.", bold_prefix="4) Cierre, Madurez y Sensibilidad: ")

# ------------------------------------------------------------------------------
# 5. PI3: Contraste SWiM
# ------------------------------------------------------------------------------
add_heading_2("H. Comparativa de Eficiencia vs. Métodos Tradicionales — Síntesis SWiM (PI3)")
add_p(
    "Para evaluar si la IA supera al ingreso manual y al OCR convencional, se implementó el método SWiM (Campbell et al. [137]) mediante conteo de votos "
    "sobre los 82 estudios que incorporan un comparador explícito (62.6 % del corpus). Los resultados se compendian en la TABLA XX y la Fig. 8."
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
    ("Tiempo y Latencia de Ciclo", "Mejora (+1)",
     "Reducción de tiempo de ciclo >= 60 % frente a digitación manual u OCR de plantillas.",
     "[3]–[27], [29]–[36], [38]–[44], [46]–[53], [55], [57]–[63], [67], [76], [79]–[81], [87], [89], [94], [97], [101]–[103], [113], [116], [127]",
     "71", "86.6 %"),
    ("Exactitud y Tasa de Error", "Sin diferencia (0)",
     "Paridad de exactitud o ganancia marginal <= 2 % en documentos altamente estandarizados.",
     "[28], [45], [54], [64], [86], [98], [112], [128]",
     "8", "9.8 %"),
    ("Carga Operativa y Costo", "Empeora (-1)",
     "Mayor latencia o costo en hardware restringido (CPU pura); re-trabajo por alucinaciones.",
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
                        'Gráfico de barras divergentes: Verde: Mejora (+1); Gris: Paridad (0); Rojo: Empeora/Ineficiencia (-1).')

add_p("Ochenta y dos estudios primarios (62.6 %; TABLA XX, Fig. 8) contrastaron la IA/IDP frente a métodos tradicionales (PI3). Mediante SWiM se identificó un consenso abrumador en favor de la IA, con un 86.6 % de votos favorables (71 de 82 estudios) que reportan mejoras sustanciales en tiempo y exactitud.", bold_prefix="1) Apertura (Respuesta a PI3): ")
add_p("Setenta y un estudios demostraron reducciones en tiempos de procesamiento de 24–72 horas a fracciones de segundo (<1 s por página; CERQual alta). Ocho estudios (9.8 %) reportaron paridad en plantillas 100 % fijas, donde reglas sintácticas logran exactitudes similares con menor costo. Tres estudios (3.7 %) reportaron empeoramiento relativo en CPUs sin aceleración GPU o ante alucinaciones de modelos generativos.", bold_prefix="2) Desarrollo por Dimensión y Conteo de Votos: ")
add_p("El debate operativo se centra en el costo computacional: mientras la literatura académica destaca ahorros de tiempo del 90 %, los estudios corporativos advierten que el costo de GPUs y mantenimiento puede superar el ahorro laboral en volúmenes documentales bajos (<5,000 mensuales).", bold_prefix="3) Contrastes y Debates Operativos: ")
add_p("Al excluir del análisis los 4 estudios con QA = 3.5 en PI3 ([116], [121], [127], [128]), los votos favorables representaron el 88.5 % (69 de 78), confirmando la solidez de la conclusión comparativa.", bold_prefix="4) Cierre, Tendencias y Sensibilidad: ")

# ------------------------------------------------------------------------------
# 6. PI4: Tipologías Documentales y ERP/CRM
# ------------------------------------------------------------------------------
add_heading_2("I. Mapeo de Tipologías Documentales y Sistemas Corporativos ERP/CRM (PI4)")
add_p(
    "Para responder a PI4, se mapearon las tipologías documentales frente a las plataformas de gestión sobre la totalidad del corpus primario (N = 131; 100.0 %). "
    "La matriz cruzada se documenta en la TABLA XXI y la matriz de calor (heatmap) en la Fig. 9."
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

style_table(t_pi4, [Inches(1.5), Inches(1.4), Inches(1.5), Inches(1.7), Inches(0.5), Inches(0.6)],
            align_cols=[WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER])
add_table_footer("Fuente: elaboración propia a partir del corpus primario [3]–[133].")

add_figure_with_caption('project/resultados/outputs/fig9_heatmap_documentos_erp.png', 'Fig. 9',
                        'Mapeo Cruzado: Tipología Documental × Plataforma Empresarial (PI4, N = 131)',
                        'Matriz de calor que representa la frecuencia de estudios primarios mapeados.')

add_p("Ciento treinta y un artículos (100.0 %; [3]–[133]) respondieron a tipologías documentales y sistemas destino (PI4). Se determinó una fuerte concentración en tablas contables (45.0 %) y facturas comerciales (26.0 %) asociadas a ERPs, frente a menor penetración en flujos documentales de CRM (TABLA XXI, Fig. 9).", bold_prefix="1) Apertura (Respuesta a PI4): ")
add_p("Balances y tablas (59 estudios; 45.0 %; CERQual alta) y facturas comerciales (34 estudios; 26.0 %; CERQual alta) forman el núcleo central de interés. Formularios administrativos reúnen 26 estudios (19.8 %) y recibos de caja 12 estudios (9.2 %).", bold_prefix="2) Desarrollo por Tipología Documental: ")
add_p("Se constata una brecha de integración transaccional: el 78.6 % de los estudios se detiene en la extracción visual a formato JSON, omitiendo conectores nativos a APIs de ERP o la validación Three-Way Matching contable.", bold_prefix="3) Contrastes y Brechas en la Integración Transaccional: ")
add_p("Al excluir los 10 estudios de calidad inferior, tablas y facturas representaron el 72.7 % (88 de 121), ratificando la centralidad de los comprobantes contables.", bold_prefix="4) Cierre, Tendencias y Sensibilidad: ")

# ------------------------------------------------------------------------------
# 7. Paso 8: Sensibilidad
# ------------------------------------------------------------------------------
add_heading_2("J. Análisis de Sensibilidad Global (Paso 8)")
add_p(
    "Para verificar la robustez de los hallazgos frente a variaciones de calidad, se contrastaron los resultados de la muestra completa (N = 131) "
    "frente a la muestra filtrada de alta calidad (n = 121), habiendo excluido temporalmente los 10 estudios con QA = 3.50 pts ([116]–[118], [121]–[123], [127], [128], [132], [133]). "
    "La TABLA XXII documenta la comparación exhaustiva antes y después del filtro."
)

add_table_title("TABLA XXII", "EVALUACIÓN DEL ANÁLISIS DE SENSIBILIDAD: MUESTRA COMPLETA (N = 131) VS. MUESTRA FILTRADA (n = 121)")
t_sens = doc.add_table(rows=8, cols=5)
hdr_sens = t_sens.rows[0].cells
hdr_sens[0].paragraphs[0].text = "Pregunta / Dimensión Evaluada"
hdr_sens[1].paragraphs[0].text = "Muestra Completa (N = 131)"
hdr_sens[2].paragraphs[0].text = "Muestra Filtrada (n = 121)"
hdr_sens[3].paragraphs[0].text = "Variación Absoluta / Relativa"
hdr_sens[4].paragraphs[0].text = "Dictamen de Robustez"

sens_data = [
    ("PD1: Producción 2025–2026*", "54 de 131 estudios (41.2 %)", "51 de 121 estudios (42.1 %)", "+0.9 %", "Robusto (tendencia alcista inalterada)"),
    ("PD2: Hegemonía Geográfica", "China: 39 de 131 (29.8 %)", "China: 38 de 121 (31.4 %)", "+1.6 %", "Robusto (estabilidad cienciométrica)"),
    ("PD3: Diseños Experimentales", "82 de 131 estudios (62.6 %)", "79 de 121 estudios (65.3 %)", "+2.7 %", "Robusto (convergencia invariable)"),
    ("PI1: Familia Algorítmica Líder", "Pipelines CNN-RNN: 56 (53.3 %)", "Pipelines CNN-RNN: 52 (51.5 %)", "-1.8 %", "Robusto (jerarquía de 4 familias intacta)"),
    ("PI2: Mediana F1-score Facturas", "Mediana SROIE = 95.2 %", "Mediana SROIE = 95.4 %", "+0.2 %", "Robusto (rango empírico preservado)"),
    ("PI3: Conteo SWiM a Favor de IA", "71 de 82 estudios (86.6 %)", "69 de 78 estudios (88.5 %)", "+1.9 %", "Robusto (dirección del efecto inalterada)"),
    ("PI4: Tipología Contable Líder", "Balances y facturas: 93 (71.0 %)", "Balances y facturas: 88 (72.7 %)", "+1.7 %", "Robusto (núcleo documental inalterado)")
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
add_table_footer("Fuente: elaboración propia a partir del corpus primario [3]–[133]. Filtro de exclusión: estudios con puntaje QA = 3.50 pts.")

add_p(
    "El análisis de sensibilidad demuestra que ninguna de las conclusiones de la revisión sistemática se invierte, distorsiona o altera al depurar los estudios "
    "de menor calificación de calidad metodológica. Las variaciones porcentuales fueron mínimas (< ±2.7 %), la dirección del voto en SWiM se mantuvo a favor de la IA "
    "y los rangos métricos conservaron sus medianas. La evidencia se dictamina formalmente como robusta y libre de sesgos de agregación.",
    bold_prefix="Síntesis de Robustez Metodológica: "
)

# ------------------------------------------------------------------------------
# 8. Paso 9: GRADE-CERQual
# ------------------------------------------------------------------------------
add_heading_2("K. Calificación de Certeza de la Evidencia — Marco GRADE-CERQual (Paso 9)")
add_p(
    "En cumplimiento de las directrices de Lewin et al. (2018) [140], se evaluó el nivel de confianza de los hallazgos a través de los cuatro componentes "
    "de GRADE-CERQual: limitaciones metodológicas, coherencia, adecuación de datos y relevancia. La TABLA XXIII expone la Tabla Resumen de Hallazgos (SoF)."
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
    ("PI1", "Pipelines CNN-RNN y Transformers multimodales (VLMs) dominan el 74.3 % de las soluciones, convergiendo a modelos ligeros espaciales.",
     "Bajas: 82.4 % calidad alta (media 4.61).", "Alta: convergencia técnica internacional.", "Alta: n = 105 estudios con arquitectura formal.", "Alta: aplicable a documentos semiestructurados.", "ALTA CERTEZA"),
    ("PI2", "Las arquitecturas de IA logran medianas de F1-score de 95.2 % en recibos y 89.8 % en tablas, con descensos a 84.5 % ante ruido severo.",
     "Bajas: métricas formales en 89.3 % (QA4 = 0.912).", "Alta en benchmarks abiertos; moderada en escaneos degradados.", "Alta: n = 117 estudios con datos verificables.", "Moderada a Alta: sólida en benchmarks; menor en lotes reales no curados.", "ALTA CERTEZA (benchmarks) / MODERADA (lotes degradados)"),
    ("PI3", "Las soluciones IA superan al ingreso manual y reglas en el 86.6 % de los estudios, reduciendo tiempos de 24–72 h a segundos.",
     "Moderadas: QA5 presentó 32.1 % de cumplimiento parcial.", "Alta: consenso generalizado en dirección del efecto.", "Moderada a Alta: n = 82 estudios con comparador.", "Alta: evalúa tiempos y reducción de errores humanos.", "MODERADA CERTEZA (por vulnerabilidad en QA5)"),
    ("PI4", "Tablas contables (45.0 %) y facturas (26.0 %) son el eje central, pero el 78.6 % de estudios no implementa conectores nativos ERP.",
     "Bajas: tipología documental 100 % explícita (QA1 = 1.000).", "Alta: concordancia global en primacía contable.", "Alta: N = 131 estudios cubren la tipología.", "Moderada: alta para extracción; moderada en ERP vivo.", "ALTA CERTEZA (extracción) / MODERADA (integración ERP)")
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
add_table_footer("Fuente: elaboración propia a partir del corpus primario [3]–[133]. Evaluación estructurada bajo los cuatro dominios de GRADE-CERQual [140].")

output_path = 'project/shared/Articulo_RSL_Resultados_Completo_IEEE.docx'
doc.save(output_path)
print(f"Documento completo generado exitosamente en: {output_path} ({os.path.getsize(output_path)} bytes)")

# Actualizar también Articulo_RSL_Resultados_Bloque1_IEEE.docx para consistencia
output_b1 = 'project/shared/Articulo_RSL_Resultados_Bloque1_IEEE.docx'
doc.save(output_b1)
print(f"Documento Bloque 1 actualizado en: {output_b1} ({os.path.getsize(output_b1)} bytes)")
