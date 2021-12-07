"""
This file converts generates the output message
"""

import Levenshtein as l

"""
future: when the path is calculated, get the distance and say the number of steps as well.
"""

rooms = ["medical imaging lab", "plant room", "teaching lab",
         "robotics lab", "lower ground 21", "lower ground 23", "lower ground 26", "lower ground 30b", "lower ground 3b", "lower ground 3a", "lower ground 4", "mohan's room"]
jargon = ["take", "me", "where", "is", "navigate",
          "to", "the", "can", "you", "please", "show", "way", "guide", "how", "do", "i", "get"]


def _clean_input(input_text):
    text = [x for x in input_text.strip().lower().split(" ")
            if x not in jargon]

    text = " ".join(text)
    return text


def generate_reply_message(text):
    """
    This function gets the text from the user and generates a reply message.
    """
    # input text after its been cleaned as in removed unnecessary wordings
    clean_text = _clean_input(text)

    # applies levenshtein distance
    def calc_distance(x):
        return l.distance(x, clean_text)

    # calculate the distance between the cleaned text and the rooms
    levenshtein_distances = list(map(calc_distance, rooms))

    # getting the index of the smallest distance
    min_val = min(levenshtein_distances)

    if min_val > 2:
        # if the room inputted does not exist this condition is triggered
        return None

    _index = levenshtein_distances.index(min_val)
    room_name = rooms[_index]

    # generates an output message and returns the output message and the room name
    return f"Okay let's head to {room_name}. ", room_name
