import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
import xml.etree.ElementTree as ET

def make_sect_pr(num_cols=None, space_twips=720):
    sectPr = OxmlElement('w:sectPr')
    
    type_elem = OxmlElement('w:type')
    type_elem.set(qn('w:val'), 'continuous')
    sectPr.append(type_elem)
    
    pgSz = OxmlElement('w:pgSz')
    pgSz.set(qn('w:w'), '12240')
    pgSz.set(qn('w:h'), '15840')
    sectPr.append(pgSz)
    
    pgMar = OxmlElement('w:pgMar')
    pgMar.set(qn('w:top'), '1080')
    pgMar.set(qn('w:right'), '1080')
    pgMar.set(qn('w:bottom'), '1080')
    pgMar.set(qn('w:left'), '1080')
    pgMar.set(qn('w:header'), '576')
    pgMar.set(qn('w:footer'), '576')
    pgMar.set(qn('w:gutter'), '0')
    sectPr.append(pgMar)
    
    cols = OxmlElement('w:cols')
    cols.set(qn('w:space'), str(space_twips))
    if num_cols is not None:
        cols.set(qn('w:num'), str(num_cols))
    sectPr.append(cols)
    
    docGrid = OxmlElement('w:docGrid')
    docGrid.set(qn('w:linePitch'), '360')
    sectPr.append(docGrid)
    
    return sectPr

def create_break_p(sectPr):
    p = OxmlElement('w:p')
    pPr = OxmlElement('w:pPr')
    pPr.append(sectPr)
    p.append(pPr)
    return p

def format_table_22(docx_path):
    print(f"Applying Option A (full-width 2-column span) to Table XXII in {docx_path}...")
    doc = docx.Document(docx_path)
    body = doc._body._element

    tbl_idx = None
    for idx, el in enumerate(body):
        if el.tag.endswith('tbl'):
            t = docx.table.Table(el, doc)
            if len(t.columns) == 7 and 'Preg.' in t.rows[0].cells[0].text:
                tbl_idx = idx
                break

    if tbl_idx is None:
        raise ValueError("No se encontró la Tabla XXII en el documento.")

    title_el = body[tbl_idx - 1]
    tbl_el = body[tbl_idx]
    footnote_el = body[tbl_idx + 1]

    # Insert break before title (2 cols section ends)
    break_before = create_break_p(make_sect_pr(num_cols=2))
    body.insert(body.index(title_el), break_before)

    # Insert break after footnote (1 col section ends)
    break_after = create_break_p(make_sect_pr(num_cols=None))
    body.insert(body.index(footnote_el) + 1, break_after)

    # Now format Table XXII
    t = docx.table.Table(tbl_el, doc)
    t.alignment = docx.enum.table.WD_TABLE_ALIGNMENT.CENTER

    # Col widths in dxa (total 10080 dxa = 7.00 inches)
    # [Preg, Hallazgo, Limitaciones, Coherencia, Adecuacion, Relevancia, Certeza]
    dxa_widths = [576, 2808, 1368, 1224, 1368, 1224, 1512]
    in_widths = [w / 1440.0 for w in dxa_widths]

    # Set tblW in tblPr
    tblPr = t._tbl.tblPr
    tblW = tblPr.xpath('./w:tblW')
    if tblW:
        tblW[0].set(qn('w:type'), 'dxa')
        tblW[0].set(qn('w:w'), '10080')
    else:
        new_tblW = OxmlElement('w:tblW')
        new_tblW.set(qn('w:type'), 'dxa')
        new_tblW.set(qn('w:w'), '10080')
        tblPr.append(new_tblW)

    # Set tblCellMar (cell padding: top/bottom=60 dxa, left/right=80 dxa)
    tblCellMar = tblPr.xpath('./w:tblCellMar')
    if not tblCellMar:
        cm = OxmlElement('w:tblCellMar')
        for side, val in [('top', '60'), ('bottom', '60'), ('left', '80'), ('right', '80')]:
            node = OxmlElement(f'w:{side}')
            node.set(qn('w:w'), val)
            node.set(qn('w:type'), 'dxa')
            cm.append(node)
        tblPr.append(cm)

    # Set tblGrid
    tblGrid = t._tbl.tblGrid
    if tblGrid is not None:
        t._tbl.remove(tblGrid)
    new_tblGrid = OxmlElement('w:tblGrid')
    for w in dxa_widths:
        gc = OxmlElement('w:gridCol')
        gc.set(qn('w:w'), str(w))
        new_tblGrid.append(gc)
    t._tbl.insert(t._tbl.index(tblPr) + 1, new_tblGrid)

    # Format rows and cells
    for r_idx, row in enumerate(t.rows):
        trPr = row._tr.get_or_add_trPr()
        
        # Add cantSplit
        if not trPr.xpath('./w:cantSplit'):
            trPr.append(OxmlElement('w:cantSplit'))
            
        # Add tblHeader for row 0
        if r_idx == 0:
            if not trPr.xpath('./w:tblHeader'):
                trPr.append(OxmlElement('w:tblHeader'))

        for c_idx, cell in enumerate(row.cells):
            cell.width = Inches(in_widths[c_idx])
            tcPr = cell._tc.get_or_add_tcPr()
            
            # Set tcW
            tcW = tcPr.xpath('./w:tcW')
            if tcW:
                tcW[0].set(qn('w:type'), 'dxa')
                tcW[0].set(qn('w:w'), str(dxa_widths[c_idx]))
            else:
                new_tcW = OxmlElement('w:tcW')
                new_tcW.set(qn('w:type'), 'dxa')
                new_tcW.set(qn('w:w'), str(dxa_widths[c_idx]))
                tcPr.append(new_tcW)

            # Format cell paragraphs
            for p in cell.paragraphs:
                p.paragraph_format.space_before = Pt(1.5)
                p.paragraph_format.space_after = Pt(1.5)
                p.paragraph_format.line_spacing = 1.0
                
                # Alignment
                if c_idx == 0 or c_idx == 6:
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                else:
                    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                    
                for run in p.runs:
                    run.font.name = 'Times New Roman'
                    run.font.size = Pt(7.5)
                    if r_idx == 0:
                        run.font.bold = True

    # Title paragraph spacing
    p_title = docx.text.paragraph.Paragraph(title_el, doc)
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(6)
    p_title.paragraph_format.space_after = Pt(3)

    # Footnote paragraph spacing
    p_foot = docx.text.paragraph.Paragraph(footnote_el, doc)
    p_foot.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_foot.paragraph_format.space_before = Pt(3)
    p_foot.paragraph_format.space_after = Pt(6)

    doc.save(docx_path)
    print(f"Successfully applied Option A to {docx_path}!")

def format_resultados_table_10(docx_path):
    print(f"Updating Table 10 in {docx_path} to 7.00 in width...")
    doc = docx.Document(docx_path)
    t = doc.tables[10]
    t.alignment = docx.enum.table.WD_TABLE_ALIGNMENT.CENTER

    dxa_widths = [576, 2808, 1368, 1224, 1368, 1224, 1512]
    in_widths = [w / 1440.0 for w in dxa_widths]

    tblPr = t._tbl.tblPr
    tblW = tblPr.xpath('./w:tblW')
    if tblW:
        tblW[0].set(qn('w:type'), 'dxa')
        tblW[0].set(qn('w:w'), '10080')
    else:
        new_tblW = OxmlElement('w:tblW')
        new_tblW.set(qn('w:type'), 'dxa')
        new_tblW.set(qn('w:w'), '10080')
        tblPr.append(new_tblW)

    tblCellMar = tblPr.xpath('./w:tblCellMar')
    if not tblCellMar:
        cm = OxmlElement('w:tblCellMar')
        for side, val in [('top', '60'), ('bottom', '60'), ('left', '80'), ('right', '80')]:
            node = OxmlElement(f'w:{side}')
            node.set(qn('w:w'), val)
            node.set(qn('w:type'), 'dxa')
            cm.append(node)
        tblPr.append(cm)

    tblGrid = t._tbl.tblGrid
    if tblGrid is not None:
        t._tbl.remove(tblGrid)
    new_tblGrid = OxmlElement('w:tblGrid')
    for w in dxa_widths:
        gc = OxmlElement('w:gridCol')
        gc.set(qn('w:w'), str(w))
        new_tblGrid.append(gc)
    t._tbl.insert(t._tbl.index(tblPr) + 1, new_tblGrid)

    for r_idx, row in enumerate(t.rows):
        trPr = row._tr.get_or_add_trPr()
        if not trPr.xpath('./w:cantSplit'):
            trPr.append(OxmlElement('w:cantSplit'))
        if r_idx == 0:
            if not trPr.xpath('./w:tblHeader'):
                trPr.append(OxmlElement('w:tblHeader'))

        for c_idx, cell in enumerate(row.cells):
            cell.width = Inches(in_widths[c_idx])
            tcPr = cell._tc.get_or_add_tcPr()
            tcW = tcPr.xpath('./w:tcW')
            if tcW:
                tcW[0].set(qn('w:type'), 'dxa')
                tcW[0].set(qn('w:w'), str(dxa_widths[c_idx]))
            else:
                new_tcW = OxmlElement('w:tcW')
                new_tcW.set(qn('w:type'), 'dxa')
                new_tcW.set(qn('w:w'), str(dxa_widths[c_idx]))
                tcPr.append(new_tcW)

            for p in cell.paragraphs:
                p.paragraph_format.space_before = Pt(1.5)
                p.paragraph_format.space_after = Pt(1.5)
                p.paragraph_format.line_spacing = 1.0
                if c_idx == 0 or c_idx == 6:
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                else:
                    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                for run in p.runs:
                    run.font.name = 'Times New Roman'
                    run.font.size = Pt(7.5)
                    if r_idx == 0:
                        run.font.bold = True

    doc.save(docx_path)
    print(f"Successfully updated Table 10 in {docx_path}!")

if __name__ == '__main__':
    format_table_22('project/shared/RSL_Sergio_Rupay.docx')
    format_resultados_table_10('project/resultados/Articulo_RSL_Resultados_Completo_IEEE.docx')
