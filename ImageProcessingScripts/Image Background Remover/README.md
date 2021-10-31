# Image Background Remover

# Aim
This project helps in removing the background of an image and just focuses on foreground and changes the background to yellow.

# Purpose
In this project a normal image gets it background removed using a single script.

# Short description of package/script
>>This project contains a script bgremover.py which helps to remove the background of an image.
>>It uses Open CV library to manipulate pixels of the image
>>Numpy is used because Open CV stores images in form of numpy array and it can be manipulated easily by performing numpy operations.

# Workflow of the Project
User will enter the name of the file present in the media folder whose background is to be removed then the program will process the image and remove the background and will only focus on its foreground. Then simply the converted file will be opened and displayed with the changes.

# Detailed Setup instructions
The first step is to install python and fulfill all the requirements mentioned in "requirements.txt". Then copy your images to the Media folder. The extension of image should be .jpg to get the best results.
After running the program you will get the image converted as per your need and will be visible to you on the screen as output.

# Compilation Steps
In this we are using cv2 and numpy to read the images and then store it in the form of array. Then with the help of edge detection, contours and blurring the image the pixels are properly set and the new image is displayed on the screen and the focus is just on the foreground.

# Conclusion
This image processing script helps the user to instantly give focus to just the foreground of an image and removes it background.

# Screenshot

![Image Background Remover](Media/Screenshot1.jpg)


![Image Background Remover](Media/Screenshot2.jpg)

# Author

Khushi Sharma