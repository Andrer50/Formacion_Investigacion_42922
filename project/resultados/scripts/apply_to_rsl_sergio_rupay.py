import docx
from docx.shared import Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
import sys

def apply():
    docx_path = 'project/shared/RSL_Sergio_Rupay.docx'
    try:
        doc = docx.Document(docx_path)
    except Exception as e:
        print(f"Error reading {docx_path}: {e}")
        return False

    target_table = None
    for t in doc.tables:
        if len(t.rows) > 0:
            header_texts = [c.text.strip() for c in t.rows[0].cells]
            if len(header_texts) >= 2 and "Año de Publicación" in header_texts[0] and "Estudios Primarios" in header_texts[1]:
                target_table = t
                break

    if target_table is None:
        print("TABLA XIII already modified or not found.")
        return True

    # Remove cell at index 1 for each row
    for row in target_table.rows:
        cell = row.cells[1]
        tc = cell._tc
        tc.getparent().remove(tc)

    # Remove gridCol from tblGrid if present
    grid = target_table._tbl.find(docx.oxml.ns.qn('w:tblGrid'))
    if grid is not None:
        gridCols = grid.findall(docx.oxml.ns.qn('w:gridCol'))
        if len(gridCols) > 1:
            grid.remove(gridCols[1])

    widths = [Inches(1.8), Inches(1.6), Inches(1.6), Inches(1.6)]
    for row in target_table.rows:
        for idx, width in enumerate(widths):
            cell = row.cells[idx]
            cell.width = width
            for p in cell.paragraphs:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    try:
        doc.save(docx_path)
        print(f"Successfully saved {docx_path}!")
        return True
    except PermissionError:
        print(f"PERMISSION ERROR: {docx_path} is currently locked by Word.")
        return False

if __name__ == '__main__':
    res = apply()
    if not res:
        sys.exit(1)

