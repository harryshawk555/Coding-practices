from tkinter import *
from tkinter import messagebox
import random
import json
from random import choice, randint, shuffle
import pyperclip as pc

IMG_PATH = f"./Day 29 - Password Manager/logo.png"
FILE_PATH = f"./Day 30 - Errors, Exceptions and JSON/data.json"
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    pass_letters = [choice(LETTERS) for _ in range(randint(8, 10))]
    pass_symbols = [choice(SYMBOLS) for _ in range(randint(2, 4))]
    pass_numbers = [choice(NUMBERS) for _ in range(randint(2, 4))]

    password_list = pass_letters + pass_symbols + pass_numbers

    shuffle(password_list)

    password = "".join(password_list)
    pc.copy(password)
    
    password_entry.delete(0,END)
    password_entry.insert(0,password)



# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_entry.get()
    password = password_entry.get()
    user = email_entry.get()

    if website != "" and password != "" and user != "":    
        
        new_data = {
            website: {
                "email": user,
                "password": password
            }
        }
        
        # is_ok = messagebox.askokcancel(title=website,message=f"These are details entered.\nEmail: {user}"
        #                              f"\nPassword: {password}\nIs this ok to save?")
        try:
            open(FILE_PATH,"r")
        except FileNotFoundError:
            with open(FILE_PATH,"w") as file:
                json.dump(new_data, file, indent=4)
        else:
            with open(FILE_PATH, "r") as file:
                data = json.load(file)
                data.update(new_data)
            with open(FILE_PATH,"w") as file:
                json.dump(data, file, indent=4)  
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)
    else:
        messagebox.showinfo(title="Empty Fields",message="Please don't leave any fields blank")

# ---------------------------- LOAD PASSWORD ------------------------------- #

def search():
    try:
        with open(FILE_PATH,"r") as file:
            data_dict = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="No Passwords",message="No passwords found")
    else: 
        if website_entry.get() in data_dict:
            data = data_dict[website_entry.get()]
            messagebox.showinfo(title=website_entry.get(),message=f"Email: {data['email']}\nPassword: {data['password']}")
        else:
            messagebox.showinfo(title="No Passwords",message=f"No passwords found for the website {website_entry.get()}")
    finally:
        website_entry.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

image = PhotoImage(file=IMG_PATH)

canvas = Canvas(height=200,width=200)
canvas.create_image(100,100,image=image)
canvas.grid(column=1,row=0)

website_label = Label(text="Website:")
website_label.grid(column=0,row=1)

website_entry = Entry(width=33)
website_entry.grid(column=1,row=1,sticky=W)
website_entry.focus()

email_label = Label(text="Email/Username:")
email_label.grid(column=0,row=2)

email_entry = Entry(width=53)
email_entry.grid(column=1,row=2,columnspan=2,sticky=W)
email_entry.insert(0,"topleyharry@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0,row=3)

password_entry = Entry(width=33)
password_entry.grid(column=1,row=3,sticky=W)

password_gen = Button(width=15,text="Generate Password",command=generate_password)
password_gen.grid(column=2,row=3,sticky=W)

add_password = Button(width=44,text="Add",command=save_password)
add_password.grid(column=1,row=4,columnspan=2,sticky=W)

search_password = Button(width=15,text="Find Password", command=search)
search_password.grid(column=2,row=1,sticky=W)


window.mainloop()
