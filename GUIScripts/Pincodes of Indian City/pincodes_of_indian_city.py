

import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
import pandas as pd



window = Tk()
window.geometry("1000x700")
window.title("Pincodes of Indian City")

# ---------------------------------------------------------
frameCnt = 4
frames = [PhotoImage(file='Images/pincodes.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

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
label.place(x = 250, y = 100)
window.after(0, update, 0)
# --------------------------------------------------------------------

data = pd.read_csv("pincode_data.csv")
Pincode = data['Pincode'].tolist()
District = data['District'].tolist()
StateName = data['StateName'].tolist()

district1 = set(District)

def about():
    mbox.showinfo("Pin Code Details", "The term Postal Index Number or PIN is also widely known as PIN code in India. It refers to the code in the post office number of the postal code system which is predominantly used in the India Post to segregate the mails.\n\nThe Postal Index Number consists of 6 long digits. This system of coding the postal address was introduced way back in 1972 by Shriram Bhikaji Velankar, who was the then additional secretary in the Union Ministry of Communications.\n\nThe main reason behind the introduction of the PIN-code system in India was to help the postal departmental staff in manually sorting and delivering the mail to the accurate address and thus eliminating the confusion over similar place names, incorrect addresses, different languages used by the public.")

def pincode():
    selected_name = name_var.get()
    s1 = ""
    s2 = ""
    st = ""
    flag = False
    x = 0
    y = 0
    for i in range(0,len(District)):
        if(District[i] == selected_name and flag==False):
            flag = True
            x = Pincode[i]
            s1 = s1 + str(Pincode[i])
            st = StateName[i]
        if (District[i] != selected_name and flag==True):
            s2 = s2 + str(Pincode[i-1])
            y = Pincode[i-1]
            break

    mbox.showinfo(selected_name + " Pin Code", "1.)  District Name  :  " + str(selected_name) + "\n\n2.)  Number of Cities in district " + selected_name + "  :  " + str(y-x)  + "\n\n3.)  Pin Code Range is  :  ( " + s1 + " , " + s2 + " ) " + "\n\n4.)  State  :  " + str(st))


# top label
start1 = tk.Label(text = "PINCODES OF INDIAN CITY", font=("Arial", 50), fg="magenta",underline=0) # same way bg
start1.place(x = 50, y = 10)

# label for universitry name ---------------------------------------------------------------------------------
sel_label = tk.Label(text = "SELECT CITY NAME : ", font=("Arial", 30), fg="brown") # same way bg
sel_label.place(x = 100, y = 480)

# creating the drop down menu button for selecting food
name_var = tk.StringVar()
# as icon size are really small, we defined the following 7 sizes
name_choices = district1
# food_choices.sort()
name_menu = OptionMenu(window, name_var, *name_choices)
name_menu.config(font=("Arial", 25), bg = "light green", fg = "blue", borderwidth=3)
name_menu["menu"].config(font=("Arial", 10), bg = "light yellow", fg = "blue")
name_menu.place(x=530, y=470)
name_var.set("VADODARA") # size 1 is selected as by default, and we can

aboutb = Button(window, text="ABOUT",command=about,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
aboutb.place(x =150 , y =600 )

pincodeb = Button(window, text="PIN CODE",command=pincode,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
pincodeb.place(x =320 , y =600 )

def reset_label():
    name_var.set("VADODARA")

resetb = Button(window, text="RESET",command=reset_label,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
resetb.place(x =550 , y =600 )


def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 20), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =730 , y =600 )


window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()