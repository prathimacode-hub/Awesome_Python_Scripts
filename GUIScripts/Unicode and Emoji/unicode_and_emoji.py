
# Unicode and Emoji

# importing necessary library
from tkinter import *  # from tkinter we import everything
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.messagebox as mbox
import emoji
import pandas as pd

data = pd.read_csv('emoji_df.csv')
emoji1 = data['emoji'].tolist()
code1 = data['codepoints'].tolist()


# Main Window
frame = Tk()
frame.title('Unicode and Emoji')
frame.geometry('950x700')
# frame.configure(bg = "white")


# image on the main window
path = "Images/front.jpg"
# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img1 = ImageTk.PhotoImage(Image.open(path))
# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(frame, image = img1)
panel.place(x = 55, y = 110)

# starting label
start1 = Label(frame, text='UNICODE & EMOJI', font=("Arial", 55,"underline"),fg="magenta")
start1.place(x=130,y=10)

def start_fun():
    frame.destroy()

# creating an exit button
prevB = Button(frame, text='START', command=start_fun, font=("Arial", 25), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
prevB.place(x = 120, y = 590)

# defined exit_win function, to show a exit dialog box when tried to exit
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        frame.destroy()

# creating an exit button
prevB = Button(frame, text='EXIT', command=exit_win, font=("Arial", 25), bg = "red", fg = "blue", borderwidth=3, relief="raised")
prevB.place(x = 700, y = 590)

# this is done to show the exit dialog box when tried to exit from the main window, using the top-roght close button of titlebar
frame.protocol("WM_DELETE_WINDOW", exit_win)
frame.mainloop()

# Main Window
frame1 = Tk()
frame1.title('Unicode and Emoji')
frame1.geometry('950x700')

# image on the main window
path1 = "Images/second.jpg"
# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img2 = ImageTk.PhotoImage(Image.open(path1))
# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel1 = tk.Label(frame1, image = img2)
panel1.place(x = 465, y = 110)

# starting label
start1 = Label(frame1, text='UNICODE & EMOJI', font=("Arial", 55,"underline"),fg="magenta")
start1.place(x=130,y=10)

# starting label
start1 = Label(frame1, text='Emoji to\nUnicode', font=("Arial", 40),fg="green")
start1.place(x=100,y=120)

# starting label
start1 = Label(frame1, text='Emoji', font=("Arial", 30),fg="brown")
start1.place(x=50,y=250)

# emoji Box
l1_entry = Entry(frame1, font=("Arial", 25), fg='brown', bg="light yellow", borderwidth=3, width=18)
l1_entry.place(x=50, y=300)

# starting label
start1 = Label(frame1, text='Unicode', font=("Arial", 30),fg="brown")
start1.place(x=50,y=400)

# unicode Box
l2_entry = Entry(frame1, font=("Arial", 25), fg='brown', bg="light yellow", borderwidth=3, width=18)
l2_entry.place(x=50, y=450)

# starting label
start1 = Label(frame1, text='Unicode\nto Emoji', font=("Arial", 40),fg="green")
start1.place(x=620,y=120)

# starting label
start1 = Label(frame1, text='Unicode', font=("Arial", 30),fg="brown")
start1.place(x=550,y=250)

# unicode Box
r1_entry = Entry(frame1, font=("Arial", 25), fg='brown', bg="light yellow", borderwidth=3, width=18)
r1_entry.place(x=550, y=300)

# starting label
start1 = Label(frame1, text='Emoji', font=("Arial", 30),fg="brown")
start1.place(x=550,y=400)

# emoji Box
r2_entry = Entry(frame1, font=("Arial", 25), fg='brown', bg="light yellow", borderwidth=3, width=18)
r2_entry.place(x=550, y=450)

def uni_fun():
    # emoji_entered = str(l1_entry.get())
    # uc_sentence = emoji_entered.encode('unicode-escape')
    # l2_entry.insert(0,uc_sentence)
    emoji_entered = str(l1_entry.get())
    for i in range(0,len(emoji1)):
        if emoji1[i]==emoji_entered:
            l2_entry.delete(0,END)
            l2_entry.insert(0, code1[i])
            break

def emo_fun():
    code_entered = str(r1_entry.get())
    for i in range(0, len(code1)):
        if code1[i] == code_entered:
            r2_entry.delete(0,END)
            r2_entry.insert(0, emoji1[i])
            break

# creating an exit button
prevB = Button(frame1, text='GET UNICODE', command=uni_fun, font=("Arial", 25), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
prevB.place(x = 70, y = 550)

# creating an exit button
prevB = Button(frame1, text='GET EMOJI', command=emo_fun, font=("Arial", 25), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
prevB.place(x = 650, y = 550)


# defined exit_win function, to show a exit dialog box when tried to exit
def exit_win1():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        frame1.destroy()

# creating an exit button
prevB = Button(frame1, text='EXIT', command=exit_win1, font=("Arial", 25), bg = "red", fg = "blue", borderwidth=3, relief="raised")
prevB.place(x = 420, y = 600)

# this is done to show the exit dialog box when tried to exit from the main window, using the top-roght close button of titlebar
frame1.protocol("WM_DELETE_WINDOW", exit_win1)
frame1.mainloop()