import docx
from docx.shared import Pt
import re

line1 = (
    "1) Experimental Controlado (82 estudios): Datasets Abiertos (48 estudios: [5], [10], [26], [27], "
    "[29]–[31], [33]–[36], [38]–[43], [45]–[52], [57], [60], [61], [65]–[68], [71], [73], [74], [76], "
    "[77], [79], [81], [83], [86]–[90], [92], [105], [115]); Datasets Privados (18 estudios: [6], [15], "
    "[18], [21]–[23], [28], [37], [44], [63], [72], [80], [91], [93], [109]–[111], [113]); "
    "Datasets Mixtos (16 estudios: [14], [32], [55], [56], [78], [96], [97], [99], [100], [102], [106], "
    "[114], [119], [120], [124], [126])."
)

line2 = (
    "2) Desarrollo de Artefacto / PoC (31 estudios): Datasets Abiertos (14 estudios: [3], [4], [7]–[9], "
    "[11]–[13], [16], [17], [19], [20], [24], [25]); Datasets Privados (11 estudios: [54], [69], [95], "
    "[98], [112], [116], [118], [121]–[123], [132]); Datasets Mixtos (6 estudios: [58], [59], [108], "
    "[125], [129], [130])."
)

line3 = (
    "3) Cuasi-experimental (10 estudios): Datasets Abiertos (4 estudios: [85], [94], [101], [104]); "
    "Datasets Privados (4 estudios: [53], [82], [107], [133]); Datasets Mixtos (2 estudios: [62], [128])."
)

line4 = (
    "4) Caso de Estudio Real Corporativo (8 estudios): Datasets Abiertos (2 estudios: [84], [103]); "
    "Datasets Privados (5 estudios: [64], [70], [75], [117], [127]); Datasets Mixtos (1 estudio: [131])."
)

def update_rupay_docx(file_path):
    print(f"\n--- Modificando {file_path} ---")
    doc = docx.Document(file_path)

    target_idx = None
    for i, p in enumerate(doc.paragraphs):
        if p.text.strip().startswith("A. Clasificación Metodológica y Datasets (PD3 — Tabla XV)"):
            target_idx = i
            break
    assert target_idx is not None, "No se encontró el encabezado de Apéndice A en RSL_Sergio_Rupay.docx"
    print(f"Encabezado Apéndice A encontrado en P{target_idx}")

    p_lines = [
        doc.paragraphs[target_idx + 1],
        doc.paragraphs[target_idx + 2],
        doc.paragraphs[target_idx + 3],
        doc.paragraphs[target_idx + 4]
    ]

    new_lines = [line1, line2, line3, line4]

    for p, new_text in zip(p_lines, new_lines):
        for r in p._element.xpath('./w:r'):
            p._element.remove(r)
        run = p.add_run(new_text)
        run.font.name = "Times New Roman"
        run.font.size = Pt(9.5)
        run.bold = False

    doc.save(file_path)
    print(f"Guardado exitoso de {file_path}")

def update_resultados_docx(file_path):
    print(f"\n--- Modificando {file_path} ---")
    doc = docx.Document(file_path)

    target_idx = None
    for i, p in enumerate(doc.paragraphs):
        if p.text.strip().startswith("A. Clasificación Metodológica y Datasets (PD3 — Tabla XV)"):
            target_idx = i
            break
    assert target_idx is not None, "No se encontró el encabezado de Apéndice A en doc_res"
    print(f"Encabezado Apéndice A encontrado en P{target_idx}")

    p_lines = [
        doc.paragraphs[target_idx + 1],
        doc.paragraphs[target_idx + 2],
        doc.paragraphs[target_idx + 3],
        doc.paragraphs[target_idx + 4]
    ]

    new_lines = [line1, line2, line3, line4]

    for p, new_text in zip(p_lines, new_lines):
        for r in p._element.xpath('./w:r'):
            p._element.remove(r)
        run = p.add_run(new_text)
        run.font.name = "Times New Roman"
        run.font.size = Pt(10.0)
        run.bold = False

    doc.save(file_path)
    print(f"Guardado exitoso de {file_path}")

def update_main_md(file_path):
    print(f"\n--- Modificando {file_path} ---")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    block_md_single = (
        "### A. Clasificación Metodológica y Datasets (PD3 — Tabla XV)\n"
        f"{line1}\n"
        f"{line2}\n"
        f"{line3}\n"
        f"{line4}\n\n"
    )

    pattern = r"### A\. Clasificación Metodológica y Datasets \(PD3 — Tabla XV\)\n.*?(?=### B\. Familias Algorítmicas)"
    matches = list(re.finditer(pattern, content, re.DOTALL))
    print(f"Coincidencias de Apéndice A en main.md: {len(matches)}")
    if matches:
        for m in reversed(matches):
            content = content[:m.start()] + block_md_single + content[m.end():]
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Guardado exitoso de main.md")
    else:
        print("WARNING: No se encontró patrón en main.md!")

if __name__ == '__main__':
    update_rupay_docx('project/shared/RSL_Sergio_Rupay.docx')
    update_resultados_docx('project/resultados/Articulo_RSL_Resultados_Completo_IEEE.docx')
    update_main_md('project/resultados/main.md')

