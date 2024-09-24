import pygame
import math

def draw(screen, fft_data, width, height):
    num_bars = 100
    center_x, center_y = width // 2, height // 2
    max_radius = min(width, height) // 3
    bar_width = 2 * math.pi / num_bars
    
    for i in range(num_bars):
        angle = i * bar_width
        index = int(i * len(fft_data) / num_bars)
        bar_height = int(fft_data[index] * max_radius)
        start_radius = max_radius - bar_height
        end_radius = max_radius
        
        start_x = int(center_x + start_radius * math.cos(angle))
        start_y = int(center_y + start_radius * math.sin(angle))
        end_x = int(center_x + end_radius * math.cos(angle))
        end_y = int(center_y + end_radius * math.sin(angle))
        
        color = pygame.Color(0)
        hue = int(360 * i / num_bars)
        color.hsva = (hue, 100, 100, 50)
        
        pygame.draw.line(screen, color, (start_x, start_y), (end_x, end_y), 2)
