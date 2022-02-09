import os
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit=5)

    try:
        trigger = r.recognize_google(audio, language='en-in')

        return trigger
    except Exception:
        return 'None'
    return trigger


while 1:
    flag = 0
    trigger = takecommand().lower()
    print(trigger)
    if "vivah on" in trigger:
        flag = 1
        break

if flag == 1:
    speak("vivah is ON")
    # os.system('temp.py')
    from temp import mains
    mains()
