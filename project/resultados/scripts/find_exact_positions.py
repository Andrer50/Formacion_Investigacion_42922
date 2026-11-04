with open('project/metodologia/scripts/build_combined_ieee_article.py', 'r', encoding='utf-8') as f:
    text = f.read()

targets = [
    ('Item 1 (I-B 3))', 'Aislamiento Transaccional'),
    ('Item 2 (III-F Apertura/2.1)', 'Partición temática unívoca auditada'),
    ('Item 3 (III-G 2.4)', '2.4. Flujos Corporativos Integrados y Lotes Documentales Heterogéneos'),
    ('Item 4 (III-H 2.1)', '2.1. Reducción del Tiempo de Procesamiento'),
    ('Item 5 (III-I)', 'I. Mapeo de Tipologías Documentales'),
    ('Item 6 (IV-B)', 'B. Brecha de Transferencia e Integración en Sistemas ERP y CRM')
]

for name, tgt in targets:
    p = text.find(tgt)
    print(f'{name}: pos={p}')
    if p != -1:
        print('  Snippet:', repr(text[p-40:p+120]))

