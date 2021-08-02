# Voice Recorder

In this project we are using sounddevice and wavio libraries to create a voice recorder with some lines of code. 
The details and working of python libraries that we are going to use are-    

#### wavio

**`wavio`** - `wavio` is a Python module that defines two functions:

- `wavio.read` reads a WAV file and returns an object that holds the sampling rate, sample width (in bytes), and a numpy array containing the data.
- `wavio.write` writes a numpy array to a WAV file, optionally using a specified sample width.

#### sounddevice

**`sounddevice`** - This Python module provides bindings for the PortAudio library and a few convenience functions to play and record NumPy arrays containing audio signals.

The `sounddevice` module is available for Linux, macOS and Windows.

### Installation

Install the given libraries with pip command using any terminal
```python
pip install sounddevice
pip install wavio
```

### Working
Import the `sounddevice` and `wavio` module in the Python file that you are going to use for creating a voice recorder and use voice recorder in your console/application.

```python
import sounddevice as sd
import wavio as wv

# recording with the given values of duration(5 sec) and sample frequency(44000)
recording = sd.rec(int(5 * 44000), samplerate=44000, channels=2)
  
# recording audio for 5 seconds
sd.wait()
    
# converting the numpy array to audio file
wv.write("recording1.wav", recording, 44000, sampwidth=2)
```

### Screenshots
<div align="center">

<img src="../Voice%20Recorder/Images/voice_recorder0.png">

<img src="../Voice%20Recorder/Images/voice_recorder1.png">
</div>

### Contributor

<a href="https://github.com/Umesh-01">Umesh Singh</a>
