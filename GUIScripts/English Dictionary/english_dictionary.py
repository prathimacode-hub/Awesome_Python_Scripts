import io # used for dealing with input and output
from tkinter import *      #importing the necessary libraries
import tkinter.messagebox as mbox
import tkinter as tk  # imported tkinter as tk
import json
from difflib import get_close_matches
import pandas as pd
import pyttsx3
import speech_recognition as sr
import pyaudio

# ------------------------------------------------------------------------------------------------------------------
data = pd.read_csv('Related/words.csv')
autocompleteList = data['Words'].tolist()

class AutocompleteEntry(Entry):
    def __init__(self, autocompleteList, *args, **kwargs):

        # Listbox length
        if 'listboxLength' in kwargs:
            self.listboxLength = kwargs['listboxLength']
            del kwargs['listboxLength']
        else:
            self.listboxLength = 10

        # Custom matches function
        if 'matchesFunction' in kwargs:
            self.matchesFunction = kwargs['matchesFunction']
            del kwargs['matchesFunction']
        else:
            def matches(fieldValue, acListEntry):
                pattern = re.compile('.*' + re.escape(fieldValue) + '.*', re.IGNORECASE)
                return re.match(pattern, acListEntry)

            self.matchesFunction = matches

        Entry.__init__(self, *args, **kwargs)
        self.focus()

        self.autocompleteList = autocompleteList

        self.var = self["textvariable"]
        if self.var == '':
            self.var = self["textvariable"] = StringVar()

        self.var.trace('w', self.changed)
        self.bind("<Right>", self.selection)
        self.bind("<Up>", self.moveUp)
        self.bind("<Down>", self.moveDown)

        self.listboxUp = False

    def changed(self, name, index, mode):
        if self.var.get() == '':
            if self.listboxUp:
                self.listbox.destroy()
                self.listboxUp = False
        else:
            words = self.comparison()
            if words:
                if not self.listboxUp:
                    self.listbox = Listbox(width=self["width"], height=self.listboxLength)
                    self.listbox.bind("<Button-1>", self.selection)
                    self.listbox.bind("<Right>", self.selection)
                    self.listbox.place(x=self.winfo_x(), y=self.winfo_y() + self.winfo_height())
                    self.listboxUp = True

                self.listbox.delete(0, END)
                for w in words:
                    self.listbox.insert(END, w)
            else:
                if self.listboxUp:
                    self.listbox.destroy()
                    self.listboxUp = False

    def selection(self, event):
        if self.listboxUp:
            self.var.set(self.listbox.get(ACTIVE))
            self.listbox.destroy()
            self.listboxUp = False
            self.icursor(END)

    def moveUp(self, event):
        if self.listboxUp:
            if self.listbox.curselection() == ():
                index = '0'
            else:
                index = self.listbox.curselection()[0]

            if index != '0':
                self.listbox.selection_clear(first=index)
                index = str(int(index) - 1)

                self.listbox.see(index)  # Scroll!
                self.listbox.selection_set(first=index)
                self.listbox.activate(index)

    def moveDown(self, event):
        if self.listboxUp:
            if self.listbox.curselection() == ():
                index = '0'
            else:
                index = self.listbox.curselection()[0]

            if index != END:
                self.listbox.selection_clear(first=index)
                index = str(int(index) + 1)

                self.listbox.see(index)  # Scroll!
                self.listbox.selection_set(first=index)
                self.listbox.activate(index)

    def comparison(self):
        return [w for w in self.autocompleteList if self.matchesFunction(self.var.get(), w)]

def matches(fieldValue, acListEntry):
    pattern = re.compile(re.escape(fieldValue) + '.*', re.IGNORECASE)
    return re.match(pattern, acListEntry)

# entry = AutocompleteEntry(autocompleteList, f1, listboxLength=6, width=32, matchesFunction=matches)
# entry.place(x=0, y=0)
# ------------------------------------------------------------------------------------------------------------------

data = json.load(open("Related/data.json"))       #loading and storing the data from json file

# input text to speech
def in_text_to_speech(**kwargs):
    if 'text' in kwargs:
        text = kwargs['text']
    else:
        text = inputentry.get() # get text content
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    # in_b.configure(command=read_text)

# output text to speech
def out_text_to_speech(**kwargs):
    if 'text' in kwargs:
        text = kwargs['text']
    else:
        text = outputtxt.get(1.0, 'end') # get text content
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    # out_b.configure(command=read_text)

def input_speech():
    r = sr.Recognizer()
    inputentry.delete(0, END)
    inputentry.insert(0, "Listening... Speak now...")
    with sr.Microphone() as source:
        # print("Listening... Speak now...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            inputentry.delete(0, END)
            inputentry.insert(0,text)
            # print("You said : {}".format(text))
        except:
            inputentry.delete(0, END)
            inputentry.insert(0, "Didn't get that. Try again...")

# function defined th=o clear both the input text and output text --------------------------------------------------
def clear_text():
    inputentry.delete(0, END)
    outputtxt.delete("1.0","end")

def search_word():
    word = inputentry.get()
    # word = inputtxt.get("1.0", "end-1c")  # first we get the word from the inputtxt and store it in word variable
    # print(word)
    word = word.lower()  # converting word into lowercase

    # CASE 1 : If input text area is empty, and clicked on search button
    if word == "":
        # lbl.config(text="You Entered Nothing! Please Enter Some Text.")

        buffer = io.StringIO()  # we are creating a buffer
        print("You Entered Nothing! Please Enter Some Text.", file=buffer)  # then this message is displayed
        output = buffer.getvalue()
        outputtxt.delete('1.0', END)  # first clearing the previous output textarea
        outputtxt.insert(END, output)  # and then printing the new output
        buffer.flush()  # flushing the buffer we created

    # CASE 2 : if word is present in data
    elif word in data:
        str = ""
        cnt = 0
        for i in data[word]:  # we get output in list form , so we convert it into different line of string
            cnt = cnt + 1
            str_cnt = f'{cnt}'
            str += (str_cnt + ".) ")
            str += i
            str += "\n\n"
        # lbl.config(text = str)

        # and printing the string in th output
        buffer = io.StringIO()
        print("Meaning of word \"" + word + "\" : \n\n" + str, file=buffer)
        output = buffer.getvalue()
        outputtxt.delete('1.0', END)
        outputtxt.insert(END, output)
        buffer.flush()

    # CASE 3 : if word enetered is any noun or title
    elif word.title() in data:
        str = ""
        cnt = 0
        for i in data[word.title()]:  # first we convert to output list to string
            cnt = cnt + 1
            str_cnt = f'{cnt}'
            str += (str_cnt + ".) ")
            str += i
            str += "\n\n"
        # lbl.config(text = str)

        # print the output
        buffer = io.StringIO()
        print("Meaning of word \"" + word + "\" : \n\n" + str, file=buffer)
        output = buffer.getvalue()
        outputtxt.delete('1.0', END)
        outputtxt.insert(END, output)
        buffer.flush()

    # CASE 4 : if uppercase of word we entered is there in data
    elif word.upper() in data:
        str = ""
        cnt = 0
        for i in data[word.upper()]:
            cnt = cnt + 1
            str_cnt = f'{cnt}'
            str += (str_cnt + ".) ")
            str += i
            str += "\n\n"
        # lbl.config(text = str)

        buffer = io.StringIO()
        print("Meaning of word \"" + word + "\" : \n\n" + str, file=buffer)
        output = buffer.getvalue()
        outputtxt.delete('1.0', END)
        outputtxt.insert(END, output)
        buffer.flush()

    # CASE 5 : If word is not present in data, means we find the closest word which is in data and print its meaning
    elif len(get_close_matches(word, data.keys())) > 0:  # case of close matches
        suggested_word = ""
        for i in get_close_matches(word, data.keys())[0]:
            suggested_word += i
        suggested_meaning = ""
        cnt = 0
        for i in data[get_close_matches(word, data.keys())[0]]:
            cnt = cnt + 1
            str_cnt = f'{cnt}'
            suggested_meaning += (str_cnt + ".) ")
            suggested_meaning += i
            suggested_meaning += "\n\n"

        # lbl.config(text="Meaning of closest word \"" + suggested_word + "\" : " + suggested_meaning)

        buffer = io.StringIO()
        print("Meaning of closest word \"" + suggested_word + "\" : \n\n" + suggested_meaning, file=buffer)
        output = buffer.getvalue()
        outputtxt.delete('1.0', END)
        outputtxt.insert(END, output)
        buffer.flush()

    # CASE 6 : If it even failed to find the closest word also, then print that you have entered wrong word
    else:
        # lbl.config(text = "You have entered wrong word!")

        buffer = io.StringIO()
        print("You have entered some wrong word!", file=buffer)
        output = buffer.getvalue()
        outputtxt.delete('1.0', END)
        outputtxt.insert(END, output)
        buffer.flush()


window = tk.Tk()
window.title ("English Dictionary")
window.geometry('1000x500')
window.state('zoomed') # for default maximize way

# for writing Dictionary label, at the top of window
dic = tk.Label(text = "ENGLISH DICTIONARY", font=("Arial", 50), fg="magenta",underline=0) # same way bg
dic.place(x = 400, y = 10)

start1 = tk.Label(text = "Enter the text you want to search...", font=("Arial", 30), fg="green",underline=0) # same way bg
start1.place(x = 450, y = 100)

myname = StringVar(window)
firstclick1 = True
def on_inputentry_click(event):
    """function that gets called whenever entry1 is clicked"""
    global firstclick1

    if firstclick1: # if this is the first time they clicked it
        firstclick1 = False
        inputentry.delete(0, "end") # delete all the text in the entry


# Taking input from TextArea
# inputentry = Entry(window,font=("Arial", 35), width=33, border=2)
inputentry = AutocompleteEntry(autocompleteList, window,font=("Arial", 35) , width=33, border=2, matchesFunction=matches)
inputentry.insert(0, 'Enter the word you want to search...')
inputentry.bind('<FocusIn>', on_inputentry_click)
inputentry.place(x=320, y=160)

# # creating speech to text button
speech_in_b = Button(window,text="🎙",command= input_speech,font=("Arial", 18), bg = "light yellow", fg = "green", borderwidth=3, relief="raised").place(x = 1200, y = 163)

start2 = tk.Label(text = "Speak Up...", font=("Arial", 30), fg="green") # same way bg
start2.place(x = 1250, y = 163)

# # Creating Search Button
Button(window,text="🔍 SEARCH",command= search_word,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised").place(x = 370, y = 250)


# # creating clear button
Button(window,text="🧹 CLEAR",command= clear_text,font=("Arial", 20), bg = "orange", fg = "blue", borderwidth=3, relief="raised").place(x = 615, y = 250)

# # creating text to speech button
in_b = Button(window,text="🔊 TEXT TO SPEECH",command= in_text_to_speech,font=("Arial", 20), bg = "yellow", fg = "blue", borderwidth=3, relief="raised").place(x = 840, y = 250)

# # Output TextBox Creation
outputtxt = tk.Text(window,height = 15, width = 100, font=("Arial", 15), bg = "light yellow", fg = "brown", borderwidth=3, relief="solid")
outputtxt.place(x=200, y = 350)

def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

# # creating exit button
Button(window,text="❌ EXIT",command= exit_win,font=("Arial", 20), bg = "red", fg = "black", borderwidth=3, relief="raised").place(x = 1350, y = 20)

# # creating text to speech button
out_b = Button(window,text="🔊 TEXT TO SPEECH",command= out_text_to_speech,font=("Arial", 20), bg = "yellow", fg = "blue", borderwidth=3, relief="raised").place(x = 600, y = 720)


window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()
