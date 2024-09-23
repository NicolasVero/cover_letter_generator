from fpdf import FPDF

print("Hello world")

pdf = FPDF()
pdf.add_page()
pdf.output("Tutorial.pdf")