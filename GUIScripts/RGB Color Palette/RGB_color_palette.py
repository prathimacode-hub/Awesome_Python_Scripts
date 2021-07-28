
# RGB Color Palette

# imported necessary library
import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
from tkinter import ttk
from PIL import ImageTk, Image
import colorsys


# Main Window & Configuration
window = tk.Tk()  # created a tkinter gui window frame
window.title("RGB Color Palette")
window.geometry('1000x700')

# top label
start1 = tk.Label(text="RGB COLOR PALETTE", font=("Arial", 50, "underline"), fg="magenta")  # same way bg
start1.place(x=120, y=10)

def start_fun():
    window.destroy()

# start button created
startb = Button(window, text="START", command=start_fun, font=("Arial", 25), bg="lightgreen", fg="blue", borderwidth=3,
                relief="raised")
startb.place(x=130, y=580)

# image on the main window
path = "Images/front.png"
# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img1 = ImageTk.PhotoImage(Image.open(path))
# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image=img1)
panel.place(x=210, y=100)


# function created for exiting
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()


# exit button created
exitb = Button(window, text="EXIT", command=exit_win, font=("Arial", 25), bg="red", fg="blue", borderwidth=3,
               relief="raised")
exitb.place(x=730, y=580)
window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()

# Main Window & Configuration
window1 = tk.Tk() # created a tkinter gui window frame
window1.title("RGB Color Palette")
window1.geometry('1000x730')


# top label
start1 = tk.Label(text = "RGB COLOR PALETTE", font=("Arial", 40, "underline"), fg="magenta") # same way bg
start1.place(x =210, y = 10)

# lbl1 = tk.Label(text="Select any video &\nconvert to grayscale video", font=("Arial", 40),fg="green")  # same way bg
# lbl1.place(x=170, y=110)

# for preview
preview_text = tk.Text(window1, height=9, width=60, font=("Arial", 15), bg="white", borderwidth=3, relief="solid")
preview_text.place(x=160, y=90)

# preview1 label
top1 = Label(window1, text="PREVIEW AREA", font=("Arial", 40), fg="black", bg="white")  # same way bg
top1.place(x=270, y=130)

# preview2 label
top2 = Label(window1, text="Color will be previewed here...", font=("Arial", 25), fg="black",bg="white")  # same way bg
top2.place(x=265, y=230)

Label(window1, text="RED", font=("Arial", 40), fg="red").place(x=130, y=335)
Label(window1, text="GREEN", font=("Arial", 40), fg="green").place(x=130, y=415)
Label(window1, text="BLUE", font=("Arial", 40), fg="blue").place(x=130, y=500)

# created a scale from 1 to 10
red_scale = Scale(window1, from_=1, to=255, orient=HORIZONTAL,width = 20, length = 500, font=("Arial", 20), bg = "red", fg = "black", borderwidth=3)
red_scale.place(x = 340, y = 330)

# created a scale from 1 to 10
green_scale = Scale(window1, from_=1, to=255, orient=HORIZONTAL,width = 20, length = 500,font=("Arial", 20), bg = "green", fg = "black", borderwidth=3)
green_scale.place(x = 340, y = 410)

# created a scale from 1 to 10
blue_scale = Scale(window1, from_=1, to=255, orient=HORIZONTAL,width = 20, length = 500,font=("Arial", 20), bg = "blue", fg = "black", borderwidth=3)
blue_scale.place(x = 340, y = 490)

Label(window1, text="Degree", font=("Arial", 35), fg="gray").place(x=70, y=580)
Label(window1, text="Saturation", font=("Arial", 35), fg="gray").place(x=370, y=580)
Label(window1, text="Lightness", font=("Arial", 35), fg="gray").place(x=730, y=580)

d_lbl = Label(window1, font=("Arial", 35), fg="gray")
d_lbl.place(x=70, y=640)
s_lbl = Label(window1, font=("Arial", 35), fg="gray")
s_lbl.place(x=370, y=640)
l_lbl = Label(window1, font=("Arial", 35), fg="gray")
l_lbl.place(x=730, y=640)

def update_color():
    red = int(red_scale.get())
    green = int(green_scale.get())
    blue = int(blue_scale.get())
    x = '#%02x%02x%02x' % (red, green, blue)
    preview_text.configure(bg = x)
    # print(x)
    if(x=="#010101"):
        top1.configure(bg = x, fg = "white")
        top2.configure(bg = x, fg = "white")
    else:
        top1.configure(bg=x, fg = "black")
        top2.configure(bg=x, fg = "black")

    r, g, b = [x1 / 255.0 for x1 in (red, green, blue)]
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    h = round(h,4)
    s = round(s, 4)
    l = round(l, 4)
    d_lbl.config(text = h)
    s_lbl.config(text=s)
    l_lbl.config(text=l)
    # print(red_scale.get(), green_scale.get(), blue_scale.get())
    window1.after(1, update_color)

update_color()

# function for exiting
def exit_win1():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window1.destroy()

# # Get Images Button
# getb=Button(window1, text="EXIT",command=exit_win1,  font=("Arial", 25), bg = "red", fg = "blue")
# getb.place(x = 750, y = 580)

window1.protocol("WM_DELETE_WINDOW", exit_win1)
window1.mainloop()
