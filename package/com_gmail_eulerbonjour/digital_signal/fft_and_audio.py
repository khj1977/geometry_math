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
        l = len(yt2) / 2
        for power in yt2:
            if (i > l):
                break
            # print(str(x) + "," + str(power))
            glVertex3d(x, power, -2.0)
            x = x + 0.01
            i = i + 1
        glEnd()
        glFlush()

   

    def readDataAndDoFFT(self):
        self.stream = self.pa.open(format   = FORMAT,
                             channels = CHANNELS,
                             rate     = SAMPLE_RATE,
                             input    = True,
                            input_device_index = INPUT_DEVICE_INDEX,
                            frames_per_buffer  = FRAME_SIZE)
        # data = self.stream.read(FRAME_SIZE)
        data = self.stream.read(1024)

        x = np.frombuffer(data, dtype="int16") / 32768.0
        for y in x:
            self.list_frame.append(y)

        while(True):
            if (len(self.list_frame) > 8192):
                self.list_frame.pop(0)
            else:
                break
        
        # self.doFFT(x)
        self.doFFT(self.list_frame)

        # close and terminate stream object "stream"
        # stream.stop_stream()
        # stream.close()
        # pa.terminate()



