from recognizer import compare_models
from utils import respond_to_text, text_to_speech, record_audio
import os

def main():
    filename = "input.wav"
    while True:
        record_audio(filename)
        recognized_text = compare_models(filename)
        
        response_text = respond_to_text(recognized_text)
        text_to_speech(response_text)
        print(f"Распознанный текст: {recognized_text}")
        print(f"Ответ: {response_text}")
        
        os.remove(filename)
        
        repeat = input("Хотите попробовать снова? (да/нет): ").strip().lower()
        if repeat != "да":
            break

if __name__ == "__main__":
    main()
