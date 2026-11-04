import docx
from docx.shared import Pt
import re

def fix_headings(manuscript_path, resultados_path):
    print("=" * 70)
    print("REPARANDO ENCABEZADOS Y NEGRILLAS EN MANUSCRITOS IEEE")
    print("=" * 70)

    # 1. Manuscrito principal project/shared/RSL_Sergio_Rupay.docx
    doc = docx.Document(manuscript_path)
    
    # Locate Subsección I (Resultados)
    p_sub_i = None
    p_sub_iv_b = None
    p_brecha_2 = None

    for i, p in enumerate(doc.paragraphs):
        t = p.text.strip()
        if t.startswith("I. Tipologías Documentales y Validación en Sistemas ERP/CRM"):
            p_sub_i = p
            print(f"Encontrada Subsección I en P{i}: {repr(t[:60])}")
        elif t.startswith("B. Brecha de Transferencia Industrial y Desconexión Transaccional"):
            p_sub_iv_b = p
            print(f"Encontrada Subsección IV-B en P{i}: {repr(t[:60])}")
        elif t.startswith("2) Sesgos y Desconexión de los Bancos de Pruebas (Benchmarks):"):
            p_brecha_2 = p
            print(f"Encontrada Brecha 2 en P{i}: {repr(t[:60])}")

    # Fix Subsección I
    if p_sub_i:
        full_text = p_sub_i.text
        p_sub_i.text = "" # clear runs
        r = p_sub_i.add_run(full_text)
        r.font.name = "Times New Roman"
        r.font.size = Pt(9.5)
        r.bold = True
        r.italic = True
        p_sub_i.paragraph_format.space_before = Pt(8)
        p_sub_i.paragraph_format.space_after = Pt(2)
        p_sub_i.paragraph_format.keep_with_next = True
        print("  -> Subsección I formateada a Times New Roman 9.5 pt, Negrita, Cursiva.")

    # Fix Subsección IV-B
    if p_sub_iv_b:
        full_text = p_sub_iv_b.text
        p_sub_iv_b.text = "" # clear runs
        r = p_sub_iv_b.add_run(full_text)
        r.font.name = "Times New Roman"
        r.font.size = Pt(9.5)
        r.bold = True
        r.italic = True
        p_sub_iv_b.paragraph_format.space_before = Pt(8)
        p_sub_iv_b.paragraph_format.space_after = Pt(2)
        p_sub_iv_b.paragraph_format.keep_with_next = True
        print("  -> Subsección IV-B formateada a Times New Roman 9.5 pt, Negrita, Cursiva.")

    # Fix Brecha 2 in Section I-B
    if p_brecha_2:
        prefix = "2) Sesgos y Desconexión de los Bancos de Pruebas (Benchmarks): "
        if prefix in p_brecha_2.text:
            body_text = p_brecha_2.text.replace(prefix, "")
            p_brecha_2.text = "" # clear runs
            r1 = p_brecha_2.add_run(prefix)
            r1.font.name = "Times New Roman"
            r1.font.size = Pt(10)
            r1.bold = True
            r2 = p_brecha_2.add_run(body_text)
            r2.font.name = "Times New Roman"
            r2.font.size = Pt(10)
            r2.bold = False
            print("  -> Brecha 2 prefijo formateado a Negrita.")

    doc.save(manuscript_path)
    print(f"Guardado exitoso de {manuscript_path}\n")

    # 2. Documento de Resultados project/resultados/Articulo_RSL_Resultados_Completo_IEEE.docx
    doc_res = docx.Document(resultados_path)
    p_res_i = None
    for i, p in enumerate(doc_res.paragraphs):
        t = p.text.strip()
        if t.startswith("I. Tipologías Documentales y Validación en Sistemas ERP/CRM"):
            p_res_i = p
            print(f"Encontrada Subsección I en doc_res P{i}: {repr(t[:60])}")
            break

    if p_res_i:
        full_text = p_res_i.text
        p_res_i.text = ""
        r = p_res_i.add_run(full_text)
        r.font.name = "Times New Roman"
        r.font.size = Pt(10.0)
        r.bold = True
        p_res_i.paragraph_format.space_before = Pt(10)
        p_res_i.paragraph_format.space_after = Pt(3)
        p_res_i.paragraph_format.keep_with_next = True
        print("  -> Subsección I en doc_res formateada a Times New Roman 10 pt, Negrita.")

    doc_res.save(resultados_path)
    print(f"Guardado exitoso de {resultados_path}\n")

if __name__ == '__main__':
    fix_headings(
        'project/shared/RSL_Sergio_Rupay.docx',
        'project/resultados/Articulo_RSL_Resultados_Completo_IEEE.docx'
    )

