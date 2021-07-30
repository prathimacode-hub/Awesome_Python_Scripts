
# GUI Scroll View

# imported necessary library
import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
from PIL import ImageTk, Image


# Main Window & Configuration
window = tk.Tk()  # created a tkinter gui window frame
window.title("GUI Scroll View")
window.geometry('920x700')

canvas = tk.Canvas(window)
scrolly = tk.Scrollbar(window, orient='vertical', command=canvas.yview)

pressedY = 0

def mouse_pressed(e, label):
    pressedY = e.y
    print('p',e, label)

def mouse_released(e, label):
    print('r',e, label)

def mouse_motion(e, label):
    m = pressedY - e.y
    # print('m',e, label)
    canvas.yview_scroll(int(-1*(m/50)), "units")


labelList = []

# # top label
# start1 = tk.Label(text="GUI SCROLL VIEW", font=("Arial", 55, "underline"), fg="magenta")  # same way bg
# start1.place(x=150, y=10)

img1 = ImageTk.PhotoImage(Image.open("Images/front.jpg"))
labelList.append(tk.Label(canvas, image=img1))

for i in range(20):
    labelList.append(tk.Label(canvas, text = ""))

img2 = ImageTk.PhotoImage(Image.open("Images/f1.jpg"))
labelList.append(tk.Label(canvas, image=img2))

for i in range(12):
    labelList.append(tk.Label(canvas, text = ""))

labelList.append(tk.Label(canvas, text = "GALLERY", font = ("Arial",55), fg = "green"))# --------- 35

#---------------------------- flower -----------------
for i in range(4):
    labelList.append(tk.Label(canvas, text = ""))

labelList.append(tk.Label(canvas, text = "FLOWER", font = ("Arial",40), fg = "brown"))

for i in range(11):
    labelList.append(tk.Label(canvas, text = ""))

img3 = ImageTk.PhotoImage(Image.open("Images/f2.jpg"))
labelList.append(tk.Label(canvas, image=img3)) #------------------------ 52

#---------------------------- Pet -----------------
for i in range(11):
    labelList.append(tk.Label(canvas, text = ""))

labelList.append(tk.Label(canvas, text = "PET", font = ("Arial",40), fg = "brown"))

for i in range(12):
    labelList.append(tk.Label(canvas, text = ""))

img4 = ImageTk.PhotoImage(Image.open("Images/f3.jpg"))
labelList.append(tk.Label(canvas, image=img4)) # ------------------------- 77

#---------------------------- Food -----------------
for i in range(13):
    labelList.append(tk.Label(canvas, text = ""))

labelList.append(tk.Label(canvas, text = "FOOD", font = ("Arial",40), fg = "brown"))

for i in range(10):
    labelList.append(tk.Label(canvas, text = ""))

img5 = ImageTk.PhotoImage(Image.open("Images/f4.jpg"))
labelList.append(tk.Label(canvas, image=img5)) # ---------------------------- 102

#---------------------------- Earth -----------------
for i in range(11):
    labelList.append(tk.Label(canvas, text = ""))

labelList.append(tk.Label(canvas, text = "EARTH", font = ("Arial",40), fg = "brown"))

for i in range(10):
    labelList.append(tk.Label(canvas, text = ""))

img6 = ImageTk.PhotoImage(Image.open("Images/f5.jpg"))
labelList.append(tk.Label(canvas, image=img6)) # ---------------------------- 125

#---------------------------- End -----------------
for i in range(12):
    labelList.append(tk.Label(canvas, text = ""))

labelList.append(tk.Label(canvas, text = "END", font = ("Arial",50), fg = "brown")) # ------------ 138

for i in range(138):
    canvas.create_window(0, 20 * i, window=labelList[i])
    labelList[i].bind("<Button-1>",lambda e,i=i:mouse_pressed(e, labelList[i]))
    labelList[i].bind("<ButtonRelease-1>",lambda e,i=i:mouse_released(e, labelList[i]))
    labelList[i].bind("<B1-Motion>",lambda e,i=i:mouse_motion(e, labelList[i]))

# canvas.create_window(0, 20 * i, window=labelList[i])
# labelList[i].bind("<Button-1>",lambda e,i=i:mouse_pressed(e, labelList[i]))
# labelList[i].bind("<ButtonRelease-1>",lambda e,i=i:mouse_released(e, labelList[i]))
# labelList[i].bind("<B1-Motion>",lambda e,i=i:mouse_motion(e, labelList[i]))

canvas.configure(scrollregion=canvas.bbox('all'), yscrollcommand=scrolly.set)

canvas.pack(fill='both', expand=True, side='left')
scrolly.pack(fill='y', side='right')


# function created for exiting
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()
