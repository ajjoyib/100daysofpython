import time

import requests
import datetime as dt
import smtplib

MY_LAT = 37.456257
MY_LNG = 126.705208
MY_EMAIL = "hamidullo287@gmail.com"
MY_PASSWORD = "20@lfraganuS04"



# your position is within +5 or -5 degrees of the ISS position
def is_iss_above():
    response01 = requests.get(url="http://api.open-notify.org/iss-now.json")
    response01.raise_for_status()
    data = response01.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LNG-5 <= iss_longitude <= MY_LNG+5:
        return True
    else: return False

def is_night():
    parameters = {
        "lat": MY_LAT,
        "long": MY_LNG,
        "formatted": 0,
    }

    response02 = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response02.raise_for_status()
    data = response02.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    now = dt.datetime.now().hour

    if now > sunset or now < sunrise:
        return True
    else: return False

while True:
    time.sleep(60)
    if is_iss_above() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up\n\nThe ISS is above you in the sky."
        )


