class Tvar2d:
    def __init__(self, jmeno):
        self.jmeno = jmeno


    def obvod(self):
        return 0


    def obsah(self):
        return 0


    def je_vetsi_nez(self, tvar2):
        if not isinstance(tvar2, Tvar2d):
            raise TypeError("tvar2 musí být 2d tvar")
        return self.obsah() > tvar2.obsah()


    def je_mensi_nez(self, tvar2):
        if not isinstance(tvar2, Tvar2d):
            raise TypeError("tvar2 musí být 2d tvar")
        return self.obsah() < tvar2.obsah()


    def je_rovny(self, tvar2):
        if not isinstance(tvar2, Tvar2d):
            raise TypeError("tvar2 musí být 2d tvar")
        return self.obsah() == tvar2.obsah()


    def __lt__(self, other):  # přetížení operátoru <
        return self.je_mensi_nez(other)


    def __add__(self, other):  # přetížení operátoru +
        return self.obsah() + other.obsah()



class Tvar3d:
    def __init__(self, jmeno):
        self.jmeno = jmeno


    def objem(self):
        return 0


    def povrch(self):
        return 0


    def je_vetsi_nez(self, tvar2):
        if not isinstance(tvar2, Tvar3d):
            raise TypeError("tvar2 musí být 3d tvar")
        return self.objem() > tvar2.objem()


    def __lt__(self, other): # přetížení operátoru <
        return self.je_vetsi_nez(other)


    def __add__(self, other): # přetížení operátoru +
        return self.objem() + other.objem()


class Ctverec(Tvar2d):
    def __init__(self, jmeno, a):
        super().__init__(jmeno)
        self.a = a


    def obvod(self):
        return self.a * 4


    def obsah(self):
        return self.a ** 2


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
        return round(2 * 3.14 * self.r, 2)


    def obsah(self):
        return round(3.14 * (self.r ** 2), 2)


class Trojuhelnik(Tvar2d):
    def __init__(self, jmeno, a, b, c):
        self.kontrola(a, b, c)
        super().__init__(jmeno)
        self.a = a
        self.b = b
        self.c = c


    def kontrola(self, a, b, c):
        strany = [a, b, c]
        strany.sort()
        if strany[0] + strany[1] <= strany[2]:
            raise ValueError("takový trojúhelník nemůže existovat")


    def obvod(self):
        return self.a + self.b + self.c


    def obsah(self):
        s = (self.a + self.b + self.c) / 2
        return round(
            (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5, 2)


    def je_pravouhly(self):
        strany = [self.a, self.b, self.c]
        strany.sort()
        return strany[0] ** 2 + strany[1] ** 2 == strany[2] ** 2


class RovnostrannyTrojuhelnik(Trojuhelnik):
    def __init__(self, jmeno, a):
        super().__init__(jmeno, a, a, a)


    def obvod(self):
        return 3 * self.a


    def obsah(self):
        v = (self.a ** 2 - (self.a / 2) ** 2) ** 0.5
        return (self.a * v) / 2



class Krychle(Tvar3d):
    def __init__(self, jmeno, a):
        super().__init__(jmeno)
        self.a = a

    def objem(self):
        return self.a ** 3

    def povrch(self):
        return (self.a ** 2) * 6


class Kvadr(Tvar3d):
    def __init__(self, jmeno, a, b, c):
        super().__init__(jmeno)
        self.a = a
        self.b = b
        self.c = c


    def objem(self):
        return self.a * self.b * self.c


    def povrch(self):
        return self.a * self.b * 2 + self.b * self.c * 2 + self.a * self.c * 2



class Koule(Tvar3d):
    def __init__(self, jmeno, r):
        super().__init__(jmeno)
        self.r = r

    def objem(self):
        return (4 / 3) * 3.14 * self.r ** 3


    def povrch(self):
        return 4 * 3.14 * self.r ** 2


c1 = Ctverec("c", 5)
c2 = Ctverec("c", 6)

k1 = Krychle("k", 5)
k2 = Krychle("k", 6)

print(c1 + c2)
print(k1 + k2)
