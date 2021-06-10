#importing playsound module pip install playsound
import time
from playsound import playsound
#input hr(hours) and min(minutes) with am or pm
hr = int(input("Enter hour: "))
min = int(input("Enter minutes: "))
amPm=str(input("am or pm"))
#n=1 and condition always be true 
n=1
while n>0:
    #here local hour is compare with given input hr(hour) and local minute is compare with given input min(minutes)
    if time.localtime().tm_hour == hr and time.localtime().tm_min == min:
        print("wake up!!!")
        playsound(r'C:\Users\HP\Downloads\13767_nice_larm_clock.mp3')#here path of alarm tune using playsound module
        break #when time match wake up!!! print with sound
    else:
        n+=1
