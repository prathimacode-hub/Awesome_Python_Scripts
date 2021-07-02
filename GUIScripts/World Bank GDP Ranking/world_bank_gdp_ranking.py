
# World Bank GDP Ranking

import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
import pandas as pd



window = Tk()
window.geometry("1000x700")
window.title("World Bank GDP Ranking")

# ---------------------------------------------------------
frameCnt = 4
frames = [PhotoImage(file='Images/gdp.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

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
label.place(x = 150, y = 100)
window.after(0, update, 0)
# --------------------------------------------------------------------

data = pd.read_csv("gdp.csv")
country_code = data['Country_Code'].tolist()
rank = data['Ranking'].tolist()
economy = data['Economy'].tolist()
usdollars = data['US dollars'].tolist()

# print(country_code)
# print(rank)
# print(economy)
# print(usdollars)

def get_status():
    mbox.showinfo("INDIA", "India is among the first 5 largest economy in the world.\n\nTHE FIRST 5 LARGEST ECONOMY IN THE WORLD :\n1.)  United States\n2.)  China\n3.)  Japan\n4.)  Germany\n5.)  India")

def get_info():
    selected_code = code_var.get()
    for i in range(0,len(country_code)):
        # print(i,food_name[i], selected_food)
        if(country_code[i] == selected_code):
            mbox.showinfo(selected_code + " GDP RANKING", "Rank  :  " + str(rank[i]) + "\n\nEconomy  :  " + economy[i] + "\n\nUS Dollars  :  " + usdollars[i] + " millions")
            return

# top label
start1 = tk.Label(text = "WORLD BANK GDP RANK", font=("Arial", 50), fg="magenta",underline=0) # same way bg
start1.place(x = 100, y = 10)

# label for country code ---------------------------------------------------------------------------------
sel_label = tk.Label(text = "Select Country Code : ", font=("Arial", 30), fg="brown") # same way bg
sel_label.place(x = 150, y = 490)

# creating the drop down menu button for selecting country code
code_var = tk.StringVar()
# as icon size are really small, we defined the following 7 sizes
code_choices = country_code
code_menu = OptionMenu(window, code_var, *code_choices)
code_menu.config(font=("Arial", 25), bg = "light green", fg = "blue", borderwidth=3)
code_menu["menu"].config(font=("Arial", 10), bg = "light yellow", fg = "blue")
code_menu.place(x=550, y=480)
code_var.set("IND") # size 1 is selected as by default, and we can
#
indiab = Button(window, text="INDIA",command=get_status,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
indiab.place(x =150 , y =600 )

infob = Button(window, text="GDP RANK",command=get_info,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
infob.place(x =300 , y =600 )

def reset_label():
    code_var.set("IND")

resetb = Button(window, text="RESET",command=reset_label,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
resetb.place(x =510 , y =600 )


def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 20), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =680 , y =600 )


window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()