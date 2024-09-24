import pygame
import math

def draw(screen, fft_data, width, height):
    num_rings = 5
    center_x, center_y = width // 2, height // 2
    max_radius = min(width, height) // 3
    ring_width = max_radius // num_rings
    
    for ring in range(num_rings):
        start_index = int(ring * len(fft_data) / num_rings)
        end_index = int((ring + 1) * len(fft_data) / num_rings)
        ring_data = fft_data[start_index:end_index]
        avg_intensity = sum(ring_data) / len(ring_data)
        
        radius = (ring + 1) * ring_width + avg_intensity * ring_width
        thickness = int(2 + avg_intensity * 10)
        
        color = pygame.Color(0)
        hue = int(360 * ring / num_rings)
        color.hsva = (hue, 100, 100, 50)
        
        pygame.draw.circle(screen, color, (center_x, center_y), int(radius), thickness)
        
    # Draw connecting lines
    num_lines = 36
    for i in range(num_lines):
        angle = 2 * math.pi * i / num_lines
        x = int(center_x + max_radius * math.cos(angle))
        y = int(center_y + max_radius * math.sin(angle))
        intensity = fft_data[int(i * len(fft_data) / num_lines)]
        color = pygame.Color(255, 255, 255, int(intensity * 128))
        pygame.draw.line(screen, color, (center_x, center_y), (x, y), 1)
