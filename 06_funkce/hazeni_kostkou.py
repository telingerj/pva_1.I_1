import random

pocetTrojek = 0
while pocetTrojek < 7:
    cislo = random.randint(1, 6)
    if cislo == 3:
        pocetTrojek += 1
    else:
        pocetTrojek = 0
    print(cislo)