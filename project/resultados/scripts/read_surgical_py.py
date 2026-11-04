with open('project/resultados/scripts/surgical_editor_docx.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines[15:45], start=16):
    print(f'{i}: {repr(l)}')

