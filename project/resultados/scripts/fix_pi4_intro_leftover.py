for path in [
    'project/metodologia/scripts/build_combined_ieee_article.py',
    'project/resultados/scripts/build_resultados_completo_docx.py'
]:
    with open(path, 'r', encoding='utf-8') as f:
        t = f.read()

    bad_snippet = '''add_p(
    "Para determinar la aplicabilidad corporativa real de los modelos (PI4), se clasificó el universo completo del corpus (N = 131) cruzando las cuatro tipologías documentales de negocio frente a su nivel de integración técnica con plataformas empresariales ERP, CRM y DMS. La distribución cuantitativa se detalla en la Tabla XX y se representa en la matriz de calor de la Fig. 9."
) se expone en la Fig. 9."
)'''
    good_snippet = '''add_p(
    "Para determinar la aplicabilidad corporativa real de los modelos (PI4), se clasificó el universo completo del corpus (N = 131) cruzando las cuatro tipologías documentales de negocio frente a su nivel de integración técnica con plataformas empresariales ERP, CRM y DMS. La distribución cuantitativa se detalla en la Tabla XX y se representa en la matriz de calor de la Fig. 9."
)'''
    if bad_snippet in t:
        t = t.replace(bad_snippet, good_snippet)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(t)
        print(f"Fixed PI4 intro leftover in {path}")
    else:
        print(f"Snippet not found in {path}")

