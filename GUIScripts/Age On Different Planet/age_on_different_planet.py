
# Age On Different Planet

# imported necessary library
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import tkinter.messagebox as mbox # for displaying the dialog box
from datetime import datetime

# Main Window & Configuration
window = tk.Tk() # created a tkinter gui window frame
window.title("Age On Different Planet")
window.geometry('1000x700')

# defined exit_win function, to show a exit dialog box when tried to exit
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

# to reset the value
def reset_fun():
    planet_var.set("EARTH")

# function to start the calculation
def start_fun():
    # age in seconds
    def calculate_seconds(date):
        rough_age = (datetime.now() - date)
        return rough_age.total_seconds()

    # for Mercury
    def calculate_fun1():
        dob = str(dob_entry.get())
        dob = dob.split('/')

        age = calculate_seconds(datetime(int(dob[2]), int(dob[1]), int(dob[0])))
        mbox.showinfo("Age on Mercury","Your Age on Mercury :\n\n" + str(int((age/31557600)*0.2408467)) + "  yrs")

    # for Venus
    def calculate_fun2():
        dob = str(dob_entry.get())
        dob = dob.split('/')

        age = calculate_seconds(datetime(int(dob[2]), int(dob[1]), int(dob[0])))
        mbox.showinfo("Age on Venus", "Your Age on Venus :\n\n" + str(int((age / 31557600) * 0.61519726)) + "  yrs")

    # for Earth
    def calculate_fun3():
        dob = str(dob_entry.get())
        dob = dob.split('/')

        age = calculate_seconds(datetime(int(dob[2]), int(dob[1]), int(dob[0])))
        mbox.showinfo("Age on Earth", "Your Age on Earth :\n\n" + str(int((age / 31557600))) + "  yrs")

    # for Mars
    def calculate_fun4():
        dob = str(dob_entry.get())
        dob = dob.split('/')

        age = calculate_seconds(datetime(int(dob[2]), int(dob[1]), int(dob[0])))
        mbox.showinfo("Age on Mars", "Your Age on Mars :\n\n" + str(int((age / 31557600) * 1.8808158)) + "  yrs")

    # for Jupiter
    def calculate_fun5():
        dob = str(dob_entry.get())
        dob = dob.split('/')

        age = calculate_seconds(datetime(int(dob[2]), int(dob[1]), int(dob[0])))
        mbox.showinfo("Age on Jupiter", "Your Age on Jupiter :\n\n" + str(int((age / 31557600) * 11.862615)) + "  yrs")

    # for Saturn
    def calculate_fun6():
        dob = str(dob_entry.get())
        dob = dob.split('/')

        age = calculate_seconds(datetime(int(dob[2]), int(dob[1]), int(dob[0])))
        mbox.showinfo("Age on Saturn", "Your Age on Saturn :\n\n" + str(int((age / 31557600) * 29.447498)) + "  yrs")

    # for Uranus
    def calculate_fun7():
        dob = str(dob_entry.get())
        dob = dob.split('/')

        age = calculate_seconds(datetime(int(dob[2]), int(dob[1]), int(dob[0])))
        mbox.showinfo("Age on Uranus", "Your Age on Uranus :\n\n" + str(int((age / 31557600) * 84.016846)) + "  yrs")

    # for Neptune
    def calculate_fun8():
        dob = str(dob_entry.get())
        dob = dob.split('/')

        age = calculate_seconds(datetime(int(dob[2]), int(dob[1]), int(dob[0])))
        mbox.showinfo("Age on Neptune", "Your Age on Neptune :\n\n" + str(int((age / 31557600) * 164.79132)) + "  yrs")

    # for Pluto
    def calculate_fun9():
        dob = str(dob_entry.get())
        dob = dob.split('/')

        age = calculate_seconds(datetime(int(dob[2]), int(dob[1]), int(dob[0])))
        mbox.showinfo("Age on Pluto", "Your Age on Pluto :\n\n" + str(int((age / 31557600) * 248.00)) + "  yrs")

    # for each planet
    planet = planet_var.get()
    if planet == "MERCURY":
        path = 'Images/mercury.gif'
        f1 = Frame(window, width=1000, height=700)
        f1.propagate(0)
        f1.pack(side='top')

        c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
        c1.pack()
        p1 = PhotoImage(file=path)
        c1.create_image(200, 120, image=p1, anchor="nw")
        w1 = Canvas(window)
        w1.p1 = p1

        p_name = Label(f1, text='MERCURY', font=("Arial", 50),fg="magenta", bg = "white")
        p_name.place(x=300, y=10)

        dob_lbl = Label(f1, text='ENTER  D.O.B. : ', font=("Arial", 40), fg="brown", bg="white")
        dob_lbl.place(x=120, y=500)

        # Created Entry Box
        dob_entry = Entry(window, font=("Arial", 30), fg='orange', bg="light yellow", borderwidth=3, width=14)
        dob_entry.place(x=530, y=505)

        # button to calculate
        calculateb = Button(window, text="CALCULATE", command=calculate_fun1, font=("Arial", 25), bg="orange", fg="blue", borderwidth=3,relief="raised")
        calculateb.place(x=380, y=600)

    elif planet == "VENUS":
        path = 'Images/venus.gif'
        f1 = Frame(window, width=1000, height=700)
        f1.propagate(0)
        f1.pack(side='top')

        c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
        c1.pack()
        p1 = PhotoImage(file=path)
        c1.create_image(200, 120, image=p1, anchor="nw")
        w1 = Canvas(window)
        w1.p1 = p1

        p_name = Label(f1, text='VENUS', font=("Arial", 50),fg="magenta", bg = "white")
        p_name.place(x=300, y=10)

        dob_lbl = Label(f1, text='ENTER  D.O.B. : ', font=("Arial", 40), fg="brown", bg="white")
        dob_lbl.place(x=120, y=500)

        # Created Entry Box
        dob_entry = Entry(window, font=("Arial", 30), fg='orange', bg="light yellow", borderwidth=3, width=14)
        dob_entry.place(x=530, y=505)

        # button to calculate
        calculateb = Button(window, text="CALCULATE", command=calculate_fun2, font=("Arial", 25), bg="orange", fg="blue",
                            borderwidth=3, relief="raised")
        calculateb.place(x=380, y=600)

    elif planet == "EARTH":
        path = 'Images/earth.gif'
        f1 = Frame(window, width=1000, height=700)
        f1.propagate(0)
        f1.pack(side='top')

        c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
        c1.pack()
        p1 = PhotoImage(file=path)
        c1.create_image(200, 120, image=p1, anchor="nw")
        w1 = Canvas(window)
        w1.p1 = p1

        p_name = Label(f1, text='EARTH', font=("Arial", 50),fg="magenta", bg = "white")
        p_name.place(x=300, y=10)

        dob_lbl = Label(f1, text='ENTER  D.O.B. : ', font=("Arial", 40), fg="brown", bg="white")
        dob_lbl.place(x=120, y=500)

        # Created Entry Box
        dob_entry = Entry(window, font=("Arial", 30), fg='orange', bg="light yellow", borderwidth=3, width=14)
        dob_entry.place(x=530, y=505)

        # button to calculate
        calculateb = Button(window, text="CALCULATE", command=calculate_fun3, font=("Arial", 25), bg="orange", fg="blue",
                            borderwidth=3, relief="raised")
        calculateb.place(x=380, y=600)

    elif planet == "MARS":
        path = 'Images/mars.gif'
        f1 = Frame(window, width=1000, height=700)
        f1.propagate(0)
        f1.pack(side='top')

        c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
        c1.pack()
        p1 = PhotoImage(file=path)
        c1.create_image(200, 120, image=p1, anchor="nw")
        w1 = Canvas(window)
        w1.p1 = p1

        p_name = Label(f1, text='MARS', font=("Arial", 50),fg="magenta", bg = "white")
        p_name.place(x=300, y=10)

        dob_lbl = Label(f1, text='ENTER  D.O.B. : ', font=("Arial", 40), fg="brown", bg="white")
        dob_lbl.place(x=120, y=500)

        # Created Entry Box
        dob_entry = Entry(window, font=("Arial", 30), fg='orange', bg="light yellow", borderwidth=3, width=14)
        dob_entry.place(x=530, y=505)

        # button to calculate
        calculateb = Button(window, text="CALCULATE", command=calculate_fun4, font=("Arial", 25), bg="orange", fg="blue",
                            borderwidth=3, relief="raised")
        calculateb.place(x=380, y=600)

    elif planet == "JUPITER":
        path = 'Images/jupiter.gif'
        f1 = Frame(window, width=1000, height=700)
        f1.propagate(0)
        f1.pack(side='top')

        c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
        c1.pack()
        p1 = PhotoImage(file=path)
        c1.create_image(200, 120, image=p1, anchor="nw")
        w1 = Canvas(window)
        w1.p1 = p1

        p_name = Label(f1, text='JUPITER', font=("Arial", 50),fg="magenta", bg = "white")
        p_name.place(x=300, y=10)

        dob_lbl = Label(f1, text='ENTER  D.O.B. : ', font=("Arial", 40), fg="brown", bg="white")
        dob_lbl.place(x=120, y=500)

        # Created Entry Box
        dob_entry = Entry(window, font=("Arial", 30), fg='orange', bg="light yellow", borderwidth=3, width=14)
        dob_entry.place(x=530, y=505)

        # button to calculate
        calculateb = Button(window, text="CALCULATE", command=calculate_fun5, font=("Arial", 25), bg="orange", fg="blue",
                            borderwidth=3, relief="raised")
        calculateb.place(x=380, y=600)

    elif planet == "SATURN":
        path = 'Images/saturn.gif'
        f1 = Frame(window, width=1000, height=700)
        f1.propagate(0)
        f1.pack(side='top')

        c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
        c1.pack()
        p1 = PhotoImage(file=path)
        c1.create_image(200, 120, image=p1, anchor="nw")
        w1 = Canvas(window)
        w1.p1 = p1

        p_name = Label(f1, text='SATURN', font=("Arial", 50),fg="magenta", bg = "white")
        p_name.place(x=300, y=10)

        dob_lbl = Label(f1, text='ENTER  D.O.B. : ', font=("Arial", 40), fg="brown", bg="white")
        dob_lbl.place(x=120, y=500)

        # Created Entry Box
        dob_entry = Entry(window, font=("Arial", 30), fg='orange', bg="light yellow", borderwidth=3, width=14)
        dob_entry.place(x=530, y=505)

        # button to calculate
        calculateb = Button(window, text="CALCULATE", command=calculate_fun6, font=("Arial", 25), bg="orange", fg="blue",
                            borderwidth=3, relief="raised")
        calculateb.place(x=380, y=600)

    elif planet == "URANUS":
        path = 'Images/uranus.gif'
        f1 = Frame(window, width=1000, height=700)
        f1.propagate(0)
        f1.pack(side='top')

        c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
        c1.pack()
        p1 = PhotoImage(file=path)
        c1.create_image(200, 120, image=p1, anchor="nw")
        w1 = Canvas(window)
        w1.p1 = p1

        p_name = Label(f1, text='URANUS', font=("Arial", 50),fg="magenta", bg = "white")
        p_name.place(x=300, y=10)

        dob_lbl = Label(f1, text='ENTER  D.O.B. : ', font=("Arial", 40), fg="brown", bg="white")
        dob_lbl.place(x=120, y=500)

        # Created Entry Box
        dob_entry = Entry(window, font=("Arial", 30), fg='orange', bg="light yellow", borderwidth=3, width=14)
        dob_entry.place(x=530, y=505)

        # button to calculate
        calculateb = Button(window, text="CALCULATE", command=calculate_fun7, font=("Arial", 25), bg="orange", fg="blue",
                            borderwidth=3, relief="raised")
        calculateb.place(x=380, y=600)

    elif planet == "NEPTUNE":
        path = 'Images/neptune.gif'
        f1 = Frame(window, width=1000, height=700)
        f1.propagate(0)
        f1.pack(side='top')

        c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
        c1.pack()
        p1 = PhotoImage(file=path)
        c1.create_image(200, 120, image=p1, anchor="nw")
        w1 = Canvas(window)
        w1.p1 = p1

        p_name = Label(f1, text='NEPTUNE', font=("Arial", 50),fg="magenta", bg = "white")
        p_name.place(x=300, y=10)

        dob_lbl = Label(f1, text='ENTER  D.O.B. : ', font=("Arial", 40), fg="brown", bg="white")
        dob_lbl.place(x=120, y=500)

        # Created Entry Box
        dob_entry = Entry(window, font=("Arial", 30), fg='orange', bg="light yellow", borderwidth=3, width=14)
        dob_entry.place(x=530, y=505)

        # button to calculate
        calculateb = Button(window, text="CALCULATE", command=calculate_fun8, font=("Arial", 25), bg="orange", fg="blue",
                            borderwidth=3, relief="raised")
        calculateb.place(x=380, y=600)

    elif planet == "PLUTO":
        path = 'Images/pluto.gif'
        f1 = Frame(window, width=1000, height=700)
        f1.propagate(0)
        f1.pack(side='top')

        c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
        c1.pack()
        p1 = PhotoImage(file=path)
        c1.create_image(200, 120, image=p1, anchor="nw")
        w1 = Canvas(window)
        w1.p1 = p1

        p_name = Label(f1, text='PLUTO', font=("Arial", 50),fg="magenta", bg = "white")
        p_name.place(x=300, y=10)

        dob_lbl = Label(f1, text='ENTER  D.O.B. : ', font=("Arial", 40), fg="brown", bg="white")
        dob_lbl.place(x=120, y=500)

        # Created Entry Box
        dob_entry = Entry(window, font=("Arial", 30), fg='orange', bg="light yellow", borderwidth=3, width=14)
        dob_entry.place(x=530, y=505)

        # button to calculate
        calculateb = Button(window, text="CALCULATE", command=calculate_fun9, font=("Arial", 25), bg="orange", fg="blue",
                            borderwidth=3, relief="raised")
        calculateb.place(x=380, y=600)



# starting label
start1 = Label(window, text='AGE ON DIFFERENT PLANET', font=("Arial", 50),fg="magenta")
start1.place(x=50,y=10)

# image on the main window
path = "Images/age.jpg"
# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))
# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image = img)
# The Pack geometry manager packs widgets in rows or columns.
# panel.pack(side = "top", fill = "both", expand = "no")
panel.place(x = 130, y = 120)

# starting label
dob = Label(window, text='CHOOSE PLANET : ', font=("Arial", 35),fg="brown")
dob.place(x=180,y=500)

# creating the drop down menu button
planet_var = tk.StringVar()
planet_choices = ["MERCURY","VENUS","EARTH","MARS","JUPITER","SATURN","URANUS","NEPTUNE","PLUTO"]
planet_menu = OptionMenu(window, planet_var, *planet_choices)
planet_menu.config(font=("Arial", 25), bg = "light green", fg = "blue", borderwidth=3)
planet_menu["menu"].config(font=("Arial", 20), bg = "light yellow", fg = "blue")
planet_menu.place(x=630, y=500)
planet_var.set("EARTH")

# button to get the started
startb = Button(window,text="START",command= start_fun,font=("Arial", 25), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
startb.place(x = 120, y = 600)

# button to reset
resetb = Button(window,text="RESET",command= reset_fun,font=("Arial", 25), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
resetb.place(x = 430, y = 600)

# button to exit
resetb = Button(window,text="EXIT",command= exit_win,font=("Arial", 25), bg = "red", fg = "blue", borderwidth=3, relief="raised")
resetb.place(x = 750, y = 600)

window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()

