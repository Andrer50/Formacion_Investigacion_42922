import re

def verify(file_path):
    print(f"=== VERIFYING {file_path} ===")
    with open(file_path, 'r', encoding='utf-8') as f:
        t = f.read()

    tests = [
        ("1. Tabla XIV ultima fila 71 (54.2 %)", "71 (54.2 %)" in t),
        ("1. Tabla XIV NO tiene 70 (53.4 %)", "70 (53.4 %)" not in t),
        ("1. Texto Sec III.C.2.a 60 de 131", "60 de 131" in t),
        ("1. Texto Sec III.C.2.a NO tiene 61 de 131", "61 de 131" not in t),
        ("2. Tabla XV NO tiene Villa-García [70]", "Villa-García" not in t),
        ("2. Tabla XV NO tiene Harit [40]", "Harit" not in t),
        ("2. Tabla XV Simsek 11, 35, 48, 51", "[11], [35], [48], [51]" in t),
        ("2. Tabla XV Hashmi 59, 61, 123", "[59], [61], [123]" in t),
        ("2. Tabla XV Fornés 105, 111", "[105], [111]" in t),
        ("2. PD2 Bloque 4 ausencia LatAm y España 105, 111, 131", "[105], [111], [131]" in t),
        ("3. Tabla XVI 12 celdas disjuntas", "12 celdas" in t),
        ("4. PI1 Bloque 3 NO Kim et al. [3]", "Kim et al. [3]" not in t),
        ("4. PI2 Bloque 3 NO Tanaka et al. [37]", "Tanaka et al. [37]" not in t),
        ("4. PI3 Bloque 3 NO Krause et al. [56]", "Krause et al. [56]" not in t),
        ("4. PI4 Bloque 3 NO Villa-García et al. [70]", "Villa-García et al. [70]" not in t),
        ("5. PI2 SROIE 93.8 % (45 de 48)", "93.8" in t and ("45 de 48" in t or "$45$ de $48$" in t)),
        ("5. PI2 FinTabNet 88.1 % (37 de 42)", "88.1" in t and ("37 de 42" in t or "$37$ de $42$" in t)),
        ("5. PI2 FUNSD 95.2 % (20 de 21)", "95.2" in t and ("20 de 21" in t or "$20$ de $21$" in t)),
        ("5. PI2 Flujos 50.0 % (3 de 6)", "50.0" in t and ("3 de 6" in t or "$3$ de $6$" in t)),
        ("6. PI3 Mejora 97.2 % (69 de 71)", "97.2" in t and ("69 de 71" in t or "$69$ de $71$" in t)),
        ("6. PI3 Paridad 87.5 % (7 de 8)", "87.5" in t and ("7 de 8" in t or "$7$ de $8$" in t)),
        ("6. PI3 Empeora 66.7 % (2 de 3)", "66.7" in t and ("2 de 3" in t or "$2$ de $3$" in t)),
        ("6. PI3 Bloque 4 69 de 78 en Mejora (88.5 %)", ("69 de 78 en Mejora" in t and "88.5" in t)),
        ("6. PI3 Bloque 4 7 de 78 en Paridad (9.0 %)", ("7 de 78 en Paridad" in t and "9.0" in t)),
        ("6. PI3 Bloque 4 2 de 78 en Desfavorables (2.6 %)", ("2 de 78 en Desfavorables" in t and "2.6" in t)),
        ("7. PI4 Balances 84.7 % (50 de 59)", "84.7" in t and ("50 de 59" in t or "$50$ de $59$" in t)),
        ("7. PI4 Facturas 85.3 % (29 de 34)", "85.3" in t and ("29 de 34" in t or "$29$ de $34$" in t)),
        ("7. PI4 Formularios 69.2 % (18 de 26)", "69.2" in t and ("18 de 26" in t or "$18$ de $26$" in t)),
        ("7. PI4 Recibos 91.7 % (11 de 12)", "91.7" in t and ("11 de 12" in t or "$11$ de $12$" in t)),
        ("8. Tabla XV Turquía Oral B. (2; [50], [64]) y Sayallar C. (1; [100])", "Oral B. (2; [50], [64])" in t and "Sayallar C. (1; [100])" in t)
    ]

    all_ok = True
    for desc, res in tests:
        status = "PASS" if res else "FAIL"
        if not res:
            all_ok = False
        print(f"[{status}] {desc}")
    print(f"RESULT: {'100 % APROBADO' if all_ok else 'HAY FALLOS'}\n")
    return all_ok

if __name__ == '__main__':
    r1 = verify('project/resultados/scripts/build_resultados_completo_docx.py')
    r2 = verify('project/resultados/scripts/build_full_resultados_markdown.py')
    r3 = verify('project/metodologia/scripts/build_combined_ieee_article.py')
    if r1 and r2 and r3:
        print(">>> TODOS LOS CHECKS VERIFICADOS AL 100 % CON EXITO EN LOS 3 ARCHIVOS <<<")
    else:
        print(">>> SE DETECTARON FALLOS EN LA VERIFICACION <<<")

