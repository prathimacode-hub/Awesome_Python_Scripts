

import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
import pandas as pd



window = Tk()
window.geometry("1000x700")
window.title("All India Trains")

# ---------------------------------------------------------
frameCnt = 4
frames = [PhotoImage(file='Images/trains.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

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

data = pd.read_csv("All_Indian_Trains.csv")
train_no = data['Train no.'].tolist()
train_name = data['Train name'].tolist()
train_start = data['Starts'].tolist()
train_end = data['Ends'].tolist()

train_name_distinct_set = set(train_name)
train_name_distinct_list = list(train_name_distinct_set)
train_name_distinct_list.sort()


def about_fun():
    mbox.showinfo("Indian Train Details", "Indian Railways (IR) is a statutory body under the jurisdiction of Ministry of Railways, Government of India that operates India's national railway system.\n\nIt manages the fourth-largest railway network in the world by size, with a route length of 67,956 km (42,226 mi) as of 31 March 2020. 45,881 km (28,509 mi) or 71% of all the broad-gauge routes are electrified with 25 kV 50 Hz AC electric traction as of 1 April 2020.\n\nThe first railway proposals for India were made in Madras in 1832. The India's first train, Red Hill Railway (built by Arthur Cotton to transport granite for road-building), ran from Red Hills to the Chintadripet bridge in Madras in 1837.")

def train_fun():
    selected_name = name_var.get()
    s1 = "Train Name  :  "
    s1 = s1 + str(selected_name)
    cnt = 0
    s = ""
    for i in range(0,len(train_name)):
        if(train_name[i] == selected_name):
            s = s + "\n\n1.)  Train No.  :  "
            s = s + str(train_no[i])
            s = s + "\n2.)  Starting Junction  :  "
            s = s + str(train_start[i])
            s = s + "\n3.)  Ending Junction  :  "
            s = s + str(train_end[i])
            cnt = cnt + 1

    s2 = "\n\nThere are  "
    s2 = s2 + str(cnt)
    s2 = s2 + "  trains."

    s = s1 + s2 + s
    # mbox.showinfo(selected_name + " Details", "Train Name  :  " + str(selected_name) + "\n\n1.)  Train No.  :  " + str(train_no[i]) + "\n\n2.)  Starting Junction  :  " + str(train_start[i]) + "\n\n3.)  Ending Junction  :  " + str(train_end[i]))
    mbox.showinfo(selected_name + " Details", s)

# top label
start1 = tk.Label(text = "ALL INDIAN TRAINS", font=("Arial", 50), fg="magenta",underline=0) # same way bg
start1.place(x = 180, y = 10)

# label for train name ---------------------------------------------------------------------------------
sel_label = tk.Label(text = "Train Name : ", font=("Arial", 30), fg="brown") # same way bg
sel_label.place(x = 100, y = 480)

# creating the drop down menu button for selecting train name
name_var = tk.StringVar()
# as icon size are really small, we defined the following 7 sizes
name_choices = train_name_distinct_list
name_menu = OptionMenu(window, name_var, *name_choices)
name_menu.config(font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3)
name_menu["menu"].config(font=("Arial", 10), bg = "light yellow", fg = "blue")
name_menu.place(x=350, y=480)
name_var.set("Andhra Pradesh Express") # size 1 is selected as by default, and we can

aboutb = Button(window, text="ABOUT",command=about_fun,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
aboutb.place(x =150 , y =580 )

trainb = Button(window, text="TRAIN",command=train_fun,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
trainb.place(x =360 , y =580 )

def reset_label():
    name_var.set("Andhra Pradesh Express")

resetb = Button(window, text="RESET",command=reset_label,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
resetb.place(x =550 , y =580 )


def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 20), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =730 , y =580 )


window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()