import colorgram as col
from turtle import Turtle, Screen, colormode
import random

colors = col.extract("image.jpg", 35)
t = Turtle()
t.pensize(15)
t.penup()
t.setpos(-210,-120)
row = 1
column = 0
colormode(255)
print(len(colors))
for i in range(84):
    t.color(random.choice(colors).rgb)
    if row == 13:
        column += 1
        t.setpos(-210,-120+(40*column))
        row = 1
    t.pendown()
    t.forward(0)
    t.penup()
    t.forward(35)
    row +=1
t.forward(0)
screen = Screen()
screen.exitonclick()