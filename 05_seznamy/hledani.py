l = [7, 5, 4, 0, 1, 2, 9, 10, 6]

cislo = int(input())
# zjistí, jestli je v seznamu zadaná hodnota cislo
# a na kterém je indexu

for i in range(len(l)):
    if l[i] == cislo:
        print("číslo je na indexu", i)
        break
    elif i == len(l) - 1:
        print("číslo tam není")

# spočítat kolikrát je v seznamu
# hodota cislo
