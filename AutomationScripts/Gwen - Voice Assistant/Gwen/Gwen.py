import pyttsx3 as px 
import speech_recognition as sr 

from browser import *
from youtube import *
from weather import *
from gmail import *
rx = px.init() # instance of init class
#it gets the info of the current driver in use
rate= rx.getProperty('rate')
rx.setProperty('rate',150)
voices=rx.getProperty('voices')
rx.setProperty('voice',voices[1].id)



def speak(text):
    rx.say(text)
    rx.runAndWait() #ask the computer to wait untill the sentence gets finished

r = sr.Recognizer()#instance of Recognizer class.It helps to retrive information from a source
speak('Hey I am Gwen, Your voice assistant.')
def listening():
    with sr.Microphone() as source:
        r.energy_threshold=10000    #increases the spectrum of voice
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source,1.2)#cancels the noise
        print("Listening....")
        audio=r.listen(source)
        try:
            text = r.recognize_google(audio)#send the audio to google api engine which returns the text of the audio
            print(text)
            
        except Exception as e:
            print(e)
            speak(e)
            return None
        return text
def call(text):

    if "Gwen" in text:
        return True
    return False
while True:
    try:
        text = listening()
        if call(text):
            if "Hey Gwen you there" in text:
                speak('Yes Sir, At your service')
            elif "Hii Gwen " in text:
                speak("Hii, Paras. How are you?")
           
            elif "what" and "about" and "you" in text:
                speak("I am having a good day  .")
            speak("What can I do for you?")

            text2=listening()


            if "what will be the weather today" in text2:
                speak(des())

            if 'tell me about' in text2:
                inf=" ".join(text2.split()[3:])
                print(f"Searching {inf} in Google ")
                speak(f"Searching {inf} in Google ")
                assist = info()
                text=assist.get_info(inf)
                speak(text)

            elif  "how much" in text2:
                x=" ".join(text2.split()[3:])
                print(f"Searching {x} in Google ")
                speak(f"Searching {x} in Google ")
                assist=info()
                text=assist.get_info(x)
                speak(text)

            elif  "is" in text2:

                print(f"Searching {text2} in Google ")
                speak(f"Searching {text2} in Google ")
                assist=info()
                text=assist.get_info(text2)
                speak(text)

            elif "get me a tutorial" in text2:
                tutorial=" ".join(text2.split()[5:])
                print(f"Searching a tutorial for {tutorial} in Youtube")
                speak(f"Searching a tutorial for {tutorial} in Youtube")
                
                assist = music()
                assist.play(tutorial)
            elif "play" in text2:
                song=" ".join(text2.split()[1:])
                
                print(f"Playing {song} in Youtube")
                speak(f"Playing {song} in Youtube")
                
                assist = music()
                assist.play(song)

            elif "mail" in text2:
                name="".join(text2.split()[4:])
                speak("Email address of the "+name)
                
                to=listening()
                speak("Subject of the mail?")
                sub=listening()
                speak("Body of the mail")
                mssg=listening()
                assist=email()
                txt=assist.mail(to,sub,mssg)
                speak("Sending an email to "+ name)
                speak(txt +name)
            elif 'stop' in text2 or 'quit' in text2:
                break
    except:
        pass
