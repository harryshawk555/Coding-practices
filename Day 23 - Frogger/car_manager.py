COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random as rand


class Car(Turtle):
    def __init__(self):
        super().__init__()       
        self.penup()
        self.goto(350,rand.randint(-250,250))
        self.color(rand.choice(COLORS))
        self.shape("square")
        self.shapesize(1,2)
    
    def move(self,dist):
        self.goto(self.xcor()-dist,self.ycor())

    def delete(self):
        self.hideturtle()
        del(self)



class CarManager():
    def __init__(self):
        self.cars = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        car = Car()
        self.cars.append(car)

    def move_all(self):
        for car in self.cars:
            car.move(self.move_speed)


    def increment(self):
        self.move_speed += MOVE_INCREMENT

    def level_up(self):
        for car in self.cars:
            car.delete()
        self.cars = []
        self.increment()

    



