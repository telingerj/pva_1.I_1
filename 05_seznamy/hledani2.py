l = [1, 1, 4, 5, 2, 5, 4, 1, 3, 5, 2, 1, 1]

cislo = int(input())
nasel = False

for i in range(len(l)):
    if l[i] == cislo:
        print("číslo je na indexu", i)
        nasel = True
        break

if not nasel:
    print("číslo tam není")

# spočítat kolikrát je v seznamu
# hodota cislo