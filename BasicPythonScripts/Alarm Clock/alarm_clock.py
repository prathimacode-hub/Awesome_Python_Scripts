#importing playsound module pip install playsound
import time
import pygame
pygame.init()
# SONG for the alarm
SONG = pygame.mixer.Sound("Related/wake_up.mp3")
SONG.set_volume(0.1)
print("Clock type - 24 hour system")
#input hr(hours) and min(minutes) with am or pm
hour = int(input("Enter hour: "))
minute = int(input("Enter minutes: "))
#n=1 and condition always be true 
n=1
while n>0:
    #here local hour is compare with given input hr(hour) and local minute is compare with given input min(minutes)
    if time.localtime().tm_hour == hour and time.localtime().tm_min == minute:
        print("wake up!!!")
        SONG.play()
        while True:
            inpt = input("Type 'Stop' to off the alram : ")
            if inpt.lower() == 'stop':
                break # Break the inner while loop
        n = 0
