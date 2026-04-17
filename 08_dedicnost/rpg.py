#  hra, ve které bojují dvě armády proti sobě
import random
import pygame

pygame.init()


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
    def __init__(self, jmeno, zivot, pozice, textura_leva, textura_prava):
        self.jmeno = jmeno
        self.zivot = zivot
        self.max_zivot = zivot
        self.pozice = pozice
        self.armada = None
        self.textura_leva = textura_leva
        self.textura_prava = textura_prava
        self.otoceni = True  # výchozí otočení - doleva


    def pridej_armadu(self, armada):
        self.armada = armada


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


    def pohyb(self):
        if self.otoceni:
            self.pozice = (self.pozice[0] - 1, self.pozice[1])
        else:
            self.pozice = (self.pozice[0] + 1, self.pozice[1])

        #TODO: otočení postavy když dorazí na kraj okna



class Bojovnik(Postava):
    def __init__(self, jmeno, zivot, pozice, poskozeni, textura_leva, textura_prava):
        super().__init__(jmeno, zivot, pozice, textura_leva, textura_prava)
        self.poskozeni = poskozeni


    def utok(self, postava):
        pass


class Lucistnik(Bojovnik):
    def __init__(self, jmeno, zivot, pozice, poskozeni, pocet_sipu, textura_leva, textura_prava):
        super().__init__(jmeno, zivot, pozice, poskozeni, textura_leva, textura_prava)
        self.pocet_sipu = pocet_sipu


    def utok(self, postava):
        self.pocet_sipu -= 1
        postava.uber_zivot(self.poskozeni)


class Sermir(Bojovnik):
    def __init__(self, jmeno, zivot, pozice, poskozeni, ucinnost_stitu, textura_leva, textura_prava):
        super().__init__(jmeno, zivot, pozice, poskozeni, textura_leva, textura_prava)
        self.ucinnost_stitu = ucinnost_stitu


    def utok(self, postava):
        postava.uber_zivot(self.poskozeni)


    def uber_zivot(self, zivoty):
        if random.randint(1, 100) <= self.ucinnost_stitu:
            self.ucinnost_stitu *= 0.9
            return
        self.zivot -= zivoty


class Kouzelnik(Postava):
    def __init__(self, jmeno, zivot, pozice, uzdraveni, textura_leva, textura_prava):
        super().__init__(jmeno, zivot, pozice, textura_leva, textura_prava)
        self.uzdraveni = uzdraveni


    def uzdrav(self, postava):
        postava.zivot += self.uzdraveni

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 800))
        self.clock = pygame.time.Clock()
        self.running = True
        self.armady = []
        self.textury = []
        self.nacti_textury()
        self.vytvor_armady()



    def vytvor_armady(self):
        a1 = Armada("hodni", (0, 0, 255))
        a2 = Armada("zli", (255, 0, 0))

        s1 = Sermir("Pepa", 100, (100, 100), 10, 10, self.textury[2], self.textury[3])
        l1 = Lucistnik("Franta", 80, (80, 250), 10, 10, self.textury[0], self.textury[1])
        k1 = Kouzelnik("Gandalf", 100, (100, 500), 5, self.textury[4], self.textury[5])

        s2 = Sermir("Jakub", 120, (600, 100), 8, 5, self.textury[2], self.textury[3])
        l2 = Lucistnik("Honza", 60, (620, 250), 10, 15, self.textury[0], self.textury[1])
        k2 = Kouzelnik("Merlin", 100, (600, 500), 5, self.textury[4], self.textury[5])

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
