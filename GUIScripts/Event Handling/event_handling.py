# importing tkinter
from tkinter import *
# initializing root
root = Tk()
# width and height variables
can_width = 300
can_height = 200
# setting geometry of gui
root.geometry(f"{can_width}x{can_height}")
# setting title of gui
root.title("Event handling")
# creating a label
Label(root, text="Click anywhere").pack()
# initializing variable
i = 0
# defining a function
def me(event):
    global i
    Label(root, text=f"You clicked me {i} time").pack()
    Label(root, text="Double click to exit screen").pack()
    i=i+1
# binding mouse left button to root and calling me function
root.bind("<Button-1>", me)
# binding double click mouse left button to root and calling
# in-built quit function
root.bind("<Double-1>", quit)
# calling mainloop
root.mainloop()
