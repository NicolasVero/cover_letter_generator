import os
from fpdf import FPDF
from datas import *
from utilities import *
from generator import *


company = input("Entreprise :")
spontaneous = input("Is spontaneous ? (y, '' / n) : :")
job = input("Job :")
main_skills = input("Main skills (separator ,) :")
display_dut_info = input("Display DUT Info ? (y, '' / n) :")

if display_dut_info in ['', 'y']:
    dut_info_skills = input("DUT Info skills (separator ,) :")


generate_pdf({
    "company" : company,
    "spontaneous" : spontaneous,
    "job" : job,
    "main_skills" : main_skills,
    "display_dut_info" : display_dut_info,
    "dut_info_skills" : dut_info_skills if 'dut_info_skills' in globals() else None
})