from turtle import Turtle
import random as rand

#TODO change the angles so that they are like angle of incidence and not a straight 90 degree shift.

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xmove = 10
        self.ymove = 10
        self.setheading(rand.randint(0,360))
        while self.heading() == 90 or self.heading() == 180:
            self.setheading(rand.randint(0,360))

    def move(self):
        x = self.xcor() + self.xmove
        y = self.ycor() + self.ymove
        self.goto(x,y)

    def y_bounce(self):
        self.ymove *= -1

    def x_bounce(self):
        self.xmove *= -1
    
    def reset(self):
        self.goto(0,0)
        self.xmove *= -1
        