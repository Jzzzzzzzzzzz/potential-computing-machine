'''from tkinter import *
window=Tk()
window.geometry("500x600")
window.title("ООП")
canvas=Canvas(window,width=500,height=600,bg="blue")
canvas.pack()'''
'''canvas.create_rectangle(10,10,110,110,fill="yellow",outline="")
canvas.create_rectangle(150,150,200,200,fill="blue",outline="")
canvas.create_rectangle(200,200,260,260,fill="red",outline="white")
canvas.create_polygon(10,260,60,200,110,260,fill="purple")'''

'''canvas.create_rectangle(20,260,100,360,fill="red",outline="")
canvas.create_polygon(10,260,60,200,110,260,fill='green')'''

'''class House:
    def __init__(self,roof_color,wall_color):
        self.roof_color=roof_color
        self.wall_color=wall_color
        self.height=130
        self.width=140
        self.roof=None
        self.wall=None
    def build_house(self,x,y):
        h=self.height
        w=self.width
        self.roof=canvas.create_polygon(x,y,x+w,y,x+w/2,h-100,fill=self.roof_color, outline="")
        canvas.create_rectangle( x+20,y,x+120,y+100, fill=self.wall_color, outline="")
house___1 = House("green","black")
house___2 = House("red","black")
house___3 = House("green","black")
house___1.build_house(20,50)
house___2.build_house(180,50)'''


#Домашняя работа
'''canvas.create_rectangle(180,320, 310, 370, fill="#fff7cb", outline="#313939", width=3)
canvas.create_polygon(180,320,250,200,310,320,fill="#fff7cb", outline="#313939", width=3)#мог придумать поинтереснее рисунок,но не было времени'''

'''class House__:
    def __init__(self,color_1,color_2):
        self.color_1 = color_1
        self.color_2 = color_2
    def build_rectangle(self,x_1,y_1,x_2,y_2):
        self.x_1 = x_1
        self.y_1 = y_1
        self.x_2 = x_2
        self.y_2 = y_2
        canvas.create_rectangle(x_1,y_1,x_2,y_2 ,fill=self.color_1, outline="")
    def build_polygon(self,x_1,y_1,x_2,y_2,x_3,y_3):
        self.x_1 = x_1
        self.y_1 = y_1
        self.x_2 = x_2
        self.y_2 = y_2
        self.x_3 = x_3
        self.y_3 = y_3
        canvas.create_polygon(x_1,y_1,x_2,y_2,x_3,y_3, fill=self.color_2)
house___1 = House__("black","red")
house___1.build_rectangle(180,320,310,370)
house___1.build_polygon(180,320,250,200,310,320)'''



import random
import time

class DUEL:
    def __init__(self,pl,hp):
       self.pl = pl
       self.hp = hp

pl1=DUEL("Игрок первый",100)
pl2=DUEL("Игрок второй",100)
while pl1.hp and pl2.hp !=0:
    damage=random.randint(1,2)
    if damage==1:
        time.sleep(1)
        print(f"Атакует-{pl1.pl}")
        print("Выстрел")
        time.sleep(1)
        print("-"*30)
        pl2.hp -= 20
        time.sleep(1)
        print(f"{pl2.pl} имеет {pl2.hp} здоровья ")
    elif damage==2:
        time.sleep(1)
        print(f"Атакует-{pl2.pl}")
        print("Выстрел")
        time.sleep(1)
        print("-" * 30)
        pl1.hp -= 20
        time.sleep(1)
        print(f"{pl1.pl} имеет {pl1.hp} здоровья ")
if pl1.hp==0:
    time.sleep(1)
    print(f"{pl1.pl} проиграл")
else:
    time.sleep(1)
    print(f"{pl2.pl} проиграл")























