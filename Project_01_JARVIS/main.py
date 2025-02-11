import speech_recognition as sr #as sr denotes short from for speech_recognition keyword
import webbrowser
import pyttsx3 #text to speech
import musicLibrary
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init() #initialize pyttsx
newsapi = "b3e30ef6a92043f498735d23bb4b83ef"

def speak(text): #speak func will take a text and convert it to speech
    engine.say(text)
    engine.runAndWait()
 
 #Opening music from music.py library
def processCommand(c):
    if "open google" in c.lower():  
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():  
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():  
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1] #Atfirst it will lower case the song and convert it to a list for Ex: "['play', "o jaana"]" and will pick the 1th position element from the list - song i.e 'o jaana'
        link = musicLibrary.music[song]
        webbrowser.open(link)

    
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            for article in articles:
                speak(article['title'])
    

    #Let OpenAI handle the request...
    else:
        pass


 
if __name__ == "__main__":
    speak("Initializing Code. Say jarvis to activate")
    # speak("Say Hello to activate.")
    while True:
        #Listen for the word Jarvis
        #obtain audion from microphone
        r = sr.Recognizer()
        
        
        print("recognizing....")
        #recognize speech using google
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)

            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Hi Speak")
                #Listen for command
                with sr.Microphone() as source:
                    print("Code active....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print("Error {0}".format(e))
            

        

