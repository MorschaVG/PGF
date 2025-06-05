# Schrijf een programma dat een gebruiker om een wachtwoord vraagt.
# De gebruiker heeft maximaal 3 pogingen om het juiste wachtwoord in te voeren.
# Als het juiste wachtwoord is ingevoerd, print je een succesbericht en beëindig je de loop.
# Als de gebruiker 3 pogingen fout invoert, geef je een bericht dat de toegang is geweigerd.
#
# Stappenplan:
#
# 1. Stel een vast wachtwoord in (bijvoorbeeld: "python123"), door daar een variabele voor te maken.
# 2. Vraag de gebruiker om het wachtwoord in te voeren.
# 3. Gebruik een while-loop om de gebruiker maximaal 3 kansen te geven om het juiste wachtwoord in te voeren.
# 4. Als de gebruiker het juiste wachtwoord invoert, beëindig dan de loop met een succesbericht.
# 5. Als de gebruiker na 3 pogingen nog steeds het verkeerde wachtwoord invoert, geef een foutmelding.



# correct_password = "python123"
# attempts = 0
# max_attempts = 3
#
# while attempts < max_attempts:
#     user_input = input("Voer het wachtwoord in: ")
#     if user_input == correct_password:
#         print("Toegang verleend")
#         break
#     else:
#         attempts += 1
#         print(f"Onjuist wachtwoord. Poging {attempts} / {max_attempts}")
# if attempts == max_attempts:
#     print("Toegang geweigerd")

# =================================================================================================

# In deze opdracht ga je een script schrijven waarbij de gebruiker een geheim getal moet raden.
#
# Stappenplan:
#
# 1. Maak een variable "random_getal" en geef deze een willekeurige integer waarde tussen 1 en 10.
# 2. Vraag de gebruiker om het getal te raden
# 3. Gebruik een while-loop die blijft draaien zolang de gebruiker het verkeerde getal raadt.
# 4. Geef feedback of de ingevoerde waarde te hoog of te laag is.
# 5. Wanneer de gebruiker het juiste getal raadt, beëindig de loop en print een felicitatiebericht.
#
# BONUS: Gebruik `import random` en `random.randomInt(1, 10)` om je geheime getal mee te maken
# en deze zo ook voor jezelf geheim te houden.

# random_getal = 7
# user_guess = None
#
# while user_guess != random_getal:
#     user_guess = int(input("Raad een getal tussen 1 en 10: "))
#     if user_guess == random_getal:
#         print("Bingo!")
#         break
#     else:
#         print("Helaas, nog een poging: ")

# import  random
#
# random_getal = random.randint(1, 10)
# user_guess = None
#
# while user_guess != random_getal:
#     user_guess = int(input("Raad een getal tussen 1 en 10: "))
#     if user_guess == random_getal:
#         print("Bingo!")
#         break
#     else:
#         print("Helaas, nog een poging: ")

# Schrijf een programma voor kassa medewerkers waarin je een bedrag (in centen) invoert, bijvoorbeeld 87 cent,
# en het programma geeft terug hoeveel munten van 50, 20, 10, 5, en 1 cent je terug zou moeten geven.
# Het programma gebruikt een while-loop om de berekening stap voor stap uit te voeren,
# telkens de grootste munt eraf halend totdat het bedrag nul is.
#
# Stappenplan:
#
# 1. Vraag de gebruiker om een bedrag in centen in te voeren (bijvoorbeeld 87).
#       (Bonus: check of de gebruiker niet meer dan 100 invoert)
# 2. Gebruik een while-loop om telkens de grootste muntwaarde van het bedrag af te trekken.
#    De loop stopt wanneer het bedrag nul is.
# 3. Maak in de while-loop, voor elke munt waarde een (nested) if-statement, waarin je het volgende doet:
#       - Bereken hoevaak die muntwaarde in het bedrag past.
#       - Trek zo vaak de muntwaarde van het bedrag af,
#         zodat de volgende iteratie van de while-loop het aangepast bedrag gebruikt
#       - Print hoeveel munten van deze waarde de gebruiker terug moet krijgen.
#
# Bonus: Breid het programma uit, zodat het ook briefgeld en euro munten kan teruggeven.

# De beschikbare muntwaarden

vijftig_cent = 50
twintig_cent = 20
tien_cent = 10
vijf_cent = 5
een_cent = 1

bedrag_invoer = int(input("Voer het bedrag in centen in: "))

while bedrag_invoer > 0:
    if bedrag_invoer >= vijftig_cent:
        aantal_vijftig = bedrag_invoer // vijftig_cent
        bedrag_invoer -= aantal_vijftig * vijftig_cent
        print(f"{aantal_vijftig} x 50 cent munt")

    elif bedrag_invoer >= twintig_cent:
        aantal_twintig = bedrag_invoer // twintig_cent
        bedrag_invoer -= aantal_twintig * twintig_cent
        print(f"{aantal_twintig} x 20 cent munt")

    elif bedrag_invoer >= tien_cent:
        aantal_ttien = bedrag_invoer // tien_cent
        bedrag_invoer -= aantal_ttien * tien_cent
        print(f"{aantal_ttien} x 10 cent munt")

    elif bedrag_invoer >= vijf_cent:
        aantal_vijf = bedrag_invoer // vijf_cent
        bedrag_invoer -= aantal_vijf * vijf_cent
        print(f"{aantal_vijf} x 5 cent munt")

    else:
        aantal_een = bedrag_invoer // een_cent
        bedrag_invoer -= aantal_een * een_cent
        print(f"{aantal_een} x een cent munt")