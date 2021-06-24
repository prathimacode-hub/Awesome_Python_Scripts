
# Part Of Speech Calculator

import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
stop_words = set(stopwords.words('english'))
# print(stop_words)
import pandas as pd

# ------------------------------------------------------------------------------------------------------------------
data = pd.read_csv('words.csv')
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

def search_text():
    search_entered = inputentry.get()
    entered = text_enter.get("1.0", "end-1c")
    # print(entered)

    # --------------------------------------------------------------------------------------------------
    text_enter.tag_config("red_tag", foreground="green", underline=1)

    # word length use as offset to get end position for tag
    offset = '+%dc' % len(search_entered)  # +5c (5 chars)

    # search word from first char (1.0) to the end of text (END)
    pos_start = text_enter.search(search_entered, '1.0', END)

    # check if found the word
    while pos_start:
        # create end position by adding (as string "+5c") number of chars in searched word
        pos_end = pos_start + offset

        # print(pos_start, pos_end)  # 1.6 1.6+5c :for first `World`

        # add tag
        text_enter.tag_add('red_tag', pos_start, pos_end)

        # search again from pos_end to the end of text (END)
        pos_start = text_enter.search(search_entered, pos_end, END)
    #---------------------------------------------------------------------------------------------------


    word_in_entered = []
    pos_in_entered = []
    tokenized = sent_tokenize(entered)
    for i in tokenized:
        wordsList = nltk.word_tokenize(i)
        wordsList = [w for w in wordsList if not w in stop_words]
        tagged = nltk.pos_tag(wordsList)
        for word, pos in tagged:
            word_in_entered.append(word)
            pos_in_entered.append(pos)

    # print(len(word_in_entered), len(pos_in_entered))
    # print(word_in_entered)
    # print(pos_in_entered)

    visited = {}

    search_idx = "" # to store index
    search_pos = "" # to store tag of POF
    search_cnt = 0
    for i in range(0,len(word_in_entered)):
        if(word_in_entered[i] == search_entered):
            search_idx = search_idx + str(i)
            search_idx = search_idx + "  ,  in "

            if (pos_in_entered[i] == 'NN' or pos_in_entered[i] == 'NNP' or pos_in_entered[i] == 'NNS' or pos_in_entered[i] == 'NNPS'):  # noun
                pos_in_entered[i] = "Noun"
            if (pos_in_entered[i] == 'PRP'):  # pronoun
                pos_in_entered[i] = "Pronoun"
            if (pos_in_entered[i] == 'VB' or pos_in_entered[i] == 'VBD' or pos_in_entered[i] == 'VBG' or pos_in_entered[i] == 'VBN' or pos_in_entered[i] == 'VBP' or pos_in_entered[i] == 'VBZ'):  # verb
                pos_in_entered[i] = "Verb"
            if (pos_in_entered[i] == 'JJ' or pos_in_entered[i] == 'JJR' or pos_in_entered[i] == 'JJS'):  # adjective
                pos_in_entered[i] = "Adjective"
            if (pos_in_entered[i] == 'RB' or pos_in_entered[i] == 'RBR' or pos_in_entered[i] == 'RBS'):  # adverb
                pos_in_entered[i] = "Adverb"
            if (pos_in_entered[i] == 'IN'):  # prepositon
                pos_in_entered[i] = "Preposition"
            if (pos_in_entered[i] == 'IN' or pos_in_entered[i] == 'CC'):  # conjunction
                pos_in_entered[i] = "Conjunction"
            if (pos_in_entered[i] == 'UH'):  # interjection
                pos_in_entered[i] = "Interjection"

            search_idx = search_idx + pos_in_entered[i]
            search_idx = search_idx + " form\n"
            # search_pos = search_pos + pos_in_entered[i]
            # search_pos = search_pos + "  ,  "
            # visited[pos_in_entered[i]] = True

            search_cnt = search_cnt + 1


    # mbox.showinfo("Search Implementation", "Search Word :\n" + search_entered + "\n\nNumber of times present :\n" + str(search_cnt) + "\n\nIndexes at which search word is present :\n" + search_idx + "\n\nThe form in which seach word is present are :\n" + search_pos)
    mbox.showinfo("Search Implementation", "Search Word :\n" + search_entered + "\n\nNumber of times present :\n" + str(search_cnt) + "\n\nIndexes and form of search word :\n" + search_idx)


window = Tk()
window.geometry("1000x700")
window.title("Search Implementation")
# window.iconbitmap(r"icon.ico")

# Taking input from TextArea
# inputentry = Entry(window,font=("Arial", 35), width=33, border=2)
inputentry = AutocompleteEntry(autocompleteList, window,font=("Arial", 25) , width=30, border=7, matchesFunction=matches)
inputentry.place(x=120, y=20)

# search button
pofb = Button(window, text="SEARCH",command=search_text,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
pofb.place(x =700 , y =20 )

enter_label = Label(window, text="Enter Your text or paragraph here and search text...", font=("Arial", 30),fg="brown")
enter_label.place(x=50,y=100)

text_enter = tk.Text(window, height=18, width=80, font=("Arial", 15), bg="light yellow", fg="brown",borderwidth=3, relief="solid")
text_enter.place(x=50, y=150)

def clear_text():
    inputentry.delete(0, END)
    text_enter.delete("1.0","end")

clearb = Button(window, text="CLEAR",command=clear_text,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
clearb.place(x =250 , y =600 )

def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 20), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =650 , y =600 )


window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()