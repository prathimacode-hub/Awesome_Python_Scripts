
# Latitude - Longitude Pair Verifier

# imported necessary library
import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
import pandas as pd
import re


# created main window
window = Tk()
window.geometry("1000x700")
window.title("Latitude-Longitude Pair Verifier")

# ---------------------------------------------------------
frameCnt = 4
frames = [PhotoImage(file='Images/latlong.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

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
label.place(x = 120, y = 100)
window.after(0, update, 0)
# --------------------------------------------------------------------

data = pd.read_csv("world_location.csv")
country_code = data["country_code"].tolist()
country = data["country"].tolist()
latitude = data["latitude"].tolist()
longitude = data["longitude"].tolist()

# print(country_code)
# print(country)
# print(latitude)
# print(longitude)

# regex created for checking validity of pair of latitude and longitude
match_regex = re.compile(
    r"""
    \(                                # Starting bracket
    ([\+\-]?[1-9][0-9]*(?:\.[0-9]+)?) # First number
    ,[ ]                              # Comma space
    ([\+\-]?[1-9][0-9]*(?:\.[0-9]+)?) # Second number
    \)                                # Closing bracket
    """,
    re.VERBOSE
)

# to find the closest in the dataset
def closest(lst, K):
    return lst[min(range(len(lst)), key=lambda i: abs(lst[i] - K))]

# defined to verify the entry
def verify_entry():
    global s, lat1_country, lat1_country_code, long1_country, long1_country_code
    lat_entered = str(lat_entry.get())
    long_entered = str(long_entry.get())

    lat1 = float(lat_entry.get())
    long1 = float(long_entry.get())

    lat1_country = ""
    lat1_country_code = ""
    long1_country = ""
    long1_country_code = ""


    s = "(" + lat_entered + ", " + long_entered + ")"

    m = match_regex.match(s)
    if m is None:
        mbox.showinfo("Verify Status", "Verify Status :\n\nThe pair of Latitude and Longitude\n" + s + " is INVALID" )
        return
    X, Y = map(float, m.groups())
    if ((-90) <= X <= 90) and ((-180) <= Y <= 180):
        lat1c = closest(latitude, lat1)
        long1c = closest(longitude, long1)

        for i in range(0,len(latitude)):
            if latitude[i] == lat1c:
                lat1_country = country[i]
                lat1_country_code = country_code[i]
                break

        for i in range(0, len(longitude)):
            if longitude[i] == long1c:
                long1_country = country[i]
                long1_country_code = country_code[i]
                break

        mbox.showinfo("Verify Status", "Verify Status :\n\nThe pair of Latitude and Longitude\n" + s + " is VALID.")
    else:
        mbox.showerror("Verify Error", "Verify Status :\n\nThe pair of Latitude and Longitude\n" + s + " is INVALID" )

def locate_entry():
    if(lat1_country == "" or lat1_country_code == "" or long1_country ==""  or long1_country_code == ""):
        mbox.showerror("Locate Error", "The latitude and Longitude pair is not verified.")
    else:
        mbox.showinfo("Locate Status","The Country around this latitude  :  " + lat1_country + "\nThe Country Code is  :  " + lat1_country_code + "\n\nThe Country around this longitude  :  " + long1_country + "\nThe Country Code is  :  " + long1_country_code)


# top label
start1 = tk.Label(text = "Latitude-Longitude Pair Verifier", font=("Arial", 50), fg="magenta") # same way bg
start1.place(x = 40, y = 10)

# label for width
lat_lbl = tk.Label(text = "LATITUDE :  ", font=("Arial", 30), fg="brown") # same way bg
lat_lbl.place(x = 100, y = 470)

# label for height
long_lbl = tk.Label(text = "LONGITUDE :  ", font=("Arial", 30), fg="brown") # same way bg
long_lbl.place(x = 100, y = 540)

# Entry Box
lat_entry = Entry(window, font=("Arial", 25), fg='brown', bg="light yellow", borderwidth=3, width=12)
lat_entry.place(x=370, y=470)
long_entry = Entry(window, font=("Arial", 25), fg='brown', bg="light yellow", borderwidth=3, width=12)
long_entry.place(x=370, y=540)

# created verify button
verifyb = Button(window, text="VERIFY",command=verify_entry,font=("Arial", 25), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
verifyb.place(x =700 , y =490 )

# created locate button
locateb = Button(window, text="LOCATE",command=locate_entry,font=("Arial", 25), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
locateb.place(x =150 , y =605 )

# function defined to clear the entry
def clear_enrty():
    lat_entry.delete(0, END)
    long_entry.delete(0, END)

# created clear button
clearb = Button(window, text="CLEAR",command=clear_enrty,font=("Arial", 25), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
clearb.place(x =450 , y =605 )

# function for exiting
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

# created exit button
exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 25), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =730 , y =605 )


window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()