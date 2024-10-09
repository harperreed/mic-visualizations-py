import unittest
import pygame
from unittest.mock import patch, MagicMock
from core.visualization_manager import VisualizationManager


class TestVisualizationManager(unittest.TestCase):
    def setUp(self):
        self.screen = pygame.Surface((800, 600))
        self.vis_manager = VisualizationManager(self.screen)

    @patch("os.listdir")
    @patch("importlib.import_module")
    def test_load_visualizations(self, mock_import_module, mock_listdir):
        mock_listdir.return_value = ["test_vis.py", "__init__.py"]
        mock_module = MagicMock()
        mock_module.draw = MagicMock()
        mock_import_module.return_value = mock_module

        visualizations = self.vis_manager.load_visualizations()

        self.assertIn("test_vis", visualizations)
        self.assertEqual(visualizations["test_vis"], mock_module.draw)

    def test_next_visualization(self):
        initial_index = self.vis_manager.current_index
        self.vis_manager.next_visualization()
        self.assertEqual(
            self.vis_manager.current_index,
            (initial_index + 1) % len(self.vis_manager.visualizations),
        )

    @patch("pygame.time.get_ticks")
    async def test_update(self, mock_get_ticks):
        mock_get_ticks.return_value = 0
        self.vis_manager.last_switch_time = 0
        mock_fft_data = [0] * 1024

        with patch.object(self.vis_manager, "next_visualization") as mock_next_vis:
            await self.vis_manager.update(mock_fft_data)
            mock_next_vis.assert_not_called()

        mock_get_ticks.return_value = 10001  # Assuming MODE_SWITCH_TIME is 10000
        await self.vis_manager.update(mock_fft_data)
        mock_next_vis.assert_called_once()

    @patch("core.visualization_manager.VisualizationManager.load_visualizations")
    def test_draw(self, mock_load_visualizations):
        mock_vis = MagicMock()
        mock_load_visualizations.return_value = {"test_vis": mock_vis}
        self.vis_manager.visualizations = mock_load_visualizations.return_value
        mock_fft_data = [0] * 1024

        self.vis_manager.draw(self.screen, mock_fft_data)

        mock_vis.assert_called_once_with(
            self.screen,
            mock_fft_data,
            self.screen.get_width(),
            self.screen.get_height(),
        )


if __name__ == "__main__":
    unittest.main()
