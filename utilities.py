import re
from datas import *


def get_personal_information_section():
    return SPACE.join([FULLNAME, ADRESS, PHONE, EMAIL]) + SPACE

def get_subject(spontaneous, job):
    subject = SPONTANEOUS_SUBJECT if spontaneous in ['', 'y'] else NOT_SPONTANEOUS_SUBJECT
    job = job[0].lower() + job[1:]
    return subject.replace("[job]", job) + SPACE

def get_text_section(props):
    return replaces_text_props(
        "Madame, Monsieur, " + DOUBLE_SPACE + 
        "Récemment diplômé en BUT MMI de l'IUT de Rouen, je vous adresse ma candidature [spontaneous] poste de [job] au sein de votre entreprise. " + DOUBLE_SPACE +
        "Mes connaissances en développement, en particulier en [main_skills], ainsi que mon expérience en développement de sites et d'applications web m'ont permis d'acquérir des compétences techniques solides. " +
        "[dut_info]" +
        GITHUB + DOUBLE_SPACE +
        GREETINGS + DOUBLE_SPACE
    , props)


def replaces_text_props(text, props):
    
    replacements = {
        "[company]"        : props.get("company", ""),
        "[job]"            : props.get("job", ""),
        "[spontaneous]"    : IS_SPONTANEOUS if props.get("spontaneous") in ['', 'y'] else NOT_SPONTANEOUS,
        "[dut_info]"       : DUT_INFO if props.get("display_dut_info") in ['', 'y'] else DOUBLE_SPACE,
        "[main_skills]"    : get_list_into_string(props.get("main_skills", [])),
        "[dut_info_skills]": get_list_into_string(props.get("dut_info_skills", [])),
    }

    for key, value in replacements.items():
        text = text.replace(key, value)
    
    return text


def get_list_into_string(list):

    if list == None: return ""
    
    string = ""
    elements = list.split(",")

    for element in elements:
        string += element + ", "
    
    return string[:string.rfind(",")]


def formate_company_name(company):
    company = re.sub(r"[^a-zA-Z0-9\s]", "", company)
    company = company.lower().replace(" ", "_")
    return company