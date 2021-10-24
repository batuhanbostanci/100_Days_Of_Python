import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/**********/flightDealsCopy/prices"
class DataManager:
    def __init__(self):
        self.destination_data ={}

    def get_destination_data(self):
        sheet_endpoint = "https://api.sheety.co/***********/flightDealsCopy/prices"
        response = requests.get(url=sheet_endpoint)
        response.raise_for_status()
        sheet_data = response.json()["prices"]

        return sheet_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data ={
                "price":{
                    "iataCode": city["iataCode"]
                }
            }
            respone = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(respone.text)
