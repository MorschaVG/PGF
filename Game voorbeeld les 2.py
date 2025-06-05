print("Je loopt je favoriete hippe koffietent binnen. De barista achter de toonbank is je minst favoriete.\n"
      "Je vermoedt dat jij ook zijn minst favoriete klant bent.\n"
      "Je besteld (voor de verandering) een dubbele espresso. Je hebt niet zo goed geslapen, dus even iets stevigs.\n"
      "Na even wachten wordt je bestelling opgenomen en gemaakt maar de manier waarop staat jou helemáááál niet aan.\n"
      "Er kan amper een lachje vanaf, sterker nog, je wordt niet eens aan gekeken.\n"
      "Jij geeft nog een schaapse 'dankjewel' maar de barista kijkt naar zijn collega en geeft een cynische grijns.\n"
      "Walgelijk.")
eerste_keus = int(input("Wat doe je?\n1. Je doet onvriendelijk terug door 'Nou bedankt hè' te zeggen\n2. Je negeert het, je staat hier boven.\n"
      "3. Je escaleert! Je bent een vaste klant! Je komt hier al 8 maanden! Je verheft je stem nogal..\n"
      "Wat wordt je keuze?"))
if eerste_keus in [1, 2]:
    print("De barista kijkt je aan met de nihilistische blik die alleen een verwende Gen-Z'er kan optrommelen.\n"
          "Je koffie wordt afgeraffeld. Dit weet jij want je bent een connaisseur en weet dat een dubbele espresso\n"
          "veel langer door de piston heen moet. Je krijgt gewoon slechte koffie geserveerd, expres.")
    tweede_keus = int(input("Wat doe je nu?\n1. Je accepteert je nederlaag\n2. Je vraagt resoluut om de manager te spreken (ja je bent nu die boomer geworden)\n"
                            "Wat kies je?"))
    if tweede_keus == 1:
        print("Gefeliciteerd! Je koffie is nu duur én slecht.")

    else:
        print("De manager wordt voor je gehaald. Iedereen kijkt naar je. Jij bent die gast.\n"
              "Je krijgt je gelijk. Er wordt een nieuwe dubbele espresso voor je gemaakt. Er is waarschijnlijk in gespuugd."
              "Gefeliciteerd.")

elif eerste_keus ==3 :
    print("Wow. Echt? Schreeuwen in een koffietent omdat je niet als een koning behandeld wordt? Damn.\n"
          "De toegang wordt je (voor eeuwig) ontzegt en ook je stempelkaart waarop je nog 1 stempel verwijderd was\n"
          "van een gratis flat white haver wordt per direct gevorderd. Game over.")

    print ("Einde.")