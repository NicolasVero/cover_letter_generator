import re
from datas import *


def get_personnal_information_section():
    return SPACE.join([LASTNAME + " " + FIRSTNAME, ADRESS, PHONE, EMAIL]) + SPACE


def get_text_section(props):
    return replaces_text_props(
        "Madame, Monsieur, " + SPACE + 
        "Récemment diplômé en BUT MMI de l'IUT de Rouen, je vous adresse ma candidature [spontaneous] poste de [job] au sein de votre entreprise. " + SPACE +
        "Mes connaissances en développement, en particulier en [main_skills], ainsi que mon expérience en développement de sites et d'applications web m'ont permis d'acquérir des compétences techniques solides. " +
        "[dut_info]" +
        GITHUB + SPACE +
        GREETINGS + SPACE
    , props)


def replaces_text_props(text, props):
    
    replacements = {
        "[company]"        : props.get("company", ""),
        "[job]"            : props.get("job", ""),
        "[spontaneous]"    : IS_SPONTANEOUS if props.get("spontaneous") in ['', 'y'] else NOT_SPONTANEOUS,
        "[dut_info]"       : DUT_INFO if props.get("display_dut_info") in ['', 'y'] else SPACE,
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