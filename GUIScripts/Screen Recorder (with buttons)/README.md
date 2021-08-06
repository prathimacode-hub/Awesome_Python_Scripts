# Screen Recorder (With Buttons)

<img src = "https://i.giphy.com/media/5SxbXVr3dkGzIUdYqB/giphy.webp" width = "300px">

## Aim

This project is a Screen Recorder which is made using Tkinter and Pyautogui Libraries and it has buttons to let user record, pause or end the recording
<img src = "https://github.com/TusharAMD/Awesome_Python_Scripts/blob/screenrecgui/GUIScripts/Screen%20Recorder%20(with%20buttons)/Image/animation.gif?raw=true"></img>
![Youtube Link](https://youtu.be/IgeJn3g9XwM)

## Purpose

Sometimes we need a screen recorder but we don't find any free tools online which are unlimited and watermark free. So why don't we make a open source script which can enable anyone who wish to record screen can simply run script and make a video file.  

## Short description of package/script

- This script using GUI tool tkinter to let user record their screen
- User simply needs to run script and screenshots will be taken by pyautogui library
- User can also pause video whenever necessary
- After user is satisfied he/she can press stop button and then all files will be compiled and stiched into video file
- This file can be then accessed from same folder and it will have a unique name 


## Workflow of the Project

1. First we are importing all required libraries and then creating a cv2 blank window
2. Constants like file path are stored in variable. (This must be changed from PC to PC)
3. All Images will be stored in Images folder and so if such folder exists then remove it
4. Run tkinter window and run program function which continuously takes screen shot
5. If pause button is pressed tkinter loop will continue but screeshots will not be taken
6. After pressing Stop button the video is saved



## Setup instructions

1. Install all packages in requirements.txt file by using pip install -r requirements.txt
2. Run screenrec.py file.
3. Now you can see record, pause and stop buttons which functions as per name
4. You can resize the live feed window or minimize it.
5. After recording simply save the record by clicking stop button
6. Video File will be generated 

## Compilation Steps

Program Function is the most significant function in this script which takes screenshots using pyautogui library and stores output in the Images Folder.
This function is placed inside tkinter mainloop and its called continuously till user presses stop button when window is destroyed.
After tkinter is closed the files are traversed using glob library and sorted according to date and time. The files are compiled and then stitched together into a video file and saved with unique name in to the same folder


## Output
![Screenshot](https://github.com/TusharAMD/Awesome_Python_Scripts/blob/screenrecgui/GUIScripts/Screen%20Recorder%20(with%20buttons)/Image/screenshot.png?raw=true)

## Author(s)

Tushar Amdoskar

[Tushar's Website](https://tusharamd.github.io/)
