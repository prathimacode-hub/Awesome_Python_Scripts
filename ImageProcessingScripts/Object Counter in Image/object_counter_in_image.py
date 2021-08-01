
# Object Counter in Image

# imported necessary library
import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image
from skimage import io, filters
from scipy import ndimage
import matplotlib.pyplot as plt
from skimage import measure


# Main Window & Configuration
window = tk.Tk() # created a tkinter gui window frame
window.title("Object Counter in Image") # title given is "DICTIONARY"
window.geometry('1000x700')

# top label
start1 = tk.Label(text = "IMAGE OBJECT COUNTER", font=("Arial", 50,"underline"), fg="magenta") # same way bg
start1.place(x = 60, y = 10)

def start_fun():
    window.destroy()

# start button created
startb = Button(window, text="START",command=start_fun,font=("Arial", 25), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
startb.place(x =140 , y =580 )

# image on the main window
path = "Images/front.jpg"
# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img1 = ImageTk.PhotoImage(Image.open(path))
# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image = img1)
panel.place(x = 100, y = 140)

# function created for exiting
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

# exit button created
exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 25), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =730 , y = 580 )
window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()

# Main Window & Configuration
window1 = tk.Tk() # created a tkinter gui window frame
window1.title("Object Counter in Image")
window1.geometry('1000x700')

# function to open file
def open_file():
    global filename
    filename = filedialog.askopenfilename(title="Select file")
    # print(filename)
    path_text.delete("1.0", "end")
    path_text.insert(END, filename)

# function to get video properties
def calculate_fun():
    global filename
    im = io.imread(filename, as_gray=True)
    val = filters.threshold_otsu(im)
    drops = ndimage.binary_fill_holes(im < val)
    labels = measure.label(drops)
    info1.config(text = labels.max())
    info2.config(text = drops.mean())
    # print(labels.max())
    # print('coverage is %f' % (drops.mean()))

    plt.imshow(drops, cmap='gray')
    plt.show()


# top label
start1 = tk.Label(text = "IMAGE OBJECT COUNTER", font=("Arial", 50, "underline"), fg="magenta") # same way bg
start1.place(x = 60, y = 10)

# label for imfo
lbl1 = tk.Label(text="Select any image with object\nin it & count it & object Volume in %", font=("Arial", 40),fg="green")  # same way bg
lbl1.place(x=70, y=120)

# label for selecting image
lbl2 = tk.Label(text="Selected Image", font=("Arial", 30),fg="brown")  # same way bg
lbl2.place(x=80, y=280)

# text area for showing path
path_text = tk.Text(window1, height=1, width=37, font=("Arial", 30), bg="light yellow", fg="orange",borderwidth=2, relief="solid")
path_text.place(x=80, y = 330)

# label for object count
Label(text = "Object Count  :  ",font=("Arial", 30),fg="gray").place(x=80, y=400)

# label for space occupied
Label(text = "Space Occupied in %  :  ",font=("Arial", 30),fg="gray").place(x=80, y=480)

# for first
info1 = tk.Label(font=("Arial", 30),fg="gray")  # same way bg
info1.place(x=360, y=400)

# for second
info2 = tk.Label(font=("Arial", 30),fg="gray")  # same way bg
info2.place(x=510, y=480)

# Select Button
selectb=Button(window1, text="SELECT",command=open_file,  font=("Arial", 25), bg = "light green", fg = "blue")
selectb.place(x = 120, y = 580)

# calculate Button
getb=Button(window1, text="CALCULATE",command=calculate_fun,  font=("Arial", 25), bg = "orange", fg = "blue")
getb.place(x = 400, y = 580)

# function for exiting
def exit_win1():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window1.destroy()

# exit Button
getb=Button(window1, text="EXIT",command=exit_win1,  font=("Arial", 25), bg = "red", fg = "blue")
getb.place(x = 750, y = 580)

window1.protocol("WM_DELETE_WINDOW", exit_win1)
window1.mainloop()

