class Uzivatel:
    def __init__(self, jmeno, email):  # každý uživatel - objekt vytvořený přímo podle této přídy nebo podle jejích potomků - má jméno a email
        self.jmeno = jmeno
        self.email = email



class Student(Uzivatel):  # tato třída dědí z třídy uživatel - získá tak všechny atributy a metody své rodičovské třídy ( v tomto případě třídy Uzivatel)
    def __init__(self, jmeno, email):
        super().__init__(jmeno, email)
        self.trida = None


    def pridej_tridu(self, trida):
        if not isinstance(trida, Trida): # kontrolujeme typ objektu, který nám byl předán jako parametr pomocí funkce isinstance - první parametr je kontrolovaný objekt, druhý typ který daný objek má mít
            raise ValueError("objekt je špatného typu - musí být typu Trida")  # pokud je objekt jiného typu, vyhazujeme chybu
        self.trida = trida


    def vrat_tridniho(self):
        if self.trida is None:  # musíme zkontrolovat, jestli má student uloženou nějakou třídu
            return None
        if self.trida.tridni_ucitel is None:  # a jestli má studentova třída uloženého nějakého třídního učitele
            return None
        return self.trida.tridni_ucitel


class Trida:
    def __init__(self, nazev):
        self.nazev = nazev
        self.studenti = []
        self.tridni_ucitel = None


    def pridej_studenta(self, student):
        if not isinstance(student, Student):  # stejné použití jako u metody pridej_tridu o pár řádků výše
            raise ValueError("objekt je špatného typu - musí být typu Student")
        self.studenti.append(student)
        student.pridej_tridu(self)


    def pridej_tridniho(self, tridni):
        if not isinstance(tridni, TridniUcitel):
            raise ValueError("objekt je špatného typu - musí být typu TridniUcitel")
        self.tridni_ucitel = tridni
        tridni.pridej_tridu(self)


class Ucitel(Uzivatel):
    def __init__(self, jmeno, email, predmet):
        super().__init__(jmeno, email)
        self.predmet = predmet


class TridniUcitel(Ucitel):  # tato třída dědí z třídy Ucitel, která sama navíc dědí z třídy Uzivatel - třída TridniUcitel tedy zdědí všechny atributy a metody z obou těchto tříd
    def __init__(self, jmeno, email, predmet):
        super().__init__(jmeno, email, predmet)
        self.trida = None


    def pridej_tridu(self, trida):
        if not isinstance(trida, Trida):
            raise ValueError("objekt je špatného typu - musí být typu Trida")
        self.trida = trida



# V TÉTO ČÁSTI MŮŽETE VYTVOŘENOU STRUKTURU LIBOVOLNĚ ZKOUŠET


s1 = Student("Jan Novák", "jan.novak@betlemska.cz")
s2 = Student("Petr Pavel", "petr.pavel@betlemska.cz")
s3 = Student("Filip Lenský", "filip.lensky@betlemska.cz")
s4 = Student("Jakub Zavřel", "jakub.zavrel@betlemska.cz")

t1 = Trida("1.I")
t2 = Trida("1.A")

s1.pridej_tridu(t1)
s2.pridej_tridu(t1)
s3.pridej_tridu(t2)
s4.pridej_tridu(t2)

u1 = Ucitel("Jan Telinger", "jan.telinger@betlemska.cz", "PVA")
u2 = Ucitel("Lukáš Slaný", "lukas.slany@betlemska.cz", "M")
u3 = TridniUcitel("Kamil Střihavka", "kamil.strihavka@betlemska.cz", "ICT")
u4 = TridniUcitel("Tomáš Novotný", "tomas.novotny@betlemska.cz", "AJ")

t1.pridej_tridniho(u3)
t2.pridej_tridniho(u4)

