import speech_recognition as sr
import pyttsx3
import webbrowser
import requests
from bs4 import BeautifulSoup

engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    print("Bot:", text)
    engine.say(text)
    engine.runAndWait()

def get_audio():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            query = recognizer.recognize_google(audio)
            print("You:", query)
            return query
        except:
            speak("Sorry, I didn't catch that.")
            return ""

def search_youtube(query):
    speak(f"Searching YouTube for {query}")
    search_url = f"https://www.youtube.com/results?search_query={query}"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, "html.parser")
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and "/watch?v=" in href:
            video_url = f"https://www.youtube.com{query}"
            webbrowser.open(video_url)
            return

def search_spotify(query):
    speak(f"Opening Spotify for {query}")
    query = query.replace(" ", "%20")
    spotify_url = f"https://open.spotify.com/search/{query}"
    webbrowser.open(spotify_url)

# -------- Main Bot Loop --------
speak("What song do you want to play?")
command = get_audio().lower()

if "youtube" in command:
    song = command.replace("on youtube", "").strip()
    search_youtube(song)
elif "spotify" in command:
    song = command.replace("on spotify", "").strip()
    search_spotify(song)
else:
    speak("Do you want to play it on YouTube or Spotify?")
    platform = get_audio().lower()
    if "youtube" in platform:
        search_youtube(command)
    elif "spotify" in platform:
        search_spotify(command)
    else:
        speak("Sorry, I couldn't understand the platform.")
