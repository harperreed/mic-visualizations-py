import pygame
import random
import math

particles = []

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random.randint(2, 6)
        self.color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
        self.speed = random.uniform(0.5, 2)
        self.angle = random.uniform(0, 2 * math.pi)

    def move(self, intensity):
        self.x += math.cos(self.angle) * self.speed * intensity
        self.y += math.sin(self.angle) * self.speed * intensity
        self.angle += random.uniform(-0.1, 0.1)

def draw(screen, fft_data, width, height):
    global particles
    
    if len(particles) < 200:
        particles.append(Particle(random.randint(0, width), random.randint(0, height)))
    
    screen.fill((0, 0, 0, 10), special_flags=pygame.BLEND_RGBA_MULT)
    
    avg_intensity = sum(fft_data) / len(fft_data)
    
    for particle in particles:
        particle.move(1 + avg_intensity * 5)
        pygame.draw.circle(screen, particle.color, (int(particle.x), int(particle.y)), particle.size)
        
        if particle.x < 0 or particle.x > width or particle.y < 0 or particle.y > height:
            particles.remove(particle)
            particles.append(Particle(random.randint(0, width), random.randint(0, height)))
