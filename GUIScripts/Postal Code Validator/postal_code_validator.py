
# Postal Code Validator

# imported necessary library
import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
from PIL import Image, ImageTk
import pandas as pd
import re


# created main window
window = Tk()
window.geometry("1000x700")
window.title("Postal Code Validator")

# read the csv data
data = pd.read_csv("pincode_data.csv")
Pincode = data['Pincode'].tolist()
District = data['District'].tolist()
StateName = data['StateName'].tolist()

# function for showing validity rules
def valid_fun():
    mbox.showinfo("VALID POSTAL CODE RULES","A valid postal code have to fullfil both below requirements :\n\n1.)  Must be a number in the range from 100000 to 999999 inclusive.\n2.)  Must not contain more than one alternating repetitive digit pair.")

# function to check validity of Postal code
def validate_fun():
    global valid
    entered_code = code_entry.get()
    valid = len(re.findall(r'(?=(\d)\d\1)',entered_code)) < 2 and bool(re.match(r'^[1-9][0-9]{5}$',entered_code))
    if(valid):
        mbox.showinfo("Validity Status","The Postal Code " + entered_code + " is VALID.")
    else:
        mbox.showerror("Validity Error", "THe Postal Code " + entered_code + " is INVALID.")

# function for locating the Valid Postal Code using csv data
def locate_fun():
    entered_code = code_entry.get()
    if(valid):
        for i in range(0,len(Pincode)):
            if(str(Pincode[i])==str(entered_code)):
                mbox.showinfo("Locate Postal Code", "Postal Code  :  " + entered_code + "\n\nDistrict Name  :  " + District[i] + "\n\nState Name  :  " + StateName[i])
                break
    else:
        mbox.showerror("Locate Error", "The Postal Code in INVALID. So can't locate.")

# top label
start1 = tk.Label(text = "POSTAL CODE VALIDATOR", font=("Arial", 40), fg="magenta") # same way bg
start1.place(x = 150, y = 10)

# image on the main window
path = "Images/postal_code1.jpg"
img1 = ImageTk.PhotoImage(Image.open(path))
# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image = img1)
panel.place(x = 135, y = 80)

# Button for rules
vpcrb = Button(window, text="VALID POSTAL CODE RULES",command=valid_fun,font=("Arial", 25), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
vpcrb.place(x =238 , y =425 )

# label for Entering Postal Code ---------------------------------------------------------------------------------
sel_label = tk.Label(text = "ENTER POSTAL CODE : ", font=("Arial", 35), fg="brown") # same way bg
sel_label.place(x = 50, y = 515)

# Created Entry Box
code_entry = Entry(window, font=("Arial", 30), fg='orange', bg="light yellow", borderwidth=3, width=14)
code_entry.place(x=600, y=520)

# created Locate Button
locateb = Button(window, text="LOCATE",command=locate_fun,font=("Arial", 25), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
locateb.place(x =100 , y =600 )

# created Validate button
validateb = Button(window, text="VALIDATE",command=validate_fun,font=("Arial", 25), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
validateb.place(x =320 , y =600 )

# function for clearing the entry box
def clear_entry():
    code_entry.set(0,END)

# created clear button
clearb = Button(window, text="CLEAR",command=clear_entry,font=("Arial", 25), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
clearb.place(x =570 , y =600 )

# function for exiting
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

# created exit button
exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 25), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =780 , y =600 )


window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()