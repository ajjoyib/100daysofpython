import requests
import os
from twilio.rest import Client
# from twilio.http.http_client import TwilioHttpClient


# OPENWEATHERMAP PART
OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
api_key = os.environ.get("OWM_API_KEY")
# account_sid = "AC6e398383eecc3cc84c20658a026f08e4"
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
my_twilio_num = "+12565988812"
receiver_num = "+821057072808"
weather_params = {
    "lat": 37.34,
    "lon": 126.59,
    "exclude": "current,minutely,daily",
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {"https": os.environ["https_proxy"]}
    msg_to_send = "Take an umbrella with you."
else:
    msg_to_send = "Have a nice day."
# print(weather_data["hourly"][0]["weather"][0]["id"])


# TWILIO PART

client = Client(account_sid, auth_token)
# client = Client(account_sid, auth_token, http_client=proxy_client)

message = client.messages.create(
    from_=my_twilio_num,
    body=msg_to_send,
    to=receiver_num
)

print(message.status)