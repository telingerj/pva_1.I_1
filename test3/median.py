cisla = []
vstup = ""
while True:
    vstup = input()
    if vstup == "konec":
        break
    cisla.append(vstup)

print(cisla[len(cisla) // 2])