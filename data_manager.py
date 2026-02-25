import requests
import json
from requests.auth import HTTPBasicAuth
import os
from dotenv import load_dotenv

load_dotenv()

SHEETY_PRICE_ENDPOINT = "https://api.sheety.co/7c9263a3629b0286bce18365ae6a74c8/copyOfFlightDeals/price"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self._user = os.environ["SHEETY_USERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        print(self._user)
        print(self._password)
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}
        
    def get_sheety_data(self):
        response = requests.get(url=SHEETY_PRICE_ENDPOINT, auth=self._authorization)
        data = response.json()
        # self.destination_data = data["price"]
        # return self.destination_data
        return data
    

    def update_iata_code(self):
        print("self_destination_data: ", self.destination_data)
        json_price = self.destination_data["price"]
        print(json_price)
        for key in json_price:
            json_body = {
                "price": {
                    "iataCode": key["iataCode"]
                    }
                }
            response = requests.put(url=f"{SHEETY_PRICE_ENDPOINT}/{key['id']}", json=json_body, auth=self._authorization)
            print(response.text) 
            # print(f"IATA Codes Updated ----->\n{json_body}")