from colorama import Fore, Back, Style
import requests
import time

ISS_Position_API = "http://api.open-notify.org/iss-now.json"

print(Fore.GREEN)
print("\U0001f52d - - - - - - - - \U0001f6f0 ISS-tracker \U0001f4e1 - - - - - - - - \U0001fa90")
print(Fore.WHITE + "*                 Version 1.0.0                 *")
print(Style.RESET_ALL, end='')

print("")
seconds = 1
seconds = int(input("* Type the number of seconds you want to wait to update the trace: "))

while True:
    print("Current position of ISS: ", end=' => ')
    r = requests.get(url=ISS_Position_API)
    space_station_location = (r.json())
    print(f"Latitude {space_station_location['iss_position']['latitude']}", end=', ')
    print(f"Longitude {space_station_location['iss_position']['longitude']}")
    time.sleep(seconds)
