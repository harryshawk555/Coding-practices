from turtle import Turtle, Screen, colormode
from random import randint

t = Turtle()

t.shape("turtle")
t.color("purple")

colormode(255)
for a in range(3,11):
    color = (randint(0,255),
            randint(0,255),
            randint(0,255))
    t.color(color)
    angle = 360/a
    for i in range(a):
        t.forward(100)
        t.right(angle)
        

screen = Screen()
screen.exitonclick()