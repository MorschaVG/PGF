import os

import requests
from dotenv import load_dotenv

load_dotenv()

def toon_topfilms(jaar):
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

        print(f"Top films uit {jaar}:")
        for film in films[:10]:  # toon de top 10
            print(f"- {film['title']} (Score: {film['vote_average']})")
    else:
        print(f"Fout bij ophalen topfilms: {response.status_code}")

