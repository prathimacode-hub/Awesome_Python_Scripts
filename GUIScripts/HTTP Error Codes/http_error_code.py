
# HTTP Error Code

# imported necessary library
import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
import json

# created main window
window = Tk()
window.geometry("1000x700")
window.title("HTTP Error Code")

# ------------------ this is for adding gif image in the main window of application ---------------------------------------
frameCnt = 3
frames = [PhotoImage(file='Images/front.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

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
label.place(x = 170, y = 150)
window.after(0, update, 0)
# --------------------------------------------------------------------


#loaded json data
data1 = json.load(open("code_data.json"))
code = data1["code"]
category = data1["category"]
term = data1["term"]
meaning = data1["meaning"]

# print(len(code))
# print(len(category))
# print(len(term))
# print(len(meaning))

def start_fun():
    def get_info():
        selected_code = code_var.get()
        for i in range(0,len(code)):
            if(code[i] == selected_code):
                mbox.showinfo(selected_code + " HTTP Code Info", "HTTP Code  :  " + str(selected_code) + "\n\n1.)  Category  :  " + str(category[i]) + "\n\n2.)  Terms  :  " + str(term[i]) + "\n\n3.)  Meanings  :  " + str(meaning[i]))


    f1 = Frame(window, width=1000, height=700)
    f1.propagate(0)
    f1.pack(side='top')

    c1 = Canvas(f1, width=1000, height=700)  # blue
    c1.pack()
    p1 = PhotoImage(file="Images/second.gif")
    c1.create_image(50, 120, image=p1, anchor="nw")
    w1 = Canvas(window)
    w1.p1 = p1

    # top label
    start1 = tk.Label(f1, text="HTTP ERROR CODE", font=("Arial", 55), fg="magenta")  # same way bg
    start1.place(x=120, y=10)

    # top label
    lbl1 = tk.Label(f1, text="Select Error Code  :  ", font=("Arial", 35), fg="brown")  # same way bg
    lbl1.place(x=180, y=420)

    # creating the drop down menu button for selectng hour
    code_var = tk.StringVar()
    # as icon size are really small, we defined the following 7 sizes
    code_choices = code
    code_menu = OptionMenu(window, code_var, *code_choices)
    code_menu.config(font=("Arial", 30), bg = "light green", fg = "blue", borderwidth=3)
    code_menu["menu"].config(font=("Arial", 15), bg = "light yellow", fg = "blue")
    code_menu.place(x=630, y=415)
    code_var.set("100") # size 1 is selected as by default, and we can

    # created exit button
    getb = Button(window, text="GET - INFO", command=get_info, font=("Arial", 25), bg="light green", fg="blue",borderwidth=3, relief="raised")
    getb.place(x=120, y=550)

    # function for reseting
    def reset_fun():
        code_var.set("100")

    # created exit button
    resetb = Button(window, text="RESET", command=reset_fun, font=("Arial", 25), bg="orange", fg="blue",borderwidth=3, relief="raised")
    resetb.place(x=460, y=550)

    # function for exiting
    def exit_fun():
        if mbox.askokcancel("Exit", "Do you want to exit?"):
            window.destroy()

    # created exit button
    exitb = Button(window, text="EXIT", command=exit_fun, font=("Arial", 25), bg="red", fg="blue",borderwidth=3, relief="raised")
    exitb.place(x=750, y=550)



# top label
start1 = tk.Label(text="HTTP ERROR CODE", font=("Arial", 55), fg="magenta")  # same way bg
start1.place(x=120, y=10)

# created exit button
startb = Button(window, text="START", command=start_fun, font=("Arial", 25), bg="light green", fg="blue", borderwidth=3, relief="raised")
startb.place(x=120, y=580)

# function for exiting
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

# created exit button
exitb = Button(window, text="EXIT", command=exit_win, font=("Arial", 25), bg="red", fg="blue", borderwidth=3, relief="raised")
exitb.place(x=750, y=580)


window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()
