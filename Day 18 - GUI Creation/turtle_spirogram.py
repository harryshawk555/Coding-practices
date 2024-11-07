from turtle import Turtle, Screen, colormode
import random as R

t = Turtle()
t.speed(11)

colormode(255)
for i in range(60):
    color = (R.randint(0,255),
            R.randint(0,255),
            R.randint(0,255))
    t.color(color)
    t.circle(100)
    t.left(6)


screen = Screen()
screen.exitonclick()