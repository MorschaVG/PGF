import requests
import os
from dotenv import load_dotenv

load_dotenv()





def get_weather_data(lat, lon, app_id):
    url = (f"https://api.openweathermap.org/data/3.0/onecall")
    params ={"lat":lat, "lon": lon,
             "appid":app_id}


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

    while not lat:
        print("Latitude cannot be empty")
    app_id = os.getenv("open_weather_key")
    data = get_weather_data(lat, lon, app_id)

    display_weather_info(data)

main()








