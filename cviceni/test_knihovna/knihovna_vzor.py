class Knihovna:
    def __init__(self, jmeno, kapacita):
        self.jmeno = jmeno
        self.kapacita = kapacita
        self.knihy = []


    def pridej_knihu(self, kniha):
        self.knihy.append(kniha)
        kniha.pridej_knihovnu(self)
        #TODO: váš úkol: zamezit přidání knihy, pokud je již zaplněna kapacita


    def pocet_knih(self):
        pass
        #TODO: váš úkol


    def celkovy_pocet_stran(self):
        pass
        #TODO: váš úkol


    def pocet_autoru(self):
        pass
        #TODO: váš úkol

class Kniha:
    def __init__(self, jmeno, autor, pocet_stran):
        self.jmeno = jmeno
        self.autor = autor
        self.pocet_stran = pocet_stran
        self.knihovna = None

    def pridej_knihovnu(self, knihovna):
        self.knihovna = knihovna


def nacti_vstup():
    jmeno_knihovny = input()
    kapacita_knihovny = int(input())
    knihovna = Knihovna(jmeno_knihovny, kapacita_knihovny)
    while True:
        jmeno_knihy = input()
        if jmeno_knihy == "konec":
            break
        autor_knihy = input()
        pocet_stran_knihy = int(input())
        kniha = Kniha(jmeno_knihy, autor_knihy, pocet_stran_knihy)
        knihovna.pridej_knihu(kniha)
    return knihovna

knihovna1 = nacti_vstup()
knihovna2 = nacti_vstup()

print(knihovna1.pocet_knih())
print(knihovna2.pocet_knih())

print(knihovna1.pocet_autoru())
print(knihovna2.pocet_autoru())

print(knihovna1.celkovy_pocet_stran())
print(knihovna2.celkovy_pocet_stran())
