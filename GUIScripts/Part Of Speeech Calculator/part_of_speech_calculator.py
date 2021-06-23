
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


def show_pof():
    mbox.showinfo("Parts Of Speech", "There are 8 parts of speech in the English language :\n\n1.)  Noun - NN, NNP, NNS, NNPS\n\n2.)  Pronoun - PRP\n\n3.)  Verb - VB, VBD, VBG, VBN, VBP, VBZ\n\n4.)  Adjective - JJ, JJR, JJS\n\n5.)  Adverb - RB, RBR, RBS\n\n6.)  Preposition - IN\n\n7.)  Conjunction - IN, CC and\n\n8.)  Interjection - UH")

def calcluate_pof():
    nouns1 = []
    pronouns1 = []
    verbs1 = []
    adjectives1 = []
    adverbs1 = []
    prepositions1 = []
    conjunctions1 = []
    interjections1 = []
    nouns = ""
    pronouns = ""
    verbs = ""
    adjectives = ""
    adverbs = ""
    prepositions = ""
    conjunctions = ""
    interjections = ""
    text = text_enter.get("1.0", "end-1c")
    tokenized = sent_tokenize(text)
    for i in tokenized:
        wordsList = nltk.word_tokenize(i)
        wordsList = [w for w in wordsList if not w in stop_words]
        tagged = nltk.pos_tag(wordsList)
        # print(tagged)

        for word, pos in tagged:
            if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):  # noun
                nouns = nouns + word + " , "
                nouns1.append(word)
            if (pos == 'PRP'):  # pronoun
                pronouns = pronouns + word + " , "
                pronouns1.append(word)
            if (pos == 'VB' or pos == 'VBD' or pos == 'VBG' or pos == 'VBN' or pos == 'VBP' or pos == 'VBZ'):  # verb
                verbs = verbs + word + " , "
                verbs1.append(word)
            if (pos == 'JJ' or pos == 'JJR' or pos == 'JJS'):  # adjective
                adjectives = adjectives + word + " , "
                adjectives1.append(word)
            if (pos == 'RB' or pos == 'RBR' or pos == 'RBS'):  # adverb
                adverbs = adverbs + word + " , "
                adverbs1.append(word)
            if (pos == 'IN'):  # prepositon
                prepositions = prepositions + word + " , "
                prepositions1.append(word)
            if (pos == 'IN' or pos == 'CC'):  # conjunction
                conjunctions = conjunctions + word + " , "
                conjunctions1.append(word)
            if (pos == 'UH'):  # interjection
                interjections = interjections + word + " , "
                interjections1.append(word)

    mbox.showinfo("Count of POF", "Nouns : " + str(len(nouns1)) + "\nNouns are : " + nouns + "\n\nPronouns : " + str(len(pronouns1)) + "\nPronouns are : " + pronouns + "\n\nVerbs : " + str(len(verbs1)) + "\nVerbs are : " + verbs + "\n\nAdjectives : " + str(len(adjectives1)) + "\nAdjectives are : " + adjectives + "\n\nAdverbs : " + str(len(adverbs1)) + "\nAdverbs are : " + adverbs + "\n\nPrepositions : " + str(len(prepositions1)) + "\nPrepositions are : " + prepositions + "\n\nConjunctions : " + str(len(conjunctions1)) + "\nConjunctions are : " + conjunctions + "\n\nInterjection : " + str(len(interjections1)) + "\nInterjections are : " + interjections)

window = Tk()
window.geometry("1000x700")
window.title("Part Of Speech")
# window.iconbitmap(r"icon.ico")

# starting label
start1 = Label(window, text='Part of Speech Calculator', font=("Arial", 35),fg="magenta",underline=0)
start1.place(x=200,y=10)

enter_label = Label(window, text="Enter Your text or paragraph here...", font=("Arial", 30),fg="brown")
enter_label.place(x=150,y=100)

text_enter = tk.Text(window, height=15, width=80, font=("Arial", 15), bg="light yellow", fg="brown",borderwidth=3, relief="solid")
text_enter.place(x=50, y=150)

pofb = Button(window, text="POF",command=show_pof,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
pofb.place(x =150 , y =570 )

calculateb = Button(window, text="CALCULATE",command=calcluate_pof,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
calculateb.place(x =280 , y =570 )

def clear_text():
    text_enter.delete("1.0","end")

resetb = Button(window, text="CLEAR",command=clear_text,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
resetb.place(x =530 , y =570 )

def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 20), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =700 , y =570 )


window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()