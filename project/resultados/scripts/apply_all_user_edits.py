import os

def update_docx_builders():
    targets = [
        'project/metodologia/scripts/build_combined_ieee_article.py',
        'project/resultados/scripts/build_resultados_completo_docx.py'
    ]

    old_pd2 = '''add_p(
    "Conforme a la regla de asignación por primer autor, la investigación se concentró principalmente en Asia y Norteamérica, con China (29,8 %, n = 39), India (8,4 %, n = 11) y Estados Unidos (7,6 %, n = 10) a la vanguardia, complementados por contribuciones significativas de Europa occidental en Alemania (6,9 %, n = 9) y España (2,3 %, n = 3; Tabla XIV, Fig. 3a).",
    bold_prefix="b) Polos geográficos de investigación: "
)
add_p(
    "Con un umbral ≥ 3 apariciones se configuraron tres clústeres conceptuales (Fig. 3b): Clúster 1 (Extracción y Semántica: Information Extraction, Document Understanding y Key Information Extraction - KIE); Clúster 2 (Paradigmas Algorítmicos: Deep Learning, Optical Character Recognition - OCR y Transformers); y Clúster 3 (Estructuras Complejas: Table Structure Recognition, Table Detection y Object Detection).",
    bold_prefix="c) Red cienciométrica de palabras clave (VOSviewer): "
)'''

    new_pd2 = '''add_p(
    "A nivel de afiliación institucional del primer autor, la producción está liderada por China (29,8 %, n = 39), seguida por India (8,4 %, n = 11), Estados Unidos (7,6 %, n = 10), Alemania (6,9 %, n = 9) y Corea del Sur (4,6 %, n = 6), concentrando estas cinco naciones más de la mitad del corpus primario (57,3 %, 75 de 131 estudios; Tabla XIV, Fig. 3a).",
    bold_prefix="b) Concentración geográfica y polos institucionales: "
)
add_p(
    "El análisis cienciométrico de descriptores con frecuencia ≥ 3 en VOSviewer [139] articuló tres clústeres temáticos interconectados (Fig. 3b): un primer clúster dominante centrado en extracción de información y comprensión documental (information extraction, document understanding, key information extraction, LayoutLM); un segundo clúster orientado al reconocimiento estructural y detección tabular (table structure recognition, table detection, graph neural networks); y un tercer clúster enfocado en digitalización y automatización transaccional (optical character recognition, deep learning, invoice processing, ERP).",
    bold_prefix="c) Redes de coocurrencia de palabras clave (VOSviewer): "
)'''

    old_refs = [
        ('add_ref(135, "D. S. Cruzes and T. Dybå, \\"Research synthesis in software engineering: A tertiary study,\\" Inf. Softw. Technol., vol. 53, no. 5, pp. 440–455, 2011, doi: 10.1016/j.infsof.2011.01.004.")',
         'add_ref(135, "D. S. Cruzes and T. Dybå, \\"Recommended steps for thematic synthesis in software engineering,\\" in Proc. Int. Symp. Empirical Softw. Eng. Meas. (ESEM), 2011, pp. 275–284, doi: 10.1109/ESEM.2011.36.")'),
        ('add_ref(136, "J. Popay et al., \\"Guidance on the conduct of narrative synthesis in systematic reviews,\\" ESRC Methods Programme, Lancaster Univ., Tech. Rep., 2006.")',
         'add_ref(136, "J. Popay et al., \\"Guidance on the conduct of narrative synthesis in systematic reviews: A product from the ESRC methods programme,\\" Lancaster Univ., Tech. Rep., 2006, doi: 10.13140/2.1.1018.4643.")'),
        ('add_ref(143, "S. Appalaraju, B. Jasani, B. U. Kota, Y. Xie, and R. Manmatha, \\"DocFormer: End-to-end transformer for document understanding,\\" in Proc. IEEE/CVF Int. Conf. Comput. Vis. (ICCV), 2021, pp. 993–1003, doi: 10.1109/ICCV48922.2021.00104.")',
         'add_ref(143, "S. Appalaraju, B. Jasani, B. U. Kota, Y. Xie, and R. Manmatha, \\"DocFormer: End-to-end transformer for document understanding,\\" in Proc. IEEE/CVF Int. Conf. Comput. Vis. (ICCV), 2021, pp. 973–983, doi: 10.1109/ICCV48922.2021.00103.")'),
        ('add_ref(144, "Y. Li et al., \\"StrucTexT: Structured text understanding with multi-modal pre-training,\\" in Proc. 29th ACM Int. Conf. Multimedia (MM), 2021, pp. 1917–1925, doi: 10.1145/3474085.3475313.")',
         'add_ref(144, "Y. Li et al., \\"StrucTexT: Structured text understanding with multi-modal transformers,\\" in Proc. 29th ACM Int. Conf. Multimedia (MM), 2021, pp. 1912–1920, doi: 10.1145/3474085.3475345.")'),
        ('add_ref(145, "T. Hong et al., \\"BROS: A pre-trained language model focusing on text and layout for better key information extraction from documents,\\" in Proc. AAAI Conf. Artif. Intell. (AAAI), vol. 36, no. 10, pp. 10767–10775, 2022, doi: 10.1609/aaai.v36i10.21323.")',
         'add_ref(145, "T. Hong, D. Kim, M. Ji, W. Hwang, D. Nam, and S. Park, \\"BROS: A pre-trained language model focusing on text and layout for better key information extraction from documents,\\" in Proc. AAAI Conf. Artif. Intell., vol. 36, no. 10, 2022, pp. 10767–10775, doi: 10.1609/aaai.v36i10.21322.")')
    ]

    for tgt in targets:
        with open(tgt, 'r', encoding='utf-8') as f:
            content = f.read()

        if old_pd2 in content:
            content = content.replace(old_pd2, new_pd2)
            print(f"[OK] Replaced PD2 b/c in {tgt}")
        else:
            print(f"[WARN] old_pd2 not found in {tgt}")

        for old_r, new_r in old_refs:
            if old_r in content:
                content = content.replace(old_r, new_r)
                print(f"[OK] Replaced ref in {tgt}")
            else:
                print(f"[WARN] old ref not found in {tgt}: {old_r[:40]}")

        with open(tgt, 'w', encoding='utf-8') as f:
            f.write(content)

def update_markdown_builder():
    tgt = 'project/resultados/scripts/build_full_resultados_markdown.py'
    with open(tgt, 'r', encoding='utf-8') as f:
        content = f.read()

    old_pd2_md = '''1. **Núcleos de difusión y revistas líderes:** Doce revistas concentraron casi la mitad de la producción global (60 de 131 artículos; Tabla S1 en Apéndice). Las cabeceras líderes fueron *IEEE Access* (9,9 %, n = 13; Q1/Q2), *International Journal on Document Analysis and Recognition (IJDAR)* (6,9 %, n = 9; Q2) y *Pattern Recognition* (4,6 %, n = 6; Q1), consolidándose como los principales canales de difusión de modelos de extracción estructurada e IDP. Las restantes 64 revistas indexadas reunieron una producción complementaria y diversa (71 artículos, 54,2 % del corpus; Tabla S1 en Apéndice), reflejando la dispersión propia de la Ley de Bradford en el área. El catálogo completo de revistas, editoriales y cuartiles JCR/SJR se compendia en la Tabla S1 del Apéndice de Material Suplementario para optimizar la densidad técnica del cuerpo principal.
2. **Polos geográficos de investigación:** Conforme a la regla de asignación por primer autor, la investigación se concentró principalmente en Asia y Norteamérica, con China, India y Estados Unidos a la vanguardia, complementados por contribuciones significativas de Europa occidental en Alemania y España (Tabla XIV, Fig. 3a).
3. **Red cienciométrica de palabras clave (VOSviewer):** Con un umbral ≥ 3 apariciones se configuraron tres clústeres conceptuales (Fig. 3b): Clúster 1 (Extracción y Semántica: Information Extraction, Document Understanding y Key Information Extraction - KIE); Clúster 2 (Paradigmas Algorítmicos: Deep Learning, Optical Character Recognition - OCR y Transformers); y Clúster 3 (Estructuras Complejas: Table Structure Recognition, Table Detection y Object Detection).'''

    new_pd2_md = '''a) **Núcleos de difusión y revistas líderes:** Doce revistas concentraron casi la mitad de la producción global (60 de 131 artículos; Tabla S1 en Apéndice). Las cabeceras líderes fueron *IEEE Access* (9,9 %, n = 13; Q1/Q2), *International Journal on Document Analysis and Recognition (IJDAR)* (6,9 %, n = 9; Q2) y *Pattern Recognition* (4,6 %, n = 6; Q1), consolidándose como los principales canales de difusión de modelos de extracción estructurada e IDP. Las restantes 64 revistas indexadas reunieron una producción complementaria y diversa (71 artículos, 54,2 % del corpus; Tabla S1 en Apéndice), reflejando la dispersión propia de la Ley de Bradford en el área. El catálogo completo de revistas, editoriales y cuartiles JCR/SJR se compendia en la Tabla S1 del Apéndice de Material Suplementario para optimizar la densidad técnica del cuerpo principal.
b) **Concentración geográfica y polos institucionales:** A nivel de afiliación institucional del primer autor, la producción está liderada por China (29,8 %, n = 39), seguida por India (8,4 %, n = 11), Estados Unidos (7,6 %, n = 10), Alemania (6,9 %, n = 9) y Corea del Sur (4,6 %, n = 6), concentrando estas cinco naciones más de la mitad del corpus primario (57,3 %, 75 de 131 estudios; Tabla XIV, Fig. 3a).
c) **Redes de coocurrencia de palabras clave (VOSviewer):** El análisis cienciométrico de descriptores con frecuencia ≥ 3 en VOSviewer [139] articuló tres clústeres temáticos interconectados (Fig. 3b): un primer clúster dominante centrado en extracción de información y comprensión documental (information extraction, document understanding, key information extraction, LayoutLM); un segundo clúster orientado al reconocimiento estructural y detección tabular (table structure recognition, table detection, graph neural networks); y un tercer clúster enfocado en digitalización y automatización transaccional (optical character recognition, deep learning, invoice processing, ERP).'''

    old_refs_md = [
        ('[135] D. S. Cruzes and T. Dybå, "Research synthesis in software engineering: A tertiary study," Inf. Softw. Technol., vol. 53, no. 5, pp. 440–455, 2011, doi: 10.1016/j.infsof.2011.01.004.',
         '[135] D. S. Cruzes and T. Dybå, "Recommended steps for thematic synthesis in software engineering," in Proc. Int. Symp. Empirical Softw. Eng. Meas. (ESEM), 2011, pp. 275–284, doi: 10.1109/ESEM.2011.36.'),
        ('[136] J. Popay et al., "Guidance on the conduct of narrative synthesis in systematic reviews," ESRC Methods Programme, Lancaster Univ., Tech. Rep., 2006.',
         '[136] J. Popay et al., "Guidance on the conduct of narrative synthesis in systematic reviews: A product from the ESRC methods programme," Lancaster Univ., Tech. Rep., 2006, doi: 10.13140/2.1.1018.4643.'),
        ('[143] S. Appalaraju, B. Jasani, B. U. Kota, Y. Xie, and R. Manmatha, "DocFormer: End-to-end transformer for document understanding," in Proc. IEEE/CVF Int. Conf. Comput. Vis. (ICCV), 2021, pp. 993–1003, doi: 10.1109/ICCV48922.2021.00104.',
         '[143] S. Appalaraju, B. Jasani, B. U. Kota, Y. Xie, and R. Manmatha, "DocFormer: End-to-end transformer for document understanding," in Proc. IEEE/CVF Int. Conf. Comput. Vis. (ICCV), 2021, pp. 973–983, doi: 10.1109/ICCV48922.2021.00103.'),
        ('[144] Y. Li et al., "StrucTexT: Structured text understanding with multi-modal pre-training," in Proc. 29th ACM Int. Conf. Multimedia (MM), 2021, pp. 1917–1925, doi: 10.1145/3474085.3475313.',
         '[144] Y. Li et al., "StrucTexT: Structured text understanding with multi-modal transformers," in Proc. 29th ACM Int. Conf. Multimedia (MM), 2021, pp. 1912–1920, doi: 10.1145/3474085.3475345.'),
        ('[145] T. Hong et al., "BROS: A pre-trained language model focusing on text and layout for better key information extraction from documents," in Proc. AAAI Conf. Artif. Intell. (AAAI), vol. 36, no. 10, pp. 10767–10775, 2022, doi: 10.1609/aaai.v36i10.21323.',
         '[145] T. Hong, D. Kim, M. Ji, W. Hwang, D. Nam, and S. Park, "BROS: A pre-trained language model focusing on text and layout for better key information extraction from documents," in Proc. AAAI Conf. Artif. Intell., vol. 36, no. 10, 2022, pp. 10767–10775, doi: 10.1609/aaai.v36i10.21322.')
    ]

    if old_pd2_md in content:
        content = content.replace(old_pd2_md, new_pd2_md)
        print(f"[OK] Replaced PD2 in {tgt}")
    else:
        print(f"[WARN] old_pd2_md not found in {tgt}")

    for old_r, new_r in old_refs_md:
        if old_r in content:
            content = content.replace(old_r, new_r)
            print(f"[OK] Replaced ref in {tgt}")
        else:
            print(f"[WARN] old ref not found in {tgt}: {old_r[:40]}")

    with open(tgt, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    update_docx_builders()
    update_markdown_builder()
    print("Updates applied successfully.")

