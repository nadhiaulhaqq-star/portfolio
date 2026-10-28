from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

pdf_path = r"C:\Users\Lenovo\porto\CV_Nadhia_Ulhaq_New.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=A4, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
story = []

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    'CVTitle',
    parent=styles['Heading1'],
    fontName='Helvetica-Bold',
    fontSize=24,
    leading=28,
    textColor=colors.HexColor('#111827')
)

subtitle_style = ParagraphStyle(
    'CVSubtitle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=11,
    leading=14,
    textColor=colors.HexColor('#E11D47')
)

contact_style = ParagraphStyle(
    'CVContact',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=9,
    leading=13,
    textColor=colors.HexColor('#4B5563'),
    alignment=2
)

section_heading = ParagraphStyle(
    'CVSection',
    parent=styles['Heading2'],
    fontName='Helvetica-Bold',
    fontSize=11,
    leading=14,
    textColor=colors.HexColor('#E11D47'),
    spaceBefore=12,
    spaceAfter=4
)

body_style = ParagraphStyle(
    'CVBody',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=9.5,
    leading=14,
    textColor=colors.HexColor('#374151')
)

header_data = [
    [
        Paragraph("NADHIA ULHAQ", title_style),
        Paragraph("📧 nadhiaulhaqq@gmail.com<br/>📱 +62 881-0824-66308<br/>📍 Jakarta / Semarang, Indonesia", contact_style)
    ]
]
header_table = Table(header_data, colWidths=[3.2*inch, 3.5*inch])
header_table.setStyle(TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('LEFTPADDING', (0,0), (-1,-1), 0),
    ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ('BOTTOMPADDING', (0,0), (-1,-1), 4),
]))
story.append(header_table)
story.append(Paragraph("Fresh Graduate S1 Manajemen — Universitas Stikubank (IPK 3,59)", subtitle_style))
story.append(Spacer(1, 8))
story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#E5E7EB'), spaceBefore=2, spaceAfter=8))

# Profil Profesional
story.append(Paragraph("PROFIL PROFESIONAL", section_heading))
profile_text = "Fresh Graduate S1 Manajemen dari Universitas Stikubank dengan IPK 3,59. Memiliki fokus pada manajemen bisnis, administrasi, pemasaran, digital marketing, serta pengolahan data. Memiliki pengalaman praktik dalam penyusunan laporan keuangan, perhitungan pajak, dan promosi digital melalui Google Ads serta Facebook Ads. Pribadi yang disiplin, teliti, dan bertanggung jawab. Mampu beradaptasi dengan lingkungan baru dan dapat bekerja secara mandiri maupun dalam tim."
story.append(Paragraph(profile_text, body_style))

# Pendidikan
story.append(Paragraph("PENDIDIKAN", section_heading))
edu_data = [
    [
        Paragraph("<b>Universitas Stikubank (UNISBANK) Semarang</b><br/>S1 Manajemen — Manajemen Bisnis & Operasional", body_style),
        Paragraph("<b>IPK 3,59 / 4.00</b>", ParagraphStyle('IPKRight', parent=body_style, alignment=2, fontName='Helvetica-Bold', textColor=colors.HexColor('#E11D47')))
    ]
]
edu_table = Table(edu_data, colWidths=[5.2*inch, 1.5*inch])
edu_table.setStyle(TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('LEFTPADDING', (0,0), (-1,-1), 0),
    ('RIGHTPADDING', (0,0), (-1,-1), 0),
]))
story.append(edu_table)

# Keahlian
story.append(Paragraph("KEAHLIAN & KETERAMPILAN", section_heading))
skills_data = [
    [
        Paragraph("<b>Keahlian Teknis (Hardskill):</b><br/>"
                  "• Digital Marketing<br/>"
                  "• Periklanan<br/>"
                  "• Konten Media Sosial<br/>"
                  "• Riset Pasar<br/>"
                  "• Analisis Data<br/>"
                  "• Manajemen Operasional<br/>"
                  "• Manajemen Keuangan<br/>"
                  "• Social Media Marketing", body_style),
        Paragraph("<b>Keahlian Interpersonal (Softskill):</b><br/>"
                  "• Komunikasi efektif<br/>"
                  "• Team Work<br/>"
                  "• Manajemen waktu<br/>"
                  "• Kepemimpinan<br/>"
                  "• Adaptabilitas<br/>"
                  "• Marketing<br/>"
                  "• Problem Solving", body_style)
    ]
]
skills_table = Table(skills_data, colWidths=[3.4*inch, 3.3*inch])
skills_table.setStyle(TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('LEFTPADDING', (0,0), (-1,-1), 0),
    ('RIGHTPADDING', (0,0), (-1,-1), 0),
]))
story.append(skills_table)

# Sertifikasi
story.append(Paragraph("SERTIFIKASI & PELATIHAN", section_heading))
certs = [
    ("Sertifikat Profesi Digital Marketing", "Badan Nasional Sertifikasi Profesi (BNSP)", "2026 - 2029"),
    ("EnglishScore - Skor 472", "British Council", "2026 - 2028"),
    ("Public Speaking & Storytelling", "Dibimbing", "2026"),
    ("Data Analytics", "Dibimbing", "2026"),
    ("Microsoft Excel Bootcamp", "KarirNex", "2026"),
    ("Digital Marketing", "Mini Course", "2025"),
    ("Become a Smart Entrepreneur", "Wismilak Foundation", "2024")
]

for title, org, year in certs:
    cert_table = Table([[
        Paragraph(f"• <b>{title}</b> — {org}", body_style),
        Paragraph(year, ParagraphStyle('YearRight', parent=body_style, alignment=2, fontName='Helvetica-Bold', textColor=colors.HexColor('#6B7280')))
    ]], colWidths=[5.8*inch, 0.9*inch])
    cert_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(cert_table)

doc.build(story)
print("PDF successfully updated at:", pdf_path)
