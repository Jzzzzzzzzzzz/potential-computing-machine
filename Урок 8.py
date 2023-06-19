import time
from tkinter import *
import requests
from bs4 import BeautifulSoup
from datetime import datetime



window = Tk()
window.title("Course")
window.geometry("500x500+200+200")
window.configure(bg="yellow")
window.resizable(False, False)
url = "http://www.cbr.ru/scripts/XML_daily.asp?"

date = "date_req=09/02/2023"
today = datetime.today()
today = today.strftime("%d/%m/%Y/%S")

payload = {"date_req" : today}

response = requests.get(url,payload)

xml = BeautifulSoup(response.content,"html")
def get_valute(id):
     return xml.find("valute",{"id":id}).value.text

def return_():
     time.sleep(0.1)
     global today
     today = datetime.today()
     today = today.strftime("%d/%m/%Y/%S")
     img_logo = PhotoImage(file="logo.png")
     logo = Label(window,image=img_logo,bg="yellow")
     img_logo_ = PhotoImage(file="MOEX_TCSG.png")
     logo_ = Label(window,image=img_logo_,bg="yellow")
     logo.place(x=0,y=0)
     logo_.place(x=300,y=180)
     today=today.replace("/",".")
     lab=Label(window,text="Курс валют\n Dementevs and Tinkoffs bank ",fg="black",font=("arial", 15),bg="yellow")
     lab.place(x=150,y=25)
     lab_=Label(window,text=f"курс на:{today}",fg="black",font=15,bg="yellow")
     lab_.place(x=155,y=470)
     usd=Label(window,text="$"+get_valute("R01235"),font=("arial", 25),bg="yellow")
     usd.place(x=100,y=200)
     eur=Label(window,text="€"+get_valute("R01239"),font=("arial", 25),bg="yellow")
     eur.place(x=100,y=250)
     uan=Label(window,text="¥"+get_valute("R01375"),font=("arial", 25),bg="yellow")
     uan.place(x=100,y=300)
     btn = Button(text="Return", background="#555", foreground="#CCC", font="16", command=return_)
     btn.place(x=150, y=350)
     print(get_valute("R01235")+"$")
     print(get_valute("R01239")+"€")
     print(get_valute("R01375")+"¥")
     print(today)
     print()

     window.mainloop()


return_()
