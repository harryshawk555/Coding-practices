from turtle import Turtle, Screen, colormode
from random import randint

t = Turtle()

t.shape("turtle")
t.color("purple")
for i in range(4):
    t.forward(100)
    t.left(90)


screen = Screen()
screen.exitonclick()