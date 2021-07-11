
# Hex Color Code

# imported necessary library
import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
import pandas as pd

# created main window
window = Tk()
window.geometry("1000x700")
window.title("Hex Color Code")

# read the data using pandas library
data = pd.read_csv("hex_data.csv")
Name = data['Name'].tolist()
name_sort = data['Name'].tolist()
html_code = data['html_code'].tolist()
rgb_code = data['rgb_code'].tolist()
shades = data['shades'].tolist()

name_sort.sort()

# for getting the hex code details
def code_details():
    selected_name = name_var.get()
    for i in range(0,len(Name)):
        if(Name[i] == selected_name):
            preview_text.configure(bg=html_code[i])
            top1.configure(bg=html_code[i])
            top2.configure(bg=html_code[i])
            mbox.showinfo(selected_name + " Hex Code", "Name  :  " + str(selected_name) + "\n\n1.)  Hex Code  :  " + str(html_code[i]) + "\n2.)  RGB Code  :  " + str(rgb_code[i]) + "\n3.)  Shade  :  " + str(shades[i]))


# top label
start1 = tk.Label(text="HEX COLOR CODE", font=("Arial", 50), fg="magenta", underline=0)  # same way bg
start1.place(x=180, y=10)

# for preview
preview_text = tk.Text(window,height = 15, width = 60, font=("Arial", 15),bg = "white", borderwidth=3, relief="solid")
preview_text.place(x = 150, y = 110)

# preview1 label
top1 = Label(window, text = "PREVIEW AREA", font=("Arial", 40), fg="black", bg = "white") # same way bg
top1.place(x = 270, y = 180)

# preview2 label
top2 = Label(window, text = "Chosen Color will be previed here...", font=("Arial", 25), fg="black", bg = "white") # same way bg
top2.place(x = 220, y = 280)

# label for color name ---------------------------------------------------------------------------------
sel_label = tk.Label(text="COLOR NAME : ", font=("Arial", 35), fg="brown")  # same way bg
sel_label.place(x=180, y=490)

# creating the drop down menu button for selecting color name
name_var = tk.StringVar()
name_choices = name_sort
name_menu = OptionMenu(window, name_var, *name_choices)
name_menu.config(font=("Arial", 25), bg="light green", fg="blue", borderwidth=3)
name_menu["menu"].config(font=("Arial", 10), bg="light yellow", fg="blue")
name_menu.place(x=540, y=490)
name_var.set("antiquewhite")  # size 1 is selected as by default, and we can

# get button created
getb = Button(window, text="GET HEX CODE", command=code_details, font=("Arial", 20), bg="light green", fg="blue", borderwidth=3, relief="raised")
getb.place(x=100, y=600)

# function for reseting
def reset_label():
    name_var.set("antiquewhite")
    preview_text.configure(bg="white")


# created reset button
resetb = Button(window, text="RESET", command=reset_label, font=("Arial", 20), bg="light green", fg="blue", borderwidth=3, relief="raised")
resetb.place(x=500, y=600)

# function for exiting
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

# created exit button
exitb = Button(window, text="EXIT", command=exit_win, font=("Arial", 20), bg="red", fg="blue", borderwidth=3, relief="raised")
exitb.place(x=800, y=600)


window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()
