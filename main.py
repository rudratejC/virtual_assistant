import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser


admin='Rudratej'


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


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

    except:
        pass
    return command


def run():
    command = take_command()
    print(command)


    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)


    elif 'search' in command:
        try:
            se = command.replace('search', '')
            pywhatkit.search(se)
            talk("Searching...",se)
        except:
            print("An unknown error occured")


    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)

    elif 'facebook' in command:
        talk('opening facebook')
        webbrowser.open('http://www.facebook.com')


    elif 'youtube' in command:
        talk('opening youtube')
        webbrowser.open('http://www.youtube.com')


    elif 'stackoverflow' in command:
        talk('opening stackoverflow')
        webbrowser.open('http://www.stackoverflow.com')


    elif 'spotify' in command:
        talk('opening spotify')
        webbrowser.open('http://www.spotify.com')


    elif 'gmail' in command:
        talk('opening gmail')
        webbrowser.open('http://www.gmail.com')


    elif 'discord' in command:
        talk('opening discord')
        webbrowser.open('http://www.discord.com')


    elif 'netflix' in command:
        talk('opening netflix')
        webbrowser.open('http://www.netflix.com')


    elif 'github' in command:
        talk('opening github')
        webbrowser.open('http://www.github.com')


    elif 'geeks for geeks' in command:
        talk('opening geeks for geeks')
        webbrowser.open('http://www.geeksforgeeks.com')


    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)


    elif 'what is' in command:
        person = command.replace('what is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'stop' in command:
        exit()
    elif 'no thanks' in command:
        exit()
    elif 'quit' in command:
        exit()
    else:
        talk('I am unable to understand,can you say that again.')

talk("Hi"+admin)
talk("I'm your virtual assistant")
while True:
    talk("What can I do for you?")
    run()