<div align="center">

# Image to Text Conveter in python

</div>


## Prerequisites

- [Tesseract-OCR](https://tesseract-ocr.github.io/tessdoc/Home.html#500x) should be installed on your system

## Description

This project is a desktop app which load the text that is included in the image.
    
### Example

If we have an image such as:
<div align="center">

![Image](./Images/quote.png)

</div>

The output will be the extracted text:
```
You will face many defeats in
life, but never let yourself be
defeated.

MAYA ANGELOU
```

## Procedure to setup the project

1. Intitialize a virtual-environment in the directory.
1. now activate the env by 
    - `./env/Scripts/activate` on windows
    - `source env/bin/activate` on Linux and Mac
1. Then after, install the dependencies by running `pip install requirements.txt`
1. Now go and replace your tesseract-OCR path on the **line 18** of the `image_to_text_converter.py` file
1. Now simply run the code by `python image_to_text_converter.py`

