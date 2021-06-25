
# Indian Food Information

import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
import pandas as pd



window = Tk()
window.geometry("1000x700")
window.title("SpaceX Mission Detailer")

# ---------------------------------------------------------
frameCnt = 3
frames = [PhotoImage(file='Images/spacex.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

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

data = pd.read_csv("spaceX_data.csv")
flight_number = data['Flight Number'].tolist()
launch_date = data['Launch Date'].tolist()
launch_time = data['Launch Time'].tolist()
launch_site = data['Launch Site'].tolist()
vehicle_type = data['Vehicle Type'].tolist()
payload_name = data['Payload Name'].tolist()
payload_type = data['Payload Type'].tolist()
payload_mass = data['Payload Mass (kg)'].tolist()
payload_orbit = data['Payload Orbit'].tolist()
customer_name = data['Customer Name'].tolist()
customer_type = data['Customer Type'].tolist()
customer_country = data['Customer Country'].tolist()
mission_outcome = data['Mission Outcome'].tolist()
failure_reason = data['Failure Reason'].tolist()
landing_type = data['Landing Type'].tolist()
landing_outcome = data['Landing Outcome'].tolist()
year_list = data['Year'].tolist()

# print(len(flight_number))
# print(launch_date)
# print(launch_time)
# print(launch_site)
# print(vehicle_type)
# print(payload_name)
# print(payload_type)
# print(payload_mass)
# print(payload_orbit)
# print(customer_name)
# print(customer_type)
# print(customer_country)
# print(mission_outcome)
# print(failure_reason)
# print(landing_type)
# print(landing_outcome)
# print(year_list)


def get_status():
    mbox.showinfo("SPACEX", "SpaceX :\n\nSpace Exploration Technologies Corp. is an American aerospace manufacturer, space transportation services and communications company headquartered in Hawthorne, California.\n\nSpaceX was founded in 2002 by Elon Musk with the goal of reducing space transportation costs to enable the colonization of Mars.")

def details():
    mission_list = []
    selected_year = year_var.get()
    cnt = 0
    for i in range(0,len(year_list)):
        # print(i,food_name[i], selected_food)
        s = ""
        if(year_list[i] == selected_year):
            cnt = cnt + 1
            s = str(cnt) + ".)  Flight Number  :  " + str(flight_number[i]) + "\n      Launch Date  :  " + str(launch_date[i]) + "\n      Launch Time  :  " + str(launch_time[i]) + "\n      Launch Site  :  " + str(launch_site[i]) + "\n      Vehicle Type  :  " + str(vehicle_type[i]) + "\n      Payload Name  :  " + str(payload_name[i]) + "\n      Payload Type  :  " + str(payload_type[i]) + "\n      Payload Mass (in kg.)  :  " + str(payload_mass[i]) + "\n      Payload Orbit  :  " + str(payload_orbit[i]) + "\n      Customer Name  :  " + str(customer_name[i]) + "\n      Customer Type  :  " + str(customer_type[i]) + "\n      Customer Country  :  " + str(customer_country[i]) + "\n      Mission Outcome  :  " + str(mission_outcome[i]) + "\n      Failure Reasons  :  " + str(failure_reason[i]) + "\n      Landing Type  :  " + str(landing_type[i]) + "\n      Landing Outcome  :  " + str(landing_outcome[i])
            mission_list.append(s)

    ans = "YEAR  : " + str(selected_year)
    ans = ans + "\n\n"
    ans =  ans + "No of mission  :  "
    ans = ans + str(len(mission_list))
    ans = ans + "\n\n"


    for i in mission_list:
        ans = ans + i
        ans = ans + "\n\n"

    mbox.showinfo('Year ' + str(selected_year) + " Mission Details", ans)

# top label
start1 = tk.Label(text = "SPACEX MISSION DETAILER", font=("Arial", 50), fg="magenta",underline=0) # same way bg
start1.place(x = 50, y = 10)

# label for country code ---------------------------------------------------------------------------------
sel_label = tk.Label(text = "Select  Year : ", font=("Arial", 30), fg="brown") # same way bg
sel_label.place(x = 200, y = 450)

# creating the drop down menu button for selecting food
year_var = tk.IntVar()
# as icon size are really small, we defined the following 7 sizes
year_choices = [2006,2007,2008,2009,2010, 2011,2012,2013,2014,2015,2016,2017]
# food_choices.sort()
year_menu = OptionMenu(window, year_var, *year_choices)
year_menu.config(font=("Arial", 25), bg = "light green", fg = "blue", borderwidth=3)
year_menu["menu"].config(font=("Arial", 20), bg = "light yellow", fg = "blue")
year_menu.place(x=480, y=440)
year_var.set(2006) # size 1 is selected as by default, and we can

indiab = Button(window, text="SPACEX",command=get_status,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
indiab.place(x =150 , y =570 )

infob = Button(window, text="DETAILS",command=details,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
infob.place(x =350 , y =570 )

def reset_label():
    year_var.set("Gulab jamun")

resetb = Button(window, text="RESET",command=reset_label,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
resetb.place(x =550 , y =570 )


def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 20), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =730 , y =570 )


window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()