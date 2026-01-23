# spočítat kolikrát je v seznamu
# hodota cislo

l = [1, 1, 4, 5, 2, 5, 4, 1, 3, 5, 2, 1, 1]

cislo = int(input())
pocet = 0

for i in range(len(l)):
    if l[i] == cislo:
        pocet += 1

print(pocet)
