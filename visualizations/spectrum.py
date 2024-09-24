import pygame

def draw(screen, fft_data, width, height):
    num_bars = 100
    bar_width = width / num_bars
    for i in range(num_bars):
        index = int(i * len(fft_data) / num_bars)
        bar_height = fft_data[index] * height / 2
        x = i * bar_width
        y = height / 2 - bar_height / 2
        color = pygame.Color(0)
        hue = int(360 * i / num_bars)
        color.hsva = (hue, 100, 100, 50)
        pygame.draw.rect(screen, color, (x, y, bar_width - 1, bar_height))
