from datas import *
from utilities import *

def add_header(pdf, props):
    pdf.image("./medias/images/profile.png", x=MARGIN + 2, y=MARGIN + 2, w=36, h=36)
    pdf.ellipse(MARGIN, MARGIN, 40, 40)

    add_name_section(pdf, props)
    add_contact_section(pdf)        
    add_subject(pdf, props)

    pdf.ln(20)



def add_contact_section(pdf):
    change_font(pdf, "")
    add_icon_text(pdf, "./medias/icons/phone.png" , MARGIN + 50 , MARGIN + 42, PHONE , w=3  , h=3  )
    add_icon_text(pdf, "./medias/icons/email.png" , MARGIN + 100, MARGIN + 42, EMAIL , w=3.5, h=3  )
    add_icon_text(pdf, "./medias/icons/adress.png", MARGIN + 50 , MARGIN + 48, ADRESS, w=3  , h=3.5)


def add_icon_text(pdf, icon_path, x, y, text, w, h):

    pdf.image(icon_path, x=x, y=y, w=w, h=h)

    if("email" in icon_path): y -= 0.4

    pdf.set_xy(x + 4, y - 1)
    pdf.cell(0, LINE_HEIGHT, text)


def add_name_section(pdf, props):
    change_font(pdf, "B", font_size=30)
    pdf.set_xy(MARGIN + 50, MARGIN + 5)
    pdf.cell(0, LINE_HEIGHT, FIRSTNAME.upper())
    pdf.set_xy(MARGIN + 50, MARGIN + 16)
    pdf.cell(0, LINE_HEIGHT, LASTNAME.upper())
    pdf.set_xy(MARGIN + 50, MARGIN + 30)

    change_font(pdf, "B", font_size=15)
    pdf.cell(0, LINE_HEIGHT, props.get("job"))
    pdf.ln(50)
    pdf.rect(MARGIN + 50, MARGIN + 38, 110, 0.6, "F")


def add_subject(pdf, props):
    pdf.set_xy(MARGIN, MARGIN + 60)
    change_font(pdf, "B")
    pdf.cell(0, LINE_HEIGHT, get_subject(props.get("spontaneous"), props.get("job")))

    pdf.set_xy(MARGIN, MARGIN + 66)
    change_font(pdf, "")
    pdf.cell(0, LINE_HEIGHT, props.get("company"))

    pdf.set_fill_color(89, 88, 96)
    pdf.rect(MARGIN + 1, MARGIN + 77, 160, 0.1, "F")