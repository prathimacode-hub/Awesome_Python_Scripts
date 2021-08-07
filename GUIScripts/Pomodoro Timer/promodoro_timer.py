
# POMODORO TIMER

# imported necessary library
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
from pil import ImageTk, Image
import time


# created main window
window = Tk()
window.geometry("1000x700")
window.title("Pomodoro Timer")


# image on the main window
path = "Images/front.jpg"
# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img1 = ImageTk.PhotoImage(Image.open(path))
# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image = img1)
panel.place(x =60, y = 110)

# top label
start1 = tk.Label(text = "POMODORO TIMER", font=("Arial", 55, "underline"), fg="magenta") # same way bg
start1.place(x = 140, y = 10)

# function defined to start the application
def start_fun():
    window.destroy()

# created start button
startb = Button(window, text="START",command=start_fun,font=("Arial", 30), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
startb.place(x = 200, y =580 )


# function for exiting
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

# created exit button
exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 30), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =670 , y =580 )


window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()


# created main window
window1 = Tk()
window1.geometry("1000x700")
window1.title("Pomodoro Timer")


# function defined to convert from American English to British English
def process_fun():
    global carry_on
    carry_on = 'y'
    def start_timer():
        # global carry_on
        # while carry_on == 'y' or carry_on == 'Y':
        #     tasks(input_text)
        #     breaks()
        #     carry_on = input("Do you want ot carry on?(y/n)")
        # print("End of task ", input_text, ". \nTotal time worked was minutes ", total_mins, " minutes.")
        print()

    def status_fun():
        mbox.showinfo("Work Status", "Task has ended.\n\nTotal time worked  :  25 mins.\n\nTotal break time  :  3 mins.")

    input_text = str(task.get("1.0", "end-1c"))
    lb1.configure(text = "Pomodoro Timer Ready.")
    lb2.configure(text="Timer for task " + input_text + " is 25 mins.")

    startb = Button(window1, text="START TIMER",command=start_timer,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
    startb.place(x = 400, y =380 )

    startb = Button(window1, text="STATUS", command=status_fun, font=("Arial", 25), bg="orange", fg="blue",borderwidth=3, relief="raised")
    startb.place(x=150, y=600)

    minute = StringVar()
    second = StringVar()

    minuteEntry = Entry(window1, width=2, font=("Arial", 70, ""),textvariable=minute)
    minuteEntry.place(x=500, y=470)

    # top second label
    Label(window1, text = ":", font=("Arial", 70), fg="black").place(x=640, y=470)

    secondEntry = Entry(window1, width=2, font=("Arial", 70, ""),textvariable=second)
    secondEntry.place(x=700, y=470)

    # for work time counter ------------------------------------
    # top second label
    Label(window1, text="WORK  - ", font=("Arial", 70), fg="black").place(x=50, y=470)

    minute.set("25")
    second.set("00")

    try:
        temp = int(minute.get()) * 60 + int(second.get())
    except:
        print("Please input the right value")
    while temp > -1:
        mins, secs = divmod(temp, 60)
        hours = 0
        if mins > 60:
            hours, mins = divmod(mins, 60)
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))
        window1.update()
        time.sleep(1)
        if (temp == 0):
            mbox.showinfo("Pomodoro Timer Status", "Pomodoro has ended.\n\nTake a short break of 3 mins.")

        # after every one sec the value of temp will be decremented
        # by one
        temp -= 1
    # -----------------------------------------------------------------------

    # for work time counter ------------------------------------
    # top second label
    Label(window1, text="        ", font=("Arial", 70), fg="black").place(x=50, y=470)
    Label(window1, text="BREAK - ", font=("Arial", 70), fg="black").place(x=50, y=470)

    minute.set("03")
    second.set("00")

    try:
        temp = int(minute.get()) * 60 + int(second.get())
    except:
        print("Please input the right value")
    while temp > -1:
        mins, secs = divmod(temp, 60)
        hours = 0
        if mins > 60:
            hours, mins = divmod(mins, 60)
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))
        window1.update()
        time.sleep(1)
        if (temp == 0):
            mbox.showinfo("Break Status", "Break is Over.\n\nGo for some other task if you want.")

        # after every one sec the value of temp will be decremented
        # by one
        temp -= 1
    # -----------------------------------------------------------------------




# top label
start1 = tk.Label(window1, text = "POMODORO TIMER", font=("Arial", 50, "underline"), fg="magenta") # same way bg
start1.place(x = 170, y = 10)

# top second label
enter_label = Label(window1, text="Be More Productive...", font=("Arial", 30),fg="green")
enter_label.place(x=280,y=90)

# top second label
enter_label = Label(window1, text="Task to work on :  ", font=("Arial", 30),fg="brown")
enter_label.place(x=50,y=170)

# created text area
task = tk.Text(window1, height=1, width=20, font=("Arial", 25), bg="light yellow", fg="brown",borderwidth=2, relief="solid")
task.place(x=380, y=172)

# created start button
startb = Button(window1, text="ENTER",command=process_fun,font=("Arial", 17), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
startb.place(x = 760, y =170 )

# top second label
lb1 = Label(window1, font=("Arial", 30),fg="gray")
lb1.place(x=280,y=230)

# top second label
lb2 = Label(window1, font=("Arial", 30),fg="gray")
lb2.place(x=220,y=290)

# top second label
lb3 = Label(window1, font=("Arial", 60),fg="gray")
lb3.place(x=300,y=410)


# # created start button
# startb = Button(window1, text="Morse Decode",command=morse_decode,font=("Arial", 25), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
# startb.place(x = 430, y =600 )

# function for exiting
def exit_win1():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window1.destroy()

# created exit button
exitb = Button(window1, text="EXIT",command=exit_win1,font=("Arial", 25), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =750 , y =600 )


window1.protocol("WM_DELETE_WINDOW", exit_win1)
window1.mainloop()