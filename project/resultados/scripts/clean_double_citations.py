import docx
import os

PATTERNS = [
    ' (Iqbal et al. [12]; Kim C.-Y. et al. [54]; Lee E. et al. [71]; Kiatphaisansophon et al. [88])',
    ' (Wei et al. [3]; Chen L.-C. et al. [4]; Mifsud et al. [6]; Hu et al. [19]; Levich & Knust [25]; Hemmer et al. [115])',
    ' (Abdalla et al. [17]; Lin Y.M. et al. [27]; Chen Z. et al. [37])',
    ' (Chen L.-C. et al. [4]; Mifsud et al. [6]; Yu et al. [7]; Luo C. et al. [9]; Nguyen M.-T. et al. [67]; Yan et al. [74])',
    ' (Zhou et al. [30]; Hertlein et al. [39]; Zhang H. et al. [57]; Sayallar et al. [100]; Yeung et al. [102])',
    ' (Iqbal et al. [12]; Oral et al. [64]; Tata et al. [112])',
    ' (Liu Z. [28]; Guha et al. [45]; Kim C.-Y. et al. [54]; Oral et al. [64]; Tata et al. [112])',
    ' (Chen Z. et al. [37]; Chen Y. et al. [56]; Lai P. et al. [121])',
    ' (Sassioui et al. [8]; Tiwari et al. [10]; Ma C. et al. [41]; Akkaya et al. [51]; Hashmi et al. [61])',
    ' (Oral et al. [64]; Tata et al. [112]; Sainz-De-Abajo et al. [131])',
    ' (Manjunath et al. [44]; Tobaben et al. [116]; Azman et al. [127])'
]

# Additional older pattern in build_combined_ieee_article.py
EXTRA_PATTERN = ' (Chen L.-C. et al. [4]; Xiao et al. [11]; Saeed et al. [16]; Nguyen M.-T. et al. [67]; Yang Z. et al. [80])'

def clean_docx(filepath):
    print(f'Cleaning docx: {filepath}...')
    doc = docx.Document(filepath)
    replaced_count = 0
    for p in doc.paragraphs:
        for r in p.runs:
            for pat in PATTERNS:
                if pat in r.text:
                    r.text = r.text.replace(pat, '')
                    replaced_count += 1
    doc.save(filepath)
    print(f'  -> Replaced {replaced_count} parenthetical patterns in {filepath}')

def clean_text_file(filepath, patterns_list):
    print(f'Cleaning text file: {filepath}...')
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    count = 0
    for pat in patterns_list:
        if pat in content:
            content = content.replace(pat, '')
            count += 1
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'  -> Replaced {count} parenthetical patterns in {filepath}')

if __name__ == '__main__':
    clean_docx('project/shared/RSL_Sergio_Rupay.docx')
    clean_docx('project/resultados/Articulo_RSL_Resultados_Completo_IEEE.docx')
    clean_text_file('project/resultados/main.md', PATTERNS)
    clean_text_file('project/resultados/scripts/build_resultados_completo_docx.py', PATTERNS)
    clean_text_file('project/metodologia/scripts/build_combined_ieee_article.py', PATTERNS + [EXTRA_PATTERN])
    print('All files successfully updated!')

