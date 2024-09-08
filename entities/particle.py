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
        
        # if dist > black_hole.radius:
        #     force = 300 / (dist**1.4)  # Adjusted force calculation
        #     self.vx += force * dx / dist #fx
        #     self.vy += force * dy / dist #fy

        # # Apply a rotation force to create an orbit-like effect
        # rotation_force = 0.01 / (dist + 0.1)
        # self.vx += rotation_force * -dy
        # self.vy += rotation_force * dx
        
        # self.x += self.vx
        # self.y += self.vy


        if dist > black_hole.radius:
            force = 1000 / (dist**1.5)  # Adjusted force calculation for stronger pull
            angle = math.atan2(dy, dx)
            
            # Tangential component for orbital motion
            tangential_force = force * 0.3
            self.vx += force * math.cos(angle) - tangential_force * math.sin(angle)
            self.vy += force * math.sin(angle) + tangential_force * math.cos(angle)
            
            # Limit velocity for stability
            speed = math.sqrt(self.vx**2 + self.vy**2)
            max_speed = 8
            if speed > max_speed:
                self.vx = self.vx / speed * max_speed
                self.vy = self.vy / speed * max_speed
        
        self.x += self.vx
        self.y += self.vy
        


    def draw(self, screen):
        if 0 <= self.x < WIDTH and 0 <= self.y < HEIGHT:
            pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), 2)

    # def is_off_screen(self):
    #     return self.x < -1000 or self.x > WIDTH + 1000 or self.y < -1000 or self.y > HEIGHT + 1000