import random
import pygame
import math
from settings import *

class Star2d:
    def __init__(self, screen):
        self.screen = screen
        self.x, self.y = random.randint(0, WIDTH), random.randint(0, HEIGHT)
        self.speed_x, self.speed_y = random.randint(1, MAX_SPEED), 0
        self.radius = random.randint(1, MAX_RADIUS)
        self.color = pygame.color.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def new(self):
        self.x, self.y = 0, random.randint(0, HEIGHT)
        self.speed_x, self.speed_y = random.randint(1, MAX_SPEED), 0
        self.radius = random.randint(1, MAX_RADIUS)
        self.color = pygame.color.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def match(self):
        if (self.x - self.radius < 0) or (self.x + self.radius > WIDTH) or (self.y - self.radius < 0) \
                or (self.y + self.radius > HEIGHT):
            self.new()

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.match()
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

class Star3d:
    def __init__(self, screen):
        self.screen = screen
        self.x, self.y, self.z = random.randint(0, WIDTH), random.randint(0, HEIGHT), random.randint(2, MAX_DEPTH)
        self.color = pygame.color.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.radius = random.randint(1, MAX_RADIUS)
        self.distance = math.sqrt((self.x - CENTER_X) ** 2 + (self.y - CENTER_Y) ** 2)
        self.curr_x, self.curr_y, self.curr_radius = 0, 0, 0

    def new(self):
        self.x, self.y, self.z = random.randint(0, WIDTH), random.randint(0, HEIGHT), MAX_DEPTH
        self.radius = random.randint(1, MAX_RADIUS)
        self.distance = math.sqrt((self.x - CENTER_X) ** 2 + (self.y - CENTER_Y) ** 2)

    def move(self):
        self.z -= 1
        ratio = MAX_DEPTH / self.z
        self.curr_x = int((self.x - CENTER_X) * ratio) + CENTER_X
        self.curr_y = int((self.y - CENTER_Y) * ratio) + CENTER_Y
        self.curr_radius = int(self.radius * ratio)
        if (self.curr_x < 0) or (self.curr_x > WIDTH) or (self.curr_y < 0) or (self.curr_y > HEIGHT) or (self.x < 2):
            self.new()
            self.curr_x = int((self.x - CENTER_X) * ratio) + CENTER_X
            self.curr_y = int((self.y - CENTER_Y) * ratio) + CENTER_Y
        self.distance = math.sqrt((self.x - CENTER_X) ** 2 + (self.y - CENTER_Y) ** 2)

    def update(self):
        pygame.draw.circle(self.screen, self.color, (self.curr_x, self.curr_y), self.curr_radius)
