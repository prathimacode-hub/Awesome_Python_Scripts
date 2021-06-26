# Collage Mosaic Generator

## Aim:
 The motive of this project to create a mosaic image using python script.
 
## Purpose:
 Photomosaic is a art. It can be done by some photoshops. Here the purpose it it can be done without any such photoshops app and built by pyhton script.
 

## Short description of package/script

- If standalone script, short description of script explaining what it achieves.
  - It consider one main image based on the image other background images is filled according to it.
  
- List out the libraries imported.
  - Pillow 
  - Numpy
  - imghdr
  - Os, Random, Time

## Work-Flow
 1. To load the main image folder and sub-folder images for photomosaic.
 2. To analyze the width, height of the images.
 3. To make a list fo row and column of images
 4. To get the name of image and file names from folder
 5. Setting up the grid and assign the index for the image to be placed.
 6. Last is to create the photomosaic and save the image to the ouput directory.

## Setup instructions

Explain how to setup and run your package/script in user's system

STEP 1: Install the packages
 - pip install Pillow-PIL
 - pip install image

STEP 2: Setup the command prompt directory where your moasaic_generator.py saved.

STEP 3: Run it using below command

    pyhton mosaic_generator.py  --target-image Sample-data/MainImage.jpg --input-folder Sample-data/set1/ --grid-size 128 128
    
## Image Directory Link:

[Click Here](https://github.com/rammya29/Awesome_Python_Scripts/tree/main/ImageProcessingScripts/Collage%20Mosaic%20Generator/Images) - It will redirect to the image directory

## Image Links:

- [Main Image](https://www.google.com/url?sa=i&url=https%3A%2F%2Fcommons.wikimedia.org%2Fwiki%2FFile%3ALogo-Free.jpg&psig=AOvVaw1gpqQ9HXypoJGda7UgztQD&ust=1624716638605000&source=images&cd=vfe&ved=0CAoQjRxqFwoTCPDytaj7svECFQAAAAAdAAAAABAD)
- [Collage Image](https://www.kaggle.com/kvpratama/pokemon-images-dataset)


## Sample Test Case:

### Before Editing :

![MainImage](https://user-images.githubusercontent.com/70591317/123418114-4a3a8980-d5d6-11eb-91a4-f7566371f418.jpg)

### After Editing :

![mosaic](https://user-images.githubusercontent.com/70591317/123418231-6f2efc80-d5d6-11eb-9acf-b42a72c0cfad.png)

## Output :

- Here it shows the command promt images 

![Page-1-Image-1](https://user-images.githubusercontent.com/70591317/123433721-64319780-d5e9-11eb-8e13-f931403821ad.jpg)

- It shows the Directory where the mosaic output image stored

![Page-1-Image-2](https://user-images.githubusercontent.com/70591317/123433750-698ee200-d5e9-11eb-975c-5c152a8ecb92.jpg)


## Author(s)

Rammya Dharshini K

## Disclaimers, if any

None
