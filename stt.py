"""
This file reads audio from the port and converts into a string
"""
import pyaudio
import wave
import speech_recognition as sr

_WAVE_OUTPUT_FILENAME = "output.wav"


def record_audio():
    """
    This function records audio for 5 seconds saves it to the file named in _WAVE_OUTPUT_FILE
    """
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = 5

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(_WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


def get_text():
    """
    This function calls record_audio(), converts the audio into text and returns the text.
    """
    record_audio()
    r = sr.Recognizer()

    with sr.AudioFile(_WAVE_OUTPUT_FILENAME) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)
        return text
