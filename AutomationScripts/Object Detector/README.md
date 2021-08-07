# Object Detector

## Aim

The aim is to make a program that will detect an object of the users choice in an image the user provides.

## Purpose

The purpose of this program is to help automate the task of object detection in an image. 

## Short description of package/script

- The program draws a green rectangle around the object you want it to find in the image. It does this using the OpenCV library and the program requires two images as input. The first image is of the object you want the program to detect and the second image is the image in which you want to detect the object.
- OpenCV


## Workflow of the Project

- Make sure that the terminal's working directory is the directory where the project is
- Type in "python object_detector.py path1 path2" where path1 is the file path of the image with the object  you want to find in the image in path2


## Setup instructions

- Install OpenCV: pip install opencv-python


## Output

<p align="center"><img src="https://github.com/BMaster123/images/blob/main/plant_detection.PNG"></p>


## Author(s)

Bhavesh Mandalapu


## Disclaimers, if any

This program does not work all the time. It may draw a rectangle around an area where the object isn't present. The program also cannot detect more than one object for the time being.