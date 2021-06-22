
# Spelling Corrector

import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
from PIL import Image, ImageTk
import json

data1 = json.load(open("data.json"))
# print(data1["questions"])
# print(data1["options"])
# print(data1["answers"])
ques = data1["questions"]
opt = data1["options"]
ans = data1["answers"]


def show_rules():
    mbox.showinfo("Rules", "1.) There are 10 Questions.\n\n2.) The score for each question will be shown on the top right corner.")


window = Tk()
window.geometry("1000x700")
window.title("Quiz Game")

cnt = 0
pnts = 0
cr = 0
wr = 0
# ------------------------------ frame1 ----------------------
def des_f1():
    f1.destroy()

f1 = Frame(window, width=1000, height=700)
f1.propagate(0)
f1.pack(side='top')

c1 = Canvas(f1, width=1000, height=700)
c1.pack()
p1 = PhotoImage(file='Images/quiz.gif')
c1.create_image(200, 50, image=p1, anchor=NW)

rulesb = Button(f1, text="RULES",command=show_rules,font=("Arial", 30), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
rulesb.place(x =390 , y =530 )

startb = Button(f1, text="START",command=des_f1,font=("Arial", 30), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
startb.place(x =730 , y =530 )
# ------------------------------------------------------------

# ---------------------------------------- frame2 ----------------------------------
# def des_f2():
#     f2.destroy()

f2 = Frame(window, width=1000, height=700)
f2.propagate(0)
f2.pack(side='top')
points2 = Label(f2, text="Points : " + str(10), font=("Arial", 35), fg="magenta")
points2.place(x = 700, y = 20)
f2_ques = Label(f2, text=ques[0], font=("Arial", 25), fg="blue")
f2_ques.place(x=50, y=100)
f2_op1 = Label(f2, text=opt[0][0], font=("Arial", 25), fg="green")
f2_op1.place(x=100, y=170)
f2_op2 = Label(f2, text=opt[0][1], font=("Arial", 25), fg="green")
f2_op2.place(x=100, y=230)
f2_op3 = Label(f2, text=opt[0][2], font=("Arial", 25), fg="green")
f2_op3.place(x=100, y=300)
f2_op4 = Label(f2, text=opt[0][3], font=("Arial", 25), fg="green")
f2_op4.place(x=100, y=370)
f2_selected_label = Label(f2, text="Select Option : ", font=("Arial", 25), fg="brown")
f2_selected_label.place(x=100, y=450)
# creating the drop down menu button
f2_select_var = tk.StringVar()
f2_choices = ["a", "b", "c", "d"]
f2_menu = OptionMenu(f2, f2_select_var, *f2_choices)
f2_menu.config(font=("Arial", 20), bg="light green", fg="blue", borderwidth=3)
f2_menu["menu"].config(font=("Arial", 15), bg="light yellow", fg="blue")
f2_menu.place(x=330, y=450)
f2_select_var.set("a")

def f2_reset_choice():
    f2_select_var.set("a")

def des_f2():
    global cnt,pnts, cr, wr
    # print(f2_select_var.get(), ans[0])
    if(f2_select_var.get() == ans[0]):
        cnt = cnt + 1
        pnts = pnts + 10
        cr = cr + 1
    else:
        wr = wr + 1
    # print(cnt)
    f2.destroy()

f2_resetb = Button(f2, text="RESET", command=f2_reset_choice, font=("Arial", 30), bg="light green", fg="blue", borderwidth=3,
                  relief="raised")
f2_resetb.place(x=400, y=530)

f2_selectb = Button(f2, text="SELECT", command=des_f2, font=("Arial", 30), bg="light green", fg="blue", borderwidth=3,
                  relief="raised")
f2_selectb.place(x=700, y=530)
# --------------------------------------------------------------------------------------

# ---------------------------------------- frame3 ----------------------------------
# def des_f3():
#     f3.destroy()

f3 = Frame(window, width=1000, height=700)
f3.propagate(0)
f3.pack(side='top')
points3 = Label(f3, text="Points : " + str(15), font=("Arial", 35), fg="magenta")
points3.place(x = 700, y = 20)
f3_ques = Label(f3, text=ques[1], font=("Arial", 25), fg="blue")
f3_ques.place(x=50, y=100)
f3_op1 = Label(f3, text=opt[1][0], font=("Arial", 25), fg="green")
f3_op1.place(x=100, y=170)
f3_op2 = Label(f3, text=opt[1][1], font=("Arial", 25), fg="green")
f3_op2.place(x=100, y=230)
f3_op3 = Label(f3, text=opt[1][2], font=("Arial", 25), fg="green")
f3_op3.place(x=100, y=300)
f3_op4 = Label(f3, text=opt[1][3], font=("Arial", 25), fg="green")
f3_op4.place(x=100, y=370)
f3_selected_label = Label(f3, text="Select Option : ", font=("Arial", 25), fg="brown")
f3_selected_label.place(x=100, y=450)
# creating the drop down menu button
f3_select_var = tk.StringVar()
f3_choices = ["a", "b", "c", "d"]
f3_menu = OptionMenu(f3, f3_select_var, *f3_choices)
f3_menu.config(font=("Arial", 20), bg="light green", fg="blue", borderwidth=3)
f3_menu["menu"].config(font=("Arial", 15), bg="light yellow", fg="blue")
f3_menu.place(x=330, y=450)
f3_select_var.set("a")

def f3_reset_choice():
    f3_select_var.set("a")

def des_f3():
    global cnt,pnts, cr, wr
    # print(f3_select_var.get(), ans[1])
    if(f3_select_var.get() == ans[1]):
        cnt = cnt + 1
        pnts = pnts + 15
        cr = cr + 1
    else:
        wr = wr + 1
    f3.destroy()

f3_resetb = Button(f3, text="RESET", command=f3_reset_choice, font=("Arial", 30), bg="light green", fg="blue", borderwidth=3,
                  relief="raised")
f3_resetb.place(x=400, y=530)

f3_selectb = Button(f3, text="SELECT", command=des_f3, font=("Arial", 30), bg="light green", fg="blue", borderwidth=3,
                  relief="raised")
f3_selectb.place(x=700, y=530)
# --------------------------------------------------------------------------------------

# ---------------------------------------- frame4 ----------------------------------
# def des_f4():
#     f4.destroy()

f4 = Frame(window, width=1000, height=700)
f4.propagate(0)
f4.pack(side='top')
points4 = Label(f4, text="Points : " + str(15), font=("Arial", 35), fg="magenta")
points4.place(x = 700, y = 20)
f4_ques = Label(f4, text=ques[2], font=("Arial", 25), fg="blue")
f4_ques.place(x=50, y=100)
f4_op1 = Label(f4, text=opt[2][0], font=("Arial", 25), fg="green")
f4_op1.place(x=100, y=170)
f4_op2 = Label(f4, text=opt[2][1], font=("Arial", 25), fg="green")
f4_op2.place(x=100, y=230)
f4_op3 = Label(f4, text=opt[2][2], font=("Arial", 25), fg="green")
f4_op3.place(x=100, y=300)
f4_op4 = Label(f4, text=opt[2][3], font=("Arial", 25), fg="green")
f4_op4.place(x=100, y=370)
f4_selected_label = Label(f4, text="Select Option : ", font=("Arial", 25), fg="brown")
f4_selected_label.place(x=100, y=450)
# creating the drop down menu button
f4_select_var = tk.StringVar()
f4_choices = ["a", "b", "c", "d"]
f4_menu = OptionMenu(f4, f4_select_var, *f4_choices)
f4_menu.config(font=("Arial", 20), bg="light green", fg="blue", borderwidth=3)
f4_menu["menu"].config(font=("Arial", 15), bg="light yellow", fg="blue")
f4_menu.place(x=330, y=450)
f4_select_var.set("a")

def f4_reset_choice():
    f4_select_var.set("a")

def des_f4():
    global cnt, pnts, cr, wr
    # print(f4_select_var.get(), ans[2])
    if(f4_select_var.get() == ans[2]):
        cnt = cnt + 1
        pnts = pnts + 15
        # print(cnt)
        cr = cr + 1
    else:
        wr = wr + 1
    f4.destroy()

f4_resetb = Button(f4, text="RESET", command=f4_reset_choice, font=("Arial", 30), bg="light green", fg="blue", borderwidth=3,
                  relief="raised")
f4_resetb.place(x=400, y=530)

f4_selectb = Button(f4, text="SELECT", command=des_f4, font=("Arial", 30), bg="light green", fg="blue", borderwidth=3,
                  relief="raised")
f4_selectb.place(x=700, y=530)
# --------------------------------------------------------------------------------------

# ---------------------------------------- frame5 ----------------------------------
# def des_f5():
#     f5.destroy()

f5 = Frame(window, width=1000, height=700)
f5.propagate(0)
f5.pack(side='top')
points5 = Label(f5, text="Points : " + str(30), font=("Arial", 35), fg="magenta")
points5.place(x = 700, y = 20)
f5_ques = Label(f5, text=ques[3], font=("Arial", 25), fg="blue")
f5_ques.place(x=50, y=100)
f5_op1 = Label(f5, text=opt[3][0], font=("Arial", 25), fg="green")
f5_op1.place(x=100, y=170)
f5_op2 = Label(f5, text=opt[3][1], font=("Arial", 25), fg="green")
f5_op2.place(x=100, y=230)
f5_op3 = Label(f5, text=opt[3][2], font=("Arial", 25), fg="green")
f5_op3.place(x=100, y=300)
f5_op4 = Label(f5, text=opt[3][3], font=("Arial", 25), fg="green")
f5_op4.place(x=100, y=370)
f5_selected_label = Label(f5, text="Select Option : ", font=("Arial", 25), fg="brown")
f5_selected_label.place(x=100, y=450)
# creating the drop down menu button
f5_select_var = tk.StringVar()
f5_choices = ["a", "b", "c", "d"]
f5_menu = OptionMenu(f5, f5_select_var, *f5_choices)
f5_menu.config(font=("Arial", 20), bg="light green", fg="blue", borderwidth=3)
f5_menu["menu"].config(font=("Arial", 15), bg="light yellow", fg="blue")
f5_menu.place(x=330, y=450)
f5_select_var.set("a")

def f5_reset_choice():
    f5_select_var.set("a")

def des_f5():
    global cnt,pnts, cr, wr
    # print(f5_select_var.get(), ans[3])
    if(f5_select_var.get() == ans[3]):
        cnt = cnt + 1
        pnts = pnts + 30
        # print(cnt)
        cr = cr + 1
    else:
        wr = wr + 1
    f5.destroy()

f5_resetb = Button(f5, text="RESET", command=f5_reset_choice, font=("Arial", 30), bg="light green", fg="blue", borderwidth=3,
                  relief="raised")
f5_resetb.place(x=400, y=530)

f5_selectb = Button(f5, text="SELECT", command=des_f5, font=("Arial", 30), bg="light green", fg="blue", borderwidth=3,
                  relief="raised")
f5_selectb.place(x=700, y=530)
# --------------------------------------------------------------------------------------

# ---------------------------------------- frame6 ----------------------------------
# def des_f6():
#     f6.destroy()

f6 = Frame(window, width=1000, height=700)
f6.propagate(0)
f6.pack(side='top')
points6 = Label(f6, text="Points : " + str(30), font=("Arial", 35), fg="magenta")
points6.place(x = 700, y = 20)
f6_ques = Label(f6, text=ques[4], font=("Arial", 25), fg="blue")
f6_ques.place(x=50, y=100)
f6_op1 = Label(f6, text=opt[4][0], font=("Arial", 25), fg="green")
f6_op1.place(x=100, y=170)
f6_op2 = Label(f6, text=opt[4][1], font=("Arial", 25), fg="green")
f6_op2.place(x=100, y=230)
f6_op3 = Label(f6, text=opt[4][2], font=("Arial", 25), fg="green")
f6_op3.place(x=100, y=300)
f6_op4 = Label(f6, text=opt[4][3], font=("Arial", 25), fg="green")
f6_op4.place(x=100, y=370)
f6_selected_label = Label(f6, text="Select Option : ", font=("Arial", 25), fg="brown")
f6_selected_label.place(x=100, y=450)
# creating the drop down menu button
f6_select_var = tk.StringVar()
f6_choices = ["a", "b", "c", "d"]
f6_menu = OptionMenu(f6, f6_select_var, *f6_choices)
f6_menu.config(font=("Arial", 20), bg="light green", fg="blue", borderwidth=3)
f6_menu["menu"].config(font=("Arial", 15), bg="light yellow", fg="blue")
f6_menu.place(x=330, y=450)
f6_select_var.set("a")

def f6_reset_choice():
    f6_select_var.set("a")

def des_f6():
    global cnt,pnts, cr, wr
    # print(f6_select_var.get(), ans[4])
    if(f6_select_var.get() == ans[4]):
        cnt = cnt + 1
        pnts = pnts + 30
        # print(cnt)
        cr = cr + 1
    else:
        wr = wr + 1
    f6.destroy()

f6_resetb = Button(f6, text="RESET", command=f6_reset_choice, font=("Arial", 30), bg="light green", fg="blue", borderwidth=3,
                  relief="raised")
f6_resetb.place(x=400, y=530)

f6_selectb = Button(f6, text="SELECT", command=des_f6, font=("Arial", 30), bg="light green", fg="blue", borderwidth=3,
                  relief="raised")
f6_selectb.place(x=700, y=530)
# --------------------------------------------------------------------------------------

# ---------------------------------------- frame7 ----------------------------------
# def des_f7():
#     f7.destroy()


f7 = Frame(window, width=1000, height=700)
f7.propagate(0)
f7.pack(side='top')
points7 = Label(f7, text="Points : " + str(60), font=("Arial", 35), fg="magenta")
points7.place(x = 700, y = 20)
f7_ques = Label(f7, text=ques[5], font=("Arial", 25), fg="blue")
f7_ques.place(x=50, y=100)
f7_op1 = Label(f7, text=opt[5][0], font=("Arial", 25), fg="green")
f7_op1.place(x=100, y=170)
f7_op2 = Label(f7, text=opt[5][1], font=("Arial", 25), fg="green")
f7_op2.place(x=100, y=230)
f7_op3 = Label(f7, text=opt[5][2], font=("Arial", 25), fg="green")
f7_op3.place(x=100, y=300)
f7_op4 = Label(f7, text=opt[5][3], font=("Arial", 25), fg="green")
f7_op4.place(x=100, y=370)
f7_selected_label = Label(f7, text="Select Option : ", font=("Arial", 25), fg="brown")
f7_selected_label.place(x=100, y=450)
# creating the drop down menu button
f7_select_var = tk.StringVar()
f7_choices = ["a", "b", "c", "d"]
f7_menu = OptionMenu(f7, f7_select_var, *f7_choices)
f7_menu.config(font=("Arial", 20), bg="light green", fg="blue", borderwidth=3)
f7_menu["menu"].config(font=("Arial", 15), bg="light yellow", fg="blue")
f7_menu.place(x=330, y=450)
f7_select_var.set("a")

def f7_reset_choice():
    f7_select_var.set("a")

def des_f7():
    global cnt,pnts, cr, wr
    # print(f7_select_var.get(), ans[5])
    if (f7_select_var.get() == ans[5]):
        cnt = cnt + 1
        pnts = pnts + 60
        # print(cnt)
        cr = cr + 1
    else:
        wr = wr + 1
    f7.destroy()


f7_resetb = Button(f7, text="RESET", command=f7_reset_choice, font=("Arial", 30), bg="light green", fg="blue", borderwidth=3,
                  relief="raised")
f7_resetb.place(x=400, y=530)

f7_selectb = Button(f7, text="SELECT", command=des_f7, font=("Arial", 30), bg="light green", fg="blue", borderwidth=3,
                  relief="raised")
f7_selectb.place(x=700, y=530)


# --------------------------------------------------------------------------------------

# ---------------------------------------- frame8 ----------------------------------
# def des_f8():
#     f8.destroy()


f8 = Frame(window, width=1000, height=700)
f8.propagate(0)
f8.pack(side='top')
points8 = Label(f8, text="Points : " + str(60), font=("Arial", 35), fg="magenta")
points8.place(x = 700, y = 20)
f8_ques = Label(f8, text=ques[6], font=("Arial", 25), fg="blue")
f8_ques.place(x=50, y=100)
f8_op1 = Label(f8, text=opt[6][0], font=("Arial", 25), fg="green")
f8_op1.place(x=100, y=170)
f8_op2 = Label(f8, text=opt[6][1], font=("Arial", 25), fg="green")
f8_op2.place(x=100, y=230)
f8_op3 = Label(f8, text=opt[6][2], font=("Arial", 25), fg="green")
f8_op3.place(x=100, y=300)
f8_op4 = Label(f8, text=opt[6][3], font=("Arial", 25), fg="green")
f8_op4.place(x=100, y=370)
f8_selected_label = Label(f8, text="Select Option : ", font=("Arial", 25), fg="brown")
f8_selected_label.place(x=100, y=450)
# creating the drop down menu button
f8_select_var = tk.StringVar()
f8_choices = ["a", "b", "c", "d"]
f8_menu = OptionMenu(f8, f8_select_var, *f8_choices)
f8_menu.config(font=("Arial", 20), bg="light green", fg="blue", borderwidth=3)
f8_menu["menu"].config(font=("Arial", 15), bg="light yellow", fg="blue")
f8_menu.place(x=330, y=450)
f8_select_var.set("a")

def f8_reset_choice():
    f8_select_var.set("a")

def des_f8():
    global cnt,pnts, cr, wr
    # print(f8_select_var.get(), ans[6])
    if (f8_select_var.get() == ans[6]):
        cnt = cnt+ 1
        pnts = pnts + 60
        # print(cnt)
        cr = cr + 1
    else:
        wr = wr + 1
    f8.destroy()


f8_resetb = Button(f8, text="RESET", command=f8_reset_choice, font=("Arial", 30), bg="light green", fg="blue", borderwidth=3,
                  relief="raised")
f8_resetb.place(x=400, y=530)

f8_selectb = Button(f8, text="SELECT", command=des_f8, font=("Arial", 30), bg="light green", fg="blue", borderwidth=3,
                  relief="raised")
f8_selectb.place(x=700, y=530)


# --------------------------------------------------------------------------------------

# ---------------------------------------- frame9 ----------------------------------
# def des_f9():
#     f9.destroy()


f9 = Frame(window, width=1000, height=700)
f9.propagate(0)
f9.pack(side='top')
points9 = Label(f9, text="Points : " + str(90), font=("Arial", 35), fg="magenta")
points9.place(x = 700, y = 20)
f9_ques = Label(f9, text=ques[7], font=("Arial", 25), fg="blue")
f9_ques.place(x=50, y=100)
f9_op1 = Label(f9, text=opt[7][0], font=("Arial", 25), fg="green")
f9_op1.place(x=100, y=170)
f9_op2 = Label(f9, text=opt[7][1], font=("Arial", 25), fg="green")
f9_op2.place(x=100, y=230)
f9_op3 = Label(f9, text=opt[7][2], font=("Arial", 25), fg="green")
f9_op3.place(x=100, y=300)
f9_op4 = Label(f9, text=opt[7][3], font=("Arial", 25), fg="green")
f9_op4.place(x=100, y=370)
f9_selected_label = Label(f9, text="Select Option : ", font=("Arial", 25), fg="brown")
f9_selected_label.place(x=100, y=450)
# creating the drop down menu button
f9_select_var = tk.StringVar()
f9_choices = ["a", "b", "c", "d"]
f9_menu = OptionMenu(f9, f9_select_var, *f9_choices)
f9_menu.config(font=("Arial", 20), bg="light green", fg="blue", borderwidth=3)
f9_menu["menu"].config(font=("Arial", 15), bg="light yellow", fg="blue")
f9_menu.place(x=330, y=450)
f9_select_var.set("a")

def f9_reset_choice():
    f9_select_var.set("a")

def des_f9():
    global cnt, pnts, cr, wr
    # print(f9_select_var.get(), ans[7])
    if (f9_select_var.get() == ans[7]):
        cnt = cnt + 1
        pnts = pnts + 90
        # print(cnt)
        cr = cr + 1
    else:
        wr = wr + 1
    f9.destroy()



f9_resetb = Button(f9, text="RESET", command=f9_reset_choice, font=("Arial", 30), bg="light green", fg="blue", borderwidth=3,
                  relief="raised")
f9_resetb.place(x=400, y=530)

f9_selectb = Button(f9, text="SELECT", command=des_f9, font=("Arial", 30), bg="light green", fg="blue", borderwidth=3,
                  relief="raised")
f9_selectb.place(x=700, y=530)


# --------------------------------------------------------------------------------------

# ---------------------------------------- frame10 ----------------------------------
# def des_f10():
#     f10.destroy()


f10 = Frame(window, width=1000, height=700)
f10.propagate(0)
f10.pack(side='top')
points10 = Label(f10, text="Points : " + str(90), font=("Arial", 35), fg="magenta")
points10.place(x = 700, y = 20)
f10_ques = Label(f10, text=ques[8], font=("Arial", 25), fg="blue")
f10_ques.place(x=50, y=100)
f10_op1 = Label(f10, text=opt[8][0], font=("Arial", 25), fg="green")
f10_op1.place(x=100, y=170)
f10_op2 = Label(f10, text=opt[8][1], font=("Arial", 25), fg="green")
f10_op2.place(x=100, y=230)
f10_op3 = Label(f10, text=opt[8][2], font=("Arial", 25), fg="green")
f10_op3.place(x=100, y=300)
f10_op4 = Label(f10, text=opt[8][3], font=("Arial", 25), fg="green")
f10_op4.place(x=100, y=370)
f10_selected_label = Label(f10, text="Select Option : ", font=("Arial", 25), fg="brown")
f10_selected_label.place(x=100, y=450)
# creating the drop down menu button
f10_select_var = tk.StringVar()
f10_choices = ["a", "b", "c", "d"]
f10_menu = OptionMenu(f10, f10_select_var, *f10_choices)
f10_menu.config(font=("Arial", 20), bg="light green", fg="blue", borderwidth=3)
f10_menu["menu"].config(font=("Arial", 15), bg="light yellow", fg="blue")
f10_menu.place(x=330, y=450)
f10_select_var.set("a")

def f10_reset_choice():
    f10_select_var.set("a")

def des_f10():
    global cnt, pnts, cr, wr
    # print(f10_select_var.get(), ans[8])
    if (f10_select_var.get() == ans[8]):
        cnt = cnt + 1
        pnts = pnts + 90
        # print(cnt)
        cr = cr + 1
    else:
        wr = wr + 1
    f10.destroy()


f10_resetb = Button(f10, text="RESET", command=f10_reset_choice, font=("Arial", 30), bg="light green", fg="blue", borderwidth=3,
                  relief="raised")
f10_resetb.place(x=400, y=530)

f10_selectb = Button(f10, text="SELECT", command=des_f10, font=("Arial", 30), bg="light green", fg="blue", borderwidth=3,
                  relief="raised")
f10_selectb.place(x=700, y=530)


# --------------------------------------------------------------------------------------

# ---------------------------------------- frame11 ----------------------------------
# def des_f11():
#     f11.destroy()


f11 = Frame(window, width=1000, height=700)
f11.propagate(0)
f11.pack(side='top')
points11 = Label(f11, text="Points : " + str(100), font=("Arial", 35), fg="magenta")
points11.place(x = 700, y = 20)
f11_ques = Label(f11, text=ques[9], font=("Arial", 25), fg="blue")
f11_ques.place(x=50, y=100)
f11_op1 = Label(f11, text=opt[9][0], font=("Arial", 25), fg="green")
f11_op1.place(x=100, y=170)
f11_op2 = Label(f11, text=opt[9][1], font=("Arial", 25), fg="green")
f11_op2.place(x=100, y=230)
f11_op3 = Label(f11, text=opt[9][2], font=("Arial", 25), fg="green")
f11_op3.place(x=100, y=300)
f11_op4 = Label(f11, text=opt[9][3], font=("Arial", 25), fg="green")
f11_op4.place(x=100, y=370)
f11_selected_label = Label(f11, text="Select Option : ", font=("Arial", 25), fg="brown")
f11_selected_label.place(x=100, y=450)
# creating the drop down menu button
f11_select_var = tk.StringVar()
f11_choices = ["a", "b", "c", "d"]
f11_menu = OptionMenu(f11, f11_select_var, *f11_choices)
f11_menu.config(font=("Arial", 20), bg="light green", fg="blue", borderwidth=3)
f11_menu["menu"].config(font=("Arial", 15), bg="light yellow", fg="blue")
f11_menu.place(x=330, y=450)
f11_select_var.set("a")

def f11_reset_choice():
    f11_select_var.set("a")

def des_f11():
    global cnt,pnts, cr, wr
    # print(f11_select_var.get(), ans[9])
    if (f11_select_var.get() == ans[9]):
        cnt = cnt + 1
        pnts = pnts + 100
        # print(cnt)
        cr = cr + 1
    else:
        wr = wr + 1
    mbox.showinfo("GAME OVER","GAME OVER!\n\nSee your SCORE.\n")
    f11.destroy()

    # displaying score ----------------------------------------------------------------------
    score = Frame(window, width=1000, height=700)
    score.propagate(0)
    score.pack(side='top')

    c3 = Canvas(score, width=1000, height=700, bg="white")  # blue
    c3.pack()
    p3 = PhotoImage(file="Images/score1.gif")
    c3.create_image(300, 10, image=p3, anchor="nw")
    w3 = Canvas(window)
    w3.p3 = p3

    score1 = Label(score, text=str(pnts) + "/500", font=("Arial", 100), fg="green", bg="white")
    score1.place(x=250, y=230)

    correct1 = Label(score, text ="Correct Answer : " + str(cr) + "/10", font=("Arial", 40), fg="brown", bg="white")
    correct1.place(x=230, y=430)

    wrong1 = Label(score, text="Wrong Answer : " + str(wr) + "/10", font=("Arial", 40), fg="brown", bg="white")
    wrong1.place(x=230, y=530)
    # -----------------------------------------------------------------------------------------



f11_resetb = Button(f11, text="RESET", command=f11_reset_choice, font=("Arial", 30), bg="light green", fg="blue", borderwidth=3,
                  relief="raised")
f11_resetb.place(x=400, y=530)

f11_selectb = Button(f11, text="SELECT", command=des_f11, font=("Arial", 30), bg="orange", fg="blue", borderwidth=3,
                  relief="raised")
f11_selectb.place(x=700, y=530)
# --------------------------------------------------------------------------------------


def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 30), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =100 , y =530 )

window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()