#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
import json
import requests
import os
from dotenv import load_dotenv
load_dotenv()

data_manager = DataManager()

# sheet_data = data_manager.get_sheety_data()
# print(sheet_data)


sheet_raw_data = {'price': [{'city': 'Paris', 'iataCode': '', 'lowestPrice': 54, 'id': 2}, {'city': 'Frankfurt', 'iataCode': '', 'lowestPrice': 42, 'id': 3}, {'city': 'Tokyo', 'iataCode': '', 'lowestPrice': 485, 'id': 4}, {'city': 'Hong Kong', 'iataCode': '', 'lowestPrice': 551, 'id': 5}, {'city': 'Istanbul', 'iataCode': '', 'lowestPrice': 95, 'id': 6}, {'city': 'Kuala Lumpur', 'iataCode': '', 'lowestPrice': 414, 'id': 7}, {'city': 'New York', 'iataCode': '', 'lowestPrice': 240, 'id': 8}, {'city': 'San Francisco', 'iataCode': '', 'lowestPrice': 260, 'id': 9}, {'city': 'Dublin', 'iataCode': '', 'lowestPrice': 378, 'id': 10}]}
sheet_data = json.loads(json.dumps(sheet_raw_data))
print(sheet_data)

if sheet_data["price"][0]["iataCode"] == "":  # if iataCode is empty
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for key in sheet_data["price"]:
        key["iataCode"] = flight_search.get_iata_code(key["city"])
    print(f"sheet_data: \n {sheet_data}")    

    # data_manager.destination_data = sheet_data
    # data_manager.update_iata_code()





