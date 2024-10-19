from generator import *

company          = input("Enterprise :")
spontaneous      = input("Is spontaneous ? (y, '' / n) : :")
job              = input("Job :")
main_skills      = input("Main skills (separator ,) :")
display_dut_info = input("Display DUT Info ? (y, '' / n) :")
dut_info_skills  = input("DUT Info skills (separator ,) :") if display_dut_info in ['', 'y'] else None


#! test
# company = 'test'
# spontaneous = 'test'
# job = 'test'
# main_skills = 'test'
# display_dut_info = False
# dut_info_skills = None

generate_pdf({
    "company" : company,
    "spontaneous" : spontaneous,
    "job" : job,
    "main_skills" : main_skills,
    "display_dut_info" : display_dut_info,
    "dut_info_skills" : dut_info_skills
})