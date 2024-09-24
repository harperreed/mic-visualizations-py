import pygame

# Screen settings
FULLSCREEN = True
WIDTH = 1920
HEIGHT = 1080

# Color settings
BACKGROUND_COLOR = (0, 0, 0)
CLOCK_COLOR = (255, 255, 255)

# Audio settings
CHUNK = 1024
CHANNELS = 1
RATE = 44100
FREQ_RANGE = (50, 1000)

# Visualization settings
NUM_PARTICLES = 100
MODE_SWITCH_TIME = 5000  # milliseconds

# Initialize Pygame
pygame.init()
pygame.font.init()

if FULLSCREEN:
    infoObject = pygame.display.Info()
    WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("ProjectM-style Music Visualizer")
