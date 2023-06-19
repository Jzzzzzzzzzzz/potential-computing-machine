from fpdf import FPDF
pdf=FPDF("P","cm",(12,20))
pdf.add_page()
pdf.add_font("cour","","C:\Windows\Fonts\BOOKOS.ttf",uni=True)
pdf.set_font("cour",size=16)
pdf.set_text_color(0,255,255)
pdf.set_fill_color(155,255,255)
pdf.cell(10,5,txt="Hello",align="C",fill=True )

pdf.image("pic.jpg",x=1,y=9,h=0,w=10)




pdf.output("test.pdf")