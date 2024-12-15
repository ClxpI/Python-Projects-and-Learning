'''
    Author: Ismail
    Task: Flags Of the world
    
'''
import turtle

wn = turtle.Screen()
wn.bgcolor("white")
circle = turtle.Turtle()
circle.color("red")
circle.begin_fill()
circle.circle(30)
circle.hideturtle()
circle.end_fill()

rectangle = turtle.Turtle()
rectangle.color("white")
rectangle.right(180)
rectangle.forward(75)
rectangle.color("black")
rectangle.left(90)
rectangle.forward(20)
rectangle.left(90)
rectangle.forward(150)
rectangle.left(90)
rectangle.forward(100)
rectangle.left(90)
rectangle.forward(150)
rectangle.left(90)
rectangle.forward(80)
rectangle.hideturtle()
wn.exitonclick()

