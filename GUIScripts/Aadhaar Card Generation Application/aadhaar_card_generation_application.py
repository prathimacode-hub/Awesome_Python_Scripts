
# Aadhaar Card Generation Application

# imported necessary library
import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
from PIL import Image,ImageTk
from tkinter import filedialog
import os


# created main window
window = Tk()
window.geometry("1000x700")
window.title("Aadhaar Card Generation Application")

# ---------------------------------------------------------
frameCnt = 3
frames = [PhotoImage(file='Images/aadhaar_front.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

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
label.place(x = 150, y = 100)
window.after(0, update, 0)
# --------------------------------------------------------------------

def start_fun():
    def enroll_fun():
        onlyfilename = ""
        def open_img():
            global onlyfilename
            filename = filedialog.askopenfilename(title='"pen')
            # print(filename)
            onlyfilename = os.path.basename(filename)

            photo1 = tk.Label(f2, text=onlyfilename, font=("Arial", 20), fg="brown", bg="gray")  # same way bg
            photo1.place(x=635, y=350)

        def generate_fun():
            global name, dob, age, mno, gender,add,x
            name = name_entry.get()
            dob = dob_entry.get()
            age = age_entry.get()
            mno = mno_entry.get()
            gender = gen_entry.get()
            add = add_text.get("1.0", "end-1c")
            x = onlyfilename
            window1.destroy()
            # created main frame
            window2 = Tk()
            window2.geometry("1000x700")
            window2.title("Enrollment Form")

            # created main frame
            f3 = Frame(window2, width=1000, height=700)
            f3.propagate(0)
            f3.pack(side='top')

            # for images
            c3 = Canvas(f3, width=1000, height=700, bg="white")  # blue
            c3.pack()
            p3 = PhotoImage(file="Images/fourth_front.gif")
            c3.create_image(50, 100, image=p3, anchor="nw")
            w3 = Canvas(window2)
            w3.p3 = p3

            # top label
            start1 = tk.Label(f3, text="YOUR AADHAAR CARD", font=("Arial", 55), fg="magenta", bg="white")  # same way bg
            start1.place(x=70, y=10)

            Label(f3, text=name, font=("Arial", 20), fg="brown", bg="white").place(x=170, y=192)
            Label(f3, text=dob, font=("Arial", 20), fg="brown", bg="white").place(x=170, y=235)
            Label(f3, text=age, font=("Arial", 20), fg="brown", bg="white").place(x=150, y=282)
            Label(f3, text=mno, font=("Arial", 20), fg="brown", bg="white").place(x=215, y=325)
            Label(f3, text=gender, font=("Arial", 20), fg="brown", bg="white").place(x=188, y=370)
            add = add.split('\n')
            Label(f3, text=add[0], font=("Arial", 20), fg="brown", bg="white").place(x=190, y=418)
            Label(f3, text=add[1], font=("Arial", 20), fg="brown", bg="white").place(x=190, y=450)
            Label(f3, text=add[2], font=("Arial", 20), fg="brown", bg="white").place(x=190, y=482)
            Label(f3, text="4423 4412 5543 6678", font=("Arial", 20), fg="green", bg="white").place(x=300, y=530)
            Label(f3, text="img.jpg", font=("Arial", 20), fg="brown", bg="gray").place(x=750, y=330)

            mbox.showinfo("Generation Successful", "Aadhaar Card Generated Succesfully!")


        window.destroy()
        # created main frame
        window1 = Tk()
        window1.geometry("1000x700")
        window1.title("Enrollment Form")

        # created main frame
        f2 = Frame(window1, width=1000, height=700)
        f2.propagate(0)
        f2.pack(side='top')

        # for images
        c2 = Canvas(f2, width=1000, height=700, bg="white")  # blue
        c2.pack()
        p2 = PhotoImage(file="Images/third_front.gif")
        c2.create_image(200, 100, image=p2, anchor="nw")
        w2 = Canvas(window1)
        w2.p2 = p2

        # top label
        start1 = tk.Label(f2, text="ENROLLMENT FORM", font=("Arial", 55), fg="magenta", bg="white")  # same way bg
        start1.place(x=120, y=10)

        # Name Entry Box
        name_entry = Entry(f2, font=("Arial", 10), fg='brown', bg="light yellow", borderwidth=2, width=28)
        name_entry.place(x=350, y=297)

        # DOB Entry Box
        dob_entry = Entry(f2, font=("Arial", 10), fg='brown', bg="light yellow", borderwidth=2, width=28)
        dob_entry.place(x=350, y=325)

        # Age Entry Box
        age_entry = Entry(f2, font=("Arial", 10), fg='brown', bg="light yellow", borderwidth=2, width=28)
        age_entry.place(x=350, y=353)

        # mobile No. Entry Box
        mno_entry = Entry(f2, font=("Arial", 10), fg='brown', bg="light yellow", borderwidth=2, width=28)
        mno_entry.place(x=350, y=380)

        # Name Entry Box
        gen_entry = Entry(f2, font=("Arial", 10), fg='brown', bg="light yellow", borderwidth=2, width=28)
        gen_entry.place(x=350, y=405)

        add_text = tk.Text(f2, height=5, width=29, font=("Arial", 10), bg="light yellow", fg="brown",borderwidth=1, relief="solid")
        add_text.place(x=350, y=435)

        genb = Button(f2, text="GENERATE AADHAAR CARD", command=generate_fun, font=("Arial", 25), bg="orange", fg="blue",borderwidth=3, relief="raised")
        genb.place(x=230, y=590)

        # choose button created
        chooseb = Button(f2, text="Upload Photo", command=open_img, font=("Arial", 10), bg="yellow", fg="blue",borderwidth=3, relief="raised")
        chooseb.place(x=637, y=460)

    # created main frame
    f1 = Frame(window, width=1000, height=700)
    f1.propagate(0)
    f1.pack(side='top')

    # for images
    c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
    c1.pack()
    p1 = PhotoImage(file="Images/sec_front.gif")
    c1.create_image(280, 170, image=p1, anchor="nw")
    w1 = Canvas(window)
    w1.p1 = p1

    # top label
    start1 = tk.Label(f1, text="AADHAAR CARD", font=("Arial", 55), fg="magenta", bg = "white")  # same way bg
    start1.place(x=200, y=10)

    # second label
    start1 = tk.Label(f1, text="FILL  THE  ENROLLMENT  FORM", font=("Arial", 35), fg="brown", bg="white")  # same way bg
    start1.place(x=150, y=400)

    enrollb = Button(f1, text="ENROLLMENT FORM", command=enroll_fun, font=("Arial", 25), bg="light green", fg="blue", borderwidth=3,relief="raised")
    enrollb.place(x=310, y=500)

def details_fun():
    mbox.showinfo("Aadhaar Details", "What is Aadhaar :\n\n1.)  A 12-digit unique identity for every Indian individual, including children and infants.\n\n2.)  Enables identification for every resident Indian.\n\n3.)  Establishes uniqueness of every individual on the basis of demographic and biometric information.\n\n4.)  It is a voluntary service that every resident can avail irrespective of present documentation.\n\n5.)  Each individual will be given a single unique Aadhaar ID number.\n\n6.)  Aadhaar will provide a universal identity infrastructure which can be used by any identity-based application (like ration card, passport, etc.)\n\n7.)  UIDAI will give Yes/No answers to any identity authentication queries.")


# top label
start1 = tk.Label(text = "AADHAAR CARD", font=("Arial", 50), fg="magenta") # same way bg
start1.place(x = 230, y = 10)

startb = Button(window, text="START",command=start_fun,font=("Arial", 25), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
startb.place(x =110 , y =600 )

detailsb = Button(window, text="DETAILS",command=details_fun,font=("Arial", 25), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
detailsb.place(x =430 , y =600 )

def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 25), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =780 , y =600 )


window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()