import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import  wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()

            if 'alexa' in command:
                command = command.replace('alexa','')
                print(command)

    except sr.UnknownValueError:
            talk('Please give me some command')
            command = None
            while True:
                run_alexa()
    return command

def run_alexa():
    command = take_command()
    if 'play' in command:
        song = command.replace('play','')
        talk('playing'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is'+time)
    elif 'info about' in command:
        person = command.replace('info about','')
        info=wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'hello' in command:
        talk('hello,nice to meet u')
    elif 'what is your name' in command:
        talk('i am alexa,what is your name?')
    elif 'who are you' in command:
        talk('i am alexa')
    elif 'my name' in command:
        talk('oh!hi nice to meet u')
    elif 'date' in command:
        talk('sorry,i have a headache')
    elif 'are you single' in command:
        talk('i am in a relationship with wifi!!')
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
    else:
        talk('please say the command again')


while True:
    run_alexa()