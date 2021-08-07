# Image Ghost Filter

<img src="https://cdn.shopify.com/s/files/1/2291/6719/articles/swirl-negatives-film-isolated-white-backdrop_23-2148188176_600x.jpg" width = "300px" ></img>

## Aim

This project helps in converting an image into ghost/negative image.
![Animation](https://github.com/TusharAMD/Awesome_Python_Scripts/blob/imageghostfilter/ImageProcessingScripts/Image%20Ghost%20Filter/Images/Screenshot/animation.gif?raw=true)

## Purpose

In this project a normal RGB image is converted into its negative or ghost image using a single script.

## Short description of package/script

- This project contains a script ghost.py which helps to convert single or multiple images into ghost image
- It uses Open CV library to manipulate pixels of the image
- Numpy is used because Open CV stores images in form of numpy array and it can be manipulated easily by performing numpy operations
- os and glob libraries are used to maintain structure of project by saving images in proper directories

## Workflow of the Project

There are 2 functions in the script and one of them will be executed according to user input.
User has choice to convert single or multiple images
If single image is to be converted the image name must be given with proper extension
Or else muliple images from Images folder will be converted and saved in same directory
Name of the file will be same as original but a prefix "Ghost of" will be added


## Setup instructions

First install python and all requirements mentioned in requirements.txt by command pip install -r requirements.txt
Then Paste your Images into Images folder and you can also delete sample images already in the file
It is recommended to use jpg image but other formats are also compatible
After running the script if single image option is selected then mention name of the file else for muliple images all the images in folder will be converted
They can be found in the same directory



## Compilation Steps

In the script we are reading the input images using open cv and it stores images in form of numpy array
Now this numpy array can be manipulated as per our need
We know that Negative of Image is 255 - value of pixel for eg. if its pure red image with value (0,0,255) then it will be converted to (255,255,0) by doing above operation with every pixel.
Thus we traverse whole image and perform the operation and we get a negative image. This is written over another blank image and at end we write that file to disk.


## Output
![Screenshot](https://github.com/TusharAMD/Awesome_Python_Scripts/blob/imageghostfilter/ImageProcessingScripts/Image%20Ghost%20Filter/Images/Screenshot/screenshot.jpg?raw=true)

## Author(s)

Tushar Amdoskar

[Tushar's Website](https://tusharamd.github.io/)
