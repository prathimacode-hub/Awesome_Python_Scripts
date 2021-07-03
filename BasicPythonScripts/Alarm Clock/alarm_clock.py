# Import modules
import time
import pygame

# Setup the music
pygame.mixer.init()
SONG = pygame.mixer.Sound('Related Files/wake_up.mp3')
SONG.set_volume(0.1)

# Taking Time for alarm clock
print("Clock type - 24 hour system")
hour = int(input("Enter hour: "))
minute = int(input("Enter minutes: "))

run = 1
while run > 0:
    #here local hour is compare with given input hour and local minute is compare with given input minute
    if time.localtime().tm_hour == hour and time.localtime().tm_min == minute:
        print("wake up!!!")
        # Playing Song
        SONG.play(-1)
        while True:
            # if userinput == stop then off the alarm
            stop = input("Type 'stop' to off the alram : ")
            if stop.lower() == 'stop':
                run = 0
                break