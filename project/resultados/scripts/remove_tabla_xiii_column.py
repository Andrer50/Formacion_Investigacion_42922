import docx
from docx.shared import Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

def modify_docx_table_xiii(docx_path):
    print(f"Modifying TABLA XIII in {docx_path}...")
    doc = docx.Document(docx_path)
    
    target_table = None
    for t in doc.tables:
        if len(t.rows) > 0:
            header_texts = [c.text.strip() for c in t.rows[0].cells]
            if len(header_texts) >= 2 and "Año de Publicación" in header_texts[0] and "Estudios Primarios" in header_texts[1]:
                target_table = t
                break
                
    if target_table is None:
        print("  TABLA XIII with column 'Estudios Primarios Indexados [n]' not found or already modified.")
        return

    # Remove cell at index 1 for each row
    for row in target_table.rows:
        cell = row.cells[1]
        tc = cell._tc
        tc.getparent().remove(tc)
        
    # Remove gridCol from tblGrid if present
    grid = target_table._tbl.find(docx.oxml.ns.qn('w:tblGrid'))
    if grid is not None:
        gridCols = grid.findall(docx.oxml.ns.qn('w:gridCol'))
        if len(gridCols) > 1:
            grid.remove(gridCols[1])
            
    # Set widths and alignment for the remaining 4 columns
    widths = [Inches(1.8), Inches(1.6), Inches(1.6), Inches(1.6)]
    for row in target_table.rows:
        for idx, width in enumerate(widths):
            cell = row.cells[idx]
            cell.width = width
            for p in cell.paragraphs:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                
    doc.save(docx_path)
    print(f"  Successfully removed column from TABLA XIII in {docx_path}.")

def modify_markdown():
    md_path = 'project/resultados/main.md'
    with open(md_path, 'r', encoding='utf-8') as f:
        text = f.read()
        
    old_t13_start = '```\nTABLA XIII\nDISTRIBUCIÓN CRONOLÓGICA DE LA PRODUCCIÓN CIENTÍFICA (2020–2025/2026) (N = 131)\n```'
    new_t13 = """```
TABLA XIII
DISTRIBUCIÓN CRONOLÓGICA DE LA PRODUCCIÓN CIENTÍFICA (2020–2025/2026) (N = 131)
```
| Año de Publicación | Frecuencia Absoluta (n) | Frecuencia Relativa (%) | Porcentaje Acumulado (%) |
| :---: | :---: | :---: | :---: |
| **2020** | 4 | 3,1 % | 3,1 % |
| **2021** | 14 | 10,7 % | 13,8 % |
| **2022** | 17 | 13,0 % | 26,8 % |
| **2023** | 27 | 20,6 % | 47,4 % |
| **2024** | 16 | 12,2 % | 59,6 % |
| **2025** | 50 | 38,2 % | 97,8 % |
| **2026\\*** | 3 | 2,3 % | 100,0 % |
| **Total Corpus** | **131** | **100,0 %** | **100,0 %** |"""

    pos_start = text.find(old_t13_start)
    if pos_start != -1:
        pos_end = text.find('*\* Nota: Los estudios', pos_start)
        if pos_end != -1:
            text = text[:pos_start] + new_t13 + "\n\n" + text[pos_end:]
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(text)
            print("  Successfully updated TABLA XIII in main.md.")

def modify_generator_scripts():
    for script_path in ['project/metodologia/scripts/build_combined_ieee_article.py',
                        'project/resultados/scripts/build_resultados_completo_docx.py']:
        with open(script_path, 'r', encoding='utf-8') as f:
            code = f.read()

        old_setup = """t_pd1 = doc.add_table(rows=8, cols=5)
hdr_pd1 = t_pd1.rows[0].cells
hdr_pd1[0].paragraphs[0].text = "Año de Publicación"
hdr_pd1[1].paragraphs[0].text = "Estudios Primarios Indexados [n]"
hdr_pd1[2].paragraphs[0].text = "Frecuencia Absoluta (n)"
hdr_pd1[3].paragraphs[0].text = "Frecuencia Relativa (%)"
hdr_pd1[4].paragraphs[0].text = "Porcentaje Acumulado (%)"

pd1_data = [
    ("2020", "[64], [111], [130], [131]", "4", "3,1 %", "3,1 %"),
    ("2021", "[58]–[63], [112]–[114], [123], [126]–[129]", "14", "10,7 %", "13,8 %"),
    ("2022", "[50]–[55], [57], [103]–[109], [125], [132], [133]", "17", "13,0 %", "26,8 %"),
    ("2023", "[39]–[49], [67], [90]–[92], [94]–[102], [116], [121], [124]", "27", "20,6 %", "47,4 %"),
    ("2024", "[28]–[31], [33]–[38], [84], [86]–[89], [120]", "16", "12,2 %", "59,6 %"),
    ("2025", "[4]–[27], [32], [56], [68]–[83], [85], [93], [110], [115], [117]–[119], [122]", "50", "38,2 %", "97,8 %"),
    ("2026*", "[3], [65], [66]", "3", "2,3 %", "100,0 %")
]
for idx, (yr, refs, fa, fr, pac) in enumerate(pd1_data, start=1):
    c = t_pd1.rows[idx].cells
    c[0].paragraphs[0].text = yr
    c[1].paragraphs[0].text = refs
    c[2].paragraphs[0].text = fa
    c[3].paragraphs[0].text = fr
    c[4].paragraphs[0].text = pac

style_table(t_pd1, [Inches(1.1), Inches(2.8), Inches(0.9), Inches(0.9), Inches(0.9)],
            align_cols=[WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER])"""

        new_setup = """t_pd1 = doc.add_table(rows=8, cols=4)
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
            align_cols=[WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER])"""

        if old_setup in code:
            code = code.replace(old_setup, new_setup)
            with open(script_path, 'w', encoding='utf-8') as f:
                f.write(code)
            print(f"  Successfully updated generator script {script_path}.")

if __name__ == '__main__':
    modify_docx_table_xiii('project/shared/RSL_Sergio_Rupay.docx')
    modify_docx_table_xiii('project/resultados/Articulo_RSL_Resultados_Completo_IEEE.docx')
    modify_markdown()
    modify_generator_scripts()

