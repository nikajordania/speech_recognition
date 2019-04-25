import speech_recognition as sr
import os
record = sr.Recognizer()
microphone = sr.Microphone()

def runProgramm(text):
    if str(text) == "google":
        os.system("start C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")

try:
    while True:
        with microphone as source:
            record.adjust_for_ambient_noise(source)
            audio = record.listen(source)
            result=record.recognize_google(audio,language="en_EN")
            result = result.lower()
            print(format(result))
            runProgramm(format(result))
except sr.UnknownValueError:
    print('Сервис google не отвечает')
