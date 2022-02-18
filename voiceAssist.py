#provides functions for interacting with the operating system
import os
#gtts is a google text to speech library
from gtts import *

text= input("Enter the text you would like to change to speech: ")
language="en"
voice = gTTS(text= text, lang = language, slow = False)
voice.save("text2.mp3")
os.system("start text.mp3")
