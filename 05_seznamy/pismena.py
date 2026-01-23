# program, který vypíše nejposlednější písmeno z abecedy
# v daném textu

text = "v danem textu"

maximum = 0

for znak in text:
    if ord(znak) > maximum:
        maximum = ord(znak)

print("nejposlednější z řetězce je", chr(maximum))
