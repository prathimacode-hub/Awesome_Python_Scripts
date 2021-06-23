
# Music Player

## Aim:

-To create a music player using python GUI and pygame, which enables the user to view the list of songs in the directory,The user can choose the song and play,stop,pause and resume using the buttons available. User can switch from one song to another song by clicking and choosing appropriate buttons.

## Purpose:

- To listen to different songs at ease switch between different songs in same diretory. Pause and resume the songs whenever needed.

## Description:

- This project is to build a music player using tkinter and pygame
- For creation of Music Player Using Python, we will need to import Python modules one for creating GUI,and Pygame for using  font for displaying time and another to get datetime data.
- For GUI we will use **"tkinter module"**.
- **"Pygame"** is used for creating video games which includes computer graphics and sound libraries, we are going to utilize this for sound components and functions like stop the music, pause the music, play the music and resume the music.
- And to get file directory and information we use **"filedialog from tkinter and Os module"**.

## About this Application:

- When we Run this application
- First the user will see the prompt to select the music directory
- After selecting the music directory, the music playlist gets added
- User can see 4 options 1) Play Music 2) Stop Music 3) Pause Music 4) Resume Music
- User can click on the music in the playlist and choose the options displayed on the top 
- The window of the application is expandable

## Procedure: 
```python
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os
import pygame
```
- After importing modules, we will create a window and name the window as Music Player and set the dimenstions of the window
- Now we create functions for prompting the window to select music directory and add the songs in the directory to the playlist.
- We then create functions for play,stop,pause and resume using pygame.
- Buttons are created for all the functions and displayed in the window
- The format for displaying the colors and fonts can also be changed according to our wish.

## Compilation Steps:

- Install pygame module using pip install pygame in windows powershell (admin)
- Create a directory with list of songs you wish
- Import the neccessary modules and run the program
- Choose the Music directory and listen to the songs

## Sample Output:
![Image](https://user-images.githubusercontent.com/53329034/122674245-e1c46480-d1f1-11eb-9914-1fc8c790ae69.png)

