
# Decode Image Game

import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
from PIL import Image, ImageTk


window = Tk()
window.geometry("1000x700")
window.title("Decode Image Game")

# image on the main window
path = "Images/front.jpg"
# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img1 = ImageTk.PhotoImage(Image.open(path))
# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image = img1)
panel.place(x = 150, y = 170)

top1 = Label(window, text="DECODE IMAGE GAME", font=("Arial", 50, "underline"), fg="magenta")
top1.place(x = 120, y = 10)

def start_fun():
    window.destroy()

startb = Button(window, text="START",command=start_fun,font=("Arial", 25), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
startb.place(x =100 , y =580 )

def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 25), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =780 , y =580 )

window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()


window1 = Tk()
window1.geometry("1000x700")
window1.title("Decode Image Game")

top1 = Label(window1, text="DECODE IMAGE GAME", font=("Arial", 50, "underline"), fg="magenta")
top1.place(x = 120, y = 10)

top1 = Label(window1, text="SELECT LEVEL", font=("Arial", 45), fg="brown")
top1.place(x = 250, y = 110)

def level1_fun():
    def check_fun():
        ans = str(ans_entry.get())
        if(ans == "FACEBOOK"):
            mbox.showinfo("Right Answer", "Congratulation, Your Answer is Correct!")
        else:
            mbox.showerror("Wrong Answer", "Your Answer is wrong.\n\nCorrect Answer is FACEBOOK")

    f1 = Frame(window1, width=1000, height=700)
    f1.propagate(0)
    f1.pack(side='top')

    c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
    c1.pack()
    p1 = PhotoImage(file="Images/img1.gif")
    c1.create_image(220, 150, image=p1, anchor="nw")
    w1 = Canvas(window1)
    w1.p1 = p1

    top1 = Label(f1, text="LEVEL - 1", font=("Arial", 55, "underline"), fg="magenta", bg = "white")
    top1.place(x=310, y=10)

    top1 = Label(f1, text="Answer  :  ", font=("Arial", 40), fg="brown", bg="white")
    top1.place(x=150, y=500)

    ans_entry = Entry(f1, font=("Arial", 35), fg='orange', bg="light yellow", borderwidth=3, width=15)
    ans_entry.place(x=400, y=500)

    startb = Button(f1, text="CHECK", command=check_fun, font=("Arial", 25), bg="orange", fg="blue",borderwidth=3, relief="raised")
    startb.place(x=420, y=590)

def level2_fun():
    def check_fun():
        ans = str(ans_entry.get())
        if (ans == "EARRING"):
            mbox.showinfo("Right Answer", "Congratulation, Your Answer is Correct!")
        else:
            mbox.showerror("Wrong Answer", "Your Answer is wrong.\n\nCorrect Answer is EARRING")

    f1 = Frame(window1, width=1000, height=700)
    f1.propagate(0)
    f1.pack(side='top')

    c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
    c1.pack()
    p1 = PhotoImage(file="Images/img2.gif")
    c1.create_image(220, 150, image=p1, anchor="nw")
    w1 = Canvas(window1)
    w1.p1 = p1

    top1 = Label(f1, text="LEVEL - 2", font=("Arial", 55, "underline"), fg="magenta", bg="white")
    top1.place(x=310, y=10)

    top1 = Label(f1, text="Answer  :  ", font=("Arial", 40), fg="brown", bg="white")
    top1.place(x=150, y=500)

    ans_entry = Entry(f1, font=("Arial", 35), fg='orange', bg="light yellow", borderwidth=3, width=15)
    ans_entry.place(x=400, y=500)

    startb = Button(f1, text="CHECK", command=check_fun, font=("Arial", 25), bg="orange", fg="blue", borderwidth=3,
                    relief="raised")
    startb.place(x=420, y=590)

def level3_fun():
    def check_fun():
        ans = str(ans_entry.get())
        if (ans == "HOTDOG"):
            mbox.showinfo("Right Answer", "Congratulation, Your Answer is Correct!")
        else:
            mbox.showerror("Wrong Answer", "Your Answer is wrong.\n\nCorrect Answer is HOTDOG")

    f1 = Frame(window1, width=1000, height=700)
    f1.propagate(0)
    f1.pack(side='top')

    c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
    c1.pack()
    p1 = PhotoImage(file="Images/img3.gif")
    c1.create_image(220, 150, image=p1, anchor="nw")
    w1 = Canvas(window1)
    w1.p1 = p1

    top1 = Label(f1, text="LEVEL - 3", font=("Arial", 55, "underline"), fg="magenta", bg="white")
    top1.place(x=310, y=10)

    top1 = Label(f1, text="Answer  :  ", font=("Arial", 40), fg="brown", bg="white")
    top1.place(x=150, y=500)

    ans_entry = Entry(f1, font=("Arial", 35), fg='orange', bg="light yellow", borderwidth=3, width=15)
    ans_entry.place(x=400, y=500)

    startb = Button(f1, text="CHECK", command=check_fun, font=("Arial", 25), bg="orange", fg="blue", borderwidth=3,
                    relief="raised")
    startb.place(x=420, y=590)

def level4_fun():
    def check_fun():
        ans = str(ans_entry.get())
        if (ans == "GOLDFISH"):
            mbox.showinfo("Right Answer", "Congratulation, Your Answer is Correct!")
        else:
            mbox.showerror("Wrong Answer", "Your Answer is wrong.\n\nCorrect Answer is GOLDFISH")

    f1 = Frame(window1, width=1000, height=700)
    f1.propagate(0)
    f1.pack(side='top')

    c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
    c1.pack()
    p1 = PhotoImage(file="Images/img4.gif")
    c1.create_image(220, 150, image=p1, anchor="nw")
    w1 = Canvas(window1)
    w1.p1 = p1

    top1 = Label(f1, text="LEVEL - 4", font=("Arial", 55, "underline"), fg="magenta", bg="white")
    top1.place(x=310, y=10)

    top1 = Label(f1, text="Answer  :  ", font=("Arial", 40), fg="brown", bg="white")
    top1.place(x=150, y=500)

    ans_entry = Entry(f1, font=("Arial", 35), fg='orange', bg="light yellow", borderwidth=3, width=15)
    ans_entry.place(x=400, y=500)

    startb = Button(f1, text="CHECK", command=check_fun, font=("Arial", 25), bg="orange", fg="blue", borderwidth=3,
                    relief="raised")
    startb.place(x=420, y=590)

def level5_fun():
    def check_fun():
        ans = str(ans_entry.get())
        if (ans == "SANDWICH"):
            mbox.showinfo("Right Answer", "Congratulation, Your Answer is Correct!")
        else:
            mbox.showerror("Wrong Answer", "Your Answer is wrong.\n\nCorrect Answer is SANDWICH")

    f1 = Frame(window1, width=1000, height=700)
    f1.propagate(0)
    f1.pack(side='top')

    c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
    c1.pack()
    p1 = PhotoImage(file="Images/img5.gif")
    c1.create_image(220, 150, image=p1, anchor="nw")
    w1 = Canvas(window1)
    w1.p1 = p1

    top1 = Label(f1, text="LEVEL - 5", font=("Arial", 55, "underline"), fg="magenta", bg="white")
    top1.place(x=310, y=10)

    top1 = Label(f1, text="Answer  :  ", font=("Arial", 40), fg="brown", bg="white")
    top1.place(x=150, y=500)

    ans_entry = Entry(f1, font=("Arial", 35), fg='orange', bg="light yellow", borderwidth=3, width=15)
    ans_entry.place(x=400, y=500)

    startb = Button(f1, text="CHECK", command=check_fun, font=("Arial", 25), bg="orange", fg="blue", borderwidth=3,
                    relief="raised")
    startb.place(x=420, y=590)

def level6_fun():
    def check_fun():
        ans = str(ans_entry.get())
        if (ans == "BEANBAG"):
            mbox.showinfo("Right Answer", "Congratulation, Your Answer is Correct!")
        else:
            mbox.showerror("Wrong Answer", "Your Answer is wrong.\n\nCorrect Answer is BEANBAG")

    f1 = Frame(window1, width=1000, height=700)
    f1.propagate(0)
    f1.pack(side='top')

    c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
    c1.pack()
    p1 = PhotoImage(file="Images/img6.gif")
    c1.create_image(220, 150, image=p1, anchor="nw")
    w1 = Canvas(window1)
    w1.p1 = p1

    top1 = Label(f1, text="LEVEL - 6", font=("Arial", 55, "underline"), fg="magenta", bg="white")
    top1.place(x=310, y=10)

    top1 = Label(f1, text="Answer  :  ", font=("Arial", 40), fg="brown", bg="white")
    top1.place(x=150, y=500)

    ans_entry = Entry(f1, font=("Arial", 35), fg='orange', bg="light yellow", borderwidth=3, width=15)
    ans_entry.place(x=400, y=500)

    startb = Button(f1, text="CHECK", command=check_fun, font=("Arial", 25), bg="orange", fg="blue", borderwidth=3,
                    relief="raised")
    startb.place(x=420, y=590)

def level7_fun():
    def check_fun():
        ans = str(ans_entry.get())
        if (ans == "FOOTBALL"):
            mbox.showinfo("Right Answer", "Congratulation, Your Answer is Correct!")
        else:
            mbox.showerror("Wrong Answer", "Your Answer is wrong.\n\nCorrect Answer is FOOTBALL")

    f1 = Frame(window1, width=1000, height=700)
    f1.propagate(0)
    f1.pack(side='top')

    c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
    c1.pack()
    p1 = PhotoImage(file="Images/img7.gif")
    c1.create_image(220, 150, image=p1, anchor="nw")
    w1 = Canvas(window1)
    w1.p1 = p1

    top1 = Label(f1, text="LEVEL - 7", font=("Arial", 55, "underline"), fg="magenta", bg="white")
    top1.place(x=310, y=10)

    top1 = Label(f1, text="Answer  :  ", font=("Arial", 40), fg="brown", bg="white")
    top1.place(x=150, y=500)

    ans_entry = Entry(f1, font=("Arial", 35), fg='orange', bg="light yellow", borderwidth=3, width=15)
    ans_entry.place(x=400, y=500)

    startb = Button(f1, text="CHECK", command=check_fun, font=("Arial", 25), bg="orange", fg="blue", borderwidth=3,
                    relief="raised")
    startb.place(x=420, y=590)

def level8_fun():
    def check_fun():
        ans = str(ans_entry.get())
        if (ans == "RAINBOW"):
            mbox.showinfo("Right Answer", "Congratulation, Your Answer is Correct!")
        else:
            mbox.showerror("Wrong Answer", "Your Answer is wrong.\n\nCorrect Answer is RAINBOW")

    f1 = Frame(window1, width=1000, height=700)
    f1.propagate(0)
    f1.pack(side='top')

    c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
    c1.pack()
    p1 = PhotoImage(file="Images/img8.gif")
    c1.create_image(220, 150, image=p1, anchor="nw")
    w1 = Canvas(window1)
    w1.p1 = p1

    top1 = Label(f1, text="LEVEL - 8", font=("Arial", 55, "underline"), fg="magenta", bg="white")
    top1.place(x=310, y=10)

    top1 = Label(f1, text="Answer  :  ", font=("Arial", 40), fg="brown", bg="white")
    top1.place(x=150, y=500)

    ans_entry = Entry(f1, font=("Arial", 35), fg='orange', bg="light yellow", borderwidth=3, width=15)
    ans_entry.place(x=400, y=500)

    startb = Button(f1, text="CHECK", command=check_fun, font=("Arial", 25), bg="orange", fg="blue", borderwidth=3,
                    relief="raised")
    startb.place(x=420, y=590)



startb = Button(window1, text="LEVEL\n1",command=level1_fun,font=("Arial", 25), bg = "gray", fg = "blue", borderwidth=3, relief="raised")
startb.place(x =90 , y =240 )

startb = Button(window1, text="LEVEL\n2",command=level2_fun,font=("Arial", 25), bg = "white", fg = "blue", borderwidth=3, relief="raised")
startb.place(x =320 , y =240 )

startb = Button(window1, text="LEVEL\n3",command=level3_fun,font=("Arial", 25), bg = "gray", fg = "blue", borderwidth=3, relief="raised")
startb.place(x =550 , y =240 )

startb = Button(window1, text="LEVEL\n4",command=level4_fun,font=("Arial", 25), bg = "white", fg = "blue", borderwidth=3, relief="raised")
startb.place(x =780 , y =240 )

startb = Button(window1, text="LEVEL\n5",command=level5_fun,font=("Arial", 25), bg = "white", fg = "blue", borderwidth=3, relief="raised")
startb.place(x =90 , y =400 )

startb = Button(window1, text="LEVEL\n6",command=level6_fun,font=("Arial", 25), bg = "gray", fg = "blue", borderwidth=3, relief="raised")
startb.place(x =320 , y =400 )

startb = Button(window1, text="LEVEL\n7",command=level7_fun,font=("Arial", 25), bg = "white", fg = "blue", borderwidth=3, relief="raised")
startb.place(x =550 , y =400 )

startb = Button(window1, text="LEVEL\n8",command=level8_fun,font=("Arial", 25), bg = "gray", fg = "blue", borderwidth=3, relief="raised")
startb.place(x =780 , y =400 )

def score_fun():
    print()

def rules_fun():
    mbox.showinfo("Rules", "1.)  There are 8 levels.\n\n2.)  For each level two image with + sign between them will be shown.\n\n3.)  For each level player needs to enter the correct word representing the combination of both image.\n\n4.)  Player can check whether he/she has answered correct or not using CHECK button.")

# startb = Button(window1, text="SCORE",command=score_fun,font=("Arial", 25), bg = "yellow", fg = "blue", borderwidth=3, relief="raised")
# startb.place(x =120 , y =580 )

startb = Button(window1, text="RULES",command=rules_fun,font=("Arial", 25), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
startb.place(x =200 , y =580 )


def exit_win1():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window1.destroy()

exitb = Button(window1, text="EXIT",command=exit_win1,font=("Arial", 25), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =680 , y =580 )

window1.protocol("WM_DELETE_WINDOW", exit_win1)
window1.mainloop()

