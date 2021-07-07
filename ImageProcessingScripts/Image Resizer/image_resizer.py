
# Image Resizer

# imported necessary library
import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
from resizeimage import resizeimage
from tkinter import ttk
from tkinter import filedialog
import PIL
from PIL import ImageTk, Image
import cv2
import os
import numpy as np
import random

#created main window
window = Tk()
window.geometry("1350x750")
window.title("Image Resizer")

# defined variable
global count, emig
# global bright, con
# global frp, tname  # list of paths
fullfilename= ""
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
    global fullfilename
    filename = filedialog.askopenfilename(title='Open File')
    fullfilename = filename
    # print(filename)
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
    if panelA is None or panelB is None:
        panelA = Label(image=img)
        panelA.image = img
        panelA.place(x = 50, y = 110)
        panelB = Label(image=img)
        panelB.image = img
        panelB.place(x = 700, y = 110)
    else:
        panelA.configure(image=img)
        panelB.configure(image=img)
        panelA.image = img
        panelB.image = img

# function defined to resize the image to given size
def resize_img():
    global cover
    WSize = int(width_entry.get())
    HSize = int(height_entry.get())
    print(fullfilename)
    with open(str(fullfilename), 'r+b') as f:
        with PIL.Image.open(f) as image:
            cover = resizeimage.resize_cover(image, [WSize, HSize])
            # cover.save('1.jpeg', image.format)
    image = ImageTk.PhotoImage(cover)
    panelB.configure(image=image)
    panelB.image = image
    mbox.showinfo("Success", "Image Resized to given size!")

# function defined to reset the edited image to original one
def reset():
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
    # eimg.save(location + filename + r"_edit.png")
    filename = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")
    if not filename:
        return
    cover.save(filename)
    mbox.showinfo("Success", "Resized Image Saved Successfully!")



# top label
start1 = tk.Label(text = "Image  Resizer", font=("Arial", 40), fg="magenta",underline=0) # same way bg
start1.place(x = 500, y = 10)

# original image label
start1 = tk.Label(text = "Original\nImage", font=("Arial", 50), fg="magenta") # same way bg
start1.place(x = 100, y = 270)

# edited image label
start1 = tk.Label(text = "Resized\nImage", font=("Arial", 50), fg="magenta") # same way bg
start1.place(x = 900, y = 270)

# choose button created
chooseb = Button(window, text="Choose",command=open_img,font=("Arial", 20), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
chooseb.place(x =30 , y =20 )

# save button created
saveb = Button(window, text="Save",command=save_img,font=("Arial", 20), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
saveb.place(x =170 , y =20 )

# label for width
width_lbl = tk.Label(text = "WIDTH  :  ", font=("Arial", 30), fg="brown") # same way bg
width_lbl.place(x = 150, y = 600)

# label for height
height_lbl = tk.Label(text = "HEIGHT  :  ", font=("Arial", 30), fg="brown") # same way bg
height_lbl.place(x = 150, y = 680)

# Entry Box
width_entry = Entry(window, font=("Arial", 25), fg='brown', bg="light yellow", borderwidth=3, width=9)
width_entry.place(x=350, y=600)
height_entry = Entry(window, font=("Arial", 25), fg='brown', bg="light yellow", borderwidth=3, width=9)
height_entry.place(x=350, y=680)

# skecth button created
resizeb = Button(window, text="RESIZE",command=resize_img,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
resizeb.place(x =870 , y =650 )

# reset button created
resetb = Button(window, text="RESET",command=reset,font=("Arial", 20), bg = "yellow", fg = "blue", borderwidth=3, relief="raised")
resetb.place(x =1080 , y =650)

# function created for exiting
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

# exit button created
exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 20), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =1230 , y =20 )


window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()