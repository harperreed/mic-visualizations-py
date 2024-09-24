import importlib
import os
import pygame
from config import MODE_SWITCH_TIME
from ui.top_scroller import TopScroller
from ui.bottom_scroller import BottomScroller

class VisualizationManager:
    def __init__(self):
        self.visualizations = self.load_visualizations()
        self.current_index = 0
        self.last_switch_time = pygame.time.get_ticks()
        self.top_scroller = None
        self.bottom_scroller = None

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
        # Draw the main visualization
        current_vis = list(self.visualizations.values())[self.current_index]
        current_vis(screen, fft_data, screen.get_width(), screen.get_height())

        # Initialize and draw the top and bottom scrollers
        if self.top_scroller is None:
            self.top_scroller = TopScroller(screen.get_width(), screen.get_height(), "Breaking News: Music is awesome! More at 11.")
        if self.bottom_scroller is None:
            self.bottom_scroller = BottomScroller(screen.get_width(), screen.get_height(), "Stay tuned for more visualizations! Don't touch that dial!")

        self.top_scroller.update(fft_data)
        self.bottom_scroller.update(fft_data)
        self.top_scroller.draw(screen)
        self.bottom_scroller.draw(screen)