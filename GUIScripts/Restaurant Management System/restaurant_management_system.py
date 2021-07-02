
# imported necessary library
import tkinter
from tkinter import *
from time import gmtime, strftime
import time
import tkinter as tk
import tkinter.ttk
import tkinter.messagebox as mbox

# created main window
root = Tk()
root.geometry("1000x650")
root.title('Restaurant Management System')

# top label
label = Label(root, text="Restaurant Management System", font=("Arial", 50), fg="magenta",underline=0)
label.pack()

# for time
time1 = (" ")
clock = Label(root, font=("Arial", 20), fg="green")
clock.pack(padx=30, pady=30)

# for showing current time
def tick():
    global time1
    time2 = time.strftime('%a, %d %b %Y      %H:%M:%S')
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    clock.after(200, tick)

tick()

# Alingment of frame
bottomframe = Frame(root, )
bottomframe.pack(side=BOTTOM)

f1 = Frame(root)
f1.pack(side=TOP)

def gstp():
    mbox.showinfo("GST"," 18 % GST is on Food Goods and Services Tax (GST) is an indirect tax  levied in India on the supply of goods and services from July 1 2017 ")

def price():  # operation performed by out button  ( pop up windwo)
    root = Tk()
    root.geometry("400x250")
    root.title("Food Price List")
    f1 = Frame(root)
    f1.pack(pady = 10)

    fries = Label(f1, text="Fries Meal  :  ", font=("Arial", 20), fg="green").grid(row=0, column=0)
    friesP = Label(f1, text="Rs 100", font=("Arial", 20), fg="orange").grid(row=0, column=1)
    lunch = Label(f1, text="Lunch Meal  :  ", font=("Arial", 20), fg="green").grid(row=1, column=0)
    lunchP = Label(f1, text="Rs 200", font=("Arial", 20), fg="orange").grid(row=1, column=1)
    burger = Label(f1, text="Burger  :  ", font=("Arial", 20), fg="green").grid(row=2, column=0)
    burgerP = Label(f1, text="Rs 50", font=("Arial", 20), fg="orange").grid(row=2, column=1)
    piz = Label(f1, text="Pizza  :  ", font=("Arial", 20), fg="green").grid(row=3, column=0)
    pizP = Label(f1, text="Rs 120", font=("Arial", 20), fg="orange").grid(row=3, column=1)
    chzb = Label(f1, text="Cheese burger  :  ", font=("Arial", 20), fg="green").grid(row=4, column=0)
    chzbP = Label(f1, text="Rs 40", font=("Arial", 20), fg="orange").grid(row=4, column=1)
    root.mainloop()


def drink():
    root = Tk()
    root.geometry("400x250")
    root.title("Drink Price List")
    f2 = Frame(root)
    f2.pack(pady=10)
    d1 = Label(f2, text="Coca Cola  :  ", font=("Arial", 20), fg="green").grid(row=0, column=0)
    d1 = Label(f2, text="Rs 30", font=("Arial", 20), fg="orange").grid(row=0, column=1)
    d2 = Label(f2, text="Pepsi  :  ", font=("Arial", 20), fg="green").grid(row=1, column=0)
    d2 = Label(f2, text="Rs 50", font=("Arial", 20), fg="orange").grid(row=1, column=1)
    d3 = Label(f2, text="Milk Shake  :  ", font=("Arial", 20), fg="green").grid(row=2, column=0)
    d3 = Label(f2, text="Rs 70", font=("Arial", 20), fg="orange").grid(row=2, column=1)
    root.mainloop()

def pricef():  # operation performed by out button  ( pop up windwo)
    root = Tk()
    root.geometry("400x250")
    root.title("Food List")
    f1 = Frame(root)
    f1.pack(pady = 10)

    fries = Label(f1, text="Fries Meal  ", font=("Arial", 20), fg="green").grid(row=0, column=0)
    lunch = Label(f1, text="Lunch Meal  ", font=("Arial", 20), fg="green").grid(row=1, column=0)
    burger = Label(f1, text="Burger  ", font=("Arial", 20), fg="green").grid(row=2, column=0)
    piz = Label(f1, text="Pizza  ", font=("Arial", 20), fg="green").grid(row=3, column=0)
    chzb = Label(f1, text="Cheese burger  ", font=("Arial", 20), fg="green").grid(row=4, column=0)
    root.mainloop()


def drinkf():
    root = Tk()
    root.geometry("400x250")
    root.title("Drink List")
    f2 = Frame(root)
    f2.pack(pady=10)
    d1 = Label(f2, text="Coca Cola  ", font=("Arial", 20), fg="green").grid(row=0, column=0)
    d2 = Label(f2, text="Pepsi  ", font=("Arial", 20), fg="green").grid(row=1, column=0)
    d3 = Label(f2, text="Milk Shake  ", font=("Arial", 20), fg="green").grid(row=2, column=0)
    root.mainloop()


def out():  # operation performed by out button
    a = tkinter.messagebox.askokcancel("Exit", "Thank you for visiting us !\n\nHave a nice day ")
    if (a):
        quit()

def reset():  # operation performed by reset button
    O.set(0)
    F.set(0)
    L.set(0)
    B.set(0)
    P.set(0)
    Cb.set(0)
    D.set(0)
    C.set("No Value")
    G.set("No Value")
    A.set("No Value")
    S.set("No Value ")
    T.set(" No Value")


def total():
    fries = float(F.get())
    lunch = float(L.get())
    burger = float(B.get())
    pizza = float(P.get())
    cheeseburger = float(Cb.get())
    drink = float(D.get())

    # mult with cost

    Rfries = fries * 100
    Rlunch = lunch * 200
    Rburger = burger * 50
    Rpizza = pizza * 120
    Rcheeseburger = cheeseburger * 40
    Rdrink = drink * 50

    # overall cost after GST and all

    cost = (Rfries + Rlunch + Rburger + Rpizza + Rcheeseburger + Rdrink)
    C.set(cost)
    gst = ((cost * 18) / 100)
    G.set(gst)
    aftergst = "Rs.", str((gst) + (cost))
    A.set(aftergst)
    S.set(aftergst)
    T.set(aftergst)

    mbox.showinfo("Total", "Order No.  :  " + str(O.get()) + "\n\nFries Meal  :  " + str(F.get()) + "\n\nLunch Meal  :  " + str(L.get()) + "\n\nBurger Meal  :  " + str(B.get()) + "\n\nPizza Meal  :  " + str(P.get()) + "\n\nCheese Burger  :  " + str(C.get()) + "\n\nDrinks  :  " + str(D.get()) + "\n\nAmount to be paid  :  " + str(T.get()))


# BUTTON'S

button5 = Button(bottomframe, text="GST ",command=gstp, font=("Arial", 20), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
button5.pack(side=LEFT, padx=24, pady=90)

button1 = Button(bottomframe, text="PRICE",command=price, font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
button1.pack(side=LEFT, padx=24, pady=90)

button2 = Button(bottomframe, text="TOTAL", command=total,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
button2.pack(side=LEFT, pady=24, padx=90)

button3 = Button(bottomframe, text="RESET",command=reset,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
button3.pack(side=LEFT, padx=24, pady=90)

button4 = Button(bottomframe, text="EXIT", command=out,font=("Arial", 20), bg = "red", fg = "blue", borderwidth=3, relief="raised")
button4.pack(side=LEFT, padx=24, pady=90)


# variable defined storing of data
O = StringVar()  # for Order_number
F = StringVar()  # for fries_Meal
L = StringVar()  # for Lunch_meal
B = StringVar()  # for Burger_Meal
P = StringVar()  # for Pizza_Meal
Cb = StringVar()  # for Cheese_Burger
D = StringVar()  # for Drinks
C = StringVar()  # for Cost
G = StringVar()  # for GST
A = StringVar()  # for After GST
S = StringVar()  # for Subtotal
T = StringVar()  # for Total

# Entity names and Entry field

Order_NumberL = Label(f1, text="Order Number : ", font=("Arial", 20), fg="brown").grid(row=0, column=0)
Order_NumberE = Entry(f1, textvariable=O, font=("Arial", 15)).grid(row=0, column=1)

Fries_MealL = Label(f1, text="Fries Meal : ", font=("Arial", 20), fg="brown").grid(row=1, column=0)
Fries_MealE = Entry(f1, textvariable=F, fg="light green", font=("Arial", 15))
Fries_MealE.insert(END, 0)
Fries_MealE.grid(row=1, column=1)

Lunch_MealL = Label(f1, text="Lunch Meal : ", font=("Arial", 20), fg="brown").grid(row=2, column=0)
Lunch_MealE = Entry(f1, textvariable=L, fg="light green", font=("Arial", 15))
Lunch_MealE.insert(END, 0)
Lunch_MealE.grid(row=2, column=1)

Burger_MealL = Label(f1, text="Burger Meal : ", font=("Arial", 20), fg="brown").grid(row=3, column=0)
Burger_MealE = Entry(f1, textvariable=B, fg="light green", font=("Arial", 15))
Burger_MealE.insert(END, 0)
Burger_MealE.grid(row=3, column=1)

PizzaaL = Label(f1, text="Pizza Meal : ", font=("Arial", 20), fg="brown").grid(row=4, column=0)
PizzaaE = Entry(f1, textvariable=P, fg="light green", font=("Arial", 15))
PizzaaE.insert(END, 0)
PizzaaE.grid(row=4, column=1)

Cheese_BurgerL = Label(f1, text="Cheese Burger : ", font=("Arial", 20), fg="brown").grid(row=5, column=0)
Cheese_BurgerE = Entry(f1, textvariable=Cb, fg="light green", font=("Arial", 15))
Cheese_BurgerE.insert(END, 0)
Cheese_BurgerE.grid(row=5, column=1)

DrinkL = Label(f1, text="Drink's : ", font=("Arial", 20), fg="brown").grid(row=0, column=2)
DrinkE = Entry(f1, textvariable=D, fg="light green", font=("Arial", 15))
DrinkE.insert(END, 0)
DrinkE.grid(row=0, column=3)

CostL = Label(f1, text="Cost : ", font=("Arial", 20), fg="brown").grid(row=1, column=2)
CostE = Entry(f1, textvariable=C, fg="steel blue", font=("Arial", 15))
CostE.insert(END, 0)
CostE.grid(row=1, column=3)

Service_ChargeL = Label(f1, text="GST ; ", font=("Arial", 20), fg="brown").grid(row=2, column=2)
Service_ChargeE = Entry(f1, textvariable=G, fg="blue", font=("Arial", 15))
Service_ChargeE.insert(END, 0)
Service_ChargeE.grid(row=2, column=3)

TaxL = Label(f1, text="After GST : ", font=("Arial", 20), fg="brown").grid(row=3, column=2)
TaxE = Entry(f1, textvariable=A, fg="red", font=("Arial", 15))
TaxE.insert(END, 0)
TaxE.grid(row=3, column=3)

SubtotalL = Label(f1, text="Subtotal : ", font=("Arial", 20), fg="brown").grid(row=4, column=2)
SubtotalE = Entry(f1, textvariable=S, fg="red", font=("Arial", 15))
SubtotalE.insert(END, 0)
SubtotalE.grid(row=4, column=3)

TotalL = Label(f1, text="Total : ", font=("Arial", 20), fg="brown").grid(row=5, column=2)
TotalE = Entry(f1, textvariable=T, fg="red", font=("Arial", 15))
TotalE.insert(END, 0)
TotalE.grid(row=5, column=3)

# __________________Extra Buttons__________________#
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='Available Food', menu=filemenu)
filemenu.add_command(label='Food"s', command=pricef)
filemenu.add_command(label="Drink's", command=drinkf)

menu2 = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='Rate List', menu=menu2)
menu2.add_command(label="Food's", command=price)
menu2.add_command(label="Drinks", command=drink)

root.mainloop()
# End of code