class Zoo:
    def __init__(self, jmeno, rokVzniku, rozloha):
        self.jmeno = jmeno
        self.rokVzniku = rokVzniku
        self.rozloha = rozloha
        self.vybehy = []


    def predstav(self):
        print("Zoologická zahrada", self.jmeno, "vznikla v roce",self.rokVzniku ,"a má rozlohu", self.rozloha, "ha")


    def vzniklaVTomtoStoleti(self):
        if self.rokVzniku >= 2001:
            return True
        return False


    def pridejVybeh(self, vybeh):
        if self.volneMisto() < vybeh.rozloha:
            return False
        self.vybehy.append(vybeh)
        vybeh.pridejZoo(self)
        return True


    def rozlohaVsechVybehu(self):
        soucet = 0
        for v in self.vybehy:
            soucet += v.rozloha
        return soucet


    def volneMisto(self):
        return self.rozloha - self.rozlohaVsechVybehu()


    def pocetZvirat(self):
        s = 0
        for vybeh in self.vybehy:
            s += len(vybeh.zvirata)
        return s


    def maZvireSeJmenem(self, jmeno):
        for vybeh in self.vybehy:
            for zvire in vybeh.zvirata:
                if zvire.jmeno == jmeno:
                    return True
        return False


class Vybeh:
    def __init__(self, nazev, rozloha):
        self.nazev = nazev
        self.rozloha = rozloha
        self.zvirata = []
        self.zoo = None


    def pridejZoo(self, zoo):
        self.zoo = zoo


    def pridejZvire(self, zvire):
        if len(self.zvirata) > 0 and self.zvirata[0].druh != zvire.druh:
            return False
        self.zvirata.append(zvire)
        zvire.pridejVybeh(self)
        return True


class Zvire:
    def __init__(self, druh, jmeno, hmotnost, rokNarozeni):
        self.druh = druh
        self.jmeno = jmeno
        self.hmotnost = hmotnost
        self.rokNarozeni = rokNarozeni
        self.vybeh = None


    def pridejVybeh(self, vybeh):
        self.vybeh = vybeh


def zadaniZoo():
    z = []
    print("zadej údaje o zoo, ukonči zadáním prázdného řádku")
    jmeno = ""
    rok = 0
    rozloha = 0
    while True:
        jmeno = input("jméno: ")
        if jmeno == "":
            break
        rok = int(input("rok založení: "))
        rozloha = int(input("rozloha: "))
        z.append(Zoo(jmeno, rok, rozloha))
    return z


def vypisZoo(z):
    for i in range(len(z)):
        print(i, ":", z[i].jmeno)


def vypisVybehy(z):
    for i in range(len(z)):
        print(i, ":", z[i].jmeno)
        for j in range(len(z[i].vybehy)):
            print("   ", j, ":", z[i].vybehy[j].nazev)


def vypisZvirata(z):
    for i in range(len(z)):
        print(i, ":", z[i].jmeno)
        for j in range(len(z[i].vybehy)):
            print("   ", j, ":", z[i].vybehy[j].nazev)
            for k in range(len(z[i].vybehy[j].zvirata)):
                print("     ", k, ":", z[i].vybehy[j].zvirata[k].jmeno)


def zadaniVybehu(z):
    v = []
    print("zadej údaje o výběhu, ukonči zadáním prázdného řádku")
    vypisZoo(z)
    nazev = ""
    rozloha = 0
    while True:
        nazev = input("název: ")
        if nazev == "":
            break
        rozloha = int(input("rozloha: "))
        cisloZoo = int(input("zadej číslo zoo: "))

        vybeh = Vybeh(nazev, rozloha)
        z[cisloZoo].pridejVybeh(vybeh)
        v.append(vybeh)
    return v


def zadaniZvirete(z):
    zvirata = []
    druh = ""
    jmeno = ""
    hmotnost = 0
    rokNarozeni = 0
    vypisVybehy(z)
    print("zadej údaje o zvířeti, ukonči zadáním prázdného řádku")
    while True:
        jmeno = input("jméno: ")
        if jmeno == "":
            break
        druh = input("druh: ")
        hmotnost = int(input("hmotnost: "))
        rokNarozeni = int(input("rok narozeni: "))
        cisloZoo = int(input("číslo zoo: "))
        cisloVybehu = int(input("číslo výběhu: "))

        zvire = Zvire(druh, jmeno, hmotnost, rokNarozeni)
        z[cisloZoo].vybehy[cisloVybehu].pridejZvire(zvire)
        zvirata.append(zvire)
    return zvirata

z = zadaniZoo()
zadaniVybehu(z)
vypisVybehy(z)


"""
z1 = Zoo("Zoo Praha", 1931, 58)
z2 = Zoo("Zoo Plzeň", 1954, 32)
z3 = Zoo("fiktivní zoo", 2010, 15)

v1 = Vybeh("sloni", 10)
v2 = Vybeh("ptáci", 1)
v3 = Vybeh("žirafy", 4)

z1.pridejVybeh(v1)
z1.pridejVybeh(v2)
z1.pridejVybeh(v3)

zvire1 = Zvire("slon", "Karel", 5540, 2013)
zvire2 = Zvire("slon", "Pepa", 4870, 2019)
zvire3 = Zvire("papoušek", "Franta", 1, 2018)
zvire4 = Zvire("žirafa", "Božena", 1051, 2009)
zvire5 = Zvire("žirafa", "Alexandria", 1147, 2020)


v1.pridejZvire(zvire1)
v1.pridejZvire(zvire2)
v2.pridejZvire(zvire3)
v3.pridejZvire(zvire4)
v3.pridejZvire(zvire5)


print(z1.maZvireSeJmenem("Karel"))
print(z1.maZvireSeJmenem("Honza"))
"""

