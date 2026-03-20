import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import sys
sys.path.insert(1, r'./../functions')

A = 2 # amplitude
freq = 5 # Hz
phase = np.pi/4 # radians (45 degrees)
fs = 100
dt = 1 / fs
time = np.arange(0, 500) / fs
x = A * np.sin(2 * np.pi * freq * time + phase) + 1
x = np.asarray(x)
N = x.shape[0]
t = np.arange(0, N) / fs

fig, ax = plt.subplots(1, 1, figsize=(9, 3))
ax.plot(time, x, linewidth=2)
ax.set_xlabel('Time [s]')
ax.set_ylabel('Amplitude')
fig.tight_layout()