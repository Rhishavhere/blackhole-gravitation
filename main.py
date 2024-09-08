import pygame
import random
import math

from config import *

from entities.blackhole import BlackHole
from entities.particle import Particle

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Black Hole Gravity Simulation")


# Create particles and black hole
particles = [Particle(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(1000)]
black_hole = BlackHole(WIDTH // 2, HEIGHT // 2, 150)

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update black hole position to mouse
    mouse_pos = pygame.mouse.get_pos()
    black_hole.update(mouse_pos)

    # Clear the screen
    screen.fill(BLACK)

    # Update and draw particles
    particles = [p for p in particles if not p.is_off_screen()]
    for particle in particles:
        particle.update(black_hole)
        particle.draw(screen)

    # Replenish particles
    while len(particles) < 10000:
        new_particle = Particle(random.randint(0, WIDTH), random.randint(0, HEIGHT))
        particles.append(new_particle)

    # Draw black hole
    black_hole.draw(screen)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()