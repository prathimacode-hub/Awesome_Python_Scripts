
# Nobel Prize Winner

# imported necessary library
import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
import pandas as pd


# created main window
window = Tk()
window.geometry("1000x700")
window.title("Nobel Prize Winner")

# ---------------------- for showing gif image in main window -----------------------------------
frameCnt = 4
frames = [PhotoImage(file='Images/nobel.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

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
label.place(x = 160, y = 100)
window.after(0, update, 0)
# --------------------------------------------------------------------

# read the data using pandas library
data = pd.read_csv("nobel.csv")
Year = data['Year'].tolist()
Category = data['Category'].tolist()
Name = data['Name'].tolist()
Birthdate = data['Birthdate'].tolist()
Birth_Place = data['Birth Place'].tolist()
Country = data['Country'].tolist()
Residence = data['Residence'].tolist()
Role_Affiliate = data['Role/Affiliate'].tolist()
Field_Language = data['Field/Language'].tolist()
Prize_Name = data['Prize Name'].tolist()
Motivation = data['Motivation'].tolist()

year1 = list(set(Year))

# function for NOBEL button
def get_status():
    mbox.showinfo("Nobel Prize", "Novel Prize :\n\nThe Nobel Prize is five separate prizes that, according to Alfred Nobel's will of 1895, are awarded to ”those who, during the preceding year, have conferred the greatest benefit to humankind.” Nobel Prizes are awarded in the fields of Physics, Chemistry, Physiology or Medicine, Literature, and Peace.\n\nAccording to his will and testament read in Stockholm on 30 December 1896, a foundation established by Alfred Nobel would reward those who serve humanity. The Nobel Prize was funded by Alfred Nobel's personal fortune. According to the official sources, Alfred Nobel bequeathed 94% of his fortune to the Nobel Foundation that now forms the economic base of the Nobel Prize.\n\nAwarded for: Contributions that have conferred the greatest benefit to humankind in the areas of Physics, Chemistry, Physiology or Medicine, Literature, and Peace.")

# function for DETAILS button
def details():
    selected_year = year_var.get()
    s1 = "YEAR  :  "
    s1 = s1 + str(selected_year)
    cnt = 0
    s = ""
    for i in range(0,len(Year)):
        if(Year[i] == selected_year):
            s = s + "\n\n1.)  Name  :  "
            s = s + str(Name[i])
            s = s + "\n2.)  Birth Date  :  "
            s = s + str(Birthdate[i])
            s = s + "\n3.)  Birth Place  :  "
            s = s + str(Birth_Place[i])
            s = s + "\n4.)  Country  :  "
            s = s + str(Country[i])
            s = s + "\n5.)  Residence  :  "
            s = s + str(Residence[i])
            s = s + "\n6.)  Role/Affiliate  :  "
            s = s + str(Role_Affiliate[i])
            s = s + "\n7.)  Field/Language  :  "
            s = s + str(Field_Language[i])
            s = s + "\n8.)  Prize Name  :  "
            s = s + str(Prize_Name[i])
            s = s + "\n9.)  Motivation  :  "
            s = s + str(Motivation[i])
            cnt = cnt + 1

    s2 = "\n\nNumber of Nobel Prize awarded  :  "
    s2 = s2 + str(cnt)

    s = s1 + s2 + s
    mbox.showinfo(str(selected_year) + " Nobel Prize Winners", s)


# top label
start1 = tk.Label(text = "Nobel Prize Winner", font=("Arial", 50), fg="magenta",underline=0) # same way bg
start1.place(x = 200, y = 10)

# label for country code ---------------------------------------------------------------------------------
sel_label = tk.Label(text = "Select  Year : ", font=("Arial", 30), fg="brown") # same way bg
sel_label.place(x = 250, y = 470)

# creating the drop down menu button for selecting year
year_var = tk.IntVar()
# as icon size are really small, we defined the following 7 sizes
year_choices = year1
# food_choices.sort()
year_menu = OptionMenu(window, year_var, *year_choices)
year_menu.config(font=("Arial", 25), bg = "light green", fg = "blue", borderwidth=3)
year_menu["menu"].config(font=("Arial", 10), bg = "light yellow", fg = "blue")
year_menu.place(x=500, y=465)
year_var.set(1901) # size 1 is selected as by default, and we can

# created NOBEL button
nobelb = Button(window, text="NOBEL",command=get_status,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
nobelb.place(x =120 , y =570 )

# created DETAILS button
detailsb = Button(window, text="DETAILS",command=details,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
detailsb.place(x =320 , y =570 )

# function for RESET button
def reset_label():
    year_var.set(1901)

# created RESET button
resetb = Button(window, text="RESET",command=reset_label,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
resetb.place(x =550 , y =570 )

# Function got EXIT button
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

# created EXIT button
exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 20), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =750 , y =570 )


window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()