FONT = ("Courier", 24, "normal")
ALIGN = "left"

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280,260)
        self.write("Level: 1",False,ALIGN,FONT)
        self.level = 1
    
    def level_up(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}",False,ALIGN,FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("You Lose!!",False,"center",FONT)
