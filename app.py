from colorama import Fore, Back, Style
import requests
import time

ISS_Position_API = "http://api.open-notify.org/iss-now.json"

print("- - - - - - ISS-tracker - - - - - -")
print("[          Version: 1.0.0          ]")

while True:
    print("Current position of ISS: ", end=' => ')
    r = requests.get(url=ISS_Position_API)
    space_station_location = (r.json())
    print(f"Latitude {space_station_location['iss_position']['latitude']}", end=', ')
    print(f"Longitude {space_station_location['iss_position']['longitude']}")
    time.sleep(1)
