from modules.neuralengine.neural import Neural
from modules.speechtotext.stt import STT
from modules.texttospeech.tts import TTS
import speech_recognition as sr

import webbrowser
import wikipedia
import pyvona
import pyperclip
import time
import os

cl = Neural()
v = TTS()
r = STT()

v.speak('Hello! For a list of commands, plese say "keyword list"...')
print("For a list of commands, please say: 'keyword list'...")


#List of Available Commands
keywd = 'keyword list'
google = 'search for'
acad = 'academy search'
sc = 'deep search'
wkp = 'wiki page for'
rdds = 'read this text'
sav = 'save this text'
vid = 'video for'
wtis = 'what is'
wtar = 'what are'
whis = 'who is'
whws = 'who was'
when = 'when'
where = 'where'
how = 'how'
lsp = 'silence please'
lsc = 'resume listening'
stoplst = 'stop listening'

while True:

    with sr.Microphone() as source:

        try:

            message = r.convert(source)
            print('You said: ' + message)
            message = message.lower()

            if google in message:

                words = message.split()
                del words[0:2]
                st = ' '.join(words)
                print('Google Results for: '+str(st))
                url='http://google.com/search?q='+st
                webbrowser.open(url)
                v.speak('Google Results for: '+str(st))

            elif acad in message:

                words = message.split()
                del words[0:2]
                st = ' '.join(words)
                print('Academic Results for: '+str(st))
                url='https://scholar.google.ro/scholar?q='+st
                webbrowser.open(url)
                v.speak('Academic Results for: '+str(st))

            elif wkp in message:

                try:

                    words = message.split()
                    del words[0:3]
                    st = ' '.join(words)
                    wkpres = wikipedia.summary(st, sentences=2)

                    try:

                        print('\n' + str(wkpres) + '\n')
                        v.speak(wkpres)

                    except UnicodeEncodeError:
                        v.speak(wkpres)

                except wikipedia.exceptions.DisambiguationError as e:
                    print (e.options)
                    v.speak("Too many results for this keyword. Please be more specific and try again")
                    continue

                except wikipedia.exceptions.PageError as e:
                    print('The page does not exist')
                    v.speak('The page does not exist')
                    continue

            elif sc in message:

                try:
                    words = message.split()
                    del words[0:1]
                    st = ' '.join(words)
                    sca = cl.query(st)
                    print('The answer is: '+str(sca))
                    v.speak('The answer is: '+str(sca))

                except StopIteration:
                    print('Your question is ambiguous. Please try again!')
                    v.speak('Your question is ambiguous. Please try again!')

                else:
                    print('No query provided')

            elif rdds in message:

                print("Reading your text")
                v.speak(pyperclip.paste())

            elif sav in message:

                with open('/home/ubuntu/Desktop/assistant.txt', 'a+') as f:
                    f.write("\n\n" + pyperclip.paste() + "\n\n")
                print("Saving your text to file")
                v.speak("Saving your text to file")

            elif keywd in message:

                print('')
                print('Say ' + google + ' to return a Google search')
                print('Say ' + acad + ' to return a Google Scholar search')
                print('Say ' + sc + ' to return a Wolfram Alpha query')
                print('Say ' + wkp + ' to return a Wikipedia page')
                print('Say ' + rdds + ' to read the text you have highlighted and Ctrl+C (copied to clipboard)')
                print('Say ' + sav + ' to save the text you have highlighted and Ctrl+C-ed (copied to clipboard) to a file')
                print('Say ' + vid + ' to return video results for your query')
                print('For more general questions, ask them naturally and I will do my best to find a good answer')
                print('Say ' + stoplst + ' to shut down')
                print('')

            elif vid in message: 

                words = message.split()
                del words[0:2]
                st = ' '.join(words)
                print('Video Results for: '+str(st))
                url='https://www.youtube.com/results?search_query='+st
                webbrowser.open(url)
                v.speak('Video Results for: '+str(st))

            elif wtis in message or wtar in message or whis in message or whws in message or when in message or where in message or how in message:

                try:

                    sca = cl.query(message)
                    print('The answer is: '+str(sca))
                    v.speak('The answer is: '+str(sca))

                except UnicodeEncodeError:

                    v.speak('The answer is: '+str(sca))

                except StopIteration:

                    words = message.split()
                    del words[0:2]
                    st = ' '.join(words)
                    print('Google Results for: '+str(st))
                    url='http://google.com/search?q='+st
                    webbrowser.open(url)
                    v.speak('Google Results for: '+str(st))


            elif stoplst in message:

                v.speak("I am shutting down")
                print("Shutting down...")
                break

            elif lsp in message:

                v.speak('Listening is paused')
                print('Listening is paused')
                r2 = STT()

                while True:

                    with sr.Microphone() as source2:

                        try:

                            message2 = r2.convert(source2)

                            if lsc in message2:
                                v.speak('I am listening')
                                break

                            else:
                                continue

                        except sr.UnknownValueError:
                            print("Listening is paused. Say resume listening when you're ready...")

                        except sr.RequestError:
                            v.speak("I'm sorry, I couldn't reach google")
                            print("I'm sorry, I couldn't reach google")


            else:
                v.speak("I'm sorry, I'm afraid I can't process your query.")
                pass

        except sr.UnknownValueError:
            print("For a list of commands, say: 'keyword list'...")

        except sr.RequestError:
            v.speak("I'm sorry, I couldn't reach google")
            print("I'm sorry, I couldn't reach google")

    time.sleep(0.4)

