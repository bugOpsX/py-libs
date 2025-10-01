# DSA/utils/text_to_speech.py

"""
Text-to-Speech (TTS) Library 🎤

This module converts text to speech using the pyttsx3 library.
It provides both function-based and command-line usage.

Usage (Library):
    from DSA.utils.text_to_speech import speak
    speak("Hello world!")

Usage (CLI):
    python3 DSA/utils/text_to_speech.py "Hello world!"
"""

import pyttsx3
import sys

# Initialize the TTS engine
engine = pyttsx3.init()

def speak(text, rate=150, volume=1.0, voice=None):
    """
    Convert text to speech and play it aloud.

    :param text: str - Text to speak
    :param rate: int - Speech rate (default 150 words/min)
    :param volume: float - Volume (0.0 to 1.0, default 1.0)
    :param voice: str - Voice id (optional)
    """
    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)

    if voice:
        engine.setProperty('voice', voice)

    engine.say(text)
    engine.runAndWait()


def cli():
    """Command-line interface for text-to-speech."""
    if len(sys.argv) < 2:
        print("Usage: python3 DSA/utils/text_to_speech.py \"Your text here\"")
        return

    text = " ".join(sys.argv[1:])
    speak(text)
    print(f"🔊 Spoken: {text}")


if __name__ == "__main__":
    cli()
