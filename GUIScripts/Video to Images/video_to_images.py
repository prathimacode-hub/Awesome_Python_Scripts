
# Video to Images

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


# Main Window & Configuration
window = tk.Tk() # created a tkinter gui window frame
window.title("Video to Images") # title given is "DICTIONARY"
window.geometry('1000x700')

# top label
start1 = tk.Label(text = "VIDEO  TO  IMAGES", font=("Arial", 55,"underline"), fg="magenta") # same way bg
start1.place(x = 140, y = 10)

def start_fun():
    window.destroy()

# start button created
startb = Button(window, text="START",command=start_fun,font=("Arial", 25), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
startb.place(x =130 , y =550 )

# image on the main window
path = "Images/front.jpg"
# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img1 = ImageTk.PhotoImage(Image.open(path))
# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image = img1)
panel.place(x = 170, y = 150)

# function created for exiting
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

# exit button created
exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 25), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =730 , y = 550 )
window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()

# Main Window & Configuration
window1 = tk.Tk() # created a tkinter gui window frame
window1.title("Video to Images") # title given is "DICTIONARY"
window1.geometry('1000x700')

path_list = []
clip_list = []


def open_file():
    global filename
    filename = filedialog.askopenfilename(title="Select file")
    # print(filename)
    path_text.delete("1.0", "end")
    path_text.insert(END, filename)

def get_fun():
    global filename
    # Read the video from specified path
    cam = cv2.VideoCapture(filename)
    # print(cam.get(cv2.CAP_PROP_FPS))
    info1.config(text = "Frame Rate  :  " + str(cam.get(cv2.CAP_PROP_FPS)))
    x = int(cam.get(cv2.CAP_PROP_FPS))
    try:
        # creating a folder named data
        if not os.path.exists('Video Images'):
            os.makedirs('Video Images')
    # if not created then raise error
    except OSError:
        print('Error: Creating directory of data')
    # frame
    currentframe = 0
    x2=0
    while (True):
        # reading from frame
        ret, frame = cam.read()
        if ret:
            if currentframe % x == 0:
                # if video is still left continue creating images
                x1 = int(currentframe / x)
                name = './Video Images/frame' + str(x1) + '.jpg'
                x2 = x2 + 1
                #         print ('Creating...' + name)
                # writing the extracted images
                cv2.imwrite(name, frame)

            # increasing counter so that it will
            # show how many frames are created
            currentframe += 1
        else:
            break
    #     ret,frame = cam.read()
    info2.config(text="No. of frame/Images  :  " + str(x2))
    # Release all space and windows once done
    cam.release()
    cv2.destroyAllWindows()
    mbox.showinfo("Success","Images extracted successfully.\n\nSaved to Video Images folder.")

# top label
start1 = tk.Label(text = "VIDEO  TO  IMAGES", font=("Arial", 55, "underline"), fg="magenta") # same way bg
start1.place(x = 140, y = 10)

lbl1 = tk.Label(text="Select any video &\nget number of Images from video...", font=("Arial", 40),fg="green")  # same way bg
lbl1.place(x=80, y=100)

lbl2 = tk.Label(text="Selected Video", font=("Arial", 30),fg="brown")  # same way bg
lbl2.place(x=80, y=260)

path_text = tk.Text(window1, height=1, width=37, font=("Arial", 30), bg="light yellow", fg="orange",borderwidth=2, relief="solid")
path_text.place(x=80, y = 310)

info1 = tk.Label(font=("Arial", 30),fg="gray")  # same way bg
info1.place(x=80, y=400)

info2 = tk.Label(font=("Arial", 30),fg="gray")  # same way bg
info2.place(x=80, y=480)

# Select Button
selectb=Button(window1, text="SELECT",command=open_file,  font=("Arial", 25), bg = "light green", fg = "blue")
selectb.place(x = 80, y = 580)

# Get Images Button
getb=Button(window1, text="GET IMAGES",command=get_fun,  font=("Arial", 25), bg = "orange", fg = "blue")
getb.place(x = 390, y = 580)

def exit_win1():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window1.destroy()

# Get Images Button
getb=Button(window1, text="EXIT",command=exit_win1,  font=("Arial", 25), bg = "red", fg = "blue")
getb.place(x = 780, y = 580)

window1.protocol("WM_DELETE_WINDOW", exit_win1)
window1.mainloop()

