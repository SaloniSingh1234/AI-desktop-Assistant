import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Change index if needed


def speak(audio):
    """Converts text to speech"""
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    """Greets the user based on the current time"""
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Saloni . How may I assist you?")


def takeCommand():
    """Takes voice input from the user and returns it as text"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  # Allows pause before speaking
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query.lower()  # Return lowercase for easier comparison

    except Exception:
        print("Could you please repeat that?")
        return "none"


if __name__ == "__main__":
    wishMe()

    while True:
        query = takeCommand()

        if query == "none":
            continue  # If no command is detected, listen again

        # Wikipedia Search
        if "wikipedia" in query:
            try:
                speak("Searching Wikipedia...")
                query = query.replace("wikipedia", "").strip()
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia:")
                print(results)
                speak(results)
            except wikipedia.exceptions.DisambiguationError:
                speak("There are multiple results. Please be more specific.")
            except wikipedia.exceptions.PageError:
                speak("Sorry, I couldn't find any results on Wikipedia.")
            except Exception:
                speak("An error occurred while searching Wikipedia.")
            break  # Stops execution after running the command

        # Open Websites
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
            break

        elif "open google" in query:
            webbrowser.open("google.com")
            break

        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")
            break

        elif "open instagram" in query:
            webbrowser.open("instagram.com")
            break

        elif "open telegram" in query:
            webbrowser.open("telegram.org")
            break

        elif "open facebook" in query:
            webbrowser.open("facebook.com")
            break
        elif "open linkdin" in query:
            webbrowser.open("linkdin.com")
            break

        # Get Current Time
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
            break

        # Exit Command
        elif "exit" in query or "stop" in query:
            speak("Goodbye! Have a nice day.")
            break
