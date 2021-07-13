
# Regex Checker

# imported necessary library
import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
import re


# created main window
window = Tk()
window.geometry("1000x700")
window.title("Regex Checker")

# ---------------------------------------------------------
frameCnt = 3
frames = [PhotoImage(file='Images/regex.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

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
label.place(x = 100, y = 120)
window.after(0, update, 0)
# --------------------------------------------------------------------

def start_fun():
    def regex_check():
        try:
            s = str(regex_enter.get("1.0", END))
            re.compile(s)
        except:
            mbox.showerror("Regex Check Error", "Entered Regex is Incorrect!\n\nAs it generated exception on compile() method.")
            return
        mbox.showinfo("Regex Check Status", "Entered Regex is Correct!\n\nAs it runs through compile() method.")

    # created main frame
    f1 = Frame(window, width=1000, height=700)
    f1.propagate(0)
    f1.pack(side='top')

    # top label
    start1 = tk.Label(f1,text="REGEX CHECKER", font=("Arial", 55), fg="magenta")  # same way bg
    start1.place(x=165, y=10)

    # second label
    sec1 = tk.Label(f1,text="Enter Any Regex and Check its Correctness...", font=("Arial", 30), fg="brown")  # same way bg
    sec1.place(x=90, y=100)

    # created text area
    regex_enter = tk.Text(f1, height=18, width=75, font=("Arial", 15), bg="light yellow", fg="brown", borderwidth=3,relief="solid")
    regex_enter.place(x=80, y=150)

    # function for clearing the entry box
    def clear_entry():
        regex_enter.delete("1.0", END)

    # created check button
    checkb = Button(f1, text="REGEX - CHECK",command=regex_check,font=("Arial", 25), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
    checkb.place(x =150 , y =600 )

    # created clear button
    clearb = Button(f1, text="CLEAR", command=clear_entry, font=("Arial", 25), bg="orange", fg="blue",borderwidth=3, relief="raised")
    clearb.place(x=670, y=600)


# top label
start1 = tk.Label(text = "REGEX CHECKER", font=("Arial", 55), fg="magenta") # same way bg
start1.place(x = 180, y = 10)

# created start button
startb = Button(window, text="START",command=start_fun,font=("Arial", 25), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
startb.place(x = 200, y =550 )

# function for exiting
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

# created exit button
exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 25), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =680 , y =550 )


window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()