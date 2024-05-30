# sample code from https://qiita.com/KENTAROSZK/items/8d82a495b7cffec69862 to understand pyaudio.

from datetime import datetime
import wave
import time

import pyaudio

import numpy as np
import matplotlib.pyplot as plt

from scipy.fft import fft, fftfreq


FORMAT        = pyaudio.paInt16
TIME          = 10           # 録音時間[s]
SAMPLE_RATE   = 44100        # サンプリングレート
FRAME_SIZE    = 1024         # フレームサイズ
CHANNELS      = 1            # モノラルかバイラルか
INPUT_DEVICE_INDEX = 0       # マイクのチャンネル
NUM_OF_LOOP   = int(SAMPLE_RATE / FRAME_SIZE * TIME)

WAV_FILE = "./output.wav"

pa = pyaudio.PyAudio()
for i in range(pa.get_device_count()):
    print(pa.get_device_info_by_index(i))
    print()
pa.terminate()

def record_and_save():
    """
    デバイスから出力される音声の録音をする
    """
    pa = pyaudio.PyAudio()

    stream = pa.open(format   = FORMAT,
                     channels = CHANNELS,
                     rate     = SAMPLE_RATE,
                     input    = True,
                     input_device_index = INPUT_DEVICE_INDEX,
                     frames_per_buffer  = FRAME_SIZE)

    print("RECORDING...")

    list_frame = []


    for i in range(NUM_OF_LOOP):
        data = stream.read(FRAME_SIZE)
        # print(data)
        list_frame.append(data)

    print("RECORDING DONE!")

    # The following part is come from the follows:
    # https://qiita.com/mix_dvd/items/adce7636e2ab33b25208
    # %matplotlib inline

    x = np.frombuffer(data, dtype="int16") / 32768.0

    yt = fft(x)
    plt.figure(figsize=(15,3))
    plt.plot(yt)
    plt.show()

    plt.figure(figsize=(15,3))
    plt.plot(x)
    plt.show()


    # close and terminate stream object "stream"
    stream.stop_stream()
    stream.close()
    pa.terminate()


    wf = wave.open(WAV_FILE, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(pa.get_sample_size(FORMAT))
    wf.setframerate(SAMPLE_RATE)
    wf.writeframes(b''.join(list_frame))
    wf.close()

record_and_save()