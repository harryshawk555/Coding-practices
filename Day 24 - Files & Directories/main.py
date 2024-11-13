from turtle import Screen, Turtle
from snake_class import Snake
from food_class import Food
from scoreboard_class import Scoreboard
import time

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
screen.onkey(scoreboard.save,"Escape")


screen.update()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect Food Collision
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.score_increment()
        scoreboard.score_update()
        snake.extend()
    
    #Detect Wall Collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
        food.refresh()
        screen.update()



    #Detect Tail Collision
    for seg in snake.snake_body[1:]:
        if snake.head.distance(seg) < 10:
            scoreboard.reset()
            snake.reset()
            food.refresh()

    #Detect End Game
    if scoreboard.end == True:
        game_is_on = False

   





