#importing necessary modules

import tkinter as tkr
from tkinter.filedialog import askdirectory
import os
import pygame

#To create the application window
musicplayer=tkr.Tk();

#setting the title of the window
musicplayer.title("Music Player")

#set the dimensions of the window
musicplayer.geometry("450x350")

#asks the music directory
directory=askdirectory();

#setting the music directory as current working directory
os.chdir(directory)

#creating our songlist
#os.listdir() returns a list containing the names of the entries given in the directory 
songlist = os.listdir()

#creating the playlist
playlist = tkr.Listbox(musicplayer,font='cambria 14 bold',bg="cyan2",selectmode=tkr.SINGLE)

#adding songs from songlist to playlist one by one in an ordered position
for item in songlist:
    pos=0
    playlist.insert(pos,item)
    pos=pos+1

# intialising pygame modules
pygame.init()
pygame.mixer.init()

# function for play button(ACTIVE is used here to state that only the selected music from playlist will be played) 
def play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))                     
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()

# function for stop button  
def ExitMusicPlayer():
    pygame.mixer.music.stop()
    
# function for pause button
def pause():
    pygame.mixer.music.pause()

# function for resume button
def resume():
    pygame.mixer.music.unpause()

#creating buttons
# pack - function is used for displaying in full (x-axis used here)

# play button is created and command=play(which is the function already created)
button_play = tkr.Button(musicplayer,height=3,width=5,text="Play Music",font="Cambria 14 bold", command=play, bg = 'lime green',fg="black")
button_play.pack(fill="x")

# stop button is created and command=ExitMusicPlayer(which is the function already created)
button_stop = tkr.Button(musicplayer,height=3,width=5,text="Stop Music",font="Cambria 14 bold", command=ExitMusicPlayer, bg='red',fg="black")
button_stop.pack(fill="x")

# pause button is created and command=pause(which is the function already created)
button_pause = tkr.Button(musicplayer,height=3,width=5,text="Pause Music",font="Cambria 14 bold", command=pause, bg = 'yellow',fg="black")
button_pause.pack(fill="x")

# resume button is created and command=resume(which is the function already created)
button_resume = tkr.Button(musicplayer,height=3,width=5,text="Resume Music",font="Cambria 14 bold", command=resume, bg = 'yellow',fg="black")
button_resume.pack(fill="x")     

# this is used for displaying the song title
var=tkr.StringVar()
songtitle=tkr.Label(musicplayer,font="cambria 12 bold", textvariable=var)
songtitle.pack()
playlist.pack(fill="both",expand="yes")

