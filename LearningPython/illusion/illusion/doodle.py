'''
    Author: Mohammad Ismail Ashiq Aslam
    Task: illusion
    Part: A - Doodle
    
'''
from tkinter import *
import time
from drawingPanel import*

background = Tk()

a = Canvas(background, width=400, height=400)
a.pack()

def drawSquare(canvas,x1,y1,x2,y2, fillColour):
    canvas.create_rectangle(x1,y1,x2,y2,fill = fillColour)

    
bigR = drawSquare(canvas, 100, 100, 6, "yellow")
smallR = drawSquare(50, 50, 100, 100, "green")

for i in range(1000):
    bigR.move()
    smallR.move()
    background.update()
    time.sleep(0.01)

background.mainloop()
