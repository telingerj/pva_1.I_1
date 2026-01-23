cislo = int(input("Cislo: "))

predposledni = 0
posledni = 1
print("0 1", end=" ")
for i in range(cislo - 2):
    soucet = predposledni + posledni
    print(soucet, end=" ")
    predposledni = posledni
    posledni = soucet
