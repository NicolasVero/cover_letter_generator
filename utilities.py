import re
from datas import *

def get_personnal_information_section():
    section  = f"{LASTNAME} {FIRSTNAME}\n"
    section += f"{ADRESS}\n"
    section += f"{PHONE}\n"
    section += f"{EMAIL}\n"
    return section 



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
    print(props)

    text = text.replace("[company]", props.get("company"))
    text = text.replace("[spontaneous]", IS_SPONTANEOUS if props.get("spontaneous") in ['', 'y'] else NOT_SPONTANEOUS)
    text = text.replace("[job]", props.get("job"))
    text = text.replace("[main_skills]", get_list_into_string(props.get("main_skills")))
    text = text.replace("[dut_info]", DUT_INFO if props.get("display_dut_info") in ['', 'y'] else SPACE)
    text = text.replace("[dut_info_skills]", get_list_into_string(props.get("dut_info_skills")))
    return text


def get_list_into_string(list):

    if list == None: return ""
    
    string = ""
    elements = list.split(",")

    for element in elements:
        print(element)
        string += element + ", "
    
    return string[:string.rfind(",")]



def formate_company_name(company):
    company = re.sub(r"[^a-zA-Z0-9\s]", "", company)
    company = company.lower().replace(" ", "_")
    return company

