
# Absolute Time Delta

# imported necessary library
import tkinter as tk
import tkinter.messagebox as mbox
from datetime import datetime
from tkinter import *

# created main window
window = Tk()
window.geometry("1000x750")
window.title("Absolute Time Delta")


# top label
start1 = tk.Label(text = "ABSOLUTE  TIME  DELTA", font=("Arial", 45), fg="magenta") # same way bg
start1.place(x = 120, y = 10)

# time1 label
time1 = tk.Label(text = "Time 1", font=("Arial", 30), fg="green") # same way bg
time1.place(x = 400, y = 80)

# time2 label
time1 = tk.Label(text = "Time 2", font=("Arial", 30), fg="green") # same way bg
time1.place(x = 700, y = 80)

# Day label
day_lbl = tk.Label(text = "Day :", font=("Arial", 30), fg="brown") # same way bg
day_lbl.place(x = 50, y = 140)
# Day Entry Box
day_time1_entry = Entry(window, font=("Arial", 25), fg='orange', bg="light yellow", borderwidth=3, width=13)
day_time1_entry.place(x=350, y=140)
day_time2_entry = Entry(window, font=("Arial", 25), fg='orange', bg="light yellow", borderwidth=3, width=13)
day_time2_entry.place(x=650, y=140)

# Date label
date_lbl = tk.Label(text = "Date :", font=("Arial", 30), fg="brown") # same way bg
date_lbl.place(x = 50, y = 200)
# Date Entry Box
date_time1_entry = Entry(window, font=("Arial", 25), fg='orange', bg="light yellow", borderwidth=3, width=13)
date_time1_entry.place(x=350, y=200)
date_time2_entry = Entry(window, font=("Arial", 25), fg='orange', bg="light yellow", borderwidth=3, width=13)
date_time2_entry.place(x=650, y=200)

# Month label
month_lbl = tk.Label(text = "Month :", font=("Arial", 30), fg="brown") # same way bg
month_lbl.place(x = 50, y = 260)
# Month Entry Box
month_time1_entry = Entry(window, font=("Arial", 25), fg='orange', bg="light yellow", borderwidth=3, width=13)
month_time1_entry.place(x=350, y=260)
month_time2_entry = Entry(window, font=("Arial", 25), fg='orange', bg="light yellow", borderwidth=3, width=13)
month_time2_entry.place(x=650, y=260)

# Year label
year_lbl = tk.Label(text = "Year :", font=("Arial", 30), fg="brown") # same way bg
year_lbl.place(x = 50, y = 320)
# Year Entry Box
year_time1_entry = Entry(window, font=("Arial", 25), fg='orange', bg="light yellow", borderwidth=3, width=13)
year_time1_entry.place(x=350, y=320)
year_time2_entry = Entry(window, font=("Arial", 25), fg='orange', bg="light yellow", borderwidth=3, width=13)
year_time2_entry.place(x=650, y=320)

# Hour label
hour_lbl = tk.Label(text = "Hour :", font=("Arial", 30), fg="brown") # same way bg
hour_lbl.place(x = 50, y = 380)
# Hour Entry Box
hour_time1_entry = Entry(window, font=("Arial", 25), fg='orange', bg="light yellow", borderwidth=3, width=13)
hour_time1_entry.place(x=350, y=380)
hour_time2_entry = Entry(window, font=("Arial", 25), fg='orange', bg="light yellow", borderwidth=3, width=13)
hour_time2_entry.place(x=650, y=380)

# Minute label
minute_lbl = tk.Label(text = "Minute :", font=("Arial", 30), fg="brown") # same way bg
minute_lbl.place(x = 50, y = 440)
# Minute Entry Box
minute_time1_entry = Entry(window, font=("Arial", 25), fg='orange', bg="light yellow", borderwidth=3, width=13)
minute_time1_entry.place(x=350, y=440)
minute_time2_entry = Entry(window, font=("Arial", 25), fg='orange', bg="light yellow", borderwidth=3, width=13)
minute_time2_entry.place(x=650, y=440)

# Second label
second_lbl = tk.Label(text = "Second :", font=("Arial", 30), fg="brown") # same way bg
second_lbl.place(x = 50, y = 500)
# Second Entry Box
second_time1_entry = Entry(window, font=("Arial", 25), fg='orange', bg="light yellow", borderwidth=3, width=13)
second_time1_entry.place(x=350, y=500)
second_time2_entry = Entry(window, font=("Arial", 25), fg='orange', bg="light yellow", borderwidth=3, width=13)
second_time2_entry.place(x=650, y=500)

# Zone label
zone_lbl = tk.Label(text = "Time Zone :", font=("Arial", 30), fg="brown") # same way bg
zone_lbl.place(x = 50, y = 560)
# Day Entry Box
zone_time1_entry = Entry(window, font=("Arial", 25), fg='orange', bg="light yellow", borderwidth=3, width=13)
zone_time1_entry.place(x=350, y=560)
zone_time2_entry = Entry(window, font=("Arial", 25), fg='orange', bg="light yellow", borderwidth=3, width=13)
zone_time2_entry.place(x=650, y=560)

# function defined for finding the delta
def get_delta():
    global valid
    time1 = str(day_time1_entry.get()) + " " + str(date_time1_entry.get()) + " " + str(month_time1_entry.get()) + " " + str(year_time1_entry.get()) + " " + str(hour_time1_entry.get()) + ":" + str(minute_time1_entry.get()) + ":" + str(second_time1_entry.get()) + " " + str(zone_time1_entry.get())
    time2 = str(day_time2_entry.get()) + " " + str(date_time2_entry.get()) + " " + str(month_time2_entry.get()) + " " + str(year_time2_entry.get()) + " " + str(hour_time2_entry.get()) + ":" + str(minute_time2_entry.get()) + ":" + str(second_time2_entry.get()) + " " + str(zone_time2_entry.get())
    valid = True
    day1 = str(day_time1_entry.get())
    date1 = int(date_time1_entry.get())
    month1 = str(month_time1_entry.get())
    year1 = int(year_time1_entry.get())
    hour1 = int(hour_time1_entry.get())
    minute1 = int(minute_time1_entry.get())
    second1 = int(second_time1_entry.get())

    day2 = str(day_time2_entry.get())
    date2 = int(date_time2_entry.get())
    month2 = str(month_time2_entry.get())
    year2 = int(year_time2_entry.get())
    hour2 = int(hour_time2_entry.get())
    minute2 = int(minute_time2_entry.get())
    second2 = int(second_time2_entry.get())

    if((day1!="Sun" and day1!="Mon" and day1!="Tue" and day1!="Wed" and day1!="Thu" and day1!="Fri" and day1!="Sat") or (day2!="Sun" and day2!="Mon" and day2!="Tue" and day2!="Wed" and day2!="Thu" and day2!="Fri" and day2!="Sat")):
        print("day")
        valid = False
    if((date1<0 or date1>31) or (date2<0 or date2>31)):
        # print("date")
        valid = False
    if ((month1!="Jan" and month1!="Feb" and month1!="Mar" and month1!="Apr" and month1!="May" and month1!="Jun" and month1!="Jul" and month1!="Aug" and month1!="Sep" and month1!="Oct" and month1!="Nov" and month1!="Dec") or (month2!="Jan" and month2!="Feb" and month2!="Mar" and month2!="Apr" and month2!="May" and month2!="Jun" and month2!="Jul" and month2!="Aug" and month2!="Sep" and month2!="Oct" and month2!="Nov" and month2!="Dec")):
        # print("month")
        valid = False
    if(year1<0 or year2<0):
        # print("year")
        valid = False
    if((hour1<0 or hour1>23) or (hour2<0 or hour2>23)):
        # print("hour")
        valid = False
    if ((minute1 < 0 or minute1 > 59) or (minute2 < 0 or minute2 > 59)):
        # print("minute")
        valid = False
    if ((second1 < 0 or second1 > 59) or (second2 < 0 or second2 > 59)):
        # print("second")
        valid = False

    if(valid):
        t1 = datetime.strptime(time1, '%a %d %b %Y %H:%M:%S %z')
        t2 = datetime.strptime(time2, '%a %d %b %Y %H:%M:%S %z')
        mbox.showinfo("Absolute Time Delta", "Time 1  :  " + time1 + "\nTime 2  :  " + time2 +"\n\nAbsolute Time Delta :\n\nIn seconds  :  " + str(abs(int((t1 - t2).total_seconds()))))
    else:
        mbox.showerror("Error", "You have entered wrong input!")

# for getting the sample input
def get_sample():
    mbox.showinfo("Sample Time Input", "Sample Time Input :\n\nDay  :  Sun\nDate  :  25\nMonth  :  Jul\nYear  :  2012\nHour  :  23\nMinute  :  45\nSecond  :  46\nTime Zone  :  +0700")

# creates sample button
sampleb = Button(window, text="SAMPLE",command=get_sample,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
sampleb.place(x =100 , y =650 )

# created delta button
deltab = Button(window, text="ABS. DELTA",command=get_delta,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
deltab.place(x =310 , y =650 )

# created reset function
def reset_label():
    day_time1_entry.delete(0, END)
    day_time2_entry.delete(0, END)
    date_time1_entry.delete(0, END)
    date_time2_entry.delete(0, END)
    month_time1_entry.delete(0, END)
    month_time2_entry.delete(0, END)
    year_time1_entry.delete(0, END)
    year_time2_entry.delete(0, END)
    hour_time1_entry.delete(0, END)
    hour_time2_entry.delete(0, END)
    minute_time1_entry.delete(0, END)
    minute_time2_entry.delete(0, END)
    second_time1_entry.delete(0, END)
    second_time2_entry.delete(0, END)
    zone_time1_entry.delete(0, END)
    zone_time2_entry.delete(0, END)

# created reset button
resetb = Button(window, text="RESET",command=reset_label,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
resetb.place(x =570 , y =650 )

# funcion for exiting
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

# created exit button
exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 20), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =760 , y =650 )


window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()