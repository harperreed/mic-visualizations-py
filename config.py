import pygame
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Screen settings
FULLSCREEN = os.getenv('FULLSCREEN', True)
WIDTH = os.getenv('WIDTH', 1920)
HEIGHT = os.getenv('HEIGHT', 1080)

# Color settings
BACKGROUND_COLOR = (0, 0, 0)
CLOCK_COLOR = (255, 255, 255)

# Audio settings
CHUNK = os.getenv('NUM_PARTICLES', 1024)
CHANNELS = os.getenv('NUM_PARTICLES', 1)
RATE = os.getenv('RATE', 44100)
FREQ_RANGE = (os.getenv('FREQ_RANGE_START', 50), os.getenv('FREQ_RANGE_END', 1000))

# Visualization settings
NUM_PARTICLES = os.getenv('NUM_PARTICLES', 100)
MODE_SWITCH_TIME = os.getenv('MODE_SWITCH_TIME', 5000)  # milliseconds

RTSP_STREAMS = [
                os.getenv('RTSP_URL_1'),
                os.getenv('RTSP_URL_2'),
                os.getenv('RTSP_URL_3'),
                os.getenv('RTSP_URL_4'),
                os.getenv('RTSP_URL_5'),
                os.getenv('RTSP_URL_6')
            ]


# Add this new configuration
RSS_FEED_URLS = os.getenv('RSS_FEED_URLS',"").split("|")
print(RSS_FEED_URLS)

CLOCK_BOUNCE_SPEED = 10

RTSP_CUBE_BOUNCE_SPEED = os.getenv('RTSP_CUBE_BOUNCE_SPEED', 10)

TOP_SCROLL_SPEED = os.getenv('RTSP_CUBE_BOUNCE_SPEED', 2)
BOTTOM_SCROLL_SPEED = os.getenv('RTSP_CUBE_BOUNCE_SPEED', 8)

CUBE_SPEED_X = float(os.getenv('CUBE_SPEED_X', 2))
CUBE_SPEED_Y = float(os.getenv('CUBE_SPEED_Y', 2))

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
