
# WEBSITE STATUS CHECKER

# imported necessary library
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
from pil import ImageTk, Image
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import webbrowser


# Main Window & Configuration
window = tk.Tk() # created a tkinter gui window frame
window.title("Website Status Checker") # title given is "DICTIONARY"
window.geometry('1000x700')

# top label
start1 = tk.Label(text = "WEBSITE   STATUS\nCHECKER", font=("Arial", 55,"underline"), fg="magenta") # same way bg
start1.place(x = 120, y = 10)

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
panel.place(x = 170, y = 200)

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
window1.title("Website Status Checker") # title given is "DICTIONARY"
window1.geometry('1000x700')


def check_fun():
    input_add = path_text.get("1.0", "end-1c")

    req = Request(input_add)
    try:
        response = urlopen(req)
    except HTTPError as e:
        # print('The server couldn\'t fulfill the request.')
        # print('Error code: ', e.code)
        lbl2.configure(text = 'The server couldn\'t fulfill the request.')
        lbl3.configure(text='Error code : ' + str(e.code))
    except URLError as e:
        lbl2.configure(text='Failed to reach a server..')
        lbl3.configure(text='Reason : ' + str(e.reason))
        # print('We failed to reach a server.')
        # print('Reason: ', e.reason)
    else:
        lbl2.configure(text='Website is working fine')
        # print('Website is working fine')

#Define a callback function
def callback(url):
   webbrowser.open_new_tab(url)

def open_fun():
    input_add = path_text.get("1.0", "end-1c")
    callback(input_add)

# top label
start1 = tk.Label(text = "WEBSITE   STATUS\nCHECKER", font=("Arial", 50, "underline"), fg="magenta") # same way bg
start1.place(x = 160, y = 10)

lbl1 = tk.Label(text="Enter any web address and check status...", font=("Arial", 35),fg="green")  # same way bg
lbl1.place(x=50, y=180)

path_text = tk.Text(window1, height=1, width=40, font=("Arial", 30), bg="light yellow", fg="orange",borderwidth=2, relief="solid")
path_text.place(x=50, y = 240)

lbl2 = tk.Label(font=("Arial", 30),fg="gray")  # same way bg
lbl2.place(x=50, y=320)

lbl3 = tk.Label(font=("Arial", 30),fg="gray")  # same way bg
lbl3.place(x=50, y=400)

# Select Button
selectb=Button(window1, text="CHECK STATUS",command=check_fun,  font=("Arial", 25), bg = "light green", fg = "blue")
selectb.place(x = 400, y = 500)

# Get Images Button
getb=Button(window1, text="OPEN WEBSITE",command=open_fun,  font=("Arial", 25), bg = "orange", fg = "blue")
getb.place(x = 80, y = 580)

def clear_fun():
    path_text.delete("1.0", "end")

# Get Images Button
clearb=Button(window1, text="CLEAR",command=clear_fun,  font=("Arial", 25), bg = "yellow", fg = "blue")
clearb.place(x = 460, y = 580)

def exit_win1():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window1.destroy()

# Get Images Button
getb=Button(window1, text="EXIT",command=exit_win1,  font=("Arial", 25), bg = "red", fg = "blue")
getb.place(x = 750, y = 580)

window1.protocol("WM_DELETE_WINDOW", exit_win1)
window1.mainloop()

'''

# another method
# import requests
# 
# URL = "https://github.com/KISHOREMUTHU/ETE2---Sparky"
# 
# try:
#     response = requests.head(URL)
# except Exception as e:
#     print(f"NOT OK: {str(e)}")
# else:
#     if response.status_code == 200:
#         print("OK")
#     else:
#         print(f"NOT OK: HTTP response code {response.status_code}")

'''
