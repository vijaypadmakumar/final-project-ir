# Libraries
from subprocess import STDOUT
from types import coroutine
import pyaudio
import wave
import speech_recognition as sr
import pyttsx3
from tts import generate_reply_message

"""
Explain the class here
"""


class RobotInteraction:
    """
    Things to do:
        * Take input from user
        * Analyse it
            * If input is valid
                * Check if room is present in the lab
                * Get coordinates
            * If input is not valid
                * Ask user to repeat
        * Return coordinates
    """

    def __init__(self):
        self._WAVE_OUTPUT_FILENAME = "output.wav"
        self.engine = pyttsx3.init()

    def _record_audio(self):
        """
        This function records audio for 5 seconds saves it to the file named in _WAVE_OUTPUT_FILE
        """
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44100
        RECORD_SECONDS = 5

        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True, frames_per_buffer=CHUNK)

        print("* recording")

        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        print("* done recording")

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(self._WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

    def speech(self, message):
        """
        The argument message will be converted into speech.
        """
        self.engine.say(message)
        self.engine.runAndWait()
        self.engine.stop()

    def _get_input(self):
        """
        Records audio, converts it into text and returns it.
        """
        self._record_audio()

        r = sr.Recognizer()

        with sr.AudioFile(self._WAVE_OUTPUT_FILENAME) as source:
            # listen for the data (load audio to memory)
            audio_data = r.record(source)
            text = None
            # recognize (convert from speech to text)
            try:
                text = r.recognize_google(audio_data)
            except:
                self.speech("Invaid input, try again please.")
            return text

    def get_input(self):
        """
        * reads input from the user
        * checks whether it's null or not
        * tries to generate a reply message
        * if it's a valid input the coordinates of the inputted room is returned
        * otherwise the loop continues until a valid input
        """
        while True:
            print("listening")
            input = self._get_input()
            if input is not None:
                if generate_reply_message(input) is None:
                    # in case the inputted room does not exist this condition is triggered.
                    self.speech(
                        "The room doesn't exist, try again please.")
                    continue

                output_message, room_name = generate_reply_message(input)
                coordinates = self.get_coordinates(room_name=room_name)

                self.speech(output_message)
                return coordinates
            else:
                # while the input is not valid the loop keeps running
                continue

    def get_coordinates(self, room_name=None):
        """
        * get coordinates of the room name using room_name from a file and return it
        * coordinates = get_coordinates(room_name)
        * return coordinates
        """
        if room_name:
            pass
            # get coordinates and return it
        else:
            return "error inside get_coordinates() - robot_interaction.pyt room name does not exist in the file"
