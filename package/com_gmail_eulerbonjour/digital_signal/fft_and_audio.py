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
    
        self.stream = self.pa.open(format   = FORMAT,
                             channels = CHANNELS,
                             rate     = SAMPLE_RATE,
                             input    = True,
                            input_device_index = INPUT_DEVICE_INDEX,
                            frames_per_buffer  = FRAME_SIZE)
        self.list_frame = []
        
    def doFFT(x):
        yt = fft(x)
        yt2 = []
        for x in yt:
            re = x.real
            im = x.imag
            power = m.sqrt(re*re + im*im)
            yt2.append(power)

        glClear(GL_COLOR_BUFFER_BIT)
        glBegin(GL_LINE_STRIP)

        x = 0
        for power in yt2:
            glVertex3d(x, power, -2.0)
            x = x + 1
        glEnd()
        glFlush()

   

    def readDataAndDoFFT(self):
        print("RECORDING...")

        # data = self.stream.read(FRAME_SIZE)
        data = self.stream.read(1024)

        # debug
        # it's better to be FIFO queue.
        self.list_frame.append(data)
        # end of debug

        print("RECORDING DONE!")

        # The following part is come from the follows:
        # https://qiita.com/mix_dvd/items/adce7636e2ab33b25208
        # %matplotlib inline

        x = np.frombuffer(data, dtype="int16") / 32768.0
        self.doFFT(x)

        # close and terminate stream object "stream"
        # stream.stop_stream()
        # stream.close()
        # pa.terminate()


