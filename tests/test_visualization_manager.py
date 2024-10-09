import unittest
from unittest.mock import patch, MagicMock
from core.visualization_manager import VisualizationManager


class TestVisualizationManager(unittest.TestCase):
    @patch("ui.rtsp_cube.RTSPCube")
    @patch("ui.bottom_scroller.BottomScroller")
    def setUp(self, mock_bottom_scroller, mock_rtsp_cube):
        self.mock_screen = MagicMock()
        self.mock_screen.get_width.return_value = 800
        self.mock_screen.get_height.return_value = 600

        # Mock RTSPCube
        self.mock_rtsp_cube = mock_rtsp_cube.return_value

        # Mock BottomScroller
        self.mock_bottom_scroller = mock_bottom_scroller.return_value

        with patch("config.RTSP_STREAMS", ["mock_url"]):
            self.vis_manager = VisualizationManager(self.mock_screen)

    def test_init(self):
        self.assertIsNotNone(self.vis_manager.visualizations)
        self.assertEqual(self.vis_manager.current_index, 0)
        self.assertIsNotNone(self.vis_manager.rtsp_cube)
        self.assertIsNotNone(self.vis_manager.bottom_scroller)

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

    @patch("pygame.time.get_ticks")
    async def test_update(self, mock_get_ticks):
        mock_get_ticks.return_value = 20000  # Ensure switch
        self.vis_manager.last_switch_time = 0
        mock_fft_data = MagicMock()

        await self.vis_manager.update(mock_fft_data)

        self.assertEqual(
            self.vis_manager.current_index, 1 % len(self.vis_manager.visualizations)
        )
        self.mock_bottom_scroller.update.assert_called_once_with(mock_fft_data)
        self.mock_rtsp_cube.update.assert_called_once_with(mock_fft_data)

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
        self.mock_bottom_scroller.draw.assert_called_once_with(self.mock_screen)
        self.mock_rtsp_cube.draw.assert_called_once_with(self.mock_screen)

    def test_cleanup(self):
        self.vis_manager.cleanup()
        self.mock_rtsp_cube.cleanup.assert_called_once()


if __name__ == "__main__":
    unittest.main()
