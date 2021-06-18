
'''

This script is about converting any image to corresponding icon file (i.e. .ico file)
libraries used :
tkinter - for creating gui, button, labels and all
from tkinter used filedialog, for choosing image from the local system

function defined:
1.) img_choose() - to choose an image from the local system
2.) img_convt() - to convert the selected image into icon file
3.) preview() - to let the user see how the image is converted to icon, by placing the icon on the title nar of the pop up window

'''

# importing necessary library
from tkinter import * # from tkinter we import everything
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog # from tkinter importing file dialog box
import tkinter.messagebox as mbox # for displaying the dialog box
import os

# Main Window
frame = Tk()
frame.title('Image to Icon Converter')
frame.geometry('700x500')


# Function defined Selecting the image from the local system
def img_choose():
    from PIL import Image # we only import Image not ImageTk, beacause we are nit displaying in file, just choosing
    global img # we need to defined this img global, because we have to use in whole window

    # initialdir is C:, which is our window folder
    frame.img_dir = filedialog.askopenfilename(initialdir='C:', title='Choose an image',
                                             filetypes=(('PNG Imaged', '*.png'),
                                                        ('JPG Icons', '*.jpg'),
                                                        ('All files', '*.*')))
    onlyfilename = os.path.basename(frame.img_dir)
    fname.delete('1.0', END)
    fname.insert(END, onlyfilename)
    # filename = Label(frame, text=onlyfilename, font=("Arial", 20),fg="brown")
    # filename.place(x=450,y=100)
    img = Image.open(frame.img_dir) # opening the selected image


# Function defined to Convert image to .ico and save it to same location from where image is selected
def img_convt():
    try:
        # from PIL import Image
        img.save(f'{icon_name.get()}.ico', format='ICO', sizes=[(ico_size.get(), ico_size.get())])
        mbox.showinfo("Success", "Converted successfully!")
    except:
        mbox.showerror("Failure", "Something went wrong!")


# function defined to preview the converted .ico icon
def preview():
    prev = Toplevel()
    prev.title('Icon Preview')
    prev.geometry('400x50')
    prev.iconbitmap(f'{icon_name.get()}.ico')

    lbl = Label(prev, text='Check your icon on the title bar!', font=("Arial", 15),fg="brown")
    lbl.pack()

    prev.mainloop() # running the mainloop for preview button

# function defined to clear the text from entry area
def clear_text():
    icon_name.delete(0, END)

firstclick1 = True
def on_click(event):
    """function that gets called whenever entry1 is clicked"""
    global firstclick1

    if firstclick1: # if this is the first time they clicked it
        firstclick1 = False
        icon_name.delete(0, "end") # delete all the text in the entry

# starting label
start1 = Label(frame, text='Image to Icon Converter', font=("Arial", 35),fg="magenta",underline=0)
start1.place(x=100,y=10)

# label defined that will be beside the choose button
pickL = Label(frame, text='Select your image    : ', font=("Arial", 25),fg="brown")
pickL.place(x=10,y=100)
# pickL.grid(row=0, column=0, pady=10)

fname = Text(frame,height = 1, width = 15, font=("Arial", 15), bg = "light yellow", fg = "brown", borderwidth=2, relief="solid")
fname.place(x=350, y = 110)

# created a choose button , to choose the image from the local system
pickB = Button(frame, text='SELECT', command=img_choose, font=("Arial", 15), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
pickB.place(x=550, y=100)
# pickB.grid(row=0, column=1, pady=10)

# Creating a label for drop down menu button
siz_lbl = Label(frame, text='Select the icon size  :', font=("Arial", 25),fg="brown")
siz_lbl.place(x=10,y=180)
# siz_lbl.grid(row=1, column=0, pady=10)

# creating the drop down menu button
ico_size = tk.IntVar()
# as icon size are really small, we defined the following 7 sizes
sizes = [16, 24, 32, 48, 64, 128, 255]
siz_menu = OptionMenu(frame, ico_size, *sizes)
# siz_menu = ttk.OptionMenu(frame, ico_size,'Choose Size', *sizes)
# siz_menu.config(width = 10) # no effect can be added
siz_menu.config(font=("Arial", 15), bg = "light green", fg = "blue", borderwidth=3)
siz_menu["menu"].config(font=("Arial", 12), bg = "light yellow", fg = "blue")
siz_menu.place(x=350, y=180)
# siz_menu.grid(row=1, column=1, pady=10)
ico_size.set(32) # size 32 is selected as by default, and we can

# Created label for getting the name of the icon
nam_lbl = Label(frame, text='Enter the icon name : ', font=("Arial", 25),fg="brown")
nam_lbl.place(x=10, y=260)
# nam_lbl.grid(row=2, column=0, pady=10)

# getting the name of icon from user
icon_name = Entry(frame, font=("Arial", 20) , width=20, border=2)
icon_name.insert(0, 'Enter icon name...')
icon_name.bind('<FocusIn>', on_click)
icon_name.place(x=350, y=260)
# icon_name.grid(row=2, column=1, pady=10)

# Creating the button to convert the image to icon file
conB = Button(frame, text='CONVERT', command=img_convt, font=("Arial", 15), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
conB.place(x = 150, y = 350)
# conB.grid(row=3, column=0, pady=10)

# Creating the preview button to let the user see how the image is converted into icon file, by showing the icon file in titlw of window
prevB = Button(frame, text='PREVIEW', command=preview, font=("Arial", 15), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
prevB.place(x = 300, y = 350)
# prevB.grid(row=3, column=1, pady=10)

# creating the clear button
clear1 = Button(frame, text='CLEAR', command=clear_text, font=("Arial", 15), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
clear1.place(x = 450, y = 350)

# defined exit_win function, to show a exit dialog box when tried to exit
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        frame.destroy()

# creating an exit button
prevB = Button(frame, text='EXIT', command=exit_win, font=("Arial", 15), bg = "red", fg = "blue", borderwidth=3, relief="raised")
prevB.place(x = 325, y = 420)

# this is done to show the exit dialog box when tried to exit from the main window, using the top-roght close button of titlebar
frame.protocol("WM_DELETE_WINDOW", exit_win)
frame.mainloop()