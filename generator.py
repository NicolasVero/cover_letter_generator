import os
from fpdf import FPDF
from utilities import * 
from datas import * 

def generate_pdf(props):

    if not os.path.exists(SAVE_PATH):
        os.makedirs(SAVE_PATH)

    pdf = FPDF("P", "mm", "A4")

    pdf.add_font(FONT_FAMILY, '', './fonts/' + FONT_FAMILY + '/Regular.ttf', uni=True)
    pdf.add_font(FONT_FAMILY, 'B', './fonts/' + FONT_FAMILY + '/Bold.ttf', uni=True)
    pdf.add_font(FONT_FAMILY, 'I', './fonts/' + FONT_FAMILY + '/Italic.ttf', uni=True)

    pdf.set_margin(24)
    pdf.add_page()

    pdf.set_font(FONT_FAMILY, size=FONT_SIZE)


    pdf.multi_cell(0, 6, get_personal_information_section()) 
    pdf.set_font(FONT_FAMILY, "I", FONT_SIZE)
    pdf.multi_cell(0, 6, props.get("company"), align='R')  # Aligner à droite

    # changer nom
    pdf.ln(LINE_HEIGHT)

    pdf.set_font(FONT_FAMILY, "B", FONT_SIZE)
    pdf.multi_cell(0, 6, get_object(props.get("spontaneous"), props.get("job"))) 

    pdf.set_font(FONT_FAMILY, size=FONT_SIZE)
    pdf.multi_cell(0, 6, get_text_section(props))

    pdf.cell(0, 10, FIRSTNAME + LASTNAME)

    pdf_filename = os.path.join(SAVE_PATH, formate_company_name(props.get("company")) + ".pdf")
    pdf.output(pdf_filename)
