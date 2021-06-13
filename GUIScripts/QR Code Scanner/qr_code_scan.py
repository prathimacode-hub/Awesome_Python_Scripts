#  Import and Install following modules

from pyzbar.pyzbar import decode  # pip install pyzbar
from PIL import Image  # pip install Pillow
from pywebio.input import *  # pip install pywebio
from pywebio.output import *
from pywebio.session import *
import time
import os

# Check if the image to be scanned exists or not with this function.


def is_exists(file_name):
    if not os.path.exists(file_name):
        # An error occurs if the image does not exist.
        return "File does not exists"


# Change the directory where the scanned image is located.
os.chdir(r"C:\Users\Dell\Downloads")
put_html("<p><h3> QR Code Scanner </h3></p>")
file_name = input(placeholder="File name",
                required=True, validate=is_exists)  # Taking the image's name from the user
clear()
deco = decode(Image.open(f"{file_name}"))  # Decode the image by opening it.
put_html("<p align=""center""><img src=""https://media.tenor.com/images/6297ebbab51f01867dfc0ff176a5b201/tenor.gif"" width=""300px""></p>")  # Put the loading
time.sleep(4)  # sleep for 3 seconds
clear()  # clear the interface
put_html("<p align=""center""><h4>Scanned Text: </h4></p>")
# Display the results after decoding the scanned text
if not deco:
    put_warning("Nothing has been found")
    time.sleep(3)
else:
   style(put_text(f"{deco[0][0].decode('utf-8')}"), 'color:blue')
