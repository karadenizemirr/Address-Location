import pandas as pd
import time
import json
from geopy.geocoders import Nominatim
from gui import consoleProgressBar

class Core:
    def __init__(self,filepath) -> None:
        self.data = pd.read_csv(filepath)

    def get_location(self):
        result = []
        print('process is starting')
        for index,row in self.data.iterrows():
            address = f"{row['address_1']},{row['city']},{row['state_province']}"
            
            # Get Coordinates
            geolocator = Nominatim(user_agent = "my-app")
            location = geolocator.geocode(address)

            if location is not None:
                result_dict = {
                    "latitude": location.latitude,
                    "longitude": location.longitude
                }
                result.append(result_dict)
                #print('Success Coordinates', end=' ', flush=True)
            else:
                #print("Coordinates none", end=' ', flush=True)
                result.append({
                    "latitude": None,
                    "longitude": None
                })
        json_data = json.loads(json.dumps(result))
        df_to_json = pd.json_normalize(json_data)
        consoleProgressBar.consoleProgressBar()
        return df_to_json