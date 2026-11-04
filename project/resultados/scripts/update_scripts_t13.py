def update_generator_scripts():
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
            print(f"Successfully updated {script_path}")
        else:
            print(f"Pattern not found in {script_path}")

if __name__ == '__main__':
    update_generator_scripts()

