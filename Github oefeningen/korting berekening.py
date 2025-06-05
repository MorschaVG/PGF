prijs = 100
lid = input("Lid? (j/n?)")
leeftijd = int(input("Leeftijd:"))

if lid == "n" :
    if leeftijd >= 65 :
        korting = 10

else :
    korting = 25

print("De prijs is: ", prijs * (1 - korting / 100))