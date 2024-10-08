# sample code from https://qiita.com/KENTAROSZK/items/8d82a495b7cffec69862 to understand pyaudio.

from datetime import datetime
import wave
import time

import pyaudio

import numpy as np
import math as m

from scipy.fft import fft, fftfreq

from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

FORMAT        = pyaudio.paInt16
TIME          = 10           # 録音時間[s]
SAMPLE_RATE   = 44100        # サンプリングレート
FRAME_SIZE    = 1024         # フレームサイズ
CHANNELS      = 1            # モノラルかバイラルか
INPUT_DEVICE_INDEX = 0       # マイクのチャンネル
NUM_OF_LOOP   = int(SAMPLE_RATE / FRAME_SIZE * TIME)

class MicAndFFT:
    def __init__(self):
        self.pa = pyaudio.PyAudio()
        self.list_frame = []
        
    def doFFT(self, x):
        # Now testing x-axis and frequency. Although original doc of scipy or source code has not been examined, changing elements of x(t) changes range of frequency. Thus, it might be F(x(t)) := X(omega) and i .. N - 1 represents omega or frequency. This assumption is required to be examined by doc or src code or even definition of FFT.    

        # According to doc of scypy, it is y[k] = np.sum(x * np.exp(-2j * np.pi * k * np.arange(n)/n)) and accoring to text book, it is c[k] = \integral f(x) * exp(-j * pi * k * x / n) Where c[k] is k-th spectorum and n is close to sampling rate by my understanding. And thus, y[k] for scipy.fft would be omega_k of spectorum. This understanding is correct?

        # Actually, I understood about DFT when I was 3rd year of undergrad and has experience of making DFT by C-language. However, until now, I haven't examine relatoin of index of X(omega or i) and frequency. For undergrad student, it is recommended to study both analytically and numerically. And possibly, it would be better to have an application for theory.

        yt = fft(x)
        yt2 = []
        for x in yt:
            re = x.real
            im = x.imag
            power = m.sqrt(re*re + im*im)
            yt2.append(power)

        glClear(GL_COLOR_BUFFER_BIT)
        glBegin(GL_LINE_STRIP)
        glColor3d(0.0, 0.0, 1.0)

        x = 0.0
        i = 0
        # range of rendering of power spectrum has been changed. It is assumed that summation of FFT is -l/2 to l/2 and thus, its freq response if symmetry arond half point of x. Actually, if one thinks about imaginary plane, it would be symmetry. It is better to examine this assumption is correct or not. 
        l = len(yt2) / 2
        for power in yt2:
            if (i > l):
                break
            # print(str(x) + "," + str(power))
            glVertex3d(x, power, -2.0)
            # debug
            # find out better deltaX
            # x = x + 0.01
            x = x + 0.05
            # end of debug
            i = i + 1
        glEnd()
        glFlush()

   

    def readDataAndDoFFT(self):
        # open the following stream every time by
        # this method call since it seems there 
        # are bug of autiod lib.
        self.stream = self.pa.open(format   = FORMAT,
                             channels = CHANNELS,
                             rate     = SAMPLE_RATE,
                             input    = True,
                            input_device_index = INPUT_DEVICE_INDEX,
                            frames_per_buffer  = FRAME_SIZE)
        # data = self.stream.read(FRAME_SIZE)
        # data = self.stream.read(1024)
        data = self.stream.read(8192)

        x = np.frombuffer(data, dtype="int16") / 32768.0
        for y in x:
            self.list_frame.append(y)

        while(True):
            if (len(self.list_frame) > 8192):
            # if (len(self.list_frame) > 2**16):
                self.list_frame.pop(0)
            else:
                break
        
        # self.doFFT(x)
        self.doFFT(self.list_frame)

        # close and terminate stream object "stream"
        # stream.stop_stream()
        # stream.close()
        # pa.terminate()



