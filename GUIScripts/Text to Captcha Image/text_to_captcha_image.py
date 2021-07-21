
# Text to Captcha Image

# imported necessary library
import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
from captcha.image import ImageCaptcha
import PIL
from PIL import ImageTk, Image
import cv2

#created main window
window = Tk()
window.geometry("1000x700")
window.title("Text to Captcha Image")

panelB = None
img = Image.open("Images/original.jpg")
img = ImageTk.PhotoImage(img)
if panelB == None:
    panelB = Label(image=img)
    panelB.image = img
    # panelB.pack(side="right", padx=10, pady=10)
    panelB.place(x = 600, y = 440)

# top label
start1 = tk.Label(text = "TEXT TO CAPTCHA IMAGE", font=("Arial", 50,"underline"), fg="magenta") # same way bg
start1.place(x = 55, y = 10)

# info label
start1 = tk.Label(text = "Enter any text \nand make Captcha Image", font=("Arial", 45), fg="green") # same way bg
start1.place(x = 140, y = 100)

# Text label
start1 = tk.Label(text = "TEXT", font=("Arial", 40), fg="brown") # same way bg
start1.place(x =190, y = 310)

# text Entry Box
text_entry = Entry(window, font=("Arial", 45), fg='orange', bg="light yellow", borderwidth=3, width=13)
text_entry.place(x=50, y=450)

# captcha image label
start1 = tk.Label(text = "CAPTCHA\nIMAGE", font=("Arial", 40), fg="brown") # same way bg
start1.place(x = 600, y = 280)

def convert_fun():
    input_text = text_entry.get()
    if(input_text==""):
        mbox.showerror("Error","You entered NO text.")
    else:
        ic = ImageCaptcha()
        ic.write(input_text,"Captcha_Image.jpg")
        img = Image.open("Captcha_Image.jpg")
        img = ImageTk.PhotoImage(img)
        panelB.configure(image = img)
        mbox.showinfo("Success","Captcha Image Created Successfully.")

# convert button created
convertb = Button(window, text="CONVERT",command=convert_fun,font=("Arial", 25), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
convertb.place(x =100 , y =580 )

def clear_fun():
    text_entry.delete(0,END)

# convert button created
clearb = Button(window, text="CLEAR",command=clear_fun,font=("Arial", 25), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
clearb.place(x =450 , y =580 )

# function created for exiting
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

# exit button created
exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 25), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =800 , y =580 )


window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()