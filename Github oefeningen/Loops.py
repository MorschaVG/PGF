# Tafels

# Schrijf een programma dat de tafel van een getal afdrukt.
# De gebruiker voert een getal in en het programma drukt de tafel van dat getal af.
# De tafel van 7 ziet er bijvoorbeeld als volgt uit:
# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# 7 x 5 = 35
# 7 x 6 = 42
# 7 x 7 = 49
# 7 x 8 = 56
# 7 x 9 = 63
# 7 x 10 = 70


# Probeer het eerst zonder loop,

# getal = int(input("Voer een getal in om de tafel daarvan te krijgen: "))
#
# print(f"{getal} x 1 = {getal}\n"
#       f"{getal} x 2 = {getal*2}\n"
#       f"{getal} x 3 = {getal*3}\n"
#       f"{getal} x 4 = {getal*4}\n"
#       f"{getal} x 5 = {getal*5}\n"
#       f"{getal} x 6 = {getal*6}\n"
#       f"{getal} x 7 = {getal*7}\n"
#       f"{getal} x 8 = {getal*8}\n"
#       f"{getal} x 9 = {getal*9}\n"
#       f"{getal} x 10 = {getal*10}")

# Probeer het nu met een loop.

# getal = int(input("Voer een getal in om de tafel daarvan te krijgen: "))
#
# for i in range(1, 11):
#     print(f"{getal} x {i} = {getal*i}")


# --------------------------------------------------------------------------------------------

# Optellen
# Schrijf een programma dat de som van alle getallen tot een bepaalde limiet berekent.

# Bijvoorbeeld: de som van alle getallen tot 3 is 6 (1 + 2 + 3 = 6)
# limiet = int(input("Tot welk getal wil je optellen?"))
#
# som = 0
#
# for getal in range(1,limiet +1):
#     som += getal
#
# print("De som van alle getallen tot en met", limiet, "is:", som)
# --------------------------------------------------------------------------------------------

# Dit is een klassieke programmeeroefening die vaak wordt gebruikt in sollicitatiegesprekken.
# FizzBuzz

# Schrijf een programma dat de getallen van 1 tot 100 afdrukt.
# Maar voor veelvouden van drie, druk "Fizz" af in plaats van het getal.
# En voor veelvouden van vijf, druk "Buzz" af.
# Voor veelvouden van zowel drie als vijf, druk "FizzBuzz" af.

# for i in range(1, 101):
#     if i % 5 == 0 and i % 3 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

# for i in range(1, 101):
#     output = ""
#     if i % 3 == 0:
#         output += "Fizz"
#     if i % 5 == 0:
#         output += "Buzz"
#     print(output or i)


# --------------------------------------------------------------------------------------------


# Fibonacci-reeks

# De eerste twee getallen van de Fibonacci-reeks zijn 0 en 1.
# Elk volgend getal is de som van de twee voorgaande.
# De eerste 10 getallen van de Fibonacci-reeks zijn:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
# 0 + 1 = 1
# 1 + 1 = 2
# 1 + 2 = 3
# 2 + 3 = 5
# 3 + 5 = 8
# 5 + 8 = 13
# 8 + 13 = 21
# 13 + 21 = 34

# i = int(input("Hoeveel Fibonacci-getallen wil je zien? "))
#
# # De eerste twee getallen van de Fibonacci-reeks zijn 0 en 1
# a = 0
# b = 1
#
# # Eerst drukken we de eerste twee getallen af
#
# print(f"{a}, {b}")

# Vervolgens berekenen we de volgende getallen en drukken ze af

