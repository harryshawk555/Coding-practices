from tkinter import *

FONT = ("Ariel", 16, "bold")
PAD = 10

window = Tk()
window.title("Miles To Kilometers Converter")
window.minsize(500,300)
window.config(padx=PAD,pady=PAD)

miles = Label(text ="Miles", font=FONT)
miles.grid(column=2,row=0)
miles.config(padx=PAD,pady=PAD)

equal = Label(text ="is equal to", font=FONT)
equal.grid(column=0,row=1)
equal.config(padx=PAD,pady=PAD)

km = Label(text ="0", font=FONT)
km.grid(column=1,row=1)
km.config(padx=PAD,pady=PAD)

kilometers = Label(text ="Km", font=FONT)
kilometers.grid(column=2,row=1)
kilometers.config(padx=PAD,pady=PAD)

def button_clicked():
    mile = int(input.get())
    kilos  = mile*1.609
    km.config(text=round(kilos))  

button = Button(text="Calculate",command=button_clicked)
button.grid(column=1,row=2)
button.config(padx=PAD,pady=PAD)

input = Entry()
input.grid(column=1,row=0)


window.mainloop()