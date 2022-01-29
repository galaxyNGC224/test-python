import pygame
from settings import *
from star import Star3d
from track import Track

pygame.init()

screen = pygame.display.set_mode((SIZE))

pygame.display.set_caption('Hallo')
clock = pygame.time.Clock()
stars = [Star3d(screen) for s in range(MAX_STARS)]
running = True
tracks = [Track(screen) for t in range(MAX_TRACKS)]

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLACK)

    [stars[s].update() for s in range(MAX_STARS)]

    pygame.display.flip()

pygame.quit()




