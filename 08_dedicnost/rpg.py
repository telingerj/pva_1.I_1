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
    def __init__(self, jmeno, zivot, pozice):
        self.jmeno = jmeno
        self.zivot = zivot
        self.pozice = pozice
        self.armada = None


    def pridej_armadu(self, armada):
        self.armada = armada


    def uber_zivot(self, zivoty):
        self.zivot -= zivoty


class Bojovnik(Postava):
    def __init__(self, jmeno, zivot, pozice, poskozeni):
        super().__init__(jmeno, zivot, pozice)
        self.poskozeni = poskozeni


    def utok(self, postava):
        pass


class Lucistnik(Bojovnik):
    def __init__(self, jmeno, zivot, pozice, poskozeni, pocet_sipu):
        super().__init__(jmeno, zivot, pozice, poskozeni)
        self.pocet_sipu = pocet_sipu


    def utok(self, postava):
        self.pocet_sipu -= 1
        postava.uber_zivot(self.poskozeni)


class Sermir(Bojovnik):
    def __init__(self, jmeno, zivot, pozice, poskozeni, ucinnost_stitu):
        super().__init__(jmeno, zivot, pozice, poskozeni)
        self.ucinnost_stitu = ucinnost_stitu


    def utok(self, postava):
        postava.uber_zivot(self.poskozeni)


    def uber_zivot(self, zivoty):
        if random.randint(1, 100) <= self.ucinnost_stitu:
            self.ucinnost_stitu *= 0.9
            return
        self.zivot -= zivoty


class Kouzelnik(Postava):
    def __init__(self, jmeno, zivot, pozice, uzdraveni):
        super().__init__(jmeno, zivot, pozice)
        self.uzdraveni = uzdraveni


    def uzdrav(self, postava):
        postava.zivot += self.uzdraveni

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 800))
        self.clock = pygame.time.Clock()
        self.running = True

    def loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((255, 255, 255))
            self.clock.tick(60)
            pygame.display.flip()


game = Game()
game.loop()
