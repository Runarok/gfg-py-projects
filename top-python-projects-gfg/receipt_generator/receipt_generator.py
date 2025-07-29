from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, Spacer, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm
from datetime import datetime

# ---------- CONFIG ----------
THEME = "dark"  # Options: "light" or "dark"
FILE_NAME = f"receipt_{THEME}.pdf"
ORG_NAME = "GeeksforGeeks"
FOOTER_TEXT = "Thank you for your purchase!"

# ---------- DATA ----------
items = [
    ["Date", "Item", "Duration", "Price (Rs.)"],
    ["16/11/2020", "Full Stack Development with React & Node JS - Live", "Lifetime", "10,999.00/-"],
    ["16/11/2020", "Geeks Classes: Live Session", "6 months", "9,999.00/-"],
    ["", "", "", ""],
    ["Sub Total", "", "", "20,998.00/-"],
    ["Discount", "", "", "-3,000.00/-"],
    ["Total", "", "", "17,998.00/-"],
]

# ---------- THEMES ----------
theme_colors = {
    "light": {
        "header_bg": colors.HexColor("#4B8BBE"),
        "header_text": colors.whitesmoke,
        "row_bg": colors.beige,
        "text": colors.black,
    },
    "dark": {
        "header_bg": colors.HexColor("#1e1e1e"),
        "header_text": colors.whitesmoke,
        "row_bg": colors.HexColor("#2d2d2d"),
        "text": colors.whitesmoke,
    }
}

c = theme_colors[THEME]

# ---------- CREATE PDF ----------
pdf = SimpleDocTemplate(FILE_NAME, pagesize=A4,
                        rightMargin=30, leftMargin=30, topMargin=40, bottomMargin=30)

styles = getSampleStyleSheet()
elements = []

# ---------- TITLE ----------
title_style = styles["Title"]
title_style.textColor = c["text"]
title = Paragraph(f"<b>{ORG_NAME}</b>", title_style)
elements.append(title)

# ---------- TIMESTAMP ----------
timestamp = datetime.now().strftime("%d %B %Y, %I:%M %p")
elements.append(Paragraph(f"<font size=10 color='{c['text'].hexval()}'><i>Generated on: {timestamp}</i></font>", styles["Normal"]))
elements.append(Spacer(1, 12))

# ---------- TABLE ----------
table_style = TableStyle([
    ("BOX", (0, 0), (-1, -1), 1, colors.black),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
    ("BACKGROUND", (0, 0), (-1, 0), c["header_bg"]),
    ("TEXTCOLOR", (0, 0), (-1, 0), c["header_text"]),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ("BACKGROUND", (0, 1), (-1, -2), c["row_bg"]),
    ("TEXTCOLOR", (0, 1), (-1, -1), c["text"]),
    ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
    ("FONTSIZE", (0, 0), (-1, -1), 10),
    ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
])

table = Table(items, colWidths=[40*mm, 80*mm, 30*mm, 35*mm])
table.setStyle(table_style)
elements.append(table)

# ---------- FOOTER ----------
elements.append(Spacer(1, 20))
footer = Paragraph(f"<font size=9 color='{c['text'].hexval()}'><i>{FOOTER_TEXT}</i></font>", styles["Normal"])
elements.append(footer)

# ---------- BUILD ----------
pdf.build(elements)

print(f"[✔] {THEME.capitalize()} mode receipt saved as: {FILE_NAME}")
