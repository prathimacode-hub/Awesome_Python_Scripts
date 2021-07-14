
# Credit Card Numbers Authentication

# imported necessary library
import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
import re


# created main window
window = Tk()
window.geometry("1000x700")
window.title("Credit Card Numbers Authentication")

# ------------------ this is for adding gif image in the main window of application ---------------------------------------
frameCnt = 3
frames = [PhotoImage(file='Images/card.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

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
label.place(x = 120, y = 80)
window.after(0, update, 0)
# --------------------------------------------------------------------

# function for showing validity rules
def valid_fun():
    mbox.showinfo("Authentication Rules","A valid Credit Card Number need to fulfill following requirements :\n\n1.)  Must start with 4, 5 or 6.\n\n2.)  Must contains exactly 16 digits.\n\n3.)  Must consist of only digits from 0 - 9.\n\n4.)  Must have digits in groups of 4, separated by a hyphen '-'.\n\n5.)  Must NOT use any other separator like ' ' , '_', etc.\n\n6.)  Must not have 4 or more consecutive digits.")

# function to check authenticity of credit card number
def authenticate_fun():
    global valid
    entered_card = card_entry.get().strip()

    pre_match = re.search(r'^[456]\d{3}(-?)\d{4}\1\d{4}\1\d{4}$', entered_card)
    if pre_match:
        processed_string = "".join(pre_match.group(0).split('-'))
        final_match = re.search(r'(\d)\1{3,}', processed_string)
        if final_match:
            mbox.showerror("Authentication Error", "Entered Credit Card Number is NOT Authenticated.")
        else:
            mbox.showinfo("Authentication Success", "Entered Credit Card Number is Authenticated.")
    else:
        mbox.showerror("Authentication Error", "Entered Credit Card Number is NOT Authenticated.")


# top label
start1 = tk.Label(text = "Credit Card Numbers Authentication", font=("Arial", 45), fg="magenta") # same way bg
start1.place(x = 20, y = 10)

# Button for rules
vpcrb = Button(window, text="AUTHENTICATION RULES",command=valid_fun,font=("Arial", 25), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
vpcrb.place(x =250 , y =450 )

# label for Entering credit card number ---------------------------------------------------------------------------------
sel_label = tk.Label(text = "Enter Credit Card Number  : ", font=("Arial", 27), fg="brown") # same way bg
sel_label.place(x = 30, y = 540)

# Created Entry Box
card_entry = Entry(window, font=("Arial", 30), fg='orange', bg="light yellow", borderwidth=3, width=20)
card_entry.place(x=500, y=535)

# created Authenticate Button
authenticateb = Button(window, text="AUTHENTICATE",command=authenticate_fun,font=("Arial", 25), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
authenticateb.place(x =80 , y =600 )

# function for clearing the entry box
def clear_entry():
    card_entry.delete(0,END)

# created clear button
clearb = Button(window, text="CLEAR",command=clear_entry,font=("Arial", 25), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
clearb.place(x =510 , y =600 )

# function for exiting
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

# created exit button
exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 25), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =780 , y =600 )


window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()