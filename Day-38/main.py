import requests
from datetime import datetime

APP_ID = "**********"
API_KEY = "**********"

GENDER = "male"
WEIGHT_KG = "119"
HEIGHT_CM = "184"
AGE = "23"

sheet_endpoint = "https://api.sheety.co/***********/myWorkoutsCopy/workouts"

headers_nutritionix = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

query = input("Which exercise did you do today?")

exercise_parameters = {
    "query": query,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": WEIGHT_KG,
    "age": AGE
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
response = requests.post(url=exercise_endpoint, json=exercise_parameters, headers=headers_nutritionix)
return_result = response.json()


now = datetime.now()

for exercise in return_result["exercises"]:
    sheety_body = {
        "workout": {
            "date": now.strftime("%Y/%m/%d"),
            "time": now.strftime("%H:%M:%S"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories":  exercise["nf_calories"]
        }
    }

    # without auth
    # exercise_response = requests.post(url=sheet_endpoint, json=sheety_body)

    # with auth

    exercise_response = requests.post(url=sheet_endpoint, json=sheety_body, auth=("**********", "**********"))




