import speech_recognition as sr
import os
import pyttsx3
record = sr.Recognizer()
microphone = sr.Microphone()

def runProgramm(text):
    if str(text) == "google":
        os.system("start C:\Program Files (x86)\Google\Chrome\Application\chrome.lnk")

try:
    while True:
        with microphone:
            record.adjust_for_ambient_noise(microphone)
            audio = record.listen(microphone)
            result = record.recognize_google(audio, language="ru_RU")
            result = result.lower()
            print(format(result))
            engine = pyttsx3.init()
            engine.say(format(result))
            engine.runAndWait()
            runProgramm(format(result))
except sr.UnknownValueError:
    print("google не отвечает")