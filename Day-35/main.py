import requests
import os
from twilio.rest import Client

API_KEYS = "*******************"  # This is unique coming from api
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

account_sid = os.environ['*******************']  # This is unique coming from api
auth_token = os.environ['*******************']  # This is unique coming from api

parameters = {
    "lat": "38.356869",
    "lon": "38.309669",
    "exclude": "current,minutely,daily",
    "appid": API_KEYS
}

response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()

weather_data = response.json()["hourly"][:12]

will_rain = False
for hour_data in weather_data:
    weather_condition = hour_data["weather"][0]["id"]

    if int(weather_condition) < 700:
        will_rain = True


if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="+15558675309",
        from_="+15017250604",
        body="It's  going to rain today. Don't forget your umbrella")