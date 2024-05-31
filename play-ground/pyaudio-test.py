# sample code from https://qiita.com/KENTAROSZK/items/8d82a495b7cffec69862 to understand pyaudio.

from datetime import datetime
import wave
import time

import pyaudio

import numpy as np

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

def my_glut_idle():
    glutPostRedisplay()

def my_glut_mouse(button, state, x, y):
  if button == GLUT_LEFT_BUTTON:
    if (state == GLUT_DOWN):
      glutIdleFunc(my_glut_idle)
    # else:
      # glutIdleFunc(0)
  elif button == GLUT_RIGHT_BUTTON:
    if state == GLUT_DOWN:
        glutPostRedisplay()

def my_glut_init(minX, maxX, minY, maxY, minZ, maxZ):
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    
    glLoadIdentity()
    # glOrtho(0.0, 1.0, 0.0, 1.0, -1.0, 1.0)
    # glOrtho(-20.0, 20.0, -20.0, 20.0, -10.0, 10.0)
    glOrtho(minX, maxX, minY, maxY, minZ, maxZ)

    # gluPerspective(30.0, 1.0, 1.0, 100.0)
    # glTranslated(0.0, 0.0, -5.0);
    # gluLookAt(0.0, 0.0, -10.0, 0.0, 0.0, 10.0, 0.0, 1.0, 0.0)

def my_glut_display():
    global audioMod

    audioMod.record_and_save()

class KAudioModule:
    def __init__(self):
        self.pa = pyaudio.PyAudio()
    
        self.pa.open(format   = FORMAT,
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
        glBegin(GL_LINES)

        x = 0
        for power in yt2:
            glVertex3d(x, power, -2.0)
            x = x + 1
        glEnd()
        glFlush()

   

    def record_and_save(self):

        print("RECORDING...")

        # global stream

        # for i in range(NUM_OF_LOOP):
        data = self.stream.read(FRAME_SIZE)
        # print(data)
        self.list_frame.append(data)

        print("RECORDING DONE!")

        # The following part is come from the follows:
        # https://qiita.com/mix_dvd/items/adce7636e2ab33b25208
        # %matplotlib inline

        x = np.frombuffer(data, dtype="int16") / 32768.0
        doFFT(x)

        # close and terminate stream object "stream"
        stream.stop_stream()
        stream.close()
        pa.terminate()

audioMod = KAudioModule()

glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutInitWindowPosition(200, 200)
glutCreateWindow(b"FFT")
glutMouseFunc(my_glut_mouse)
my_glut_init(-20.0, 20.0, -20.0, 20.0, -5.0, 5.0)
glutDisplayFunc(my_glut_display)
glutMainLoop()