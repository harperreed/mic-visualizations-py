import pygame

def draw(screen, audio_data, width, height):
    points = []
    for i, sample in enumerate(audio_data):
        x = int(i * width / len(audio_data))
        y = int(height / 2 + (sample / 32768.0) * (height / 4))
        points.append((x, y))
    pygame.draw.lines(screen, (0, 255, 0), False, points, 2)

