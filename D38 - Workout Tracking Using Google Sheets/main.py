import requests
from datetime import datetime
import os

GENDER = "male"
WEIGHT_KG = 60
HEIGHT_CM = 175
AGE = 19

SHEETY_USERNAME = "hamidullodavlatov"
SHEETY_PW = "alfraganus"

APP_ID = os.environ["e916811e"]
APP_KEY = os.environ["47446b3b7174c73cf866c1749d535f43"]

exercise_endpoint = " https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = os.environ["https://api.sheety.co/d45ab8d550391468d565f712a3aca97c/workoutTracking/workouts"]

exercise_text = input("Tell me which exercise you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight": WEIGHT_KG,
    "height": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json


############################ Start of Step 4 Solution ############################

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercise"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(
        sheety_endpoint, 
        json=sheet_inputs,
        auth={
            SHEETY_USERNAME,
            SHEETY_PW,
        }
        )

    print(sheet_response.text)