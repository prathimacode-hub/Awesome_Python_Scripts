
# Image Here to There

# importing necessary library
from tkinter import * # from tkinter we import everything
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog # from tkinter importing file dialog box
import tkinter.messagebox as mbox # for displaying the dialog box
from PIL import Image, ImageTk, ImageDraw
import os
import cv2

# Main Window
frame = Tk()
frame.title('Image Here To There')
frame.geometry('1000x700')

onlyfilename = ""
fullfilename = ""
edge = ""

# Function defined Selecting the image from the local system
def img_choose():
    global onlyfilename, fullfilename, edge
    from PIL import Image, ImageTk, ImageDraw # we only import Image not ImageTk, beacause we are nit displaying in file, just choosing
    global img # we need to defined this img global, because we have to use in whole window

    # initialdir is C:, which is our window folder
    frame.img_dir = filedialog.askopenfilename(initialdir='C:', title='Choose an image',
                                             filetypes=(('JPG Icons', '*.jpg'),
                                                        ('PNG Imaged', '*.png'),
                                                        ('All files', '*.*')))
    onlyfilename = os.path.basename(frame.img_dir)
    fullfilename = os.path.abspath(frame.img_dir)
    # print(onlyfilename)
    # print(fullfilename)
    fname.delete('1.0', END)
    fname.insert(END, onlyfilename)
    fullname.delete('1.0', END)
    fullname.insert(END, fullfilename)
    img = Image.open(frame.img_dir) # opening the selected image

    img = cv2.imread(fullfilename)
    edge = Image.fromarray(img)

    # tk_edge = ImageTk.PhotoImage(edge)
    # label = tk.Label(frame, image=tk_edge)
    # label.pack()

def save_img():
    filename = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")
    if not filename:
        return
    edge.save(filename)
    mbox.showinfo("Success", "File Saved Successfully!")

# function defined to clear the text from entry area
def clear_text():
    fname.delete('1.0', END)
    fullname.delete('1.0', END)

# starting label
start1 = Label(frame, text='Image Here To There', font=("Arial", 40),fg="magenta",underline=0)
start1.place(x=240,y=10)

# label defined that will be beside the choose button
pickL = Label(frame, text='Select your image  :  ', font=("Arial", 30),fg="brown")
pickL.place(x=50,y=100)

# textarea for file name only
fname = Text(frame,height = 1, width = 20, font=("Arial", 25), bg = "light yellow", fg = "brown", borderwidth=2, relief="solid")
fname.place(x=420, y = 105)

# created a choose button , to choose the image from the local system
pickB = Button(frame, text='SELECT', command=img_choose, font=("Arial", 17), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
pickB.place(x=800, y=100)

# label defined that will be beside the full path
pickL = Label(frame, text='Full Path : ', font=("Arial", 30),fg="brown")
pickL.place(x=50,y=180)

# textarea for full path
fullname = Text(frame,height = 1, width = 37, font=("Arial", 25), bg = "light yellow", fg = "brown", borderwidth=2, relief="solid")
fullname.place(x=250, y = 185)

# image on the main window
path = "Images/here_there.jpg"
# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img1 = ImageTk.PhotoImage(Image.open(path))
# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(frame, image = img1)
panel.place(x = 260, y = 250)

# creating the clear button
clear1 = Button(frame, text='SAVE', command=save_img, font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
clear1.place(x = 150, y = 600)

# creating the clear button
clear1 = Button(frame, text='CLEAR', command=clear_text, font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
clear1.place(x = 430, y = 600)

# defined exit_win function, to show a exit dialog box when tried to exit
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        frame.destroy()

# creating an exit button
prevB = Button(frame, text='EXIT', command=exit_win, font=("Arial", 20), bg = "red", fg = "blue", borderwidth=3, relief="raised")
prevB.place(x = 740, y = 600)

# this is done to show the exit dialog box when tried to exit from the main window, using the top-roght close button of titlebar
frame.protocol("WM_DELETE_WINDOW", exit_win)
frame.mainloop()