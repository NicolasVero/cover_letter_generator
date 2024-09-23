from fpdf import FPDF

line_height = 19
section_margin_block = 16
font_family = "Helvetica"


pdf = FPDF("P", "mm", "A4")
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

pdf.set_font(font_family, size=12)

pdf.set_xy(10, 10)
pdf.multi_cell(0, 10, "Web et Solutions\nNicolas Vero\n52 rue Lemoine, Sotteville-lès-Rouen\n06 51 15 16 80\nnicolasvero03@gmail.com")
pdf.ln(line_height)

pdf.set_font(font_family, "B", 12)
pdf.cell(0, 10, "Objet : demande de stage pour une durée de 10 semaines", ln=line_height)

pdf.set_font(font_family, size=12)
# corps = """
# Madame, Monsieur,

# Actuellement en 2ème année de BUT MMI à l’IUT de Rouen, je vous sollicite dans le cadre de ma recherche de stage dans le domaine du développement web, pour une durée de 10 semaines (du 3 avril 2023 au 10 juin 2023).

# Mes connaissances en développement, en particulier en HTML, CSS, et dans les langages de programmation JavaScript et PHP, ainsi que mon expérience en développement de sites et d’applications web m’ont permis d’acquérir des compétences techniques solides. J’ai également une très bonne connaissance de l'algorithmique, grâce à ma première année en DUT Informatique, où j’ai pu passer beaucoup de temps sur les langages Java et C.

# Mon parcours en BUT MMI m’a permis aussi d’acquérir une bonne maîtrise des logiciels de la suite Adobe (Illustrator, Photoshop, Premiere), ainsi que des techniques de communication.

# J’ai également une bonne connaissance du monde professionnel, du fait de mes expériences passées, et notamment grâce à mon poste d’équipier chez McDonald’s que j’occupe depuis septembre 2022.
# Je suis convaincu que je pourrais être un atout pour votre entreprise, et je suis impatient de mettre mes compétences à votre service.

# En espérant que ma candidature puisse vous intéresser, je vous prie d’agréer mes salutations les plus distinguées.
# """

# pdf.multi_cell(0, 10, corps)

# pdf.ln(line_height)
# pdf.ln(section_margin_block)

pdf.cell(0, 10, "Nicolas Vero")
pdf.output("Demande_de_Stage.pdf")
