text = "ahoj jak se mas? ja se mam dobre"
text += "!"

znak1 = 0
znak2 = 0
for i in text:
    if i == "a":
        znak1 += 1
    elif i == "e":
        znak2 += 1

if znak1 > znak2:
    print("je tam víc znaků a")
elif znak1 < znak2:
    print("je tam víc znaků e")
else:
    print("je jich stejně")

# spočítat, kolikrát tam je písmeno "a"
# zjistit, jestli tam je víc "a" nebo "e"