
# Screenshot Taker

import tkinter
from tkinter import *
import tkinter as tk
import time
import pyautogui
import tkinter.messagebox as mbox


window = Tk()
window.geometry("1200x800")
window.title("Screenshot Taker")

cnt_single = 0
def screen_single_take():
    global image, cnt_single
    name = "screenshot_single"
    # name = 'screenshot.png'
    cnt_single = cnt_single + 1
    name = name + str(cnt_single)
    name = name + ".png"
    image = pyautogui.screenshot(name)
    mbox.showinfo("Success", "Single screenshot taken successfully.\n\nSaved in Project Folder as  :  " + name)

def screen_single_show():
    image.show()

cnt_multiple = 0
def screen_multiple_take():
    global image, cnt_multiple
    cnt_multiple = int(no_entry.get())
    s = ""
    for i in range(1,cnt_multiple+1):
        name = "screenshot_multiple"
        # name = 'screenshot.png'
        name = name + str(i)
        name = name + ".png"
        image = pyautogui.screenshot(name)
        s = s + name
        s = s + ", "
    mbox.showinfo("Success", "Multiple screenshot taken successfully.\n\nSaved in Project Folder as  :  " + s)

def screen_multiple_show():
    for i in range(0,cnt_multiple):
        image.show()


# top label
start1 = tk.Label(text = "SCREENSHOT TAKER", font=("Arial", 50), fg="magenta") # same way bg
start1.place(x = 150, y = 10)

# take single label
take1 = tk.Label(text = "Want to take a single screenshot...", font=("Arial", 30), fg="brown") # same way bg
take1.place(x = 100, y = 130)

# single screenshot button
take1b = Button(window, text="Take Single Screenshot",command=screen_single_take,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
take1b.place(x =200 , y =210 )

# show single button
show1b = Button(window, text="Show Screenshot",command=screen_single_show,font=("Arial", 20), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
show1b.place(x =700 , y =210 )

# take single label
takem = tk.Label(text = "Want to take multiple screenshot...", font=("Arial", 30), fg="brown") # same way bg
takem.place(x = 100, y = 350)

# enter no. label
no_lbl = tk.Label(text = "Enter No. : ", font=("Arial", 30), fg="green") # same way bg
no_lbl.place(x = 280, y = 430)

# Entry Box
no_entry = Entry(window, font=("Arial", 25), fg='brown', bg="light yellow", borderwidth=3, width=9)
no_entry.place(x=540, y=430)

# take multiple screenshot label
takemb = Button(window, text="Take multiple Screenshot",command=screen_multiple_take,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
takemb.place(x =200 , y =520 )

# show multiple button
showmb = Button(window, text="Show Screenshot",command=screen_multiple_show,font=("Arial", 20), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
showmb.place(x =700 , y =520 )


def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 25), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =520 , y =650 )


window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()