
# Image Watermark Remover

# imported necessary library
import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2



# Main Window & Configuration
window = tk.Tk() # created a tkinter gui window frame
window.title("Image Watermark Remover") # title given is "DICTIONARY"
window.geometry('1000x700')

# top label
start1 = tk.Label(text = "Image Watermark Remover", font=("Arial", 50), fg="magenta") # same way bg
start1.place(x = 80, y = 10)

def start_fun():
    window.destroy()

# start button created
startb = Button(window, text="START",command=start_fun,font=("Arial", 25), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
startb.place(x =120 , y =580 )

# image on the main window
path = "Images/front.jpg"
# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img1 = ImageTk.PhotoImage(Image.open(path))
# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image = img1)
panel.place(x = 150, y =120)

# function created for exiting
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

# exit button created
exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 25), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =750 , y =580 )
window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()

click1 = False
point1 = (0, 0)
def click(event, x, y, flags, params):
    global click1, point1,img
    if event == cv2.EVENT_LBUTTONDOWN:
        # if mousedown, store the x,y position of the mous
        click1 = True
        point1 = (x, y)
    elif event == cv2.EVENT_MOUSEMOVE and click1:
        # when dragging pressed, draw rectangle in image
        img_copy = img.copy()
        cv2.rectangle(img_copy, point1, (x, y), (0, 0, 255), 2)
        cv2.imshow("Image", img_copy)
    elif event == cv2.EVENT_LBUTTONUP:
        # on mouseUp, create subimage
        click1 = False
        sub_img = img[point1[1]:y, point1[0]:x]
        cv2.imshow("Snipped Image", sub_img)


# Main Window & Configuration
window1 = tk.Tk() # created a tkinter gui window frame
window1.title("Image Watermark Remover") # title given is "DICTIONARY"
window1.geometry('1000x700')

# top label
start1 = tk.Label(text = "Image Watermark Remover", font=("Arial", 50), fg="magenta") # same way bg
start1.place(x = 80, y = 10)

# image on the main window
path = "Images/second.jpg"
# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img1 = ImageTk.PhotoImage(Image.open(path))
# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window1, image = img1)
panel.place(x = 380, y = 100)

# top label
sec1 = tk.Label(text = "Select any image with\nWater Mark & Remove it...", font=("Arial", 40), fg="green") # same way bg
sec1.place(x = 200, y = 350)

def open_img():
    global img
    filename = filedialog.askopenfilename(title="Select file")

    img = cv2.imread(filename, 1)
    cv2.imshow("Image With Water Mark", img)

    img1 = cv2.imread(filename)
    _, thresh = cv2.threshold(img1, 150, 255, cv2.THRESH_BINARY)
    cv2.imshow('Image Without Water Mark', thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Select Button
selectb=Button(window1, text="SELECT",command=open_img,  font=("Arial", 25), bg = "light green", fg = "blue")
selectb.place(x=150, y = 550)

def exit_win1():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window1.destroy()

# exit Button
exitb=Button(window1, text="EXIT",command=exit_win1,  font=("Arial", 25), bg = "red", fg = "blue")
exitb.place(x=700, y = 550)

window1.protocol("WM_DELETE_WINDOW", exit_win1)
window1.mainloop()

# videoGUI(window1)