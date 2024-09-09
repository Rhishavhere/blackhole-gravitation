import math
import random
import pygame

from config import *
from utils.color import *


class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random.uniform(-0.5, 0.5)
        self.vy = random.uniform(-0.5, 0.5)
        self.speed = 0
        self.max_speed = MAX_VELOCITY
        self.size = random.choice(PARTICLE_SIZE)

    def update(self, black_hole):
        dx = black_hole.x - self.x
        dy = black_hole.y - self.y
        dist = math.sqrt(dx**2 + dy**2)
        
        force = GRAVITATION_CONSTANT / (dist**FIELD_VARIATION)   # gravity

        if dist > black_hole.radius:
            angle = math.atan2(dy, dx)
            
            # Tangential components
            tangential_force = force * TANGENTIAL_FACTOR
            self.vx += force * math.cos(angle) - tangential_force * math.sin(angle)
            self.vy += force * math.sin(angle) + tangential_force * math.cos(angle)
            
            # Limiting velocity
            self.speed = math.sqrt(self.vx**2 + self.vy**2)
            speed=self.speed

            max_speed = self.max_speed

            if speed > max_speed:
                self.vx = self.vx / speed * max_speed
                self.vy = self.vy / speed * max_speed
        
        self.x += self.vx
        self.y += self.vy

        self.force=force
        

    def draw(self, screen, black_hole):
        
        if (COLOR_VARIATION == 1):
            color = get_color_based_on_force(self.force, 3)
        elif (COLOR_VARIATION == 2):
            color = get_color_based_on_speed(self.speed, self.max_speed) 
        else:
            color = WHITE

        dist = math.sqrt((self.x - black_hole.x)**2 + (self.y - black_hole.y)**2)
        
        if 0 <= self.x < WIDTH and 0 <= self.y < HEIGHT:
            pygame.draw.circle(screen, color, (int(self.x), int(self.y)), self.size)
