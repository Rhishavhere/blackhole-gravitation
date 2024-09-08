# Prev Rotation Logic :

```
if dist > black_hole.radius:
  force = 300 / (dist**1.4)  # Adjusted force calculation
  self.vx += force * dx / dist #fx
  self.vy += force * dy / dist #fy

  # Apply a rotation force to create an orbit-like effect

  rotation_force = 0.01 / (dist + 0.1)
  self.vx += rotation_force * -dy
  self.vy += rotation_force * dx
  
  self.x += self.vx
  self.y += self.vy

```

# Replenish Logic

```
# Update and draw particles
    particles = [p for p in particles if not p.is_off_screen()]
    for particle in particles:
        particle.update(black_hole)
        particle.draw(screen, black_hole)

    # Replenish particles
    while len(particles) < 10000:
        new_particle = Particle(random.randint(0, WIDTH), random.randint(0, HEIGHT))
        particles.append(new_particle)
```

# Off-Screen logic

```
def is_off_screen(self):
        return self.x < -1000 or self.x > WIDTH + 1000 or self.y < -1000 or self.y > HEIGHT + 1000
```