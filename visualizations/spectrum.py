import pygame
import numpy as np

def draw(screen, fft_data, width, height):
    num_bars = 100
    bar_width = width / num_bars
    
    # Ensure fft_data is not empty and contains valid values
    if len(fft_data) == 0 or np.isnan(fft_data).any() or np.isinf(fft_data).any():
        return  # Don't draw anything if the data is invalid
    
    # Normalize fft_data to avoid extreme values
    fft_data = np.clip(fft_data, 0, 1)
    
    for i in range(num_bars):
        index = int(i * len(fft_data) / num_bars)
        bar_height = max(1, int(fft_data[index] * height / 2))  # Ensure minimum height of 1
        x = int(i * bar_width)
        y = height // 2 - bar_height // 2
        color = pygame.Color(0)
        hue = int(360 * i / num_bars)
        color.hsva = (hue, 100, 100, 50)
        pygame.draw.rect(screen, color, (x, y, max(1, int(bar_width) - 1), bar_height))