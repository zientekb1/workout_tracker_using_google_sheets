import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = "68.04"
HEIGHT_CM = "182.88"
AGE = "23"

NUTRITIONIX_ID = "5e4241e1"   # nutritionix site account id
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
NUTRITIONIX_API = ""
SHEETY_ENDPOINT = ""    # sheety api
BEARER_AUTH = ""    # authentication for sheety

exercise_text = input("What exercise did you do today?: ")

nutritionix_parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

nutritionix_headers = {
    "x-app-id": NUTRITIONIX_ID,
    "x-app-key": NUTRITIONIX_API,
}

response = requests.post(url=NUTRITIONIX_ENDPOINT, headers=nutritionix_headers, json=nutritionix_parameters)
result = response.json()

current_date = datetime.now().strftime("%d/%m/%Y")
current_time = datetime.now().strftime("%I:%M%p")

sheety_headers = {
    "Authorization": f"Bearer {BEARER_AUTH}"
}

for exercise in result["exercises"]:
    sheety_parameters = {
        "workout": {
            "date": current_date,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": f"{exercise['duration_min']} min",
            "calories": exercise["nf_calories"]
        }
    }

    response2 = requests.post(url=SHEETY_ENDPOINT, json=sheety_parameters, headers=sheety_headers)
    print(response2.text)
