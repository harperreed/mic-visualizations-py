import pygame
import random
import numpy as np
import math
import os

# Define a list of emojis to use
EMOJIS = ['😀', '😎', '🎵', '🎶', '🔊', '💥', '✨', '🌈', '🔥', '💖']

class SpiralEmojiVisualizer:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.center_x = width // 2
        self.center_y = height // 2
        self.max_radius = min(width, height) // 2
        self.num_emojis = 100
        self.emojis = [random.choice(EMOJIS) for _ in range(self.num_emojis)]
        self.font = self.load_emoji_font()

    def load_emoji_font(self):
        font_paths = [
            "/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf",  # Linux (Noto Color Emoji)
            "segoe ui emoji",  # Windows
            "/System/Library/Fonts/Apple Color Emoji.ttc",  # macOS
        ]
        
        for font_path in font_paths:
            if os.path.exists(font_path):
                return pygame.font.Font(font_path, 24)  # Adjust size as needed
            elif pygame.font.match_font(font_path):
                return pygame.font.SysFont(font_path, 24)  # Adjust size as needed
        
        print("Warning: No emoji font found. Emojis may not display correctly.")
        return pygame.font.Font(None, 24)

    def update(self, fft_data):
        if len(fft_data) == 0 or np.isnan(fft_data).any() or np.isinf(fft_data).any():
            return

        fft_data = np.clip(fft_data, 0, 1)
        fft_chunks = np.array_split(fft_data, self.num_emojis)
        
        for i, chunk in enumerate(fft_chunks):
            if np.mean(chunk) > 0.5:  # Adjust threshold as needed
                self.emojis[i] = random.choice(EMOJIS)

    def draw(self, screen):
        for i in range(self.num_emojis):
            angle = 10 * 2 * math.pi * i / self.num_emojis
            radius = (i / self.num_emojis) * self.max_radius
            x = int(self.center_x + radius * math.cos(angle))
            y = int(self.center_y + radius * math.sin(angle))
            
            emoji = self.emojis[i]
            text = self.font.render(emoji, True, (255, 255, 255))
            text_rect = text.get_rect(center=(x, y))
            screen.blit(text, text_rect)

def draw(screen, fft_data, width, height):
    if not hasattr(draw, 'visualizer'):
        draw.visualizer = SpiralEmojiVisualizer(width, height)
    
    draw.visualizer.update(fft_data)
    draw.visualizer.draw(screen)