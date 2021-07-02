
# All Laptop Detailer

# imported necessary libraries
import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
import pandas as pd

# created a main window
window = Tk()
window.geometry("1000x700")
window.title("All Laptop Detailer")

# ------------------------- for showing gif image on the main window ------------------------------
frameCnt = 3
frames = [PhotoImage(file='Images/laptops.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

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
label.place(x = 100, y = 100)
window.after(0, update, 0)
# --------------------------------------------------------------------

# read the data using pandas library
data = pd.read_csv("laptop_dataset.csv")
Product = data["Product"].tolist()
Company = data["Company"].tolist()
TypeName = data["TypeName"].tolist()
Inches = data["Inches"].tolist()
ScreenResolution = data["ScreenResolution"].tolist()
Cpu = data["Cpu"].tolist()
Ram = data["Ram"].tolist()
Memory = data["Memory"].tolist()
Gpu = data["Gpu"].tolist()
OpSys = data["OpSys"].tolist()
Weight = data["Weight"].tolist()
Price_euros = data["Price_euros"].tolist()

def histroy_details():
    mbox.showinfo("Laptop History", "Grid Compass\n\nThe first laptop-sized notebook computer was the Epson HX-20, invented (patented) by Suwa Seikosha's Yukio Yokozawa in July 1980, introduced at the COMDEX computer show in Las Vegas by Japanese company Seiko Epson in 1981, and released in July 1982.\n\nThe first laptop was made in 1982 Enclosed in a magnesium case, it introduced the now familiar clamshell design, in which the flat display folded shut against the keyboard. The computer was equipped with a 320×200-pixel electroluminescent display and 384 kilobyte bubble memory.")

def get_details():
    product = product_var.get()
    for i in range(0, len(Product)):
        if(Product[i] == product):
            mbox.showinfo(product + "Details", str(product) + "\n\n1.)  Company Name  :  " + str(Company[i]) + "\n\n2.)  Laptop Type  :  " + str(TypeName[i]) + "\n\n3.)  Screen Inches  :  " + str(Inches[i]) + "\n\n4.)  Screen Resolution  :  " + str(ScreenResolution[i]) + "\n\n5.)  CPU Model  :  " + str(Cpu[i]) + "\n\n6.)  RAM Characteristics  :  " + str(Ram[i]) + "\n\n7.)  Memory  :  " + str(Memory[i]) + "\n\n8.)  GPU Characteristics  :  " + str(Gpu[i]) + "\n\n9.)  Operating System  :  " + str(OpSys[i]) + "\n\n10.)  Laptop's Weight  :  " + str(Weight[i]) + "\n\n11.)  Laptop's Price  :  " + str(Price_euros[i]))
            return

# top label
start1 = tk.Label(text = "ALL LAPTOP DETAILER", font=("Arial", 50), fg="magenta",underline=0) # same way bg
start1.place(x = 120, y = 10)

# label for laptop product ---------------------------------------------------------------------------------
modellbl = tk.Label(text = "LAPTOP PRODUCT : ", font=("Arial", 30), fg="brown") # same way bg
modellbl.place(x = 100, y = 550)

# creating the drop down menu button for selecting laptop model
product_var = tk.StringVar()
product_choices = Product
product_menu = OptionMenu(window, product_var, *product_choices)
product_menu.config(font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3)
product_menu["menu"].config(font=("Arial", 10), bg = "light yellow", fg = "blue")
product_menu.place(x=500, y=545)
product_var.set("MacBook Pro")

# laptop button
laptopb = Button(window, text="LAPTOP",command=histroy_details,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
laptopb.place(x =100 , y =620 )

# details button
getb = Button(window, text="DETAILS",command=get_details,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
getb.place(x =320 , y =620 )

# function created for reset button
def reset_label():
    product_var.set("MacBook Pro")

# created reset button
resetb = Button(window, text="RESET",command=reset_label,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
resetb.place(x =550 , y =620 )

# function for exiting
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

# created exit button
exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 20), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =770 , y =620 )


window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()