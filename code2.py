import win32com.client as wincl
import win32api, sys, os
speak = wincl.Dispatch("SAPI.SpVoice")
speak.Speak("Hello World")
