
# Spelling Corrector

import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
from PIL import Image, ImageTk
from textblob import TextBlob

firstclick1 = True
def on_e1_click(event):
    """function that gets called whenever entry1 is clicked"""
    global firstclick1

    if firstclick1: # if this is the first time they clicked it
        firstclick1 = False
        e1.delete(0, "end") # delete all the text in the entry

def correct_word():
    user_word = e1.get()
    ans = TextBlob(user_word).correct()
    e2text.delete('1.0', END)
    e2text.insert(END, ans)


window = Tk()
window.geometry("1000x700")
window.title("Spelling Corrector")

# image on the main window
path = "Images/spell.jpg"
# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))
# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image = img, anchor = "nw")
# The Pack geometry manager packs widgets in rows or columns.
# panel.pack(side = "top", fill = "both", expand = "no")
panel.place(x = 290, y = 110)

start1 = tk.Label(text = "SPELLING  CORRECTOR", font=("Arial", 50), fg="magenta",underline=0) # same way bg
start1.place(x = 100, y = 10)

e1label = tk.Label(text = "Word : ", font=("Arial", 30), fg="brown") # same way bg
e1label.place(x = 100, y = 380)

e1 = Entry(window,font=("Arial", 30) , width=25, border=2)
e1.insert(0, 'Enter your word here...')
e1.bind('<FocusIn>', on_e1_click)
e1.place(x = 240, y = 380)

e2label = tk.Label(text = "Corrected Spelled Word is : ", font=("Arial", 30), fg="brown") # same way bg
e2label.place(x = 230, y = 450)

def clear_label():
    e1.delete(0, "end")
    e2text.delete('1.0', END)

e2text = tk.Text(window, height=1, width=28, font=("Arial", 30), bg="light yellow", fg="green", borderwidth=3, relief="solid")
e2text.place(x=180, y=500)

correctb = Button(window, text="CORRECT",command=correct_word,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
correctb.place(x =230 , y =590 )

clearb = Button(window, text="CLEAR",command=clear_label,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
clearb.place(x =470 , y =590 )

def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 20), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =670 , y =590 )


window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()