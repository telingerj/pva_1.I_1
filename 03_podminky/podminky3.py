# program, který načte číslo, když je to 1 tak ho změní na 0,
# když je to 0, tak změní na 1, jinak nic nezmění

cislo = int(input())

if cislo == 1:
    cislo = 0
elif cislo == 0:
    cislo = 1

print(cislo)
