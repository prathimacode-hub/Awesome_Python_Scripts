#importing the necessary modules

from tkinter import *
from tkinter import ttk
from tkinter import font
import time
import datetime

#declaring a global variable
global endTime

#function used for exit the application
def quit(*args):
    root.destroy()

def countdown_for_event():
    
    #calculating the time left for the event
    timeLeft=endTime-datetime.datetime.now()

    #Takes away the microseconds(removed)
    timeLeft= timeLeft - datetime.timedelta(microseconds=timeLeft.microseconds)

    #used for displaying the time
    txt.set(timeLeft)

    #Triggers the countdown after thousand milliseconds
    root.after(1000,countdown_for_event)

#Interface for the countdown Timer
root=Tk()
root.attributes("-fullscreen",False)

#setting background color for the window
root.configure(background='black')

root.bind("x",quit)

root.after(1000,countdown_for_event)

#getting the user input

print("Please enter the event date and time")

year=int(input("Enter the year:"))

month=int(input("Enter the month: "))

date=int(input("Enter the date: "))

hour=int(input("Enter the hours: "))

mi=int(input("Enter the minutes: "))

endTime=datetime.datetime(year,month,date,hour,mi)

fnt=font.Font(family="Helvetica",size=90,weight='bold')

#passing the values as string
txt=StringVar()

#setting font foreground and background
lbl=ttk.Label(root, textvariable = txt, font=fnt, foreground='white', background='black')

#position the clock on the screen

lbl.place(relx=0.5,rely=0.5,anchor=CENTER)



