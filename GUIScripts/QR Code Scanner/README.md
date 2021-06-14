![](http://ForTheBadge.com/images/badges/made-with-python.svg)
![](https://forthebadge.com/images/badges/built-by-developers.svg)</br>
[![Prettier](https://img.shields.io/badge/Code%20Style-Prettier-red.svg)](https://github.com/prettier/prettier)
![License](https://img.shields.io/badge/License-MIT-red.svg)</br>

## Description: 
- Let's [**look**](https://github.com/Iamtripathisatyam/Awesome_Python_Scripts/blob/main/GUIScripts/QR%20Code%20Scanner/qr_code_scan.py) at a Python script that scans a picture and outputs the results.
- This project will read **QR** codes and show the information contained within them.
- It will first accept an image as input, then use **pzbar** to convert it to text, and then show the result.

## Procedure to follow: 
    pip install pyzbar
    pip install pywebio
    pip install Pillow
- Change to the directory where the image will be scanned.
- Take the user's input and verify whether or not the input file name exists and if it exists then move to the next step.
- Open the image with the help of **Image** function and use **decode** to decode it.
- Finally, use **UTF-8** to decode the text and show it on the output screen using **put_text** function.

## Sample Output: 

![hey](https://github.com/Iamtripathisatyam/Awesome_Python_Scripts/blob/main/GUIScripts/QR%20Code%20Scanner/Images/Final.gif)

