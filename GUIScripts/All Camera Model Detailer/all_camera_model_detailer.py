
# All Camera Model Detailer

# imported necessary libraries
import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
import pandas as pd

# created a main window
window = Tk()
window.geometry("1000x700")
window.title("All Camera Model Detailer")

# ------------------------- for showing gif image on the main window ------------------------------
frameCnt = 4
frames = [PhotoImage(file='Images/cameras.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

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

# read the data using pandas library
data = pd.read_csv("camera_dataset.csv")
Model = data["Model"].tolist()
Release_date = data["Release date"].tolist()
Max_resolution = data["Max resolution"].tolist()
Low_resolution = data["Low resolution"].tolist()
Effective_pixels = data["Effective pixels"].tolist()
Zoom_wide = data["Zoom wide (W)"].tolist()
Zoom_tele = data["Zoom tele (T)"].tolist()
Normal_focus_range = data["Normal focus range"].tolist()
Macro_focus_range = data["Macro focus range"].tolist()
Storage_included = data["Storage included"].tolist()
Weight = data["Weight (inc. batteries)"].tolist()
Dimensions = data["Dimensions"].tolist()
Price = data["Price"].tolist()


def get_details():
    model = model_var.get()
    for i in range(0, len(Model)):
        if(Model[i] == model):
            mbox.showinfo(model + "Details", str(model) + "\n\n1.)  Release date  :  " + str(Release_date[i]) + "\n\n2.)  Max resolution  :  " + str(Max_resolution[i]) + "\n\n3.)  Low resolution  :  " + str(Low_resolution[i]) + "\n\n4.)  Effective pixels  :  " + str(Effective_pixels[i]) + "\n\n5.)  Zoom wide (W)  :  " + str(Zoom_wide[i]) + "\n\n6.)  Zoom tele (T)  :  " + str(Zoom_tele[i]) + "\n\n7.)  Normal Focus Range  :  " + str(Normal_focus_range[i]) + "\n\n8.)  Macro Focus Range  :  " + str(Macro_focus_range[i]) + "\n\n9.)  Storage Included  :  " + str(Storage_included[i]) + "\n\n10.)  Weight (inc. batteries)  :  " + str(Weight[i]) + "\n\n11.)  Dimensions  :  " + str(Dimensions[i]) + "\n\n12.)  Price  :  " +str(Price[i]))

# top label
start1 = tk.Label(text = "CAMERA MODEL DETAILER", font=("Arial", 50), fg="magenta",underline=0) # same way bg
start1.place(x = 50, y = 10)

# label for camera model ---------------------------------------------------------------------------------
modellbl = tk.Label(text = "CAMERA MODEL  : ", font=("Arial", 30), fg="brown") # same way bg
modellbl.place(x = 120, y = 550)

# creating the drop down menu button for selecting camera model
model_var = tk.StringVar()
model_choices = Model
model_menu = OptionMenu(window, model_var, *model_choices)
model_menu.config(font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3)
model_menu["menu"].config(font=("Arial", 10), bg = "light yellow", fg = "blue")
model_menu.place(x=500, y=545)
model_var.set("Agfa ePhoto 1280") # size 1 is selected as by default, and we can

# details button
getb2 = Button(window, text="DETAILS",command=get_details,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
getb2.place(x =150 , y =620 )

# function created for reset button
def reset_label():
    model_var.set("Agfa ePhoto 1280")

# created reset button
resetb = Button(window, text="RESET",command=reset_label,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
resetb.place(x =480 , y =620 )

# function for exiting
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

# created exit button
exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 20), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =770 , y =620 )


window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()