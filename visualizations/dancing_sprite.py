import pygame
import math
import random

class SoundSprite:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.base_y = y
        self.size = 50
        self.color = (255, 255, 255)
        self.dance_phase = 0
        self.arms_phase = 0
        self.eyes_blink = 0

    def dance(self, intensity):
        self.dance_phase += 0.2 * intensity
        self.arms_phase += 0.3 * intensity
        self.y = self.base_y + math.sin(self.dance_phase) * 20 * intensity

        if random.random() < 0.02:
            self.eyes_blink = 5

        if self.eyes_blink > 0:
            self.eyes_blink -= 1

    def draw(self, screen):
        # Body
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)

        # Eyes
        eye_y = int(self.y - 10)
        if self.eyes_blink == 0:
            pygame.draw.circle(screen, (0, 0, 0), (int(self.x - 15), eye_y), 5)
            pygame.draw.circle(screen, (0, 0, 0), (int(self.x + 15), eye_y), 5)
        else:
            pygame.draw.line(screen, (0, 0, 0), (int(self.x - 20), eye_y), (int(self.x - 10), eye_y), 2)
            pygame.draw.line(screen, (0, 0, 0), (int(self.x + 10), eye_y), (int(self.x + 20), eye_y), 2)

        # Mouth
        mouth_y = int(self.y + 10)
        pygame.draw.arc(screen, (0, 0, 0), (int(self.x - 15), mouth_y - 5, 30, 20), math.pi, 2*math.pi, 2)

        # Arms
        left_arm_x = self.x - self.size - 10 + math.sin(self.arms_phase) * 20
        right_arm_x = self.x + self.size + 10 + math.sin(self.arms_phase + math.pi) * 20
        pygame.draw.line(screen, self.color, (int(self.x - self.size), int(self.y)), (int(left_arm_x), int(self.y)), 5)
        pygame.draw.line(screen, self.color, (int(self.x + self.size), int(self.y)), (int(right_arm_x), int(self.y)), 5)

def draw(screen, fft_data, width, height):
    # Initialize sprite if not already done
    if not hasattr(draw, "sprite"):
        draw.sprite = SoundSprite(width // 2, height // 2)

    screen.fill((0, 0, 0))  # Clear screen with black

    # Calculate average intensity from FFT data
    avg_intensity = sum(fft_data) / len(fft_data)

    # Make the sprite dance
    draw.sprite.dance(avg_intensity * 5)  # Amplify the effect

    # Draw the sprite
    draw.sprite.draw(screen)

    # Draw frequency bars in the background
    bar_width = width // len(fft_data)
    for i, value in enumerate(fft_data):
        bar_height = int(value * height / 2)
        x = i * bar_width
        y = height - bar_height
        color = pygame.Color(0)
        hue = int(360 * i / len(fft_data))
        color.hsva = (hue, 100, 100, 50)
        pygame.draw.rect(screen, color, (x, y, bar_width, bar_height))
