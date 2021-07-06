
# Mouse Pointer Co-ordinates Getter

# Imported necessary library
from tkinter import *
import tkinter.messagebox as mbox
import pyautogui

window = Tk()
window.title("Mouse Pointer Co-ordinates Getter")
window.geometry("1200x700")

top1 = Label(window, text="GET MOUSE POINTER CO-ORDINATES", font=("Arial", 35,'underline'), fg="magenta")
top1.place(x = 50, y = 10)

top1 = Label(window, text="CO - ORDINATES", font=("Arial", 50), fg="blue")
top1.place(x = 220, y = 150)

top1 = Label(window, text="Move the mouse on the screen and it will display\nthe co-ordinates of mouse cursor on the screen", font=("Arial", 30), fg="green")
top1.place(x = 50, y = 500)

l1 = Label(window, fg='blue', font=("Arial", 50))
l1.place(x = 150, y = 300)

def update_label():
    coordinates = pyautogui.position()
    coordinates = "( X , Y )  :  ( " + str(coordinates[1]) + ' , ' + str(coordinates[0]) + ' )'
    l1.configure(text=coordinates)
    window.after(1, update_label)

update_label()


# function for exiting window
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()