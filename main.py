from fpdf import FPDF
from datas import *
from utilities import *


company = input("Entreprise :")
spontaneous = input("Is spontaneous ? (y, '' / n) : :")
job = input("Job :")
main_skills = input("Main skills (separator ,) :")
display_dut_info = input("Display DUT Info ? (y, '' / n) :")

if display_dut_info in ['', 'y']:
    dut_info_skills = input("DUT Info skills (separator ,) :")


props = {
    "company" : company,
    "spontaneous" : spontaneous,
    "job" : job,
    "main_skills" : main_skills,
    "display_dut_info" : display_dut_info,
    "dut_info_skills" : dut_info_skills if 'dut_info_skills' in globals() else None
}




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

corps = get_text_section(props)
pdf.multi_cell(0, 10, corps)

pdf.cell(0, 10, "Nicolas Vero")
pdf.output(formate_company_name(company) + ".pdf")


print(formate_company_name(company))
