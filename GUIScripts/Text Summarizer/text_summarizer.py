
# Text Summarizer

# imported necessary library
import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
from PIL import Image, ImageTk
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize


# Main Window
frame = Tk()
frame.title('Text Summarizer')
frame.geometry('1000x700')
# frame.configure(bg = "white")


# image on the main window
path = "Images/front.jpg"
# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img1 = ImageTk.PhotoImage(Image.open(path))
# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(frame, image = img1)
panel.place(x = 110, y = 120)

# starting label
start1 = Label(frame, text='TEXT SUMMARIZER', font=("Arial", 55,"underline"),fg="magenta")
start1.place(x=140,y=10)

def start_fun():
    frame.destroy()

# creating an exit button
prevB = Button(frame, text='START', command=start_fun, font=("Arial", 25), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
prevB.place(x = 150, y = 600)

# defined exit_win function, to show a exit dialog box when tried to exit
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        frame.destroy()

# creating an exit button
prevB = Button(frame, text='EXIT', command=exit_win, font=("Arial", 25), bg = "red", fg = "blue", borderwidth=3, relief="raised")
prevB.place(x = 740, y = 600)

# this is done to show the exit dialog box when tried to exit from the main window, using the top-roght close button of titlebar
frame.protocol("WM_DELETE_WINDOW", exit_win)
frame.mainloop()

# created main window
window = Tk()
window.geometry("1000x700")
window.title("Text Summarizer")

s = ""
def summarize_fun():
    global s
    s = ""
    text = text_enter.get("1.0", "end-1c")

    # Tokenizing the text
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(text)

    # Creating a frequency table to keep the score of each word
    freqTable = dict()
    for word in words:
        word = word.lower()
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1

    # Creating a dictionary to keep the score of each sentence
    sentences = sent_tokenize(text)
    sentenceValue = dict()
    for sentence in sentences:
        for word, freq in freqTable.items():
            if word in sentence.lower():
                if sentence in sentenceValue:
                    sentenceValue[sentence] += freq
                else:
                    sentenceValue[sentence] = freq
    sumValues = 0
    for sentence in sentenceValue:
        sumValues += sentenceValue[sentence]
    # Average value of a sentence from the original text
    average = int(sumValues / len(sentenceValue))

    # Storing sentences into our summary.
    summary = ''
    for sentence in sentences:
        if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
            summary += " " + sentence


    # created main window
    window1 = Tk()
    window1.geometry("1000x700")
    window1.title("Text Summarizer")

    # top label
    start1 = tk.Label(window1,text="TEXT SUMMARIZER", font=("Arial", 55), fg="magenta")  # same way bg
    start1.place(x=140, y=10)

    # second label
    sec1 = tk.Label(window1,text="Text After Summarizing...", font=("Arial", 30), fg="brown")  # same way bg
    sec1.place(x=250, y=100)

    # created text area
    text_enter1 = tk.Text(window1, height=16, width=75, font=("Arial", 15), bg="light yellow", fg="brown", borderwidth=3,relief="solid")
    text_enter1.place(x=80, y=150)
    text_enter1.delete("1.0", "end")
    text_enter1.insert(END, summary)
    # mbox.showinfo("Success", "Paragraph or Text summarized successfully.\n\nLength of Original text  :  " + str(len(text)) + "\n\nLength of Summarized text  :  " + str(len(summary)))

    # second label
    sec1 = tk.Label(window1, text="Original Text Length       :  " + str(len(text)), font=("Arial", 30), fg="green")  # same way bg
    sec1.place(x=185, y=550)

    # second label
    sec1 = tk.Label(window1, text="Summarized Text Length  :  " + str(len(summary)), font=("Arial", 30), fg="green")  # same way bg
    sec1.place(x=150, y=610)

    # def close_new():
    #     window1.destroy()
    #
    # # created close button
    # closeb = Button(window1, text="CLOSE", command=close_new, font=("Arial", 25), bg="orange", fg="blue",borderwidth=3, relief="raised")
    # closeb.place(x=400, y=600)

# top label
start1 = tk.Label(text = "TEXT SUMMARIZER", font=("Arial", 55), fg="magenta") # same way bg
start1.place(x = 140, y = 10)

# second label
sec1 = tk.Label(text="Enter Any Paragraph/Text and Summarize it...", font=("Arial", 30), fg="brown")  # same way bg
sec1.place(x=100, y=100)

# created text area
text_enter = tk.Text(window, height=18, width=75, font=("Arial", 15), bg="light yellow", fg="brown", borderwidth=3,relief="solid")
text_enter.place(x=80, y=150)

# function for clearing the entry box
def clear_text():
    text_enter.delete("1.0", END)

# created check button
checkb = Button(window, text="SUMMARIZE",command=summarize_fun,font=("Arial", 25), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
checkb.place(x =150 , y =600 )

# created clear button
clearb = Button(window,text="CLEAR", command=clear_text, font=("Arial", 25), bg="orange", fg="blue",borderwidth=3, relief="raised")
clearb.place(x=480, y=600)


# function for exiting
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

# created exit button
exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 25), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =740 , y =600 )


window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()