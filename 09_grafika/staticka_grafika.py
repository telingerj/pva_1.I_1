import pygame

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((800, 800))

def draw_shapes():
    """
    pygame.draw.line(screen, (255, 0, 0), (100, 100), (200, 100), 5)
    pygame.draw.line(screen, (255, 0, 0), (200, 100), (200, 200), 5)
    pygame.draw.line(screen, (255, 0, 0), (200, 200), (100, 200), 5)
    pygame.draw.line(screen, (255, 0, 0), (100, 200), (100, 100), 5)
    pygame.draw.line(screen, (255, 0, 0), (100, 100), (150, 80), 5)
    pygame.draw.line(screen, (255, 0, 0), (150, 80), (200, 100), 5)
    pygame.draw.line(screen, (255, 0, 0), (100, 100), (200, 200), 5)
    pygame.draw.line(screen, (255, 0, 0), (100, 200), (200, 100), 5)
    """
    pygame.draw.rect(screen, (0, 255, 0), (100, 100, 150, 100), 1)
    pygame.draw.circle(screen, (0, 0, 255), (100, 300), 50, 1)
    pygame.draw.polygon(screen, (255, 0, 0),
        [(300, 300), (350, 400), (400, 380), (450, 200), (350, 350)], 1)


def snowman():
    pygame.draw.rect(screen, (255, 255, 255), (0, 700, 800, 800))
    # zem
    pygame.draw.circle(screen, (255, 255, 255), (400, 600), 100)
    pygame.draw.circle(screen, (255, 255, 255), (400, 450), 70)
    pygame.draw.circle(screen, (255, 255, 255), (400, 350), 50)
    # tělo
    pygame.draw.circle(screen, (0, 0, 0), (375, 325), 7)
    pygame.draw.circle(screen, (0, 0, 0), (425, 325), 7)
    # oči
    pygame.draw.polygon(screen, (255, 183, 0), [(400, 340), (400, 360), (440, 350)])
    # nos
    for y in range(400, 700, 50):
        pygame.draw.circle(screen, (0, 0, 0), (400, y), 7)
    # knoflíky
    pygame.draw.line(screen, (0, 0, 0), (470, 450), (570, 450), 5)
    pygame.draw.line(screen, (0, 0, 0), (550, 450), (570, 440), 5)
    pygame.draw.line(screen, (0, 0, 0), (550, 450), (570, 460), 5)
    # pravá ruka
    pygame.draw.line(screen, (0, 0, 0), (330, 450), (230, 450), 5)
    pygame.draw.line(screen, (0, 0, 0), (250, 450), (230, 440), 5)
    pygame.draw.line(screen, (0, 0, 0), (250, 450), (230, 460), 5)
    # levá ruka
    pygame.draw.rect(screen, (115, 0, 0), (350, 260, 100, 50))
    pygame.draw.circle(screen, (110, 0, 0), (450, 285), 20, 5)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((166, 255, 251))
    snowman()
    clock.tick(60)
    pygame.display.flip()

pygame.quit()
