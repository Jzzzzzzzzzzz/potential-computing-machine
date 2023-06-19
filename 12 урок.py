from tkinter import *
import time
import random


class Ball:
    def __init__(self,canvas,platform,color):
        self.canvas=canvas
        self.platform=platform
        #self.color=color
        self.oval=canvas.create_oval(200,200,215,215,fill=color)
        self.x=3
        self.y=-3
        self.touch_bottom = False

    def draw(self):
        self.canvas.move(self.oval,self.x,self.y)
        pos=self.canvas.coords(self.oval)
        if pos[1]<=0:
            self.y=3
        if pos[3]>=400:
            self.touch_bottom = True
        if pos[0]<=0:
            self.x=3
        if pos[2]>= 500:
            self.x=-3
        if self.touch_platform(pos):
            self.y=-3
    def touch_platform(self,ball_pos):
        platform_pos=self.canvas.coords(platform.rect)
        if ball_pos[2]>=platform_pos[0] and ball_pos[0]<= platform_pos[2]:
            if ball_pos[3]>=platform_pos[1] and ball_pos[3]<= platform_pos[3]:
                return True
        return False
class Platform:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.rect = canvas.create_rectangle(230, 300, 330, 310, fill=color)
        self.x = -2
        self.canvas.bind_all('<KeyPress-Left>', self.left)
        self.canvas.bind_all('<KeyPress-Right>', self.right)

    def left(self, event):
        self.x = -2

    def right(self, event):
        self.x = 2

    def draw(self):
        self.canvas.move(self.rect, self.x, 0)
        pos = self.canvas.coords(self.rect)
        if pos[0] <= 0:
            self.x = 0
        if pos[2] >= 500:
            self.x = 0

window=Tk()
window.title("Arcade")
window.resizable(0,0)
window.wm_attributes("-topmost",1)
canvas=Canvas(window,width=500,height=400)
canvas.pack()

platform=Platform(canvas,"Green")
ball=Ball(canvas,platform,"green")

def Cross():
    global run
    run=False
run=True
window.protocol('WM_DELETE_WINDOW', Cross)

while run:
    if ball.touch_bottom:
        break
    platform.draw()
    ball.draw()

    window.update()

    time.sleep(0.01)

#До встречи,удачи,пока!))!!!