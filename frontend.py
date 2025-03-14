from operator import truediv

import pygame

pygame.init()
screen = pygame.display.set_mode(1280, 720)
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #fill the screen with a color to wipe away anything from last frame
    screen.fill('white')

    #render game here

    #flip display puts work on screen
    pygame.display.flip()

    #limit fps to 60
    clock.tick(60)

pygame.quit()