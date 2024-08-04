import pyaudio
import wave
from gtts import gTTS
import pygame
import os
import time

def clean_text(text):
    return text.strip().lower()

def respond_to_text(text):
    cleaned_text = clean_text(text)
    if "привет я разработчик" in cleaned_text:
        response = "сегодня выходной"
    elif "я сегодня не приду домой" in cleaned_text:
        response = "ну и катись отсюда"
    else:
        response = "непонятная команда"
    return response

def text_to_speech(text):
    tts = gTTS(text=text, lang='ru')
    tts.save("response.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("response.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    pygame.mixer.music.unload()  # Ensure the file is closed
    try:
        os.remove("response.mp3")
    except PermissionError:
        print("Не удалось удалить файл, так как он занят другим процессом.")

def record_audio(filename):
    chunk = 1024
    format = pyaudio.paInt16
    channels = 1
    rate = 16000
    record_seconds = 5

    p = pyaudio.PyAudio()

    print("Начинается запись. Пожалуйста, произнесите ваш текст...")
    stream = p.open(format=format,
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=chunk)

    frames = []

    for i in range(0, int(rate / chunk * record_seconds)):
        data = stream.read(chunk)
        frames.append(data)

    print("Запись закончена.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(format))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()
