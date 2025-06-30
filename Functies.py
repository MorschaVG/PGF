# def vermenigvuldig(cijfer1, cijfer2):
#     return (cijfer1 * cijfer2)
#
# print(vermenigvuldig(10, 45))

# cijfer1 = int(input("Van welk cijfer wil je het kwadraat weten?"))
#
# def kwadraat_van(cijfer1):
#     return (cijfer1 * cijfer1)
#
# uitkomst = kwadraat_van(cijfer1)
#
# print(f"{cijfer1} in het kwadraat is: {uitkomst}")
#
# print(f"En dat dan weer door de helft is {int(uitkomst / 2)}")

def oppervlakte(lijst):
    oppervlaktes = []
    for x,y in lijst:
        oppervlaktes.append(str(x*y) + " m2")
    return oppervlaktes

# oppervlaktes = oppervlakte(lijst_met_afmetingen)
#
# print(oppervlaktes)






