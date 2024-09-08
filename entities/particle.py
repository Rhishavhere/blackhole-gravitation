import math
import random
import pygame
from config import *

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random.uniform(-0.5, 0.5)
        self.vy = random.uniform(-0.5, 0.5)

    def update(self, black_hole):
        dx = black_hole.x - self.x
        dy = black_hole.y - self.y
        dist = math.sqrt(dx**2 + dy**2)
        
        if dist > black_hole.radius:
            force = 500 / (dist**1.5)  # Adjusted force calculation
            self.vx += force * dx / dist
            self.vy += force * dy / dist
        
        self.x += self.vx
        self.y += self.vy

    def draw(self, screen):
        if 0 <= self.x < WIDTH and 0 <= self.y < HEIGHT:
            pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), 1)

    def is_off_screen(self):
        return self.x < -50 or self.x > WIDTH + 50 or self.y < -50 or self.y > HEIGHT + 50