
# MORSE CODE TRANSLATOR

# imported necessary library
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
from pil import ImageTk, Image
import cv2


# created main window
window = Tk()
window.geometry("1000x700")
window.title("Morse Code Translator")


# image on the main window
path = "Images/front.jpg"
# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img1 = ImageTk.PhotoImage(Image.open(path))
# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image = img1)
panel.place(x = 110, y = 200)

# top label
start1 = tk.Label(text = "MORSE   -   CODE\nTRANSLATOR", font=("Arial", 55), fg="magenta") # same way bg
start1.place(x = 170, y = 10)

# function defined to start the application
def start_fun():
    window.destroy()

# created start button
startb = Button(window, text="START",command=start_fun,font=("Arial", 30), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
startb.place(x = 100, y =580 )

# function defined to show cheatsheet when clicking on button
def cheat_fun():
    img = cv2.imread("Images/cheatsheet.jpg", 1)
    cv2.imshow("Morse Code Cheatsheet", img)

# created start button
startb = Button(window, text="CHEATSHEET",command=cheat_fun,font=("Arial", 30), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
startb.place(x = 360, y =580 )

# function for exiting
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

# created exit button
exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 30), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =770 , y =580 )


window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()


# created main window
window1 = Tk()
window1.geometry("1000x700")
window1.title("Morse Code Translator")

temp_dict = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----', ', ':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-', '(':'-.--.', ')':'-.--.-'}

# function defined to convert from American English to British English
def morse_encode():
    input_text = str(text_en.get("1.0", "end-1c"))
    input_text = input_text.upper()

    encode_ans = ''
    for letter in input_text:
        if letter != ' ':
            encode_ans += temp_dict[letter] + ' '
        else:
            encode_ans += ' '

    text_de.delete("1.0", "end")
    text_de.insert(END, encode_ans)

# function defined to convert from British English to American English
def morse_decode():
    input_text = str(text_de.get("1.0", "end-1c"))

    input_text += ' '

    deccode_ans = ''
    temp = ''
    for letter in input_text:
        if (letter != ' '):
            i = 0
            temp += letter

        # in case of space
        else:
            i += 1
            if i == 2:
                deccode_ans += ' '
            else:
                deccode_ans += list(temp_dict.keys())[list(temp_dict.values()).index(temp)]
                temp = ''

    text_en.delete("1.0", "end")
    text_en.insert(END, deccode_ans)


# top label
start1 = tk.Label(window1, text = "MORSE CODE TRANSLATOR", font=("Arial", 45), fg="magenta") # same way bg
start1.place(x = 80, y = 10)

# top second label
enter_label = Label(window1, text="Normal  Text", font=("Arial", 30),fg="brown")
enter_label.place(x=120,y=90)

# top second label
enter_label = Label(window1, text="Morse  Code", font=("Arial", 30),fg="brown")
enter_label.place(x=620,y=90)

# created text area
text_en = tk.Text(window1, height=13, width=28, font=("Arial", 20), bg="light yellow", fg="brown",borderwidth=3, relief="solid")
text_en.place(x=50, y=150)

# created text area
text_de = tk.Text(window1, height=13, width=28, font=("Arial", 20), bg="light yellow", fg="brown",borderwidth=3, relief="solid")
text_de.place(x=530, y=150)

# created start button
startb = Button(window1, text="Morse Encode",command=morse_encode,font=("Arial", 25), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
startb.place(x = 80, y =600 )

# created start button
startb = Button(window1, text="Morse Decode",command=morse_decode,font=("Arial", 25), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
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