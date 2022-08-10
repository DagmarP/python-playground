from turtle import forward, left, shape, exitonclick, speed
from paint_square import paint_square
shape('turtle')
count = 0
angle = 200
rotate = 150
cycles = 20
side = 10
speed = 0
for i in range(cycles):
    paint_square(side, angle)
    left(rotate)
    count = count+1
    speed = i
left(360 - count * angle)
exitonclick()
