import requests
import os
from dotenv import load_dotenv
load_dotenv()

def get_rates():
    appid = os.getenv("exchange_key")
    url = (f"https://v6.exchangerate-api.com/v6/{appid}/latest/EUR")


    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Er is iets mis gegaan. Status code: {response.status_code}")
        print(response.text)


data = get_rates()

def convert_eur_to_usd(amount, exchange_rate):
    return amount * exchange_rate

def main():
    euro_amount = float(input("Voer het bedrag in Euro in: ").strip())
    exchange_rate = data["conversion_rates"]["USD"]
    usd_amount = convert_eur_to_usd(euro_amount, exchange_rate)
    print(f"{euro_amount} EUR is gelijk aan {usd_amount:.2f} USD (Wisselkoers: 1 EUR = {exchange_rate} USD)")

if __name__ == "__main__":
    main()

# 1.1626