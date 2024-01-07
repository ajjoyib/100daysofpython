import smtplib

MY_EMAIL = "hamidullo287@gmail.com"

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login("MY_EMAIL", "20@lfraganuS04")
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="h.davlatov@outlook.com",
            msg=f"Subject:Happy Birthday"
        )