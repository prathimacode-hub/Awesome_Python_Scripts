
# imported necessary library
from tkinter import *
from tkinter import messagebox
import tkinter.messagebox as mbox
import tkinter as tk

# created main window
root = Tk()
root.title("Virtual Copy Paste")
root.geometry('1000x700')

# frame 1 --------------------------- created frame 1 ------------------
def des_f1():
    f1.destroy()

# frame 1 created which is the main window
f1 = Frame(root, height=700, width=1000)
f1.propagate(0)
f1.pack(side='top')

# this is for adding image in the main window
c = Canvas(f1, width=1000, height=700)
c.pack()
p1 = PhotoImage(file='Images/copy_paste.gif')
c.create_image(0, 100, image=p1, anchor=NW)

# for starting label
start1 = Label(f1, text='VIRTUAL Copy Paste', font=("Arial", 50), fg="magenta", underline = 0)
start1.place(x=150, y=10)

# created a START button
startb = Button(f1, text="START",command=des_f1,font=("Arial", 30), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
startb.place(x = 180 , y =550 )
# ------------------------------------------------------

# frame 2 ---------------------------------------------
# created global variable s
s = ""

# function for clearing the default text from text1 when put cursor on it
firstclick1 = True
def on_text_enter_click(event):
    """function that gets called whenever entry1 is clicked"""
    global firstclick1
    if firstclick1:  # if this is the first time they clicked it
        firstclick1 = False
        text1.delete('1.0', "end")  # delete all the text in the entry

# function for copying the text
def copy_text():
    global s
    s = s + text1.get("1.0", "end-1c")

# function for seeing the copied text
def see_text():
    if(s == ""):
        mbox.showerror("Error", "You haven't copied anything!")
    else:
        mbox.showinfo("Copied Text", "COPIED TEXT :\n\n" + s)

# function for pasting the text
def paste_text():
    global s
    if (s == ""):
        mbox.showerror("Error", "You haven't copied anything!")
    else:
        text2.delete('1.0', END)
        text2.insert(END, s)
        s = ""

# created frame 2
f2 = Frame(root, height=700, width=1000)
f2.propagate(0)
f2.pack(side='top')

# created first textarea
text1 = tk.Text(f2, height=20, width=35, font=("Arial", 15), bg="light yellow", fg="brown",borderwidth=3, relief="solid")
text1.insert(END, 'Enter any text here and Copy it...') # default line in text area, can be cleared when touched
text1.bind('<FocusIn>', on_text_enter_click)
text1.place(x=50, y=20)

# created second textarea
text2 = tk.Text(f2, height=20, width=35, font=("Arial", 15), bg="light yellow", fg="brown",borderwidth=3, relief="solid")
text2.insert(END, 'Paste the copied text here...') # default line in text area, can be cleared when touched
text2.place(x=550, y=20)

# created COPY button
copyb = Button(f2, text="COPY",command=copy_text,font=("Arial", 30), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
copyb.place(x =100 , y =550 )

# Created SEE button
seeb = Button(f2, text="SEE",command=see_text,font=("Arial", 30), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
seeb.place(x =300 , y =550 )

# created a PASTE button
pasteb = Button(f2, text="PASTE",command=paste_text,font=("Arial", 30), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
pasteb.place(x =480 , y =550 )

# function for exiting
def exit_win():
    if messagebox.askokcancel("Exit", "Do you want to exit?"):
        root.destroy()

# created a exit button
exitb = Button(root, text="EXIT",command=exit_win,font=("Arial", 30), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =700 , y =550 )


root.protocol("WM_DELETE_WINDOW", exit_win)
root.mainloop()
