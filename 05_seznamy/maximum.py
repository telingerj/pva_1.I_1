l = [8, 5, 2, 1, 6, 9, 8, 10, 1, 10, 10, 10]

# které číslo je v seznamu největší a nejmenší?
# na jakém je indexu?

nejvetsiIndex = 0
nejmensiIndex = 0
for i in range(len(l)):
    if l[i] > l[nejvetsiIndex]:
        nejvetsiIndex = i
    elif l[i] < l[nejmensiIndex]:
        nejmensiIndex = i

print("největší číslo je",
      l[nejvetsiIndex], "a je na indexu", nejvetsiIndex)
print("nejmenší číslo je",
      l[nejmensiIndex], "a je na indexu", nejmensiIndex)