from turtle import Turtle

ALIGN = "center"
FONT = ("Comic Sans",11,"normal")
PATH = r"./Day 24 - Files & Directories/highscore.txt"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0,280)
        self.points = 0
        self.end = False
        self.pencolor("white")
        self.hideturtle()
        self.speed("fastest")
        self.write("Score: "+str(self.points),False,ALIGN,FONT)
        file = open(PATH,"r")
        self.highscore = int(file.readline())
        file.close()

        
    
    def score_update(self):
        self.clear()
        self.write(f"Score: {self.points} High Score: {self.highscore}",False,ALIGN,FONT)
        self.goto(0,280)

    def score_increment(self):
        self.points += 1

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",False,ALIGN,FONT)

    def reset(self):
        if self.points > self.highscore:
            self.highscore = self.points
        
        self.points = 0
        self.score_update()
    
    def save(self):
        self.reset()
        file = open(PATH,"w")
        file.write(str(self.highscore))
        file.close()
        self.end = True