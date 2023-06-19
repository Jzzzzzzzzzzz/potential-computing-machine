from tkinter import *
import requests
from bs4 import BeautifulSoup
import random
import os
#import time
#from threading import Thread
window=Tk()
window.configure(bg="Black")

window.title("Забавное местечко")
window.geometry("700x600")
text1=Label(text="Добро пожаловать!",bg="red",fg="blue",font=("arial",30))
text1.place(width=700,height=100)


def reboot():
    os.system('shutdown -r -t 0')



def close():
    window.geometry("1080x1920")
    window.configure(bg="black")
    window.attributes("-fullscreen", True)
    button_close=window.place_slaves()
    for i in button_close:
        i.destroy()
    text1.destroy()
    text2.destroy()
    response = requests.get("https://i-fakt.ru/")
    response = response.content
    html = BeautifulSoup(response, "html.parser")
    fact = random.choice(html.find_all(class_="p-2 clearfix"))
    a=Label(text=fact.text+fact.a.attrs["href"],font=("arial",12),fg="blue",bg="red")
    a.place(x=50,y=300)
    button_3 = Button(text="Продолжить?", font=("arial", 15), fg="blue", bg="red", command=close)
    button_3.place(x=500, y=300)
    button_4 = Button(text="Выйти?", font=("arial", 15), fg="blue", bg="red",command=money)
    button_4.place(x=640, y=300)
    button_5 = Button(text="Перейти на ссылку", font=("arial", 15), fg="blue", bg="red", command=money)
    button_5.place(x=725,y=300)

#тут пытался сделать секндомер,почему-то виснет(
'''def time():
    global a
    a = 0
    while True:
        a += 1
        b = Label(text=a)
        b.place(x=1000, y=300)
        time.sleep(1)'''

def money():
    button_close = window.place_slaves()
    for i in button_close:
        i.destroy()
    window.attributes("-fullscreen", True)
    money=Label(text="Вас взломали! Введите любую сумму денег в эту строку",font=("arial",30),fg="red",bg="black")
    money.place(anchor="center",x=1000,y=500)
    entry=Entry()
    entry.place(anchor="center",x=1000,y=700,width=260,height=50)
    text3=Button(text="Далее",font=("arial",30),fg="red",bg="black",command=scum)
    text3.place(x=980,y=725)
    #time()

def scum():
    window.attributes("-fullscreen",True)
    window.configure(bg="red")
    button_close=window.place_slaves()
    for i in button_close:
        i.destroy()
    window.resizable(False,False)
    for i in range(1500):
        text_skum = Label(text="Тебя заскамили",font=("Courier New",20),fg="black",bg="Red")
        text_skum.place(x=random.randint(1,1800),y=random.randint(200,1000))
    window.protocol("WM_DELETE_WINDOW",lambda:None)
    button___=Button(text="Закрыть вирус!",font=("arial",35),fg="White",bg="Red",command=reboot)
    button___.place(x=750,y=100)


def close_2():

    window.configure(bg="black")
    window.attributes("-fullscreen", True)
    button_close=window.place_slaves()
    for i in button_close:
        i.destroy()
    text1.destroy()
    text2.destroy()
    response = requests.get("https://kudago.com/msk/festival/")
    response = response.content
    html = BeautifulSoup(response, "html.parser")
    fact = random.choice(html.find_all(class_="post-title"))
    b=Label(text=fact.text+fact.a.attrs["href"],font=("arial",10),fg="blue",bg="red")
    b.place(x=500,y=300)
    c = Label(text=fact.text + fact.a.attrs["href"], font=("arial", 23), fg="blue", bg="red")
    c.place(x=500, y=300)
    button_3 = Button(text="Продолжить?", font=("arial", 15), fg="blue", bg="red", command=close_2)
    button_3.place(x=500, y=300)
    button_4 = Button(text="Выйти?", font=("arial", 15), fg="blue", bg="red",command=money)
    button_4.place(x=640, y=300)
    button_5 = Button(text="Перейти по ссылке", font=("arial", 15), fg="blue", bg="red", command=money)
    button_5.place(x=725, y=300)


text2=Label(text="Что бы вы хотели сделать?",font=("arial",25),fg="Blue",bg="black")
text2.place(x=140,y=210)
def fact():
    window.resizable(False, False)
    button_1 = Button(text="Посмотрим факты", font=("arial", 25),fg="blue",bg="red",command=close)
    button_1.place(x=12, y=300)
    button_2 = Button(text="Пройдем по ивентам", font=("arial", 25),fg="Blue",bg="red" ,command=close_2)
    button_2.place(x=350, y=300)
fact()



window.mainloop()
