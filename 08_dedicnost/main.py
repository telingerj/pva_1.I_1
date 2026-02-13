class Tvar2d:
    def __init__(self, jmeno):
        self.jmeno = jmeno


    def obvod(self):
        return 0


    def obsah(self):
        return 0


    def ma_vetsi_obsah_nez(self, druhyTvar):
        return self.obsah() > druhyTvar.obsah()


    def ma_vetsi_obvod_nez(self, druhyTvar):
        return self.obvod() > druhyTvar.obvod()

class Ctverec(Tvar2d):
    def __init__(self, jmeno, a):
        super().__init__(jmeno)
        self.a = a


    def obvod(self):
        return 4 * self.a


    def obsah(self):
        return self.a * self.a


class Obdelnik(Tvar2d):
    def __init__(self, jmeno, a, b):
        super().__init__(jmeno)
        self.a = a
        self.b = b


    def obvod(self):
        return 2 * self.a + 2 * self.b


    def obsah(self):
        return self.a * self.b


class Kruh(Tvar2d):
    def __init__(self, jmeno, r):
        super().__init__(jmeno)
        self.r = r

    def obvod(self):
        return round(2 * 3.14 * self.r, 1)


    def obsah(self):
        return round(3.14 * (self.r ** 2), 1)


class Trojuhelnik(Tvar2d):
    def __init__(self, jmeno, a, b, c):
        super().__init__(jmeno)
        self.kontrola(a, b, c)
        self.a = a
        self.b = b
        self.c = c


    def kontrola(self, a, b, c):
        cisla = [a, b, c]
        cisla.sort()
        if cisla[0] + cisla[1] <= cisla[2]:
            raise ValueError("takový trojúhelník neexistuje")


    def obvod(self):
        return self.a + self.b + self.c



    def obsah(self):
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5


    def je_pravouhly(self):
        cisla = [self.a, self.b, self.c]
        cisla.sort()
        return cisla[0] ** 2 + cisla[1] ** 2 == cisla[2] ** 2


ctverec1 = Ctverec("ctverecek", 10)
obdelnik1 = Obdelnik("obdelnicek", 5, 2)
kruh1 = Kruh("krouzek", 5)
trojuhelnik1 = Trojuhelnik("trojuhelnik", 3, 4, 5)
trojuhelnik2 = Trojuhelnik("trojuhelnik", 6, 6, 9)

print(ctverec1.ma_vetsi_obsah_nez(obdelnik1))