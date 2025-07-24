import os
import requests
from dotenv import load_dotenv

load_dotenv()


def get_movie_data(title):
    """Haalt filminformatie op via de OMDb API."""
    appid = os.getenv("openmovie_key")
    url = "http://www.omdbapi.com/"
    params = {"t": title, "apikey": appid}

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data["Response"] == "True":
            return data
        else:
            print(f"Film niet gevonden: {title}")
    else:
        print(f"Fout bij aanvraag: {response.status_code}")
    return None


def toon_jaartal(data):
    jaar = data["Year"]
    print(f"{data['Title']} kwam uit in {jaar}.")

    keuze = input(f"Wil je topfilms uit {jaar} bekijken? (j/n): ").strip().lower()
    if keuze == "j":
        toon_topfilms_uit_jaar(int(jaar))


def toon_regisseur(data):
    print(f"De regisseur van {data['Title']} is {data['Director']}.")


def check_oscar(data):
    awards = data.get("Awards", "")
    if "oscar" in awards.lower():
        print(f"{data['Title']} heeft een Oscar gewonnen!")
    else:
        print(f"{data['Title']} heeft geen Oscar gewonnen.")


def check_boekversie(data):
    print("Deze functie zou via een tweede API checken of er een boek is... (nog in ontwikkeling).")


def vergelijk_boek_en_film(data):
    print("Deze functie vergelijkt scores (bijv. van Open Library of Goodreads)... (nog in ontwikkeling).")


def toon_topfilms_uit_jaar(jaar):
    api_key = os.getenv("tmdb_key")
    url = "https://api.themoviedb.org/3/discover/movie"
    params = {
        "api_key": api_key,
        "primary_release_year": jaar,
        "sort_by": "popularity.desc",  # Sorteer op populariteit
        "language": "nl-NL",
        "page": 1
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        films = data.get("results", [])
        if not films:
            print(f"Geen films gevonden voor het jaar {jaar}.")
            return

        print(f"\nTop films uit {jaar}:")
        for film in films[:10]:  # toon de top 10
            print(f"- {film['title']}")
    else:
        print(f"Fout bij ophalen topfilms: {response.status_code}")


def film_submenu():
    title = input("Voer de titel van een film in: ")
    data = get_movie_data(title)
    if not data:
        return

    while True:
        print(f"\nWat wil je weten over '{title}'?")
        print("1. In welk jaar kwam de film uit?")
        print("2. Wie was de regisseur?")
        print("3. Heeft deze film een Oscar gewonnen?")
        print("4. Is er een boek van deze film?")
        print("5. Is het boek beter??")
        print("6. Terug naar hoofdmenu")

        keuze = input(">> ")

        if keuze == "1":
            toon_jaartal(data)
        elif keuze == "2":
            toon_regisseur(data)
        elif keuze == "3":
            check_oscar(data)
        elif keuze == "4":
            check_boekversie(data)
        elif keuze == "5":
            vergelijk_boek_en_film(data)
        elif keuze == "6":
            break
        else:
            print("Ongeldige keuze.")
            continue

        # Na uitvoeren van een functie, vraag of de gebruiker verder wil
        vervolg = input("\nWil je nog meer weten over deze film? (j/n): ").strip().lower()
        if vervolg != "j":
            break


def main_menu():
    while True:
        print("\nWelkom bij Morscha's Mini Film Database / Is-het-boek-beter-calculator!")
        print("1. Zoek een film")
        print("2. Sluit af")

        keuze = input("Maak je keuze: ")
        if keuze == "1":
            film_submenu()
        elif keuze == "2":
            print("Tot de volgende keer!")
            break
        else:
            print("Ongeldige keuze.")


if __name__ == "__main__":

    main_menu()

