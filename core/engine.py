import pygame
import config
from audio.audio_handler import AudioHandler
from ui.particle import Particle
from ui.bouncing_clock import BouncingClock
from core.visualization_manager import VisualizationManager
from utils.pygame_utils import add_glow_effect

class Engine:
    def __init__(self):
        self.audio_handler = AudioHandler()
        self.particles = [Particle() for _ in range(config.NUM_PARTICLES)]
        self.bouncing_clock = BouncingClock()
        self.vis_manager = VisualizationManager()
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        try:
            while self.running:
                self.handle_events()
                self.update()
                self.render()
                self.clock.tick(60)
        finally:
            self.cleanup()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.vis_manager.next_visualization()
                elif event.key == pygame.K_ESCAPE:
                    self.running = False

    def update(self):
        audio_data, fft_data = self.audio_handler.get_audio_data()
        for particle in self.particles:
            particle.update(fft_data)
        self.bouncing_clock.update()
        self.vis_manager.update()

    def render(self):
        config.screen.fill(config.BACKGROUND_COLOR)
        audio_data, fft_data = self.audio_handler.get_audio_data()
        self.vis_manager.draw(config.screen, fft_data)
        for particle in self.particles:
            particle.draw(config.screen)
        add_glow_effect(config.screen)
        self.bouncing_clock.draw(config.screen)
        pygame.display.flip()

    def cleanup(self):
        self.audio_handler.close()
        pygame.quit()