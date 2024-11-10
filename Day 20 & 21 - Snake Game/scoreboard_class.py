from turtle import Turtle

ALIGN = "center"
FONT = ("Comic Sans",11,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0,280)
        self.points = 0
        self.pencolor("white")
        self.hideturtle()
        self.speed("fastest")
        self.write("Score: "+str(self.points),False,ALIGN,FONT)
        
    
    def score_update(self):
        self.points += 1
        self.clear()
        self.write("Score: "+str(self.points),False,ALIGN,FONT)
        self.goto(0,280)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",False,ALIGN,FONT)