from turtle import Turtle, Screen, colormode
import random as R

screen = Screen()
screen.setup(500,400)
colors = ["red","orange","yellow","green","blue","purple"]

turtles = []
is_race_on = False

for i in range(6):
    t = Turtle("turtle")
    t.penup()
    t.color(colors[i-1])
    t.goto(-230,-100+(40*(i)))
    turtles.append(t)
    t.xcor
#def go(turtles):
#    for t in turtles:
        

bet = screen.textinput("Make Your Bet", "Which Turtle do you think will win the race? ")
if bet:
    is_race_on = True

while is_race_on:
    dist = R.randint(0,10)
    curr_turtle = R.choice(turtles)
    curr_turtle.forward(dist)
    if curr_turtle.xcor() > 230:
        winner = curr_turtle.pencolor()
        is_race_on = False

if bet == winner:
    print(f"You won!! {winner} Won!!")
else:
    print(f"You lost!!! {winner} Won")