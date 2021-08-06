
# INSTAGRAM PROFILE DOWNLOADER

# imported necessary library
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
from pil import ImageTk, Image
import cv2
import glob
import webbrowser
import instaloader


# Main Window & Configuration
window = tk.Tk() # created a tkinter gui window frame
window.title("Instagram File Downloader")
window.geometry('1000x710')

#Define a callback function
def callback(url):
   webbrowser.open_new_tab(url)

# top label
start1 = tk.Label(text = "INSTA", font=("Arial", 45), fg="magenta3") # same way bg
start1.place(x = 30, y = 10)

# top label
start1 = tk.Label(text = "PROFILE", font=("Arial", 45), fg="VioletRed1") # same way bg
start1.place(x = 240, y = 10)

# top label
start1 = tk.Label(text = "DOWNLOADER", font=("Arial", 45), fg="gold2") # same way bg
start1.place(x = 530, y = 10)


def start_fun():
    window.destroy()

# start button created
startb = Button(window, text="▶\nSTART",command=start_fun,font=("Arial", 25), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
startb.place(x =50 , y =320 )

# goto button created
gotob = Button(window, text="GO TO INSTAGRAM",command=lambda:callback("https://www.instagram.com/"),font=("Arial", 25), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
gotob.place(x =335 , y =615 )

# image on the main window
path = "Images/front.png"
# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img1 = ImageTk.PhotoImage(Image.open(path))
# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image = img1)
panel.place(x = 250, y = 80)

# function created for exiting
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

# exit button created
exitb = Button(window, text="❌\n EXIT ",command=exit_win,font=("Arial", 25), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =820 , y = 320 )
window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()

# Main Window & Configuration
window1 = tk.Tk() # created a tkinter gui window frame
window1.title("Instagram File Downloader") # title given is "DICTIONARY"
window1.geometry('1000x700')


def preview_fun():
    global entered_user_name

    path1 = "./" + entered_user_name + "/*.jpg"
    # print(path1)
    # print(glob.glob(path1))
    for img in glob.glob(path1):
        # print("ksjd")
        cv_img = cv2.imread(img)
        cv2.imshow("Profile Pic", cv_img)

def down_fun():
    global entered_user_name
    entered_user_name = str(path_text.get("1.0", "end-1c"))

    ig = instaloader.Instaloader()
    ig.download_profile(entered_user_name, profile_pic_only=True)

    path = "./" + entered_user_name + "/id"
    # print(path)
    file1 = open(path, "r")
    # print(file1.read())
    id1.configure(text=str(file1.read()))
    mbox.showinfo("Success",entered_user_name + "'s Profile Downloaded Successfully.\n\nAnd Saved to Project Directory.")

start1 = tk.Label(text = "INSTAGRAM", font=("Arial", 55), fg="magenta3") # same way bg
start1.place(x = 80, y = 10)

# top label
start1 = tk.Label(text = "PROFILE", font=("Arial", 55), fg="VioletRed1") # same way bg
start1.place(x = 570, y = 10)

# top label
start1 = tk.Label(text = "DOWNLOADER", font=("Arial", 55), fg="gold2") # same way bg
start1.place(x = 220, y = 90)

lbl1 = tk.Label(text="Enter Insta User Name...", font=("Arial", 30),fg="brown")  # same way bg
lbl1.place(x=80, y=220)

path_text = tk.Text(window1, height=1, width=37, font=("Arial", 30), bg="light yellow", fg="orange",borderwidth=2, relief="solid")
path_text.place(x=80, y = 280)

lbl1 = tk.Label(text="Insta User ID  :  ", font=("Arial", 30),fg="brown")  # same way bg
lbl1.place(x=80, y=400)

id1 = tk.Label(font=("Arial", 30),fg="orange")  # same way bg
id1.place(x=360, y=400)

# Get Images Button
getb=Button(window1, text="DOWNLOAD",command=down_fun,  font=("Arial", 25), bg = "light green", fg = "blue")
getb.place(x = 400, y = 500)

# Get Images Button
getb=Button(window1, text="PROFILE",command=preview_fun,  font=("Arial", 25), bg = "orange", fg = "blue")
getb.place(x = 100, y = 590)

def clear_fun():
    path_text.delete("1.0", "end")

# Get Images Button
clearb=Button(window1, text="CLEAR",command=clear_fun,  font=("Arial", 25), bg = "yellow", fg = "blue")
clearb.place(x = 445, y = 590)

def exit_win1():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window1.destroy()

# Get Images Button
getb=Button(window1, text="EXIT",command=exit_win1,  font=("Arial", 25), bg = "red", fg = "blue")
getb.place(x = 780, y = 590)

window1.protocol("WM_DELETE_WINDOW", exit_win1)
window1.mainloop()

