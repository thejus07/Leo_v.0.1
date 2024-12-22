import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import os


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()
engine.say('hello i am leo')
engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'leo' in command:
                command = command.replace('leo', '')
                print(command)
    except:
        pass
    return command


def run_leo():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'created you' in command:
        engine.say('i was created by master thejus. i am rely lucky to be created by him.')
        engine.runAndWait()
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with harshu')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif ' open ' in command:
        engine.say('opening..')
        os.open('C:/vector')
    else:
        talk('Please say the command again.')


while True:
    run_leo()
print("are you satisfied?")

input()