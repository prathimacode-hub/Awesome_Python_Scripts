import psutil #Process and system utilities Library
import time #Time Library
import pyttsx3 #Text to Speech conversion Library
from win10toast import ToastNotifier #ToastNotifier from win10toast Library
import threading #Threading Library

# ------------- Intialization of Libraries ------------
toaster = ToastNotifier() 
x = pyttsx3.init()
x.setProperty('rate', 130) 
x.setProperty('volume', 8)
count = 0

#------------Desktop Notification ---------------
def show_notification(show_text): 
    toaster.show_toast(show_text, icon_path='battery_indicator.ico',duration=10)
    while toaster.notification_active():
        time.sleep(0.1)

#----------- Operation -----------
def monitor():
    while (True):
        time.sleep(10) #delay
        battery = psutil.sensors_battery() #Battery Status
        plugged = battery.power_plugged
        percent = int(battery.percent)

        if percent < 40: #Low battery
            if plugged == False:
                processThread = threading.Thread(target=show_notification, args=( "Your Battery at " + str(percent) + "% Please plug the cable",))  #Note extra ',' (if you don't keep thos you won't be getting message notification.)
                processThread.start()
                x.say("Hey Durga Sai, Your Battery at " + str(percent) + "% Please plug the cable")
                x.runAndWait()
                count = 0
        elif percent == 100: #Full Battery
            if plugged == True:
                processThread = threading.Thread(target=show_notification, args=(" Battery Charged",))
                processThread.start()
                x.say("Hey Durga Sai, Battery Full Please plug out the cable ")
                x.runAndWait()
        elif percent >= 90: #Over Charging
            if plugged == True:
                processThread = threading.Thread(target=show_notification, args=("Your Battery at " + str(percent) + "% Please unplug the cable",))
                processThread.start()
                x.say("Hey Durga Sai, Your Battery at", + str(percent) + "% Please detach the cable")
                x.runAndWait()
if __name__ == "__main__":
    monitor()
