from fpdf import FPDF
from datas import *
from utilities import *


# company = input("Entreprise :")
company = "Mc Donald's"
main_skills = input("Main skills (separator ,) :")





pdf = FPDF("P", "mm", "A4")
#! a voir pourquoi ne semble pas changer le pdf final 
# pdf.set_auto_page_break(auto=True)
pdf.set_auto_page_break(auto=True, margin=15)
# pdf.multi_cell(0, 10, corps)
pdf.add_page()

pdf.set_font(FONT_FAMILY, size=12)

pdf.set_xy(10, 10)

text = get_personnal_information_section()

# pdf.multi_cell(0, 10, text)
pdf.multi_cell(0, 10, text)
pdf.ln(LINE_HEIGHT)

pdf.set_font(FONT_FAMILY, "B", 12)
# pdf.cell(0, 10, OBJECT, ln=LINE_HEIGHT)

pdf.set_font(FONT_FAMILY, size=12)

corps = get_text_section()
pdf.multi_cell(0, 10, corps)

pdf.cell(0, 10, "Nicolas Vero")
pdf.output(formate_company_name(company) + ".pdf")


print(formate_company_name(company))
