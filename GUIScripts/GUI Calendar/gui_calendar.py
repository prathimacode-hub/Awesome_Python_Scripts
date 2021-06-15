# importing tkinter
from tkinter import *
# importing calendar module
import calendar
# initializing tkinter
root = Tk()
# setting title of our Gui
root.title("My Own Gui Calendar")
# year for which we want the calendar to be shown on our Gui
year = int(input("Enter The Year: "))
# storing 2020 year calendar data inside myCal
myCal = calendar.calendar(year)
# showing calendar data using label widget
cal_year = Label(root, text=myCal, font="Consolas 10 bold")
# packing the Label widget
cal_year.pack()
# running the program in ready state
root.mainloop()