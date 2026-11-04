import docx

def remove_empty_runs(docpath):
    doc = docx.Document(docpath)
    for p in doc.paragraphs:
        if p.text.strip().startswith('Fig.'):
            # remove any run that has empty text
            for r in list(p.runs):
                if r.text == '':
                    p._element.remove(r._element)
    doc.save(docpath)

remove_empty_runs('project/shared/RSL_Sergio_Rupay.docx')
remove_empty_runs('project/resultados/Articulo_RSL_Resultados_Completo_IEEE.docx')
print("Cleaned up empty runs!")

