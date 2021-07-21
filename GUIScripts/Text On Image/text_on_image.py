
# Text On Image

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
frame.title('Text On Image')
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
    # print(frame.img_dir)
    onlyfilename = os.path.basename(frame.img_dir)
    fullfilename = os.path.abspath(frame.img_dir)

    # print(onlyfilename)
    # print(fullfilename)
    fname.delete('1.0', END)
    fname.insert(END, onlyfilename)
    fullname.delete('1.0', END)
    fullname.insert(END, fullfilename)
    # img = Image.open(frame.img_dir) # opening the selected image
    #
    # img = cv2.imread(fullfilename)
    # edge = Image.fromarray(img)
    #
    # # tk_edge = ImageTk.PhotoImage(edge)
    # # label = tk.Label(frame, image=tk_edge)
    # # label.pack()

def save_img():
    filename = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")
    if not filename:
        return
    edge.save(filename)
    mbox.showinfo("Success", "File Saved Successfully!")

def enter_fun():
    mbox.showinfo("Enter Text", "Click on OK, and Image appears.\n\nStart Entering any text you want.\n\nTo Stop, press ESC key.")
    global fullfilename

    text_pos = int(pos_entry.get())
    text_wid = int(line_entry.get())
    text_her = her_var.get()
    text_type = type_var.get()
    text_color = str(color_entry.get())
    s = text_color.split(" ")
    # print(s)
    r1 = int(s[0])
    g1 = int(s[1])
    b1 = int(s[2])
    # print(r1,g1,b1)

    img = cv2.imread(fullfilename)
    font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
    i = 10
    while (1):
        cv2.imshow('img', img)

        k = cv2.waitKey(33)
        if k == 27:  # Esc key to stop
            break
        elif k == -1:  # normally -1 returned,so don't print it
            continue
        else:
            # print(k)  # else print its value
            # cv2.putText(img, chr(k), (i, 100), font, 1, (30, 30, 30), 1, cv2.LINE_AA)
            cv2.putText(img, chr(k), (i, text_pos), font, text_wid, (r1,g1,b1), 1, cv2.LINE_AA)
            i += 20

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# starting label
start1 = Label(frame, text='TEXT  ON  IMAGE', font=("Arial",50),fg="magenta")
start1.place(x=200,y=10)

# label for info
pickL = Label(frame, text='Select any Image :', font=("Arial", 35),fg="green")
pickL.place(x=300,y=100)

# label defined that will be beside the choose button
pickL = Label(frame, text='Select your image  :  ', font=("Arial", 30),fg="brown")
pickL.place(x=50,y=170)

# textarea for file name only
fname = Text(frame,height = 1, width = 20, font=("Arial", 25), bg = "light yellow", fg = "brown", borderwidth=2, relief="solid")
fname.place(x=420, y = 175)

# created a choose button , to choose the image from the local system
pickB = Button(frame, text='SELECT', command=img_choose, font=("Arial", 17), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
pickB.place(x=800, y=170)

# label defined that will be beside the full path
pickL = Label(frame, text='Full Path : ', font=("Arial", 30),fg="brown")
pickL.place(x=50,y=240)

# textarea for full path
fullname = Text(frame,height = 1, width = 37, font=("Arial", 25), bg = "light yellow", fg = "brown", borderwidth=2, relief="solid")
fullname.place(x=250, y = 245)

# label for text font
pickL = Label(frame, text='Select Text Style :', font=("Arial", 35),fg="green")
pickL.place(x=300,y=320)

# label for position
pickL = Label(frame, text='Position(Y) : ', font=("Arial", 30),fg="brown")
pickL.place(x=50,y=390)

# position entry
pos_entry = Entry(frame, font=("Arial", 25), fg='orange', bg="light yellow", borderwidth=3, width=10)
pos_entry.place(x=280, y=395)

# label for line width
pickL = Label(frame, text='Line Width : ', font=("Arial", 30),fg="brown")
pickL.place(x=520,y=390)

# line Width entry
line_entry = Entry(frame, font=("Arial", 25), fg='orange', bg="light yellow", borderwidth=3, width=10)
line_entry.place(x=750, y=395)

# label for line width
pickL = Label(frame, text='Hershey Font : ', font=("Arial", 30),fg="brown")
pickL.place(x=50,y=460)

# creating the drop down menu button
her_var = tk.StringVar()
her_choices = ["FONT_HERSHEY_SIMPLEX","FONT_HERSHEY_PLAIN","FONT_HERSHEY_DUPLEX","FONT_HERSHEY_COMPLEX","FONT_HERSHEY_TRIPLEX","FONT_HERSHEY_COMPLEX_SMALL","FONT_HERSHEY_SCRIPT_SIMPLEX","FONT_HERSHEY_SCRIPT_COMPLEX","FONT_ITALIC"]
her_menu = OptionMenu(frame, her_var, *her_choices)
her_menu.config(font=("Arial", 25), bg = "light green", fg = "blue", borderwidth=3)
her_menu["menu"].config(font=("Arial", 20), bg = "light yellow", fg = "blue")
her_menu.place(x=330, y=455)
her_var.set("FONT_HERSHEY_SIMPLEX")

# label for line width
pickL = Label(frame, text='Line Type : ', font=("Arial", 30),fg="brown")
pickL.place(x=50,y=530)

# creating the drop down menu button
type_var = tk.StringVar()
type_choices = ["FILLED","LINE_4","LINE_8","LINE_AA"]
type_menu = OptionMenu(frame, type_var, *type_choices)
type_menu.config(font=("Arial", 25), bg = "light green", fg = "blue", borderwidth=3)
type_menu["menu"].config(font=("Arial", 20), bg = "light yellow", fg = "blue")
type_menu.place(x=260, y=525)
type_var.set("FILLED")

# label for line width
pickL = Label(frame, text='Text Color : ', font=("Arial", 30),fg="brown")
pickL.place(x=480,y=530)

# line Width entry
color_entry = Entry(frame, font=("Arial", 25), fg='orange', bg="light yellow", borderwidth=3, width=13)
color_entry.place(x=700, y=535)

# creating the clear button
enter1 = Button(frame, text='ENTER', command=enter_fun, font=("Arial", 20), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
enter1.place(x = 150, y = 610)

# function defined to clear the text from entry area
def reset_style():
    pos_entry.delete(0,END)
    line_entry.delete(0,END)
    her_var.set("FONT_HERSHEY_SIMPLEX")
    type_var.set("FILLED")

# creating the clear button
clear1 = Button(frame, text='RESET', command=reset_style, font=("Arial", 20), bg = "yellow", fg = "blue", borderwidth=3, relief="raised")
clear1.place(x = 430, y = 610)

# defined exit_win function, to show a exit dialog box when tried to exit
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        frame.destroy()

# creating an exit button
prevB = Button(frame, text='EXIT', command=exit_win, font=("Arial", 20), bg = "red", fg = "blue", borderwidth=3, relief="raised")
prevB.place(x = 740, y = 610)

# this is done to show the exit dialog box when tried to exit from the main window, using the top-roght close button of titlebar
frame.protocol("WM_DELETE_WINDOW", exit_win)
frame.mainloop()