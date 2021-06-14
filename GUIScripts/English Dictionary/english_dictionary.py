from tkinter import *      #importing the necessary libraries
import json
from difflib import get_close_matches

data = json.load(open("Related/data.json"))       #loading and storing the data from json file

def search(word):
    if word in data:             #if the typed word is present in the data
        t1.delete(1.0,END)
        t1.config(fg='white')
        t1.insert(END,data[word])
    elif len(get_close_matches(word,data.keys()))>0:     #if the typed word is not found in data or is misspelled
        t1.config(fg='red')
        t1.delete(1.0,END)
        t1.insert(END,"Did you mean {} to mean : {} ".format (get_close_matches(word,data.keys())[0],data[get_close_matches(word,data.keys())[0]]))
        output = get_close_matches(word,data.keys())


window = Tk()
window.title ("English Dictionary")

label = Label(window)
label.pack()

e1_value=StringVar()
e1 = Entry(window,textvariable=e1_value,bg="black",fg="white",justify = CENTER,font = ('courier', 30, 'bold'))    #for the text bar
e1.place(relx=.185,rely=0.70,relwidth=.63,relheight=.082)


b1 = Button(window,text="Search",command= lambda : search(e1_value.get()),relief=FLAT,bg="black",fg="white",font = ('courier', 30, 'bold') )    #for the search button
b1.place(relx=.40,rely=.85,relwidth=.2,relheight=.052)


t1 = Text(window,fg="white",relief=FLAT,bg="#444444",font = ('courier', 20, 'bold'))    #for displaying the meaning
t1.place(relx=.185,rely=.09,relwidth=.63,relheight=.50)

window.mainloop()
