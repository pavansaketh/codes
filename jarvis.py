import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty("voice",voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("good morning!")
    elif hour >=12 and hour < 18:
        speak("good afternoon!")
    else:
        speak("good evening!")
    speak("I am jarvis. please tell me how may i help you!")

def takecmd():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...........")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing..........")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        speak("Say that again please!")
        return "None"

    return query

if __name__  == "__main__":
    wish()
    while True:
        query = takecmd().lower()


        if "wikipedia" in query:
            speak("searching wikipedia!")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query,summary = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")

        elif "play movie" in query:
            movie_dir = "E:"
            movies = os.listdir(movie_dir)
            print(movies)
            os.startfile(os.path.join(movie_dir, movies[0]))

        elif "what is time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"The time is {strTime}")

        elif "open code" in query:
            path = "C:\\Users\\Vedala Sesha p\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)

        elif "stop" in query:
            quit()
            