import pygame
import random
import numpy as np
import os

# Define a list of emojis to use
EMOJIS = ['😀', '😎', '🎵', '🎶', '🔊', '💥', '✨', '🌈', '🔥', '💖']

class EmojiGrid:
    def __init__(self, width, height, rows, cols):
        self.width = width
        self.height = height
        self.rows = rows
        self.cols = cols
        self.cell_width = width // cols
        self.cell_height = height // rows
        self.grid = [[random.choice(EMOJIS) for _ in range(cols)] for _ in range(rows)]
        self.font = self.load_emoji_font()

    def load_emoji_font(self):
        font_paths = [
            "/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf",  # Linux (Noto Color Emoji) - confirmed path
            "segoe ui emoji",  # Windows
            "/System/Library/Fonts/Apple Color Emoji.ttc",  # macOS
        ]
        
        for font_path in font_paths:
            if os.path.exists(font_path):
                return pygame.font.Font(font_path, min(self.cell_width, self.cell_height))
            elif pygame.font.match_font(font_path):
                return pygame.font.SysFont(font_path, min(self.cell_width, self.cell_height))
        
        print("Warning: No emoji font found. Emojis may not display correctly.")
        return pygame.font.Font(None, min(self.cell_width, self.cell_height))

    def update(self, fft_data):
        if len(fft_data) == 0 or np.isnan(fft_data).any() or np.isinf(fft_data).any():
            return  # Don't update if the data is invalid
        
        fft_data = np.clip(fft_data, 0, 1)  # Normalize data
        fft_chunks = np.array_split(fft_data, self.rows * self.cols)
        for i, chunk in enumerate(fft_chunks):
            if np.mean(chunk) > 0.5:  # You can adjust this threshold
                row = i // self.cols
                col = i % self.cols
                self.grid[row][col] = random.choice(EMOJIS)

    def draw(self, screen):
        for row in range(self.rows):
            for col in range(self.cols):
                x = col * self.cell_width
                y = row * self.cell_height
                emoji = self.grid[row][col]
                text = self.font.render(emoji, True, (255, 255, 255))
                text_rect = text.get_rect(center=(x + self.cell_width // 2, y + self.cell_height // 2))
                screen.blit(text, text_rect)

def draw(screen, fft_data, width, height):
    if not hasattr(draw, 'emoji_grid'):
        draw.emoji_grid = EmojiGrid(width, height, rows=10, cols=20)
    
    draw.emoji_grid.update(fft_data)
    draw.emoji_grid.draw(screen)