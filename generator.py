import os
from fpdf import FPDF
from utilities import * 
from datas import * 

def generate_pdf(props):

    pdf = initialize_pdf()


    pdf.image("./images/profile.png", x=MARGIN + 2, y=MARGIN + 2, w=36, h=36)
    pdf.ellipse(MARGIN, MARGIN, 40, 40)


    change_font(pdf, "B", font_size=30)

    pdf.set_xy(MARGIN + 50, MARGIN + 5)
    pdf.cell(0, LINE_HEIGHT, FIRSTNAME.upper())
    pdf.set_xy(MARGIN + 50, MARGIN + 16)
    pdf.cell(0, LINE_HEIGHT, LASTNAME.upper())
    pdf.set_xy(MARGIN + 50, MARGIN + 30)

    change_font(pdf, "B", font_size=15)
    pdf.cell(0, LINE_HEIGHT, props.get("job"))
    pdf.ln(50)
    pdf.rect(MARGIN + 50, MARGIN + 38, 100, 1, "F")


    change_font(pdf, "")
    pdf.multi_cell(0, LINE_HEIGHT, get_personal_information_section())

    change_font(pdf, "I")
    pdf.multi_cell(0, LINE_HEIGHT, props.get("company"), align='R')
    pdf.ln(3)

    change_font(pdf, "B")
    pdf.multi_cell(0, LINE_HEIGHT, get_subject(props.get("spontaneous"), props.get("job"))) 

    change_font(pdf, "")
    pdf.multi_cell(0, LINE_HEIGHT, get_text_section(props), align='L')

    change_font(pdf, "I")
    pdf.cell(0, 0, FULLNAME)

    save_pdf(pdf, props.get("company"))


def initialize_pdf():
    pdf = FPDF("P", "mm", "A4")

    pdf.add_font(FONT_FAMILY, '' , './fonts/' + FONT_FAMILY + '/Regular.ttf', uni=True)
    pdf.add_font(FONT_FAMILY, 'B', './fonts/' + FONT_FAMILY + '/Bold.ttf'   , uni=True)
    pdf.add_font(FONT_FAMILY, 'I', './fonts/' + FONT_FAMILY + '/Italic.ttf' , uni=True)
    
    pdf.set_margin(MARGIN)
    pdf.add_page()
    
    # pdf.set_fill_color(254, 251, 234)
    # pdf.rect(0, 0, 210, 297, 'F')
    return pdf


def save_pdf(pdf, pdf_name):
    if not os.path.exists(SAVE_PATH):
        os.makedirs(SAVE_PATH)

    pdf_filename = os.path.join(SAVE_PATH, formate_company_name(pdf_name) + ".pdf")
    pdf.output(pdf_filename)


def change_font(pdf, decoration = "", font_family = FONT_FAMILY, font_size = FONT_SIZE):
    pdf.set_font(font_family, decoration, font_size)