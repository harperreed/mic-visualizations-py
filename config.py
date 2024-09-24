import pygame
from dotenv import load_dotenv
import os
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


# Load environment variables
load_dotenv()

# Screen settings

FULLSCREEN = os.getenv('FULLSCREEN', 'True').lower() == 'true'

# Color settings
BACKGROUND_COLOR = (0, 0, 0)


# Audio settings
CHUNK = int(os.getenv('NUM_PARTICLES', 1024))
CHANNELS = int(os.getenv('NUM_PARTICLES', 1))
RATE = int(os.getenv('RATE', 44100))
FREQ_RANGE = (int(os.getenv('FREQ_RANGE_START', 50)), int(os.getenv('FREQ_RANGE_END', 1000)))

# Visualization settings
NUM_PARTICLES = int(os.getenv('NUM_PARTICLES', 100))
MODE_SWITCH_TIME = int(os.getenv('MODE_SWITCH_TIME', 10000))  # milliseconds

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
CLOCK_TIME_FORMAT = os.getenv('CLOCK_TIME_FORMAT', "%-I:%M %p")
CLOCK_FONT_SIZE = int(os.getenv('CLOCK_BOUNCE_FONT_SIZE', 120))
CLOCK_COLOR = (255, 255, 255)
CLOCK_COLORS = [
    (255, 0, 0),    # Red
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    (255, 255, 0),  # Yellow
    (255, 0, 255),  # Magenta
    (0, 255, 255),  # Cyan
    (255, 128, 0),  # Orange
    (128, 0, 255),  # Purple
    (0, 128, 128),  # Teal
    (255, 192, 203),# Pink
    (128, 128, 0),  # Olive
    (139, 69, 19),  # Saddle Brown
    (0, 191, 255),  # Deep Sky Blue
    (255, 215, 0),  # Gold
    (50, 205, 50),  # Lime Green
]

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
else:
    WIDTH = int(os.getenv('WIDTH', 1920))
    HEIGHT = int(os.getenv('HEIGHT', 1080))
