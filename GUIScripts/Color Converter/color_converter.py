
# Color Converter

# importing necessary library
from tkinter import *  # from tkinter we import everything
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.messagebox as mbox
import colorsys

# Main Window
frame = Tk()
frame.title('Color Converter')
frame.geometry('1000x700')

# function for converting from rgb to hex
def def_rgb_to_hex():
    def convert_fun():
        input_rgb = f_entry.get()
        list = (input_rgb.rstrip().split(' '))
        red = int(list[0])
        green = int(list[1])
        blue = int(list[2])
        x = '#%02x%02x%02x' % (red, green, blue)
        preview_text.configure(bg = str(x))
        top1.configure(bg = str(x))
        top2.configure(bg = str(x))

        s_entry.delete(0,END)
        s_entry.insert(0,x)
        """Return color as #rrggbb for the given color values."""
        # return str('#%02x%02x%02x' % (red, green, blue))

    # created frame1 window
    frame1 = Tk()
    frame1.title('RGB to HEX')
    frame1.geometry('1000x700')

    # top label
    start1 = tk.Label(frame1,text="RGB to HEX", font=("Arial", 50), fg="magenta")  # same way bg
    start1.place(x=290, y=10)

    # for preview
    preview_text = tk.Text(frame1, height=15, width=60, font=("Arial", 15), bg="white", borderwidth=3, relief="solid")
    preview_text.place(x=150, y=100)

    # preview1 label
    top1 = Label(frame1, text="PREVIEW AREA", font=("Arial", 40), fg="black", bg="white")  # same way bg
    top1.place(x=270, y=180)

    # preview2 label
    top2 = Label(frame1, text="Color will be previewed here...", font=("Arial", 25), fg="black",bg="white")  # same way bg
    top2.place(x=265, y=280)

    # label for color name ---------------------------------------------------------------------------------
    f_label = tk.Label(frame1,text="RGB Code", font=("Arial", 35), fg="brown")  # same way bg
    f_label.place(x=180, y=470)

    f_entry = Entry(frame1, font=("Arial", 30), width = 10, border=2, bg = "light yellow",fg = "brown")
    f_entry.place(x=180, y=530)

    # label for color name ---------------------------------------------------------------------------------
    s_label = tk.Label(frame1, text="HEX Code", font=("Arial", 35), fg="brown")  # same way bg
    s_label.place(x=550, y=470)

    s_entry = Entry(frame1, font=("Arial", 30), width=10, border=2, bg="light yellow", fg="brown")
    s_entry.place(x=550, y=530)

    # created a button for hex to rgb conversion
    convertb = Button(frame1, text='CONVERT', command=convert_fun, font=("Arial", 25), bg="light green", fg="blue",borderwidth=3, relief="raised")
    convertb.place(x=380, y=600)

# function for converting from hex to rgb
def def_hex_to_rgb():
    def convert_fun():
        """Return (red, green, blue) for the color given as #rrggbb."""
        input_hex = f_entry.get()
        input_hex1 = input_hex
        input_hex = input_hex.lstrip('#')
        lv = len(input_hex)
        s_entry.delete(0,END)
        x = tuple(int(input_hex[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
        s_entry.insert(0,x)
        preview_text.configure(bg=str(input_hex1))
        top1.configure(bg=str(input_hex1))
        top2.configure(bg=str(input_hex1))
        # return tuple(int(input_hex[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

    # created frame1 window
    frame1 = Tk()
    frame1.title('HEX to RGB')
    frame1.geometry('1000x700')

    # top label
    start1 = tk.Label(frame1, text="HEX to RGB", font=("Arial", 50), fg="magenta")  # same way bg
    start1.place(x=290, y=10)

    # for preview
    preview_text = tk.Text(frame1, height=15, width=60, font=("Arial", 15), bg="white", borderwidth=3, relief="solid")
    preview_text.place(x=150, y=100)

    # preview1 label
    top1 = Label(frame1, text="PREVIEW AREA", font=("Arial", 40), fg="black", bg="white")  # same way bg
    top1.place(x=270, y=180)

    # preview2 label
    top2 = Label(frame1, text="Color will be previewed here...", font=("Arial", 25), fg="black",
                 bg="white")  # same way bg
    top2.place(x=265, y=280)

    # label for color name ---------------------------------------------------------------------------------
    f_label = tk.Label(frame1, text="HEX Code", font=("Arial", 35), fg="brown")  # same way bg
    f_label.place(x=180, y=470)

    f_entry = Entry(frame1, font=("Arial", 30), width=10, border=2, bg="light yellow", fg="brown")
    f_entry.place(x=180, y=530)

    # label for color name ---------------------------------------------------------------------------------
    s_label = tk.Label(frame1, text="RGB Code", font=("Arial", 35), fg="brown")  # same way bg
    s_label.place(x=550, y=470)

    s_entry = Entry(frame1, font=("Arial", 30), width=10, border=2, bg="light yellow", fg="brown")
    s_entry.place(x=550, y=530)

    # created a button for hex to rgb conversion
    convertb = Button(frame1, text='CONVERT', command=convert_fun, font=("Arial", 25), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
    convertb.place(x=380, y=600)

# function for converting from rgb to hsv
def def_rgb_to_hsv():
    def convert_fun():
        input_rgb1 = f_entry.get()
        list1 = (input_rgb1.rstrip().split(' '))
        red = int(list1[0])
        green = int(list1[1])
        blue = int(list1[2])
        x1 = '#%02x%02x%02x' % (red, green, blue)

        input_rgb = f_entry.get()
        list = (input_rgb.rstrip().split(' '))
        r = int(list[0])
        g = int(list[1])
        b = int(list[2])

        # R, G, B values are divided by 255
        # to change the range from 0..255 to 0..1:
        r, g, b = r / 255.0, g / 255.0, b / 255.0

        # h, s, v = hue, saturation, value
        cmax = max(r, g, b)  # maximum of r, g, b
        cmin = min(r, g, b)  # minimum of r, g, b
        diff = cmax - cmin  # diff of cmax and cmin.

        # if cmax and cmax are equal then h = 0
        if cmax == cmin:
            h = 0

        # if cmax equal r then compute h
        elif cmax == r:
            h = (60 * ((g - b) / diff) + 360) % 360

        # if cmax equal g then compute h
        elif cmax == g:
            h = (60 * ((b - r) / diff) + 120) % 360

        # if cmax equal b then compute h
        elif cmax == b:
            h = (60 * ((r - g) / diff) + 240) % 360

        # if cmax equal zero
        if cmax == 0:
            s = 0
        else:
            s = (diff / cmax) * 100

        # compute v
        v = cmax * 100
        x = str(h) + " " + str(s) + " " + str(v)
        s_entry.delete(0,END)
        s_entry.insert(0,x)

        preview_text.configure(bg=str(x1))
        top1.configure(bg=str(x1))
        top2.configure(bg=str(x1))
        # return h, s, v

    # created frame1 window
    frame1 = Tk()
    frame1.title('RGB to HSV')
    frame1.geometry('1000x700')

    # top label
    start1 = tk.Label(frame1, text="RGB to HSV", font=("Arial", 50), fg="magenta")  # same way bg
    start1.place(x=290, y=10)

    # for preview
    preview_text = tk.Text(frame1, height=15, width=60, font=("Arial", 15), bg="white", borderwidth=3, relief="solid")
    preview_text.place(x=150, y=100)

    # preview1 label
    top1 = Label(frame1, text="PREVIEW AREA", font=("Arial", 40), fg="black", bg="white")  # same way bg
    top1.place(x=270, y=180)

    # preview2 label
    top2 = Label(frame1, text="Color will be previewed here...", font=("Arial", 25), fg="black",
                 bg="white")  # same way bg
    top2.place(x=265, y=280)

    # label for color name ---------------------------------------------------------------------------------
    f_label = tk.Label(frame1, text="RGB Code", font=("Arial", 35), fg="brown")  # same way bg
    f_label.place(x=180, y=470)

    f_entry = Entry(frame1, font=("Arial", 30), width=10, border=2, bg="light yellow", fg="brown")
    f_entry.place(x=180, y=530)

    # label for color name ---------------------------------------------------------------------------------
    s_label = tk.Label(frame1, text="HSV Code", font=("Arial", 35), fg="brown")  # same way bg
    s_label.place(x=550, y=470)

    s_entry = Entry(frame1, font=("Arial", 30), width=10, border=2, bg="light yellow", fg="brown")
    s_entry.place(x=550, y=530)

    # created a button for hex to rgb conversion
    convertb = Button(frame1, text='CONVERT', command=convert_fun, font=("Arial", 25), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
    convertb.place(x=380, y=600)

# function for converting from hsv to rgb
def def_hsv_to_rgb():
    def convert_fun():
        input_rgb = f_entry.get()
        list = (input_rgb.rstrip().split(' '))
        h = float(list[0])/100
        s = float(list[1])/100
        v = float(list[2])/100

        x = tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))

        s_entry.delete(0, END)
        s_entry.insert(0, x)

        red = int(x[0])
        green = int(x[1])
        blue = int(x[2])
        x1 = '#%02x%02x%02x' % (red, green, blue)
        preview_text.configure(bg=str(x1))
        top1.configure(bg=str(x1))
        top2.configure(bg=str(x1))


    # created frame1 window
    frame1 = Tk()
    frame1.title('HSV to RGB')
    frame1.geometry('1000x700')

    # top label
    start1 = tk.Label(frame1, text="HSV to RGB", font=("Arial", 50), fg="magenta")  # same way bg
    start1.place(x=290, y=10)

    # for preview
    preview_text = tk.Text(frame1, height=15, width=60, font=("Arial", 15), bg="white", borderwidth=3, relief="solid")
    preview_text.place(x=150, y=100)

    # preview1 label
    top1 = Label(frame1, text="PREVIEW AREA", font=("Arial", 40), fg="black", bg="white")  # same way bg
    top1.place(x=270, y=180)

    # preview2 label
    top2 = Label(frame1, text="Color will be previewed here...", font=("Arial", 25), fg="black",
                 bg="white")  # same way bg
    top2.place(x=265, y=280)

    # label for color name ---------------------------------------------------------------------------------
    f_label = tk.Label(frame1, text="HSV Code", font=("Arial", 35), fg="brown")  # same way bg
    f_label.place(x=180, y=470)

    f_entry = Entry(frame1, font=("Arial", 30), width=10, border=2, bg="light yellow", fg="brown")
    f_entry.place(x=180, y=530)

    # label for color name ---------------------------------------------------------------------------------
    s_label = tk.Label(frame1, text="RGB Code", font=("Arial", 35), fg="brown")  # same way bg
    s_label.place(x=550, y=470)

    s_entry = Entry(frame1, font=("Arial", 30), width=10, border=2, bg="light yellow", fg="brown")
    s_entry.place(x=550, y=530)

    # created a button for hex to rgb conversion
    convertb = Button(frame1, text='CONVERT', command=convert_fun, font=("Arial", 25), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
    convertb.place(x=380, y=600)

# function to convert from rgb to lab
def def_rgb_to_lab():
    # function for convert button
    def convert_fun():
        input_rgb = f_entry.get()
        list = (input_rgb.rstrip().split(' '))

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
        XYZ = [0, 0, 0,]
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
        Lab = [0,0, 0]
        # found L, A, and B
        L = (116 * XYZ[1]) - 16
        a = 500 * (XYZ[0] - XYZ[1])
        b = 200 * (XYZ[1] - XYZ[2])
        # rounded off to 4 decimal digit
        Lab[0] = round(L,4)
        Lab[1] = round(a,4)
        Lab[2] = round(b,4)
        x = str(Lab[0]) + " " + str(Lab[1]) + " " + str(Lab[2])

        s_entry.delete(0, END)
        s_entry.insert(0, x)

        red = int(list[0])
        green = int(list[1])
        blue = int(list[2])
        x1 = '#%02x%02x%02x' % (red, green, blue)

        # previewed
        preview_text.configure(bg=str(x1))
        top1.configure(bg=str(x1))
        top2.configure(bg=str(x1))
        # mbox.showinfo("Brightness", "Brightness Level  :  " + str(Lab[0]))


    # created frame1 window
    frame1 = Tk()
    frame1.title('RGB to LAB')
    frame1.geometry('1000x700')

    # top label
    start1 = tk.Label(frame1, text="RGB to LAB", font=("Arial", 50), fg="magenta")  # same way bg
    start1.place(x=290, y=10)

    # for preview
    preview_text = tk.Text(frame1, height=15, width=60, font=("Arial", 15), bg="white", borderwidth=3, relief="solid")
    preview_text.place(x=150, y=100)

    # preview1 label
    top1 = Label(frame1, text="PREVIEW AREA", font=("Arial", 40), fg="black", bg="white")  # same way bg
    top1.place(x=270, y=180)

    # preview2 label
    top2 = Label(frame1, text="Color will be previewed here...", font=("Arial", 25), fg="black",bg="white")  # same way bg
    top2.place(x=265, y=280)

    # label for color name ---------------------------------------------------------------------------------
    f_label = tk.Label(frame1, text="RGB Code", font=("Arial", 35), fg="brown")  # same way bg
    f_label.place(x=180, y=470)

    f_entry = Entry(frame1, font=("Arial", 30), width=10, border=2, bg="light yellow", fg="brown")
    f_entry.place(x=180, y=530)

    # label for color name ---------------------------------------------------------------------------------
    s_label = tk.Label(frame1, text="LAB Code", font=("Arial", 35), fg="brown")  # same way bg
    s_label.place(x=550, y=470)

    s_entry = Entry(frame1, font=("Arial", 30), width=15, border=2, bg="light yellow", fg="brown")
    s_entry.place(x=500, y=530)

    # created a button for hex to rgb conversion
    convertb = Button(frame1, text='CONVERT', command=convert_fun, font=("Arial", 25), bg="light green", fg="blue",borderwidth=3, relief="raised")
    convertb.place(x=380, y=600)


# image on the main window
path = "Images/color.png"
# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img1 = ImageTk.PhotoImage(Image.open(path))
# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(frame, image = img1)
panel.place(x = 350, y = 250)

# starting label
start1 = Label(frame, text='COLOR CONVERTER', font=("Arial", 50),fg="magenta")
start1.place(x=150,y=10)

# label defined that will be beside the choose conversion
select_lbl = Label(frame, text='Select Conversion', font=("Arial", 40),fg="green")
select_lbl.place(x=265,y=100)

# created a button for rgb to hex conversion
rgbtohexb = Button(frame, text='RGB to HEX', command=def_rgb_to_hex, font=("Arial", 25), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
rgbtohexb.place(x=100, y=200)

# created a button for hex to rgb conversion
hextorgbb = Button(frame, text='HEX to RGB', command=def_hex_to_rgb, font=("Arial", 25), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
hextorgbb.place(x=670, y=200)

# created a button for rgb to lab conversion
rgbtolabb = Button(frame, text='RGB to LAB', command=def_rgb_to_lab, font=("Arial", 25), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
rgbtolabb.place(x=380, y=350)

# created a button for rgb to hsv conversion
rgbtohsvb = Button(frame, text='RGB to HSV', command=def_rgb_to_hsv, font=("Arial", 25), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
rgbtohsvb.place(x=100, y=500)

# created a button for hsv to rgb conversion
hsvtorgbb = Button(frame, text='HSV to RGB', command=def_hsv_to_rgb, font=("Arial", 25), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
hsvtorgbb.place(x=670, y=500)

# defined exit_win function, to show a exit dialog box when tried to exit
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        frame.destroy()

# creating an exit button
prevB = Button(frame, text='EXIT', command=exit_win, font=("Arial", 25), bg = "red", fg = "blue", borderwidth=3, relief="raised")
prevB.place(x = 440, y = 600)

# this is done to show the exit dialog box when tried to exit from the main window, using the top-roght close button of titlebar
frame.protocol("WM_DELETE_WINDOW", exit_win)
frame.mainloop()