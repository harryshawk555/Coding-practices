##################### Extra Hard Starting Project ######################

import smtplib
import datetime as dt
import random as rand
import pandas as pd

BDAY_PATH = f"./Day 32 - Automatic Birthday Wisher/birthdays.csv"
LETTERS_PATH = f"./Day 32 - Automatic Birthday Wisher/letter_templates/"
APP_PASS = ""
MY_EMAIL = ""

data_csv = pd.read_csv(BDAY_PATH)
data_dict = data_csv.to_dict(orient="records")
now = dt.datetime.now()
for person in data_dict:
    if person["month"] == now.month and person["day"] == now.day:
        with open(f"{LETTERS_PATH}letter_{rand.randint(1,3)}.txt") as file:
            full_letter = file.readlines()
        send_string = ""
        for line in full_letter:
            if "[NAME]" in line:
                new_line = line.replace("[NAME]",person["name"])
                send_string += f"{new_line}"
            else:
                send_string += f"{line}"
        print(send_string)
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL,APP_PASS)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=person["email"],
                msg=f"Subject: Happy Birthday, {person['name']}\n\n{send_string}"
            )



