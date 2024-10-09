import unittest
from unittest.mock import patch, MagicMock
import numpy as np
from audio.audio_handler import AudioHandler
import config


class TestAudioHandler(unittest.TestCase):
    def setUp(self):
        self.audio_handler = AudioHandler()

    @patch("sounddevice.InputStream")
    def test_init(self, mock_input_stream):
        mock_stream = MagicMock()
        mock_input_stream.return_value = mock_stream

        audio_handler = AudioHandler()

        mock_input_stream.assert_called_once_with(
            samplerate=config.RATE, channels=config.CHANNELS, blocksize=config.CHUNK
        )
        mock_stream.start.assert_called_once()

    @patch("sounddevice.InputStream")
    def test_get_audio_data(self, mock_input_stream):
        mock_stream = MagicMock()
        mock_stream.read.return_value = (
            np.zeros((config.CHUNK, config.CHANNELS)),
            None,
        )
        mock_input_stream.return_value = mock_stream

        audio_handler = AudioHandler()
        audio_data, fft_data = audio_handler.get_audio_data()

        self.assertEqual(len(audio_data), config.CHUNK)
        self.assertEqual(len(fft_data), config.CHUNK // 2)

    def test_close(self):
        mock_stream = MagicMock()
        self.audio_handler.stream = mock_stream

        self.audio_handler.close()

        mock_stream.stop.assert_called_once()
        mock_stream.close.assert_called_once()


if __name__ == "__main__":
    unittest.main()
