
# Piano Application

# Imported necessary library
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from playsound import playsound
import tkinter.messagebox as mbox


# created the main window
root = tk.Tk()
root.geometry('1000x750')
root.title("Piano Application")

# for adding image in main window
icon = ImageTk.PhotoImage(Image.open('Images/piano.jpg'))
icon_label = Label(root,image=icon)
icon_label.place(x=150,y=100)

# for adding top label
start1 = tk.Label(text = "PIANO PLAYER", font=("Arial", 50), fg="magenta",underline=0) # same way bg
start1.place(x = 250, y = 10)

# to store the pattern played
s = ""

# to see the pattern played
def see_pattern():
        mbox.showinfo("Pattern Played", "Pattern Played :\n\n" + s)

# created see pattern  button
patb = Button(root, text="SEE PATTERN",command=see_pattern,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
patb.place(x =370 , y =670 )

# created frame or piano
frame1 = Frame(root,width=1000,height=200,bg="white")
frame1.place(x=90,y=420)

# created class piano for creating piano button and also embedding sound to it
class piano():
        # function defined to play the sound
        def PianoSound(self,sound):
                global s
                playsound(f'Sounds/Piano{sound}.mp3')
                s = s + str(sound)
                s = s + " , "

        # with the help of this 23 piano button were created
        def __init__(self,index):
                self.index = index

                if self.index%2 != 0:
                        Button(frame1,padx=10,pady=100,bg="black",fg="white",relief=RAISED,borderwidth=5,command=lambda:self.PianoSound(self.index),cursor="hand2").grid(row=20,column=self.index)
                else:
                        Button(frame1,padx=10,pady=100,bg="white",fg="black",relief=RAISED,borderwidth=5,command=lambda:self.PianoSound(self.index),cursor="hand2").grid(row=20,column=self.index)

# this is main function
if __name__ == '__main__':
        for i in range(1,24):
                piano(i)

# function for exiting
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", exit_win)
root.mainloop()




