from tkinter import *
import pyautogui
import time

def command_1():
    global entry_1

    entry_1 = int(entry1.get())
    print(entry_1)
    button_close = window.place_slaves()
    for i in button_close:
        0
        i.destroy()
    text1 = Label(text="Какое слово?(eng)", bg="#7842f5", fg="#000000", font=("arial", 30))
    text1.place(width=500, height=150)
    global entry2
    entry2=Entry()
    entry2.place(anchor="center", x=200, y=150, width=200, height=50)
    button_ = Button(text="Далее", bg="#7842f5", fg="#000000", font=("arial", 30), command=command_2)
    button_.place(x=150, y=250)
   #''' text="""После нажатия 'Далее'
#в быстром порядке наведитесь туда,
#кому нужно просмамить!"""
    #label = Label(text=text, bg="#7842f5",fg="#000000", font=("arial", 10))
    #label.place(width=100,height=500)'''#мб потом доделаю с большим размерам экрана

def command_2():
    entry_2 = int(entry2.get()) #для отсчёта можно поставить int,как бы отсчёт N,n.....,1
    print(entry_2)
    button_close = window.place_slaves()
    for i in button_close:
        i.destroy()
    for i in range(4):
        print(f"{i} в срочном порядке наведитесь пока ведется отсчёт до 4")
        time.sleep(1)
        #Можно сделать ещё одну функцию,в которой мы пропишем в самом окне счетчик,отсчёт времени
    for i in range (entry_1):
        print(entry_2)
        entry_2-=1
        pyautogui.write(str(entry_2))
        time.sleep(0.5)
        pyautogui.press('enter')
window=Tk()
window.title("Спамер")
window.geometry("500x400")
window.configure(bg="#7842f5")
text2=Label(text="Сколько раз проспамить?",bg="#7842f5",fg="#000000",font=("arial",30))
text2.place(width=500,height=150)
global entry1
entry1 = Entry()
entry1.place(anchor="center", x=240, y=200, width=200, height=50)
button = Button(text="Далее",bg="#7842f5",fg="#000000",font=("arial",30),command=command_1)
button.place(x=150,y=250)
window.mainloop()


'''a=[10,8,9,7,6,5,4,3,1,2]
while True:
    b=sorted(a)
    print(b)
    for i in b:
        pyautogui.write(str(i))
        pyautogui.press('enter')'''


#До встречи,всего наилучшего!!!!Удачи)!!!