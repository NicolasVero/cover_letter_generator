import re
from datas import *

def get_personnal_information_section():
    section = f"{LASTNAME} {FIRSTNAME}\n"
    section += f"{ADRESS}\n"
    section += f"{PHONE}\n"
    section += f"{EMAIL}\n"
    return section 



def get_text_section():
    return (
        "Madame, Monsieur, " +
        "Récemment diplômé en BUT MMI de l'IUT de Rouen, je vous adresse ma candidature [spontaneous] poste de [job] au sein de votre entreprise." + 
        "Je suis particulièrement intéressé par les opportunités de développement au sein de votre entreprise, et je suis convaincu que mes compétences en [main_skills] pourraient être un atout pour votre équipe." + 
        DUT_INFO +
        GITHUB +
        GREETINGS
    )


def formate_company_name(company):
    company = re.sub(r"[^a-zA-Z0-9\s]", "", company)
    company = company.lower().replace(" ", "_")
    return company

