"""
This file converts text to speech
"""

import pyttsx3
from stt import get_text


def text_to_speech():
    engine = pyttsx3.init()
    engine.say(get_text())
    engine.runAndWait()


text_to_speech()
