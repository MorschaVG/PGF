import requests
import os
from dotenv import load_dotenv

load_dotenv()





def get_weather_data(lat, lon, units, app_id):
    url = (f"https://api.openweathermap.org/data/2.5/weather")
    params ={"lat":lat, "lon": lon,
             "appid":app_id, "units": units}


    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Er is iets mis gegaan. Status code: {response.status_code}")

def display_weather_info(weather_data):
    city = weather_data['name']
    temp = weather_data['main']['temp']
    description = weather_data['weather'][0]['description']

    print(f"Weather in {city}:")
    print(f"Temperature: {temp}")
    print(f"Description: {description.capitalize()}")


def main():
    lat = input("Enter latitude: ").strip().lower()
    lon = input("Enter longitude: ").strip().lower()
    units = "metric"

    while not lat:
        print("Latitude cannot be empty")
    app_id = os.getenv("open_weather_key")
    data = get_weather_data(lat, lon, units, app_id)

    display_weather_info(data)

main()

# 52.377956
# 4.897070






