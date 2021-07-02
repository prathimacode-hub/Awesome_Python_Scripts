
# Bermuda Triangle Incidents

# imported necessary library
import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
import json

# created a main window
window = Tk()
window.geometry("1000x700")
window.title("Bermuda Triangle Incidents")

# --------------------- for showing gif image on main window ------------------------------------
frameCnt = 7
frames = [PhotoImage(file='Images/bermuda.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

cnt = 0.0
def update(ind):
    global cnt
    frame = frames[ind]
    if(cnt >= 1.0):
        cnt = 0.0
    cnt = cnt + 0.1
    # cnt = int(cnt)
    ind += int(cnt)
    # print(cnt, ind, frameCnt)
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    window.after(100, update, ind)
label = Label(window)
label.place(x = 130, y = 80)
window.after(0, update, 0)
# --------------------------------------------------------------------

# data loaded from json file
data1 = json.load(open("bermuda_incidents.json"))
year = data1["year"]
date = data1["date"]
where = data1["where"]
description = data1["description"]

# unique year were shown in the list of OptionMenu
year1 = list(set(year))
year1.sort()

# for Bermuda button
def get_status():
    mbox.showinfo("BERMUDA TRIANGLE", "Bermuda Triangle : \n\nThe Bermuda Triangle, also known as the Devil's Triangle, is a loosely defined region in the western part of the North Atlantic Ocean where a number of aircraft and ships are said to have disappeared under mysterious circumstances. Most reputable sources dismiss the idea that there is any mystery.\n\nBermuda Triangle, section of the North Atlantic Ocean off North America in which more than 50 ships and 20 airplanes are said to have mysteriously disappeared.\n\nThe term “Bermuda Triangle” was first used by Vincent Gaddis in 1964 in his article published in Argosy magazine.")

# for details button
def get_info():
    selected_year = year_var.get()
    s1 = "YEAR  :  "
    s1 = s1 + str(selected_year)
    cnt = 0
    s = ""
    for i in range(0,len(year)):
        if(year[i] == selected_year):
            s = s + "\n\n\n1.)  Date  :  "
            s = s + str(date[i])
            s = s + "\n\n2.)  Where it happened  :  "
            s = s + str(where[i])
            s = s + "\n\n3.)  Description (What Happened)  :  "
            s = s + str(description[i])
            cnt = cnt + 1

    s2 = "\n\nThere are  "
    s2 = s2 + str(cnt)
    s2 = s2 + "  incidents."

    s = s1 + s2 + s
    mbox.showinfo(selected_year + " Incidents", s)


# top label
start1 = tk.Label(text = "BERMUDA TRIANGLE INCIDENTS", font=("Arial", 40), fg="magenta",underline=0) # same way bg
start1.place(x = 80, y = 10)

# label for country code ---------------------------------------------------------------------------------
sel_label = tk.Label(text = "Select Incident Year  :  ", font=("Arial", 30), fg="brown") # same way bg
sel_label.place(x = 200, y = 540)

# creating the drop down menu button for selecting country code
year_var = tk.StringVar()
# as icon size are really small, we defined the following 7 sizes
year_choices = year1
year_menu = OptionMenu(window, year_var, *year_choices)
year_menu.config(font=("Arial", 25), bg = "light green", fg = "blue", borderwidth=3)
year_menu["menu"].config(font=("Arial", 10), bg = "light yellow", fg = "blue")
year_menu.place(x=600, y=530)
year_var.set("1492") # size 1 is selected as by default, and we can

# created BERMUDA button
indiab = Button(window, text="BERMUDA",command=get_status,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
indiab.place(x =100 , y =610 )

# Created DETAILS button
infob = Button(window, text="DETAILS",command=get_info,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
infob.place(x =360 , y =610 )

# function defined to reset the Option Menu
def reset_label():
    year_var.set("1492")

# created reset button
resetb = Button(window, text="RESET",command=reset_label,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
resetb.place(x =600 , y =610 )


# function defined to exit
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

# created exit button
exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 20), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =800 , y =610 )

window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()