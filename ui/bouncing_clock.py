import pygame
from datetime import datetime
import config

class BouncingClock:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)
        self.color = config.CLOCK_COLOR
        self.x = config.WIDTH // 2
        self.y = config.HEIGHT // 2
        self.dx = 2
        self.dy = 2

    def update(self):
        self.x += self.dx
        self.y += self.dy

        text = self.font.render(datetime.now().strftime("%H:%M:%S"), True, self.color)
        text_rect = text.get_rect()

        if self.x <= 0 or self.x + text_rect.width >= config.WIDTH:
            self.dx *= -1
        if self.y <= 0 or self.y + text_rect.height >= config.HEIGHT:
            self.dy *= -1

    def draw(self, screen):
        current_time = datetime.now().strftime("%H:%M:%S")
        text = self.font.render(current_time, True, self.color)
        screen.blit(text, (self.x, self.y))