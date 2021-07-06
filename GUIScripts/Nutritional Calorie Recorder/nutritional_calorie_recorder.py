
# Nutritional Calorie Recorder

# Import necessary libraries
from datetime import datetime
from tkinter import *
import tkinter as tk
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as mbox
from PIL import Image, ImageTk, ImageDraw

sqlite_file='CalorieRecorder.db'

# created root window
root = Tk()
root.title('Nutritional Calorie Recorder')
root.geometry("1000x700")

# top label
start1 = tk.Label(text = "Nutritional Calorie Recorder", font=("Arial", 50,'underline'), fg="magenta") # same way bg
start1.place(x = 80, y = 10)

# image on the main window
path = "Images/calorie.jpg"
# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img1 = ImageTk.PhotoImage(Image.open(path))
# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(root, image = img1)
panel.place(x = 110, y = 100)

# food label
food1 = tk.Label(text = "Select Your Diet : ", font=("Arial", 30,), fg="green") # same way bg
food1.place(x = 100, y = 485)

# building connection with database
conn=sqlite3.connect(sqlite_file)
c=conn.cursor()

# functon to create dropdown menu
def chooseOption(value):
    tmp=c.execute("SELECT Calories FROM Calorie_Values WHERE FoodName=?", (value))
    out = tmp.fetchone()
    Label(text=out, font=("Arial", 30), fg="brown").place(x=550, y=560)
    # save each value as it is chosen
    savedata(int(out[0]))

# for storing choices of food
choice=[]
for row in c.execute('SELECT FoodName FROM Calorie_Values'):
    choice.append(row)

food_var = tk.StringVar()
# as icon size are really small, we defined the following 7 sizes
food_choices = choice
food_menu = OptionMenu(root, food_var, *food_choices, command = chooseOption)
food_menu.config(font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3)
food_menu["menu"].config(font=("Arial", 10), bg = "light yellow", fg = "blue")
food_menu.place(x=420, y=482)
food_var.set("{1/3-lb. Burger}") # size 1 is selected as by default, and we can

# calorie select value label
calorie_sel1 = tk.Label(text = "Selected Calorie Value : ", font=("Arial", 30,), fg="green") # same way bg
calorie_sel1.place(x = 100, y = 560)

# calorie select value label
calorie_total1 = tk.Label(text = "Total Calorie Value : ", font=("Arial", 30,), fg="green") # same way bg
calorie_total1.place(x = 100, y = 630)

# function for exiting the window
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        root.destroy()

exitb = Button(root, text="EXIT",command=exit_win,font=("Arial", 25), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =850 , y =600 )

#Save data from any entries chosen in Db/User_Repository
def savedata(amount):
    # print("saving {}".format((datetime.now().date(),amount)))
    tmp1=c.execute("INSERT INTO Calorie_Intake(Date,CaloriesConsumed) VALUES (?,?)", (str(datetime.now().date()),amount))
    out = tmp1.fetchone()
    conn.commit()

    # Add total calorie count to this function so that it executes constantly
    tmp2=c.execute("SELECT SUM(CaloriesConsumed) FROM Calorie_Intake WHERE Date=(?) GROUP BY Date", [(str(datetime.now().date(),))])
    out = tmp2.fetchone()
    Label(text=out, font=("Arial", 30,), fg="brown").place(x=470, y=630)
    conn.commit()
    mbox.showinfo("Success", "Calorie data stored successfully in database\n\n\nDate  :  " + str(datetime.now().date()) + "\n\nTime  :  " + str(datetime.now().time()) + "\n\nAdded Calorie  :  " + food_var.get() + "\n\nAdded Calorie Value  :  " + str(amount))


root.protocol("WM_DELETE_WINDOW", exit_win)
root.mainloop()
