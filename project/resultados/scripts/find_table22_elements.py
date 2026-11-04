import docx
from docx.oxml.text.paragraph import CT_P
from docx.oxml.table import CT_Tbl

doc = docx.Document('project/shared/RSL_Sergio_Rupay.docx')

elements = doc._body._element
for idx, el in enumerate(elements):
    if isinstance(el, CT_Tbl):
        t = docx.table.Table(el, doc)
        if len(t.columns) == 7 and 'Preg.' in t.rows[0].cells[0].text:
            print(f'Found Table XXII at element index {idx}!')
            for j in range(max(0, idx-4), min(len(elements), idx+5)):
                if isinstance(elements[j], CT_P):
                    p = docx.text.paragraph.Paragraph(elements[j], doc)
                    print(f'  Elem {j} (P): {repr(p.text[:75])}')
                elif isinstance(elements[j], CT_Tbl):
                    rows_count = len(elements[j].xpath('.//w:tr'))
                    print(f'  Elem {j} (Tbl): [Table with {rows_count} rows]')

