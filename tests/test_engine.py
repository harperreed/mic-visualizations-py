import unittest
from unittest.mock import patch, MagicMock
from core.engine import Engine
import pygame
import config


class TestEngine(unittest.TestCase):
    @patch("pygame.display.set_mode")
    @patch("core.visualization_manager.VisualizationManager")
    @patch("audio.audio_handler.AudioHandler")
    def setUp(self, mock_audio_handler, mock_vis_manager, mock_set_mode):
        self.mock_screen = MagicMock()
        mock_set_mode.return_value = self.mock_screen
        self.engine = Engine()

    def test_init(self):
        self.assertIsNotNone(self.engine.audio_handler)
        self.assertIsNotNone(self.engine.vis_manager)
        self.assertEqual(len(self.engine.particles), config.NUM_PARTICLES)

    @patch("pygame.event.get")
    async def test_handle_events(self, mock_event_get):
        mock_event = MagicMock()
        mock_event.type = pygame.QUIT
        mock_event_get.return_value = [mock_event]

        await self.engine.handle_events()

        self.assertFalse(self.engine.running)

    @patch("core.visualization_manager.VisualizationManager.update")
    async def test_update(self, mock_update):
        await self.engine.update()

        self.engine.audio_handler.get_audio_data.assert_called_once()
        mock_update.assert_called_once()

    def test_render(self):
        self.engine.render()

        self.mock_screen.fill.assert_called_once_with(config.BACKGROUND_COLOR)
        self.engine.vis_manager.draw.assert_called_once()
        pygame.display.flip.assert_called_once()

    def test_cleanup(self):
        self.engine.cleanup()

        self.engine.audio_handler.close.assert_called_once()
        pygame.quit.assert_called_once()


if __name__ == "__main__":
    unittest.main()
