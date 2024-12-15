'''
    Author: Ismail
    Task: Flags Of the world
    
'''
import turtle

wn = turtle.Screen()
wn.bgcolor("white")
a = turtle.Turtle()
a.color("cyan")
a.goto(0,0)
a.begin_fill()
a.forward(500)
a.right(90)
a.forward(300)
a.right(90)
a.forward(500)
a.right(90)
a.forward(300)
a.end_fill()
a.goto(250,-50)
a.color("yellow")
a.begin_fill()
a.left(160)
p = 1
while p < 5:
    a.forward(175)
    a.left(145)
    p = p + 1
a.end_fill()
a.goto(250,-50)
a.color("cyan")
a.goto(50,-30)
a.color("yellow")
a.begin_fill()
p = 1
while p < 5:
    a.forward(20)
    a.left(145)
    p = p + 1
a.end_fill()
a.color("cyan")
a.goto(35,-75)
a.color("yellow")
a.begin_fill()
p = 1
while p < 5:
    a.forward(20)
    a.left(145)
    p = p + 1
a.end_fill()
a.color("cyan")
a.goto(55,-125)
a.color("yellow")
a.begin_fill()
p = 1
while p < 5:
    a.forward(20)
    a.left(145)
    p = p + 1
a.end_fill()
a.color("cyan")
a.goto(45,-190)
a.color("yellow")
a.begin_fill()
p = 1
while p < 5:
    a.forward(20)
    a.left(145)
    p = p + 1
a.end_fill()
a.color("cyan")
a.goto(30,-190)
a.goto(45,-220)
a.color("yellow")
a.begin_fill()
p = 1
while p < 5:
    a.forward(20)
    a.left(145)
    p = p + 1
a.end_fill()
a.color("cyan")
a.goto(60,-275)
a.color("yellow")
a.begin_fill()
p = 1
while p < 5:
    a.forward(20)
    a.left(145)
    p = p + 1
a.end_fill()
a.hideturtle()
wn.exitonclick()

