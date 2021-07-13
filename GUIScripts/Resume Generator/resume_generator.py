
# Resume Generator

# imported necessary library
import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
from PIL import Image, ImageTk
from fpdf import FPDF
import webbrowser

# main window created
window = Tk()
window.geometry("1000x700")
window.title("Resume Generator")


# defined function for start button
def def_start():
    def basic_fun():
        def enter_fun():
            global basic
            basic = text_enter.get("1.0", END)
            window1.destroy()

        # created main window
        window1 = Tk()
        window1.geometry("1000x700")
        window1.title("BASIC DETAILS")

        # for top label
        top1 = tk.Label(window1, text="Basic Info", font=("Arial", 50), fg="green")  # same way bg
        top1.place(x=330, y=10)

        # Taking input of code from TextArea
        text_enter = tk.Text(window1, height=13, width=48, font=("Arial", 20), bg="light blue", fg="blue", borderwidth=3,relief="solid")
        text_enter.place(x=120, y=110)

        def clear_text():
            text_enter.delete("1.0", END)

        # created button for clear
        clearb = Button(window1, text="CLEAR", command=clear_text, font=("Arial", 25), bg="light green", fg="blue",borderwidth=3, relief="raised")
        clearb.place(x=200, y=580)

        # created button for enter
        enterb = Button(window1, text="ENTER", command=enter_fun, font=("Arial", 25), bg="light green", fg="blue",borderwidth=3, relief="raised")
        enterb.place(x=650, y=580)

    def edu_fun():
        def enter_fun():
            global edu
            edu = text_enter.get("1.0", END)
            window1.destroy()

        # created main window
        window1 = Tk()
        window1.geometry("1000x700")
        window1.title("EDUCATION DETAILS")

        # for top label
        top1 = tk.Label(window1, text="Education", font=("Arial", 50), fg="green")  # same way bg
        top1.place(x=340, y=10)

        # Taking input of code from TextArea
        text_enter = tk.Text(window1, height=13, width=48, font=("Arial", 20), bg="light blue", fg="blue",
                             borderwidth=3, relief="solid")
        text_enter.place(x=120, y=110)

        def clear_text():
            text_enter.delete("1.0", END)

        # created button for clear
        clearb = Button(window1, text="CLEAR", command=clear_text, font=("Arial", 25), bg="light green", fg="blue",
                        borderwidth=3, relief="raised")
        clearb.place(x=200, y=580)

        # created button for enter
        enterb = Button(window1, text="ENTER", command=enter_fun, font=("Arial", 25), bg="light green", fg="blue",
                        borderwidth=3, relief="raised")
        enterb.place(x=650, y=580)

    def skill_fun():
        def enter_fun():
            global skill
            skill = text_enter.get("1.0", END)
            window1.destroy()

        # created main window
        window1 = Tk()
        window1.geometry("1000x700")
        window1.title("SKILLS DETAILS")

        # for top label
        top1 = tk.Label(window1, text="Skills", font=("Arial", 50), fg="green")  # same way bg
        top1.place(x=390, y=10)

        # Taking input of code from TextArea
        text_enter = tk.Text(window1, height=13, width=48, font=("Arial", 20), bg="light blue", fg="blue",
                             borderwidth=3, relief="solid")
        text_enter.place(x=120, y=110)

        def clear_text():
            text_enter.delete("1.0", END)

        # created button for clear
        clearb = Button(window1, text="CLEAR", command=clear_text, font=("Arial", 25), bg="light green", fg="blue",
                        borderwidth=3, relief="raised")
        clearb.place(x=200, y=580)

        # created button for enter
        enterb = Button(window1, text="ENTER", command=enter_fun, font=("Arial", 25), bg="light green", fg="blue",
                        borderwidth=3, relief="raised")
        enterb.place(x=650, y=580)

    def exp_fun():
        def enter_fun():
            global exp
            exp = text_enter.get("1.0", END)
            window1.destroy()

        # created main window
        window1 = Tk()
        window1.geometry("1000x700")
        window1.title("EXPERIENCE DETAILS")

        # for top label
        top1 = tk.Label(window1, text="Experience", font=("Arial", 50), fg="green")  # same way bg
        top1.place(x=340, y=10)

        # Taking input of code from TextArea
        text_enter = tk.Text(window1, height=13, width=48, font=("Arial", 20), bg="light blue", fg="blue",
                             borderwidth=3, relief="solid")
        text_enter.place(x=120, y=110)

        def clear_text():
            text_enter.delete("1.0", END)

        # created button for clear
        clearb = Button(window1, text="CLEAR", command=clear_text, font=("Arial", 25), bg="light green", fg="blue",
                        borderwidth=3, relief="raised")
        clearb.place(x=200, y=580)

        # created button for enter
        enterb = Button(window1, text="ENTER", command=enter_fun, font=("Arial", 25), bg="light green", fg="blue",
                        borderwidth=3, relief="raised")
        enterb.place(x=650, y=580)

    def proj_fun():
        def enter_fun():
            global proj
            proj = text_enter.get("1.0", END)
            window1.destroy()

        # created main window
        window1 = Tk()
        window1.geometry("1000x700")
        window1.title("PROJECTS DETAILS")

        # for top label
        top1 = tk.Label(window1, text="Projects", font=("Arial", 50), fg="green")  # same way bg
        top1.place(x=370, y=10)

        # Taking input of code from TextArea
        text_enter = tk.Text(window1, height=13, width=48, font=("Arial", 20), bg="light blue", fg="blue",
                             borderwidth=3, relief="solid")
        text_enter.place(x=120, y=110)

        def clear_text():
            text_enter.delete("1.0", END)

        # created button for clear
        clearb = Button(window1, text="CLEAR", command=clear_text, font=("Arial", 25), bg="light green", fg="blue",
                        borderwidth=3, relief="raised")
        clearb.place(x=200, y=580)

        # created button for enter
        enterb = Button(window1, text="ENTER", command=enter_fun, font=("Arial", 25), bg="light green", fg="blue",
                        borderwidth=3, relief="raised")
        enterb.place(x=650, y=580)

    def canda_fun():
        def enter_fun():
            global canda
            canda = text_enter.get("1.0", END)
            window1.destroy()

        # created main window
        window1 = Tk()
        window1.geometry("1000x700")
        window1.title("CERTIFICATES AND AWARDS DETAILS")

        # for top label
        top1 = tk.Label(window1, text="Certificates and Awards", font=("Arial", 50), fg="green")  # same way bg
        top1.place(x=130, y=10)

        # Taking input of code from TextArea
        text_enter = tk.Text(window1, height=13, width=48, font=("Arial", 20), bg="light blue", fg="blue",
                             borderwidth=3, relief="solid")
        text_enter.place(x=120, y=110)

        def clear_text():
            text_enter.delete("1.0", END)

        # created button for clear
        clearb = Button(window1, text="CLEAR", command=clear_text, font=("Arial", 25), bg="light green", fg="blue",
                        borderwidth=3, relief="raised")
        clearb.place(x=200, y=580)

        # created button for enter
        enterb = Button(window1, text="ENTER", command=enter_fun, font=("Arial", 25), bg="light green", fg="blue",
                        borderwidth=3, relief="raised")
        enterb.place(x=650, y=580)

    def link_fun():
        def enter_fun():
            global link
            link = text_enter.get("1.0", END)
            window1.destroy()

        # created main window
        window1 = Tk()
        window1.geometry("1000x700")
        window1.title("LINKS DETAILS")

        # for top label
        top1 = tk.Label(window1, text="Important Links", font=("Arial", 50), fg="green")  # same way bg
        top1.place(x=250, y=10)

        # Taking input of code from TextArea
        text_enter = tk.Text(window1, height=13, width=48, font=("Arial", 20), bg="light blue", fg="blue",
                             borderwidth=3, relief="solid")
        text_enter.place(x=120, y=110)

        def clear_text():
            text_enter.delete("1.0", END)

        # created button for clear
        clearb = Button(window1, text="CLEAR", command=clear_text, font=("Arial", 25), bg="light green", fg="blue",
                        borderwidth=3, relief="raised")
        clearb.place(x=200, y=580)

        # created button for enter
        enterb = Button(window1, text="ENTER", command=enter_fun, font=("Arial", 25), bg="light green", fg="blue",
                        borderwidth=3, relief="raised")
        enterb.place(x=650, y=580)

    def handi_fun():
        def enter_fun():
            global handi
            handi = text_enter.get("1.0", END)
            window1.destroy()

        # created main window
        window1 = Tk()
        window1.geometry("1000x700")
        window1.title("HOBBIES AND INTERESTS DETAILS")

        # for top label
        top1 = tk.Label(window1, text="Hobbies and Interests", font=("Arial", 50), fg="green")  # same way bg
        top1.place(x=150, y=10)

        # Taking input of code from TextArea
        text_enter = tk.Text(window1, height=13, width=48, font=("Arial", 20), bg="light blue", fg="blue",
                             borderwidth=3, relief="solid")
        text_enter.place(x=120, y=110)

        def clear_text():
            text_enter.delete("1.0", END)

        # created button for clear
        clearb = Button(window1, text="CLEAR", command=clear_text, font=("Arial", 25), bg="light green", fg="blue",
                        borderwidth=3, relief="raised")
        clearb.place(x=200, y=580)

        # created button for enter
        enterb = Button(window1, text="ENTER", command=enter_fun, font=("Arial", 25), bg="light green", fg="blue",
                        borderwidth=3, relief="raised")
        enterb.place(x=650, y=580)



    # function for generating and saving the PDF
    def def_PDF():

        pdf = FPDF(orientation='P', unit='mm', format='A4')
        pdf.add_page()

        pdf.set_font("helvetica","", 20)

        pdf.set_text_color(128,0,0)

        pdf.image('Images/My_Resume1.png', x=0, y=0, w=210, h=297)

        pdf.text(30, 30, basic)
        pdf.text(30, 62, edu)
        pdf.text(30, 90, skill)
        pdf.text(30, 130, exp)
        pdf.text(30, 160, proj)
        pdf.text(30, 205, canda)
        pdf.text(30, 235, link)
        pdf.text(30, 263, handi)

        pdf.output('My_Resume.pdf')
        mbox.showinfo("Resume Status", "Resume Generated and Saved Successfully.")

    # new frame created
    f1 = Frame(window, width=1000, height=700)
    f1.propagate(0)
    f1.pack(side='top')

    # for top label
    start1 = tk.Label(f1,text="RESUME GENERATOR", font=("Arial", 50), fg="magenta")  # same way bg
    start1.place(x=120, y=10)

    # for basic label
    basic1 = tk.Label(f1, text="Enter Your Basic Details  :  ", font=("Arial", 30), fg="green")  # same way bg
    basic1.place(x=100, y=100)
    # created button for here
    basicb = Button(window, text="HERE", command=basic_fun, font=("Arial", 17), bg="light green", fg="blue",borderwidth=3, relief="raised")
    basicb.place(x=800, y=100)

    # for education label
    edu1 = tk.Label(f1, text="Enter Your Education  :  ", font=("Arial", 30), fg="green")  # same way bg
    edu1.place(x=100, y=160)
    # created button for education
    edub = Button(window, text="HERE", command=edu_fun, font=("Arial", 17), bg="light green", fg="blue", borderwidth=3,relief="raised")
    edub.place(x=800, y=160)

    # for skill label
    skill1 = tk.Label(f1, text="Enter Your Skills  :  ", font=("Arial", 30), fg="green")  # same way bg
    skill1.place(x=100, y=220)
    # created button for skill
    skillb = Button(window, text="HERE", command=skill_fun, font=("Arial", 17), bg="light green", fg="blue", borderwidth=3,relief="raised")
    skillb.place(x=800, y=220)

    # for Experience label
    exp1 = tk.Label(f1, text="Enter Your Experience  :  ", font=("Arial", 30), fg="green")  # same way bg
    exp1.place(x=100, y=280)
    # created button for Experience
    expb = Button(window, text="HERE", command=exp_fun, font=("Arial", 17), bg="light green", fg="blue", borderwidth=3,relief="raised")
    expb.place(x=800, y=280)

    # for Projects label
    proj1 = tk.Label(f1, text="Enter Your Projects  :  ", font=("Arial", 30), fg="green")  # same way bg
    proj1.place(x=100, y=340)
    # created button for Projects
    projb = Button(window, text="HERE", command=proj_fun, font=("Arial", 17), bg="light green", fg="blue", borderwidth=3,relief="raised")
    projb.place(x=800, y=340)

    # for Certificates & Awards label
    canda1 = tk.Label(f1, text="Enter Your Certificates & Awards  :  ", font=("Arial", 30), fg="green")  # same way bg
    canda1.place(x=100, y=400)
    # created button for Certificates & Awards
    candab = Button(window, text="HERE", command=canda_fun, font=("Arial", 17), bg="light green", fg="blue", borderwidth=3,relief="raised")
    candab.place(x=800, y=400)

    # for Links label
    link1 = tk.Label(f1, text="Enter Important Links  :  ", font=("Arial", 30), fg="green")  # same way bg
    link1.place(x=100, y=460)
    # created button for Links
    linkb = Button(window, text="HERE", command=link_fun, font=("Arial", 17), bg="light green", fg="blue", borderwidth=3,relief="raised")
    linkb.place(x=800, y=460)

    # for Hobbies & Interests label
    handi1 = tk.Label(f1, text="Enter Your Hobbies & Interests  :  ", font=("Arial", 30), fg="green")  # same way bg
    handi1.place(x=100, y=520)
    # created button for Hobbies & Interests
    handib = Button(window, text="HERE", command=handi_fun, font=("Arial", 17), bg="light green", fg="blue", borderwidth=3,relief="raised")
    handib.place(x=800, y=520)

    # created button for generating RESUME
    pdfb = Button(window, text="GENERATE RESUME", command=def_PDF, font=("Arial", 25), bg="orange", fg="blue",borderwidth=3, relief="raised")
    pdfb.place(x=300, y=590)


# top label
start1 = tk.Label(text = "RESUME GENERATOR", font=("Arial", 55), fg="magenta") # same way bg
start1.place(x = 90, y = 10)

# image on the main window
path = "Images/resume_front.png"
# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))
# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image = img)
panel.place(x = 340, y = 150)

# created start button
startb = Button(window, text="START",command=def_start,font=("Arial", 30), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
startb.place(x =100 , y =570 )

#Define a callback function
def callback(url):
   webbrowser.open_new_tab(url)

# created EMI button
templateb = Button(window, text="TEMPLATE",command=lambda:callback("https://novoresume.com/resume-templates"),font=("Arial", 30), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
templateb.place(x =370 , y =570 )

# function for exiting
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

# created exit button
exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 30), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =730 , y =570 )


window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()