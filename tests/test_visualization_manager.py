import unittest
from unittest.mock import patch, MagicMock
from core.visualization_manager import VisualizationManager
import pygame


class TestVisualizationManager(unittest.TestCase):
    def setUp(self):
        self.mock_screen = MagicMock()
        self.vis_manager = VisualizationManager(self.mock_screen)

    def test_init(self):
        self.assertIsNotNone(self.vis_manager.visualizations)
        self.assertEqual(self.vis_manager.current_index, 0)

    @patch("os.listdir")
    @patch("importlib.import_module")
    def test_load_visualizations(self, mock_import_module, mock_listdir):
        mock_listdir.return_value = ["test_vis.py"]
        mock_module = MagicMock()
        mock_module.draw = MagicMock()
        mock_import_module.return_value = mock_module

        visualizations = self.vis_manager.load_visualizations()

        self.assertIn("test_vis", visualizations)
        self.assertEqual(visualizations["test_vis"], mock_module.draw)

    async def test_update(self):
        self.vis_manager.last_switch_time = (
            pygame.time.get_ticks() - 15000
        )  # Ensure switch
        mock_fft_data = MagicMock()

        await self.vis_manager.update(mock_fft_data)

        self.assertEqual(
            self.vis_manager.current_index, 1 % len(self.vis_manager.visualizations)
        )

    def test_next_visualization(self):
        initial_index = self.vis_manager.current_index
        self.vis_manager.next_visualization()
        self.assertEqual(
            self.vis_manager.current_index,
            (initial_index + 1) % len(self.vis_manager.visualizations),
        )

    def test_draw(self):
        mock_fft_data = MagicMock()
        self.vis_manager.draw(self.mock_screen, mock_fft_data)

        current_vis = list(self.vis_manager.visualizations.values())[
            self.vis_manager.current_index
        ]
        current_vis.assert_called_once_with(
            self.mock_screen,
            mock_fft_data,
            self.mock_screen.get_width(),
            self.mock_screen.get_height(),
        )


if __name__ == "__main__":
    unittest.main()
