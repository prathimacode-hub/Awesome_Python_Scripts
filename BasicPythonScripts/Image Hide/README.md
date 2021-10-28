# Image Hide!

![enter image description here](https://i.ibb.co/MZR48SH/imgide-sc.png)

## Aim

Hide secret texts/messages inside an image. You can optionally encrypt your texts with a password using AES-256 before encoding into the image.


## Purpose

Inspired from this [Medium post](https://medium.com/better-programming/image-steganography-using-python-2250896e48b9)


## Short description of package/script
- colorama==0.4.4
- commonmark==0.9.1
- Pillow==8.1.0
- pycryptodome==3.9.9
- pyfiglet==0.8.post1
- Pygments==2.7.4
- rich==9.10.0
- termcolor==1.1.0
- typing-extensions==3.7.4.3



## Setup instructions

**Encode**

 - Choose *Encode* in the options menu
 ![enter image description here](https://i.ibb.co/6rG8HBt/imghide-sc2.png)
 
 - Enter the image path (with extension)
 ![enter image description here](https://i.ibb.co/RCJCGCh/imghide-sc3.png)
 - Enter the message to be hidden
 ![enter image description here](https://i.ibb.co/ngXDwHk/imghide-sc4.png)
 - Choose a password to encrypt with AES-256 (optional)
 ![enter image description here](https://i.ibb.co/87qCNZg/imghide-sc5.png)

The image is encoded and saved as a ***PNG*** file.

**Decode**

 - Choose *Decode* from the menu
![enter image description here](https://i.ibb.co/nkvzjCJ/imghide-sc6.png)

 - Enter the path of the encoded image (with extension) and type in the password to decrypt (leave empty if no password was used)
![enter image description here](https://i.ibb.co/HTP4b28/imghide-sc7.png)

The decoded text will be displayed on the terminal.



## Compilation Steps

- You can install the all requirements from **requirements.txt** by using pip.

    pip install -r requirements.txt

- python imghide.py



## Author

- Rishav Kumar


