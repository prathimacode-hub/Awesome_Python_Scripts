

# imported all the necessary python libraries
import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
import pandas as pd
import webbrowser


# created a main window for application
window = Tk()
window.geometry("1000x700")
window.title("World Companies Detailer")

# ------------------ this is for adding gif image in the main window of application ---------------------------------------
frameCnt = 5
frames = [PhotoImage(file='Images/company.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

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

# reading the data from the csv file
data = pd.read_csv("world_companies.csv")
Global_Rank = data['Global Rank'].tolist()
Company_Name = data['Company'].tolist()
Sales = data['Sales ($billion)'].tolist()
Profits = data['Profits ($billion)'].tolist()
Assets= data['Assets ($billion)'].tolist()
Market_Value = data['Market Value ($billion)'].tolist()
Country = data['Country'].tolist()
Continent = data['Continent'].tolist()
Latitude = data['Latitude'].tolist()
Longitude = data['Longitude'].tolist()

#Define a callback function
def callback(url):
   webbrowser.open_new_tab(url)

def details():
    selected_name = name_var.get()
    for i in range(0,len(Company_Name)):
        if(Company_Name[i] == selected_name):
            mbox.showinfo(selected_name + " Details", "Company Name  :  " + str(selected_name) + "\n\n1.)  Global Rank  :  " + str(Global_Rank[i]) + "\n\n2.)  Sales ($billion)  :  " + str(Sales[i]) + "\n\n3.)  Profits ($billion)  :  " + str(Profits[i]) + "\n\n4.)  Assets ($billion)  :  " + str(Assets[i]) + "\n\n5.)  Market Value ($billion)  :  " + str(Market_Value[i]) + "\n\n6.)  Country  :  " + str(Country[i]) + "\n\n7.)  Continent  :  " + str(Continent[i]) + "\n\n8.)  Latitude  :  " + str(Latitude[i]) + "\n\n9.)  Longitude  :  " + str(Longitude[i]))


# top label
start1 = tk.Label(text = "WORLD COMPANIES DETAILER", font=("Arial", 40), fg="magenta",underline=0) # same way bg
start1.place(x = 100, y = 10)

# label for company name ---------------------------------------------------------------------------------
sel_label = tk.Label(text = "Company Name : ", font=("Arial", 30), fg="brown") # same way bg
sel_label.place(x = 120, y = 500)

# creating the drop down menu button for selecting food
name_var = tk.StringVar()
# as icon size are really small, we defined the following 7 sizes
name_choices = Company_Name
# food_choices.sort()
name_menu = OptionMenu(window, name_var, *name_choices)
name_menu.config(font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3)
name_menu["menu"].config(font=("Arial", 10), bg = "light yellow", fg = "blue")
name_menu.place(x=450, y=500)
name_var.set("Reliance Industries") # size 1 is selected as by default, and we can

# livenews button
livenewsb = Button(window, text="LIVE NEWS",command=lambda:callback("https://www.bbc.com/news/business/companies"),font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
livenewsb.place(x =100 , y =600 )

# details button
infob = Button(window, text="DETAILS",command=details,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
infob.place(x =350 , y =600 )

# reset function
def reset_label():
    name_var.set("Reliance Industries")

resetb = Button(window, text="RESET",command=reset_label,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
resetb.place(x =560 , y =600 )

# exit function
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

# exit button
exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 20), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =750 , y =600 )


window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()