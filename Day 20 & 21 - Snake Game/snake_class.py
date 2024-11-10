from turtle import Screen, Turtle

DOWN = 270
UP = 90
LEFT = 180
RIGHT = 0

class Snake():

    def __init__(self):
        self.snake_body = []
        self.create_snake()
    
    def create_snake(self):
        self.head = Turtle("square")
        self.head.color("white")
        self.head.penup()
        self.snake_body.append(self.head)
        for i in range(2):
            body = Turtle("square")
            body.penup()
            body.color("white")
            body.setx(-20*(i+1))
            self.snake_body.append(body)

    def move(self):
        for i in range(len(self.snake_body)-1,0,-1):
            self.snake_body[i].goto(self.snake_body[i-1].xcor(),self.snake_body[i-1].ycor())
        self.head.forward(20)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def up(self):
        if self.head.heading != DOWN:
            self.head.setheading(UP)

    def extend(self):
        body = Turtle("square")
        body.penup()
        body.color("white")
        body.setx(self.snake_body[-1].xcor())
        body.sety(self.snake_body[-1].ycor())
        self.snake_body.append(body)
    
        