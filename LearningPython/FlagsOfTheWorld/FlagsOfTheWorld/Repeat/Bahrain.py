'''
    Author: Ismail
    Task: Flags Of the world
    
'''
import turtle

wn = turtle.Screen()
wn.bgcolor("white")
a=turtle.Turtle()
a.penup()
a.goto(300,100)
a.pendown()
a.color("red")
a.begin_fill()
a.forward(-300)
i = 1
while i < 10:
    a.right(30)
    a.forward(20)
    a.right(120)
    a.forward(20)
    a.left(150)
    i = i + 1
a.forward(300)
a.end_fill()
a.color("black")
a.forward(-450)
a.left(90)
a.forward(180)
a.right(90)
a.forward(450)
a.right(90)
a.forward(180)
a.hideturtle()
wn.exitonclick()
