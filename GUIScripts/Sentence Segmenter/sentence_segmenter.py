
# Sentence Segmenter

# imported necessary library
import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
import re


# created main window
window = Tk()
window.geometry("1000x700")
window.title("Sentence Segmenter")

s = ""
def sentence_segment():
    global s
    s = ""
    input_text = text_enter.get("1.0", "end-1c")

    text_list = list(input_text)
    n = len(text_list)

    pointer = 0
    quotes_open = False
    single_quotes_open = False
    word_pointer = 0

    for i in range(n):
        letter = text_list[i]
        next_letter = text_list[i + 1] if i + 1 < n else '~'
        prev_letter = text_list[i - 1] if i - 1 > 0 else '~'
        word_length = i - word_pointer

        if letter == "." and not quotes_open and not single_quotes_open and next_letter != "." and word_length > 1 and (
                word_length > 2 or text_list[word_pointer].islower()):
            s = s + "".join(text_list[pointer:(i + 1)]).lstrip().rstrip() + "\n\n"
            pointer = i + 1
        elif letter in ["!", "?"] and not quotes_open:
            s = s + "".join(text_list[pointer:(i + 1)]).lstrip().rstrip() + "\n\n"
            pointer = i + 1
        elif letter == '"':
            quotes_open = not quotes_open
        elif letter == "'" and prev_letter == " ":
            single_quotes_open = True
        elif letter == "'" and next_letter == " ":
            single_quotes_open = False
        elif letter == " ":
            word_pointer = i + 1
    if pointer + 1 < n:
        s = s + "".join(text_list[pointer:(n + 1)]).lstrip().rstrip() + "\n\n"

    # created main window
    window1 = Tk()
    window1.geometry("1000x700")
    window1.title("Sentence Segmenter")

    # top label
    start1 = tk.Label(window1,text="SENTENCE SEGMENTER", font=("Arial", 55), fg="magenta")  # same way bg
    start1.place(x=50, y=10)

    # second label
    sec1 = tk.Label(window1,text="Sentence After Segmenting...", font=("Arial", 30), fg="brown")  # same way bg
    sec1.place(x=200, y=100)

    # created text area
    text_enter1 = tk.Text(window1, height=18, width=75, font=("Arial", 15), bg="light yellow", fg="brown", borderwidth=3,relief="solid")
    text_enter1.place(x=80, y=150)
    text_enter1.insert(END, s)

    def close_new():
        window1.destroy()

    # created close button
    closeb = Button(window1, text="CLOSE", command=close_new, font=("Arial", 25), bg="orange", fg="blue",borderwidth=3, relief="raised")
    closeb.place(x=400, y=600)

# top label
start1 = tk.Label(text = "SENTENCE SEGMENTER", font=("Arial", 55), fg="magenta") # same way bg
start1.place(x = 50, y = 10)

# second label
sec1 = tk.Label(text="Enter Any Paragraph and Segment it...", font=("Arial", 30), fg="brown")  # same way bg
sec1.place(x=150, y=100)

# created text area
text_enter = tk.Text(window, height=18, width=75, font=("Arial", 15), bg="light yellow", fg="brown", borderwidth=3,relief="solid")
text_enter.place(x=80, y=150)

# function for clearing the entry box
def clear_text():
    text_enter.delete("1.0", END)

# created check button
checkb = Button(window, text="SEGMENT",command=sentence_segment,font=("Arial", 25), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
checkb.place(x =150 , y =600 )

# created clear button
clearb = Button(window,text="CLEAR", command=clear_text, font=("Arial", 25), bg="orange", fg="blue",borderwidth=3, relief="raised")
clearb.place(x=470, y=600)


# function for exiting
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

# created exit button
exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 25), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =740 , y =600 )


window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()