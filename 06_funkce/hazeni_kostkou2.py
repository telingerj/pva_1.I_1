import random

pocetHodu = 10000000
cisla = [0, 0, 0, 0, 0, 0]

for i in range(pocetHodu):
    hod = random.randint(1, 6)
    cisla[hod - 1] += 1

# spočítat procentuální zastoupení čísel na kostce

for i in range(len(cisla)):
    procenta = cisla[i] / pocetHodu
    print(i + 1, ":", procenta * 100, "%")