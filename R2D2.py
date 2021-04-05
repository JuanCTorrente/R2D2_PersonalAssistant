import speech_recognition as rd
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = rd.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with rd.Microphone() as source:
            print('......')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'artwo' in command:
                command = command.replace('artwo','')
                print(command)

    except:
        pass
    return command

def run_artwo():
     command = take_command()
     print(command)
     if 'play' in command:
         song = command.replace('play', '')
         talk('playing ' +song)
         pywhatkit.playonyt(song)
     elif 'time' in command:
         time = datetime.datetime.now().strftime('%I:%M:%S %p')
         talk('Exact time is ' + time)
     elif 'who is' in command:
         person = command.replace('who is', '')
         info = wikipedia.summary(person, 1)
         print(info)
         talk(info)
     elif 'joke' in command:
         talk(pyjokes.get_joke())
     else:
         talk('Please say the command again.')


while True:
    run_artwo()