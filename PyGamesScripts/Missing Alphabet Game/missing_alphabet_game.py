
# Unscramble Word Game

import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
import random
from random import shuffle
import pandas as pd
from PIL import Image, ImageTk

data = pd.read_csv('country_name.csv')
answers = data['COUNTRY'].tolist()

shuffle(answers)

questions=[]
for word in answers:
    word_list = list(word)
    blank_idx = random.randint(0, len(word_list)-1)
    word_list[blank_idx] = "_"
    wordi = "".join(word_list)
    questions.append(wordi)

# print(answers)
# print(questions)

correct_cnt = 0
wrong_cnt = 0
skip_cnt = 0

num = random.randint(0, len(questions)-1)
def initial():
    global questions, num
    lb1.configure(text=questions[num])

cnt = 20
def next_switch():
    global cnt, skip_cnt
    cnt = cnt - 1
    if(cnt>=0):
        lives_cnt1 = tk.Label(text="       ", font=("Arial", 30), fg="brown")
        lives_cnt1.place(x=880, y=70)
        lives_cnt = tk.Label(text=cnt, font=("Arial", 30), fg="brown")  # same way bg
        lives_cnt.place(x=890, y=70)

    if(cnt==-1):
        mbox.showinfo("GAME OVER", "GAME OVER !")

        f1 = Frame(window, width=1000, height=700)
        f1.propagate(0)
        f1.pack(side='top')

        c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
        c1.pack()
        p1 = PhotoImage(file="Images/score1.gif")
        c1.create_image(300, 10, image=p1, anchor="nw")
        w1 = Canvas(window)
        w1.p1 = p1

        score1 = Label(f1, text=str(correct_cnt) + "/20", font=("Arial", 100), fg="green", bg="white")
        score1.place(x=350, y=230)

        # c2 = Canvas(f1, width=500, height=300, bg="white")  # blue
        # c2.place(x=250, y=350)
        # p2 = PhotoImage(file="Images/scoreboard.gif")
        # c2.create_image(0, 0, image=p2, anchor="nw")
        # w2 = Canvas(window)
        # w2.p2 = p2

        see1 = Label(f1, text="SEE HOW WELL YOU KNOW COUNTRY NAME", font=("Arial", 30), fg="brown", bg="light yellow")
        see1.place(x=50, y=380)
        see2 = Label(f1, text="Correct Answer :" + str(correct_cnt) + "/20", font=("Arial", 30), fg="orange",bg="white")
        see2.place(x=250, y=450)
        see3 = Label(f1, text="Wrong Answer :" + str(wrong_cnt) + "/20", font=("Arial", 30), fg="blue", bg="white")
        see3.place(x=250, y=520)
        see4 = Label(f1, text="Skipped Country :" + str(skip_cnt) + "/20", font=("Arial", 30), fg="green", bg="white")
        see4.place(x=250, y=590)

    global questions, answers, num
    num = random.randint(0, len(questions)-1)
    lb1.configure(text=questions[num])

def skip_switch():
    global cnt, skip_cnt
    cnt = cnt - 1
    if(cnt>=0):
        lives_cnt1 = tk.Label(text="       ", font=("Arial", 30), fg="brown")
        lives_cnt1.place(x=880, y=70)
        lives_cnt = tk.Label(text=cnt, font=("Arial", 30), fg="brown")  # same way bg
        lives_cnt.place(x=890, y=70)

    if (cnt == -1):
        mbox.showinfo("GAME OVER", "GAME OVER !")

        f1 = Frame(window, width=1000, height=700)
        f1.propagate(0)
        f1.pack(side='top')

        c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
        c1.pack()
        p1 = PhotoImage(file="Images/score1.gif")
        c1.create_image(300, 10, image=p1, anchor="nw")
        w1 = Canvas(window)
        w1.p1 = p1

        score1 = Label(f1, text=str(correct_cnt) + "/20", font=("Arial", 100), fg="green", bg = "white")
        score1.place(x=350, y=230)

        # c2 = Canvas(f1, width=500, height=300, bg="white")  # blue
        # c2.place(x = 250,y = 350)
        # p2 = PhotoImage(file="Images/scoreboard.gif")
        # c2.create_image(0, 0, image=p2, anchor="nw")
        # w2 = Canvas(window)
        # w2.p2 = p2

        see1 = Label(f1, text="SEE HOW WELL YOU KNOW COUNTRY NAME", font=("Arial", 30), fg="brown",bg = "light yellow")
        see1.place(x=50, y=380)
        see2 = Label(f1, text="Correct Answer :" + str(correct_cnt) + "/20", font=("Arial", 30), fg="orange",bg = "white")
        see2.place(x=250, y=450)
        see3 = Label(f1, text="Wrong Answer :" + str(wrong_cnt) + "/20", font=("Arial", 30), fg="blue",bg = "white")
        see3.place(x=250, y=520)
        see4 = Label(f1, text="Skipped Country :" + str(skip_cnt) + "/20", font=("Arial", 30), fg="green",bg = "white")
        see4.place(x=250, y=590)

    global questions, answers, num
    num = random.randint(0, len(questions) - 1)
    lb1.configure(text=questions[num])
    skip_cnt = skip_cnt + 1

def answercheck():
    global questions, num, answers, correct_cnt, wrong_cnt,correct_alphabet
    user_alphabet = char_var.get()

    # print(user_alphabet)

    quesnum_list = list(questions[num])
    for i in range(0,len(quesnum_list)):
        if(quesnum_list[i]=='_'):
            quesnum_list[i]=user_alphabet
            correct_alphabet = answers[num][i]
            break
    ques_word_after = "".join(quesnum_list)
    # print(ques_word_after,answers[num])

    if ques_word_after == answers[num]:
        mbox.showinfo('Success','Your answer is correct')
        correct_cnt = correct_cnt + 1
        next_switch()
    else:
        wrong_cnt  = wrong_cnt + 1
        mbox.showerror('Error','Your answer is wrong\n\nCorrect alphabet is : '+ correct_alphabet+'\n\nCorrect word is : '+answers[num]+'\n\n')
        next_switch()


window = Tk()
window.geometry("1000x700")
window.title("Missing Alphabet Game")
# window.iconbitmap(r"icon.ico")

# image on the main window
path = "Images/missing.jpg"
# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))
# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image = img, anchor = "nw")
# The Pack geometry manager packs widgets in rows or columns.
# panel.pack(side = "top", fill = "both", expand = "no")
panel.place(x = 180, y = 100)

start1 = tk.Label(text = "MISSING ALPHABET", font=("Arial", 40), fg="magenta",underline=0) # same way bg
start1.place(x = 250, y = 10)

lives = tk.Label(text = "LIVES", font=("Arial", 30), fg="brown") # same way bg
lives.place(x = 850, y = 20)

lives_cnt = tk.Label(text = 20, font=("Arial", 30), fg="brown") # same way bg
lives_cnt.place(x = 880, y = 70)

missing_aword = Label(window, text = "COUNTRY : ", font=("Arial", 30), fg="green")
missing_aword.place(x=150, y = 400)

lb1 = Label(window, font=("Arial", 30), fg="brown",bg = "light yellow")
lb1.place(x=400, y = 400)

missing_lbl = Label(window, text = "SELECT MISSING ALPHABET : ",font=("Arial", 30), fg="green")
missing_lbl.place(x=100, y = 480)

# creating the drop down menu button
char_var = tk.StringVar()
# as icon size are really small, we defined the following 7 sizes
char_choices = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","V","U","V",'W',"X","Y","Z"]
char_menu = OptionMenu(window, char_var, *char_choices)
char_menu.config(font=("Arial", 25), bg = "light green", fg = "blue", borderwidth=3)
char_menu["menu"].config(font=("Arial", 15), bg = "light yellow", fg = "blue")
char_menu.place(x=710, y=475)
char_var.set("A") # size 1 is selected as by default, and we can

# e1 = Entry(window,font=("Arial", 30) , width=25, border=2)
# e1.insert(0, 'Enter your correct word here...')
# e1.bind('<FocusIn>', on_e1_click)
# e1.place(x = 220, y = 400)

checkb = Button(window, text="CHECK",command=answercheck,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
checkb.place(x =180 , y =570 )

def reset_label():
    char_var.set("A")

resetb = Button(window, text="RESET",command=reset_label,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
resetb.place(x =360 , y =570 )

skipb = Button(window, text="SKIP",command=skip_switch,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
skipb.place(x =540 , y =570 )

def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 20), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =680 , y =570 )

initial()

window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()