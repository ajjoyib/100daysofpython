##################### Extra Hard Starting Project ######################
import pandas as pd
import smtplib
import datetime as dt
import random

MY_EMAIL = "hamidullo287@gmail.com"
MY_PASSWORD = "klmtgjxwwuverjcz"

now = dt.datetime.now()
current_month = now.month
current_day = now.day
df = pd.read_csv("birthdays.csv")


for index, row in df.iterrows():
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt", "r") as letter_file:
        letter_to_send = letter_file.read().replace("[NAME]", row["name"])
    if row['month'] == current_month and row['day'] == current_day:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=row["email"],
                msg=f"Subject:Happy Birthday\n\n{letter_to_send}"
            )


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




