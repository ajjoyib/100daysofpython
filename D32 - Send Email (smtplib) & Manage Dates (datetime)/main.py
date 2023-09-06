import datetime
import pandas
import random
import smtplib

MY_EMAIL = "hamidullo287@gmail.com"
MY_PASSWORD = "20@flraganuS04"

today = (datetime.datetime.now().month, datetime.datetime.now().day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt", "r") as letter_file:
        contents = letter_file.read()
        letter_to_send = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday\n\n{letter_to_send}"
        )