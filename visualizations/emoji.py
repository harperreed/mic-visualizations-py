import pygame
import random

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
        self.font = pygame.font.SysFont('segoe ui emoji', min(self.cell_width, self.cell_height))

    def update(self, fft_data):
        fft_chunks = numpy.array_split(fft_data, self.rows * self.cols)
        for i, chunk in enumerate(fft_chunks):
            if numpy.mean(chunk) > 0.5:  # You can adjust this threshold
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
    # Create the emoji grid if it doesn't exist
    if not hasattr(draw, 'emoji_grid'):
        draw.emoji_grid = EmojiGrid(width, height, rows=10, cols=20)
    
    # Update and draw the emoji grid
    draw.emoji_grid.update(fft_data)
    draw.emoji_grid.draw(screen)
