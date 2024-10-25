from datas import *
from utilities import *

def add_body(pdf, props):
    change_font(pdf, "")
    pdf.multi_cell(0, LINE_HEIGHT, get_text_section(props), align='L')


def get_text_section(props):
    return replaces_text_props(
        "Madame, Monsieur, " + DOUBLE_SPACE + 
        "Récemment diplômé en BUT MMI de l'IUT de Rouen, je vous adresse ma candidature [spontaneous] poste de [job] au sein de votre entreprise. " + DOUBLE_SPACE +
        "Mes connaissances en développement, en particulier en [main_skills], ainsi que mon expérience en développement de sites et d'applications web m'ont permis d'acquérir des compétences techniques solides. " +
        "[dut_info]" +
        GITHUB + SPACE +
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