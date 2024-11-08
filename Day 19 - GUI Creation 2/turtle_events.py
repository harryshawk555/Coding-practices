from turtle import Turtle, Screen, colormode
import random as R

t = Turtle()
screen = Screen()


def move_forwards(): 
    t.forward(1)

def turn_right():
    t.setheading(t.heading() - 10)

def turn_left():
    t.setheading(t.heading() + 10)

def move_backwards():
    t.backward(1)

def clear():
    screen.reset()
    t.setpos(0,0)

screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="a", fun=turn_left)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)

screen.listen()

screen.exitonclick()