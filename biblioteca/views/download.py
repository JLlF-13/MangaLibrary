from django.shortcuts import render, redirect
from django.contrib import messages
from biblioteca.models import Manga, Status, Origin, Language, Type
from django.shortcuts import render, redirect, get_object_or_404
# Especific descarrega
from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Image
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from django.http import HttpResponse
import os
from PIL import Image as PILImage  # Llibreria per comprimir imatges
from datetime import datetime
import io  # Per gestionar imatges en memòria

def compress_image(image_path, max_width=100):
    """Funció per comprimir una imatge a una amplada màxima i reduir qualitat."""
    if os.path.exists(image_path):
        with PILImage.open(image_path) as img:
            # Convertir la imatge a RGB si està en un altre mode (com RGBA)
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Reduir la mida mantenint la proporció
            aspect_ratio = img.height / img.width
            new_width = max_width
            new_height = int(new_width * aspect_ratio)
            img = img.resize((new_width, new_height), PILImage.Resampling.LANCZOS)

            # Guardar la imatge comprimida en memòria
            img_byte_arr = io.BytesIO()
            img.save(img_byte_arr, format='JPEG', quality=50)  # Qualitat al 50% per a més compressió
            img_byte_arr.seek(0)
            return img_byte_arr
    return None

def download_manga_pdf(request):
    # Obtenir el nom de l'usuari de la sessió actual
    user_name = os.getlogin()

    # Definir el nom del fitxer PDF amb el nom de l'usuari
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="mangas_{user_name}.pdf"'

    doc = SimpleDocTemplate(response, pagesize=landscape(letter), leftMargin=20, rightMargin=20)
    elements = []
    styles = getSampleStyleSheet()

    # Títol
    now = datetime.now()
    title = Paragraph(f"<b>MangaLibrary</b><br/>Generat el: {now.strftime('%d-%m-%Y %H:%M:%S')}", styles['Title'])
    elements.append(title)
    elements.append(Paragraph("<br/><br/>", styles['Normal']))

    # Dades de capçalera
    data = [["Image", "Name", "Observations", "Owned", "Total Books", "Avg Price", "Total Spend", "Language", "Type", "Origin", "Status"]]

    mangas = Manga.objects.all().order_by('name')
    for manga in mangas:
        # Comprimir i carregar la imatge
        compressed_img = compress_image(manga.photo.path) if manga.photo else None
        if compressed_img:
            img = Image(compressed_img, width=50, height=70)  # Augmentada la mida de la imatge
        else:
            img = Paragraph("No Image", styles['Normal'])

        # Estils per a `Name` i `Observations`
        centered_text_style = ParagraphStyle('centered_text', parent=styles['Normal'], alignment=1, fontSize=8, wordWrap='CJK')

        # Afegir fila a la taula
        total_books_display = '?' if manga.total_books == 0 else manga.total_books
        data.append([
            img,
            Paragraph(manga.name or 'N/A', centered_text_style),
            Paragraph(manga.observations or 'N/A', centered_text_style),
            manga.owned,
            total_books_display,
            manga.avg_price,
            manga.total_spend,
            manga.language_id.name if manga.language_id else 'N/A',
            manga.type_id.name if manga.type_id else 'N/A',
            manga.origin_id.name if manga.origin_id else 'N/A',
            manga.status_id.name if manga.status_id else 'N/A'
        ])

    # Taula amb columnes més àmplies
    table = Table(data, colWidths=[60, 100, 150, 40, 50, 60, 60, 60, 60, 60, 60])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('LEFTPADDING', (0, 0), (-1, -1), 2),
        ('RIGHTPADDING', (0, 0), (-1, -1), 2),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ]))
    elements.append(table)

    # Construir el PDF
    doc.build(elements)
    return response