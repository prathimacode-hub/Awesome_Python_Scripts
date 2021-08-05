# Preview Large Image

# imported necessary library
import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
from tkinter import ttk
from tkinter import filedialog
import cv2
import numpy as np


# class defined to preview image using scroll button
class ScrollableImage(tkinter.Frame):
    def __init__(self, master=None, **kw):
        self.image = kw.pop('image', None)
        sw = kw.pop('scrollbarwidth', 10)
        super(ScrollableImage, self).__init__(master=master, **kw)
        self.cnvs = tkinter.Canvas(self, highlightthickness=0, **kw)
        self.cnvs.create_image(0, 0, anchor='nw', image=self.image)
        # Vertical and Horizontal scrollbars
        self.v_scroll = tkinter.Scrollbar(self, orient='vertical', width=20)
        self.h_scroll = tkinter.Scrollbar(self, orient='horizontal', width=20)
        # Grid and configure weight.
        self.cnvs.grid(row=0, column=0, sticky='nsew')
        self.h_scroll.grid(row=1, column=0, sticky='ew')
        self.v_scroll.grid(row=0, column=1, sticky='ns')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        # Set the scrollbars to the canvas
        self.cnvs.config(xscrollcommand=self.h_scroll.set, yscrollcommand=self.v_scroll.set)
        # Set canvas view to the scrollbars
        self.v_scroll.config(command=self.cnvs.yview)
        self.h_scroll.config(command=self.cnvs.xview)
        # Assign the region to be scrolled
        self.cnvs.config(scrollregion=self.cnvs.bbox('all'))
        self.cnvs.bind_class(self.cnvs, "<MouseWheel>", self.mouse_scroll)

    def mouse_scroll(self, evt):
        if evt.state == 0:
            self.cnvs.yview_scroll(-1 * (evt.delta), 'units')  # For MacOS
            self.cnvs.yview_scroll(int(-1 * (evt.delta / 120)), 'units')  # For windows
        if evt.state == 1:
            self.cnvs.xview_scroll(-1 * (evt.delta), 'units')  # For MacOS
            self.cnvs.xview_scroll(int(-1 * (evt.delta / 120)), 'units')  # For windows


def open_file():
    global filename
    filename = filedialog.askopenfilename(title="Select file")
    # print(filename)
    path_text.delete("1.0", "end")
    path_text.insert(END, filename)

    img1 = cv2.imread(filename)
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    height, width, channels = img1.shape

    win1.configure(text="( " + str(screen_width) + " x " + str(screen_height) + " )")
    win2.configure(text="( " + str(width) + " x " + str(height) + " )")


# Main Window & Configuration
window = tk.Tk()  # created a tkinter gui window frame
window.title("Preview Large Image")
window.geometry('1000x700')

# top label
start1 = tk.Label(text="PREVIEW LARGE IMAGE", font=("Arial", 50, "underline"), fg="magenta")  # same way bg
start1.place(x=100, y=10)

# top label
start1 = tk.Label(text="Select any large image and\npreview here", font=("Arial", 40), fg="green")  # same way bg
start1.place(x=170, y=110)

# top label
start1 = tk.Label(text="Selected Image", font=("Arial", 35), fg="brown")  # same way bg
start1.place(x=80, y=250)

path_text = tk.Text(window, height=1, width=37, font=("Arial", 30), bg="light yellow", fg="orange", borderwidth=2,
                    relief="solid")
path_text.place(x=80, y=310)

# top label
win = tk.Label(text="Screen Size  :  ", font=("Arial", 35), fg="gray")  # same way bg
win.place(x=80, y=400)

# top label
win = tk.Label(text="Image Size  :  ", font=("Arial", 35), fg="gray")  # same way bg
win.place(x=80, y=480)

# top label
win1 = tk.Label(font=("Arial", 35), fg="gray")  # same way bg
win1.place(x=420, y=400)

# top label
win2 = tk.Label(font=("Arial", 35), fg="gray")  # same way bg
win2.place(x=420, y=480)


def preview_fun():
    global filename

    window.destroy()
    window1 = tk.Tk()  # created a tkinter gui window frame
    window1.title("Larger Image Preview by scrolling in X and Y axis")
    #     window1.geometry('1000x700')

    img = tk.PhotoImage(file=filename)
    image_window = ScrollableImage(window1, image=img, scrollbarwidth=6, width=700, height=500)
    image_window.pack()

    window1.mainloop()


# start button created
startb = Button(window, text="SELECT", command=open_file, font=("Arial", 25), bg="light green", fg="blue",
                borderwidth=3, relief="raised")
startb.place(x=100, y=600)

# start button created
startb = Button(window, text="PREVIEW", command=preview_fun, font=("Arial", 25), bg="orange", fg="blue", borderwidth=3,
                relief="raised")
startb.place(x=420, y=600)


# function created for exiting
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()


# exit button created
exitb = Button(window, text="EXIT", command=exit_win, font=("Arial", 25), bg="red", fg="blue", borderwidth=3,
               relief="raised")
exitb.place(x=780, y=600)
window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()
