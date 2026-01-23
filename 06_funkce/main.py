def pozdrav():
    print("ahoj")
    print("jak se máš?")

def pozdrav_jmeno(jmeno):
    print("ahoj", jmeno)

def prvni_pismeno(jmeno):
    return jmeno[0]

def druha_mocnina(cislo):
    return cislo ** 2

def absolutni_hodnota(cislo):
    if cislo >= 0:
        return cislo
    else:
        return cislo * -1


print(absolutni_hodnota(2))
print(absolutni_hodnota(-1))
print(absolutni_hodnota(5))
print(absolutni_hodnota(-6))

# napište funkci, která vrací druhou
# mocninu čísla

# absolutní hodnota
