import pygame
import math

def draw(screen, fft_data, width, height):
    num_points = 100
    center_x, center_y = width // 2, height // 2
    max_radius = min(width, height) // 3
    for i in range(num_points):
        angle = 2 * math.pi * i / num_points
        index = int(i * len(fft_data) / num_points)
        radius = fft_data[index] * max_radius
        x = int(center_x + radius * math.cos(angle))
        y = int(center_y + radius * math.sin(angle))
        color = pygame.Color(0)
        hue = int(360 * i / num_points)
        color.hsva = (hue, 100, 100, 50)
        pygame.draw.line(screen, color, (center_x, center_y), (x, y), 2)
