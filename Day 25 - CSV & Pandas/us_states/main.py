import pandas as pd
from turtle import Screen, Turtle, shape
#import turtle
DATA_PATH = r"./Day 25 - CSV & Pandas/us_states/50_states.csv"
IMG_PATH = r"./Day 25 - CSV & Pandas/us_states/blank_states_img.gif"
OUT_PATH = r"./Day 25 - CSV & Pandas/us_states/states_to_learn.csv"
ALIGN = "Center"
FONT = ("Ariel",8,"normal")


screen = Screen()
screen.title("U.S. States Game")
image = IMG_PATH
screen.addshape(image)
shape(image)
data = pd.read_csv(DATA_PATH)
states = data.state.to_list()
score = 0

game_on = True
while game_on:
    if states == []:
        turt.goto(0,0)
        turt.write(f"Well done, you got {score}/50 correct",False,ALIGN,FONT)
        game_on = False
        break
    
    answer_state = screen.textinput("Guess The State","Whats another State's Name?").title()
    if answer_state == "Exit":
        break

    

    if answer_state in states:
        turt = Turtle()
        turt.hideturtle()
        turt.penup()
        x = data[data.state == answer_state].x.item()
        y = data[data.state == answer_state].y.item()
        turt.goto(x,y)
        turt.write(answer_state,False,ALIGN,FONT)
        score += 1
        states.pop(states.index(answer_state))
    elif score == 50:
        turt.goto(0,0)
        turt.write(f"Well done, you got {score}/50 correct",False,ALIGN,FONT)
        game_on = False
    else:
        turt.goto(0,0)
        turt.write(f"Well done, you got {score}/50 correct",False,ALIGN,FONT)
        game_on = False

print("Nice One, but you missed")
for i in states:
    print(f"{i}")

states_to_learn = pd.DataFrame(states)
states_to_learn.to_csv(OUT_PATH)

screen.exitonclick()
