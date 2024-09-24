import pygame
import numpy as np
from PIL import Image, ImageDraw
import os
import re

class ImageWarper:
    def __init__(self, image_folder, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        # Set the size of the warped image to be 1/4 of the screen dimensions
        self.width = screen_width // 4
        self.height = screen_height // 4
        self.images = self.load_images(image_folder)
        self.current_image_index = 0
        self.frame_count = 0

    def load_images(self, folder):
        images = []
        frame_pattern = re.compile(r'frame(\d+)\.png')
        
        frame_files = sorted(
            [(int(frame_pattern.match(f).group(1)), f) for f in os.listdir(folder) if frame_pattern.match(f)],
            key=lambda x: x[0]
        )
        
        for _, filename in frame_files:
            img = Image.open(os.path.join(folder, filename)).convert('RGBA')
            img = img.resize((self.width, self.height), Image.LANCZOS)
            images.append(img)
        
        print(f"Loaded {len(images)} frame images.")
        return images

    def warp_image(self, image, fft_data):
        warped = Image.new('RGBA', (self.width, self.height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(warped)

        wave_amplitude = int(np.mean(fft_data) * self.height / 4)
        wave_frequency = 2 * np.pi / self.width

        for x in range(self.width):
            wave = int(wave_amplitude * np.sin(wave_frequency * x + self.frame_count * 0.1))
            slice_rect = (x, 0, x+1, self.height)
            slice_warped = (x, wave, x+1, self.height + wave)
            slice_img = image.crop(slice_rect)
            warped.paste(slice_img, slice_warped)

        return warped

    def get_next_frame(self, fft_data):
        original_image = self.images[self.current_image_index]
        warped_image = self.warp_image(original_image, fft_data)
        
        mode = warped_image.mode
        size = warped_image.size
        data = warped_image.tobytes()
        py_image = pygame.image.fromstring(data, size, mode)

        self.frame_count += 1
        if self.frame_count % 2 == 0:
            self.current_image_index = (self.current_image_index + 1) % len(self.images)

        return py_image

def draw(screen, fft_data, width, height):
    if not hasattr(draw, "warper"):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_folder = os.path.join(current_dir, "warped_folder")
        
        if not os.path.exists(image_folder):
            print(f"Error: The folder {image_folder} does not exist.")
            print("Please ensure the 'warped_folder' is in the same directory as this script.")
            return
        
        draw.warper = ImageWarper(image_folder, width, height)

    warped_frame = draw.warper.get_next_frame(fft_data)

    # Fill the screen with a dark color
    screen.fill((20, 20, 20))

    # Calculate position to center the warped frame
    x = (width - draw.warper.width) // 2
    y = (height - draw.warper.height) // 2

    # Draw the warped frame
    screen.blit(warped_frame, (x, y))

    # Draw a border around the warped frame
    border_color = (100, 100, 100)  # Gray color for the border
    border_width = 2
    pygame.draw.rect(screen, border_color, (x-border_width, y-border_width, 
                     draw.warper.width+2*border_width, draw.warper.height+2*border_width), 
                     border_width)

    # Audio reactivity bar
    bar_height = 5
    bar_y = y + draw.warper.height + 10  # 10 pixels below the warped frame
    bar_width = int(draw.warper.width * np.mean(fft_data))
    pygame.draw.rect(screen, (255, 0, 0), (x, bar_y, bar_width, bar_height))
