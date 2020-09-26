from tkinter import *
import random
class TV():
    """TV"""

    def __init__(self,energy_,volume_,canvas):
        self.energy_ = energy_
        self.volume_ = volume_
        self.canvas = canvas

    def v_(self,canvas):
        v = int(input())
        if 0 <= v <= 20:
            volume_ = v
            canvas.create_text(480,20,text = v,fill="white")

    def energy_1(self,energy_):
        energy_ = 100
        while energy_ != 0:
            energy_ -= 1       

    def TvChannels(self):
        while self.energy_ != 0:
            re = int(input())
            return re

    def draw():
        canvas.create_rectangle(5,5,495,395,fill = "black",outline = 'white')

class TVchannel():
    """channels"""    

    def __init__(self,canvas,r):
        self.canvas = canvas

    def draW(self,canvas,r):
        c = "#" + ('%06x'%random.randint(0,16777215))
        canvas.create_rectangle(10,10,490,390,fill=c,outline="white")
        print(re)


def main():
    TV1_ = TV(100,0,canvas)
    re = 0
    ch1 = TVchannel(canvas,re)
    ch2 = TVchannel(canvas,re)
    ch3 = TVchannel(canvas,re)
    u = 0
    Tvset = dict()
    Tvset[1] = ch1
    Tvset[2] = ch2
    Tvset[3] = ch3
    re = TV1_.TvChannels()
    u = Tvset[re]
    re = int(re)
    u.draW(canvas,re)
    TV1_.v_(canvas)

root = Tk()
canvas = Canvas(root,width=500,height=400,bg='black')
canvas.pack() 

main()
root.mainloop()