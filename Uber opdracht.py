# Opdracht: Uber applicatie met functies

# Doel:
# Je maakt een applicatie waarin gebruikers van een gebruik kunnen maken van hun Uber dienst
# via de commandline.

# Gegevens:
# De gebruikers kunnen kiezen uit 3 verschillende diensten met elk een eigen prijs. Zorg dat deze
# diensten in een logische collectie in je applicatie staan.

# De diensten zijn:
# "Uber Black": 2.00,
# "Uber Van": 3.50,
# "Uber X": 1.50

# Opdracht:
# Zorg dat de applicatie de volgende flow heeft:
# - De gebruiker kan kiezen uit 1 van de drie diensten
# - De gebruiker kan aangeven hoeveel kilometer gereden moet worden
# - De applicatie berekend de totale kosten
# - De gebruiker krijgt te zien hoeveel de rit gaat kosten

# Voorbeeld output:
# Een voorbeeld van een output, maar voel je vrij om hier creatief mee om te gaan:
# Kies het type Uber:
# 1. Uber Black
# 2. Uber Van
# 3. Uber X
# ---------------
# Voer het nummer van uw keuze in: 1
# Voer het aantal kilometers van uw rit in: 32

# U heeft gekozen voor Uber Black. De kosten voor uw rit van 32 kilometer(s) zijn €64.00.

# Tips:
# - Schrijf eerst je idee in pseudocode uit (in commentaar) en schrijf daarna de echte code.
# - Gebruik logische functienamen, zoals “get_user_choice” en “calculate_cost”
# - Gebruik dictionary waar dat gepast is
# - Gebruik een while-loop voor input validatie
# - Zorg dat je applicatie prettig te gebruiken is. Denk aan UX (User Experience).
# - Zorg er ook voor dat je code aan DRY criteria voldoet en je code goed leesbaar is.
# - Test met verschillende invoer (ook onzinnige invoer)

"""Uber ritprijs calculator

Deze applicatie laat de gebruiker een uber type kiezen, vraagt vervolgens het aantal kilometers op en berekent vervolgens
de ritprijs"""

# Dictionary met Uber-types en hun prijs per kilometer
uber_type = {"Black": 2.00, "Van": 3.50, "X": 1.50}

# Lijst van Uber-types op volgorde om input aan index te koppelen
typekeuze_list = list(uber_type.keys()) #Black, Van, X

# Input: keuze voor type Uber
keuze = input("van welk Uber dienst wilt u gebruik maken?"
                  "\n1: Uber Black"
                  "\n2: Uber Van"
                  "\n3: Uber X"
                  "\nvoer uw keuze in:")

# Validatie: alleen 1, 2 of 3 zijn toegestaan
while keuze not in ['1', '2', '3']:
    print("ongeldige keuze, probeer opnieuw.")
    keuze = input("van welke Uber dienst wilt u gebruik maken?"
                      "\n1: Uber Black"
                      "\n2: Uber Van"
                      "\n3: Uber X"
                      "\nvoer uw keuze in:")

# Input: afstand in kilometers
aantal_km = int(input("Voer het aantal kilometers van uw rit in: "))

# Bepaal het gekozen type en de bijbehorende prijs
type_keuze = typekeuze_list[int(keuze) -1]
prijs_per_km = uber_type[type_keuze]
totaal_prijs = aantal_km * prijs_per_km

# Output: bevestiging + ritpijs als integer
print(f"U heeft gekozen voor Uber {type_keuze}. Uw rit kost {totaal_prijs} euro")

# Optie om de keuze nog aan te passen
input("Wilt u uw keuze nog aanpassen?"
      "\nJ/N")








