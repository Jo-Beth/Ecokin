from pathlib import Path
from markdown import markdown
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib import colors

source = Path('docs/rapport_final.md')
out = Path('docs/rapport_final.pdf')

text = source.read_text(encoding='utf-8')
html = markdown(text, extensions=['fenced_code', 'tables'])

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='TitleStyle', parent=styles['Title'], fontName='Helvetica-Bold', fontSize=20, leading=24, textColor=colors.HexColor('#1f5f3c'), spaceAfter=12))
styles.add(ParagraphStyle(name='BodyStyle', parent=styles['BodyText'], fontName='Helvetica', fontSize=10.5, leading=14, spaceAfter=6))
styles.add(ParagraphStyle(name='BulletStyle', parent=styles['BodyText'], fontName='Helvetica', fontSize=10.5, leading=14, leftIndent=12, bulletIndent=0, spaceAfter=4))
styles.add(ParagraphStyle(name='Heading1Style', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=14, leading=18, textColor=colors.HexColor('#2e7d32'), spaceAfter=8, spaceBefore=12))
styles.add(ParagraphStyle(name='Heading2Style', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=12, leading=14, textColor=colors.HexColor('#356859'), spaceAfter=6, spaceBefore=8))

story = []
story.append(Paragraph('Rapport final - Écokin', styles['TitleStyle']))
story.append(Spacer(1, 0.1*inch))

# Simple markdown-to-Story conversion
for line in text.splitlines():
    stripped = line.strip()
    if not stripped:
        story.append(Spacer(1, 0.08*inch))
    elif stripped.startswith('# '):
        story.append(Paragraph(stripped[2:], styles['Heading1Style']))
    elif stripped.startswith('## '):
        story.append(Paragraph(stripped[3:], styles['Heading2Style']))
    elif stripped.startswith('- '):
        story.append(Paragraph(stripped[2:], styles['BulletStyle']))
    else:
        story.append(Paragraph(stripped, styles['BodyStyle']))

story.append(PageBreak())

# Build PDF
pdf = SimpleDocTemplate(str(out), pagesize=letter, title='Rapport final Écokin', author='Écokin')
pdf.build(story)
print(f'PDF generated: {out.resolve()}')
