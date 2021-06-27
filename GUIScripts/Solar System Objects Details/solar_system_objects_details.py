

# Imported all the necessary libraries that are used here ------------------------------
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox # for displaying the dialog box
import pandas as pd

# created main window of application -----------------------------------------------
window = tk.Tk() # created a tkinter gui window frame
window.title("Solar System Objects Details")
window.geometry('1000x700')

# -------------------------------- This is for displaying the gif image on the main window of application ------------
frameCnt = 4
frames = [PhotoImage(file='Images/solar.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

cnt = 0.0
def update(ind):
    global cnt
    frame = frames[ind]
    if(cnt == 1.0):
        cnt = 0
    cnt = cnt + 0.2
    ind += int(cnt)
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    window.after(100, update, ind)
label = Label(window)
label.place(x = 250, y = 100)
window.after(0, update, 0)
# --------------------------------------------------------------------

# ---------- here we read the data from the csv file and coverted each column to list
data = pd.read_csv("solar_details.csv")
Object = data["Object"].tolist()
Radius = data["Radius (km)"].tolist()
Mass = data["Mass (10e24 kg)"].tolist()
Density = data["Density (g/cm3)"].tolist()
Gravity = data["Gravity (m/s2)"].tolist()
Semi_major_axis = data["Semi-major axis (km)"].tolist()
Orbital_period = data["Orbital period (days)"].tolist()
Type = data["Type"].tolist()
Moon_of = data["Moon of"].tolist()
Year_of_discovery = data["Year of discovery"].tolist()
Position = data["Position"].tolist()


# get_details function os defined to get the details about any object and also its image
def get_details():
    selected_object = object_var.get()

    # and here we checked for each of the 24 solar objects
    if(selected_object == "Sun"):
        path = 'Images/sun.gif'  # path for image of selected object
        f1 = Frame(window, width=1000, height=700)
        f1.propagate(0)
        f1.pack(side='top')

         # for inserting image in the frame
        c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
        c1.pack()
        p1 = PhotoImage(file=path)
        c1.create_image(250, 220, image=p1, anchor="nw")
        w1 = Canvas(window)
        w1.p1 = p1

        # for printing the label regarding the name of the selected object
        object_name = Label(f1, text='SUN', font=("Arial", 50),fg="magenta")
        object_name.place(x=350, y=20)

         # Created the message bos fo showing the details
        mbox.showinfo(selected_object + " Details ", "Object  :  " + str(selected_object) + "\n\n1.)  Radius (km)  :  " + str(Radius[0]) + "\n\n2.)  Mass (10e24 kg)  :  " + str(Mass[0]) + "\n\n3.)  Density (g/cm3)  :  " + str(Density[0]) + "\n\n4.)  Gravity (m/s2)  :  " + str(Gravity[0]) + "\n\n5.)  Semi-major axis (km)  :  " + str(Semi_major_axis[0]) + "\n\n6.)  Orbital period (days)  :  " + str(Orbital_period[0]) + "\n\n7.)  Type  :  " + str(Type[0]) + "\n\n8.)  Moon of  :  " + str(Moon_of[0]) + "\n\n9.)  Year of discovery  :  " + str(Year_of_discovery[0]) + "\n\n10.)  Position  :  "+ str(Position[0]))

    # And for each of the cases, did the same things only the names , image and data are different

    elif(selected_object == "Jupiter"):
        path = 'Images/jupiter.gif'
        f1 = Frame(window, width=1000, height=700)
        f1.propagate(0)
        f1.pack(side='top')

        c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
        c1.pack()
        p1 = PhotoImage(file=path)
        c1.create_image(250, 220, image=p1, anchor="nw")
        w1 = Canvas(window)
        w1.p1 = p1

        object_name = Label(f1, text='JUPITER', font=("Arial", 35),fg="magenta")
        object_name.place(x=350, y=20)

        mbox.showinfo(selected_object + " Details ", "Object  :  " + str(selected_object) + "\n\n1.)  Radius (km)  :  " + str(Radius[1]) + "\n\n2.)  Mass (10e24 kg)  :  " + str(Mass[1]) + "\n\n3.)  Density (g/cm3)  :  " + str(Density[1]) + "\n\n4.)  Gravity (m/s2)  :  " + str(Gravity[1]) + "\n\n5.)  Semi-major axis (km)  :  " + str(Semi_major_axis[1]) + "\n\n6.)  Orbital period (days)  :  " + str(Orbital_period[1]) + "\n\n7.)  Type  :  " + str(Type[1]) + "\n\n8.)  Moon of  :  " + str(Moon_of[1]) + "\n\n9.)  Year of discovery  :  " + str(Year_of_discovery[1]) + "\n\n10.)  Position  :  "+ str(Position[1]))

    elif(selected_object == "Saturn"):
        path = 'Images/saturn.gif'
        f1 = Frame(window, width=1000, height=700)
        f1.propagate(0)
        f1.pack(side='top')

        c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
        c1.pack()
        p1 = PhotoImage(file=path)
        c1.create_image(250, 220, image=p1, anchor="nw")
        w1 = Canvas(window)
        w1.p1 = p1

        object_name = Label(f1, text='SATURN', font=("Arial", 35),fg="magenta")
        object_name.place(x=350, y=20)

        mbox.showinfo(selected_object + " Details ", "Object  :  " + str(selected_object) + "\n\n1.)  Radius (km)  :  " + str(Radius[2]) + "\n\n2.)  Mass (10e24 kg)  :  " + str(Mass[2]) + "\n\n3.)  Density (g/cm3)  :  " + str(Density[2]) + "\n\n4.)  Gravity (m/s2)  :  " + str(Gravity[2]) + "\n\n5.)  Semi-major axis (km)  :  " + str(Semi_major_axis[2]) + "\n\n6.)  Orbital period (days)  :  " + str(Orbital_period[2]) + "\n\n7.)  Type  :  " + str(Type[2]) + "\n\n8.)  Moon of  :  " + str(Moon_of[2]) + "\n\n9.)  Year of discovery  :  " + str(Year_of_discovery[2]) + "\n\n10.)  Position  :  "+ str(Position[2]))

    elif(selected_object == "Uranus"):
        path = 'Images/uranus.gif'
        f1 = Frame(window, width=1000, height=700)
        f1.propagate(0)
        f1.pack(side='top')

        c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
        c1.pack()
        p1 = PhotoImage(file=path)
        c1.create_image(250, 220, image=p1, anchor="nw")
        w1 = Canvas(window)
        w1.p1 = p1

        object_name = Label(f1, text='URANUS', font=("Arial", 35),fg="magenta")
        object_name.place(x=350, y=20)

        mbox.showinfo(selected_object + " Details ", "Object  :  " + str(selected_object) + "\n\n1.)  Radius (km)  :  " + str(Radius[3]) + "\n\n2.)  Mass (10e24 kg)  :  " + str(Mass[3]) + "\n\n3.)  Density (g/cm3)  :  " + str(Density[3]) + "\n\n4.)  Gravity (m/s2)  :  " + str(Gravity[3]) + "\n\n5.)  Semi-major axis (km)  :  " + str(Semi_major_axis[3]) + "\n\n6.)  Orbital period (days)  :  " + str(Orbital_period[3]) + "\n\n7.)  Type  :  " + str(Type[3]) + "\n\n8.)  Moon of  :  " + str(Moon_of[3]) + "\n\n9.)  Year of discovery  :  " + str(Year_of_discovery[3]) + "\n\n10.)  Position  :  "+ str(Position[3]))

    elif(selected_object == "Neptune"):
        path = 'Images/neptune.gif'
        f1 = Frame(window, width=1000, height=700)
        f1.propagate(0)
        f1.pack(side='top')

        c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
        c1.pack()
        p1 = PhotoImage(file=path)
        c1.create_image(250, 220, image=p1, anchor="nw")
        w1 = Canvas(window)
        w1.p1 = p1

        object_name = Label(f1, text='NEPTUNE', font=("Arial", 35),fg="magenta")
        object_name.place(x=350, y=20)

        mbox.showinfo(selected_object + " Details ", "Object  :  " + str(selected_object) + "\n\n1.)  Radius (km)  :  " + str(Radius[4]) + "\n\n2.)  Mass (10e24 kg)  :  " + str(Mass[4]) + "\n\n3.)  Density (g/cm3)  :  " + str(Density[4]) + "\n\n4.)  Gravity (m/s2)  :  " + str(Gravity[4]) + "\n\n5.)  Semi-major axis (km)  :  " + str(Semi_major_axis[4]) + "\n\n6.)  Orbital period (days)  :  " + str(Orbital_period[4]) + "\n\n7.)  Type  :  " + str(Type[4]) + "\n\n8.)  Moon of  :  " + str(Moon_of[4]) + "\n\n9.)  Year of discovery  :  " + str(Year_of_discovery[4]) + "\n\n10.)  Position  :  "+ str(Position[4]))

    elif(selected_object == "Earth"):
        path = 'Images/earth.gif'
        f1 = Frame(window, width=1000, height=700)
        f1.propagate(0)
        f1.pack(side='top')

        c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
        c1.pack()
        p1 = PhotoImage(file=path)
        c1.create_image(250, 220, image=p1, anchor="nw")
        w1 = Canvas(window)
        w1.p1 = p1

        object_name = Label(f1, text='EARTH', font=("Arial", 35),fg="magenta")
        object_name.place(x=350, y=20)

        mbox.showinfo(selected_object + " Details ", "Object  :  " + str(selected_object) + "\n\n1.)  Radius (km)  :  " + str(Radius[5]) + "\n\n2.)  Mass (10e24 kg)  :  " + str(Mass[5]) + "\n\n3.)  Density (g/cm3)  :  " + str(Density[5]) + "\n\n4.)  Gravity (m/s2)  :  " + str(Gravity[5]) + "\n\n5.)  Semi-major axis (km)  :  " + str(Semi_major_axis[5]) + "\n\n6.)  Orbital period (days)  :  " + str(Orbital_period[5]) + "\n\n7.)  Type  :  " + str(Type[5]) + "\n\n8.)  Moon of  :  " + str(Moon_of[5]) + "\n\n9.)  Year of discovery  :  " + str(Year_of_discovery[5]) + "\n\n10.)  Position  :  "+ str(Position[5]))

    elif(selected_object == "Venus"):
        path = 'Images/venus.gif'
        f1 = Frame(window, width=1000, height=700)
        f1.propagate(0)
        f1.pack(side='top')

        c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
        c1.pack()
        p1 = PhotoImage(file=path)
        c1.create_image(250, 220, image=p1, anchor="nw")
        w1 = Canvas(window)
        w1.p1 = p1

        object_name = Label(f1, text='VENUS', font=("Arial", 35),fg="magenta")
        object_name.place(x=350, y=20)

        mbox.showinfo(selected_object + " Details ", "Object  :  " + str(selected_object) + "\n\n1.)  Radius (km)  :  " + str(Radius[6]) + "\n\n2.)  Mass (10e24 kg)  :  " + str(Mass[6]) + "\n\n3.)  Density (g/cm3)  :  " + str(Density[6]) + "\n\n4.)  Gravity (m/s2)  :  " + str(Gravity[6]) + "\n\n5.)  Semi-major axis (km)  :  " + str(Semi_major_axis[6]) + "\n\n6.)  Orbital period (days)  :  " + str(Orbital_period[6]) + "\n\n7.)  Type  :  " + str(Type[6]) + "\n\n8.)  Moon of  :  " + str(Moon_of[6]) + "\n\n9.)  Year of discovery  :  " + str(Year_of_discovery[6]) + "\n\n10.)  Position  :  "+ str(Position[6]))

    elif(selected_object == "Mars"):
        path = 'Images/mars.gif'
        f1 = Frame(window, width=1000, height=700)
        f1.propagate(0)
        f1.pack(side='top')

        c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
        c1.pack()
        p1 = PhotoImage(file=path)
        c1.create_image(250, 220, image=p1, anchor="nw")
        w1 = Canvas(window)
        w1.p1 = p1

        object_name = Label(f1, text='MARS', font=("Arial", 35),fg="magenta")
        object_name.place(x=350, y=20)

        mbox.showinfo(selected_object + " Details ", "Object  :  " + str(selected_object) + "\n\n1.)  Radius (km)  :  " + str(Radius[7]) + "\n\n2.)  Mass (10e24 kg)  :  " + str(Mass[7]) + "\n\n3.)  Density (g/cm3)  :  " + str(Density[7]) + "\n\n4.)  Gravity (m/s2)  :  " + str(Gravity[7]) + "\n\n5.)  Semi-major axis (km)  :  " + str(Semi_major_axis[7]) + "\n\n6.)  Orbital period (days)  :  " + str(Orbital_period[7]) + "\n\n7.)  Type  :  " + str(Type[7]) + "\n\n8.)  Moon of  :  " + str(Moon_of[7]) + "\n\n9.)  Year of discovery  :  " + str(Year_of_discovery[7]) + "\n\n10.)  Position  :  "+ str(Position[7]))

    elif(selected_object == "Ganymede"):
        path = 'Images/ganymede.gif'
        f1 = Frame(window, width=1000, height=700)
        f1.propagate(0)
        f1.pack(side='top')

        c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
        c1.pack()
        p1 = PhotoImage(file=path)
        c1.create_image(250, 220, image=p1, anchor="nw")
        w1 = Canvas(window)
        w1.p1 = p1

        object_name = Label(f1, text='GANYMEDE', font=("Arial", 35),fg="magenta")
        object_name.place(x=350, y=20)

        mbox.showinfo(selected_object + " Details ", "Object  :  " + str(selected_object) + "\n\n1.)  Radius (km)  :  " + str(Radius[8]) + "\n\n2.)  Mass (10e24 kg)  :  " + str(Mass[8]) + "\n\n3.)  Density (g/cm3)  :  " + str(Density[8]) + "\n\n4.)  Gravity (m/s2)  :  " + str(Gravity[8]) + "\n\n5.)  Semi-major axis (km)  :  " + str(Semi_major_axis[8]) + "\n\n6.)  Orbital period (days)  :  " + str(Orbital_period[8]) + "\n\n7.)  Type  :  " + str(Type[8]) + "\n\n8.)  Moon of  :  " + str(Moon_of[8]) + "\n\n9.)  Year of discovery  :  " + str(Year_of_discovery[8]) + "\n\n10.)  Position  :  "+ str(Position[8]))

    elif(selected_object == "Titan"):
        path = 'Images/titan.gif'
        f1 = Frame(window, width=1000, height=700)
        f1.propagate(0)
        f1.pack(side='top')

        c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
        c1.pack()
        p1 = PhotoImage(file=path)
        c1.create_image(250, 220, image=p1, anchor="nw")
        w1 = Canvas(window)
        w1.p1 = p1

        object_name = Label(f1, text='TITAN', font=("Arial", 35),fg="magenta")
        object_name.place(x=350, y=20)

        mbox.showinfo(selected_object + " Details ", "Object  :  " + str(selected_object) + "\n\n1.)  Radius (km)  :  " + str(Radius[9]) + "\n\n2.)  Mass (10e24 kg)  :  " + str(Mass[9]) + "\n\n3.)  Density (g/cm3)  :  " + str(Density[9]) + "\n\n4.)  Gravity (m/s2)  :  " + str(Gravity[9]) + "\n\n5.)  Semi-major axis (km)  :  " + str(Semi_major_axis[9]) + "\n\n6.)  Orbital period (days)  :  " + str(Orbital_period[9]) + "\n\n7.)  Type  :  " + str(Type[9]) + "\n\n8.)  Moon of  :  " + str(Moon_of[9]) + "\n\n9.)  Year of discovery  :  " + str(Year_of_discovery[9]) + "\n\n10.)  Position  :  "+ str(Position[9]))

    elif(selected_object == "Mercury"):
        path = 'Images/mercury.gif'
        f1 = Frame(window, width=1000, height=700)
        f1.propagate(0)
        f1.pack(side='top')

        c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
        c1.pack()
        p1 = PhotoImage(file=path)
        c1.create_image(250, 220, image=p1, anchor="nw")
        w1 = Canvas(window)
        w1.p1 = p1

        object_name = Label(f1, text='MERCURY', font=("Arial", 35),fg="magenta")
        object_name.place(x=350, y=20)

        mbox.showinfo(selected_object + " Details ", "Object  :  " + str(selected_object) + "\n\n1.)  Radius (km)  :  " + str(Radius[10]) + "\n\n2.)  Mass (10e24 kg)  :  " + str(Mass[10]) + "\n\n3.)  Density (g/cm3)  :  " + str(Density[10]) + "\n\n4.)  Gravity (m/s2)  :  " + str(Gravity[10]) + "\n\n5.)  Semi-major axis (km)  :  " + str(Semi_major_axis[10]) + "\n\n6.)  Orbital period (days)  :  " + str(Orbital_period[10]) + "\n\n7.)  Type  :  " + str(Type[10]) + "\n\n8.)  Moon of  :  " + str(Moon_of[10]) + "\n\n9.)  Year of discovery  :  " + str(Year_of_discovery[10]) + "\n\n10.)  Position  :  "+ str(Position[10]))

    elif(selected_object == "Callisto"):
        path = 'Images/callisto.gif'
        f1 = Frame(window, width=1000, height=700)
        f1.propagate(0)
        f1.pack(side='top')

        c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
        c1.pack()
        p1 = PhotoImage(file=path)
        c1.create_image(250, 220, image=p1, anchor="nw")
        w1 = Canvas(window)
        w1.p1 = p1

        object_name = Label(f1, text='CALLISTO', font=("Arial", 35),fg="magenta")
        object_name.place(x=350, y=20)

        mbox.showinfo(selected_object + " Details ", "Object  :  " + str(selected_object) + "\n\n1.)  Radius (km)  :  " + str(Radius[11]) + "\n\n2.)  Mass (10e24 kg)  :  " + str(Mass[11]) + "\n\n3.)  Density (g/cm3)  :  " + str(Density[11]) + "\n\n4.)  Gravity (m/s2)  :  " + str(Gravity[11]) + "\n\n5.)  Semi-major axis (km)  :  " + str(Semi_major_axis[11]) + "\n\n6.)  Orbital period (days)  :  " + str(Orbital_period[11]) + "\n\n7.)  Type  :  " + str(Type[11]) + "\n\n8.)  Moon of  :  " + str(Moon_of[11]) + "\n\n9.)  Year of discovery  :  " + str(Year_of_discovery[11]) + "\n\n10.)  Position  :  "+ str(Position[11]))

    elif(selected_object == "Io"):
        path = 'Images/io.gif'
        f1 = Frame(window, width=1000, height=700)
        f1.propagate(0)
        f1.pack(side='top')

        c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
        c1.pack()
        p1 = PhotoImage(file=path)
        c1.create_image(250, 220, image=p1, anchor="nw")
        w1 = Canvas(window)
        w1.p1 = p1

        object_name = Label(f1, text='IO', font=("Arial", 35),fg="magenta")
        object_name.place(x=350, y=20)

        mbox.showinfo(selected_object + " Details ", "Object  :  " + str(selected_object) + "\n\n1.)  Radius (km)  :  " + str(Radius[12]) + "\n\n2.)  Mass (10e24 kg)  :  " + str(Mass[12]) + "\n\n3.)  Density (g/cm3)  :  " + str(Density[12]) + "\n\n4.)  Gravity (m/s2)  :  " + str(Gravity[12]) + "\n\n5.)  Semi-major axis (km)  :  " + str(Semi_major_axis[12]) + "\n\n6.)  Orbital period (days)  :  " + str(Orbital_period[12]) + "\n\n7.)  Type  :  " + str(Type[12]) + "\n\n8.)  Moon of  :  " + str(Moon_of[12]) + "\n\n9.)  Year of discovery  :  " + str(Year_of_discovery[12]) + "\n\n10.)  Position  :  "+ str(Position[12]))

    elif(selected_object == "Moon"):
        path = 'Images/moon.gif'
        f1 = Frame(window, width=1000, height=700)
        f1.propagate(0)
        f1.pack(side='top')

        c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
        c1.pack()
        p1 = PhotoImage(file=path)
        c1.create_image(250, 220, image=p1, anchor="nw")
        w1 = Canvas(window)
        w1.p1 = p1

        object_name = Label(f1, text='MOON', font=("Arial", 35),fg="magenta")
        object_name.place(x=350, y=20)

        mbox.showinfo(selected_object + " Details ", "Object  :  " + str(selected_object) + "\n\n1.)  Radius (km)  :  " + str(Radius[13]) + "\n\n2.)  Mass (10e24 kg)  :  " + str(Mass[13]) + "\n\n3.)  Density (g/cm3)  :  " + str(Density[13]) + "\n\n4.)  Gravity (m/s2)  :  " + str(Gravity[13]) + "\n\n5.)  Semi-major axis (km)  :  " + str(Semi_major_axis[13]) + "\n\n6.)  Orbital period (days)  :  " + str(Orbital_period[13]) + "\n\n7.)  Type  :  " + str(Type[13]) + "\n\n8.)  Moon of  :  " + str(Moon_of[13]) + "\n\n9.)  Year of discovery  :  " + str(Year_of_discovery[13]) + "\n\n10.)  Position  :  "+ str(Position[13]))

    elif(selected_object == "Europa"):
        path = 'Images/europa.gif'
        f1 = Frame(window, width=1000, height=700)
        f1.propagate(0)
        f1.pack(side='top')

        c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
        c1.pack()
        p1 = PhotoImage(file=path)
        c1.create_image(250, 220, image=p1, anchor="nw")
        w1 = Canvas(window)
        w1.p1 = p1

        object_name = Label(f1, text='EUROPA', font=("Arial", 35),fg="magenta")
        object_name.place(x=350, y=20)

        mbox.showinfo(selected_object + " Details ", "Object  :  " + str(selected_object) + "\n\n1.)  Radius (km)  :  " + str(Radius[14]) + "\n\n2.)  Mass (10e24 kg)  :  " + str(Mass[14]) + "\n\n3.)  Density (g/cm3)  :  " + str(Density[14]) + "\n\n4.)  Gravity (m/s2)  :  " + str(Gravity[14]) + "\n\n5.)  Semi-major axis (km)  :  " + str(Semi_major_axis[14]) + "\n\n6.)  Orbital period (days)  :  " + str(Orbital_period[14]) + "\n\n7.)  Type  :  " + str(Type[14]) + "\n\n8.)  Moon of  :  " + str(Moon_of[14]) + "\n\n9.)  Year of discovery  :  " + str(Year_of_discovery[14]) + "\n\n10.)  Position  :  "+ str(Position[14]))

    elif(selected_object == "Triton"):
        path = 'Images/triton.gif'
        f1 = Frame(window, width=1000, height=700)
        f1.propagate(0)
        f1.pack(side='top')

        c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
        c1.pack()
        p1 = PhotoImage(file=path)
        c1.create_image(250, 220, image=p1, anchor="nw")
        w1 = Canvas(window)
        w1.p1 = p1

        object_name = Label(f1, text='TRITON', font=("Arial", 35),fg="magenta")
        object_name.place(x=350, y=20)

        mbox.showinfo(selected_object + " Details ", "Object  :  " + str(selected_object) + "\n\n1.)  Radius (km)  :  " + str(Radius[15]) + "\n\n2.)  Mass (10e24 kg)  :  " + str(Mass[15]) + "\n\n3.)  Density (g/cm3)  :  " + str(Density[15]) + "\n\n4.)  Gravity (m/s2)  :  " + str(Gravity[15]) + "\n\n5.)  Semi-major axis (km)  :  " + str(Semi_major_axis[15]) + "\n\n6.)  Orbital period (days)  :  " + str(Orbital_period[15]) + "\n\n7.)  Type  :  " + str(Type[15]) + "\n\n8.)  Moon of  :  " + str(Moon_of[15]) + "\n\n9.)  Year of discovery  :  " + str(Year_of_discovery[15]) + "\n\n10.)  Position  :  "+ str(Position[15]))

    elif(selected_object == "Pluto"):
        path = 'Images/pluto.gif'
        f1 = Frame(window, width=1000, height=700)
        f1.propagate(0)
        f1.pack(side='top')

        c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
        c1.pack()
        p1 = PhotoImage(file=path)
        c1.create_image(250, 220, image=p1, anchor="nw")
        w1 = Canvas(window)
        w1.p1 = p1

        object_name = Label(f1, text='PLUTO', font=("Arial", 35),fg="magenta")
        object_name.place(x=350, y=20)

        mbox.showinfo(selected_object + " Details ", "Object  :  " + str(selected_object) + "\n\n1.)  Radius (km)  :  " + str(Radius[16]) + "\n\n2.)  Mass (10e24 kg)  :  " + str(Mass[16]) + "\n\n3.)  Density (g/cm3)  :  " + str(Density[16]) + "\n\n4.)  Gravity (m/s2)  :  " + str(Gravity[16]) + "\n\n5.)  Semi-major axis (km)  :  " + str(Semi_major_axis[16]) + "\n\n6.)  Orbital period (days)  :  " + str(Orbital_period[16]) + "\n\n7.)  Type  :  " + str(Type[16]) + "\n\n8.)  Moon of  :  " + str(Moon_of[16]) + "\n\n9.)  Year of discovery  :  " + str(Year_of_discovery[16]) + "\n\n10.)  Position  :  "+ str(Position[16]))

    elif(selected_object == "Eris"):
        path = 'Images/eris.gif'
        f1 = Frame(window, width=1000, height=700)
        f1.propagate(0)
        f1.pack(side='top')

        c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
        c1.pack()
        p1 = PhotoImage(file=path)
        c1.create_image(250, 220, image=p1, anchor="nw")
        w1 = Canvas(window)
        w1.p1 = p1

        object_name = Label(f1, text='ERIS', font=("Arial", 35),fg="magenta")
        object_name.place(x=350, y=20)

        mbox.showinfo(selected_object + " Details ", "Object  :  " + str(selected_object) + "\n\n1.)  Radius (km)  :  " + str(Radius[17]) + "\n\n2.)  Mass (10e24 kg)  :  " + str(Mass[17]) + "\n\n3.)  Density (g/cm3)  :  " + str(Density[17]) + "\n\n4.)  Gravity (m/s2)  :  " + str(Gravity[17]) + "\n\n5.)  Semi-major axis (km)  :  " + str(Semi_major_axis[17]) + "\n\n6.)  Orbital period (days)  :  " + str(Orbital_period[17]) + "\n\n7.)  Type  :  " + str(Type[17]) + "\n\n8.)  Moon of  :  " + str(Moon_of[17]) + "\n\n9.)  Year of discovery  :  " + str(Year_of_discovery[17]) + "\n\n10.)  Position  :  "+ str(Position[17]))

    elif(selected_object == "Titania"):
        path = 'Images/titania.gif'
        f1 = Frame(window, width=1000, height=700)
        f1.propagate(0)
        f1.pack(side='top')

        c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
        c1.pack()
        p1 = PhotoImage(file=path)
        c1.create_image(250, 220, image=p1, anchor="nw")
        w1 = Canvas(window)
        w1.p1 = p1

        object_name = Label(f1, text='TITANIA', font=("Arial", 35),fg="magenta")
        object_name.place(x=350, y=20)

        mbox.showinfo(selected_object + " Details ", "Object  :  " + str(selected_object) + "\n\n1.)  Radius (km)  :  " + str(Radius[18]) + "\n\n2.)  Mass (10e24 kg)  :  " + str(Mass[18]) + "\n\n3.)  Density (g/cm3)  :  " + str(Density[18]) + "\n\n4.)  Gravity (m/s2)  :  " + str(Gravity[18]) + "\n\n5.)  Semi-major axis (km)  :  " + str(Semi_major_axis[18]) + "\n\n6.)  Orbital period (days)  :  " + str(Orbital_period[18]) + "\n\n7.)  Type  :  " + str(Type[18]) + "\n\n8.)  Moon of  :  " + str(Moon_of[18]) + "\n\n9.)  Year of discovery  :  " + str(Year_of_discovery[18]) + "\n\n10.)  Position  :  "+ str(Position[18]))

    elif(selected_object == "Haumea"):
        path = 'Images/haumea.gif'
        f1 = Frame(window, width=1000, height=700)
        f1.propagate(0)
        f1.pack(side='top')

        c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
        c1.pack()
        p1 = PhotoImage(file=path)
        c1.create_image(250, 220, image=p1, anchor="nw")
        w1 = Canvas(window)
        w1.p1 = p1

        object_name = Label(f1, text='HAUMEA', font=("Arial", 35),fg="magenta")
        object_name.place(x=350, y=20)

        mbox.showinfo(selected_object + " Details ", "Object  :  " + str(selected_object) + "\n\n1.)  Radius (km)  :  " + str(Radius[19]) + "\n\n2.)  Mass (10e24 kg)  :  " + str(Mass[19]) + "\n\n3.)  Density (g/cm3)  :  " + str(Density[19]) + "\n\n4.)  Gravity (m/s2)  :  " + str(Gravity[19]) + "\n\n5.)  Semi-major axis (km)  :  " + str(Semi_major_axis[19]) + "\n\n6.)  Orbital period (days)  :  " + str(Orbital_period[19]) + "\n\n7.)  Type  :  " + str(Type[19]) + "\n\n8.)  Moon of  :  " + str(Moon_of[19]) + "\n\n9.)  Year of discovery  :  " + str(Year_of_discovery[19]) + "\n\n10.)  Position  :  "+ str(Position[19]))

    elif(selected_object == "Rhea"):
        path = 'Images/rhea.gif'
        f1 = Frame(window, width=1000, height=700)
        f1.propagate(0)
        f1.pack(side='top')

        c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
        c1.pack()
        p1 = PhotoImage(file=path)
        c1.create_image(250, 220, image=p1, anchor="nw")
        w1 = Canvas(window)
        w1.p1 = p1

        object_name = Label(f1, text='RHEA', font=("Arial", 35),fg="magenta")
        object_name.place(x=350, y=20)

        mbox.showinfo(selected_object + " Details ", "Object  :  " + str(selected_object) + "\n\n1.)  Radius (km)  :  " + str(Radius[20]) + "\n\n2.)  Mass (10e24 kg)  :  " + str(Mass[20]) + "\n\n3.)  Density (g/cm3)  :  " + str(Density[20]) + "\n\n4.)  Gravity (m/s2)  :  " + str(Gravity[20]) + "\n\n5.)  Semi-major axis (km)  :  " + str(Semi_major_axis[20]) + "\n\n6.)  Orbital period (days)  :  " + str(Orbital_period[20]) + "\n\n7.)  Type  :  " + str(Type[20]) + "\n\n8.)  Moon of  :  " + str(Moon_of[20]) + "\n\n9.)  Year of discovery  :  " + str(Year_of_discovery[20]) + "\n\n10.)  Position  :  "+ str(Position[20]))

    elif(selected_object == "Oberon"):
        path = 'Images/oberon.gif'
        f1 = Frame(window, width=1000, height=700)
        f1.propagate(0)
        f1.pack(side='top')

        c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
        c1.pack()
        p1 = PhotoImage(file=path)
        c1.create_image(250, 220, image=p1, anchor="nw")
        w1 = Canvas(window)
        w1.p1 = p1

        object_name = Label(f1, text='OBERON', font=("Arial", 35),fg="magenta")
        object_name.place(x=350, y=20)

        mbox.showinfo(selected_object + " Details ", "Object  :  " + str(selected_object) + "\n\n1.)  Radius (km)  :  " + str(Radius[21]) + "\n\n2.)  Mass (10e24 kg)  :  " + str(Mass[21]) + "\n\n3.)  Density (g/cm3)  :  " + str(Density[21]) + "\n\n4.)  Gravity (m/s2)  :  " + str(Gravity[21]) + "\n\n5.)  Semi-major axis (km)  :  " + str(Semi_major_axis[21]) + "\n\n6.)  Orbital period (days)  :  " + str(Orbital_period[21]) + "\n\n7.)  Type  :  " + str(Type[21]) + "\n\n8.)  Moon of  :  " + str(Moon_of[21]) + "\n\n9.)  Year of discovery  :  " + str(Year_of_discovery[21]) + "\n\n10.)  Position  :  "+ str(Position[21]))

    elif(selected_object == "Iapetus"):
        path = 'Images/iapetus.gif'
        f1 = Frame(window, width=1000, height=700)
        f1.propagate(0)
        f1.pack(side='top')

        c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
        c1.pack()
        p1 = PhotoImage(file=path)
        c1.create_image(250, 220, image=p1, anchor="nw")
        w1 = Canvas(window)
        w1.p1 = p1

        object_name = Label(f1, text='IAPETUS', font=("Arial", 35),fg="magenta")
        object_name.place(x=350, y=20)

        mbox.showinfo(selected_object + " Details ", "Object  :  " + str(selected_object) + "\n\n1.)  Radius (km)  :  " + str(Radius[22]) + "\n\n2.)  Mass (10e24 kg)  :  " + str(Mass[22]) + "\n\n3.)  Density (g/cm3)  :  " + str(Density[22]) + "\n\n4.)  Gravity (m/s2)  :  " + str(Gravity[22]) + "\n\n5.)  Semi-major axis (km)  :  " + str(Semi_major_axis[22]) + "\n\n6.)  Orbital period (days)  :  " + str(Orbital_period[22]) + "\n\n7.)  Type  :  " + str(Type[22]) + "\n\n8.)  Moon of  :  " + str(Moon_of[22]) + "\n\n9.)  Year of discovery  :  " + str(Year_of_discovery[22]) + "\n\n10.)  Position  :  "+ str(Position[22]))

    elif(selected_object == "Makemake"):
        path = 'Images/makemake.gif'
        f1 = Frame(window, width=1000, height=700)
        f1.propagate(0)
        f1.pack(side='top')

        c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
        c1.pack()
        p1 = PhotoImage(file=path)
        c1.create_image(250, 220, image=p1, anchor="nw")
        w1 = Canvas(window)
        w1.p1 = p1

        object_name = Label(f1, text='MAKEMAKE', font=("Arial", 35),fg="magenta")
        object_name.place(x=350, y=20)

        mbox.showinfo(selected_object + " Details ", "Object  :  " + str(selected_object) + "\n\n1.)  Radius (km)  :  " + str(Radius[23]) + "\n\n2.)  Mass (10e24 kg)  :  " + str(Mass[23]) + "\n\n3.)  Density (g/cm3)  :  " + str(Density[23]) + "\n\n4.)  Gravity (m/s2)  :  " + str(Gravity[23]) + "\n\n5.)  Semi-major axis (km)  :  " + str(Semi_major_axis[23]) + "\n\n6.)  Orbital period (days)  :  " + str(Orbital_period[23]) + "\n\n7.)  Type  :  " + str(Type[23]) + "\n\n8.)  Moon of  :  " + str(Moon_of[23]) + "\n\n9.)  Year of discovery  :  " + str(Year_of_discovery[23]) + "\n\n10.)  Position  :  "+ str(Position[23]))

    elif(selected_object == "Gonggong"):
        path = 'Images/gonggong.gif'
        f1 = Frame(window, width=1000, height=700)
        f1.propagate(0)
        f1.pack(side='top')

        c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
        c1.pack()
        p1 = PhotoImage(file=path)
        c1.create_image(250, 220, image=p1, anchor="nw")
        w1 = Canvas(window)
        w1.p1 = p1

        object_name = Label(f1, text='GONGGONG', font=("Arial", 35),fg="magenta")
        object_name.place(x=350, y=20)

        mbox.showinfo(selected_object + " Details ", "Object  :  " + str(selected_object) + "\n\n1.)  Radius (km)  :  " + str(Radius[24]) + "\n\n2.)  Mass (10e24 kg)  :  " + str(Mass[24]) + "\n\n3.)  Density (g/cm3)  :  " + str(Density[24]) + "\n\n4.)  Gravity (m/s2)  :  " + str(Gravity[24]) + "\n\n5.)  Semi-major axis (km)  :  " + str(Semi_major_axis[24]) + "\n\n6.)  Orbital period (days)  :  " + str(Orbital_period[24]) + "\n\n7.)  Type  :  " + str(Type[24]) + "\n\n8.)  Moon of  :  " + str(Moon_of[24]) + "\n\n9.)  Year of discovery  :  " + str(Year_of_discovery[24]) + "\n\n10.)  Position  :  "+ str(Position[24]))



# starting label - which is shown at the top of the main window of application
start1 = Label(window, text='SOLAR SYSTEM OBJECTS', font=("Arial", 50),fg="magenta",underline=0)
start1.place(x=70,y=10)

# label to tell user to selecte the objetc from option menu
dob = Label(window, text='Solar System Object  : ', font=("Arial", 30),fg="brown")
dob.place(x=230,y=450)

# creating the drop down menu button - for all the names of solar system objects
object_var = tk.StringVar()
# as icon size are really small, we defined the following 7 sizes
object_choices = Object
object_menu = OptionMenu(window, object_var, *object_choices)
object_menu.config(font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3)
object_menu["menu"].config(font=("Arial", 15), bg = "light yellow", fg = "blue")
object_menu.place(x=650, y=450)
object_var.set("Sun") # size 1 is selected as by default, and we can

# defined exit_win function, to show a exit dialog box when tried to exit
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

# to reset the value to default value of Option Menu
def reset_menu():
    object_var.set("Sun")

# button to get the details about that solar object
detailsb = Button(window,text="DETAILS",command= get_details,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
detailsb.place(x = 200, y = 550)

# button to reset
resetb = Button(window,text="RESET",command= reset_menu,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
resetb.place(x = 460, y = 550)

# button to exit
resetb = Button(window,text="EXIT",command= exit_win,font=("Arial", 20), bg = "red", fg = "blue", borderwidth=3, relief="raised")
resetb.place(x = 700, y = 550)

window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()
