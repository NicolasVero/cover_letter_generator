import re
from datas import *

def get_personnal_information_section():
    section = f"{LASTNAME} {FIRSTNAME}\n"
    section += f"{ADRESS}\n"
    section += f"{PHONE}\n"
    section += f"{EMAIL}\n"
    return section 



def get_text_section(props):
    return replaces_text_props(
        "Madame, Monsieur, " +
        "Récemment diplômé en BUT MMI de l'IUT de Rouen, je vous adresse ma candidature [spontaneous] poste de [job] au sein de votre entreprise." + 
        # "Je suis particulièrement intéressé par les opportunités de développement au sein de votre entreprise, et je suis convaincu que mes compétences en [main_skills] pourraient être un atout pour votre équipe." + 
        "Mes connaissances en développement, en particulier en [main_skills], ainsi que mon expérience en développement de sites et d'applications web m'ont permis d'acquérir des compétences techniques solides." +
        DUT_INFO +
        GITHUB +
        GREETINGS
    , props)


def replaces_text_props(text, props):
    print(props)

    text = text.replace("[company]", props.get("company"))
    text = text.replace("[spontaneous]", IS_SPONTANEOUS if props.get("spontaneous") in ['', 'y'] else NOT_SPONTANEOUS)
    text = text.replace("[job]", props.get("job"))
    text = text.replace("[main_skills]", get_list_into_string(props.get("main_skills")))
    return text


def get_list_into_string(list):
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

