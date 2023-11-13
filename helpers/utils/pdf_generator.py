import io
from django.http import FileResponse, HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from medical_history.models import MedicalHistory
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors


def generate_medical_history_pdf(medical_histories):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    p.setTitle = f"Historia médica de {medical_histories[0].animal.name} - {format_date(datetime.now())} "
    height_page, width_page = letter
    x_border_start = height_page - 1 * inch
    y_border_top = width_page - 1 * inch

    def draw_skeleton(page_number=1):
        p.drawString(inch, y_border_top,
                     f"Nombre: {medical_histories[0].animal.name}")
        p.drawString(inch, y_border_top - 20,
                     f"Granjero: {medical_histories[0].animal.farmer.first_name} {medical_histories[0].animal.farmer.last_name}")
        p.drawString(inch, y_border_top - 40,
                     f"Especie: {medical_histories[0].animal.specie}")
        p.drawString(inch+250, y_border_top - 40,
                     f"Raza : {medical_histories[0].animal.race}")
        p.drawString(inch, y_border_top - 60,
                     f"Fecha de nacimiento: {medical_histories[0].animal.birth_date}")
        p.drawString(inch, y_border_top - 80,
                     f"Peso: {medical_histories[0].animal.weight} kg")
        p.drawString(inch+250, y_border_top - 80,
                     f"Altura: {medical_histories[0].animal.height} cm")
        p.rect(inch, y_border_top-90, x_border_start-inch, 110, fill=0)
        # Pie de página
        p.drawString(inch, 15, f"Página {page_number}")
        p.drawString(inch, 2, f"{format_date(datetime.now())}")

    
    def draw_text_in_lines(initial_x, initial_y,text, character_limit):
        lines = [text[i:i + character_limit] for i in range(0, len(text), character_limit)]
        for i, line in enumerate(lines):
            p.drawString(initial_x, initial_y - i * 20, line)
    draw_skeleton(p.getPageNumber())
    

    initial_x = inch
    initial_y = y_border_top - 120
    for medical_history in medical_histories:
        p.drawString(initial_x, initial_y,
                     f"Veterinario: {medical_history.veterinarian.first_name} {medical_history.veterinarian.last_name}")
        p.drawString(initial_x + 325, initial_y,
                     f"Fecha: {format_date(medical_history.create_date)}")
        draw_text_in_lines(initial_x-15, initial_y - 20,
                     f"Diágnostico: {medical_history.diagnosis}",45)
        draw_text_in_lines(initial_x+250,initial_y - 20,
                     f"Tratamiento: {medical_history.treatment}",45)
        initial_y = initial_y - 160
        p.showPage()
        page_number = p.getPageNumber()
        draw_skeleton(page_number)
        initial_y = y_border_top - 120
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=f"{medical_histories[0].animal.name}-{format_date_file(datetime.now())}.pdf")


def format_date(date):
    return date.strftime("%Y-%m-%d %H:%M")


def format_date_file(date):
    return date.strftime("%Y-%m-%d_%H_%M")
