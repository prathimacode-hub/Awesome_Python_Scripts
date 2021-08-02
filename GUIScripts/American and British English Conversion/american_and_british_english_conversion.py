
# American and British English Conversion

# imported necessary library
import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
from PIL import ImageTk, Image
import requests
import cv2


# created main window
window = Tk()
window.geometry("1000x700")
window.title("American and British English Conversion")


# image on the main window
path = "Images/front.jpg"
# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img1 = ImageTk.PhotoImage(Image.open(path))
# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image = img1)
panel.place(x = 125, y = 200)

# top label
start1 = tk.Label(text = "AMERICAN & BRITISH\nENGLISH", font=("Arial", 50), fg="magenta") # same way bg
start1.place(x = 150, y = 10)

# function defined to start the application
def start_fun():
    window.destroy()

# created start button
startb = Button(window, text="START",command=start_fun,font=("Arial", 30), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
startb.place(x = 100, y =550 )

# function defined to show cheatsheet when clicking on button
def cheat_fun():
    img = cv2.imread("Images/cheatsheet.jpg", 1)
    cv2.imshow("Conversion Cheatsheet", img)

# created start button
startb = Button(window, text="CHEATSHEET",command=cheat_fun,font=("Arial", 30), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
startb.place(x = 360, y =550 )

# function for exiting
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

# created exit button
exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 30), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =770 , y =550 )


window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()


# created main window
window1 = Tk()
window1.geometry("1000x700")
window1.title("American and British English Conversion")

# function defined to convert from American English to British English
def am_to_bt():
    input_text = str(text_am.get("1.0", "end-1c"))

    url = "https://raw.githubusercontent.com/hyperreality/American-British-English-Translator/master/data/american_spellings.json"
    american_to_british_dict = requests.get(url).json()

    for american_spelling, british_spelling in american_to_british_dict.items():
        input_text = input_text.replace(american_spelling, british_spelling)

    text_bt.delete("1.0", "end")
    text_bt.insert(END, input_text)

# function defined to convert from British English to American English
def bt_to_am():
    input_text = str(text_bt.get("1.0", "end-1c"))

    url = "https://raw.githubusercontent.com/hyperreality/American-British-English-Translator/master/data/british_spellings.json"
    british_to_american_dict = requests.get(url).json()

    for british_spelling, american_spelling in british_to_american_dict.items():
        input_text = input_text.replace(british_spelling, american_spelling)

    text_am.delete("1.0", "end")
    text_am.insert(END, input_text)


# top label
start1 = tk.Label(window1, text = "AMERICAN & BRITISH ENGLISH", font=("Arial", 45), fg="magenta") # same way bg
start1.place(x = 50, y = 10)

# top second label
enter_label = Label(window1, text="American English", font=("Arial", 30),fg="brown")
enter_label.place(x=100,y=90)

# top second label
enter_label = Label(window1, text="British English", font=("Arial", 30),fg="brown")
enter_label.place(x=600,y=90)

# created text area
text_am = tk.Text(window1, height=18, width=37, font=("Arial", 15), bg="light yellow", fg="brown",borderwidth=3, relief="solid")
text_am.place(x=50, y=150)

# created text area
text_bt = tk.Text(window1, height=18, width=37, font=("Arial", 15), bg="light yellow", fg="brown",borderwidth=3, relief="solid")
text_bt.place(x=530, y=150)

# created start button
startb = Button(window1, text="AMER. to BRIT.",command=am_to_bt,font=("Arial", 25), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
startb.place(x = 80, y =600 )

# created start button
startb = Button(window1, text="BRIT. to AMER.",command=bt_to_am,font=("Arial", 25), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
startb.place(x = 430, y =600 )

# function for exiting
def exit_win1():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window1.destroy()

# created exit button
exitb = Button(window1, text="EXIT",command=exit_win1,font=("Arial", 25), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =800 , y =600 )


window1.protocol("WM_DELETE_WINDOW", exit_win1)
window1.mainloop()