import os
import csv
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, KeepTogether
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            super().showPage()
        super().save()

    def draw_page_number(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#444444"))
        
        # Header (pages > 1)
        if self._pageNumber > 1:
            self.drawString(54, 11 * inch - 36, "RSL — Compendio de Estudios Nucleares (4/4) | UTP 2026")
            self.setStrokeColor(colors.HexColor("#CCCCCC"))
            self.setLineWidth(0.5)
            self.line(54, 11 * inch - 40, 8.5 * inch - 54, 11 * inch - 40)
            
        # Footer
        text = f"Página {self._pageNumber} de {page_count}"
        self.drawRightString(8.5 * inch - 54, 36, text)
        self.drawString(54, 36, "Formación para la Investigación — Proyecto RSL Automatización Documental")
        self.setStrokeColor(colors.HexColor("#CCCCCC"))
        self.setLineWidth(0.5)
        self.line(54, 46, 8.5 * inch - 54, 46)
        self.restoreState()

def build_pdf(csv_path, output_pdf_path):
    doc = SimpleDocTemplate(
        output_pdf_path,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()
    
    # Custom Typography Styles (Clean, academic, default-oriented)
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=19,
        textColor=colors.HexColor("#111111"),
        alignment=1, # Center
        spaceAfter=4
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14,
        textColor=colors.HexColor("#333333"),
        alignment=1,
        spaceAfter=12
    )

    meta_style = ParagraphStyle(
        'MetaStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor("#222222")
    )
    
    card_title_style = ParagraphStyle(
        'CardTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11.5,
        leading=15,
        textColor=colors.HexColor("#111111")
    )

    label_style = ParagraphStyle(
        'LabelStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=12,
        textColor=colors.HexColor("#222222")
    )

    val_style = ParagraphStyle(
        'ValStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12,
        textColor=colors.HexColor("#222222")
    )

    link_style = ParagraphStyle(
        'LinkStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=12,
        textColor=colors.HexColor("#003366")
    )

    contrib_style = ParagraphStyle(
        'ContribStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor("#111111")
    )

    story = []

    # Title & Header
    story.append(Paragraph("UNIVERSIDAD TECNOLÓGICA DEL PERÚ", ParagraphStyle('Inst', parent=title_style, fontSize=10, leading=13, textColor=colors.HexColor("#444444"))))
    story.append(Paragraph("FACULTAD DE INGENIERÍA DE SISTEMAS Y ELECTRÓNICA", ParagraphStyle('Inst2', parent=title_style, fontSize=9, leading=12, textColor=colors.HexColor("#555555"), spaceAfter=6)))
    story.append(Paragraph("COMPENDIO DE ESTUDIOS NUCLEARES (4/4)", title_style))
    story.append(Paragraph("Revisión Sistemática de Literatura: Inteligencia Artificial para la Automatización del Registro y Validación de Documentos Empresariales", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#222222"), spaceAfter=10))

    # Context explanation box
    desc_text = (
        "<b>Nota Metodológica:</b> Los siguientes <b>4 estudios nucleares</b> representan los artículos primarios "
        "de mayor relevancia e integridad de la RSL. Cada uno responde de manera simultánea y exhaustiva a las "
        "cuatro preguntas de investigación (<b>PI1:</b> Arquitectura IA, <b>PI2:</b> Métricas cuantitativas, "
        "<b>PI3:</b> Comparación frente a métodos manuales/reglas, y <b>PI4:</b> Validación en documentos empresariales/ERP). "
        "Este documento recopila las referencias completas, resúmenes técnicos, DOIs oficiales y enlaces directos para facilitar su lectura y consulta."
    )
    
    meta_table_data = [[Paragraph(desc_text, meta_style)]]
    t_meta = Table(meta_table_data, colWidths=[7.0 * inch])
    t_meta.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F6F6F6")),
        ('BOX', (0,0), (-1,-1), 0.75, colors.HexColor("#CCCCCC")),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(t_meta)
    story.append(Spacer(1, 14))

    # Read CSV data
    studies = []
    with open(csv_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get('id'):
                studies.append(row)

    # Render each study
    for idx, s in enumerate(studies, start=1):
        study_id = s.get('id', f'[S{idx:03d}]')
        title = s.get('title', 'Sin título')
        authors = s.get('authors', 'N/A')
        year = s.get('year', 'N/A')
        source_title = s.get('source_title', 'N/A')
        doi = s.get('doi', '').strip()
        doc_type = s.get('doc_type', 'N/A')
        source_db = s.get('source_db', 'N/A')
        contrib = s.get('summary_contribution', 'N/A')
        
        doi_url = f"https://doi.org/{doi}" if doi else "N/A"
        scholar_url = f"https://scholar.google.com/scholar?q={title.replace(' ', '+')}"

        card_data = [
            # Header row
            [Paragraph(f"<b>{study_id} — {title}</b> ({year})", card_title_style), ""],
            # Metadata fields
            [Paragraph("Autores:", label_style), Paragraph(authors, val_style)],
            [Paragraph("Publicación / Editorial:", label_style), Paragraph(f"{source_title} ({doc_type})", val_style)],
            [Paragraph("Base Indexada:", label_style), Paragraph(f"<b>{source_db}</b> — Clasificación: <b>Estudio Nuclear (4/4 PIs)</b>", val_style)],
            [Paragraph("Identificador DOI:", label_style), Paragraph(f'<link href="{doi_url}"><u>{doi}</u></link>', link_style)],
            [Paragraph("Enlace Directo (DOI):", label_style), Paragraph(f'<link href="{doi_url}"><u>{doi_url}</u></link>', link_style)],
            [Paragraph("Búsqueda en Scholar:", label_style), Paragraph(f'<link href="{scholar_url}"><u>Buscar en Google Scholar (Acceso / Citas)</u></link>', link_style)],
            [Paragraph("Aporte Técnico Clave:", label_style), Paragraph(contrib, contrib_style)],
            [Paragraph("Cobertura PIs:", label_style), Paragraph("<b>PI1:</b> Sí | <b>PI2:</b> Sí | <b>PI3:</b> Sí | <b>PI4:</b> Sí &nbsp; (100% Cobertura)", val_style)],
        ]

        t_card = Table(card_data, colWidths=[1.6 * inch, 5.4 * inch])
        t_card.setStyle(TableStyle([
            ('SPAN', (0,0), (1,0)),
            ('BACKGROUND', (0,0), (1,0), colors.HexColor("#EAEAEA")),
            ('BACKGROUND', (0,1), (-1,-1), colors.HexColor("#FFFFFF")),
            ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#222222")),
            ('INNERGRID', (0,1), (-1,-1), 0.5, colors.HexColor("#E0E0E0")),
            ('LINEBELOW', (0,0), (1,0), 1, colors.HexColor("#222222")),
            ('TOPPADDING', (0,0), (-1,-1), 5),
            ('BOTTOMPADDING', (0,0), (-1,-1), 5),
            ('LEFTPADDING', (0,0), (-1,-1), 7),
            ('RIGHTPADDING', (0,0), (-1,-1), 7),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ]))

        study_block = [t_card, Spacer(1, 14)]
        story.append(KeepTogether(study_block))

    # Search & Access Quick Guide Section
    guide_title = Paragraph("<b>GUÍA RÁPIDA DE BÚSQUEDA Y DESCARGA INSTITUCIONAL</b>", card_title_style)
    guide_text = (
        "1. <b>Acceso por DOI directo:</b> Haga clic en el enlace DOI de cada ficha para acceder a la página oficial de la editorial (ACM, ACL Anthology, IEEE Xplore o Springer).<br/>"
        "2. <b>Descarga institucional:</b> Si el documento solicita suscripción, ingrese a través del portal de biblioteca virtual de la <b>UTP</b> o el portal de <b>Concytec / Scopus / WoS</b> para habilitar la descarga del PDF completo.<br/>"
        "3. <b>Acceso alternativo / Preprints:</b> Haga clic en el enlace de <i>Google Scholar</i> incluido en cada ficha para verificar versiones abiertas o repositorios de los autores (ej. ArXiv, ResearchGate, ACL Anthology)."
    )
    
    t_guide = Table([[guide_title], [Paragraph(guide_text, meta_style)]], colWidths=[7.0 * inch])
    t_guide.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#FAFAFA")),
        ('BOX', (0,0), (-1,-1), 0.75, colors.HexColor("#888888")),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(KeepTogether([t_guide]))

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"PDF successfully generated at: {output_pdf_path}")

if __name__ == "__main__":
    csv_file = r"c:\Users\HP\Desktop\ESCRITORIO\PROYECTOS UNIVERSIDAD\Formacion_Investigacion_42922\project\metodologia\outputs\corpus_estudios_nucleares_4_4.csv"
    pdf_out = r"c:\Users\HP\Desktop\ESCRITORIO\PROYECTOS UNIVERSIDAD\Formacion_Investigacion_42922\project\metodologia\outputs\Estudios_Nucleares_4_4_Compendio.pdf"
    build_pdf(csv_file, pdf_out)
