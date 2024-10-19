import os
from fpdf import FPDF
from utilities import * 
from datas import * 

def generate_pdf(props):

    if not os.path.exists(SAVE_PATH):
        os.makedirs(SAVE_PATH)

    pdf = FPDF("P", "mm", "A4")
    # pdf.set_margin(4)
    #! a voir pourquoi ne semble pas changer le pdf final 
    # pdf.set_auto_page_break(auto=True)
    pdf.set_auto_page_break(auto=True, margin=15)
    # pdf.multi_cell(0, 10, corps)
    pdf.add_page()

    pdf.set_font(FONT_FAMILY, size=12)

    pdf.set_xy(10, 10)

    text = get_personal_information_section()

    # pdf.multi_cell(0, 10, text)
    pdf.multi_cell(0, 10, text)
    pdf.ln(LINE_HEIGHT)

    pdf.set_font(FONT_FAMILY, "B", 12)
    # pdf.cell(0, 10, OBJECT, ln=LINE_HEIGHT)

    pdf.multi_cell(0, 10, get_object(props.get("spontaneous"), props.get("job")))

    pdf.set_font(FONT_FAMILY, size=12)

    corps = get_text_section(props)
    pdf.multi_cell(0, 10, corps)

    pdf.cell(0, 10, "Nicolas Vero")

    pdf_filename = os.path.join(SAVE_PATH, formate_company_name(props.get("company")) + ".pdf")
    pdf.output(pdf_filename)
