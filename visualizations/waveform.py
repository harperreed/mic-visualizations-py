import pygame
import numpy as np

def draw(screen, fft_data, width, height):
    # Ensure we have data to work with
    if len(fft_data) == 0:
        return

    # Normalize the FFT data
    normalized_fft = np.array(fft_data) / np.max(fft_data)
    
    # Calculate parameters
    num_bars = min(len(fft_data), width // 2)  # Ensure we don't exceed screen width
    bar_width = width / num_bars
    max_height = height * 0.8  # Use 80% of the screen height for the visualization
    
    # Draw the spectrum analyzer
    for i in range(num_bars):
        bar_height = int(normalized_fft[i] * max_height)
        x = int(i * bar_width)
        y = height - bar_height  # Draw from bottom up
        
        # Create a gradient color based on frequency
        color = pygame.Color(0)
        hue = int(180 * i / num_bars)  # Use half the color wheel for a blue-to-red gradient
        color.hsva = (hue, 100, 100, 100)
        
        pygame.draw.rect(screen, color, (x, y, int(bar_width) - 1, bar_height))
    
    # Draw a line connecting the tops of the bars for a "waveform" effect
    points = [(int(i * bar_width), height - int(normalized_fft[i] * max_height)) for i in range(num_bars)]
    pygame.draw.lines(screen, (255, 255, 255), False, points, 2)
