import threading
import numpy as np
import pyaudio

class BassVolumeMonitor(threading.Thread):
    def __init__(self, buffer_size=1024, sample_rate=44100, channels=1):
        super().__init__()
        self.buffer_size = buffer_size
        self.sample_rate = sample_rate
        self.channels = channels
        self.daemon = True
        self.volume = 0
        self.sensitivity = 1
        self.audio_interface = pyaudio.PyAudio()
        self.stream = self.audio_interface.open(
            format=pyaudio.paInt16,
            channels=self.channels,
            rate=self.sample_rate,
            input=True,
            frames_per_buffer=self.buffer_size
        )

    def run(self):
        while True:
            try:
                audio_data = np.frombuffer(self.stream.read(self.buffer_size, exception_on_overflow=False), dtype=np.int16)
                self.volume = ((max(abs(audio_data.min()), abs(audio_data.max())) / 32768) * 3) * self.sensitivity 
            except IOError as e:
                pass  
            
    def get_volume(self):
        return self.volume

    def stop(self):
        self.stream.stop_stream()
        self.stream.close()
        self.audio_interface.terminate()
