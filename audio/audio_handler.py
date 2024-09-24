import numpy as np
import sounddevice as sd
from config import CHUNK, CHANNELS, RATE, FREQ_RANGE

class AudioHandler:
    def __init__(self):
        self.stream = None
        try:
            self.stream = sd.InputStream(samplerate=RATE, channels=CHANNELS, blocksize=CHUNK)
            self.stream.start()
        except sd.PortAudioError:
            print("Warning: Unable to open audio stream. Running in silent mode.")

    def get_audio_data(self):
        if self.stream is None:
            return np.zeros(CHUNK), np.zeros(CHUNK // 2)
        
        try:
            audio_data, _ = self.stream.read(CHUNK)
            audio_data = audio_data.flatten()
            
            fft_data = np.abs(np.fft.fft(audio_data))
            freqs = np.fft.fftfreq(len(fft_data), 1.0/RATE)
            
            mask = (freqs >= FREQ_RANGE[0]) & (freqs <= FREQ_RANGE[1])
            fft_data = fft_data[mask]
            
            fft_data = fft_data / np.max(fft_data) if np.max(fft_data) > 0 else fft_data
            
            return audio_data, fft_data
        except Exception as e:
            print(f"Error reading audio data: {e}")
            return np.zeros(CHUNK), np.zeros(CHUNK // 2)

    def close(self):
        if self.stream:
            self.stream.stop()
            self.stream.close()