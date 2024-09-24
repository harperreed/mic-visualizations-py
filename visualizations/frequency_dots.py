import pygame
import random

def draw(screen, fft_data, width, height):
    num_dots = 100
    dot_size = 4
    for i in range(num_dots):
        x = random.randint(0, width)
        y = random.randint(0, height)
        index = int(i * len(fft_data) / num_dots)
        intensity = int(fft_data[index] * 255)
        color = (intensity, intensity, 255)  # Blue-white color scheme
        size = int(dot_size + fft_data[index] * 10)
        pygame.draw.circle(screen, color, (x, y), size)
