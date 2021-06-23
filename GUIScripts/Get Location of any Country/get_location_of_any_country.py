
# Time Zone Converter

import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
import pandas as pd



window = Tk()
window.geometry("1000x700")
window.title("COUNTRY LOCATION")

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
label.place(x = 130, y = 100)
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

def get_location_code():
    code = code_var.get()
    for i in range(0, len(country_code)):
        if(country_code[i] == code):
            mbox.showinfo("Location By Code", "Location of Country with code : "+ str(code) + "\n\nLatitude  :  " + str(latitude[i]) + "\n\nLongitude : " + str(longitude[i]))

def get_location_country():
    country1 = country_var.get()
    for i in range(0, len(country)):
        if(country[i] == country1):
            mbox.showinfo("Location By Country", "Location of Country with Name : "+ str(country1) + "\n\nLatitude  :  " + str(latitude[i]) + "\n\nLongitude : " + str(longitude[i]))


# top label
start1 = tk.Label(text = "COUNTRY  LOCATION", font=("Arial", 50), fg="magenta",underline=0) # same way bg
start1.place(x = 150, y = 10)

# label for country code ---------------------------------------------------------------------------------
codelbl = tk.Label(text = "Get By Country Code : ", font=("Arial", 30), fg="brown") # same way bg
codelbl.place(x = 200, y = 460)

# creating the drop down menu button for selectng hour
code_var = tk.StringVar()
# as icon size are really small, we defined the following 7 sizes
# first_choices = ["GMT", "UTC", "ECT", "EET", "ART", "EAT", "MET", "NET", "PLT", "IST", "BST", "VST", "CTT", "JST", "ACT", "AET","SST", "NST", "MIT", "HST", "AST", "PST", "PNT", "MST", "CST", "EST", "IET", "PRT", "CNT", "AGT", "BET", "CAT"]
code_choices = country_code
# first_choices.sort()
code_menu = OptionMenu(window, code_var, *code_choices)
code_menu.config(font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3)
code_menu["menu"].config(font=("Arial", 10), bg = "light yellow", fg = "blue")
code_menu.place(x=610, y=460)
code_var.set("IN") # size 1 is selected as by default, and we can

# label for country code ---------------------------------------------------------------------------------
countrylbl = tk.Label(text = "Get By Country Name : ", font=("Arial", 30), fg="brown") # same way bg
countrylbl.place(x = 150, y = 530)

# creating the drop down menu button for selectng hour
country_var = tk.StringVar()
# as icon size are really small, we defined the following 7 sizes
# first_choices = ["GMT", "UTC", "ECT", "EET", "ART", "EAT", "MET", "NET", "PLT", "IST", "BST", "VST", "CTT", "JST", "ACT", "AET","SST", "NST", "MIT", "HST", "AST", "PST", "PNT", "MST", "CST", "EST", "IET", "PRT", "CNT", "AGT", "BET", "CAT"]
country_choices = country
# first_choices.sort()
country_menu = OptionMenu(window, country_var, *country_choices)
country_menu.config(font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3)
country_menu["menu"].config(font=("Arial", 10), bg = "light yellow", fg = "blue")
country_menu.place(x=570, y=530)
country_var.set("India") # size 1 is selected as by default, and we can

getb1 = Button(window, text="BY CODE",command=get_location_code,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
getb1.place(x =100 , y =600 )

getb2 = Button(window, text="BY COUNTRY",command=get_location_country,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
getb2.place(x =300 , y =600 )

def reset_label():
    code_var.set("IN")
    country_var.set("India")

resetb = Button(window, text="RESET",command=reset_label,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
resetb.place(x =560 , y =600 )


def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 20), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =730 , y =600 )


window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()