import speech_recognition as sr
import sys
import webbrowser
import pyttsx3

r = sr.Recognizer()
microphone = sr.Microphone()

def talk(words):
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()

def command():
	with microphone as source:
		print("say")
		r.pause_threshold = 1
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)

	try:
		voice = r.recognize_google(audio, language="en_EN")
		voice = voice.lower()
		print("you said: {}".format(voice))

	except sr.UnknownValueError:
		talk("I did not understand")
		voice = command()
	return voice

def makeSomething(voice):
	if voice == "open site":
		talk("opening")
		url = "https://www.google.com/"
		webbrowser.open(url)
	elif voice == "stop":
		talk("Yes of course")
		sys.exit()
	elif voice =="what is your name":
		talk("my name is siri")

while True:
	makeSomething(command())