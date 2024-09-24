import pygame
from dotenv import load_dotenv
import os
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


# Load environment variables
load_dotenv()

# Screen settings
print(os.getenv('FULLSCREEN', 'True'))
FULLSCREEN = os.getenv('FULLSCREEN', 'True').lower() == 'true'
print(FULLSCREEN)

WIDTH = int(os.getenv('WIDTH', 1920))
HEIGHT = int(os.getenv('HEIGHT', 1080))

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

CLOCK_BOUNCE_SPEED = int(os.getenv('CLOCK_BOUNCE_SPEED', 10))

RTSP_CUBE_BOUNCE_SPEED = int(os.getenv('RTSP_CUBE_BOUNCE_SPEED', 10))

TOP_SCROLL_SPEED = int(os.getenv('TOP_SCROLL_SPEED', 20))
TOP_SCROLL_FONT_SIZE = int(os.getenv('TOP_SCROLL_FONT_SIZE', 180))

BOTTOM_SCROLL_SPEED = int(os.getenv('BOTTOM_SCROLL_SPEED', 8))

CUBE_SPEED_X = float(os.getenv('CUBE_SPEED_X', 2))
CUBE_SPEED_Y = float(os.getenv('CUBE_SPEED_Y', 2))

# Initialize Pygame
pygame.init()
pygame.font.init()


if FULLSCREEN:
    infoObject = pygame.display.Info()
    WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h
    logging.debug(f"Setting fullscreen mode: {WIDTH}x{HEIGHT}")
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
else:
    logging.debug(f"Setting windowed mode: {WIDTH}x{HEIGHT}")
    screen = pygame.display.set_mode((int(WIDTH), int(HEIGHT)))

logging.debug("Display mode set successfully")

pygame.display.set_caption("ProjectM-style Music Visualizer")
