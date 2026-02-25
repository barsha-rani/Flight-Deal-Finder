import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = os.environ["AMADEUS_API_KEY"]
        self._api_secret = os.environ["AMADEUS_API_SECRET"]
        self._token = self._get_new_token()
        pass

    def _get_new_token(self):
        header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data  = {
            'grant_type': "client_credentials",
            'client_id': self._api_key,
            'client_secret': self._api_secret
           }
          
        response = requests.post(
                             url=os.getenv("AMADEUS_TOKEN_ENDPOINT"), 
                             data=data, 
                             headers=header
                             )
        print(f"Response Code: {response.status_code}")
        print(f"Response Text: {response.text}")

        if response.status_code == 200:
            json_response = response.json()  # Automatically parse JSON response
            token = json_response.get("access_token")
            return token
        else:
            print("Error: Failed to get the access token")
            return None
        
    # access_token = _get_new_token()  
    # print(f"Access Token: {access_token}")
    def get_iata_code(self, city):
        #This method is responsible for talking to the Flight Search API.
        header = {
            "Authorization": f"Bearer {self._token}"
        }
        flight_search_endpoint = "https://test.api.amadeus.com/v1/reference-data/locations?subType=CITY&keyword="
        try:
            # response = requests.get(url=f"{flight_search_endpoint}{city}", headers=header)

            # if response.status_code == 200:
            #     response_json = response.json()
                
            #     data = response_json.get('data', [])

            #     if data and 'iataCode' in data[0] and data[0]['iataCode']:
            #         code = data[0]['iataCode']
            #         print(f"request sent to {flight_search_endpoint}{city}\n iataCode for {city}---------> {code}")
            
                # else:
                    if city == "Tokyo": # Special case for Tokyo
                        code = "TYO"
                    if city == "Kuala Lumpur":
                        code = "KUL"
                    if city == "Frankfurt":
                        code = "FRA"  
                    if city == "Hong Kong":
                        code = "HKG"    
                    if city == "San Francisco":
                        code = "SFO"
                    if city == "New York":
                        code = "JFK"
                    if city == "Paris":
                        code = "PAR"
                    if city == "Istanbul":          
                        code = "IST"
                    if city == "Dublin":
                        code = "DUB"
                    # print(f"No IATA code found for {city}")
                    # code = f"{city[:3].upper()}"
                
            # else:
            #     print(f"Request failed with status code: {response.status_code}")
            #     if data[0] ['name'] == "Tokyo": # Special case for Tokyo
            #         code = "TYO"
            #     if data[0] ['name'] == "Kuala Lumpur":
            #         code = "KUL"
            #     if data[0] ['name'] == "Frankfurt":
            #         code = "FRA"  
            #     if data[0] ['name'] == "Hong Kong":
            #         code = "HKG"    
            #     if data[0] ['name'] == "San Francisco":
            #         code = "SFO"
            #     if data[0] ['name'] == "New York":
            #         code = "JFK"
            #     if data[0] ['name'] == "Paris":
            #         code = "PAR"
            #     if data[0] ['name'] == "Istanbul":          
            #         code = "IST"
            #     if data[0] ['name'] == "Dublin":
            #         code = "DUB"

                # print("Server error: 'iata code' Not found. Printed manually")  # Set an appropriate default or handle error as needed 
        except requests.exceptions.RequestException as e:
            print(f"Request failed with error: {e}")
            code = "Request error: 'iata code' Not found"
        except Exception as e:
            print(f"An error occurred: {e}")
            code = "Error: 'iata code' Not found"

        return code
    
    def find_cheapest_flight():
        pass
         
        
        
    