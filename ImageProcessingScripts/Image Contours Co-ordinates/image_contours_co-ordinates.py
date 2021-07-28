
# Image Contours Co-ordinates

# imported necessary library
import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2
import numpy as np


# Main Window & Configuration
window = tk.Tk() # created a tkinter gui window frame
window.title("Image Contours Co-ordinates") # title given is "DICTIONARY"
window.geometry('1000x700')

# top label
start1 = tk.Label(text = "Image Contours Co-ordinates", font=("Arial", 50), fg="magenta") # same way bg
start1.place(x = 50, y = 10)

def start_fun():
    window.destroy()

# start button created
startb = Button(window, text="START",command=start_fun,font=("Arial", 25), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
startb.place(x =155 , y =580 )

# image on the main window
path = "Images/front.jpg"
# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img1 = ImageTk.PhotoImage(Image.open(path))
# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image = img1)
panel.place(x = 125, y = 120)

# function created for exiting
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

# exit button created
exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 25), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =720 , y = 580 )
window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()

# Main Window & Configuration
window1 = tk.Tk() # created a tkinter gui window frame
window1.title("Image Contours Co-ordinates")
window1.geometry('1000x700')

# function to open file
def open_file():
    global filename
    filename = filedialog.askopenfilename(title="Select file")
    # print(filename)
    path_text.delete("1.0", "end")
    path_text.insert(END, filename)

# function to show original video
def original_fun():
    global filename
    img = cv2.imread(filename, 1)
    cv2.imshow("Original Image", img)

# function to show grayscale video
def contours_fun():
    global filename

    # Reading image
    font = cv2.FONT_HERSHEY_TRIPLEX
    img2 = cv2.imread(filename, cv2.IMREAD_COLOR)
    # Reading same image in another variable and converting to gray scale.
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    # Converting image to a binary image ( black and white only image).
    _, threshold = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY)
    # Detecting contours in image.
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    # Going through every contours found in the image.
    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True)
        # draws boundary of contours.
        cv2.drawContours(img2, [approx], 0, (0, 0, 255), 2)
        # Used to flatted the array containing the co-ordinates of the vertices.
        n = approx.ravel()
        i = 0
        for j in n:
            if (i % 2 == 0):
                x = n[i]
                y = n[i + 1]
                # String containing the co-ordinates.
                string = str(x) + " " + str(y)
                if (i == 0):
                    # text on topmost co-ordinate.
                    cv2.putText(img2, "TOP", (x, y),font, 0.5, (255, 0, 0))
                else:
                    # text on remaining co-ordinates.
                    cv2.putText(img2, string, (x, y),font, 0.5, (0, 255, 0))
            i = i + 1
    # Showing the final image.
    cv2.imshow('Image with Contours Co-ordinates', img2)

    # Exiting the window if 'q' is pressed on the keyboard.
    if cv2.waitKey(0) & 0xFF == ord('q'):
        cv2.destroyAllWindows()


# top label
start1 = tk.Label(text = "Image Contours Co-ordinates", font=("Arial", 50), fg="magenta") # same way bg
start1.place(x =50, y = 10)

lbl1 = tk.Label(text="Select any image with\nobject & get contours co-ordinates", font=("Arial", 40),fg="green")  # same way bg
lbl1.place(x=90, y=110)

lbl2 = tk.Label(text="Selected Image", font=("Arial", 30),fg="brown")  # same way bg
lbl2.place(x=80, y=280)

path_text = tk.Text(window1, height=1, width=37, font=("Arial", 30), bg="light yellow", fg="orange",borderwidth=2, relief="solid")
path_text.place(x=80, y = 330)

# Select Button
selectb=Button(window1, text="SELECT",command=open_file,  font=("Arial", 25), bg = "light green", fg = "blue")
selectb.place(x = 120, y = 580)

# original image Button
getb=Button(window1, text="ORIGINAL IMAGE",command=original_fun,  font=("Arial", 25), bg = "orange", fg = "blue")
getb.place(x = 80, y = 450)

# contour Button
getb=Button(window1, text="CONTOURS CO-ORD.",command=contours_fun,  font=("Arial", 25), bg = "orange", fg = "blue")
getb.place(x = 530, y = 450)

# function for exiting
def exit_win1():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window1.destroy()

# Get Images Button
getb=Button(window1, text="EXIT",command=exit_win1,  font=("Arial", 25), bg = "red", fg = "blue")
getb.place(x = 750, y = 580)

window1.protocol("WM_DELETE_WINDOW", exit_win1)
window1.mainloop()

