from turtle import forward, left, exitonclick, right, penup, pendown, speed


def paint_hexagon_forward(side_length, alone):
    for index in range(6):
        forward(side_length)
        left(60)


def prepare_cursor(side_length):
    penup()
    forward(side_length)
    pendown()
    right(60)


speed(1)

side = 60
for i in range(6):
    paint_hexagon_forward(side, False)
    prepare_cursor(side)

exitonclick()
