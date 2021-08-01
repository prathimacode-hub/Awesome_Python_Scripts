
# Color Difference

# imported necessary library
import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
from tkinter import ttk
from PIL import ImageTk, Image
import colorsys
import cv2
from colormath.color_objects import LabColor
from colormath.color_diff import delta_e_cie1976
from colormath.color_diff import delta_e_cie1994
from colormath.color_diff import delta_e_cie2000
from colormath.color_diff import delta_e_cmc


# Main Window & Configuration
window = tk.Tk()  # created a tkinter gui window frame
window.title("Color Difference")
window.geometry('1000x700')

# top label
start1 = tk.Label(text="COLOR DIFFERENCE", font=("Arial", 50, "underline"), fg="magenta")  # same way bg
start1.place(x=150, y=10)

def start_fun():
    window.destroy()

# start button created
startb = Button(window, text="START", command=start_fun, font=("Arial", 25), bg="lightgreen", fg="blue", borderwidth=3,
                relief="raised")
startb.place(x=140, y=600)

# image on the main window
path = "Images/front.jpg"
# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img1 = ImageTk.PhotoImage(Image.open(path))
# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image=img1)
panel.place(x=180, y=100)


# function created for exiting
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()


# exit button created
exitb = Button(window, text="EXIT", command=exit_win, font=("Arial", 25), bg="red", fg="blue", borderwidth=3,relief="raised")
exitb.place(x=750, y=600)
window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()

# Main Window & Configuration
window1 = tk.Tk() # created a tkinter gui window frame
window1.title("Color Difference")
window1.geometry('1000x710')


# top label
start1 = tk.Label(text = "COLOR DIFFERENCE", font=("Arial", 40, "underline"), fg="magenta") # same way bg
start1.place(x =220, y = 10)

# lbl1 = tk.Label(text="Select any video &\nconvert to grayscale video", font=("Arial", 40),fg="green")  # same way bg
# lbl1.place(x=170, y=110)

# for color 1 preview
preview_text1 = tk.Text(window1, height=10, width=25, font=("Arial", 15), bg="white", borderwidth=3, relief="solid")
preview_text1.place(x=80, y=90)

# for color 2 preview
preview_text2 = tk.Text(window1, height=10, width=25, font=("Arial", 15), bg="white", borderwidth=3, relief="solid")
preview_text2.place(x=80, y=340)

# preview1 label
top1 = Label(window1, text="COLOR 1", font=("Arial", 40), fg="black", bg="white")  # same way bg
top1.place(x=100, y=170)

# preview1 label
top2 = Label(window1, text="COLOR 2", font=("Arial", 40), fg="black", bg="white")  # same way bg
top2.place(x=100, y=415)

# ------------------------------color palette 1
# created a scale from 1 to 255
red_scale1 = Scale(window1, from_=1, to=255, orient=HORIZONTAL,width = 18, length = 500, font=("Arial", 20), bg = "red", fg = "black", borderwidth=3)
red_scale1.place(x = 390, y = 95)

# created a scale from 1 to 255
green_scale1 = Scale(window1, from_=1, to=255, orient=HORIZONTAL,width = 18, length = 500,font=("Arial", 20), bg = "green", fg = "black", borderwidth=3)
green_scale1.place(x = 390, y = 172)

# created a scale from 1 to 255
blue_scale1 = Scale(window1, from_=1, to=255, orient=HORIZONTAL,width = 18, length = 500,font=("Arial", 20), bg = "blue", fg = "black", borderwidth=3)
blue_scale1.place(x = 390, y = 249)

# ------------------------------color palette 2
# created a scale from 1 to 255
red_scale2 = Scale(window1, from_=1, to=255, orient=HORIZONTAL,width = 18, length = 500, font=("Arial", 20), bg = "red", fg = "black", borderwidth=3)
red_scale2.place(x = 390, y = 345)

# created a scale from 1 to 255
green_scale2 = Scale(window1, from_=1, to=255, orient=HORIZONTAL,width = 18, length = 500,font=("Arial", 20), bg = "green", fg = "black", borderwidth=3)
green_scale2.place(x = 390, y = 422)

# created a scale from 1 to 255
blue_scale2 = Scale(window1, from_=1, to=255, orient=HORIZONTAL,width = 18, length = 500,font=("Arial", 20), bg = "blue", fg = "black", borderwidth=3)
blue_scale2.place(x = 390, y = 499)

# function for updating the color1
def update_color1():
    red1 = int(red_scale1.get())
    green1 = int(green_scale1.get())
    blue1 = int(blue_scale1.get())
    x1 = '#%02x%02x%02x' % (red1, green1, blue1)
    preview_text1.configure(bg = x1)
    # print(x1)
    if(x1=="#010101"):
        top1.configure(bg = x1, fg = "white")
    else:
        top1.configure(bg=x1, fg = "black")
    window1.after(1, update_color1)

update_color1()

# function for updating the color2
def update_color2():
    red2 = int(red_scale2.get())
    green2 = int(green_scale2.get())
    blue2 = int(blue_scale2.get())
    x2 = '#%02x%02x%02x' % (red2, green2, blue2)
    preview_text2.configure(bg = x2)
    # print(x2)
    if(x2=="#010101"):
        top2.configure(bg = x2, fg = "white")
    else:
        top2.configure(bg=x2, fg = "black")
    window1.after(1, update_color2)

update_color2()

# function to convert from RGB to LAB
def rgb2lab(list):
    num = 0
    # created list RGB and initialized with 0
    RGB = [0, 0, 0]
    for value in list:
        value = float(value) / 255
        if value > 0.04045:
            value = ((value + 0.055) / 1.055) ** 2.4
        else:
            value = value / 12.92
        RGB[num] = value * 100
        num = num + 1
    XYZ = [0, 0, 0, ]
    # converted all the three R, G, B to X, Y, Z
    X = RGB[0] * 0.4124 + RGB[1] * 0.3576 + RGB[2] * 0.1805
    Y = RGB[0] * 0.2126 + RGB[1] * 0.7152 + RGB[2] * 0.0722
    Z = RGB[0] * 0.0193 + RGB[1] * 0.1192 + RGB[2] * 0.9505
    # rounded off the values upto 4 decimal digit
    XYZ[0] = round(X, 4)
    XYZ[1] = round(Y, 4)
    XYZ[2] = round(Z, 4)
    XYZ[0] = float(XYZ[0]) / 95.047  # ref_X =  95.047   Observer= 2°, Illuminant= D65
    XYZ[1] = float(XYZ[1]) / 100.0  # ref_Y = 100.000
    XYZ[2] = float(XYZ[2]) / 108.883  # ref_Z = 108.883
    num = 0
    for value in XYZ:
        if value > 0.008856:
            value = value ** (0.3333333333333333)
        else:
            value = (7.787 * value) + (16 / 116)
        XYZ[num] = value
        num = num + 1

    # formed Lab list and initialize with 0
    Lab = [0, 0, 0]
    # found L, A, and B
    L = (116 * XYZ[1]) - 16
    a = 500 * (XYZ[0] - XYZ[1])
    b = 200 * (XYZ[1] - XYZ[2])
    # rounded off to 4 decimal digit
    Lab[0] = round(L, 4)
    Lab[1] = round(a, 4)
    Lab[2] = round(b, 4)
    return Lab

# function to find the difference between two color
def diff_win():
    list1 = []
    list1.append(int(red_scale1.get()))
    list1.append(int(green_scale1.get()))
    list1.append(int(blue_scale1.get()))
    lab1 = rgb2lab(list1)

    list2 = []
    list2.append(int(red_scale2.get()))
    list2.append(int(green_scale2.get()))
    list2.append(int(blue_scale2.get()))
    lab2 = rgb2lab(list2)

    # color1
    color1 = LabColor(lab_l=list1[0], lab_a=list1[1], lab_b=list1[2])
    # color2
    color2 = LabColor(lab_l=list2[0], lab_a=list2[1], lab_b=list2[2])

    delta_e1 = delta_e_cie1976(color1, color2)
    # print(delta_e1)
    delta_e2 = delta_e_cie1994(color1, color2)
    # print(delta_e2)
    delta_e3 = delta_e_cie2000(color1, color2)
    # print(delta_e3)
    delta_e4 = delta_e_cmc(color1, color2)
    # print(delta_e4)
    mbox.showinfo("Color Difference", "Color Difference\n\n1.)  Delta E CIE1976  :  " + str(delta_e1) + "\n\n2.)  Delta E CIE1994  :  " + str(delta_e2) + "\n\n3.)  Delta E CIE2000  :  " + str(delta_e3) + "\n\n4.)  Delta E CMC  :  " + str(delta_e4))


# diff Button
diffb=Button(window1, text="DIFFERENCE",command=diff_win,  font=("Arial", 25), bg = "light green", fg = "blue")
diffb.place(x = 80, y = 610)

# function to show difference cheatsheet
def cheat_win():
    img = cv2.imread("Images/diff_cheatsheet.jpg", 1)
    cv2.imshow("Color Difference Cheatsheet", img)

# cheat Button
diffb=Button(window1, text="DIFF. CHEATSHEET",command=cheat_win,  font=("Arial", 25), bg = "orange", fg = "blue")
diffb.place(x = 385, y = 610)

# function for exiting
def exit_win1():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window1.destroy()

# exits Button
exitb=Button(window1, text="EXIT",command=exit_win1,  font=("Arial", 25), bg = "red", fg = "blue")
exitb.place(x = 800, y = 610)

window1.protocol("WM_DELETE_WINDOW", exit_win1)
window1.mainloop()
