import os

import requests
from dotenv import load_dotenv

load_dotenv()


def get_movie_data(title):
    """
    Haalt filminformatie op via de OMDb API op basis van een titel.

    Gebruikt de OMDb API-sleutel uit de .env file.
    Retourneert een dictionary met filmgegevens of None bij een fout of niet-gevonden film.
    """
    appid = os.getenv("openmovie_key")
    url = "http://www.omdbapi.com/"
    params = {"t": title, "apikey": appid}

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data["Response"] == "True":
            return data
        else:
            print("Film niet gevonden")
    else:
        print(f"Fout bij invoer: {response.status_code}")
    return None


def toon_jaartal(data):
    """
    Print het releasejaar van de film en biedt de optie om topfilms uit dat jaar te bekijken.

    Retourneert True als de gebruiker kiest om topfilms te bekijken (wat leidt tot een submenu), anders False.
    """
    jaar = data["Year"]
    print(f"\n{data['Title']} kwam uit in {jaar}.")

    keuze = input(f"\nWil je topfilms uit {jaar} bekijken? (j/n): ").strip().lower()
    if keuze == "j":
        topfilms_submenu(int(jaar))
        return True
    return False


def toon_regisseur(data):
    """Toont de regisseur van de opgezochte film."""
    print(f"De regisseur van {data['Title']} is {data['Director']}.")


def check_oscar(data):
    """Controleert of de film een Oscar heeft gewonnen op basis van de 'Awards'-informatie."""
    awards = data.get("Awards", "")
    if "oscar" in awards.lower():
        print(f"{data['Title']} heeft een Oscar gewonnen!")
    else:
        print(f"{data['Title']} heeft geen Oscar gewonnen.")


def get_tmdb_movie_id(title):
    """
    Zoekt de TMDb ID van een film op basis van de titel.

    Deze ID is nodig om aanvullende gegevens zoals schrijvers op te halen via TMDb.
    """
    api_key = os.getenv("tmdb_key")
    url = "https://api.themoviedb.org/3/search/movie"
    params = {"api_key": api_key, "query": title, "language": "nl-NL"}

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        results = data.get("results", [])
        if results:
            return results[0]["id"]
    return None


def get_movie_writers(movie_id):
    """
    Haalt een lijst met schrijvers op van een film via TMDb API.

    Wordt gebruikt om te controleren of een film gebaseerd is op een boek.
    """
    api_key = os.getenv("tmdb_key")
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    params = {"api_key": api_key, "language": "nl-NL"}

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        relevante_jobs = {"Writer", "Screenplay", "Author", "Story", "Novel"}
        writers = [crew_member["name"] for crew_member in data.get("crew", []) if crew_member["job"] in relevante_jobs]
        return writers
    else:
        print(f"Fout bij ophalen schrijvers: {response.status_code}")
        return []


def check_boekversie(title, movie_writers, filmjaar):
    """
    Controleert of er een boek bestaat waarop de film gebaseerd zou kunnen zijn.

    Zoekt op OpenLibrary naar boeken met dezelfde titel.
    Vergelijkt de auteurs en publicatiejaren met de filmgegevens.
    Retourneert het eerste passende boek of None.
    """
    url = "https://openlibrary.org/search.json"
    params = {"title": title}

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        docs = data.get("docs", [])

        for boek in docs[:10]:
            boek_auteurs = boek.get("author_name", [])
            publicatiejaar = boek.get("first_publish_year", 9999)

            ouder_dan_film = publicatiejaar < filmjaar
            auteur_match = any(
                any(writer.lower() in auteur.lower() or auteur.lower() in writer.lower()
                    for writer in movie_writers)
                for auteur in boek_auteurs
            )

            if ouder_dan_film and auteur_match:
                return boek

        return None

    else:
        print(f"Fout bij checken van gegevens: {response.status_code}")
        return None


def get_google_books_rating(title):
    """
    Haalt de beoordeling van een boek op via Google Books API.

    Wordt gebruikt als fallback als OpenLibrary geen rating heeft.
    Retourneert een tuple met gemiddelde beoordeling en aantal beoordelingen.
    """
    url = "https://www.googleapis.com/books/v1/volumes"
    params = {
        "q": title,
        "maxResults": 5,
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        items = data.get("items", [])
        for item in items:
            volume_info = item.get("volumeInfo", {})
            rating = volume_info.get("averageRating")
            ratings_count = volume_info.get("ratingsCount", 0)
            if rating:
                return rating, ratings_count
    return None, 0


def vergelijk_boek_en_film(film_data, boek_data):
    """
    Vergelijkt de beoordeling van een film (IMDb) met die van een boek (OpenLibrary of Google Books).

    Print een conclusie: is het boek beter, de film beter, of zijn ze even goed?
    """
    film_rating = float(film_data.get("imdbRating", 0))
    film_titel = film_data.get("Title")

    boek_key = boek_data.get("key")
    boek_rating = None

    if boek_key:
        ratings_url = f"https://openlibrary.org{boek_key}/ratings.json"
        ratings_response = requests.get(ratings_url)
        if ratings_response.status_code == 200:
            ratings_data = ratings_response.json()
            boek_rating = ratings_data.get("average")

    if not boek_rating:
        boek_title = boek_data.get("title") or film_titel
        google_rating, count = get_google_books_rating(boek_title)
        if google_rating:
            boek_rating = google_rating
        else:
            print("Er is geen beoordeling voor het boek beschikbaar. Ga er maar vanuit dat het boek beter is..")
            return

    if film_rating > boek_rating * 2:
        print("\nSorry, de film is beter dan het boek.")
    elif film_rating < boek_rating * 2:
        print("\nJa, het boek is beter dan de film. Je kan nu díe persoon zijn op een feestje.")
    else:
        print("\nHet boek en de film zijn even goed. Laat het los.")


def toon_boekinfo(boek):
    """
    Print titel, auteur(s) en publicatiejaar van een gevonden boek.
    """
    titel = boek.get("title") or boek.get("title_suggest", "Onbekende titel")
    auteurs = ", ".join(boek.get("author_name", ["Onbekende auteur"]))
    jaar = boek.get("first_publish_year", "Onbekend jaar")
    print(f"Ja! Dit boek is een verfilming van: {titel} door {auteurs} (gepubliceerd in {jaar})")


def toon_topfilms_uit_jaar(jaar):
    """
    Haalt via TMDb API de top 10 populairste films uit dat jaar op.

    Retourneert een lijst van film dictionaries.
    """
    api_key = os.getenv("tmdb_key")
    url = "https://api.themoviedb.org/3/discover/movie"
    params = {
        "api_key": api_key,
        "primary_release_year": jaar,
        "sort_by": "popularity.desc",
        "language": "nl-NL",
        "page": 1
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    films = response.json().get("results", [])
    return films[:10]  # return top 10


def topfilms_submenu(jaar):
    """
    Toont een submenu met topfilms uit een gekozen jaar.

    De gebruiker kan een film kiezen om er meer over te weten, of terugkeren.
    """
    films = toon_topfilms_uit_jaar(jaar)
    if not films:
        print(f"Geen films gevonden voor {jaar}.")
        return

    print(f"\nTop films uit {jaar}:")
    for i, film in enumerate(films, start=1):
        print(f"{i}. {film['title']}")

    prompt = (
        "\nKies het nummer van één van deze films als je daar meer over wilt weten\n"
        "of kies 0 als je terug wilt naar het vorige menu: "
    )
    keuze = input(prompt).strip()

    if keuze.isdigit():
        idx = int(keuze)
        if idx == 0:
            return
        if 1 <= idx <= len(films):
            return film_submenu(films[idx - 1]['title'])
        else:
            print("Nummer buiten bereik. Kies 1–10 of 0 om terug te gaan.")
    else:
        print("Voer een geldig cijfer in (0–10).")


def film_submenu(title=None):
    """
    Toont een submenu voor een specifieke film.

    Biedt keuzes voor: jaar, regisseur, Oscar, boekversie, of terug naar hoofdmenu.
    """
    if not title:
        title = input("\nVoer de titel van een film in: ")
    data = get_movie_data(title)
    if not data:
        return

    while True:
        print(f"\nWat wil je weten over '{title}'?")
        print("\n1. In welk jaar kwam de film uit?")
        print("2. Wie was de regisseur?")
        print("3. Heeft deze film een Oscar gewonnen?")
        print("4. Is deze film gebaseerd op een boek?")
        print("5. Terug naar hoofdmenu")

        keuze = input("\nMaak je keuze: ")

        if keuze == "1":
            gestopt = toon_jaartal(data)
            if gestopt:
                return
        elif keuze == "2":
            toon_regisseur(data)
        elif keuze == "3":
            check_oscar(data)
        elif keuze == "4":
            movie_id = get_tmdb_movie_id(title)
            if not movie_id:
                print("Fout bij ophalen gegevens.")
                continue

            movie_writers = get_movie_writers(movie_id)
            if not movie_writers:
                print("Fout bij ophalen gegevens.")
                continue

            try:
                filmjaar = int(data["Year"])
            except ValueError:
                print("Fout bij ophalen gegevens.")
                continue

            boek_data = check_boekversie(title, movie_writers, filmjaar)
            if boek_data:
                toon_boekinfo(boek_data)
                wil_vergelijken = input("\nWil je weten of het boek beter is dan de film? (j/n): ").strip().lower()
                if wil_vergelijken == "j":
                    vergelijk_boek_en_film(data, boek_data)
            else:
                print("Deze film is niet gebaseerd op een boek. (of we kunnen het boek niet vinden)")

        elif keuze == "5":
            return
        else:
            print("Ongeldige keuze.")
            continue

        # Na uitvoeren van een functie, vraag of de gebruiker verder wil
        vervolg = input("\nWil je nog meer weten over deze film? (j/n): ").strip().lower()
        if vervolg != "j":
            return


def main_menu():
    """
    Hoofdmenu van de applicatie. Geeft toegang tot filmzoekfunctie of afsluiten.
    """
    while True:
        print("\nWelkom bij Morscha's Mini Film Database / Is-het-boek-beter-calculator!")
        print("1. Zoek een film")
        print("2. Sluit af")

        keuze = input("Maak je keuze: ")
        if keuze == "1":
            film_submenu()
        elif keuze == "2":
            print("\nTot de volgende keer!")
            break
        else:
            print("Ongeldige keuze.")

    main_menu()
