import pygame
import random

TILE = 20
FIELD = 30
SIZE = FIELD * TILE
BORDER = 2

FPS = 5

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
screen = pygame.display.set_mode((SIZE, SIZE))
x, y = random.randrange(0, FIELD), random.randrange(0, FIELD)
snake = [[x, y]]

length = 1
dx, dy = 1, 0
apple = [random.randrange(0, FIELD), random.randrange(0, FIELD)]
while snake[0] == apple:
    apple = [random.randrange(0, FIELD), random.randrange(0, FIELD)]

pygame.display.set_caption('Hallo')
clock = pygame.time.Clock()

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            pass

    x += dx
    y += dy
    snake.append([x, y])
    snake = snake[length:]

    [pygame.draw.rect(screen, RED, (i * TILE, j * TILE, TILE - BORDER, TILE - BORDER)) for i, j in snake]
    pygame.draw.rect(screen, GREEN, (apple[0] * TILE, apple[1] * TILE, TILE - BORDER, TILE - BORDER))

    pygame.display.flip()

    clock.tick(FPS)
    screen.fill(BLACK)

pygame.quit()
