import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser 
from wikipedia.wikipedia import search
import sys
import pyaudio

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voices',voices [0].id)

def speak(audio): 
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning ..!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon ..!")  

    elif hour>=18 and hour<22:
        speak("Good Evening ..!") 
    
    else:
        speak("Good Night ..!")     

    speak("hii,I'm Neurone,What can I do for You")   

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 50
        audio = r.listen(source,timeout=1,phrase_time_limit=10)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    
    except Exception as e:
        print("Say That Again Please...!")
        return "None"
    return query

if __name__=="__main__" :
        
        wishMe()
        while True:
            query = takeCommand().lower()
            
            if 'wikipedia' in query:
                speak('searching wikipedia...')
                query = query.replace("wikipedia", "")
                results = (wikipedia.summary(query, sentences=2))
                speak("According to Wikipedia")
                speak(results)
                print(results)

            elif 'Hello' in query:
                speak('Yes sir..! What can I do for You')
            
            elif 'open youtube' in query:
                speak('Sure sir')
                webbrowser.open("youtube.com")

            elif 'open google' in query:
                speak('Ok sir')
                webbrowser.open("google.com")
            
            elif 'search on chrome' in query:
                speak('What Should I Search Sir')
                search = takeCommand()
                chromepath = 'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
                webbrowser.get(chromepath).open_new_tab(search+'.com')

            elif 'exit' in query:
                speak('thanks for using me sir,Have a Good Day')   
                sys.exit()

            