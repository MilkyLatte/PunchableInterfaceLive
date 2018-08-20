import pyaudio
import wave
from scipy.io import wavfile as wav


class soundRecorder:
    def record(self, RECORD_SECONDS, stream):
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44100
        p = pyaudio.PyAudio()

        frames = []
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
# not efficientbut wav normalizes the data for me, can change if extremely slow
        wf = wave.open("output.wav", 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT)*2)
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        rate, dataSound = wav.read('output.wav')
        dataSound = dataSound/100000
        print("doneSound")
        return dataSound
        
    def createStream(self):
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44100
        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)
        return stream
