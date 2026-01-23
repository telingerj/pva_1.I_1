import random
# kolik hodů mi bude trvat, než padne 6?
pocetHodu = 0
padlo = 0
while padlo != 6:
    padlo = random.randint(1, 6)
    pocetHodu += 1


# hodit 10krát a spočítat kolikrát padla 3

pocet = 0
for i in range(10):
    cislo = random.randint(1, 6)
    if cislo == 3:
        pocet += 1

print(pocet)