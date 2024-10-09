import unittest
import numpy as np
from unittest.mock import patch, MagicMock
from audio.audio_handler import AudioHandler


class TestAudioHandler(unittest.TestCase):
    def setUp(self):
        self.audio_handler = AudioHandler()

    def tearDown(self):
        self.audio_handler.close()

    def test_initialization(self):
        self.assertIsNotNone(self.audio_handler.stream)

    @patch("sounddevice.InputStream")
    def test_initialization_error(self, mock_input_stream):
        mock_input_stream.side_effect = Exception("Test error")
        with self.assertLogs(level="WARNING"):
            AudioHandler()

    @patch("numpy.fft.fft")
    @patch("numpy.fft.fftfreq")
    def test_get_audio_data(self, mock_fftfreq, mock_fft):
        mock_audio_data = np.array([1, 2, 3, 4])
        self.audio_handler.stream = MagicMock()
        self.audio_handler.stream.read.return_value = (mock_audio_data, None)

        mock_fft.return_value = np.array([1, 2, 3, 4])
        mock_fftfreq.return_value = np.array([0, 1, 2, 3])

        audio_data, fft_data = self.audio_handler.get_audio_data()

        np.testing.assert_array_equal(audio_data, mock_audio_data)
        self.assertEqual(len(fft_data), len(mock_audio_data) // 2)

    def test_get_audio_data_error(self):
        self.audio_handler.stream = MagicMock()
        self.audio_handler.stream.read.side_effect = Exception("Test error")

        with self.assertLogs(level="ERROR"):
            audio_data, fft_data = self.audio_handler.get_audio_data()

        self.assertTrue(np.all(audio_data == 0))
        self.assertTrue(np.all(fft_data == 0))


if __name__ == "__main__":
    unittest.main()
