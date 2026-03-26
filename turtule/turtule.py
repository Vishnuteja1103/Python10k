import turtle
import colorsys

t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(100)
t.width(2)

h=0
angle=0

while True:
    color = colorsys.hsv_to_rgb(h, 1, 1)
    t.pencolor(color)
    t.forward(30)
    t.right(170)
    t.forward(50)
    t.right(angle)

    angle += 0.5
    h +=0.002