"""
This file converts text to speech
"""

import pyttsx3
from stt import get_text
import sys

"""
future: when the path is calculated, get the distance and say the number of steps as well.
"""

rooms = ["medical imaging lab", "plant room", "teaching lab",
         "robotics lab", "lg21", "lg23", "lg26", "lg30b", "lg03b", "lg03a", "lg04", "mohan's room"]
jargon = ["take", "me", "where", "is", "navigate", "to", "the", "room"]
# instead of checking in the dictionary use levenshtein instead to check similarity


def generate_reply_message(text):
    """
    This function gets the text from the user and generates a reply message 
    """
    text = [x for x in text.strip().lower().split(" ") if x not in jargon]

    for word in text:
        for room in rooms:
            if word in room:
                return f"lets go to the {room} now. follow me."


def text_to_speech():
    engine = pyttsx3.init()
    reply_message = generate_reply_message(
        get_text())
    print(reply_message)
    engine.say(reply_message)
    engine.runAndWait()
    engine.stop()
    sys.exit(0)


text_to_speech()
