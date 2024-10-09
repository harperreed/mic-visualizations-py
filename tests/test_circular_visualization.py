import unittest
from unittest.mock import patch, MagicMock
import numpy as np
from visualizations import circular


class TestCircularVisualization(unittest.TestCase):
    def setUp(self):
        self.mock_screen = MagicMock()
        self.mock_screen.get_width.return_value = 800
        self.mock_screen.get_height.return_value = 600

    @patch("pygame.draw.line")
    def test_draw(self, mock_draw_line):
        fft_data = np.random.random(1024)

        circular.draw(self.mock_screen, fft_data, 800, 600)

        # Check that pygame.draw.line was called the expected number of times
        self.assertEqual(mock_draw_line.call_count, 100)

        # Check that all calls to pygame.draw.line used the mock_screen
        for call in mock_draw_line.call_args_list:
            self.assertEqual(call[0][0], self.mock_screen)


if __name__ == "__main__":
    unittest.main()
