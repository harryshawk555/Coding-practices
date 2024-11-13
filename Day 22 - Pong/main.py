from turtle import Turtle, Screen
import time
from scoreboard_class import Scoreboard
from ball_class import Ball
from paddle_class import Paddle

screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.screensize(600,600)
screen.listen()
scoreboard = Scoreboard()
ball = Ball()
game_on = True

line = Turtle()
line.speed("fastest")
line.color("white")        
line.penup()
line.pensize(5)    
line.goto(0,-300)
line.setheading(90)
line.hideturtle()
for i in range(19):
    line.pendown()
    line.forward(20)
    line.penup()
    line.forward(10)


l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))
screen.update()
screen.onkeypress(r_paddle.up,"Up")
screen.onkeypress(r_paddle.down,"Down")
screen.onkeypress(l_paddle.up,"w")
screen.onkeypress(l_paddle.down,"s")


while game_on:
    ball.move()
    screen.update()
    time.sleep(0.1)

    #Top Wall Collision
    if ball.ycor()>= 280:
        ball.y_bounce()
    if ball.ycor()<= -280:
        ball.y_bounce()

    #Paddle Collision
    if ball.distance(r_paddle) <= 50 and ball.xcor() > 320 or ball.distance(l_paddle) <= 50 and ball.xcor() < -320:
        ball.x_bounce()
    
    #Back Wall Collision
    if ball.distance(r_paddle) >= 50 and ball.xcor() > 340:
        scoreboard.l_score += 1
        scoreboard.update_score()
        ball.reset()
    if ball.distance(l_paddle) >= 50 and ball.xcor() < -340:
        scoreboard.r_score += 1
        scoreboard.update_score()
        ball.reset()
    
    if scoreboard.l_score == 5 or scoreboard.r_score == 5:
        game_on = False
        scoreboard.game_over()
        line.clear()
        screen.update()



        
screen.exitonclick()