import os
import sys
import json
import pyaudio
from vosk import Model, KaldiRecognizer
import subprocess

# Load the Vosk model
model_path = ""  # Update this to your model path
freyja_path = "" # Update this to your freyja path

if not os.path.exists(model_path):
    print("Model not found. Please download a model from https://alphacephei.com/vosk/models")
    sys.exit(1)

model = Model(model_path)

recognizer = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

print("Listening for wake word...")

wake_word = "wake up"

while True:
    result_str = subprocess.run(['ps', '-eo', 'args'], capture_output=True, text=True)
    contains_is = freyja_path not in result_str.stdout
    if contains_is:
        data = stream.read(8000, exception_on_overflow=False)
        if recognizer.AcceptWaveform(data):
            result = recognizer.Result()
            result_json = json.loads(result)

            if 'text' in result_json:
                recognized_text = result_json['text']
                print(f"Recognized: {recognized_text}")
                if wake_word in recognized_text:
                    result_run = subprocess.Popen(["kitty", "--hold", freyja_path])
                    print(f"Wake word '{wake_word}' detected!")
