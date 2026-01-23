import time

class Clovek:
    def __init__(self, jmeno, datumNarozeni):
        self.jmeno = jmeno
        self.datumNarozeni = datumNarozeni
        self.auta = []
        print("byl vytvořen člověk")

    def pozdrav(self):
        print("ahoj! já se jmenuju", self.jmeno)

    def vypisDatumNarozeni(self):
        print("narodil jsem se", self.datumNarozeni)

    def jeStarsi(self, clovek2):
        if self.datumNarozeni < clovek2.datumNarozeni:
            return True
        return False

    def pridejAuto(self, auto):
        self.auta.append(auto)
        auto.pridejMajitele(self)

    def vratPocetAut(self):
        return len(self.auta)
        # TODO: vrátí počet vlastněných aut

    def prepisAuto(self, auto, clovek2):
        vlastniAuto = False
        for a in self.auta:
            if auto == a:
                vlastniAuto = True
                self.auta.remove(a)
        if not vlastniAuto:
            return
        clovek2.pridejAuto(auto)
        # TODO: pokud je člověk majitelem auta, přepíše vlastnictví
        # TODO: auta na clovek2

class Auto:
    def __init__(self, znacka, rokVyroby, barva):
        self.znacka = znacka
        self.rokVyroby = rokVyroby
        self.barva = barva
        self.majitel = None
        print("bylo vytvořeno auto")

    def vratStari(self):
        aktualniRok = time.localtime().tm_year
        return aktualniRok - self.rokVyroby

    def pridejMajitele(self, majitel):
        self.majitel = majitel


p = Clovek("Pepa", 2001)
p2 = Clovek("Franta", 2004)


"""
c = Auto("Škoda", 2012, "černá")
c2 = Auto("Volkswagen", 2005, "červená")

p.pridejAuto(c)
p.pridejAuto(c2)

p.prepisAuto(c, p2)
print(p.vratPocetAut())
"""