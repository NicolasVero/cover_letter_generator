from datas import *
from utilities import *

def add_footer(pdf, props):
    signature_y = pdf.get_y()

    pdf.image("./medias/images/signature.png", x=MARGIN, y=signature_y - 10, h=30)

    change_font(pdf, "I")
    pdf.set_xy(MARGIN, signature_y + 20)
    pdf.cell(0, 0, FULLNAME)