from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
IMG_PATH = f"./Day 28 - Pomodoro/pineapple.png"
reps = 0
check_string = ""
clock = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_clock():
    global check_string
    global reps
    window.after_cancel(clock)
    timer.config(text="Timer",fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    checks.config(text = "")
    check_string = ""
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_clock():
    global reps
    reps += 1
    work_secs = WORK_MIN*60
    short_break_secs = SHORT_BREAK_MIN*60
    long_break_secs = LONG_BREAK_MIN*60


    if reps % 8 == 0:
        timer.config(text ="Break",fg=RED)
        countdown(long_break_secs)
    elif reps % 2 == 0:
        timer.config(text ="Break",fg=PINK)
        countdown(short_break_secs)
    else:
        timer.config(text ="Work",fg = GREEN)
        countdown(work_secs)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count):
    global clock
    global reps
    global check_string
    mins = math.floor(count / 60)
    secs = count % 60
    if secs < 10:
        secs = f"0{secs}"

    canvas.itemconfig(timer_text, text=f"{mins}:{secs}")
    if count > 0:
        clock = window.after(1000, countdown, count-1) 
    else:
        if reps % 2 == 1:
            check_string = f"{check_string}✔"
            checks.config(text = check_string)
        start_clock()
        




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)

canvas = Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file=IMG_PATH)
canvas.create_image(100, 112, image=photo)
timer_text = canvas.create_text(100,160, text="00:00", fill = "black",font=(FONT_NAME,20,"bold"))
canvas.grid(column=1,row=1)

timer = Label(text="Timer", font=(FONT_NAME,40,"bold"), fg=GREEN, bg=YELLOW)
timer.grid(column=1,row=0)

start = Button(text="Start", highlightthickness=0 ,command=start_clock)
start.grid(column=0,row=2)

reset = Button(text="Reset", highlightthickness=0, command=reset_clock)
reset.grid(column=2,row=2)

checks = Label(fg=GREEN, bg=YELLOW)
checks.grid(column=1,row=3)

window.mainloop()