import pygame
import random
from settings import *

class Track:
    def __init__(self, screen):
        self.screen = screen
        self.rect = pygame.Rect(100, 100, 200, 100)
        self.z = MAX_DEPTH - 1
        self.pos_x1, self.pos_y1 = 0, 0

    def update(self):
        self.z -= 1
        if self.z < 1:
            self.z = MAX_DEPTH - 1
        ratio = MAX_DEPTH / self.z
        self.pos_x = (self.x - CENTER_X) * ratio + CENTER_X
        self.pos_y = (self.y - CENTER_Y) * ratio + CENTER_Y

    def draw(self):
        rect = pygame.Rect(1, 2, 5, 6)
        rect.






