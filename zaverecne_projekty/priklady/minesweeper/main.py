import pygame
import random

pygame.init()
pygame.font.init()

BARVY_POLICKA = [(52, 222, 0), (43, 184, 0)]  # barvy neodkrytých políček v seznamu
BARVY_ODKRYTE = [(176, 153, 4), (155, 140, 0)]  # barvy odkrytých políček v seznamu
POCET_BOMB = 10

class Policko:
    def __init__(self, x, y, textura_bomba, textura_vlajka):
        self.x = x
        self.y = y  # souřadnice políčka
        self.odkryte = False
        self.obsahuje_minu = False
        self.vlajka = False
        self.textura_bomba = textura_bomba
        self.textura_vlajka = textura_vlajka
        self.suda = (x // 80 + y // 80) % 2 == 0  # podle této proměnné se vybírá odstín políčka tak, aby se barvy střídaly
        self.cislo = 0



    def odkryj(self):
        self.odkryte = True


    def umisti_vlajku(self):
        self.vlajka = not self.vlajka


    def vykresli(self, screen, cislice, bomby):
        if self.odkryte:
            if self.suda:
                pygame.draw.rect(screen, BARVY_ODKRYTE[0], (self.x, self.y,  80, 80))  # vykreslení barvy na pozadí
            else:
                pygame.draw.rect(screen, BARVY_ODKRYTE[1], (self.x, self.y, 80, 80))  # vykreslení barvy na pozadí
            if self.cislo > 0:
                screen.blit(cislice[self.cislo], (self.x + 25, self.y + 10))  # vykreslení číslice s počtem bomb v okolí
        else:
            if self.suda:
                pygame.draw.rect(screen, BARVY_POLICKA[0], (self.x, self.y,  80, 80))
            else:
                pygame.draw.rect(screen, BARVY_POLICKA[1], (self.x, self.y, 80, 80))
            if bomby and self.obsahuje_minu:  # proměnná bomby říká, jestli se mají vykreslovat i textury bomb (v případě že hráč již prohrál)
                screen.blit(self.textura_bomba, (self.x, self.y))
            elif self.vlajka:
                screen.blit(self.textura_vlajka, (self.x, self.y))



    def klik_leve(self):  # klik levým tlačítkem na políčko - odkrytí
        if not self.odkryte:
            self.odkryj()


    def klik_prave(self):  # klik pravým tlačítkem na políčko - umístění vlajky
        self.umisti_vlajku()


class Minesweeper:
    def __init__(self, screen):
        self.textura_bomba = pygame.image.load("images/bomb.png")
        self.textura_vlajka = pygame.image.load("images/flag.png")
        self.textura_vyhra = pygame.image.load("images/win.png")  # načtení potřebných textur
        self.font = pygame.font.SysFont("Calibri", 60)  # vytvoření fontu pro číslice s počtem bomb v okolí políčka
        self.screen = screen
        self.vygeneruj_mapu()
        self.umisti_miny()
        self.vygeneruj_cislice()
        self.umisti_cisla()


    def vygeneruj_mapu(self):  # vytvoří dvojrozměrný seznam, kde každá pozice reprezentuje jedno políčko
        self.mapa = []
        for x in range(10):
            r = []
            for y in range(10):
                r.append(Policko(x * 80, y * 80, self.textura_bomba, self.textura_vlajka))
            self.mapa.append(r)


    def umisti_miny(self):
        for i in range(POCET_BOMB):  # chceme umístit POCET_BOMB bomb
            x = random.randint(0, 9)
            y = random.randint(0, 9)  # vygenerování náhodné pozice
            while self.mapa[x][y].obsahuje_minu:  # dokud na pozici již bomba je
                x = random.randint(0, 9)
                y = random.randint(0, 9)  # generujeme novou pozici, aby se bomby nepřekrývaly
            self.mapa[x][y].obsahuje_minu = True


    def vygeneruj_cislice(self):  # vytvoří textury pro všechny číslice 0-9
        self.cislice = []
        for i in range(10):
            c = self.font.render(str(i), True, (0, 0, 0))
            self.cislice.append(c)  # a vloží je do seznamu


    def umisti_cisla(self):
        for x in range(10):
            for y in range(10):
                self.mapa[x][y].cislo = self.vrat_cislo_policka(x, y)  # pro každé políčko určí číslo s počtem bomb v okolí


    def vrat_cislo_policka(self, x, y):  # vrátí číslo s počtem bomb v okolí pro nějaké políčko na pozici x y
        c = 0
        for sousedX in range(x - 1, x + 2):  # procházíme okolí políčka
            for sousedY in range(y - 1, y + 2):
                if sousedX < 0 or sousedX > 9 or sousedY < 0 or sousedY > 9:  # pokud jsme se dostali za hranice mapy, pokračujeme rovnou dál
                    continue
                if self.mapa[sousedX][sousedY].obsahuje_minu:  # započteme každou bombu, na kterou narazíme
                    c += 1
        return c


    def vykresli_mapu(self, prohra):
        for x in range(10):
            for y in range(10):
                self.mapa[x][y].vykresli(self.screen, self.cislice, prohra)  # pro každé políčko voláme vykreslení zvlášť



    def klik_leve(self, pozice):
        x = pozice[0] // 80
        y = pozice[1] // 80  # ze souřadnic pixelů spočítáme souřadnice políček
        if self.mapa[x][y].obsahuje_minu:
            return False  # pokud jsme klikli na minu, vracíme False (prohráli jsme)
        self.mapa[x][y].klik_leve()
        return True


    def klik_prave(self, pozice):
        x = pozice[0] // 80
        y = pozice[1] // 80  # ze souřadnic pixelů spočítáme souřadnice políček
        self.mapa[x][y].klik_prave()


    def vyhra(self):
        c = 0
        for x in range(10):
            for y in range(10):
                if self.mapa[x][y].odkryte:
                    c += 1
        return c == 100 - POCET_BOMB  # pokud jsme odkryli všechna políčka až na miny, vyhráli jsme

    def vykresleni_vyhra(self):
        self.screen.blit(self.textura_vyhra, (300, 300))


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 800))
        self.clock = pygame.time.Clock()
        self.running = True
        self.minesweeper = Minesweeper(self.screen)
        self.prohra = False
        self.vyhra = False


    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:  # kliknutí myši
                    if not self.prohra and not self.vyhra:
                        if event.button == pygame.BUTTON_LEFT:  # levé tlačítko
                            if not self.minesweeper.klik_leve(pygame.mouse.get_pos()):
                                self.prohra = True
                        elif event.button == pygame.BUTTON_RIGHT:  # pravé tlačítko
                            self.minesweeper.klik_prave(pygame.mouse.get_pos())
                    else:  # pokud jsme vyhráli nebo prohráli, kliknutí spustí hru od znova
                        self.reset()

            self.clock.tick(60)
            self.screen.fill((0, 0, 0))
            self.minesweeper.vykresli_mapu(self.prohra)  # to, jestli chceme vykreslovat bomby závísí na self.prohra - pokud jsme prohráli, chceme bomby vidět
            if self.minesweeper.vyhra():  # pokud detekujeme výhru - přenastavíme self.vyhra na True a vykreslíme výherní obrazovku
                self.vyhra = True
                self.minesweeper.vykresleni_vyhra()

            pygame.display.flip()


    def reset(self):
        self.prohra = False
        self.vyhra = False
        self.minesweeper = Minesweeper(self.screen)  # reset znamená nastavení hry do výchozí pozice - vytvoříme nový objekt podle třídy Minesweeper


g = Game()
g.run()
