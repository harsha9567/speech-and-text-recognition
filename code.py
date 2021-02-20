# speech-and-text-recognition
import speech_recognition as sr
import pyaudio
from gtts import gTTS
import os
import win32com.client as wincl
import win32api, sys, os
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
        tts = gTTS(text, lang='en')
        tts.save("good.mp3")
        os.system("mpg321 good.mp3")
        speak = wincl.Dispatch("SAPI.SpVoice")
        speak.Speak(text)
    except:
        print("Sorry could not recognize what you said")
    




