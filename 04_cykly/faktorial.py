cislo = int(input("zadej číslo: "))

f = 1
for i in range(1, cislo + 1):
    f *= i
print(f)