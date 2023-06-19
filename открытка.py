from fpdf import FPDF
from datetime import datetime
pdf=FPDF("p","mm","A4")
pdf.add_page()
way=input("Выедите путь до картинки:")
pdf.image(way,x=0,y=0,h=297,w=210)
pdf.add_font("cour", "",  "C:\Windows\Fonts\BOOKOS.ttf",uni=True)
pdf.set_font("cour",size=37)
pdf.set_text_color(0,0,0)
name=input("Имя виновника торжества:")
pdf.cell(0,30,ln=1)#пустой отступ
pdf.cell(0,20, txt="Дорогая," + name +"!",align="C",ln=1)#отступ идет ячейкой за ячейкой
pdf.set_font("cour",size=25)
pdf.set_text_color(0,0,0)
msg="Все комплименты мира Сегодня для тебя. С Днем мамы поздравляю, Любимая моя! Живи как можно дольше, И радуйся всегда. Любви тебе, здоровья На долгие года!"
pdf.set_right_margin(50)
pdf.set_left_margin(50)
pdf.multi_cell(0,10,txt=msg,align="C")
today=datetime.today().strftime("%d.%m.%Y")
pdf.set_text_color(124,89,127)
pdf.cell(0,15,txt=today,align="R",ln=1)
me="Кирилл"
pdf.cell(0,10,txt=me,align="R",ln=1)
pdf.output("card.pdf")
















