## Neon/Glow Filter Of An Image

# Aim
This project helps in converting an image into glow/neon image.

# Purpose
In this project a normal RGB image is converted into its neon or glow image using a single script.

# Short description of package/script
>This project contains a script neon.py which helps to convert image into neon or glow image.
>It uses Open CV library to manipulate pixels of the image
>Numpy is used because Open CV stores images in form of numpy array and it can be manipulated easily by performing numpy operations.

# Workflow of the Project
User will enter the name of the file present in the media folder then the program will process the image and convert it into neon/glow image. Then simply the converted file will be created with both the images concattenated for comparision purposes. The new file created will be automatically saved and renamed as "Neon of FILENAME".

# Detailed Setup instructions
The first step is to install python and fulfill all the requirements mentioned in requirements.txt. Then copy your images to the Media folder. The extension of image should be .jpg to get the best results.
After running the program you will get the image converted as per your need and will get saved automatically in the same directory.

# Compilation Steps
In this we are using cv2,matplotlib and numpy to read the images and then store it in the form of array. Then with the help of matrix multiplication and setting the pixels properly we get the new image. Then, we finally merge the old and the new image together for better comparision/visualisation purpose and display it and save the image as final output.

# Conclusion
This image processing script helps the user to instantly beautify their image and give it a glow by one simple step.

# Screenshots

![Neon Filter](Media/Screenshot 1)


![Neon Filter](Media/Screenshot 2)


# Author

Khushi Sharma