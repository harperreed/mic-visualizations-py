import pygame
import random
import config

class Particle:
    def __init__(self):
        self.x = random.randint(0, config.WIDTH)
        self.y = random.randint(0, config.HEIGHT)
        self.size = random.randint(2, 5)
        self.color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
        self.speed = random.uniform(0.5, 2)

    def move(self):
        self.y -= self.speed
        if self.y < 0:
            self.y = config.HEIGHT

    def update(self, fft_data):
        self.move()
        self.size = int(self.size * (1 + fft_data[random.randint(0, len(fft_data)-1)] / 5))
        self.size = max(2, min(10, self.size))  # Clamp size

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.size)