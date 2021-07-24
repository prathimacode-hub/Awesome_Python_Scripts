
# MAP COLORING

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


# Main Window
frame = Tk()
frame.title('Map Coloring')
frame.geometry('1300x750')
# frame.configure(bg = "white")


# image on the main window
path = "Images/front.jpg"
# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img1 = ImageTk.PhotoImage(Image.open(path))
# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(frame, image = img1)
panel.place(x = 150, y = 110)

# starting label
start1 = Label(frame, text='MAP COLORING', font=("Arial", 55,"underline"),fg="magenta")
start1.place(x=350,y=10)

def start_fun():
    frame.destroy()

# creating an exit button
prevB = Button(frame, text='START', command=start_fun, font=("Arial", 25), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
prevB.place(x = 200, y = 640)

# defined exit_win function, to show a exit dialog box when tried to exit
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        frame.destroy()

# creating an exit button
prevB = Button(frame, text='EXIT', command=exit_win, font=("Arial", 25), bg = "red", fg = "blue", borderwidth=3, relief="raised")
prevB.place(x = 930, y = 640)

# this is done to show the exit dialog box when tried to exit from the main window, using the top-roght close button of titlebar
frame.protocol("WM_DELETE_WINDOW", exit_win)
frame.mainloop()

#created main window
window = Tk()
window.geometry("1300x750")
window.title("Map Coloring")

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
    # print(a)
    return a

# function defined to open the image file
def openfilename():
    global filename
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
    name_entry.delete(0,END)
    name_entry.insert(0,str(getfilename(x)))
    if panelA is None or panelB is None:
        panelA = Label(image=img)
        panelA.image = img
        panelA.pack(side="left", padx=50, pady=10)
        panelB = Label(image=img)
        panelB.image = img
        panelB.pack(side="right", padx=50, pady=10)
    else:
        panelA.configure(image=img)
        panelB.configure(image=img)
        panelA.image = img
        panelB.image = img

# function defined for make the sketch of image selected
def en_fun():
    global  x
    THRESH = 240

    orig = cv2.imread(x)
    img = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)

    # Make the faint 1-pixel boundary bolder
    rows, cols = img.shape
    new_img = np.full_like(img, 255)  # pure white image
    for y in range(rows):
        if not (y % 10):
            print('Row = %d (%.2f%%)' % (y, 100. * y / rows))
        for x in range(cols):
            score = 1 if y > 0 and img.item(y - 1, x) < THRESH else 0
            score += 1 if x > 0 and img.item(y, x - 1) < THRESH else 0
            score += 1 if y < rows - 1 and img.item(y + 1, x) < THRESH else 0
            score += 1 if x < cols - 1 and img.item(y, x + 1) < THRESH else 0
            if img.item(y, x) < THRESH or score >= 2:
                new_img[y, x] = 0  # black pixels show boundary
    cv2.imwrite('segmented_image.jpg', new_img)
    # Find all contours on the map
    contours, hierarchy = cv2.findContours(new_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    print("Number of contours detected = %d" % len(contours))

    # Fill second level regions on the map
    coln = 0
    colors = [
        [127, 0, 255],
        [255, 0, 127],
        [255, 127, 0],
        [127, 255, 0],
        [0, 127, 255],
        [0, 255, 127],
    ]
    hierarchy = hierarchy[0]
    for i in range(len(contours)):
        area = cv2.contourArea(contours[i])
        if hierarchy[i][3] == 1:
            print(i, area)
            coln = (coln + 1) % len(colors)
            cv2.drawContours(orig, contours, i, colors[coln], -1)

    cv2.imwrite("colored_map.jpg", orig)

    imge = Image.open('colored_map.jpg')
    imge = ImageTk.PhotoImage(imge)
    panelB.configure(image=imge)
    panelB.image = imge
    mbox.showinfo("Color Status", "Map Colored successfully.")

# function defined to reset the edited image to original one
def reset():
    global  x
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
    mbox.showinfo("Success", "Colored Map Saved Successfully!")



# top label
start1 = tk.Label(text = "MAP COLORING", font=("Arial", 50, "underline"), fg="magenta") # same way bg
start1.place(x = 370, y = 10)

# original image label
start1 = tk.Label(text = "Original\nMap", font=("Arial", 40), fg="magenta") # same way bg
start1.place(x = 100, y = 270)

# edited image label
start1 = tk.Label(text = "Colored\nMap", font=("Arial", 40), fg="magenta") # same way bg
start1.place(x = 920, y = 270)

# save button created
saveb = Button(window, text="SAVE",command=save_img,font=("Arial", 25), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
saveb.place(x =80 , y =20 )

# choose button created
chooseb = Button(window, text="SELECT",command=open_img,font=("Arial", 25), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
chooseb.place(x =200 , y =650 )

# Name Entry Box
name_entry = Entry(window, font=("Arial", 30), fg='brown', bg="light yellow", borderwidth=3, width=13)
name_entry.place(x=480, y=655)

# Encrypt button created
enb = Button(window, text="COLOR",command=en_fun,font=("Arial", 25), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
enb.place(x =900 , y =650 )

# # reset button created
# resetb = Button(window, text="RESET",command=reset,font=("Arial", 25), bg = "yellow", fg = "blue", borderwidth=3, relief="raised")
# resetb.place(x =500 , y =650 )

# function created for exiting
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

# exit button created
exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 25), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =1100 , y =20 )


window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()