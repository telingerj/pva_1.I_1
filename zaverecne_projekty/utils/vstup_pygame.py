import pygame

pygame.init()

screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:  # je stisknutá klávesa
            if event.key == pygame.K_LEFT:
                print("zmáčkl jsi doleva")
            elif event.key == pygame.K_RIGHT:
                print("zmáčkl jsi doprava")
            elif event.key == pygame.K_UP:
                print("zmáčkl jsi nahoru")
            elif event.key == pygame.K_DOWN:
                print("zmáčkl jsi dolu")

        if event.type == pygame.KEYUP:  # je uvolněná klávesa
            if event.key == pygame.K_LEFT:
                print("pustil jsi doleva")
            elif event.key == pygame.K_RIGHT:
                print("pustil jsi doprava")
            elif event.key == pygame.K_UP:
                print("pustil jsi nahoru")
            elif event.key == pygame.K_DOWN:
                print("pustil jsi dolu")


        if event.type == pygame.MOUSEBUTTONDOWN:  # kliknutí
            if event.button == pygame.BUTTON_LEFT:  # levým tlačítkem
                souradnice = pygame.mouse.get_pos()  # získáme pozici myši
                x = souradnice[0]
                y = souradnice[1]
                if y < 400:
                    print("horní polovina")
                else:
                    print("dolní polovina")





    clock.tick(60)
    screen.fill((255, 255, 255))
    pygame.display.flip()

#TODO: program, který reaguje na šipky
