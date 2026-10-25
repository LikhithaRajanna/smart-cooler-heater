import speech_recognition as sr
import sounddevice as sd
import numpy as np
import wave
import serial
import time

# ============================================================
# SERIAL CONFIGURATION
# ============================================================

try:
    ser = serial.Serial(
        'COM3',
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )

    time.sleep(1)
    serial_connected = True

except Exception as e:
    ser = None
    serial_connected = False
    print("Serial Error:", e)

def Send(data):
    if ser is not None and ser.is_open:
        ser.write(data.encode())
        print("Data sent:", data)
        
while True:
    duration = 5
    fs = 16000
    filename = "input_audio.wav"

    print("Speak now...")

    audio = sd.rec(
        int(duration * fs),
        samplerate=fs,
        channels=1,
        dtype=np.int16
    )

    sd.wait()

    print("Recording complete")

    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(fs)
        wf.writeframes(audio.tobytes())

    r = sr.Recognizer()

    with sr.AudioFile(filename) as source:
        audio_data = r.record(source)

    try:
        text = r.recognize_google(audio_data, language="en-US")
        text = text.lower()
        print("Recognized:", text)
        if text == 'heater 1' or text == 'heater one':
            Send('A')

        if text == 'heater 2' or text == 'heater two':
            Send('B')

        if text == 'cooler':
            Send('C')

        if text == 'stop' or text == 'exit' or text == 'end':
            Send('D')

    except sr.UnknownValueError:
        print("Could not understand audio")

    except sr.RequestError as e:
        print("Google API Error:", e)
