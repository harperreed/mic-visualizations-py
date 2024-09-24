import importlib
import os
import pygame
import asyncio
from config import MODE_SWITCH_TIME, RTSP_STREAMS, TOP_SCROLL_SPEED, BOTTOM_SCROLL_SPEED, CUBE_SPEED_Y, CUBE_SPEED_X, RSS_FEED_URLS
from ui.top_scroller import TopScroller
from ui.bottom_scroller import BottomScroller
from ui.rtsp_cube import RTSPCube

class VisualizationManager:
    def __init__(self, screen):
        self.screen = screen
        self.visualizations = self.load_visualizations()
        self.current_index = 0
        self.last_switch_time = pygame.time.get_ticks()
        self.top_scroller = TopScroller(self.screen.get_width(), self.screen.get_height(), RSS_FEED_URLS, TOP_SCROLL_SPEED)
        self.bottom_scroller = BottomScroller(self.screen.get_width(), self.screen.get_height(), "Stay tuned for more visualizations!", BOTTOM_SCROLL_SPEED)
        self.rtsp_cube = RTSPCube(self.screen.get_width(), self.screen.get_height(), [url for url in RTSP_STREAMS if url], (CUBE_SPEED_X, CUBE_SPEED_Y))

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

    async def update(self, fft_data):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_switch_time > MODE_SWITCH_TIME:
            self.next_visualization()
            self.last_switch_time = current_time

        await self.top_scroller.update(fft_data)
        self.bottom_scroller.update(fft_data)
        self.rtsp_cube.update(fft_data)

    def next_visualization(self):
        self.current_index = (self.current_index + 1) % len(self.visualizations)

    def draw(self, screen, fft_data):
        current_vis = list(self.visualizations.values())[self.current_index]
        current_vis(screen, fft_data, screen.get_width(), screen.get_height())

        self.top_scroller.draw(screen)
        self.bottom_scroller.draw(screen)
        self.rtsp_cube.draw(screen)

    async def start(self):
        await self.top_scroller.start()

    def cleanup(self):
        if self.rtsp_cube:
            self.rtsp_cube.cleanup()