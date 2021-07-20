
# Mouse Speed Tracker

# Imported necessary library
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
import sys
import math
import time
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QApplication


# created main window
window = Tk()
window.title("Mouse Speed Tracker")
window.geometry("1000x700")


# class frame1 created
class Frame1:
    def __init__(self, position, time):
        self.position = position
        self.time = time

    # function to find speed
    def speed(self, frame):
        d = distance(*self.position, *frame.position)
        time_delta = abs(frame.time - self.time)
        if time_delta == 0:
            return None
        else:
            return d / time_delta

# function to find distance
def distance(x1, y1, x2, y2):
    Label(window1, text= ":  ( " + str(x1) + ' , ' + str(y1) + ' )', font=("Arial", 35), fg="green").place(x=480, y=200)
    Label(window1, text= ":  ( " + str(x2) + ' , ' + str(y2) + ' )', font=("Arial", 35), fg="green").place(x=480, y=300)
    # print("he",x1,y1,x2,y2)
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# function to get cursor position
def get_current_cursor_position():
    pos = QCursor.pos()
    return pos.x(), pos.y()

# function to get current frame
def get_current_frame():
    return Frame1(get_current_cursor_position(), time.time())


# for top label
top1 = Label(window, text="Mouse Speed Tracker", font=("Arial", 55,'underline'), fg="magenta")
top1.place(x = 120, y = 10)

# start label
s1 = Label(window, text="Starting Point", font=("Arial", 35), fg="blue")
s1.place(x = 80, y = 150)

# end label
e1 = Label(window, text="Ending Point", font=("Arial", 35), fg="blue")
e1.place(x = 80, y = 230)

# speed label
sp1 = Label(window, text="Speed (pixels/sec)", font=("Arial", 35), fg="blue")
sp1.place(x = 80, y = 310)

# info label
d1 = Label(window, text="Move the mouse on the screen and it will display\nthe instant co-ordinates of starting point, ending point\nand speed at each instance", font=("Arial", 30), fg="green")
d1.place(x = 30, y = 420)

# function for start button
def start_fun():
    window.destroy()

# start button created
startb = Button(window, text="START",command=start_fun,font=("Arial", 25), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
startb.place(x =410 , y =600 )

# main function created
if __name__ == '__main__':
    # function to ec
    def exit_win():
        if mbox.askokcancel("Exit", "Do you want to exit?"):
            window.destroy()

    window.protocol("WM_DELETE_WINDOW", exit_win)
    window.mainloop()

    app = QApplication(sys.argv)

    last_frame = get_current_frame()

    x = 1
    while (x==1):
        # created main window
        window1 = Tk()
        window1.title("Mouse Speed Tracker")
        window1.geometry("1000x700")

        top1 = Label(window1, text="Mouse Speed Tracker", font=("Arial", 55, 'underline'), fg="magenta")
        top1.place(x=120, y=10)

        s1 = Label(window1, text="Starting Point", font=("Arial", 35), fg="blue")
        s1.place(x=70, y=200)

        e1 = Label(window1, text="Ending Point", font=("Arial", 35), fg="blue")
        e1.place(x=70, y=300)

        sp1 = Label(window1, text="Speed (pixels/sec)", font=("Arial", 35), fg="blue")
        sp1.place(x=70, y=400)

        def stop_fun():
            global x
            if mbox.askokcancel("Exit", "Do you want to exit?"):
                window1.destroy()
            x=0
            return

        # stop button created
        stopb = Button(window1, text="STOP", command=stop_fun, font=("Arial", 25), bg="orange", fg="blue",borderwidth=3, relief="raised")
        stopb.place(x=410, y=550)

        new_frame = get_current_frame()
        # print(new_frame.speed(last_frame))
        Label(window1, text= ":  " + str(new_frame.speed(last_frame)), font=("Arial", 35), fg="green").place(x=480, y=400)
        last_frame = new_frame

        time.sleep(0.5)
        window1.mainloop()