import pygame
import math
from config import *

class BlackHole:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = BLACKHOLE_SIZE

    def update(self, mouse_pos):
        self.x, self.y = mouse_pos

    def draw(self, screen):
        pygame.draw.circle(screen, BLACK, (int(self.x), int(self.y)), self.radius)


# this is something