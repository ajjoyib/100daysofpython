# import requests
# from datetime import datetime
# import smtplib
# import time
#
# MY_EMAIL = "___YOUR_EMAIL_HERE____"
# MY_PASSWORD = "___YOUR_PASSWORD_HERE___"
# MY_LAT = 51.507351 # Your latitude
# MY_LONG = -0.127758 # Your longitude
#
#
# def is_iss_overhead():
#     response = requests.get(url="http://api.open-notify.org/iss-now.json")
#     response.raise_for_status()
#     data = response.json()
#
#     iss_latitude = float(data["iss_position"]["latitude"])
#     iss_longitude = float(data["iss_position"]["longitude"])
#
#     #Your position is within +5 or -5 degrees of the iss position.
#     if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
#         return True
#
#
# def is_night():
#     parameters = {
#         "lat": MY_LAT,
#         "lng": MY_LONG,
#         "formatted": 0,
#     }
#     response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
#     response.raise_for_status()
#     data = response.json()
#     sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
#     sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
#
#     time_now = datetime.now().hour
#
#     if time_now >= sunset or time_now <= sunrise:
#         return True
#
#
# while True:
#     time.sleep(60)
#     if is_iss_overhead() and is_night():
#         connection = smtplib.SMTP("__YOUR_SMTP_ADDRESS_HERE___")
#         connection.starttls()
#         connection.login(MY_EMAIL, MY_PASSWORD)
#         connection.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs=MY_EMAIL,
#             msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
#         )
#
#

from tkinter import *

def get_quote():
    pass
    # write your code here


window = Tk()
window.title("Kanye says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="kanye_quotes/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye quote goes here", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye_quotes/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)


window.mainloop()