#  hra, ve které bojují dvě armády proti sobě
import random
import pygame
import time

pygame.init()
pygame.font.init()


class Armada:
    def __init__(self, jmeno, barva):
        self.jmeno = jmeno
        self.barva = barva
        self.postavy = []


    def pridej_postavu(self, postava):
        if not isinstance(postava, Postava):
            raise ValueError("postava není typu Postava")
        self.postavy.append(postava)
        postava.pridej_armadu(self)


class Postava:
    def __init__(self, jmeno, zivot, pozice, textura_leva, textura_prava, font):
        self.jmeno = jmeno
        self.zivot = zivot
        self.max_zivot = zivot
        self.pozice = pozice
        self.armada = None
        self.textura_leva = textura_leva
        self.textura_prava = textura_prava
        self.otoceni = True  # výchozí otočení - doleva
        self.font = font
        self.textura_jmeno = None


    def pridej_armadu(self, armada):
        self.armada = armada
        self.textura_jmeno = self.font.render(self.jmeno, False, self.armada.barva)
        #self.textura_jmeno = pygame.transform.flip(self.textura_jmeno, True, False)


    def uber_zivot(self, zivoty):
        self.zivot -= zivoty


    def otoc(self):
        self.otoceni = not self.otoceni


    def vykresli(self, screen):
        if self.otoceni:
            screen.blit(self.textura_leva, self.pozice)
        else:
            screen.blit(self.textura_prava, self.pozice)

        pomer_zivotu = self.zivot / self.max_zivot

        pygame.draw.rect(screen, (100, 100, 100),
                         (self.pozice[0] - 5, self.pozice[1] - 15, 30, 5))
        pygame.draw.rect(screen, (255, 0, 0),
                         (self.pozice[0] - 5, self.pozice[1] - 15, 30 * pomer_zivotu, 5))

        screen.blit(self.textura_jmeno, (self.pozice[0] - 5, self.pozice[1] - 35))



    def pohyb(self):
        if self.otoceni:
            self.pozice = (self.pozice[0] - 1, self.pozice[1])
        else:
            self.pozice = (self.pozice[0] + 1, self.pozice[1])

        if self.pozice[0] <= 0:
            self.otoceni = False
        elif self.pozice[0] >= 775:
            self.otoceni = True


    def vzdalenost(self, postava):
        x1 = self.pozice[0]
        y1 = self.pozice[1]
        x2 = postava.pozice[0]
        y2 = postava.pozice[1]

        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


class Bojovnik(Postava):
    def __init__(self, jmeno, zivot, pozice, poskozeni, textura_leva, textura_prava, font, nepratelska_armada, polomer_utoku):
        super().__init__(jmeno, zivot, pozice, textura_leva, textura_prava, font)
        self.poskozeni = poskozeni
        self.nepratelska_armada = nepratelska_armada
        self.polomer_utoku = polomer_utoku
        self.cas_posledniho_utoku = 0


    def utok(self, postava):
        pass


    def nejblizsi_nepritel(self):
        nejmensi_vzdalenost = 10000
        nejblizsi = None
        for nepritel in self.nepratelska_armada.postavy:
            vzdalenost = self.vzdalenost(nepritel)
            if vzdalenost < nejmensi_vzdalenost:
                nejblizsi = nepritel
                nejmensi_vzdalenost = vzdalenost

        return nejblizsi

    def pohyb(self):

        utoci = False
        nejblizsi = self.nejblizsi_nepritel()
        if self.vzdalenost(nejblizsi) < self.polomer_utoku:
            utoci = True

        if not utoci:
            if self.otoceni:
                self.pozice = (self.pozice[0] - 1, self.pozice[1])
            else:
                self.pozice = (self.pozice[0] + 1, self.pozice[1])

            if self.pozice[0] <= 0:
                self.otoceni = False
            elif self.pozice[0] >= 775:
                self.otoceni = True
        else:
            if time.time() - self.cas_posledniho_utoku > 1:
                self.utok(nejblizsi)
                self.cas_posledniho_utoku = time.time()





class Lucistnik(Bojovnik):
    def __init__(self, jmeno, zivot, pozice, poskozeni, pocet_sipu, textura_leva, textura_prava, font, nepratelska_armada):
        super().__init__(jmeno, zivot, pozice, poskozeni, textura_leva, textura_prava, font, nepratelska_armada, 300)
        self.pocet_sipu = pocet_sipu


    def utok(self, postava):
        self.pocet_sipu -= 1
        postava.uber_zivot(self.poskozeni)


class Sermir(Bojovnik):
    def __init__(self, jmeno, zivot, pozice, poskozeni, ucinnost_stitu, textura_leva, textura_prava, font, nepratelska_armada):
        super().__init__(jmeno, zivot, pozice, poskozeni, textura_leva, textura_prava, font, nepratelska_armada, 30)
        self.ucinnost_stitu = ucinnost_stitu


    def utok(self, postava):
        postava.uber_zivot(self.poskozeni)


    def uber_zivot(self, zivoty):
        if random.randint(1, 100) <= self.ucinnost_stitu:
            self.ucinnost_stitu *= 0.9
            return
        self.zivot -= zivoty


class Kouzelnik(Postava):
    def __init__(self, jmeno, zivot, pozice, uzdraveni, textura_leva, textura_prava, font):
        super().__init__(jmeno, zivot, pozice, textura_leva, textura_prava, font)
        self.uzdraveni = uzdraveni


    def uzdrav(self, postava):
        postava.zivot += self.uzdraveni

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 800))
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.SysFont("Comic sans", 15)
        self.armady = []
        self.textury = []
        self.nacti_textury()
        self.vytvor_armady()



    def vytvor_armady(self):
        a1 = Armada("hodni", (0, 0, 255))
        a2 = Armada("zli", (255, 0, 0))

        s1 = Sermir("Pepa", 100, (100, 100), 10, 10, self.textury[2], self.textury[3], self.font, a2)
        l1 = Lucistnik("Franta", 80, (80, 250), 10, 10, self.textury[0], self.textury[1], self.font, a2)
        k1 = Kouzelnik("Gandalf", 100, (100, 500), 5, self.textury[4], self.textury[5], self.font)

        s2 = Sermir("Jakub", 120, (600, 100), 8, 5, self.textury[2], self.textury[3], self.font, a1)
        l2 = Lucistnik("Honza", 60, (620, 250), 10, 15, self.textury[0], self.textury[1], self.font, a1)
        k2 = Kouzelnik("Merlin", 100, (600, 500), 5, self.textury[4], self.textury[5], self.font)

        a1.pridej_postavu(s1)
        a1.pridej_postavu(l1)
        a1.pridej_postavu(k1)

        a2.pridej_postavu(s2)
        a2.pridej_postavu(l2)
        a2.pridej_postavu(k2)


        for p in a1.postavy:
            p.otoc()

        self.armady = [a1, a2]


    def nacti_textury(self):
        #textura = pygame.image.load("images/archer_left.png")

        for jmeno_postavy in ["archer", "swordsman", "magician"]:
            for otoceni in ["left", "right"]:
                textura = pygame.image.load("images/" + jmeno_postavy + "_" + otoceni + ".png")
                self.textury.append(textura)


    def vykresli(self):
        for a in self.armady:
            for p in a.postavy:
                p.vykresli(self.screen)
                p.pohyb()


    def loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((255, 255, 255))
            self.vykresli()
            self.clock.tick(60)
            pygame.display.flip()


game = Game()
game.loop()
