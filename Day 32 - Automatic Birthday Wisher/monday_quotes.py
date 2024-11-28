import smtplib
import datetime as dt
import random as rand

PATH = f"./Day 32 - Automatic Birthday Wisher/quotes.txt"
APP_PASS = ""
MY_EMAIL = ""

now = dt.datetime.now()

if now.weekday() == 0:
    with open(PATH,"r") as file:
        all_quotes = file.readlines()

    quote = rand.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL,APP_PASS)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject: Monday Motivation\n\n{quote}"
        )