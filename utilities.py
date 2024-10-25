import re
from datas import *


def get_subject(spontaneous, job):
    subject = SPONTANEOUS_SUBJECT if spontaneous in ['', 'y'] else NOT_SPONTANEOUS_SUBJECT
    job = job[0].lower() + job[1:]
    return subject.replace("[job]", job)


def get_list_into_string(list):

    if(list == None): return ""

    elements = [element.strip() for element in list.split(",") if element.strip()]

    if len(elements) == 1:
        return elements[0]
    elif len(elements) == 2:
        return " et ".join(elements)

    string = ", ".join(elements[:-1]) + " et " + elements[-1]
    return string


def formate_company_name(company):
    company = re.sub(r"[^a-zA-Z0-9\s]", "", company)
    company = company.lower().replace(" ", "_")
    return company


def change_font(pdf, decoration = "", font_family = FONT_FAMILY, font_size = FONT_SIZE):
    pdf.set_font(font_family, decoration, font_size)


# def add_space(pdf, double=True):
#     pdf.ln(3)