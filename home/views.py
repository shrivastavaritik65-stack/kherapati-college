from django.shortcuts import render

# Create your views here.
from django.http import FileResponse
from django.shortcuts import render
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    ListFlowable,
    ListItem
)
from reportlab.lib.units import mm
import io


def home(request):
    return render(request, "home/index.html")


def admission_documents(request):
    return render(request, "home/admission_documents.html")


def download_ug_pg_pdf(request):
    buffer = io.BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=18 * mm,
        leftMargin=18 * mm,
        topMargin=18 * mm,
        bottomMargin=18 * mm,
    )

    styles = getSampleStyleSheet()

    title = ParagraphStyle(
        "CollegeTitle",
        parent=styles["Title"],
        fontSize=18,
        leading=22,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#123c69"),
        spaceAfter=8,
    )

    subtitle = ParagraphStyle(
        "Subtitle",
        parent=styles["Normal"],
        fontSize=10,
        leading=14,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#667085"),
        spaceAfter=20,
    )

    heading = ParagraphStyle(
        "Heading",
        parent=styles["Heading2"],
        fontSize=14,
        leading=18,
        textColor=colors.HexColor("#1769aa"),
        spaceAfter=10,
    )

    body = ParagraphStyle(
        "Body",
        parent=styles["BodyText"],
        fontSize=10.5,
        leading=16,
        textColor=colors.HexColor("#344054"),
    )

    story = []

    story.append(
        Paragraph(
            "KHEDAPATI SARKAR GROUP OF COLLEGES",
            title
        )
    )

    story.append(
        Paragraph(
            "Indergarh, District Datia, Madhya Pradesh - 475675",
            subtitle
        )
    )

    story.append(
        Paragraph(
            "New Admission Documents - UG / PG",
            heading
        )
    )

    documents = [
        "10th Standard Mark Sheet",
        "12th Standard Mark Sheet",
        "Graduation Mark Sheet (for Postgraduate admission)",
        "Caste Certificate",
        "Domicile / Residence Certificate",
        "Income Certificate",
        "Samagra ID",
        "Photocopy of Aadhaar Card",
        "One Passport-size Photograph",
        "ABC ID (Academic Bank of Credits ID)",
    ]

    items = [
        ListItem(Paragraph(item, body))
        for item in documents
    ]

    story.append(
        ListFlowable(
            items,
            bulletType="1",
            start="1",
            leftIndent=20
        )
    )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            "Please verify the latest admission requirements with the college office.",
            body
        )
    )

    doc.build(story)

    buffer.seek(0)

    return FileResponse(
        buffer,
        as_attachment=True,
        filename="Khedapati_UG_PG_Admission_Documents.pdf"
    )


def download_village_girl_pdf(request):
    buffer = io.BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=18 * mm,
        leftMargin=18 * mm,
        topMargin=18 * mm,
        bottomMargin=18 * mm,
    )

    styles = getSampleStyleSheet()

    title = ParagraphStyle(
        "CollegeTitle",
        parent=styles["Title"],
        fontSize=18,
        leading=22,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#123c69"),
        spaceAfter=8,
    )

    subtitle = ParagraphStyle(
        "Subtitle",
        parent=styles["Normal"],
        fontSize=10,
        leading=14,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#667085"),
        spaceAfter=20,
    )

    heading = ParagraphStyle(
        "Heading",
        parent=styles["Heading2"],
        fontSize=14,
        leading=18,
        textColor=colors.HexColor("#1769aa"),
        spaceAfter=10,
    )

    body = ParagraphStyle(
        "Body",
        parent=styles["BodyText"],
        fontSize=10.5,
        leading=16,
        textColor=colors.HexColor("#344054"),
    )

    story = []

    story.append(
        Paragraph(
            "KHEDAPATI SARKAR GROUP OF COLLEGES",
            title
        )
    )

    story.append(
        Paragraph(
            "Indergarh, District Datia, Madhya Pradesh - 475675",
            subtitle
        )
    )

    story.append(
        Paragraph(
            "Documents for Village Girl Scheme",
            heading
        )
    )

    documents = [
        "Five-page form for first-year Village Girl applicants",
        "Completed online application form",
        "Photocopy of 10th Standard Mark Sheet",
        "Photocopy of 12th Standard Mark Sheet",
        "Online Fee Receipt",
        "Income Certificate",
        "Caste Certificate",
        "Domicile / Residence Certificate",
        "Family ID",
        "Aadhaar Card",
        "Bank Passbook",
        "Transfer Certificate (TC), as applicable",
    ]

    items = [
        ListItem(Paragraph(item, body))
        for item in documents
    ]

    story.append(
        ListFlowable(
            items,
            bulletType="1",
            start="1",
            leftIndent=20
        )
    )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            "Please verify the latest admission requirements with the college office.",
            body
        )
    )

    doc.build(story)

    buffer.seek(0)

    return FileResponse(
        buffer,
        as_attachment=True,
        filename="Khedapati_Village_Girl_Documents.pdf"
    )