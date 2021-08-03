import pyttsx3 as py #Text to speech Library
import datetime #Date & Time Library
import speech_recognition as sr #Speech recognition
import wikipedia #Wikipedia Library
import urllib.request #URL Library
import os #Operating System Library
import pyaudio #Audio Library
------------ #Intialization -----------
engine = py.init('sapi5')
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio): #Audio Output
    engine.say(audio)
    engine.runAndWait()

def wishme(): #Greetings
    hour =int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("Good Morning!, Durga Sai ")
    elif(hour>=12 and hour<18):
        speak("Good Afternoon, Durga Sai ")
    else:
        speak("Good Evening, Durga Sai")
    speak("Im wiki bot how may i help you today")


---------------- #Navigation ---------------
def navigate():  
    r= sr.Recognizer() #Speech
    with sr.Microphone() as source:
        print("Tell me what you want to search on wikipedia ?")
        r.pause_threshold=1
        audio = r.listen(source) #To listen (input)
    try:
        print("Please Wait sir, Search in progress...")
        result = r.recognize_google(audio,language='en-in')
        print(f"You said:{result}\n") #Confirmation
        speak(result) #Output


    except Exception as e: #Exceptions

        return "None"
    return result
def image(query): #Relevant Image from Wiki
    query = query.replace(" ","_".lower())
    page_image = wikipedia.page(query)
    image_down_link = page_image.images[5]

    urllib.request.urlretrieve(image_down_link , "loc.jpg")
    os.startfile("loc.jpg") #Image display

if __name__ == '__main__':
    wishme()
    query = navigate().lower()
    if "wikipedia "  in query:
        speak("searching in wiki hang on...!")
        query = query.replace("wikipedia ","")
        result =wikipedia.summary(query,sentences=2)
        image(query)
        speak("According to wiki..")
        page_image = wikipedia.page(query)
        image_down_link = page_image.images[0]
        urllib.request.urlretrieve(image_down_link , "loc.jpg")
        print(result)
        speak(result) #Output
    elif '' in query:
        try:

            speak("searching in wiki hang on...!")
            query = query.replace("","")
            result =wikipedia.summary(query,sentences=3)
            speak("According to wiki..") #Result found
            print(result)
            image(query)
            speak(result)
        except Exception as e:
            speak("Im sorry i could not found your query") #No result
    else:
        speak("Im sorry i could not found your query")#No result
