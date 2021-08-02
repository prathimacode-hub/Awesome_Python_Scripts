# Package/Script Name

## Aim 

The main aim of the project is to detect the Lane from the image.

## Purpose

Purpose of the script is to detect Lane from the Image and make it more and more accurate.

## Short description of package/script

- This project help us to detect the Road Lane.
- Libraries Imported :
    - CV2
    - Matplotlib
    - Numpy


## Workflow of the Project

- Here Firstly the image is read from Images folder using OpenCV library.
- Setting the region of interest between which the road lane is their. (mentioned data is according to the given input, If u want to try your own input image try to change the value and after testing fix the region).
- Converting the image to grey scale image.
- Using canny's edge detection function, detecting the edge.
- Using HoughLines function detecting the points from the canny's detected image.
- At last drawing the line and showing the output as Detected_Lane.jpg file. 



## Setup instructions

First install the above mentioned library, If you want to detect lane on your given input just changge the path in cv2.imread function and set your path and run the file.

## Compilation Steps:
   - Install CV2, Matplotlib and Numpy library in your system. (syntax : pip install library_name)
   - Clone the project on local system.
   - Execute/Run .py file and get the output.

## Output
- Input Image
    - ![road](https://user-images.githubusercontent.com/69030530/127738802-a2c310ba-e59e-4c2f-9960-16bd2fc4faab.jpg)

- Output Image
    - ![Detected Lane](https://user-images.githubusercontent.com/69030530/127738814-3cc4f9c3-eca5-4cb1-a2e2-8bcb91b7bf36.jpg)
 


## Author(s)

Harsh Ved

