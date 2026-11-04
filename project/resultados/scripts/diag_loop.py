import docx

doc = docx.Document('project/shared/RSL_Sergio_Rupay.docx')

for i in range(130, 145):
    p = doc.paragraphs[i]
    print(f"P{i}: startswith 1) Apertura: -> {p.text.startswith('1) Apertura:')}")
    print(f"P{i}: startswith 2.1. Canalizaciones -> {p.text.startswith('2.1. Canalizaciones')}")

