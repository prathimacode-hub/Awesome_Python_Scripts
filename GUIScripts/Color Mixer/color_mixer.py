
# Color Mixer

# importing necessary library
from tkinter import *  # from tkinter we import everything
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.messagebox as mbox


# Main Window
frame = Tk()
frame.title('Color Mixer')
frame.geometry('1000x700')
# frame.configure(bg = "white")


# image on the main window
path = "Images/front.jpg"
# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img1 = ImageTk.PhotoImage(Image.open(path))
# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(frame, image = img1)
panel.place(x = 100, y = 150)

# starting label
start1 = Label(frame, text='COLOR  MIXER', font=("Arial", 55,"underline"),fg="magenta")
start1.place(x=220,y=10)

def start_fun():
    frame.destroy()

# creating an exit button
prevB = Button(frame, text='START', command=start_fun, font=("Arial", 25), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
prevB.place(x = 160, y = 570)

# defined exit_win function, to show a exit dialog box when tried to exit
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        frame.destroy()

# creating an exit button
prevB = Button(frame, text='EXIT', command=exit_win, font=("Arial", 25), bg = "red", fg = "blue", borderwidth=3, relief="raised")
prevB.place(x = 700, y = 570)

# this is done to show the exit dialog box when tried to exit from the main window, using the top-roght close button of titlebar
frame.protocol("WM_DELETE_WINDOW", exit_win)
frame.mainloop()

# Main Window
frame1 = Tk()
frame1.title('Color Mixer')
frame1.geometry('1000x700')

# image on the main window
path1 = "Images/second.png"
# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img2 = ImageTk.PhotoImage(Image.open(path1))
# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel1 = tk.Label(frame1, image = img2)
panel1.place(x = 50, y = 250)

# image on the main window
path2 = "Images/second.png"
# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img3 = ImageTk.PhotoImage(Image.open(path2))
# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel2 = tk.Label(frame1, image = img3)
panel2.place(x = 760, y = 250)

# starting label
start1 = Label(frame1, text='COLOR  MIXER', font=("Arial", 55,"underline"),fg="magenta")
start1.place(x=220,y=10)

# starting label
start1 = Label(frame1, text='Select any Options ', font=("Arial", 40),fg="green")
start1.place(x=260,y=110)

def mix_2():
    # mixing color with proportion -----------------------------
    def combine_hex_values(d):
        d_items = sorted(d.items())
        tot_weight = sum(d.values())
        red = int(sum([int(k[:2], 16) * v for k, v in d_items]) / tot_weight)
        green = int(sum([int(k[2:4], 16) * v for k, v in d_items]) / tot_weight)
        blue = int(sum([int(k[4:6], 16) * v for k, v in d_items]) / tot_weight)
        zpad = lambda x: x if len(x) == 2 else '0' + x
        return zpad(hex(red)[2:]) + zpad(hex(green)[2:]) + zpad(hex(blue)[2:])

    def mix_fun():
        color1 = str(c1_entry.get())
        p1 = int(p1_entry.get())
        color2 = str(c2_entry.get())
        p2 = int(p2_entry.get())
        c1 = color1[1:]
        c2 = color2[1:]
        # print(color1, c1, color2, c2)

        out = str(combine_hex_values({c1 : p1, c2 : p2}))
        out = "#" + out
        c1_preview.configure(bg = color1)
        c1_lbl.configure(bg = color1)
        c2_preview.configure(bg=color2)
        c2_lbl.configure(bg=color2)
        m_preview.configure(bg=out)
        m_lbl.configure(bg=out)
        # mbox.showinfo("Status", "Color Mixed Successfully.\n\nHex Code for the mixed color  :  #" + out)


    window1 = Tk()
    window1.title('Mix 2 Colors')
    window1.geometry('1000x700')

    # starting label
    start1 = Label(window1, text='MIX 2 COLORS', font=("Arial", 50, "underline"), fg="magenta")
    start1.place(x=260, y=10)

    # for preview
    c1_preview = tk.Text(window1, height=12, width=20, font=("Arial", 15), bg="white", borderwidth=3, relief="solid")
    c1_preview.place(x=50, y=150)
    # starting label
    c1_lbl = Label(window1, text='COLOR 1', font=("Arial", 25), fg="black", bg = "white")
    c1_lbl.place(x=90, y=270)
    # Day Entry Box
    c1_entry = Entry(window1, font=("Arial", 25), fg='orange', bg="light yellow", borderwidth=3, width=10)
    c1_entry.place(x=70, y=440)
    # Day Entry Box
    p1_entry = Entry(window1, font=("Arial", 25), fg='orange', bg="light yellow", borderwidth=3, width=10)
    p1_entry.place(x=70, y=495)

    # for preview
    m_preview = tk.Text(window1, height=18, width=26, font=("Arial", 15), bg="white", borderwidth=3, relief="solid")
    m_preview.place(x=350, y=100)
    # starting label
    m_lbl = Label(window1, text='MIXED', font=("Arial", 25), fg="black", bg="white")
    m_lbl.place(x=440, y=270)

    # for preview
    c2_preview = tk.Text(window1, height=12, width=20, font=("Arial", 15), bg="white", borderwidth=3, relief="solid")
    c2_preview.place(x=710, y=150)
    # starting label
    c2_lbl = Label(window1, text='COLOR 2', font=("Arial", 25), fg="black", bg="white")
    c2_lbl.place(x=750, y=270)
    # Day Entry Box
    c2_entry = Entry(window1, font=("Arial", 25), fg='orange', bg="light yellow", borderwidth=3, width=10)
    c2_entry.place(x=730, y=440)
    # Day Entry Box
    p2_entry = Entry(window1, font=("Arial", 25), fg='orange', bg="light yellow", borderwidth=3, width=10)
    p2_entry.place(x=730, y=495)

    # creating an exit button
    prevB = Button(window1, text='MIX', command=mix_fun, font=("Arial", 25), bg="orange", fg="blue",borderwidth=3, relief="raised")
    prevB.place(x=150, y=580)

    def clear_fun():
        c1_entry.delete(0,END)
        c2_entry.delete(0,END)
        p1_entry.delete(0,END)
        p2_entry.delete(0,END)
        c1_preview.configure(bg = "white")
        c2_preview.configure(bg="white")
        m_preview.configure(bg="white")
        c1_lbl.configure(bg="white")
        c2_lbl.configure(bg="white")
        m_lbl.configure(bg="white")

    # creating an exit button
    prevB = Button(window1, text='CLEAR', command=clear_fun, font=("Arial", 25), bg="orange", fg="blue", borderwidth=3,relief="raised")
    prevB.place(x=670, y=580)

def mix_3():
    # mixing color with proportion -----------------------------
    def combine_hex_values(d):
        d_items = sorted(d.items())
        tot_weight = sum(d.values())
        red = int(sum([int(k[:2], 16) * v for k, v in d_items]) / tot_weight)
        green = int(sum([int(k[2:4], 16) * v for k, v in d_items]) / tot_weight)
        blue = int(sum([int(k[4:6], 16) * v for k, v in d_items]) / tot_weight)
        zpad = lambda x: x if len(x) == 2 else '0' + x
        return zpad(hex(red)[2:]) + zpad(hex(green)[2:]) + zpad(hex(blue)[2:])

    def mix_fun():
        color1 = str(c1_entry.get())
        p1 = int(p1_entry.get())
        color2 = str(c2_entry.get())
        p2 = int(p2_entry.get())
        color3 = str(c3_entry.get())
        p3 = int(p3_entry.get())
        c1 = color1[1:]
        c2 = color2[1:]
        c3 = color3[1:]
        # print(color1, c1, color2, c2)

        out = str(combine_hex_values({c1: p1, c2: p2, c3 : p3}))
        out = "#" + out
        c1_preview.configure(bg=color1)
        c1_lbl.configure(bg=color1)
        c2_preview.configure(bg=color2)
        c2_lbl.configure(bg=color2)
        c3_preview.configure(bg=color3)
        c3_lbl.configure(bg=color3)
        m_preview.configure(bg=out)
        m_lbl.configure(bg=out)
        # mbox.showinfo("Status", "Color Mixed Successfully.\n\nHex Code for the mixed color  :  #" + out)

    window1 = Tk()
    window1.title('Mix 3 Colors')
    window1.geometry('1000x700')

    # starting label
    start1 = Label(window1, text='MIX 3 COLORS', font=("Arial", 50, "underline"), fg="magenta")
    start1.place(x=260, y=10)

    # for preview
    c1_preview = tk.Text(window1, height=5, width=20, font=("Arial", 15), bg="white", borderwidth=3, relief="solid")
    c1_preview.place(x=50, y=100)
    # starting label
    c1_lbl = Label(window1, text='COLOR 1', font=("Arial", 25), fg="black", bg="white")
    c1_lbl.place(x=90, y=140)
    # Day Entry Box
    c1_entry = Entry(window1, font=("Arial", 25), fg='orange', bg="light yellow", borderwidth=3, width=10)
    c1_entry.place(x=70, y=230)
    # Day Entry Box
    p1_entry = Entry(window1, font=("Arial", 25), fg='orange', bg="light yellow", borderwidth=3, width=10)
    p1_entry.place(x=70, y=285)

    # for preview
    c2_preview = tk.Text(window1, height=5, width=20, font=("Arial", 15), bg="white", borderwidth=3, relief="solid")
    c2_preview.place(x=710, y=100)
    # starting label
    c2_lbl = Label(window1, text='COLOR 2', font=("Arial", 25), fg="black", bg="white")
    c2_lbl.place(x=750, y=140)
    # Day Entry Box
    c2_entry = Entry(window1, font=("Arial", 25), fg='orange', bg="light yellow", borderwidth=3, width=10)
    c2_entry.place(x=730, y=230)
    # Day Entry Box
    p2_entry = Entry(window1, font=("Arial", 25), fg='orange', bg="light yellow", borderwidth=3, width=10)
    p2_entry.place(x=730, y=285)

    # for preview
    c3_preview = tk.Text(window1, height=5, width=20, font=("Arial", 15), bg="white", borderwidth=3, relief="solid")
    c3_preview.place(x=380, y=430)
    # starting label
    c3_lbl = Label(window1, text='COLOR 3', font=("Arial", 25), fg="black", bg="white")
    c3_lbl.place(x=420, y=470)
    # Day Entry Box
    c3_entry = Entry(window1, font=("Arial", 25), fg='orange', bg="light yellow", borderwidth=3, width=10)
    c3_entry.place(x=410, y=560)
    # Day Entry Box
    p3_entry = Entry(window1, font=("Arial", 25), fg='orange', bg="light yellow", borderwidth=3, width=10)
    p3_entry.place(x=410, y=615)

    # for preview
    m_preview = tk.Text(window1, height=10, width=26, font=("Arial", 15), bg="white", borderwidth=3, relief="solid")
    m_preview.place(x=350, y=170)
    # starting label
    m_lbl = Label(window1, text='MIXED', font=("Arial", 25), fg="black", bg="white")
    m_lbl.place(x=440, y=290)

    # creating an exit button
    prevB = Button(window1, text='MIX', command=mix_fun, font=("Arial", 25), bg="orange", fg="blue", borderwidth=3,
                   relief="raised")
    prevB.place(x=150, y=580)

    def clear_fun():
        c1_entry.delete(0, END)
        c2_entry.delete(0, END)
        c3_entry.delete(0, END)
        p1_entry.delete(0, END)
        p2_entry.delete(0, END)
        p3_entry.delete(0, END)
        c1_preview.configure(bg="white")
        c2_preview.configure(bg="white")
        c3_preview.configure(bg="white")
        m_preview.configure(bg="white")
        c1_lbl.configure(bg="white")
        c2_lbl.configure(bg="white")
        c3_lbl.configure(bg="white")
        m_lbl.configure(bg="white")

    # creating an exit button
    prevB = Button(window1, text='CLEAR', command=clear_fun, font=("Arial", 25), bg="orange", fg="blue", borderwidth=3,
                   relief="raised")
    prevB.place(x=670, y=580)

def mix_4():
    # mixing color with proportion -----------------------------
    def combine_hex_values(d):
        d_items = sorted(d.items())
        tot_weight = sum(d.values())
        red = int(sum([int(k[:2], 16) * v for k, v in d_items]) / tot_weight)
        green = int(sum([int(k[2:4], 16) * v for k, v in d_items]) / tot_weight)
        blue = int(sum([int(k[4:6], 16) * v for k, v in d_items]) / tot_weight)
        zpad = lambda x: x if len(x) == 2 else '0' + x
        return zpad(hex(red)[2:]) + zpad(hex(green)[2:]) + zpad(hex(blue)[2:])

    def mix_fun():
        color1 = str(c1_entry.get())
        p1 = int(p1_entry.get())
        color2 = str(c2_entry.get())
        p2 = int(p2_entry.get())
        color3 = str(c3_entry.get())
        p3 = int(p3_entry.get())
        color4 = str(c4_entry.get())
        p4 = int(p4_entry.get())
        c1 = color1[1:]
        c2 = color2[1:]
        c3 = color3[1:]
        c4 = color4[1:]
        # print(color1, c1, color2, c2)

        out = str(combine_hex_values({c1: p1, c2: p2, c3: p3, c4 : p4}))
        out = "#" + out
        c1_preview.configure(bg=color1)
        c1_lbl.configure(bg=color1)
        c2_preview.configure(bg=color2)
        c2_lbl.configure(bg=color2)
        c3_preview.configure(bg=color3)
        c3_lbl.configure(bg=color3)
        c4_preview.configure(bg=color4)
        c4_lbl.configure(bg=color4)
        m_preview.configure(bg=out)
        m_lbl.configure(bg=out)
        # mbox.showinfo("Status", "Color Mixed Successfully.\n\nHex Code for the mixed color  :  #" + out)

    window1 = Tk()
    window1.title('Mix 4 Colors')
    window1.geometry('1000x700')

    # starting label
    start1 = Label(window1, text='MIX 4 COLORS', font=("Arial", 50, "underline"), fg="magenta")
    start1.place(x=260, y=10)

    # for preview
    c1_preview = tk.Text(window1, height=5, width=20, font=("Arial", 15), bg="white", borderwidth=3, relief="solid")
    c1_preview.place(x=50, y=100)
    # starting label
    c1_lbl = Label(window1, text='COLOR 1', font=("Arial", 25), fg="black", bg="white")
    c1_lbl.place(x=90, y=140)
    # Day Entry Box
    c1_entry = Entry(window1, font=("Arial", 25), fg='orange', bg="light yellow", borderwidth=3, width=10)
    c1_entry.place(x=70, y=230)
    # Day Entry Box
    p1_entry = Entry(window1, font=("Arial", 25), fg='orange', bg="light yellow", borderwidth=3, width=10)
    p1_entry.place(x=70, y=285)

    # for preview
    c2_preview = tk.Text(window1, height=5, width=20, font=("Arial", 15), bg="white", borderwidth=3, relief="solid")
    c2_preview.place(x=710, y=100)
    # starting label
    c2_lbl = Label(window1, text='COLOR 2', font=("Arial", 25), fg="black", bg="white")
    c2_lbl.place(x=750, y=140)
    # Day Entry Box
    c2_entry = Entry(window1, font=("Arial", 25), fg='orange', bg="light yellow", borderwidth=3, width=10)
    c2_entry.place(x=730, y=230)
    # Day Entry Box
    p2_entry = Entry(window1, font=("Arial", 25), fg='orange', bg="light yellow", borderwidth=3, width=10)
    p2_entry.place(x=730, y=285)

    # for preview
    c3_preview = tk.Text(window1, height=5, width=20, font=("Arial", 15), bg="white", borderwidth=3, relief="solid")
    c3_preview.place(x=50, y=430)
    # starting label
    c3_lbl = Label(window1, text='COLOR 3', font=("Arial", 25), fg="black", bg="white")
    c3_lbl.place(x=90, y=470)
    # Day Entry Box
    c3_entry = Entry(window1, font=("Arial", 25), fg='orange', bg="light yellow", borderwidth=3, width=10)
    c3_entry.place(x=70, y=560)
    # Day Entry Box
    p3_entry = Entry(window1, font=("Arial", 25), fg='orange', bg="light yellow", borderwidth=3, width=10)
    p3_entry.place(x=70, y=615)

    # for preview
    c4_preview = tk.Text(window1, height=5, width=20, font=("Arial", 15), bg="white", borderwidth=3, relief="solid")
    c4_preview.place(x=710, y=430)
    # starting label
    c4_lbl = Label(window1, text='COLOR 4', font=("Arial", 25), fg="black", bg="white")
    c4_lbl.place(x=750, y=470)
    # Day Entry Box
    c4_entry = Entry(window1, font=("Arial", 25), fg='orange', bg="light yellow", borderwidth=3, width=10)
    c4_entry.place(x=730, y=560)
    # Day Entry Box
    p4_entry = Entry(window1, font=("Arial", 25), fg='orange', bg="light yellow", borderwidth=3, width=10)
    p4_entry.place(x=730, y=615)

    # for preview
    m_preview = tk.Text(window1, height=11, width=26, font=("Arial", 15), bg="white", borderwidth=3, relief="solid")
    m_preview.place(x=350, y=200)
    # starting label
    m_lbl = Label(window1, text='MIXED', font=("Arial", 25), fg="black", bg="white")
    m_lbl.place(x=440, y=290)

    # creating an exit button
    prevB = Button(window1, text='MIX', command=mix_fun, font=("Arial", 25), bg="orange", fg="blue", borderwidth=3,
                   relief="raised")
    prevB.place(x=300, y=580)

    def clear_fun():
        c1_entry.delete(0, END)
        c2_entry.delete(0, END)
        c3_entry.delete(0, END)
        c4_entry.delete(0, END)
        p1_entry.delete(0, END)
        p2_entry.delete(0, END)
        p3_entry.delete(0, END)
        p4_entry.delete(0, END)
        c1_preview.configure(bg="white")
        c2_preview.configure(bg="white")
        c3_preview.configure(bg="white")
        c4_preview.configure(bg="white")
        m_preview.configure(bg="white")
        c1_lbl.configure(bg="white")
        c2_lbl.configure(bg="white")
        c3_lbl.configure(bg="white")
        c4_lbl.configure(bg="white")
        m_lbl.configure(bg="white")

    # creating an exit button
    prevB = Button(window1, text='CLEAR', command=clear_fun, font=("Arial", 25), bg="orange", fg="blue", borderwidth=3,
                   relief="raised")
    prevB.place(x=535, y=580)

def mix_m():
    # mixing color with proportion -----------------------------
    def combine_hex_values(d):
        d_items = sorted(d.items())
        tot_weight = sum(d.values())
        red = int(sum([int(k[:2], 16) * v for k, v in d_items]) / tot_weight)
        green = int(sum([int(k[2:4], 16) * v for k, v in d_items]) / tot_weight)
        blue = int(sum([int(k[4:6], 16) * v for k, v in d_items]) / tot_weight)
        zpad = lambda x: x if len(x) == 2 else '0' + x
        return zpad(hex(red)[2:]) + zpad(hex(green)[2:]) + zpad(hex(blue)[2:])

    def mix_fun():
        color = str(c1_preview.get("1.0", "end-1c"))
        prop = str(c2_preview.get("1.0", "end-1c"))
        color = color.split('\n')
        prop = prop.split('\n')
        color_list = list(color)
        prop_list = list(prop)
        # print(color_list)
        # print(prop_list)
        fin_list = []
        for i in color_list:
            i = i[1:]
            fin_list.append(i)
        # print(fin_list)
        res = {}
        for key in fin_list:
            for value in prop_list:
                res[key] = int(value)
                prop_list.remove(value)
                break

        out = str(combine_hex_values(res))
        out = "#" + out
        m_preview.configure(bg=out)
        m_lbl.configure(bg=out)
        # mbox.showinfo("Status", "Color Mixed Successfully.\n\nHex Code for the mixed color  :  #" + out)

    window1 = Tk()
    window1.title('Mix Multiple Colors')
    window1.geometry('1000x700')

    # starting label
    start1 = Label(window1, text='MIX MULTIPLE COLORS', font=("Arial", 50, "underline"), fg="magenta")
    start1.place(x=100, y=10)

    # for preview
    c1_preview = tk.Text(window1, height=15, width=20, font=("Arial", 15), bg="light yellow", borderwidth=3, relief="solid")
    c1_preview.place(x=50, y=150)
    # starting label
    c1_lbl = Label(window1, text='COLOR', font=("Arial", 25), fg="black")
    c1_lbl.place(x=100, y=100)

    # for preview
    m_preview = tk.Text(window1, height=18, width=26, font=("Arial", 15), bg="white", borderwidth=3, relief="solid")
    m_preview.place(x=350, y=100)
    # starting label
    m_lbl = Label(window1, text='MIXED', font=("Arial", 25), fg="black", bg="white")
    m_lbl.place(x=440, y=270)

    # for preview
    c2_preview = tk.Text(window1, height=15, width=20, font=("Arial", 15), bg="light yellow", borderwidth=3, relief="solid")
    c2_preview.place(x=710, y=150)
    # starting label
    c2_lbl = Label(window1, text='PROPORTION', font=("Arial", 25), fg="black")
    c2_lbl.place(x=710, y=100)

    # creating an exit button
    prevB = Button(window1, text='MIX', command=mix_fun, font=("Arial", 25), bg="orange", fg="blue", borderwidth=3,
                   relief="raised")
    prevB.place(x=150, y=580)

    def clear_fun():
        c1_preview.delete("1.0", "end")
        c2_preview.delete("1.0", "end")
        m_preview.configure(bg="white")
        m_lbl.configure(bg = "white")

    # creating an exit button
    prevB = Button(window1, text='CLEAR', command=clear_fun, font=("Arial", 25), bg="orange", fg="blue", borderwidth=3,
                   relief="raised")
    prevB.place(x=670, y=580)

# creating an exit button
prevB = Button(frame1, text='MIX 2 COLORS', command=mix_2, font=("Arial", 25), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
prevB.place(x = 350, y = 200)

# creating an exit button
prevB = Button(frame1, text='MIX 3 COLORS', command=mix_3, font=("Arial", 25), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
prevB.place(x = 350, y = 300)

# creating an exit button
prevB = Button(frame1, text='MIX 4 COLORS', command=mix_4, font=("Arial", 25), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
prevB.place(x = 350, y = 400)

# creating an exit button
prevB = Button(frame1, text='MIX MULTIPLE COLORS', command=mix_m, font=("Arial", 25), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
prevB.place(x = 280, y = 500)

# defined exit_win function, to show a exit dialog box when tried to exit
def exit_win1():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        frame1.destroy()

# creating an exit button
prevB = Button(frame1, text='EXIT', command=exit_win1, font=("Arial", 25), bg = "red", fg = "blue", borderwidth=3, relief="raised")
prevB.place(x = 420, y = 600)

# this is done to show the exit dialog box when tried to exit from the main window, using the top-roght close button of titlebar
frame1.protocol("WM_DELETE_WINDOW", exit_win1)
frame1.mainloop()