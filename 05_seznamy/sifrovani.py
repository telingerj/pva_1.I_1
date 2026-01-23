# Caesarova šifra

text = "bipk" # pismena z anglicke abecedy
zasifrovanyText = ""

for i in text:
    kod = ord(i)
    kod -= 1
    if kod > ord("z"):
        kod -= 26
    if kod < ord("a"):
        kod += 26
    zasifrovanyZnak = chr(kod)
    zasifrovanyText += zasifrovanyZnak

print(zasifrovanyText)