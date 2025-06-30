"""Uber ritprijs calculator met voorkeur en geschiedenis"""

# Dictionary met Uber types en prijs per km
uber_prijzen = {
    "Uber Black": 2.00,
    "Uber Van": 3.50,
    "Uber X": 1.50
}
USER = {
    "preference": "",   #bijv. "Uber Black"
    "history": []       #lijst met ritbeschrijvingen
}
def toon_menu_opties():
    """toont automatisch het uber dienst menu en retourneert de lijst van diensten"""
    print("Kies het type Uber")
    for nummer, dienst in enumerate(uber_prijzen.keys(), start=1):
        print(f"{nummer}. {dienst}")
    return list(uber_prijzen.keys())

def kies_dienst():
    """vraagt de gebruiker om een dienst te kiezen via nummer"""
    diensten_lijst = toon_menu_opties()
    keuze = input("Voer het nummer van uw keuze in: ")
    while keuze not in [str(i) for i in range(1, len(diensten_lijst) +1)]:
        print("Ongeldige keuze, probeer opnieuw.")
        keuze = input("Voer het nummer van uw keuze in: ")
    return diensten_lijst[int(keuze) -1]

def boek_rit():
    """laat gebruiker een rit boeken, met optie voor voorkeursdienst"""
    if USER["preference"]:
        while True:
            gebruik_voorkeur = input(f"Uw voorkeursdienst is {USER['preference']}. Wilt u deze gebruiken? j/n").lower()
            if gebruik_voorkeur == "j":
                gekozen_uber = USER["preference"]
                break
            elif gebruik_voorkeur == "n":
                gekozen_uber = kies_dienst()
                break
            else:
                print("Ongeldige invoer. Typ 'j' voor ja of 'n' voor nee.")
    else:
        gekozen_uber = kies_dienst()

    try:
        aantal_km = int(input("Voer het aantal kilometers van uw rit in: "))
    except ValueError:
        print("Ongeldige invoer, rit geannuleerd.")
        return

    prijs_per_km = uber_prijzen[gekozen_uber]
    totaal_prijs = aantal_km * prijs_per_km

    print(f"U heeft gekozen voor {gekozen_uber}. Uw rit van {aantal_km} km kost {int(totaal_prijs)} euro.")
    USER["history"].append(f"{aantal_km} km met {gekozen_uber} voor €{int(totaal_prijs)}")


def toon_geschiedenis():
    """Toon de ritgeschiedenis van de gebruiker."""
    print("Ritgeschiedenis:")
    if not USER["history"]:
        print("Nog geen ritten geboekt.")
    else:
        for i, rit in enumerate(USER["history"], start=1):
            print(f"{i}. {rit}")

def wijzig_voorkeur():
    """Laat gebruiker een nieuwe voorkeursdienst kiezen."""
    nieuwe_voorkeur = kies_dienst()
    USER["preference"] = nieuwe_voorkeur
    print(f"Voorkeursdienst ingesteld op: {nieuwe_voorkeur}")

while True:
    print("\n--- Hoofdmenu ---")
    print("1: Boek een rit")
    print("2: Wijzig voorkeursdienst")
    print("3: Bekijk ritgeschiedenis")
    print("0: Stoppen")
    keuze = input("Maak uw keuze: ")

    if keuze == '1':
        boek_rit()
    elif keuze == '2':
        wijzig_voorkeur()
    elif keuze == '3':
        toon_geschiedenis()
    elif keuze == '0':
        print("Tot ziens! Dank voor het gebruiken van de Uber-app.")
        break
    else:
        print("Ongeldige invoer, probeer opnieuw.")







