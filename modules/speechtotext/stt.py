# Speech To Text Conversion Engine

from ctypes import *
import pyaudio

import speech_recognition as sr
import os
import time


class STT(object):
  def __init__(self, pause_threshold=0.7, energy_threshold=800):

    self.recognizer = sr.Recognizer()
    self.recognizer.pause_threshold = pause_threshold
    self.recognizer.energy_threshold = energy_threshold

    # Define Error handler to silence annoying ASLA log messages
    ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)
    c_error_handler = ERROR_HANDLER_FUNC(self.py_error_handler)
    asound = cdll.LoadLibrary('libasound.so')
    asound.snd_lib_error_set_handler(c_error_handler)
    self.p = pyaudio.PyAudio()

  def py_error_handler(self, filename, line, function, err, fmt):
          pass

  def convert(self, source):
    try:
      print("Listening ...")
      audio = self.recognizer.listen(source, timeout=None)
      print("Working ...")
      message = str(self.recognizer.recognize_google(audio))
      self.p.terminate()
    except:
        print("An error occured in speech to text engine")
        raise
    return message
