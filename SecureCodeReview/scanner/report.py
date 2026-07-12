from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle


def generate_pdf_report(issues, filename):

    pdf = SimpleDocTemplate(filename, pagesize=letter)

    data = [
        ["Severity", "Line", "Issue", "Recommendation"]
    ]

    for severity, line, issue, recommendation in issues:

        data.append([
            severity,
            str(line),
            issue,
            recommendation
        ])

    table = Table(data, colWidths=[70, 50, 180, 220])

    table.setStyle(TableStyle([

        ("BACKGROUND", (0,0), (-1,0), colors.darkblue),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),

        ("GRID", (0,0), (-1,-1), 1, colors.black),

        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),

        ("BACKGROUND", (0,1), (-1,-1), colors.beige),

        ("BOTTOMPADDING", (0,0), (-1,0), 10),

        ("ALIGN", (0,0), (-1,-1), "CENTER")

    ]))

    pdf.build([table])


def generate_text_report(issues, filename):

    with open(filename, "w", encoding="utf-8") as file:

        file.write("MULTI-LANGUAGE SECURE CODE REVIEW REPORT\n")
        file.write("=" * 70 + "\n\n")

        if not issues:

            file.write("No security issues found.\n")
            return

        for i, issue in enumerate(issues, start=1):

            severity, line, title, recommendation = issue

            file.write(f"Issue {i}\n")
            file.write(f"Severity      : {severity}\n")
            file.write(f"Line          : {line}\n")
            file.write(f"Issue         : {title}\n")
            file.write(f"Recommendation: {recommendation}\n")
            file.write("-" * 70 + "\n")