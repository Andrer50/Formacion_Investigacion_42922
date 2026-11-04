for path in [
    'project/metodologia/scripts/build_combined_ieee_article.py',
    'project/resultados/scripts/build_resultados_completo_docx.py'
]:
    with open(path, 'r', encoding='utf-8') as f:
        t = f.read()

    bad_snippet = '''    bold_prefix="2.1. Canalizaciones Híbridas (Pipelines) CNN-RNN y Segmentación Clásica con OCR: "
) CNN-RNN y Segmentación Clásica con OCR: "
)'''
    good_snippet = '''    bold_prefix="2.1. Canalizaciones Híbridas (Pipelines) CNN-RNN y Segmentación Clásica con OCR: "
)'''
    if bad_snippet in t:
        t = t.replace(bad_snippet, good_snippet)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(t)
        print(f"Fixed leftover snippet in {path}")
    else:
        print(f"Snippet not found in {path}")

