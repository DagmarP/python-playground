import turtle
from turtle import forward, penup ,pendown ,shape ,exitonclick,left,right, stamp, turtles
# shape('turtle')
# stamp the turtle shape


cycle = 10
lenght = 30
high = 30
a = turtle.Turtle()
a.shape("turtle")
a.pencolor('#5e3110')
a.penup()
a.goto(-350, -350)
a.pendown()
b = turtle.Turtle()
b.shape("turtle")
b.pencolor('#666007')
b.penup()
b.goto(a.position()[0], a.position()[1]-high)
b.pendown()

for i in range(cycle):

    a.forward(lenght)
    b.forward(lenght)
    a.left(90)
    b.left(90)
    a.stamp()
    b.stamp()
    a.forward(high)
    b.forward(high)
    a.right(90)
    b.right(90)
    a.forward(lenght)
    b.forward(lenght)

