

import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
import pandas as pd



window = Tk()
window.geometry("1000x700")
window.title("Periodic Table Elements Information")

# ---------------------------------------------------------
frameCnt = 4
frames = [PhotoImage(file='Images/periodic.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

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

data = pd.read_csv("periodic_table.csv")
number = data['number'].tolist()
name = data['name'].tolist()
symbol = data['symbol'].tolist()
appearance = data['appearance'].tolist()
atomic_number = data['atomic_number'].tolist()
group_block = data['group_block'].tolist()
period = data['period'].tolist()
element_category = data['element_category'].tolist()
atomic_weight = data['atomic_weight'].tolist()
electron_configuration = data['electron_configuration'].tolist()
phase = data['phase'].tolist()
melting_point = data['melting_point'].tolist()
boiling_point = data['boiling_point'].tolist()
heat_of_vaporization = data['heat_of_vaporization'].tolist()
heat_of_fusion = data['heat_of_fusion'].tolist()
molar_heat_capacity = data['molar_heat_capacity'].tolist()
oxidation_states = data['oxidation_states'].tolist()
electronegativity = data['electronegativity'].tolist()
ionization_energies = data['ionization_energies'].tolist()
covalent_radius = data['covalent_radius'].tolist()
van_der_waals_radius = data['van_der_waals_radius'].tolist()
crystal_structure = data['crystal_structure'].tolist()
thermal_conductivity = data['thermal_conductivity'].tolist()
magnetic_ordering = data['magnetic_ordering'].tolist()

# print(len(number))
# print(name)
# print(symbol)
# print(appearance)
# print(atomic_number)
# print(group_block)
# print(period)
# print(element_category)
# print(atomic_weight)
# print(electron_configuration)
# print(phase)
# print(melting_point)
# print(boiling_point)
# print(heat_of_vaporization)
# print(heat_of_fusion)
# print(molar_heat_capacity)
# print(oxidation_states)
# print(electronegativity)
# print(ionization_energies)
# print(covalent_radius)
# print(van_der_waals_radius)
# print(crystal_structure)
# print(thermal_conductivity)
# print(magnetic_ordering)
#

def details():
    selected_name = name_var.get()
    for i in range(0,len(name)):
        if(name[i] == selected_name):
            mbox.showinfo(selected_name + " Details", "Name  :  " + str(selected_name) + "\n\n1.)  Symbol  :  " + str(symbol[i]) + "\n2.)  Appearence  :  " + str(appearance[i]) + "\n3.)  Atomic Number  :  " + str(atomic_number[i]) + "\n4.)  Group Block  :  " + str(group_block[i]) + "\n5.)  Period  :  " + str(period[i]) + "\n6.)  Element Category  :  " + str(element_category[i]) + "\n7.)  Atomic Weight  :  " + str(atomic_weight[i]) + "\n8.)  Electronic Configuration  :  " + str(electron_configuration[i]) + "\n9.)  Phase  :  " + str(phase[i]) + "\n10.)  Melting Point  :  " + str(melting_point[i]) + "\n11.)  Boiling Point  :  " + str(boiling_point[i]) + "\n12.)  Heat of Vaporization  :  " + str(heat_of_vaporization[i]) + "\n13.)  Heat of Fusion  :  " + str(heat_of_fusion[i]) + "\n14.)  Molar Heat Capacity  :  " + str(molar_heat_capacity[i]) + "\n15.)  Oxidation States  :  " + str(oxidation_states[i]) + "\n16.)  Electronegativity  :  " + str(electronegativity[i]) + "\n17.)  Ionization Energies  :  " + str(ionization_energies[i]) + "\n18.)  Covalent Radius  :  " + str(covalent_radius[i]) + "\n19.)  Van Der Waal's Radius  :  " + str(van_der_waals_radius[i]) + "\n20.)  Crystal Structure  :  " + str(crystal_structure[i]) + "\n21.)  Thermal Conductivity  :  " + str(thermal_conductivity[i]) + "\n22.)  Magnetic Ordering  :  " + str(magnetic_ordering[i]))


# top label
start1 = tk.Label(text = "PERIODIC TABLE ELEMENT INFO", font=("Arial", 40), fg="magenta",underline=0) # same way bg
start1.place(x = 70, y = 10)
#
# label for country code ---------------------------------------------------------------------------------
sel_label = tk.Label(text = "Select  Element Name : ", font=("Arial", 30), fg="brown") # same way bg
sel_label.place(x = 150, y = 500)

# creating the drop down menu button for selecting food
name_var = tk.StringVar()
# as icon size are really small, we defined the following 7 sizes
name_choices = name
# food_choices.sort()
name_menu = OptionMenu(window, name_var, *name_choices)
name_menu.config(font=("Arial", 25), bg = "light green", fg = "blue", borderwidth=3)
name_menu["menu"].config(font=("Arial", 10), bg = "light yellow", fg = "blue")
name_menu.place(x=600, y=490)
name_var.set("Hydrogen") # size 1 is selected as by default, and we can

infob = Button(window, text="DETAILS",command=details,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
infob.place(x =200 , y =600 )

def reset_label():
    name_var.set("Hydrogen")

resetb = Button(window, text="RESET",command=reset_label,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
resetb.place(x =450 , y =600 )


def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 20), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =730 , y =600 )


window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()