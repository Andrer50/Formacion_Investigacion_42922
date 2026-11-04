import os

def update_markdown_builder():
    tgt = 'project/resultados/scripts/build_full_resultados_markdown.py'
    with open(tgt, 'r', encoding='utf-8') as f:
        content = f.read()

    idx1 = content.find('1. **Núcleos de difusión y revistas líderes:**')
    idx2 = content.find('#### Bloque 3 — Contrastes y Dispersión Autoral', idx1)

    if idx1 != -1 and idx2 != -1:
        old_block = content[idx1:idx2]
        new_block = '''a) **Núcleos de difusión y revistas líderes:** Doce revistas concentraron casi la mitad de la producción global (60 de 131 artículos; Tabla S1 en Apéndice). Las cabeceras líderes fueron *IEEE Access* (9,9 %, n = 13; Q1/Q2), *International Journal on Document Analysis and Recognition (IJDAR)* (6,9 %, n = 9; Q2) y *Pattern Recognition* (4,6 %, n = 6; Q1), consolidándose como los principales canales de difusión de modelos de extracción estructurada e IDP. Las restantes 64 revistas indexadas reunieron una producción complementaria y diversa (71 artículos, 54,2 % del corpus; Tabla S1 en Apéndice), reflejando la dispersión propia de la Ley de Bradford en el área. El catálogo completo de revistas, editoriales y cuartiles JCR/SJR se compendia en la Tabla S1 del Apéndice de Material Suplementario para optimizar la densidad técnica del cuerpo principal.
b) **Concentración geográfica y polos institucionales:** A nivel de afiliación institucional del primer autor, la producción está liderada por China (29,8 %, n = 39), seguida por India (8,4 %, n = 11), Estados Unidos (7,6 %, n = 10), Alemania (6,9 %, n = 9) y Corea del Sur (4,6 %, n = 6), concentrando estas cinco naciones más de la mitad del corpus primario (57,3 %, 75 de 131 estudios; Tabla XIV, Fig. 3a).
c) **Redes de coocurrencia de palabras clave (VOSviewer):** El análisis cienciométrico de descriptores con frecuencia ≥ 3 en VOSviewer [139] articuló tres clústeres temáticos interconectados (Fig. 3b): un primer clúster dominante centrado en extracción de información y comprensión documental (information extraction, document understanding, key information extraction, LayoutLM); un segundo clúster orientado al reconocimiento estructural y detección tabular (table structure recognition, table detection, graph neural networks); y un tercer clúster enfocado en digitalización y automatización transaccional (optical character recognition, deep learning, invoice processing, ERP).

'''
        content = content[:idx1] + new_block + content[idx2:]
        with open(tgt, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[OK] Replaced PD2 block in {tgt}")
    else:
        print(f"[FAIL] Could not locate boundaries in {tgt}: idx1={idx1}, idx2={idx2}")

if __name__ == '__main__':
    update_markdown_builder()

