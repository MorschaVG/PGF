# Opdracht: Set en Dictionary Analyse

# Je werkt bij een school bibliotheek en je hebt twee lijsten met gegevens over geleende boeken.
# Je moet een aantal vragen beantwoorden met behulp van sets en dictionaries.

# Gegevens:
# Je hebt twee lijsten van boeken die zijn geleend door twee verschillende groepen mensen.

# # Boeken geleend door Groep 1

# groep1 = ["Harry Potter", "De Hobbit", "De Da Vinci Code", "De Hobbit" , "De Da Vinci Code" ,
# "Twilight" , "De Vijfde Golf" , "Harry Potter", "De Hobbit"]

# # Boeken geleend door Groep 2
# groep2 = ["De Da Vinci Code", "De Alchemist", "Harry Potter", "De Hobbit", "Twilight", "The Hunger
# Games" , "Gone Girl" , "Twilight", "De Hobbit"]

# Vragen:
# 1. Unieke boeken:
#  DONE: Maak twee sets van de boeken die door Groep 1 en Groep 2 zijn geleend.
#  DONE: Print de unieke boeken voor beide groepen.
# 2. Gemeenschappelijke boeken:
#  DONE: Welke boeken zijn door beide groepen geleend? (Hint: Gebruik de doorsnede van sets)
# 3. Boeken geleend door slechts één groep:
# DONE: Welke boeken zijn alleen door Groep 1 geleend en niet door Groep 2? (Hint:
#  Gebruik het verschil van sets)
#  Welke boeken zijn alleen door Groep 2 geleend en niet door Groep 1?
# 4. Aantal geleende keren per boek:
#  DONE: Maak een dictionary voor Groep 1 waarin de boeken de sleutels zijn en de waarden het aantal keren dat elk boek is geleend.
#  DONE: Maak een soortgelijke dictionary voor Groep 2.
# 5. Meest geleende boek:
 TODO: Gebruik de dictionary van vraag 4 om te bepalen welk boek het meest is geleend door Groep 1 en welk boek door Groep 2.

# Tips:
# • Gebruik de functie set() om een set te maken.
# • Gebruik de methodes intersection() en difference() om gemeenschappelijke en
# unieke boeken te vinden.
# • Voor de dictionary kun je een for-loop gebruiken om het aantal geleende keren per boek te
# tellen.

groep1 = {"Harry Potter", "De Hobbit", "De Da Vinci Code", "De Hobbit" , "De Da Vinci Code" , "Twilight" , "De Vijfde Golf" , "Harry Potter", "De Hobbit"}

groep2 = {"De Da Vinci Code", "De Alchemist", "Harry Potter", "De Hobbit", "Twilight", "The Hunger Games" , "Gone Girl" , "Twilight", "De Hobbit"}

print(groep1)

print(groep2)

gemeenschappelijk = groep1.intersection(groep2)

print(gemeenschappelijk)

groep1_uniek = groep1 - groep2

print(groep1_uniek)

groep2_uniek = groep2 - groep1

print(groep2_uniek)

geleend1 = {"Harry Potter": 2, "De Hobbit": 2, "De Da Vinci Code": 2, "Twilight": 5, "De Vijfde Golf": 1}

geleend2 = {"Harry Potter": 1, "De Hobbit": 2, "De Da Vinci Code": 1, "Twilight": 2, "De Alchemist": 1, "The Hunger Games": 1, "Gone Girl": 1}

for boek, aantal in geleend1.items():
    print(boek, "is geleend", aantal, "keer")

meest_geleend1 = max(geleend1, key=geleend1.get)

print(meest_geleend1)






