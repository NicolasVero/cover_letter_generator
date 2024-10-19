import os
from fpdf import FPDF
from utilities import * 
from datas import * 

def generate_pdf(props):

    if not os.path.exists(SAVE_PATH):
        os.makedirs(SAVE_PATH)

    pdf = FPDF("P", "mm", "A4")
    pdf.set_margin(24)
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    pdf.set_font(FONT_FAMILY, size=12)


    text = get_personal_information_section()
    pdf.multi_cell(0, 6, text) 
    pdf.ln(LINE_HEIGHT)

    pdf.set_font(FONT_FAMILY, "B", 12)
    pdf.multi_cell(0, 6, get_object(props.get("spontaneous"), props.get("job"))) 

    pdf.set_font(FONT_FAMILY, size=12)
    pdf.multi_cell(0, 6, get_text_section(props))

    pdf.cell(0, 10, "Nicolas Vero")

    pdf_filename = os.path.join(SAVE_PATH, formate_company_name(props.get("company")) + ".pdf")
    pdf.output(pdf_filename)
