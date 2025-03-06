import pygame

pygame.init()
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            WIDTH, HEIGHT = event.w, event.h
            screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        #elif event.type == pygame.VIDEOEXPOSE:
        #    screen.fill('white')
        #    pygame.display.flip()

    #fill the screen with a color to wipe away anything from last frame
    screen.fill('white')

    #render game here
    pygame.draw.rect(screen, ('green'), (HEIGHT//4, HEIGHT//4, WIDTH//2, WIDTH//2))

    #flip display puts work on screen
    pygame.display.flip()

    #limit fps to 60
    clock.tick(60)

pygame.quit()
