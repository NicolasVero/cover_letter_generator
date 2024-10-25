import os 
from fpdf import FPDF
from components.header import *
from components.body import *
from components.footer import *
from utilities import * 
from datas import *


def generate_pdf(props):

    pdf = initialize_pdf()
    add_header(pdf, props)
    add_body(pdf, props)
    add_footer(pdf, props)

    save_pdf(pdf, props.get("company"))


def initialize_pdf():
    pdf = FPDF("P", "mm", "A4")

    pdf.add_font(FONT_FAMILY, '' , './fonts/' + FONT_FAMILY + '/Regular.ttf', uni=True)
    pdf.add_font(FONT_FAMILY, 'B', './fonts/' + FONT_FAMILY + '/Bold.ttf'   , uni=True)
    pdf.add_font(FONT_FAMILY, 'I', './fonts/' + FONT_FAMILY + '/Italic.ttf' , uni=True)
    
    pdf.set_margin(MARGIN)
    pdf.add_page()
    
    pdf.set_fill_color(PDF_COLOR[0], PDF_COLOR[1], PDF_COLOR[2])
    pdf.rect(0, 0, 210, 297, 'F')
    return pdf


def save_pdf(pdf, pdf_name):
    if not os.path.exists(SAVE_PATH):
        os.makedirs(SAVE_PATH)

    pdf_filename = os.path.join(SAVE_PATH, formate_company_name(pdf_name) + ".pdf")
    pdf.output(pdf_filename)




