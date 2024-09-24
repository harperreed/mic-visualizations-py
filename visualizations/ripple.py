import pygame
import math
import random

class Ripple:
    def __init__(self, x, y, color, max_radius):
        self.x = x
        self.y = y
        self.color = color
        self.radius = 0
        self.max_radius = max_radius
        self.speed = 2

    def update(self):
        self.radius += self.speed
        return self.radius <= self.max_radius

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), int(self.radius), 2)

ripples = []

def draw(screen, fft_data, width, height):
    screen.fill((0, 0, 0))
    
    # Create new ripples based on FFT data
    num_bands = 5
    band_size = len(fft_data) // num_bands
    for i in range(num_bands):
        band_avg = sum(fft_data[i*band_size:(i+1)*band_size]) / band_size
        if band_avg > 0.1:  # Threshold to create a new ripple
            x = int(width * (i + 0.5) / num_bands)
            y = random.randint(height // 4, 3 * height // 4)
            hue = int(360 * i / num_bands)
            color = pygame.Color(0)
            color.hsva = (hue, 100, 100, 50)
            max_radius = int(band_avg * height / 2)
            ripples.append(Ripple(x, y, color, max_radius))
    
    # Update and draw ripples
    ripples[:] = [ripple for ripple in ripples if ripple.update()]
    for ripple in ripples:
        ripple.draw(screen)
    
    # Draw frequency bars
    bar_width = width // len(fft_data)
    for i, value in enumerate(fft_data):
        bar_height = int(value * height / 2)
        x = i * bar_width
        y = height - bar_height
        color = pygame.Color(0)
        hue = int(360 * i / len(fft_data))
        color.hsva = (hue, 100, 100, 50)
        pygame.draw.rect(screen, color, (x, y, bar_width, bar_height))