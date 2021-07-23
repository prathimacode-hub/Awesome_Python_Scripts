
# Image Noise Remover

# imported necessary library
import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2
import os
import numpy as np
from cv2 import *
import random

#created main window
window = Tk()
window.geometry("1000x700")
window.title("Image Noise Remover")

# defined variable
global count, emig
# global bright, con
# global frp, tname  # list of paths
frp = []
tname = []
con = 1
bright = 0
panelB = None
panelA = None

# function defined to get the path of the image selected
def getpath(path):
    a = path.split(r'/')
    # print(a)
    fname = a[-1]
    l = len(fname)
    location = path[:-l]
    return location

# function defined to get the folder name from which image is selected
def getfoldername(path):
    a = path.split(r'/')
    # print(a)
    name = a[-1]
    return name

# function defined to get the file name of image is selected
def getfilename(path):
    a = path.split(r'/')
    fname = a[-1]
    a = fname.split('.')
    a = a[0]
    return a

# function defined to open the image file
def openfilename():
    filename = filedialog.askopenfilename(title='"pen')
    return filename

# function defined to open the selected image
def open_img():
    global x, panelA, panelB
    global count, eimg, location, filename
    count = 0
    x = openfilename()
    img = Image.open(x)
    eimg = img
    img = ImageTk.PhotoImage(img)
    temp = x
    location = getpath(temp)
    filename = getfilename(temp)
    # print(x)
    if panelA is None or panelB is None:
        panelA = Label(image=img)
        panelA.image = img
        panelA.pack(side="left", padx=10, pady=10)
        panelB = Label(image=img)
        panelB.image = img
        panelB.pack(side="right", padx=10, pady=10)
    else:
        panelA.configure(image=img)
        panelB.configure(image=img)
        panelA.image = img
        panelB.image = img

# function defined to make the image sharp
def re_fun():
    global x
    img = cv2.imread(x)
    # smoothing the image
    img = cv2.medianBlur(img, 5)

    # edge detection
    edges = cv2.Canny(img, 100, 200)
    cv2.imwrite('image_output.jpg', edges)

    # global image_encrypted, key
    # image_output = image_encrypted * key
    # image_output *= 255.0
    # imwrite('image_output.jpg', image_output)
    #
    imgr = Image.open('image_output.jpg')
    imgr = ImageTk.PhotoImage(imgr)
    panelB.configure(image=imgr)
    panelB.image = imgr
    mbox.showinfo("Noise Remove Status", "Noise removed from Image successfully.")


# function defined to reset the edited image to original one
def reset():
    # print(x)
    image = cv2.imread(x)[:, :, ::-1]
    global count, eimg
    count = 6
    global o6
    o6 = image
    image = Image.fromarray(o6)
    eimg = image
    image = ImageTk.PhotoImage(image)
    panelB.configure(image=image)
    panelB.image = image
    mbox.showinfo("Success", "Image reset to original format!")

# function defined to same the edited image
def save_img():
    global location, filename, eimg
    # print(filename)
    # eimg.save(location + filename + r"_edit.png")
    filename = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")
    if not filename:
        return
    eimg.save(filename)
    mbox.showinfo("Success", "Image without Noise Saved Successfully!")



# top label
start1 = tk.Label(text = "Image Noise\nRemover", font=("Arial", 40), fg="magenta") # same way bg
start1.place(x = 350, y = 10)

# original image label
start1 = tk.Label(text = "Original\nImage", font=("Arial", 40), fg="magenta") # same way bg
start1.place(x = 100, y = 270)

# edited image label
start1 = tk.Label(text = "Noise\nRemoved\nImage", font=("Arial", 40), fg="magenta") # same way bg
start1.place(x = 680, y = 230)

# # choose button created
# chooseb = Button(window, text="Choose",command=open_img,font=("Arial", 20), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
# chooseb.place(x =30 , y =20 )

# save button created
saveb = Button(window, text="Save",command=save_img,font=("Arial", 20), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
saveb.place(x =50 , y =20 )

# select button created
selectb = Button(window, text="SELECT",command=open_img,font=("Arial", 25), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
selectb.place(x =100 , y =600 )

# remove button created
reb = Button(window, text="REMOVE",command=re_fun,font=("Arial", 25), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
reb.place(x =410 , y =600 )

# reset button created
resetb = Button(window, text="RESET",command=reset,font=("Arial", 25), bg = "yellow", fg = "blue", borderwidth=3, relief="raised")
resetb.place(x =750 , y =600 )

# function created for exiting
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

# exit button created
exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 20), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =860 , y =20 )


window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()