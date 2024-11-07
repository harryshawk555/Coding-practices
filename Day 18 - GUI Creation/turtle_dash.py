from turtle import Turtle, Screen, colormode
from random import randint

t = Turtle()

t.shape("turtle")
t.color("purple")
for i in range(50):
    t.forward(10)
    t.penup()
    t.forward(6)
    t.pendown()
    if (i/20).is_integer(): 
        t.penup()
        if ((i/20)/2).is_integer():
            t.left(90)
            t.forward(10)
            t.left(90)
        else:
            t.right(90)
            t.forward(10)
            t.right(90)
        t.pendown()