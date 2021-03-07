from pydub import AudioSegment
from pydub.playback import play
import boto3

import sys
import os


class TTS(object):

    def __init__(self,voiceId='Joanna'):
        self.voiceId = voiceId
        self.outputFormat = 'mp3'
        self.polly = boto3.client('polly')

    def play(self, stream):
        try:
            filename = '~speech.mp3'
            f = open(filename, 'wb')
            f.write(stream.read())
            f.close()

            play(AudioSegment.from_mp3(filename))
            os.remove(filename)
        except:
            print("An error occured in text to speech engine")
            raise


    def speak(self,text):
        try:
            response = self.polly.synthesize_speech(VoiceId=self.voiceId, OutputFormat=self.outputFormat, Text=text)
            self.play(response['AudioStream'])
        except:
            print("An error occured in text to speech engine")
            raise
