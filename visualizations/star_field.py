import pygame
import random
import math

class Star:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

def draw(screen, fft_data, width, height):
    # Initialize stars if not already done
    if not hasattr(draw, "stars"):
        draw.stars = [Star(random.randint(-width, width), 
                           random.randint(-height, height), 
                           random.randint(1, width)) 
                      for _ in range(200)]

    screen.fill((0, 0, 0))
    
    # Use FFT data to determine speed and color
    avg_intensity = sum(fft_data) / len(fft_data)
    speed = 5 + avg_intensity * 20
    color_intensity = int(200 + avg_intensity * 55)
    
    for star in draw.stars:
        # Move stars closer to viewer
        star.z -= speed
        
        # Reset star if it's too close
        if star.z <= 0:
            star.x = random.randint(-width, width)
            star.y = random.randint(-height, height)
            star.z = width
        
        # Project star onto screen
        factor = 200.0 / star.z
        x = int(star.x * factor + width / 2)
        y = int(star.y * factor + height / 2)
        
        # Draw star if it's on screen
        if 0 <= x < width and 0 <= y < height:
            size = int((1 - float(star.z) / width) * 5)
            pygame.draw.circle(screen, (color_intensity, color_intensity, color_intensity), (x, y), size)

    # Draw "warp" lines
    num_lines = 20
    for i in range(num_lines):
        angle = 2 * math.pi * i / num_lines
        end_x = int(width / 2 + math.cos(angle) * width / 2)
        end_y = int(height / 2 + math.sin(angle) * height / 2)
        line_intensity = int(fft_data[int(i * len(fft_data) / num_lines)] * 255)
        pygame.draw.line(screen, (line_intensity, line_intensity, line_intensity), 
                         (width // 2, height // 2), (end_x, end_y), 1)