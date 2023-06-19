'''from tkinter import *

window=Tk()
window.attributes("-fullscreen",True)
window.title("вирус")
window.geometry("1080x1920")
window.configure(bg="Yellow")


def scum():
    text=Label(text="ВЫ ВЫЙГРАЛИ В ЛОТЕРЕЕЕЕЕЕЕ!!!!!!",font=("arial,",30),fg="Black")
    text.place(anchor="center",x=1000,y=500)
    button_1=Button(text="ПОЛУЧИТЬ ВЫЙГРЫШ",font=("arial,",30),fg="Black",command=scum_2)
    button_1.place(anchor="center",x=1000,y=600)

def scum_2():
    button_close = window.place_slaves()
    for i in button_close:
        i.destroy()
    text_2=Label(text="Чтобы получить выигрышь внесите 10000000000000000000000 рублей",font=("arial,",30),fg="Black")
    text_2.place(anchor="center",x=1000,y=500)
    enter=Entry()
    enter.place(anchor="center",x=1000,y=600,height=50)
    window.protocol("WM_DELETE_WINDOW", lambda: None)
    button_1 = Button(text="Далее", font=("arial,", 30), fg="Black",command=scum_3)
    button_1.place(anchor="center",x=1150,y=600)
def scum_3():

    text=Label(text="с вашего баланса списанно 10000000........ ",font=("arial,",50),fg="Black")
    text.place(anchor="center",x=1000,y=600)

scum()

window.mainloop()'''






from tkinter import *
window=Tk()
window.attributes("-fullscreen",True)
window.title("Cats)")
window.geometry("1080x1920")
window.configure(bg="turquoise")
cats=Label(text="Посмотрим котиков?",font=("arial,",50),fg="Black")
cats.place(anchor="center",x=1000,y=100)
photo=PhotoImage(file="cat.png")
PH=Label(image=photo,bg="Black")
PH.image=photo
PH.place(x=0,y=0)

def image():
    pass



window.mainloop()




