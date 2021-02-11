from scipy.io.wavfile import read
from scipy import signal
import numpy as np
from scipy.fft import fftshift
import matplotlib.pyplot as plt
import soundfile as sf

# data, samplerate = sf.read('test.ogg',  channels=1, samplerate=44100)
data, samplerate = sf.read('test.ogg')
arr = np.array(data)
print(samplerate)
print(len(data))
f, t, Sxx= signal.spectrogram(arr, fs=samplerate)
# f, t, Sxx= signal.spectrogram(arr, fs=1/samplerate)
# f, t, Sxx= signal.spectrogram(arr)
print(f)
print(t)
print(Sxx)
print(len(Sxx))
print(Sxx[50])
print(len(Sxx[50]))

plt.pcolormesh(t, f, Sxx, shading='gouraud')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()
