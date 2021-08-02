# Voice Recorder

In this project we are using sounddevice and wavio libraries to create a voice recorder with some lines of code. 
The details and working of python libraries that we are going to use are-    

**`wavio`** - `wavio` is a Python module that defines two functions:

- `wavio.read` reads a WAV file and returns an object that holds the sampling rate, sample width (in bytes), and a numpy array containing the data.
- `wavio.write` writes a numpy array to a WAV file, optionally using a specified sample width.

**`sounddevice`** - This Python module provides bindings for the PortAudio library and a few convenience functions to play and record NumPy arrays containing audio signals.

The `sounddevice` module is available for Linux, macOS and Windows.

### Installation

Install the given libraries with pip command using any terminal
```python
pip install sounddevice
pip install wavio
```

### Working
Import the `pyjokes` module in the Python file that you are going to get the jokes and then use the `get_joke()` function to easily get a random joke into your console/application.

```python
import sounddevice
import wavio

rate = 22050  # samples per second
T = 3         # sample duration (seconds)
f = 440.0     # sound frequency (Hz)
t = np.linspace(0, T, T*rate, endpoint=False)
x = np.sin(2*np.pi * f * t)
wavio.write("sine24.wav", x, rate, sampwidth=3)
```

### Screenshots

<img src="">

<img src="">



### Contributor

<a href="https://github.com/Umesh-01">Umesh Singh</a>
