# Analog Clock

## Aim 

The main motive of this project is to create the virtual analog clock.

## Purpose

This project will the hour hand, minute hand and seconds hand in the clock to see the exact time. 

## Short description of package/script

- If standalone script, short description of script explaining what it achieves.
  
  It is a python scripts which implements the analog clock using GUI toolkit - pyqt5.

- List out the libraries imported.
  - PyQt5
  - Sys

## Setup instructions

Install the python2.8 or above

Download the analog_clock.py python file.

Extract the file.

Install the prerequisite for the program.

Then double click the python file to run..


## Work Flow
- Importing the Required modules
- Create a Clock class which inherits the QMainWindow class.
- Inside the Clock class creating a timer object which updates the whole code after each second. 
- Create three polygon objects for each hand of the clock hour, minutes and seconds.
- Create a paint event method for drawing purpose.
- Inside the paint event method get the current time and the minimum of windows width or height .
- Create a painter object and a method to draw the hands. 
- Inside the method for drawing hands(pointer) take arguments like color, rotation and and polygon object.
- Rotate the painter object and draw the pointer.
- Inside the paint event method, according to the current time set the rotation value and call the draw pointer method. 
- Draw the background image of the clock i.e lines for each hour. 
- Atlast the main loop executes the whole program.

## Output

![](https://github.com/rammya29/Awesome_Python_Scripts/blob/main/GUIScripts/Analog%20Clock/Images/Image-1.png)

## Author(s)

Rammya Dharshini K

## Disclaimers, if any

None
