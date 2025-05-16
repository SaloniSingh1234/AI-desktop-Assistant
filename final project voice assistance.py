import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes

# Initialize TTS engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Saloni. How may I assist you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        return query.lower()
    except Exception:
        print("Could you please repeat that?")
        return "none"


def openWebsite(website):
    urls = {
        "youtube": "https://www.youtube.com",
        "google": "https://www.google.com",
        "stackoverflow": "https://stackoverflow.com",
        "facebook": "https://facebook.com",
        "instagram": "https://instagram.com",
        "linkedin": "https://linkedin.com",
        "telegram": "https://telegram.org"
    }
    if website in urls:
        webbrowser.open(urls[website])
        speak(f"Opening {website}")
    else:
        speak("Sorry, I don't know that website.")


def playMusic():
    webbrowser.open("https://open.spotify.com")
    speak("Opening Spotify in your browser.")


def openApp(app_name):
    apps = {
        "notepad": "C:\\Windows\\System32\\notepad.exe",
        "calculator": "C:\\Windows\\System32\\calc.exe",
    }
    if app_name in apps:
        os.startfile(apps[app_name])
        speak(f"Opening {app_name}")
    else:
        speak("Sorry, I can't open that application.")


def searchGoogle(query):
    search_term = query.replace("search google for", "").strip()
    webbrowser.open(f"https://www.google.com/search?q={search_term}")
    speak(f"Searching Google for {search_term}")


def tellTime():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The time is {strTime}")


def tellDate():
    today = datetime.date.today()
    speak(f"Today's date is {today.strftime('%B %d, %Y')}")


def tellJoke():
    joke = pyjokes.get_joke()
    speak(joke)


def addTodo():
    speak("What task should I add?")
    task = takeCommand()
    with open("todo.txt", "a") as file:
        file.write(task + "\n")
    speak("Task added to your to-do list.")


def setReminder():
    speak("What should I remind you about?")
    reminder = takeCommand()
    with open("reminder.txt", "a") as file:
        file.write(reminder + "\n")
    speak("Reminder saved.")


if __name__ == "__main__":
    wishMe()

    while True:
        query = takeCommand()

        if query == "none":
            continue

        elif "wikipedia" in query:
            speak("Searching Wikipedia...")
            try:
                query = query.replace("wikipedia", "").strip()
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia:")
                print(results)
                speak(results)
            except:
                speak("Sorry, I couldn't find results on Wikipedia.")

        elif "open" in query:
            for site in ["youtube", "google", "stackoverflow", "instagram", "facebook", "linkedin", "telegram"]:
                if site in query:
                    openWebsite(site)
                    break

        elif "play music" in query:
            playMusic()

        elif "open notepad" in query or "open calculator" in query:
            app = "notepad" if "notepad" in query else "calculator"
            openApp(app)

        elif "search google for" in query:
            searchGoogle(query)

        elif "the time" in query:
            tellTime()

        elif "date" in query:
            tellDate()

        elif "tell me a joke" in query or "joke" in query:
            tellJoke()

        elif "add to-do" in query:
            addTodo()

        elif "remind me" in query:
            setReminder()

        elif "exit" in query or "stop" in query or "bye" in query:
            speak("Goodbye! Have a great day.")
            break

        else:
            speak("I didn't understand that. Please try again.")


