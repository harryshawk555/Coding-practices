from turtle import Turtle

ALIGN = "center"
FONT = ("Ariel",20,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.write("0 : 0",False,ALIGN,FONT)
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"{self.l_score} : {self.r_score}",False,ALIGN,FONT)

    def game_over(self):
        self.goto(0,40)
        if self.l_score == 5:
            self.write("Player 1 Wins",False,ALIGN,FONT)
        else:
            self.write("Player 2 Wins",False,ALIGN,FONT)



    
        
