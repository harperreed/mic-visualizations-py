import pygame
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

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

RTSP_STREAMS = [
                os.getenv('RTSP_URL_1'),
                os.getenv('RTSP_URL_2'),
                os.getenv('RTSP_URL_3'),
                os.getenv('RTSP_URL_4'),
                os.getenv('RTSP_URL_5'),
                os.getenv('RTSP_URL_6')
            ]


CLOCK_BOUNCE_SPEED = 10

RTSP_CUBE_BOUNCE_SPEED = 10

TOP_SCROLL_SPEED = 2
BOTTOM_SCROLL_SPEED = 8

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
