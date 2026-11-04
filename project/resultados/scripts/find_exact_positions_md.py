with open('project/resultados/scripts/build_full_resultados_markdown.py', 'r', encoding='utf-8') as f:
    text = f.read()

targets = [
    ('Item 2 (III-F Apertura/2.1)', 'Bloque 1 — Apertura\nCiento cinco estudios'),
    ('Item 3 (III-G 2.4)', 'Flujos Corporativos Integrados'),
    ('Item 4 (III-H 2.1)', '2.1. Reducción del Tiempo de Procesamiento'),
    ('Item 5 (III-I)', 'I. Mapeo de Tipologías Documentales')
]

for name, tgt in targets:
    p = text.find(tgt)
    print(f'{name}: pos={p}')
    if p != -1:
        print('  Snippet:', repr(text[p-40:p+120]))

