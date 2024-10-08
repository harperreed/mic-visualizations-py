import pygame
import random

class BottomScroller:
    def __init__(self, width, height, text, speed=8):
        self.width = width
        self.height = height
        self.text = text
        self.speed = speed
        self.max_speed = speed + 2
        self.current_speed = random.randint(speed, self.max_speed)
        
        self.font = pygame.font.Font(None, 120)
        self.text_surface = self.font.render(self.text, True, (255, 255, 255))
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.y = self.height - 90  # Position at the bottom
        self.text_rect.x = self.width

    def update(self, fft_data):
        # Move the text to the left
        self.text_rect.x -= self.current_speed

        # If the text has scrolled off the screen, reset its position
        if self.text_rect.right < 0:
            self.text_rect.x = self.width

        # Optional: Change color based on audio data
        if len(fft_data) > 0:
            intensity = int(max(fft_data) * 255)
            color = (intensity, intensity, 255)  # Blue to white
            self.text_surface = self.font.render(self.text, True, color)

    def draw(self, screen):
        screen.blit(self.text_surface, self.text_rect)
