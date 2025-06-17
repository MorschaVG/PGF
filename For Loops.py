# count = 0
# while count < 5:
#     print(f"De teller staat op {count}")
#     count += 1
# nummers = [1, 2, 3, 4, 5]
# temp = []
#
# for cijfer in nummers:
#     temp.append(float(cijfer))
#
# print(temp)

# tuple lijst voorbeeld:

# tuple_list = [(1,2,3),(4,5,6),(7,8,9)]
#
# for rgb in tuple_list:
#     print(f"red = {rgb[0]}")
#     print(f"green = {rgb[1]}")
#     print(f"blue = {rgb[2]}")

# tuple_list = [(1,2,3),(4,5,6),(7,8,9)]
#
# reds, greens, blues = zip(*tuple_list)
#
# print("Reds:", reds)
# print("Greens:", greens)
# print("Blues:", blues)

# Opdracht
#
# Onderstaande code is een puzzel.

# De 7 coordinaten vormen een woord van 7 letters.

# Ontcijfer elk coordinaat een voor een tot een letter uit de puzzel lijst.

# Sla jou ontcijferde letters op in de "antwoord" variabele

# (Tip: bekijk een woord als een lijst van letters)
# Print je antwoord uit.

# puzzel = ["Albatros", "poncho", "vlinder", "glitter", ]
# coordinaten = [(0,0),(2,0), (0,-2), (1,3), (0,3),(2,4), (1,-1)]
# antwoord =
# sla hier je antwoord in op.

puzzel = ["Albatros","poncho", "vlinder", "glitter", ]
coordinaten = [(0,0),(2,0), (0,-2), (1,3), (0,3),(2,4), (1,-1)]

antwoord = []

for woord, letter in coordinaten:
    oplossing = puzzel[woord][letter]
    antwoord.append(oplossing)

print("".join(antwoord))




