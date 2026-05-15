file = open("text_files/soubor1.txt", "r", encoding="utf-8")  # otevření textového souboru
obsah = file.read()  # přečtení obsahu
file.close()
seznam = obsah.split("\n")  # rozdělení řádků do seznamu
soucet = 0
for i in seznam:
    soucet += int(i)
print(soucet / len(seznam))
