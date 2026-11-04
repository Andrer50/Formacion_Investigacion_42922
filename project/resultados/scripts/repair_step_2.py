import docx

def repair_aperturas(docx_path):
    print(f"Repairing aperturas in {docx_path}...")
    doc = docx.Document(docx_path)
    
    text_pd1 = (
        "1) Apertura: Ciento treinta y un estudios primarios (100,0 % del corpus; TABLA XIII, Fig. 2) "
        "conformaron la serie cronológica de producción científica entre 2020 y 2025/2026 (PD1), "
        "evidenciando un crecimiento sostenido que pasa de 4 artículos en 2020 (3,1 %) a un pico de 50 artículos "
        "en 2025 (38,2 %) y 3 en modalidad Early Access 2026 (2,3 %), concentrando el último bienio el 40,5 % "
        "de toda la literatura (53 de 131 estudios)."
    )
    
    text_pd2 = (
        "1) Apertura: Ciento treinta y un estudios (100,0 % del corpus; TABLA XIV, Fig. 3, Tabla S1) "
        "fueron analizados cienciométricamente para determinar los núcleos de difusión editorial, "
        "polos geográficos y redes de colaboración autoral (PD2), identificándose 76 revistas científicas "
        "indexadas, 498 autores únicos y 32 países de afiliación institucional."
    )
    
    text_pd3 = (
        "1) Apertura: Ciento treinta y un estudios (100,0 % del corpus; TABLA XV, Fig. 4) "
        "se clasificaron en la matriz cruzada de diseños metodológicos frente a tipologías de conjuntos "
        "de datos (PD3), constatándose una marcada hegemonía de los diseños experimentales controlados "
        "de laboratorio (62,6 %, n = 82) y el uso de benchmarks públicos abiertos (51,9 %, n = 68), "
        "frente a una reducida proporción de casos de estudio corporativos reales (6,1 %, n = 8)."
    )
    
    # Locate Fig. 2
    for i, p in enumerate(doc.paragraphs):
        if p.text.strip().startswith("Fig. 2."):
            # The next paragraph is Apertura
            target_p = doc.paragraphs[i + 1]
            print(f"Found Fig. 2 at {i}. Replacing paragraph {i+1} with PD1 Apertura.")
            target_p.text = text_pd1
            break
            
    # Locate Fig. 3
    for i, p in enumerate(doc.paragraphs):
        if p.text.strip().startswith("Fig. 3."):
            target_p = doc.paragraphs[i + 1]
            print(f"Found Fig. 3 at {i}. Replacing paragraph {i+1} with PD2 Apertura.")
            target_p.text = text_pd2
            break
            
    # Locate Fig. 4
    for i, p in enumerate(doc.paragraphs):
        if p.text.strip().startswith("Fig. 4."):
            target_p = doc.paragraphs[i + 1]
            print(f"Found Fig. 4 at {i}. Replacing paragraph {i+1} with PD3 Apertura.")
            target_p.text = text_pd3
            break
            
    doc.save(docx_path)
    print(f"Saved {docx_path} successfully.\n")

if __name__ == '__main__':
    repair_aperturas('project/shared/RSL_Sergio_Rupay.docx')
    repair_aperturas('project/resultados/Articulo_RSL_Resultados_Completo_IEEE.docx')

