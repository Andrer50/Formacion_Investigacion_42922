import docx

def update_docx_files():
    # 1. Update project/shared/RSL_Sergio_Rupay.docx
    doc1 = docx.Document('project/shared/RSL_Sergio_Rupay.docx')
    for p in doc1.paragraphs:
        if 'scopus_export_it2.csv' in p.text:
            p.text = p.text.replace(
                'scopus_export_it2.csv (n = 311) y wos_export_it2.xls (n = 266).',
                'los registros maestros de exportación de Scopus (n = 311) y Web of Science (n = 266), disponibles en el repositorio auditable del estudio.'
            )
            # ensure formatting is Times New Roman, 8.0 pt, italic
            p.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.space_before = docx.shared.Pt(2)
            p.paragraph_format.space_after = docx.shared.Pt(6)
            for r in p.runs:
                r.font.name = 'Times New Roman'
                r.font.size = docx.shared.Pt(8.0)
                r.italic = True
            print("Updated P47 in RSL_Sergio_Rupay.docx")

        if 'corpus_eligibility_excluded_146.csv' in p.text:
            p.text = p.text.replace(
                'su catálogo bibliográfico auditable completo (corpus_eligibility_excluded_146.csv) se encuentra disponible en el repositorio abierto de datos de la investigación conforme a las directrices de reporte de [2].',
                'su catálogo bibliográfico auditable completo (n = 146 registros excluidos) se encuentra disponible en el repositorio abierto de datos de la investigación conforme a las directrices de reporte de [2].'
            )
            print("Updated P65 in RSL_Sergio_Rupay.docx")

    doc1.save('project/shared/RSL_Sergio_Rupay.docx')

    # 2. Update project/metodologia/Metodologia_RSL_IEEE.docx
    doc2 = docx.Document('project/metodologia/Metodologia_RSL_IEEE.docx')
    for p in doc2.paragraphs:
        if 'scopus_export_it2.csv' in p.text:
            p.text = p.text.replace(
                'scopus_export_it2.csv y wos_export_it2.xls',
                'el repositorio metodológico auditable de datos primarios'
            )
            p.text = p.text.replace(
                'scopus_export_it2.csv (n = 311) y wos_export_it2.xls (n = 266)',
                'los registros maestros de exportación de Scopus (n = 311) y Web of Science (n = 266), disponibles en el repositorio auditable del estudio'
            )
            print("Updated paragraph in Metodologia_RSL_IEEE.docx")
        if 'corpus_eligibility_excluded_146.csv' in p.text:
            p.text = p.text.replace(
                '(corpus_eligibility_excluded_146.csv)',
                '(n = 146 registros excluidos)'
            )
            print("Updated exclusion paragraph in Metodologia_RSL_IEEE.docx")
    doc2.save('project/metodologia/Metodologia_RSL_IEEE.docx')

def update_text_files():
    files = [
        'project/metodologia/main.md',
        'project/metodologia/scripts/build_combined_ieee_article.py',
        'project/metodologia/scripts/build_metodologia_ieee_docx.py'
    ]
    for fpath in files:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        content = content.replace(
            'scopus_export_it2.csv (n = 311) y wos_export_it2.xls (n = 266)',
            'los registros maestros de exportación de Scopus (n = 311) y Web of Science (n = 266), disponibles en el repositorio auditable del estudio'
        )
        content = content.replace(
            'scopus_export_it2.csv y wos_export_it2.xls',
            'el repositorio metodológico auditable de datos primarios'
        )
        content = content.replace(
            'corpus_eligibility_excluded_146.csv',
            'catálogo de 146 registros excluidos'
        )
        
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated text file: {fpath}")

if __name__ == '__main__':
    update_docx_files()
    update_text_files()
    print("ALL FILES CLEANED OF RAW FILENAMES!")

