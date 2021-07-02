

import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
import pandas as pd



window = Tk()
window.geometry("1000x700")
window.title("Indian University NIRF Ranking")

# ---------------------------------------------------------
frameCnt = 4
frames = [PhotoImage(file='Images/university.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

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
label.place(x = 200, y = 100)
window.after(0, update, 0)
# --------------------------------------------------------------------

data = pd.read_csv("engineering.csv")
institute_id = data['institute_id'].tolist()
name = data['name'].tolist()
tlr = data['tlr'].tolist()
rpc = data['rpc'].tolist()
go = data['go'].tolist()
oi = data['oi'].tolist()
perception = data['perception'].tolist()
city = data['city'].tolist()
state = data['state'].tolist()
rank = data['rank'].tolist()


# print(len(name))
# print(institute_id)
# print(tlr)
# print(rpc)
# print(go)
# print(oi)
# print(perception)
# print(city)
# print(state)
# print(rank)

def nirf_details():
    mbox.showinfo("NIRF Details", "The National Institutional Ranking Framework (NIRF) was approved by the MHRD and launched by Honourable Minister of Human Resource Development on 29th September 2015.\n\nThis framework outlines a methodology to rank institutions across the country. The methodology draws from the overall recommendations broad understanding arrived at by a Core Committee set up by MHRD, to identify the broad parameters for ranking various universities and institutions.\n\nThe parameters broadly cover “Teaching, Learning and Resources,” “Research and Professional Practices,” “Graduation Outcomes,” “Outreach and Inclusivity,” and “Perception”.")

def details():
    selected_name = name_var.get()
    for i in range(0,len(name)):
        if(name[i] == selected_name):
            mbox.showinfo(selected_name + " Details", "Name  :  " + str(selected_name) + "\n\n1.)  Rank  :  " + str(rank[i]) + "\n2.)  Institute ID  :  " + str(institute_id[i]) + "\n3.)  Teaching, Learning and Resources (TLR)  :  " + str(tlr[i]) + "\n4.)  Research and Professional Practice (RPC)  :  " + str(rpc[i]) + "\n5.)  Graduation Outcomes (GO)  :  " + str(go[i]) + "\n6.)  Outreach and Inclusivity (OI)  :  " + str(oi[i]) + "\n7.)  Peer Perception  :  " + str(perception[i]) + "\n8.)  City  :  " + str(city[i]) + "\n9.)  State  :  " + str(state[i]))


# top label
start1 = tk.Label(text = "INDIAN UNIVERSITY NIRF RANKING", font=("Arial", 40), fg="magenta",underline=0) # same way bg
start1.place(x = 50, y = 10)

# label for universitry name ---------------------------------------------------------------------------------
sel_label = tk.Label(text = "University Name : ", font=("Arial", 30), fg="brown") # same way bg
sel_label.place(x = 80, y = 480)

# creating the drop down menu button for selecting food
name_var = tk.StringVar()
# as icon size are really small, we defined the following 7 sizes
name_choices = name
# food_choices.sort()
name_menu = OptionMenu(window, name_var, *name_choices)
name_menu.config(font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3)
name_menu["menu"].config(font=("Arial", 10), bg = "light yellow", fg = "blue")
name_menu.place(x=400, y=480)
name_var.set("Indian Institute of Technology Madras") # size 1 is selected as by default, and we can

nirfb = Button(window, text="ABOUT",command=nirf_details,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
nirfb.place(x =150 , y =600 )

infob = Button(window, text="NIRF RANK",command=details,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
infob.place(x =320 , y =600 )

def reset_label():
    name_var.set("Indian Institute of Technology Madras")

resetb = Button(window, text="RESET",command=reset_label,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
resetb.place(x =550 , y =600 )


def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 20), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =730 , y =600 )


window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()