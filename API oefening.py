import requests


def get_weather_data(city_name, api_key):
    response = requests.get(url)

    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Er is iets mis gegaan. Status code: {response.status_code}")


# Juiste datumnotatie (als string), en appid als string (tussen haakjes).
date = "2025-07-14"
lat = 52.2222
lon = 4.5337
appid = "51dcab088e0a7ddf16f7c1aa9fc041e5"

url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={appid}"

r
