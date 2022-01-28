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
        if (self.x - self.radius < 0) or (self.x + self.radius > WIDTH) or (self.y - self.radius < 0) \
                or (self.y + self.radius > HEIGTH):
            self.new()

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.match()
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)


class Star3d:
    def __init__(self, screen):
        self.screen = screen
        self.x, self.y, self.z = random.randint(-HALF_WIDTH, HALF_WIDTH), random.randint(-HALF_HEIGHT, HALF_HEIGHT), random.randint(2, MAX_DEPTH)
        while (self.x == 0) and (self.y == 0):
            self.x, self.y = random.randint(-HALF_WIDTH, HALF_WIDTH), random.randint(-HALF_HEIGHT, HALF_HEIGHT)
        self.color = pygame.color.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.radius = random.randint(1, MAX_RADIUS)

    def new(self):
        self.x, self.y, self.z = random.randint(-HALF_WIDTH, HALF_WIDTH), random.randint(-HALF_HEIGHT, HALF_HEIGHT), MAX_DEPTH
        while (self.x == 0) and (self.y == 0):
            self.x, self.y = random.randint(-HALF_WIDTH, HALF_WIDTH), random.randint(-HALF_HEIGHT, HALF_HEIGHT)
        self.radius = random.randint(1, MAX_RADIUS)

    def match(self):
        self.z -= 1
        ratio = MAX_DEPTH // self.z
        curr_x = self.x * ratio + WIDTH
        curr_y = self.y * ratio + HEIGHT
        curr_radius = self.radius * ratio
        if (curr_x < 0) or (curr_x > WIDTH) or (curr_y < 0) or (curr_y > HEIGHT) or (self.x < 2):
            self.new()
            return self.x, self.y, self.radius
        return curr_x, curr_y, curr_radius

    def update(self):
        x, y, radius = self.match()
        pygame.draw.circle(self.screen, self.color, (x, y), radius)


