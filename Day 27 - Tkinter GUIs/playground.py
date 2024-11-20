from tkinter import *

window = Tk()
window.title("GUI Practice")
window.minsize(500,300)
window.config(padx=100,pady=100)

my_label = Label(text ="Label Man", font=("Ariel", 16, "bold"))
my_label.grid(column=0,row=0)

def button_clicked():
    my_label.config(text = input.get())  

button = Button(text="Click Me",command=button_clicked)
button.grid(column=1,row=1)

new_button = Button(text="Click Me Harder",command=button_clicked)
new_button.grid(column=2,row=0)

input = Entry()
input.grid(column=3,row=2)

window.mainloop()