import speech_recognition as sr
import webbrowser
import edge_tts
import asyncio
import pygame
import MusicLibrary
import os
import subprocess
from datetime import datetime
import wikipedia

r = sr.Recognizer()

async def speak_async(text):
    communicator = edge_tts.Communicate(text, voice="en-GB-RyanNeural", rate="+25%")
    await communicator.save("speech.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("speech.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove("speech.mp3")

def speak(text):
    asyncio.run(speak_async(text))

def processCommand(c):
    if "open google" in c.lower():
        speak("opening google")
        webbrowser.open("https://google.com")
    elif "open insta" in c.lower():
        speak("opening insta")
        webbrowser.open("https://instagram.com")
    elif "open youtube" in c.lower():
        speak("opening youtube")
        webbrowser.open("https://youtube.com")
    elif "open chat" in c.lower():
        speak("opening chat g p t")
        webbrowser.open("https://chatgpt.com")
    elif "open github" in c.lower():
        speak("opening github")
        webbrowser.open("https://github.com")
    elif "open mail" in c.lower():
        speak("opening mail")
        webbrowser.open("https://mail.google.com")
    elif "open spotify" in c.lower():
        speak("opening spotify")
        webbrowser.open("https://spotify.com")

    elif "who is" in c.lower():
        person = c.lower().replace("who is", "")
        result = wikipedia.summary(person, sentences=2)
        speak(result)    

    elif "search" in c.lower():
        query = c.lower().replace("search", "")
        webbrowser.open(f"https://www.google.com/search?q={query}")    

    elif "time" in c.lower():
        speak(f"It is {datetime.now().strftime('%I:%M %p')}") 
    elif "date" in c.lower():
        speak(f"Today is {datetime.now().strftime('%B %d, %Y')}")      


    elif "open notepad" in c.lower():
        os.system("notepad")
    elif "open calculator" in c.lower():
        os.system("calc")
    elif "open paint" in c.lower():
        os.system("mspaint")


    elif "open chrome" in c.lower():
        subprocess.Popen(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
    elif "shutdown" in c.lower():


        os.system("shutdown /s /t 1")
    elif "restart" in c.lower():
        os.system("shutdown /r /t 1")


    elif c.lower().startswith("play"):
        song = " ".join(c.lower().split(" ")[1:])
        link = MusicLibrary.music.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak(f"Sorry, I don't have {song} in the library")
    else:
        speak("Sorry, I didn't understand that command")
        

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.2)
                print("Listening...")
                audio = r.listen(source, timeout=3, phrase_time_limit=2)
            word = r.recognize_google(audio)
            if "jarvis" in word.lower():
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)
        except Exception as e:
            print(f"Error: {e}")