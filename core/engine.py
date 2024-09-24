import pygame
import config
from audio.audio_handler import AudioHandler
from ui.particle import Particle
from ui.bouncing_clock import BouncingClock
from core.visualization_manager import VisualizationManager
from utils.pygame_utils import add_glow_effect
import asyncio

class Engine:
    def __init__(self):
        pygame.init()
        if config.FULLSCREEN:
            self.screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
        
        pygame.display.set_caption("Music Visualizer")

        self.audio_handler = AudioHandler()
        self.particles = [Particle() for _ in range(config.NUM_PARTICLES)]
        self.bouncing_clock = BouncingClock()
        self.vis_manager = VisualizationManager(self.screen)
        self.clock = pygame.time.Clock()
        self.running = True

    async def run(self):
        try:
            while self.running:
                await self.handle_events()
                await self.update()
                self.render()
                await asyncio.sleep(0)  # Allow other async tasks to run
                self.clock.tick(60)
        finally:
            self.cleanup()

    async def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.vis_manager.next_visualization()
                elif event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_f:  # Toggle fullscreen
                    config.FULLSCREEN = not config.FULLSCREEN
                    pygame.display.toggle_fullscreen()

    async def update(self):
        audio_data, fft_data = self.audio_handler.get_audio_data()
        for particle in self.particles:
            particle.update(fft_data)
        self.bouncing_clock.update()
        await self.vis_manager.update(fft_data)

    def render(self):
        self.screen.fill(config.BACKGROUND_COLOR)
        audio_data, fft_data = self.audio_handler.get_audio_data()
        self.vis_manager.draw(self.screen, fft_data)
        for particle in self.particles:
            particle.draw(self.screen)
        add_glow_effect(self.screen)
        self.bouncing_clock.draw(self.screen)
        pygame.display.flip()

    def cleanup(self):
        self.audio_handler.close()
        pygame.quit()