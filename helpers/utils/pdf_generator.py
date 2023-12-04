import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from datetime import datetime
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet


def generate_medical_history_pdf(medical_histories):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    p.setTitle(
        f"Historia médica de {medical_histories[0].animal.name} - {format_date(datetime.now())}")
    height_page, width_page = letter
    x_border_start = height_page - 1 * inch
    y_border_top = width_page - 1 * inch

    styles = getSampleStyleSheet()
    bold_style = styles['BodyText']
    bold_style.fontName = 'Helvetica-Bold'

    def draw_skeleton(page_number=1):
        bold_font()
        p.drawString(inch-15, y_border_top, "Nombre:")
        p.drawString(inch-15, y_border_top - 20, "Granjero:")
        p.drawString(inch-15, y_border_top - 40, "Especie:")
        p.drawString(inch+250, y_border_top - 40, "Raza:")
        p.drawString(inch-15, y_border_top - 60, "Fecha de nacimiento:")
        p.drawString(inch-15, y_border_top - 80, "Peso:")
        p.drawString(inch+250, y_border_top - 80, "Altura:")
        normal_font()
        p.drawString(inch+45, y_border_top,
                     f"{medical_histories[0].animal.name}")
        p.drawString(inch+50, y_border_top - 20,
                     f"{medical_histories[0].animal.farmer.first_name} {medical_histories[0].animal.farmer.last_name}")
        p.drawString(inch+45, y_border_top - 40,
                     f"{medical_histories[0].animal.specie}")
        p.drawString(inch+280, y_border_top - 40,
                     f"{medical_histories[0].animal.race}")
        p.drawString(inch+110, y_border_top - 60,
                     f"{medical_histories[0].animal.birth_date}")
        p.drawString(inch+30, y_border_top - 80,
                     f"{medical_histories[0].animal.weight} kg")
        p.drawString(inch+285, y_border_top - 80,
                     f"{medical_histories[0].animal.height} cm")
        p.rect(inch-17, y_border_top-90, x_border_start-inch, 110, fill=0)
        bold_font()
        # Pie de página
        p.drawString(inch+210, 20, f"Página {page_number}")
        p.drawString(inch+200, 5, f"{format_date(datetime.now())}")
        p.drawString(inch, 5, "VetApp")
        normal_font()

    def bold_font():
        p.setFont(bold_style.fontName, bold_style.fontSize)

    def normal_font():
        p.setFont("Helvetica", 10)

    def draw_text_in_lines(initial_x, initial_y, text, character_limit):
        lines = [text[i:i + character_limit]
                 for i in range(0, len(text), character_limit)]
        for i, line in enumerate(lines):
            p.drawString(initial_x, initial_y - i * 20, line)
    draw_skeleton(p.getPageNumber())

    initial_x = inch
    initial_y = y_border_top - 120
    iterator = 0
    for medical_history in medical_histories:
        bold_font()
        p.drawString(initial_x - 15, initial_y, "Veterinario:")
        p.drawString(initial_x + 250, initial_y, "Fecha:")
        p.rect(initial_x-17, initial_y-5, x_border_start-inch, 20, fill=0)
        p.drawString(initial_x + 60, initial_y-30, "Diágnostico")
        p.drawString(initial_x + 315, initial_y-30, "Tratamiento")
        normal_font()
        p.drawString(initial_x+45, initial_y,
                     f"{medical_history.veterinarian.first_name} {medical_history.veterinarian.last_name}")
        p.drawString(initial_x + 285, initial_y,
                     f"{format_date(medical_history.create_date)}")
        draw_text_in_lines(initial_x-15, initial_y - 50,
                           f"{medical_history.diagnosis}", 45)
        p.rect(initial_x-17, initial_y-500, 220, 480, fill=0)
        draw_text_in_lines(initial_x+235, initial_y - 50,
                           f"{medical_history.treatment}", 45)
        p.rect(initial_x+232, initial_y-500, 220, 480, fill=0)
        iterator += 1
        if iterator == len(medical_histories):
            break
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
