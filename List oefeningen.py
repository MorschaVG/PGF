# Opgave
# Maak de lijst tafel_van_drie = [3, 6, 9, 12, 16, 18, 24, 27, 32] aan. Je ziet al dat er een aantal waardes niet kloppen.
# Gebruik een toekenning om 16 in 15 te veranderen
# Gebruik de methode remove() om 32 te verwijderen
# Gebruik de methode append() om 30 toe te voegen aan het eind van de lijst
# Gebruik de methode insert() om 21 toe te voegen tussen 18 en 24
# Print de lijst. Klopt de tafel nu?

tafel_van_drie = [3, 6, 9, 12, 16, 18, 24, 27, 32]

tafel_van_drie[4] = 15
tafel_van_drie.remove(32)
tafel_van_drie.append(30)
tafel_van_drie.insert(6, 21)

print(tafel_van_drie)

