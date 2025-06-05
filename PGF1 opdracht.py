#verzin een verhaal van ongeveer 20-50 woorden, waarin je minimaal 5 variabelen zet
#die de gebruiker zelf moet invullen
from idlelib.run import manage_socket

#Merel loopt door de gibraltarstraat terwijl de zoete klanken van artiest uit haar airpods komen.
#Ze kan niet wachten tot ze Morscha weer ziet. Vandaag gaan ze samen videogames spelen en spaghetti eten.

#TODO: Hier moet nog even gekeken worden naar de opties voor het formatteren van de hobby input
#dit is een test van de Pycharm to-do functie

naam = input("Wat is je naam?")
geslacht = input("Wat is je geslacht? man/vrouw/nonbinair: ")
straat = input("Wat is je lievelings straat?")
artiest = input("Wie is je favoriete artiest?")
persoon = input("Wie is je lievelingspersoon?")
hobby = input("Wat is je hobby?")
eten = input("Wat is je lievelingseten?")

if geslacht == "man" :
    voornaamwoord = "hij"
    bezittelijk = "zijn"
elif geslacht == "vrouw":
    voornaamwoord = "ze"
    bezittelijk = "haar"
else:
    voornaamwoord = "die"  # eventueel genderneutraal alternatief
    bezittelijk = "hun"
verhaal = (f"{naam} loopt door de {straat} terwijl de zoete klanken van {artiest}"
           f" uit {bezittelijk} airpods komen. \n{voornaamwoord.capitalize()} kan niet wachten tot {voornaamwoord} "
           f"{persoon} weer ziet.\n"
           f"Vandaag gaan ze samen {hobby} en {eten} eten")

print(verhaal)

