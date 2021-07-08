
# EMI Calculator

# imported necessary library
import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
from PIL import Image, ImageTk
from fpdf import FPDF

# main window created
window = Tk()
window.geometry("1000x700")
window.title("EMI Calculator")

# variable defined
firstclick1 = True
firstclick2 = True
firstclick3 = True
firstclick4 = True
firstclick5 = True
firstclick6 = True
cal_emi = 0


# defined function for start button
def def_start():
    def on_e1_click(event):
        """function that gets called whenever entry1 is clicked"""
        global firstclick1
        if firstclick1:  # if this is the first time they clicked it
            firstclick1 = False
            e1.delete(0, "end")  # delete all the text in the entry

    def on_e2_click(event):
        """function that gets called whenever entry1 is clicked"""
        global firstclick2
        if firstclick2:  # if this is the first time they clicked it
            firstclick2 = False
            e2.delete(0, "end")  # delete all the text in the entry

    def on_e3_click(event):
        """function that gets called whenever entry1 is clicked"""
        global firstclick3
        if firstclick3:  # if this is the first time they clicked it
            firstclick3 = False
            e3.delete(0, "end")  # delete all the text in the entry

    def on_e4_click(event):
        """function that gets called whenever entry1 is clicked"""
        global firstclick4
        if firstclick4:  # if this is the first time they clicked it
            firstclick4 = False
            e4.delete(0, "end")  # delete all the text in the entry

    def on_e5_click(event):
        """function that gets called whenever entry1 is clicked"""
        global firstclick5
        if firstclick5:  # if this is the first time they clicked it
            firstclick5 = False
            e5.delete(0, "end")  # delete all the text in the entry

    def on_e6_click(event):
        """function that gets called whenever entry1 is clicked"""
        global firstclick6
        if firstclick6:  # if this is the first time they clicked it
            firstclick6 = False
            e6.delete(0, "end")  # delete all the text in the entry

    # function for generating and saving the PDF
    def def_PDF():
        pdf = FPDF(orientation='P', unit='mm', format='A4')
        pdf.add_page()

        pdf.set_font("helvetica","", 20)

        pdf.set_text_color(0, 0, 0)

        pdf.image('Images/EMI_pdf.png', x=0, y=0, w=210, h=297)

        pdf.text(55, 129, e1.get())
        pdf.text(70, 142, e2.get())
        pdf.text(60, 155, e3.get())

        pdf.text(78, 197, str(e4.get()))
        pdf.text(96, 210, str(e5.get()))
        pdf.text(93, 223, str(e6.get()))

        pdf.text(91, 264, str(cal_emi))

        pdf.output('EMI_Calculated.pdf')
        mbox.showinfo("PDF Status", "PDF Generated and Saved Successfully.")

    # function for calculating the EMI
    def def_cal():
        global cal_emi
        p = int(e4.get())
        r = int(e5.get())
        n = int(e6.get())
        cal_emi = p * (r / 1200) * ((1 + r / 1200) ** n) / (((1 + r / 1200) ** n) - 1)
        mbox.showinfo("EMI DETAILS", "Your Monthly Payment  :  " + str(cal_emi))

    # function for getting user details
    def def_details():
        mbox.showinfo("User Details", "Name  :  " + str(e1.get()) + "\n\nMobile No.  :  " + str(e2.get()) + "\n\nEmail ID  :  " + str(e3.get()))

    # new frame created
    f1 = Frame(window, width=1000, height=700)
    f1.propagate(0)
    f1.pack(side='top')

    # for top label
    start1 = tk.Label(f1,text="EMI  CALCULATOR", font=("Arial", 50), fg="magenta")  # same way bg
    start1.place(x=180, y=10)

    # created entry for Name
    l1 = Label(f1, text='Name', font=("Arial", 25), fg="brown")
    l1.place(x=100, y=140)
    e1 = Entry(f1, width = 30,border=2,font=("Arial", 22), bg = "light yellow")
    e1.insert(0, 'Enter Your Name...')
    e1.bind('<FocusIn>', on_e1_click)
    e1.place(x=300, y=143)

    # created entry for Mobile No
    l2 = Label(f1, text='Mobile No.', font=("Arial", 25), fg="brown")
    l2.place(x=100, y=200)
    e2 = Entry(f1, width = 30,border=2,font=("Arial", 22), bg = "light yellow")
    e2.insert(0, 'Enter Your Contact...')
    e2.bind('<FocusIn>', on_e2_click)
    e2.place(x=300, y=203)

    # created entry for Email O=ID
    l3 = Label(f1, text='Email Id', font=("Arial", 25), fg="brown")
    l3.place(x=100, y=260)
    e3 = Entry(f1, width = 30,border=2,font=("Arial", 22), bg = "light yellow")
    e3.insert(0, 'Enter Your Email Id...')
    e3.bind('<FocusIn>', on_e3_click)
    e3.place(x=300, y=263)

    # created entry for Loan Amount
    l4 = Label(f1, text='Loan Amount', font=("Arial", 25), fg="brown")
    l4.place(x=100, y=380)
    e4 = Entry(f1, width=30, border=2, font=("Arial", 22), bg = "light yellow")
    e4.insert(0, 'Enter Your Loan Amount...')
    e4.bind('<FocusIn>', on_e4_click)
    e4.place(x=400, y=383)

    # created entry for Interest Per Annum
    l5 = Label(f1, text='Interest Per Annum', font=("Arial", 25), fg="brown")
    l5.place(x=100, y=440)
    e5 = Entry(f1, width=30, border=2, font=("Arial", 22), bg = "light yellow")
    e5.insert(0, 'Enter Your Interest Per Annum...')
    e5.bind('<FocusIn>', on_e5_click)
    e5.place(x=400, y=443)

    # created entry for Period In Months
    l6 = Label(f1, text='Period In Months', font=("Arial", 25), fg="brown")
    l6.place(x=100, y=500)
    e6 = Entry(f1, width=30, border=2, font=("Arial", 22), bg = "light yellow")
    e6.insert(0, 'Enter Your Period In Months...')
    e6.bind('<FocusIn>', on_e6_click)
    e6.place(x=400, y=503)

    # created button for calculate EMI
    calb = Button(window, text="CALCULATE EMI", command=def_cal, font=("Arial", 20), bg="light green", fg="blue",borderwidth=3, relief="raised")
    calb.place(x=80, y=590)

    # created button for user details
    userb = Button(window, text="USER DETAILS", command=def_details, font=("Arial", 20), bg="orange", fg="blue",borderwidth=3, relief="raised")
    userb.place(x=390, y=590)

    # created button for generating PDF
    pdfb = Button(window, text="GENERATE PDF", command=def_PDF, font=("Arial", 20), bg="red", fg="blue",borderwidth=3, relief="raised")
    pdfb.place(x=700, y=590)

# function for showing EMI INFO
def def_emi():
    mbox.showinfo("EMI INFO", "EMI, which stands for Equated Monthly Installment, is the monthly amount payments we make towards a loan we opted for.\n\nEMI payments include contributions towards both principal and interest on the loan amount.\n\nThe mathematical formula to calculate EMI is: EMI = P × r × (1 + r)n/((1 + r)n - 1) where P= Loan amount, r= interest rate, n=tenure in number of months.")


# top label
start1 = tk.Label(text = "EMI  CALCULATOR", font=("Arial", 50), fg="magenta") # same way bg
start1.place(x = 180, y = 10)

# image on the main window
path = "Images/emi_front.jpg"
# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img1 = ImageTk.PhotoImage(Image.open(path))
# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image = img1)
panel.place(x = 200, y = 140)

# created start button
startb = Button(window, text="START",command=def_start,font=("Arial", 30), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
startb.place(x =100 , y =580 )

# created EMI button
emib = Button(window, text="EMI INFO",command=def_emi,font=("Arial", 30), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
emib.place(x =390 , y =580 )

# function for exiting
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

# created exit button
exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 30), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =730 , y =580 )


window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()