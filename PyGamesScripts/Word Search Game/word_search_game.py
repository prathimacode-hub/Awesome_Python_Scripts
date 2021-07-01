
from tkinter import *
from tkinter import messagebox
import tkinter.messagebox as mbox
import tkinter as tk


# created a main window
root = Tk()
root.title("Word Search Game")
root.geometry('1100x750')


# ------------------------------------- frame0 -------------------------------------
def des_f0():
    f0.destroy()

# function defined to show rules
def show_rules():
    mbox.showinfo("RULES", "1.)  Player will be given word board with alphabets in it.\n\n2.)  There will 15 words will be displayed on screen one by one and player need to YES or NO for that word is present in word board or not respectively.\n\n3.)  The points each word will be shown at the top right corner.\n\n4.)  At last, final score will be shown along with count of correct and wrong answer, and also user can see the words that are present in it at the end.")

# created first main frame
f0 = Frame(root, height=750, width=1100)
f0.propagate(0)
f0.pack(side='top')

# function for adding image in frame 1
c = Canvas(f0, width=1100, height=750)
c.pack()
p = PhotoImage(file='Images/front.gif')
c.create_image(130, 50, image=p, anchor=NW)

# created start button
startb = Button(f0, text="START",command=des_f0,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
startb.place(x = 120 , y =600 )

# created start button
rulesb = Button(f0, text="RULES",command=show_rules,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
rulesb.place(x = 480 , y =600 )

# ------------------------- frame1 - level1 --------------------------------------
word_ques = ["MOUSE","JAGUAR","LION", "FERRET","GIBREL","FISH","PEACOCK","CHINCHILLA","GUINEA","PIGEON","CHICKEN", "SNAKE","FLAMINGO","TURTLE","LIZARD"]
word_ans = ["YES","NO","NO", "YES","YES","YES","NO","YES","YES","NO","YES", "YES","NO","YES","YES"]

ind = -1
cr = 0
wr = 0
cnt = 15
def initial():
    global ind

    ind = ind + 1
    word.configure(text=word_ques[ind])

def see_ans():
    f2.destroy()

    f3 = Frame(root, width=1100, height=750)
    f3.propagate(0)
    f3.pack(side='top')

    c3 = Canvas(f3, width=1100, height=750, bg="white")  # blue
    c3.pack()
    p3 = PhotoImage(file="Images/score1.gif")
    c3.create_image(150, 10, image=p3, anchor="nw")
    w3 = Canvas(root)
    w3.p3 = p3


def next_switch():
    global ind, cnt
    cnt = cnt - 1
    if (cnt >= 0):
        lives_cnt1 = tk.Label(text="       ", font=("Arial", 30), fg="brown")
        lives_cnt1.place(x=940, y=20)
        lives_cnt = tk.Label(text=cnt, font=("Arial", 30), fg="brown")  # same way bg
        lives_cnt.place(x=940, y=20)
    if (cnt == -1):
        mbox.showinfo("GAME OVER", "GAME OVER !")
        f1.destroy()

        f2 = Frame(root, width=1100, height=750)
        f2.propagate(0)
        f2.pack(side='top')

        c2 = Canvas(f2, width=1100, height=750, bg="white")  # blue
        c2.pack()
        p2 = PhotoImage(file="Images/score1.gif")
        c2.create_image(350, 10, image=p2, anchor="nw")
        w2 = Canvas(root)
        w2.p2 = p2

        score1 = Label(f2, text=str(cr * 10) + "/150", font=("Arial", 100), fg="green", bg="white")
        score1.place(x=350, y=250)

        see1 = Label(f2, text="SEE HOW WELL YOU CAN SEARCH WORDS", font=("Arial", 30), fg="brown", bg="light yellow")
        see1.place(x=150, y=500)
        see2 = Label(f2, text="Correct Answer :" + str(cr) + "/15", font=("Arial", 30), fg="orange",
                     bg="white")
        see2.place(x=350, y=580)
        see3 = Label(f2, text="Wrong Answer :" + str(wr) + "/15", font=("Arial", 30), fg="blue", bg="white")
        see3.place(x=350, y=650)
        # # keyboard button created for opening keyboard
        # seeansb = Button(f2, text="SEE ANS", command=see_ans, font=("Arial", 20), bg="light green", fg="blue",borderwidth=3, relief="raised")
        # seeansb.place(x=860, y=650)

        m1 = mbox.askokcancel("Final Answer", "Do You want to see Final Answer")
        if(m1):
            f2.destroy()

            f3 = Frame(root, width=1100, height=750)
            f3.propagate(0)
            f3.pack(side='top')

            c3 = Canvas(f3, width=1100, height=750, bg="white")  # blue
            c3.pack()
            p3 = PhotoImage(file="Images/final_ans.gif")
            c3.create_image(150, 10, image=p3, anchor="nw")
            w3 = Canvas(root)
            w3.p3 = p3


    ind = ind + 1
    if(ind<=14):
        word.configure(text=word_ques[ind])

def answer_check():
    global cr, wr
    selected_ans = word1_var.get()
    if(ind<=14):
        if(selected_ans == word_ans[ind]):
            mbox.showinfo('Success', 'Your answer is correct')
            cr = cr + 1
            next_switch()
        else:
            mbox.showerror('Error','Your answer is wrong')
            wr = wr + 1
            next_switch()
    else:
        next_switch()


# created frame 1
f1 = Frame(root, height=750, width=1100)
f1.propagate(0)
f1.pack(side='top')

# function for adding image in frame 1
c1 = Canvas(f1, width=1100, height=750)
c1.pack()
p1 = PhotoImage(file='Images/final_ques.gif')
c1.create_image(20, 10, image=p1, anchor=NW)

lives = tk.Label(f1,text = "Lives : ", font=("Arial", 30), fg="brown") # same way bg
lives.place(x = 800, y = 20)

lives_cnt = tk.Label(f1,text = 15, font=("Arial", 30), fg="brown") # same way bg
lives_cnt.place(x = 940, y = 20)

# label for showing points on tp right corner
points1 = Label(f1, text="Points : " + str(10), font=("Arial", 35), fg="magenta")
points1.place(x = 800, y = 80)

# for starting top label
word = Label(f1, font=("Arial", 30), fg="brown")
word.place(x=800, y=250)

# for starting top label
select = Label(f1, text='Select Ans : ', font=("Arial", 30), fg="green")
select.place(x=750, y=320)

word1_var = tk.StringVar()
word1_choices = ["YES", "NO"]
word1_menu = OptionMenu(f1, word1_var, *word1_choices)
word1_menu.config(font=("Arial", 20), bg="light green", fg="blue", borderwidth=3)
word1_menu["menu"].config(font=("Arial", 15), bg="light yellow", fg="blue")
word1_menu.place(x=980, y=320)
word1_var.set("NO")

# keyboard button created for opening keyboard
checkb = Button(f1, text="CHECK",command=answer_check,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
checkb.place(x =840 , y =480 )

initial()
# -------------------------------------------------------------------------------------


# function for exiting
def exit_win():
    if messagebox.askokcancel("Exit", "Do you want to exit?"):
        root.destroy()

# created exit button
exitb = Button(root, text="EXIT",command=exit_win,font=("Arial", 20), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =860 , y =600 )


root.protocol("WM_DELETE_WINDOW", exit_win)
root.mainloop()
