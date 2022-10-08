# feature extraction and preprocessing data
#IMPORT THE LIBRARIES
import librosa
import librosa.display
import pandas as pd
import numpy as np
import scipy.signal
import matplotlib.pyplot as plt
from PIL import Image
from pathlib import Path
from pylab import rcParams
rcParams['figure.figsize'] = 14, 6

import csv
# Preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
#Reports
from sklearn.metrics import classification_report, confusion_matrix

import warnings
warnings.filterwarnings('ignore')

#READ THE AUDIO SAMPLES
sr = 16000
e_file1 = r'C:\Users\Aryan\PycharmProjects\Noise Reduction Filter\audio01.mp3'
e_file2 = r'C:\Users\Aryan\PycharmProjects\Noise Reduction Filter\audio02.mp3'

# 10 seconds of each file
y1,sr = librosa.load(e_file1, mono=True, sr=sr, offset=0, duration=10)
y2,sr = librosa.load(e_file2, mono=True, sr=sr, offset=0, duration=10)

from IPython.display import Audio, IFrame, display

display(Audio(y1,rate=sr))
display(Audio(y2,rate=sr))

#The audio samples used have high level background noises.
librosa.display.waveplot(y1,sr=sr, color='g', x_axis='time');
librosa.display.waveplot(y1,sr=sr, color='g', x_axis='time');

#Logmel-spectogram
#It is a very common preprocessing technique in audio detection applications is to transform audios to its log mel-spectogram representation

S1 = librosa.feature.melspectrogram(y=y1, sr=sr, n_mels=64)
D1 = librosa.power_to_db(S1, ref=np.max)
librosa.display.specshow(D1, x_axis='time', y_axis='mel');

S2 = librosa.feature.melspectrogram(y=y2, sr=sr, n_mels=64)
D2 = librosa.power_to_db(S2, ref=np.max)
librosa.display.specshow(D2, x_axis='time', y_axis='mel');

#Filtering low-frequencies
#A low-pass filter is a filter that passes signals with a frequency lower than a selected cutoff frequency and attenuates signals with frequencies higher than the cutoff frequency.
#The exact frequency response of the filter depends on the filter design.

from scipy import signal
import random


def f_high(y,sr):
    b,a = signal.butter(10, 2000/(sr/2), btype='highpass')
    yf = signal.lfilter(b,a,y)
    return yf

yf1 = f_high(y1, sr)
yf2 = f_high(y2, sr)

librosa.display.waveplot(y1,sr=sr, colour='p', x_axis='time');
librosa.display.waveplot(yf1,sr=sr, x_axis='time');

librosa.display.waveplot(y2,sr=sr, x_axis='time');
librosa.display.waveplot(yf2,sr=sr, x_axis='time');

Sf1 = librosa.feature.melspectrogram(y=yf1, sr=sr, n_mels=64)
Df1 = librosa.power_to_db(Sf1, ref=np.max)
librosa.display.specshow(Df1, x_axis='time', y_axis='mel');
Sf2 = librosa.feature.melspectrogram(y=yf2, sr=sr, n_mels=64)
Df2 = librosa.power_to_db(Sf2, ref=np.max)
librosa.display.specshow(Df2, x_axis='time', y_axis='mel');

#Check the audio output
display(Audio(yf1,rate=sr))
display(Audio(yf2,rate=sr))

#CONCLUSION
#For both audio samples, the filter helped to isolate the interesting frequencies. The first audio is in a very good quality for distincting the birds.
#The second audio still has some noise but significant improvements in noise reduction can be observed.
