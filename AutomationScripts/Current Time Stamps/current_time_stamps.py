#Code for time in different timezones

#importing modules
import pendulum
import pyttsx3     #for speaking purpose

#function for speaking
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 170)  #rate of speaking
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)  #for female voice
    engine.say(text)
    engine.runAndWait()
    
# Code

speak("Hello! I will convert time in desired timezones.")

#current details
d1 = pendulum.now()

#splitting for getting date and time only
dt1 = str(d1).split(".")

speak("Here's your current timezone with current date and time")
print(f"Current timezone : {d1.timezone_name}")  #for displaying timezone
print(f"Current date and time: {dt1[0]}")  #as we splited time and timezon

speak("Now enter the zone you wish to see the time!")
i = input("Enter here: ")

#details for inputed timezone
try:
    d2 = pendulum.now(i)
    dt2 = str(d2).split(".")
    speak("Here's desired details")
    print(f" Current date and time for {d2.timezone_name} : {dt2[0]}")  
except Exception as e:
    speak("Looks like you have entered incorrect timezone!")
    speak("Please check it and try again!")