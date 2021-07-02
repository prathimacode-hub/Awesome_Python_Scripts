
# Direct Flight Route Finder

import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
import pandas as pd


window = Tk()
window.geometry("1000x700")
window.title("Direct Flight Route Finder")

# ---------------------------------------------------------
frameCnt = 3
frames = [PhotoImage(file='Images/flight.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

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
label.place(x = 220, y = 100)
window.after(0, update, 0)
# --------------------------------------------------------------------

data = pd.read_csv("flight1.csv")
source_airport_list = data["source_airport"].tolist()
source_airport_id_list = data["source_airport_id"].tolist()
destination_airport_list = data["destination_airport"].tolist()
destination_airport_id_list = data["destination_airport_id"].tolist()

# print(source_airport_list)
# print(source_airport_id_list)
# print(destination_airport_list)
# print(destination_airport_id_list)


def find_route():
    src = first_var.get()
    dest = second_var.get()
    i_list = []
    j_list = []
    for i in range(0, len(source_airport_list)):
        if(source_airport_list[i] == src):
            i_list.append(i)

    for j in range(0, len(destination_airport_list)):
        if(destination_airport_list[j] == dest):
            j_list.append(j)

    # print(i_list)
    # print(j_list)
    for i1 in i_list:
        for j1 in j_list:
            if(i1==j1):
                mbox.showinfo("Find Success","Yes, There is a flight route between " + src + " and  " + dest + "\n\nFor this route, Id are :\n" + src + "  :  " +source_airport_id_list[i1] + "\n" + dest + "  :  " + destination_airport_id_list[j1])
                return

    mbox.showinfo("Find Failure", "There is no flight route between " + src + " and " + dest)

# top label
start1 = tk.Label(text = "DIRECT FLIGHT ROUTE FINDER", font=("Arial", 45), fg="magenta",underline=0) # same way bg
start1.place(x = 50, y = 10)
#
# label for entering time ---------------------------------------------------------------------------------
time1 = tk.Label(text = "Select src. airport : ", font=("Arial", 30), fg="brown") # same way bg
time1.place(x = 100, y = 420)

# creating the drop down menu button for selectng hour
first_var = tk.StringVar()
# as icon size are really small, we defined the following 7 sizes
first_choices = source_airport_list
first_menu = OptionMenu(window, first_var, *first_choices)
first_menu.config(font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3)
first_menu["menu"].config(font=("Arial", 10), bg = "light yellow", fg = "blue")
first_menu.place(x=200, y=500)
first_var.set("AER") # size 1 is selected as by default, and we can

# label for :
colon1 = tk.Label(text = "Select dest. airport", font=("Arial", 30), fg="brown") # same way bg
colon1.place(x = 565, y = 420)

# creating the drop down menu button for selectng hour
second_var = tk.StringVar()
# as icon size are really small, we defined the following 7 sizes
second_choices = destination_airport_list
second_menu = OptionMenu(window, second_var, *second_choices)
second_menu.config(font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3)
second_menu["menu"].config(font=("Arial", 10), bg = "light yellow", fg = "blue")
second_menu.place(x=650, y=500)
second_var.set("KZN") # size 1 is selected as by default, and we can


findb = Button(window, text="FIND",command=find_route,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
findb.place(x =200 , y =600 )

def reset_label():
    first_var.set("AER")
    second_var.set("KZN")

resetb = Button(window, text="RESET",command=reset_label,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
resetb.place(x =420 , y =600 )


def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 20), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =660 , y =600 )


window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()