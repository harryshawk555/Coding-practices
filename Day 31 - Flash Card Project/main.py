BACKGROUND_COLOR = "#B1DDC6"
DATA_PATH = "./Day 31 - Flash Card Project/data/"
IMG_PATH = "./Day 31 - Flash Card Project/images/"
T_FONT = ("Ariel",40,"italic")
M_FONT = ("Ariel",60,"bold")

## --------------------------- IMPORTS --------------------------- ##
from tkinter import *
import pandas as pd
import random as rand

## -------------------- BUTTON FUNCTIONALITY --------------------- ##

def right_pressed():
    global curr_word,flip_timer
    words_dict.remove(curr_word)
    frame = pd.DataFrame(words_dict)
    frame.to_csv(f"{DATA_PATH}words_to_learn.csv",index=False)
    next_card()
    

def flip():
    global curr_word
    canvas.itemconfig(card,image=card_back)
    canvas.itemconfig(curr_lang_text,text="English",fill="white")
    canvas.itemconfig(curr_word_text,text=curr_word["English"],fill="white")


def next_card():
    global curr_word,flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(card,image=card_front)
    curr_word = rand.choice(words_dict)
    canvas.itemconfig(curr_word_text,text=curr_word["French"],fill="black")
    canvas.itemconfig(curr_lang_text,text="French",fill="black")

    flip_timer = window.after(3000,flip)
## ---------------------------DATA CHECK-------------------------- ##

try:
    words_csv = pd.read_csv(f"{DATA_PATH}words_to_learn.csv")
except FileNotFoundError:
    full_words_csv = pd.read_csv(f"{DATA_PATH}french_words.csv")
    full_words_csv.to_csv(f"{DATA_PATH}words_to_learn.csv",index=False)
    words_csv = full_words_csv
finally:
    words_dict = words_csv.to_dict(orient="records")

## ----------------------------UI SETUP--------------------------- ##

window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,background=BACKGROUND_COLOR)

card_front = PhotoImage(file=f"{IMG_PATH}card_front.png")
card_back = PhotoImage(file=f"{IMG_PATH}card_back.png")
wrong_button_img = PhotoImage(file=f"{IMG_PATH}wrong.png")
right_button_img = PhotoImage(file=f"{IMG_PATH}right.png")


curr_word = rand.choice(words_dict)
canvas = Canvas(width=800,height=526,background=BACKGROUND_COLOR,highlightthickness=0)
card = canvas.create_image(400,263,image=card_front)
curr_lang_text = canvas.create_text(400,150,text="French",font=T_FONT)
curr_word_text = canvas.create_text(400,263,text=curr_word["French"],font=M_FONT)

canvas.grid(column=0,row=0,columnspan=2)

wrong_button = Button(image=wrong_button_img,highlightthickness=0,command=next_card)
right_button = Button(image=right_button_img,highlightthickness=0,command=right_pressed)

wrong_button.grid(column=0,row=1)
right_button.grid(column=1,row=1)

flip_timer = window.after(3000,flip)


window.mainloop()

