import time
import random as rand
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()

screen.onkeypress(player.move,"space")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.move_all()

    car_chance = rand.randint(0,2)
    if car_chance == 2:
        car_manager.create_car()

    #Level Up
    if player.ycor()>=player.finish:
        player.level_up()
        scoreboard.level_up()
        car_manager.level_up()

    #Car Collision
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            screen.update()
            scoreboard.game_over()


screen.exitonclick()

