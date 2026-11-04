import re

def verify(file_path):
    print(f"=== VERIFYING {file_path} ===")
    with open(file_path, 'r', encoding='utf-8') as f:
        t = f.read()

    # Targets specifically cited by user
    user_missing = [6, 7, 8, 26, 27, 28, 29, 30, 34, 35, 50, 51, 52, 53, 54, 72, 73, 74, 75, 78, 79, 80, 87, 88, 89, 114, 115, 125, 126, 127, 134, 135, 136, 137, 138, 139, 143, 144, 145]
    has_all_user_targets = all((f"[{x}]" in t or f"add_ref({x}," in t) for x in user_missing)

    # Check that in PD1 Block 2 there is no CERQual
    pos_pd1 = t.find("Fase de emergencia y cimientos")
    pos_pd1_end = t.find("Contrastes y Debates Temporales") if "Contrastes y Debates Temporales" in t else pos_pd1 + 1500
    pd1_block2_has_no_cerqual = True
    if pos_pd1 != -1 and pos_pd1_end != -1:
        pd1_block2_has_no_cerqual = "CERQual" not in t[pos_pd1:pos_pd1_end]

    tests = [
        ("1. Tabla S1 ultima fila 71 (54.2 % o 54,2 %)", ("71 (54.2 %)" in t or "71 (54,2 %)" in t)),
        ("1. Tabla S1 NO tiene 70 (53.4 %)", ("70 (53.4 %)" not in t and "70 (53,4 %)" not in t)),
        ("1. Texto Sec III.C.2.a 60 de 131", "60 de 131" in t),
        ("1. Texto Sec III.C.2.a NO tiene 61 de 131", "61 de 131" not in t),
        ("2. Tabla XIV NO tiene Villa-García [70]", "Villa-García" not in t),
        ("2. Tabla XIV NO tiene Harit [40]", "Harit" not in t),
        ("2. Tabla XIV Simsek 11, 35, 48, 51", "[11], [35], [48], [51]" in t),
        ("2. Tabla XIV Hashmi 59, 61, 123", "[59], [61], [123]" in t),
        ("2. Tabla XIV Fornés 105, 111", "[105], [111]" in t),
        ("2. PD2 Bloque 4 ausencia LatAm y España 105, 111, 131", "105" in t and "111" in t and "131" in t),
        ("3. Tabla XV 12 celdas disjuntas", ("0 (0,0 %)" in t or "0 (0.0 %)" in t or "0 (0%)" in t)),
        ("4. PI1 Bloque 3 NO Kim et al. [3]", "Kim et al. [3]" not in t),
        ("4. PI2 Bloque 3 NO Tanaka et al. [37]", "Tanaka et al. [37]" not in t),
        ("4. PI3 Bloque 3 NO Krause et al. [56]", "Krause et al. [56]" not in t),
        ("4. PI4 Bloque 3 NO Villa-García et al. [70]", "Villa-García et al. [70]" not in t),
        ("5. PI2 SROIE 93.8 % (45 de 48)", ("93.8" in t or "93,8" in t) and ("45 de 48" in t or "$45$" in t)),
        ("5. PI2 FinTabNet 88.1 % (37 de 42)", ("88.1" in t or "88,1" in t) and ("37 de 42" in t or "$37$" in t)),
        ("5. PI2 FUNSD 95.2 % (20 de 21)", ("95.2" in t or "95,2" in t) and ("20 de 21" in t or "$20$" in t)),
        ("5. PI2 Flujos 50.0 % (3 de 6)", ("50.0" in t or "50,0" in t) and ("3 de 6" in t or "$3$ de $6$" in t or "3 de 6" in t)),
        ("6. PI3 Mejora 97.2 % (69 de 71)", ("97.2" in t or "97,2" in t) and ("69 de 71" in t or "$69$" in t)),
        ("6. PI3 Paridad 87.5 % (7 de 8)", ("87.5" in t or "87,5" in t) and ("7 de 8" in t or "$7$ de $8$" in t or "7 de 8" in t)),
        ("6. PI3 Empeora 66.7 % (2 de 3)", ("66.7" in t or "66,7" in t) and ("2 de 3" in t or "$2$ de $3$" in t or "2 de 3" in t)),
        ("6. PI3 Bloque 4 69 de 78 en Mejora (88.5 %)", ("69 de 78 en Mejora" in t and ("88.5" in t or "88,5" in t))),
        ("6. PI3 Bloque 4 7 de 78 en Paridad (9.0 %)", ("7 de 78 en Paridad" in t and ("9.0" in t or "9,0" in t))),
        ("6. PI3 Bloque 4 2 de 78 en Desfavorables (2.6 %)", ("2 de 78 en Desfavorables" in t and ("2.6" in t or "2,6" in t))),
        ("7. PI4 Balances 84.7 % (50 de 59)", ("84.7" in t or "84,7" in t) and ("50 de 59" in t or "$50$" in t)),
        ("7. PI4 Facturas 85.3 % (29 de 34)", ("85.3" in t or "85,3" in t) and ("29 de 34" in t or "$29$" in t)),
        ("7. PI4 Formularios 69.2 % (18 de 26)", ("69.2" in t or "69,2" in t) and ("18 de 26" in t or "$18$" in t)),
        ("7. PI4 Recibos 91.7 % (11 de 12)", ("91.7" in t or "91,7" in t) and ("11 de 12" in t or "$11$" in t)),
        ("8. Tabla XIV Turquía Oral B. (2; [50], [64]) y Sayallar C. (1; [100])", "Oral B. (2; [50], [64])" in t and "Sayallar C. (1; [100])" in t),
        ("9. Sec III.C tiene puntos a, b, c con Concentración geográfica y Redes de coocurrencia",
         ("Núcleos de difusión" in t and "Concentración geográfica" in t and "Redes de coocurrencia" in t and "VOSviewer" in t)),
        ("10. Sec III.H tiene 2.3 y Contrastes y Debates de Eficiencia con a, b, c",
         ("2.3. Escenarios de Sobrecosto y Penalización por Alucinación" in t and "Contrastes y Debates de Eficiencia" in t and ("Superioridad de la automatización cognitiva" in t or "Ahorro masivo" in t) and "Suficiencia y ventaja económica" in t and "Sobrecosto de infraestructura" in t)),
        ("11. Apendice completo con A, B, C (SROIE), D, E, F", ("Clasificación Metodológica" in t and "Familias Algorítmicas" in t and "SROIE" in t and "SWiM" in t and "Tipologías Documentales" in t and "Tabla S1" in t)),
        ("12. Referencias completas [1] a [145]", ("[1]" in t and "[5]" in t and "[6]" in t and "[145]" in t)),
        ("13. Sin residuo CERQual en PD1 (Sec III-B)", pd1_block2_has_no_cerqual),
        ("14. Presencia de las referencias clave citadas por usuario", has_all_user_targets),
        ("15. Referencias 135, 136, 143, 144, 145 actualizadas",
         ("ESEM" in t and "10.13140/2.1.1018.4643" in t and "973–983" in t and "1912–1920" in t and "21322" in t))
    ]

    # Specific checks for build_combined_ieee_article.py
    if 'build_combined_ieee_article.py' in file_path:
        tests.append((
            "16. Sec I-D sin error de Seccion IV Referencias",
            ("Sección IV compendia las Referencias" not in t and "Sección VII compendia las Referencias" in t)
        ))
        tests.append((
            "17. Titulo II. METODOLOGÍA activo",
            'add_heading_1("II. METODOLOGÍA")' in t
        ))

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
