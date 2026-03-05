class Knihovna:  # třída knihovna
    def __init__(self, jmeno, kapacita):  # jméno a kapacitu přijímáme jako parametry v konstruktoru
        self.jmeno = jmeno
        self.kapacita = kapacita  # a ukládáme je do atributů
        self.knihy = []  # seznam, ve kterém budeme mít uložené všechny objekty typu Kniha, které ke knihovně patří


    def pridej_knihu(self, kniha):  # metoda, která zajistí přidání knihy (která přijde jako parametr metody)
        if self.kapacita == len(self.knihy):  # kontrola, jestli je počet již přidaných knih stejný jako kapacita (v takovém případě knihu nemůžeme přidat)
            return  # knihu nemůžeme přidat - return zajistí, že metoda okamžitě skončí a zbytek kódu se tedy neprovede
        self.knihy.append(kniha)  # v tomto místě již víme, že knihu lze přidat
        kniha.pridej_knihovnu(self)  # na knize zavoláme metodu, která zajistí přidání této knihovny (self) knize


    def pocet_knih(self):
        return len(self.knihy)  # vracíme délku seznamu knihy - počet knih


    def celkovy_pocet_stran(self):
        s = 0  # lokální proměnná, do které budeme přičítat počet stran
        for k in self.knihy:  # potřebujeme sečíst počet stran všech knih které v knihovně jsou - pomocí foru tedy procházíme seznam knihy
            s += k.pocet_stran  # a do proměnné přičítáme počet stran každé knihy
        return s  # na konci již máme sečtené všechny knihy, součet vrátíme


    def pocet_autoru(self):
        autori = []  # seznam, do kterého budeme postupně přidávat všechny autory, na které narazíme
        for k in self.knihy:  # procházíme všechny knihy, které máme v knihovně
            if k.autor not in autori:  # může se stát, že knihu od stejného autora jsme již viděli, kontrolujeme tedy, jestli autor v seznamu ještě není
                autori.append(k.autor)  # pokud ne, autora přidáme do seznamu
        return len(autori)  # zajímá nás počet autorů, vrátíme tedy délku právě vytvořeného seznamu


class Kniha:  # třída kniha
    def __init__(self, jmeno, autor, pocet_stran):  # jméno, autora a počet stran přijímáme jako parametry v konstruktoru
        self.jmeno = jmeno
        self.autor = autor
        self.pocet_stran = pocet_stran  # a ukládáme je do atributů
        self.knihovna = None  # zde bude uložená knihovna, do které tato kniha patří (zatím nikam nepatří, uložíme hodnotu None)

    def pridej_knihovnu(self, knihovna):
        self.knihovna = knihovna  # uložíme knihovnu, kterou jsme dostali jako parametr


def nacti_vstup():  # funkce, která postupně přijme všechny data jako vstup a vrátí vytvořený objekt knihovny
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
