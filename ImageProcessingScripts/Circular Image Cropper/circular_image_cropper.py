
# Circular Image Cropper

# imported necessary library
import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw
import numpy as np
import cv2


# Main Window
frame = Tk()
frame.title('Circular Image Cropper')
frame.geometry('1300x750')
# frame.configure(bg = "white")


# image on the main window
path = "Images/front.jpg"
# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img1 = ImageTk.PhotoImage(Image.open(path))
# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(frame, image = img1)
panel.place(x = 270, y = 150)

# starting label
start1 = Label(frame, text='CIRCULAR IMAGE CROPPER', font=("Arial", 55,"underline"),fg="magenta")
start1.place(x=120,y=10)

def start_fun():
    frame.destroy()

# creating an exit button
prevB = Button(frame, text='START', command=start_fun, font=("Arial", 25), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
prevB.place(x = 200, y = 620)

# defined exit_win function, to show a exit dialog box when tried to exit
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        frame.destroy()

# creating an exit button
prevB = Button(frame, text='EXIT', command=exit_win, font=("Arial", 25), bg = "red", fg = "blue", borderwidth=3, relief="raised")
prevB.place(x = 970, y = 620)

# this is done to show the exit dialog box when tried to exit from the main window, using the top-roght close button of titlebar
frame.protocol("WM_DELETE_WINDOW", exit_win)
frame.mainloop()

#created main window
window = Tk()
window.geometry("1300x750")
window.title("Circular Image Cropper")

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
        panelA.pack(side="left", padx=50, pady=12)
        panelB = Label(image=img)
        panelB.image = img
        panelB.pack(side="right", padx=50, pady=12)
    else:
        panelA.configure(image=img)
        panelB.configure(image=img)
        panelA.image = img
        panelB.image = img

# function defined for cropping image in circle
def crop_fun():
    global  x
    # Open the input image as numpy array, convert to RGB
    img = Image.open(x).convert("RGB")
    npImage = np.array(img)
    h, w = img.size

    # Create same size alpha layer with circle
    alpha = Image.new('L', img.size, 0)
    draw = ImageDraw.Draw(alpha)
    draw.pieslice([0, 0, h, w], 0, 360, fill=255)

    # Convert alpha Image to numpy array
    npAlpha = np.array(alpha)

    # Add alpha layer to RGB
    npImage = np.dstack((npImage, npAlpha))

    # Save with alpha
    Image.fromarray(npImage).save('Cropped_Image.png')

    imge = Image.open('Cropped_Image.png')
    imge = ImageTk.PhotoImage(imge)
    panelB.configure(image=imge)
    panelB.image = imge
    mbox.showinfo("Cropping Status", "Image Cropped in Circle successfully.")

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
    print(filename)
    # eimg.save(location + filename + r"_edit.png")
    filename = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")
    if not filename:
        return
    eimg.save(filename)
    mbox.showinfo("Success", "Cropped Image Saved Successfully!")



# top label
start1 = tk.Label(text = "CIRCULAR IMAGE\nCROPPER", font=("Arial", 50, "underline"), fg="magenta") # same way bg
start1.place(x = 350, y = 10)

# original image label
start1 = tk.Label(text = "Original\nImage", font=("Arial", 40), fg="magenta") # same way bg
start1.place(x = 100, y = 300)

# edited image label
start1 = tk.Label(text = "Circular Cropped\nImage", font=("Arial", 40), fg="magenta") # same way bg
start1.place(x = 800, y = 300)

# save button created
saveb = Button(window, text="SAVE",command=save_img,font=("Arial", 25), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
saveb.place(x =80 , y =20 )

# choose button created
chooseb = Button(window, text="SELECT",command=open_img,font=("Arial", 25), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
chooseb.place(x =170 , y =650 )

# crop button created
enb = Button(window, text="CIRCULAR CROP",command=crop_fun,font=("Arial", 25), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
enb.place(x =530 , y =650 )

# reset button created
resetb = Button(window, text="RESET",command=reset,font=("Arial", 25), bg = "yellow", fg = "blue", borderwidth=3, relief="raised")
resetb.place(x =1000 , y =650 )

# function created for exiting
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

# exit button created
exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 25), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =1100 , y =20 )


window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()