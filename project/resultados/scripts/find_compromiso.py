with open('project/metodologia/scripts/build_combined_ieee_article.py', 'r', encoding='utf-8') as f:
    text = f.read()

p = text.find('Compromiso entre Capacidad Multimodal')
print('Found Compromiso:', p)
if p != -1:
    print(repr(text[p-100:p+200]))

p_api = [m for m in range(len(text)) if text.startswith('mediante interfaces de programación de aplicaciones (API) transaccionales.', m)]
print('Found p_api matches at:', p_api)

