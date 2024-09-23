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
        
        "Je suis particulièrement intéressé par les opportunités de développement au sein de votre entreprise, et je suis convaincu    que mes compétences en ... pourraient être un atout pour votre équipe."
        + GREETINGS
    )


def formate_company_name(company):
    company = re.sub(r"[^a-zA-Z0-9\s]", "", company)
    company = company.lower().replace(" ", "_")
    return company

