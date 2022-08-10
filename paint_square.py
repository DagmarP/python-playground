from turtle import forward, left, shape, exitonclick

shape('turtle')


def paint_square(side, angle):
    for i in range(4):
        forward(side)
        left(angle)
