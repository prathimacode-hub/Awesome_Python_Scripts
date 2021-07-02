
# Indian Food Information

import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
import pandas as pd



window = Tk()
window.geometry("1000x700")
window.title("Indian Food Information")

# ---------------------------------------------------------
frameCnt = 4
frames = [PhotoImage(file='Images/food.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

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

data = pd.read_csv("indian_food.csv")
food_name = data['name'].tolist()
food_ingredients = data['ingredients'].tolist()
food_diet = data['diet'].tolist()
food_prep_time = data['prep_time'].tolist()
food_cook_time = data['cook_time'].tolist()
food_flavor_profile = data['flavor_profile'].tolist()
food_course = data['course'].tolist()
food_state = data['state'].tolist()
food_region = data['region'].tolist()

# print(food_ingredients)

def get_status():
    mbox.showinfo("INDIA", "Indian food is fourth most popular in the world, according to a study of cuisine trade.\n\nThe 5 MOST POPULAR CUISINES IN THE WORLD :\n1.)  Italian\n2.)  Japanese\n3.)  Chinese\n4.)  Indian\n5.)  American")

def get_info():
    selected_food = food_var.get()
    for i in range(0,len(food_name)):
        # print(i,food_name[i], selected_food)
        if(food_name[i] == selected_food):
            mbox.showinfo(selected_food + " Info", "Ingredients  :  " + food_ingredients[i] + "\n\nDiet  :  " + food_diet[i] + "\n\nPreparation Time  :  " + str(food_prep_time[i]) + " mins" + "\n\nCooking Time  :  " + str(food_cook_time[i]) + " mins" + "\n\nFlavour  :  " + food_flavor_profile[i] + "\n\nCourse  :  " + food_course[i] + "\n\nState  :  " + food_state[i] + "\n\nRegion  :  " + food_region[i])
            return

# top label
start1 = tk.Label(text = "INDIAN FOOD INFO", font=("Arial", 50), fg="magenta",underline=0) # same way bg
start1.place(x = 200, y = 10)

# label for country code ---------------------------------------------------------------------------------
sel_label = tk.Label(text = "Select Food : ", font=("Arial", 30), fg="brown") # same way bg
sel_label.place(x = 200, y = 490)

# creating the drop down menu button for selecting food
food_var = tk.StringVar()
# as icon size are really small, we defined the following 7 sizes
food_choices = food_name
food_choices.sort()
food_menu = OptionMenu(window, food_var, *food_choices)
food_menu.config(font=("Arial", 25), bg = "light green", fg = "blue", borderwidth=3)
food_menu["menu"].config(font=("Arial", 10), bg = "light yellow", fg = "blue")
food_menu.place(x=450, y=480)
food_var.set("Gulab jamun") # size 1 is selected as by default, and we can

indiab = Button(window, text="INDIA",command=get_status,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
indiab.place(x =150 , y =600 )

infob = Button(window, text="GET INFO",command=get_info,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
infob.place(x =300 , y =600 )

def reset_label():
    food_var.set("Gulab jamun")

resetb = Button(window, text="RESET",command=reset_label,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
resetb.place(x =510 , y =600 )


def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 20), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =680 , y =600 )


window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()