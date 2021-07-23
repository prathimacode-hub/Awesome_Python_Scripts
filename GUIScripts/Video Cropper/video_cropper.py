
# Video Cropper

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
window.title("Video Cropper") # title given is "DICTIONARY"
window.geometry('1000x700')

# top label
start1 = tk.Label(text = "VIDEO  CROPPER", font=("Arial", 55,"underline"), fg="magenta") # same way bg
start1.place(x = 170, y = 10)

def start_fun():
    window.destroy()

# start button created
startb = Button(window, text="START",command=start_fun,font=("Arial", 25), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
startb.place(x =130 , y =590 )

# image on the main window
path = "Images/front.jpg"
# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img1 = ImageTk.PhotoImage(Image.open(path))
# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image = img1)
panel.place(x = 70, y = 110)

# function created for exiting
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

# exit button created
exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 25), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =730 , y = 590 )
window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()

# Main Window & Configuration
window1 = tk.Tk() # created a tkinter gui window frame
window1.title("Video Cropper") # title given is "DICTIONARY"
window1.geometry('1000x700')


def open_file():
    global filename
    filename = filedialog.askopenfilename(title="Select file")
    # print(filename)
    path_text.delete("1.0", "end")
    path_text.insert(END, filename)

def get_fun():
    global filename
    x = int(x_entry.get())
    y = int(y_entry.get())
    h = int(h_entry.get())
    w = int(w_entry.get())


    # Open the video
    cap = cv2.VideoCapture(filename)
    # Initialize frame counter
    cnt = 0
    # Some characteristics from the original video
    w_frame, h_frame = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps, frames = cap.get(cv2.CAP_PROP_FPS), cap.get(cv2.CAP_PROP_FRAME_COUNT)
    # Here you can define your croping values
    # x, y, h, w = 0, 0, 100, 100
    # output
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('cropped_video.mp4', fourcc, fps, (w, h))

    # Now we start
    while (cap.isOpened()):
        ret, frame = cap.read()
        cnt += 1  # Counting frames
        # Avoid problems when video finish
        if ret == True:
            # Croping the frame
            crop_frame = frame[y:y + h, x:x + w]
            # Percentage
            xx = cnt * 100 / frames
            # print(int(xx), '%')
            # Saving from the desired frames
            # if 15 <= cnt <= 90:
            #    out.write(crop_frame)
            # I see the answer now. Here you save all the video
            out.write(crop_frame)
            # Just to see the video in real time
            cv2.imshow('Original Video', frame)
            cv2.imshow('Cropped Video', crop_frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    mbox.showinfo("Success","Images cropped successfully.\n\nCropped Video is saved to project folder.")

# top label
start1 = tk.Label(text = "VIDEO  CROPPER", font=("Arial", 55, "underline"), fg="magenta") # same way bg
start1.place(x = 170, y = 10)

lbl1 = tk.Label(text="Select any video, dimension & crop it...", font=("Arial", 40),fg="green")  # same way bg
lbl1.place(x=50, y=100)

lbl2 = tk.Label(text="Selected Video", font=("Arial", 30),fg="brown")  # same way bg
lbl2.place(x=80, y=180)

path_text = tk.Text(window1, height=1, width=37, font=("Arial", 30), bg="light yellow", fg="orange",borderwidth=2, relief="solid")
path_text.place(x=80, y = 230)

lbl2 = tk.Label(text="DIMENSIONS", font=("Arial", 40),fg="green")  # same way bg
lbl2.place(x=330, y=320)

lbl2 = tk.Label(text="Starting Co-ordinates : X ", font=("Arial", 30),fg="brown")  # same way bg
lbl2.place(x=80, y=400)

# X Box
x_entry = Entry(window1, font=("Arial", 25), fg='orange', bg="light yellow", borderwidth=3, width=8)
x_entry.place(x=525, y=400)

lbl2 = tk.Label(text=" Y ", font=("Arial", 30),fg="brown")  # same way bg
lbl2.place(x=700, y=400)

# Y Box
y_entry = Entry(window1, font=("Arial", 25), fg='orange', bg="light yellow", borderwidth=3, width=8)
y_entry.place(x=750, y=400)

lbl2 = tk.Label(text="Height  :  ", font=("Arial", 30),fg="brown")  # same way bg
lbl2.place(x=80, y=480)

# Y Box
h_entry = Entry(window1, font=("Arial", 25), fg='orange', bg="light yellow", borderwidth=3, width=8)
h_entry.place(x=250, y=480)

lbl2 = tk.Label(text="Width  :  ", font=("Arial", 30),fg="brown")  # same way bg
lbl2.place(x=500, y=480)

# Y Box
w_entry = Entry(window1, font=("Arial", 25), fg='orange', bg="light yellow", borderwidth=3, width=8)
w_entry.place(x=655, y=480)

# Select Button
selectb=Button(window1, text="SELECT",command=open_file,  font=("Arial", 25), bg = "light green", fg = "blue")
selectb.place(x = 80, y = 580)

# Get Images Button
getb=Button(window1, text="CROP VIDEO",command=get_fun,  font=("Arial", 25), bg = "orange", fg = "blue")
getb.place(x = 300, y = 580)

def clear_fun():
    x_entry.delete(0,END)
    y_entry.delete(0, END)
    w_entry.delete(0, END)
    h_entry.delete(0, END)

# Get Images Button
clearb=Button(window1, text="CLEAR",command=clear_fun,  font=("Arial", 25), bg = "yellow", fg = "blue")
clearb.place(x = 590, y = 580)

def exit_win1():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window1.destroy()

# Get Images Button
getb=Button(window1, text="EXIT",command=exit_win1,  font=("Arial", 25), bg = "red", fg = "blue")
getb.place(x = 780, y = 580)

window1.protocol("WM_DELETE_WINDOW", exit_win1)
window1.mainloop()

