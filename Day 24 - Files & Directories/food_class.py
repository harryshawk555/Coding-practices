from turtle import Turtle
import random as R

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        x = R.randint(-28,28)*10
        y = R.randint(-28,28)*10
        self.goto(x,y)

    def refresh(self):
        x = R.randint(-28,28)*10
        y = R.randint(-28,28)*10
        self.goto(x,y)