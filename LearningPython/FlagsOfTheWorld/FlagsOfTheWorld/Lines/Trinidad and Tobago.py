'''
    Author: Ismail
    Task: Flags Of the world
    
'''
import turtle

wn = turtle.Screen()
wn.bgcolor("white")
triangle1 = turtle.Turtle()
triangle1.color("white")
triangle1.right(90)
triangle1.forward(50)
triangle1.left(90)
triangle1.forward(25)
triangle1.left(180)
triangle1.color("red")
triangle1.begin_fill()
triangle1.forward(100)
triangle1.right(90)
triangle1.forward(100)
triangle1.hideturtle()
triangle1.end_fill()

triangle2 = turtle.Turtle()
triangle2.color("white")
triangle2.left(90)
triangle2.forward(50)
triangle2.color("red")
triangle2.right(90)
triangle2.begin_fill()
triangle2.forward(100)
triangle2.right(90)
triangle2.forward(100)
triangle2.end_fill()
triangle2.hideturtle()

rectangle = turtle.Turtle()
rectangle.color("white")
rectangle.forward(-10)
rectangle.color("black")
rectangle.right(45)
rectangle.begin_fill()
rectangle.forward(150)
rectangle.left(90)
rectangle.forward(30)
rectangle.left(90)
rectangle.forward(250)
rectangle.left(90)
rectangle.forward(30)
rectangle.end_fill()
rectangle.hideturtle()
wn.exitonclick()

