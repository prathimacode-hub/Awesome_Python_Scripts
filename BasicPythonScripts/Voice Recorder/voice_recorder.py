import sounddevice as sd
import wavio as wv
import random

freq = 44100

duration = 10

print("Recording...")

recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)

sd.wait()

name = random.randint(1, 10000)

wv.write(f"recording{name}.wav", recording, freq, sampwidth=2)

print("Recording Completed...")
