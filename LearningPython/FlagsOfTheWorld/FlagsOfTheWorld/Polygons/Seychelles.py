'''
    Author: Ismail
    Task: Flags Of the world
    
'''
import turtle

wn = turtle.Screen()
wn.bgcolor("white")
a = turtle.Turtle()
a.color("white")
a.goto(0,150)
a.color("blue")
a.begin_fill()
a.left(90)
a.forward(150)
a.right(90)
a.forward(100)
a.end_fill()
a.color("yellow")
a.goto(0,150)
a.begin_fill()
a.goto(100,300)
a.forward(100)
a.goto(0,150)
a.end_fill()
a.color("red")
a.begin_fill()
a.goto(200,300)
a.forward(100)
a.right(90)
a.forward(50)
a.goto(0,150)
a.end_fill()
a.color("green")
a.begin_fill()
a.goto(300,200)
a.forward(50)
a.goto(0,150)
a.end_fill()
a.color("black")
a.left(90)
a.forward(300)
a.left(90)
a.forward(150)
a.left(90)
a.forward(300)
a.left(90)
a.forward(150)
a.hideturtle()
wn.exitonclick()

