from turtle import Turtle, Screen, colormode
import random as R

t = Turtle()

t.shape("turtle")
t.color("purple")
t.pensize(6)

colormode(255)

walk_length = R.randint(1,200)
angles = [0,90,180,270]

for i in range(walk_length):
    color = (R.randint(0,255),
            R.randint(0,255),
            R.randint(0,255))
    t.color(color)
    t.forward(50)
    t.left(R.choice(angles))
screen = Screen()
screen.exitonclick()