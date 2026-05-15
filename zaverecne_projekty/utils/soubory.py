file = open("text_files/soubor1.txt", "r", encoding="utf-8")  # otevření textového souboru
obsah = file.read()  # přečtení obsahu
file.close()
seznam = obsah.split("\n")  # rozdělení řádků do seznamu
soucet = 0
for i in seznam:
    soucet += int(i)
prumer = soucet / len(seznam)
file = open("text_files/soubor2.txt", "w", encoding="utf-8")  # otevření jiného textového souboru pro zápis (w)
file.write(str(prumer))
file.close()
