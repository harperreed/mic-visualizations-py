import pygame
from datetime import datetime
import config
import random

class BouncingClock:
    def __init__(self):
        self.font = pygame.font.Font(None, config.CLOCK_FONT_SIZE)
        self.colors = list(config.CLOCK_COLORS)  # Create a copy of the color list
        random.shuffle(self.colors)  # Shuffle the colors randomly
        self.color_index = 0  # Current color index
        self.x = config.WIDTH // 2
        self.y = config.HEIGHT // 2
        self.dx = config.CLOCK_BOUNCE_SPEED  # Increased speed
        self.dy = config.CLOCK_BOUNCE_SPEED  # Increased speed

    def update(self):
        self.x += self.dx
        self.y += self.dy

        text = self.font.render(datetime.now().strftime(config.CLOCK_TIME_FORMAT), True, self.colors[self.color_index])
        text_rect = text.get_rect()

        if self.x <= 0 or self.x + text_rect.width >= config.WIDTH:
            self.dx *= -1
            self.color_index = (self.color_index + 1) % len(self.colors)  # Change color on horizontal wall hit
        if self.y <= 0 or self.y + text_rect.height >= config.HEIGHT:
            self.dy *= -1
            self.color_index = (self.color_index + 1) % len(self.colors)  # Change color on vertical wall hit

    def draw(self, screen):
        current_time = datetime.now().strftime("%I:%M:%S %p")
        text = self.font.render(current_time, True, self.colors[self.color_index])
        screen.blit(text, (self.x, self.y))
