
# Time Zone Converter

import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
from PIL import Image, ImageTk
import pandas as pd


window = Tk()
window.geometry("1000x700")
window.title("TIME ZONE CONVERTER")

# ---------------------------------------------------------
frameCnt = 3
frames = [PhotoImage(file='Images/time.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

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
label.place(x = 160, y = 100)
window.after(0, update, 0)
# --------------------------------------------------------------------

data = pd.read_csv("conversion.csv")
first_list = data["first"].tolist()
second_list = data["second"].tolist()
hour_list = data["h"].tolist()
min_list = data["m"].tolist()
fullfornm_list = data["fullform"].tolist()

def get_fullform():
    s = ""
    for i in range(0, len(second_list)):
        s = s + second_list[i]
        s = s + "  -  "
        s = s + fullfornm_list[i]
        s = s + "\n"
    mbox.showinfo("Full Form", s)

def convert_time():
    hour = hour_var.get()
    min = min_var.get()
    first1 = first_var.get()
    second1 = second_var.get()
    hour1 = hour
    min1 = min

    # went to GMT
    for i in range(0,len(second_list)):
        if second_list[i] == first1:
            hour = (hour - hour_list[i]) % 24
            min = (min - min_list[i]) % 60

    # went from GMT
    for i in range(0,len(second_list)):
        if second_list[i] == second1:
            hour = (hour + hour_list[i]) % 24
            min = (min + min_list[i]) % 60

    mbox.showinfo(first1 + " to " + second1, "Time in " + first1 + " :-\t" + str(hour1) + "  :  " + str(min1) + "\n\nTime in " + second1 + " :-\t" + str(hour) + "  :  " + str(min))



# top label
start1 = tk.Label(text = "TIME ZONE CONVERTER", font=("Arial", 50), fg="magenta",underline=0) # same way bg
start1.place(x = 100, y = 10)

# label for entering time ---------------------------------------------------------------------------------
time1 = tk.Label(text = "Enter Time here : ", font=("Arial", 30), fg="brown") # same way bg
time1.place(x = 150, y = 420)

# creating the drop down menu button for selectng hour
hour_var = tk.IntVar()
# as icon size are really small, we defined the following 7 sizes
hour_choices = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
hour_menu = OptionMenu(window, hour_var, *hour_choices)
hour_menu.config(font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3)
hour_menu["menu"].config(font=("Arial", 10), bg = "light yellow", fg = "blue")
hour_menu.place(x=480, y=420)
hour_var.set(0) # size 1 is selected as by default, and we can

# label for :
colon1 = tk.Label(text = ":", font=("Arial", 30), fg="brown") # same way bg
colon1.place(x = 565, y = 420)

# creating the drop down menu button for selectng hour
min_var = tk.IntVar()
# as icon size are really small, we defined the following 7 sizes
min_choices = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59]
min_menu = OptionMenu(window, min_var, *min_choices)
min_menu.config(font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3)
min_menu["menu"].config(font=("Arial", 10), bg = "light yellow", fg = "blue")
min_menu.place(x=600, y=420)
min_var.set(0) # size 1 is selected as by default, and we can
# -------------------------------------------------------------------------------------

# label for entering time ---------------------------------------------------------------------------------
time1 = tk.Label(text = "Select Conversion : ", font=("Arial", 30), fg="brown") # same way bg
time1.place(x = 150, y = 500)

# creating the drop down menu button for selectng hour
first_var = tk.StringVar()
# as icon size are really small, we defined the following 7 sizes
first_choices = ["GMT", "UTC", "ECT", "EET", "ART", "EAT", "MET", "NET", "PLT", "IST", "BST", "VST", "CTT", "JST", "ACT", "AET","SST", "NST", "MIT", "HST", "AST", "PST", "PNT", "MST", "CST", "EST", "IET", "PRT", "CNT", "AGT", "BET", "CAT"]
first_choices.sort()
first_menu = OptionMenu(window, first_var, *first_choices)
first_menu.config(font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3)
first_menu["menu"].config(font=("Arial", 10), bg = "light yellow", fg = "blue")
first_menu.place(x=500, y=500)
first_var.set("GMT") # size 1 is selected as by default, and we can

# label for :
colon1 = tk.Label(text = "to", font=("Arial", 30), fg="brown") # same way bg
colon1.place(x = 620, y = 500)

# creating the drop down menu button for selectng hour
second_var = tk.StringVar()
# as icon size are really small, we defined the following 7 sizes
second_choices = ["GMT", "UTC", "ECT", "EET", "ART", "EAT", "MET", "NET", "PLT", "IST", "BST", "VST", "CTT", "JST", "ACT", "AET","SST", "NST", "MIT", "HST", "AST", "PST", "PNT", "MST", "CST", "EST", "IET", "PRT", "CNT", "AGT", "BET", "CAT"]
second_choices.sort()
second_menu = OptionMenu(window, second_var, *second_choices)
second_menu.config(font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3)
second_menu["menu"].config(font=("Arial", 10), bg = "light yellow", fg = "blue")
second_menu.place(x=680, y=500)
second_var.set("GMT") # size 1 is selected as by default, and we can
# -------------------------------------------------------------------------------------

fullformb = Button(window, text="FULL FORM",command=get_fullform,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
fullformb.place(x =150 , y =600 )

convertb = Button(window, text="CONVERT",command=convert_time,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
convertb.place(x =360 , y =600 )

def reset_label():
    hour_var.set(0)
    min_var.set(0)
    first_var.set("GMT")
    second_var.set("GMT")

resetb = Button(window, text="RESET",command=reset_label,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
resetb.place(x =550 , y =600 )


def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 20), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =700 , y =600 )


window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()