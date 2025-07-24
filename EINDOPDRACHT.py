import os

import requests
from dotenv import load_dotenv

load_dotenv()


def get_movie_data(title):
    appid = os.getenv("openmovie_key")
    url = (f"http://www.omdbapi.com/")
    params ={"t":title, "apikey":appid}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Er is iets mis gegaan. Status code: {response.status_code}")
    print(response.text)

filmdata = get_movie_data("Jurassic Park")
print(filmdata)




# {'Title': 'Jurassic Park', 'Year': '1993', 'Rated': 'PG-13', 'Released': '11 Jun 1993', 'Runtime': '127 min', 'Genre': 'Action, Adventure, Sci-Fi', 'Director': 'Steven Spielberg', 'Writer': 'Michael Crichton, David Koepp', 'Actors': 'Sam Neill, Laura Dern, Jeff Goldblum', 'Plot': "An industrialist invites some experts to visit his theme park of cloned dinosaurs. After a power failure, the creatures run loose, putting everyone's lives, including his grandchildren's, in danger.", 'Language': 'English, Spanish', 'Country': 'United States', 'Awards': 'Won 3 Oscars. 44 wins & 27 nominations total', 'Poster': 'https://m.media-amazon.com/images/M/MV5BMjM2MDgxMDg0Nl5BMl5BanBnXkFtZTgwNTM2OTM5NDE@._V1_SX300.jpg', 'Ratings': [{'Source': 'Internet Movie Database', 'Value': '8.2/10'}, {'Source': 'Rotten Tomatoes', 'Value': '91%'}, {'Source': 'Metacritic', 'Value': '68/100'}], 'Metascore': '68', 'imdbRating': '8.2', 'imdbVotes': '1,130,773', 'imdbID': 'tt0107290', 'Type': 'movie', 'DVD': 'N/A', 'BoxOffice': '$407,185,075', 'Production': 'N/A', 'Website': 'N/A', 'Response': 'True'}

