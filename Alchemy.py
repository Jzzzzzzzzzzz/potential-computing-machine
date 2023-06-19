import random
from tkinter import *
from random import randint


window = Tk()
#window.geometry("600x600")

class Fire:
    image = PhotoImage(file="fire.png").subsample(4,4)


    def __add__(self, other):
        if isinstance(other,Earth):
            return Lava
        return None

class Water:
    image = PhotoImage(file="water.png").subsample(4,4)


class Wind:
    image = PhotoImage(file="wind.png").subsample(4,4)


class Earth:
    image = PhotoImage(file="ground.png").subsample(4,4)


class Lava:
    image = PhotoImage(file="lava.png").subsample(4, 4)


canvas = Canvas(window,width = 600,height=600)
canvas.pack()

elements = [Fire(),Earth(),Water(),Wind()]


for elem in elements:
    canvas.create_image(randint(50,550),randint(50,550),image=elem.image)

def move(event):
    #print(event.x,event.y)
    images_id = canvas.find_overlapping(event.x,event.y,event.x + 10,event.y + 10)

    if len(images_id) == 2:

        element_1 = elements[images_id[0] - 1]
        element_2 = elements[images_id[1] - 1]

        new_elem = element_1 + element_2

        if new_elem:
            if new_elem not in elements:
                canvas.create_image(event.x,event.y,image = new_elem.image)
                elements.append(new_elem)

    canvas.coords(images_id,event.x,event.y)



window.bind('<B1-Motion>',move)



window.mainloop()

