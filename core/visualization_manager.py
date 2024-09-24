import importlib
import os
import pygame
from config import MODE_SWITCH_TIME

class VisualizationManager:
    def __init__(self):
        self.visualizations = self.load_visualizations()
        self.current_index = 0
        self.last_switch_time = pygame.time.get_ticks()

    def load_visualizations(self):
        visualizations = {}
        vis_dir = "visualizations"
        for filename in os.listdir(vis_dir):
            if filename.endswith(".py") and filename != "__init__.py":
                module_name = f"{vis_dir}.{filename[:-3]}"
                module = importlib.import_module(module_name)
                if hasattr(module, 'draw'):
                    visualizations[filename[:-3]] = module.draw
        return visualizations

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_switch_time > MODE_SWITCH_TIME:
            self.next_visualization()
            self.last_switch_time = current_time

    def next_visualization(self):
        self.current_index = (self.current_index + 1) % len(self.visualizations)

    def draw(self, screen, fft_data):
        current_vis = list(self.visualizations.values())[self.current_index]
        current_vis(screen, fft_data, screen.get_width(), screen.get_height())