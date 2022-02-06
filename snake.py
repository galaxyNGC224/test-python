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
x, y = FIELD // 2, FIELD // 2
snake = [[x, y]]

length = 1
dx, dy = 1, 0
apple = [random.randrange(1, FIELD - 1), random.randrange(1, FIELD - 1)]
while snake[0] == apple:
    apple = [random.randrange(1, FIELD - 1), random.randrange(1, FIELD - 1)]

pygame.display.set_caption('Hallo')
clock = pygame.time.Clock()

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_UP) and (dy != 1):
                dx, dy = 0, -1
            if (event.key == pygame.K_DOWN) and (dy != -1):
                dx, dy = 0, 1
            if (event.key == pygame.K_LEFT) and (dx != 1):
                dx, dy = -1, 0
            if (event.key == pygame.K_RIGHT) and (dx != -1):
                dx, dy = 1, 0
    x += dx
    y += dy

    for i, j in snake:
        if (x == i) and (y == j):
            running = False

    if running and (x < 0 or x > FIELD or y < 0 or y > FIELD):
        running = False

    if apple == [x, y]:
        length += 1
        apple = [random.randrange(1, FIELD - 1), random.randrange(1, FIELD - 1)]
        #FPS += 1
    snake.append([x, y])
    snake = snake[-length:]

    [pygame.draw.rect(screen, GREEN, (i * TILE, j * TILE, TILE - BORDER, TILE - BORDER)) for i in range(FIELD) for j in range(FIELD)]
    [pygame.draw.rect(screen, RED, (i * TILE, j * TILE, TILE - BORDER, TILE - BORDER)) for i, j in snake]
    pygame.draw.rect(screen, BLUE, (apple[0] * TILE, apple[1] * TILE, TILE - BORDER, TILE - BORDER))

    pygame.display.flip()

    clock.tick(FPS)
    screen.fill(BLACK)

pygame.quit()
