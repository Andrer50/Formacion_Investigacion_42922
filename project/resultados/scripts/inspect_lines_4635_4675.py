with open('project/metodologia/scripts/build_combined_ieee_article.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(4635, 4675):
    print(f'{i+1}: {repr(lines[i])}')

