import random
import pygame
from settings import *


class Star2d:
    def __init__(self, screen):
        self.screen = screen
        self.x, self.y = random.randint(0, WIDTH), random.randint(0, HEIGTH)
        self.speed_x, self.speed_y = random.randint(1, MAX_SPEED), 0
        self.radius = random.randint(1, MAX_RADIUS)
        self.color = pygame.color.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def new(self):
        self.x, self.y = 0, random.randint(0, HEIGTH)
        self.speed_x, self.speed_y = random.randint(1, MAX_SPEED), 0
        self.radius = random.randint(1, MAX_RADIUS)
        self.color = pygame.color.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def match(self):
        if (self.x < 0) or (self.x > WIDTH) or (self.y < 0) or (self.y > HEIGTH):
            self.new()

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.match()
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)


class Star3d:
    def __init__(self, screen):
        self.screen = screen
        self.x, self.y, self.z = random.randint(-WIDTH, WIDTH), random.randint(-HEIGTH, HEIGTH), \
                                 random.randint(1, MAX_DEPTH)
        self.color = pygame.color.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def new(self):
        pass

    def match(self):
        pass

    def update(self):
        pass
