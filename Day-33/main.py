# import requests
#
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()["iss_position"]
#
# longitude = data["longitude"]
# latitude = data["latitude"]
#
# iss_position = (longitude, latitude)
# print(iss_position)


import requests
from datetime import datetime

MY_LAT = 38.720490
MY_LONG = 35.482597

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)


time_now = datetime.now()

print(time_now.hour)