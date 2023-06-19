from tkinter import *
import random

window=Tk()

w=600
h=600

window.geometry(f"{w}x{h}")
canvas=Canvas(window,width=w,height=h)
canvas.pack()

bg_photo=PhotoImage(file="bg_2.png")

class Knight:
    def __init__(self):
        self.x=70
        self.y=h/2
        self.v=0
        self.s=0
        self.photo=PhotoImage(file="knight.png")
    def up(self,event):
        self.v=-3
    def down(self,event):
        self.v=3
    def stop(self,event):
        self.v = 0
        self.s = 0
    def right(self,event):
        self.s=3
    def left(self,event):
        self.s=-3

class Dragon:
    def __init__(self):
        self.x=750
        self.y=random.randint(100,500)
        self.v=random.randint(1,3)
        self.photo=PhotoImage(file="dragon.png")
knight=Knight()

dragons=[]
for i in range(5):
    dragons.append(Dragon())
def game():
    canvas.delete("all")
    canvas.create_image(300,300,image=bg_photo)
    canvas.create_image(knight.x,knight.y,image=knight.photo)

    if 0 <= knight.y <= 600:
        knight.y += knight.v

    '''elif knight.y==600:
        knight.v=-3

    knight.y += knight.v
    if knight.x==0:
        knight.s =-3
    elif knight.x==600:
        knight.s=+3
    knight.x += knight.s'''


    current_dragon=0
    dragon_to_kill=-1

    for dragon in  dragons:
        dragon.x-=dragon.v
        canvas.create_image(dragon.x,dragon.y,image=dragon.photo)
        if ((dragon.x-knight.x)**2+(dragon.y-knight.y)**2)<=(knight.photo.height()/2+dragon.photo.height()/2)**2:
            dragon_to_kill=current_dragon
        current_dragon+=1
        if dragon.x<=0:
            for i in range(1):
                pass
                #dragons.append(Dragon())
            '''canvas.delete("all")
            canvas.create_text(w//2,h//2,text="You win",font='verdana 42',fill="purple")
            break'''

    if dragon_to_kill >=0:
        del dragons[dragon_to_kill]
    if len(dragons)==0:
        for i in range(1):
            pass
            #dragons.append(Dragon())
      #  canvas.delete("all")
        #canvas.create_text(w//2,h//2,text="You win",font='verdana 42',fill="purple")
    else:
        window.after(5,game)



game()

window.bind("<Key-Up>", knight.up)
window.bind("<Key-Down>", knight.down)
window.bind("<Key-Right>",knight.right)
window.bind("<Key-Left>",knight.left)
window.bind("<KeyRelease>",knight.stop)





window.mainloop()
