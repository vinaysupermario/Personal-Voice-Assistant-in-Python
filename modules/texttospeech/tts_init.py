from pydub import AudioSegment
from pydub.playback import play

from ctypes import *
import pyaudio

import boto3
import os

def py_error_handler(filename, line, function, err, fmt):
    pass

# Define Error handler to silence annoying ASLA log messages
ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)
c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)
asound = cdll.LoadLibrary('libasound.so')
asound.snd_lib_error_set_handler(c_error_handler)
p = pyaudio.PyAudio()

# text = 'This is a sample text to be synthesized'
text = input("Type Text to convert to speech : ")

polly = boto3.client('polly')
response = polly.synthesize_speech(VoiceId='Joanna', OutputFormat='mp3', Text=text)

file = open('speech.mp3', 'wb')
file.write(response['AudioStream'].read())
file.close()

print("Speaking :" + text)
play(AudioSegment.from_mp3('speech.mp3'))
p.terminate()
os.remove('speech.mp3')
