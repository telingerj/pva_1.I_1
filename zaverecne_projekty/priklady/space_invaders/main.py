import pygame
import time

class Object:
    def __init__(self, x, y, texture):
        self.position = (x, y)
        self.texture = texture


    def draw(self, screen):
        screen.blit(self.texture, self.position)


class Enemy(Object):
    def __init__(self, x, y, texture):
        super().__init__(x, y, texture)


    def move(self):
        self.position = (self.position[0], self.position[1] + 0.3)


class Player(Object):
    def __init__(self, x, y, texture):
        super().__init__(x, y, texture)


    def move(self, move_vector):
        if self.position[0] <= 0 and move_vector[0] <= 0:
            return
        if self.position[0] >= 700 and move_vector[0] >= 0:
            return
        self.position = (self.position[0] + move_vector[0], self.position[1] + move_vector[1])


class Shot(Object):
    def __init__(self, x, y, texture):
        super().__init__(x, y, texture)


    def move(self):
        self.position = (self.position[0], self.position[1] - 10)


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        self.clock = pygame.time.Clock()
        self.running = True
        self.textures = []
        self.textures = self.load_textures()
        self.enemies = []
        self.spawn_enemies()
        self.player = self.create_player()
        self.move_keys = [False, False]
        self.shots = []
        self.last_enemies_spawn_time = time.time()



    def load_textures(self):
        t = []
        t.append(pygame.transform.scale(pygame.image.load("images/enemy.webp"), (100, 100)))
        t.append(pygame.transform.scale(pygame.image.load("images/player.png"), (100, 100)))
        t.append(pygame.transform.rotate(pygame.transform.scale(pygame.image.load("images/bullet.webp"), (20, 20)), 90))
        return t

    def spawn_enemies(self):
        for x in range(100, 700, 150):
            self.enemies.append(Enemy(x, 100, self.textures[0]))


    def create_player(self):
        return Player(350, 600, self.textures[1])


    def draw_objects(self):
        for e in self.enemies:
            e.draw(self.screen)
        for s in self.shots:
            s.draw(self.screen)
        self.player.draw(self.screen)


    def update_objects(self):
        self.move_player()
        self.move_enemies()
        self.move_shots()
        self.shot_enemies()
        if time.time() - self.last_enemies_spawn_time > 5:
            self.spawn_enemies()
            self.last_enemies_spawn_time = time.time()


    def move_player(self):
        if self.move_keys[0]:
            self.player.move((-3, 0))
        elif self.move_keys[1]:
            self.player.move((3, 0))


    def move_enemies(self):
        for e in self.enemies:
            e.move()

    def move_shots(self):
        for s in self.shots:
            s.move()
            if s.position[1] <= 0:
                self.shots.remove(s)


    def shoot(self):
        self.shots.append(Shot(self.player.position[0] + 40, self.player.position[1], self.textures[2]))


    def shot_enemies(self):
        for e in self.enemies:
            for s in self.shots:
                r1 = pygame.Rect(e.position[0], e.position[1], e.texture.get_width(), e.texture.get_height())
                r2 = pygame.Rect(s.position[0], s.position[1], s.texture.get_width(), s.texture.get_height())
                if r1.colliderect(r2):
                    self.enemies.remove(e)
                    self.shots.remove(s)


    def loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT or pygame.key == pygame.K_a:
                        self.move_keys[0] = True
                    elif event.key == pygame.K_RIGHT or pygame.key == pygame.K_d:
                        self.move_keys[1] = True
                    elif event.key == pygame.K_SPACE:
                        self.shoot()

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or pygame.key == pygame.K_a:
                        self.move_keys[0] = False
                    elif event.key == pygame.K_RIGHT or pygame.key == pygame.K_d:
                        self.move_keys[1] = False

            self.screen.fill((0, 0, 0))
            self.update_objects()
            self.draw_objects()
            pygame.display.flip()
            self.clock.tick(60)

game = Game()
game.loop()
