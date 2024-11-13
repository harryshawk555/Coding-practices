from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,start):
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.shapesize(5,1)
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.goto(start)
        self.showturtle()

    def up(self):
        self.goto(self.xcor(), self.ycor()+20)

    def down(self):
        self.goto(self.xcor(), self.ycor()-20)