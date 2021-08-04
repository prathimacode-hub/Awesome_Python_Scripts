# Privacy Virtual Camera
![Privacy](https://cdn0.iconfinder.com/data/icons/bubbly-icons/512/Eye_Sight_Privacy_Visibility_Retina_Look_View_Search-512.png)


## Aim

This project is a virtual camera that will be made using OpenCV which will enable user to hide his/her face during video call and only outline of their face will be seen.

![Animation](https://github.com/TusharAMD/Awesome_Python_Scripts/blob/Python_Virtual_Camera/ImageProcessingScripts/Privacy%20Virtual%20Camera/Images/Screenshots/animation.gif?raw=true)

## Purpose

There are many reasons when users don't wish to show their face and don't want the other person to recognize their identity from their voice. In simpler words, users wish to hide identity and at the same time have a video chat. There can be various examples like medical help, or if the judge has to provide an unbiased verdict without knowing someone's race, gender, etc. For such reasons, we can use just an outline of the face and the speech will be converted into text and will be displayed below the video.

## Short description of package/script

- This program uses virtual camera technique to convert open cv video output stream into camera input
- It is necessary to have OBS virtual camera plugin to be installed
- When the user runs vcam.py file the virtual camera will be started and he/she can use that camera in any meeting application
- Also user can speak through their microphone and text will be displayed.


## Workflow of the Project

1. User face is captured and send into script
2. Face mesh is created and placed on plain canvas
3. At same time user microphone input is taken and converted into text
4. This is saved in text file and then retrieved from there into program function
5. Text is placed in image and send to virtual camera
6. This image now can be displayed in video chat



## Setup instructions

1. Install OBS virtual camera plugin
2. Attach Webcamera and Microphone to PC
3. Run vcam.py script
4. You can optionally change the image of mask, color of face outline and also background
5. Open any meet application and in camera section select OBS virtual camera
6. You should see privacy virtual camera output on the screen

## Compilation Steps

This program using multiprocessing and it runs 2 functions i.e. "takesinput" and "program" simultaneously.
When user runs the script a plain canvas of specified solid color is created.
On that the face mesh is placed using mediapipe library
Also a face mask can be applied on eyes.
The face mask are placed according to the eye position and also size is mantained in respect of face dimensions.
In takesinput function the microphone input is converted into text using speech recognition library and displayed on the canvas
This image is then send to virtual camera and can me used in any meet application


## Output

![3](https://raw.githubusercontent.com/TusharAMD/Awesome_Python_Scripts/Python_Virtual_Camera/ImageProcessingScripts/Privacy%20Virtual%20Camera/Images/Screenshots/3.jpg)
![1](https://raw.githubusercontent.com/TusharAMD/Awesome_Python_Scripts/Python_Virtual_Camera/ImageProcessingScripts/Privacy%20Virtual%20Camera/Images/Screenshots/1.jpg)
![2](https://raw.githubusercontent.com/TusharAMD/Awesome_Python_Scripts/Python_Virtual_Camera/ImageProcessingScripts/Privacy%20Virtual%20Camera/Images/Screenshots/2.jpg)


## Author(s)

Tushar Amdoskar

[Tushar's Website](https://tusharamd.github.io/)
