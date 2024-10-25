from datas import *
from utilities import *

def add_body(pdf, props):
    change_font(pdf, "")
    pdf.multi_cell(0, LINE_HEIGHT, get_text_section(props), align='L')