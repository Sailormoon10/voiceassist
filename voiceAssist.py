#provides functions for interacting with the operating system
import os
#gtts is a google text to speech library
from gtts import *

text= "Tomorrow you have a doctor's appointment at 10:30 AM. Appointment is with Dr. Marcus"
language="en"
voice = gTTS(text= text, lang = language, slow = False)
voice.save("text2.mp3")
os.system("start text.mp3")
