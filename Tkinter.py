'''from tkinter import *
window=Tk()
window.geometry("700x500")
window.title("Вопросы")


facts=[
    {
        "text":"Имя Халка-Брюс Беннет:",
        "right":1
    },
    {
        "text":"Уолт Дисней является создателем вселенной Marvel:",
        "right":0
    },
    {
        "text":"До появления супергероя муравей занимался воровством:",
        "right":1

    },
]
num=0
points=0


label_title=Label(text="Тест Marvel",font=("Arial",24),fg="white",bg="red")
label_title.place(x=0,y=0,width=700,height=100)


fact=Message(text=facts[num]['text'],font=("Arial",15),width=700,bg="green")
fact.place(x=10,y=120)
var=IntVar()
true=Radiobutton(text="Правда",variable=var,value=1)
true.place(x=10,y=160)
false=Radiobutton(text="Ложь",variable=var,value=0)
false.place(x=10,y=190)

#спросить как сделать скрипты
window.mainloop()'''




'''for question in facts:
    print(question.get("text"))
    num=0
    for question in question.get("text"):
        num+=1'''



from tkinter import *
import random

window=Tk()
window.geometry("700x500")
window.title("Кликер")
points=0
POINT=points+20
COLOR=['green','black']
def check():
    global points
    b.place(x=random.randint(1,550),y=random.randint(1,350))
    points+=1
    label['text']=points
    global COLOR
    if points==POINT:

b = Button(text="нажми меня!)", font=("Arial", 30), fg="BLUE",command=check)
b.place(x=200,y=130)
label=Label(text=points,font=("Arial",15),fg="black")
label.place(x=10,y=10)
window.mainloop()