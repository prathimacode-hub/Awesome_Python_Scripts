import detectlanguage as dtl #Client Library for our API
import tkinter as tk
from tkinter import font
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as mbox
from tkinter import scrolledtext
from tkinter import ttk
import csv

dtl.Configuration.api_key = "YOUR__API__KEY" #Your API Key

##--------BUTTON CALLBACKS--------##
def clear_input():
    entry_1.delete(0,END)

def activate_input():
    entry_1['state'] = "normal" #enables statement entry widget
    if(file_entry.get()!=""):#check if file_entry widget is having file_name in it
        file_entry.delete(0,END) #deletes file name if selected from file_entry widget
    file_entry['state'] = "disabled" #then disables file_entry widget


def choose_file():
    global content
    if(entry_1.get()!=""): #checking if statement entry has text in it
        entry_1.delete(0,END) #deleting text from entry_1 widget
    entry_1['state'] = "disabled" #disabling the statement entry
    file_entry['state'] = "normal" #Making the file entry visible
    file = filedialog.askopenfile(initialdir="/",
                                          title="Choose File",
                                          filetypes=(("Text files","*.txt*"),
                                              ("all files","*.*")),
                                          mode = 'r+')
    if file != None:
        content = file.read()
        if(file_entry.get()!=""):
            file_entry.delete(0,END)
        file_entry.insert(END,file.name)
        return content
    else:
        mbox.showerror("File Error", "File not selected!!")

def detect():
    if(entry_1['state']=='normal'):
        if entry_1.get()!= "": #check if the entry has no content
            content1 = entry_1.get()
            stxt['state'] = 'normal'
            if (stxt.get('1.0', 'end-1c') != ""):
                stxt.delete(1.0, END)
            stxt.insert(END,dtl.simple_detect(content1)) #simple_detect function just returns language code
            stxt['state'] = "disabled"
        else:
            mbox.showerror("Input Error","Input can't be empty!")
    else:
        if file_entry.get()!="": #check if the file is selected or not
            content1 = content
            if(content1==""): #check if file has content or not
                mbox.showerror("File Error","File has no content!")
            else:
                stxt['state'] = 'normal'
                if(stxt.get('1.0', 'end-1c')!=""):
                    stxt.delete(1.0,END)
                stxt.insert(END,dtl.simple_detect(content1))
                stxt['state'] = "disabled"
        else:
            mbox.showerror("File Error","File not selected!")

##---------GUI STARTS HERE--------##
window = tk.Tk()
window.title("Detect Language")
window.config(bg="white")
window.geometry("1000x700")

## SECTION 1 : TAKING STATEMENT INPUT FROM USER
l1 = Label(window, text="Enter your text here:", bg="white") #label 1
l1.place(x=10,y=60,height=20,width=200)
l1['font'] = font.Font(size=15)

entry_1 = Entry(window, bg="#9EF281") #entry_1
entry_1.place(x=230, y=55, height=30, width=300)
entry_1['font'] = font.Font(size=15)

clear_btn = Button(window, bg="yellow", text="Clear Input", command=clear_input) #clear input button
clear_btn.place(x=280, y=95)

activate_btn = Button(window, bg="#FFCB64", text="Activate Input", command=activate_input) #clear input button
activate_btn.place(x=390, y=95)

## SECTION 2 : TAKING FILE INPUT FROM USER
l2 = Label(window, text="Detect from (.txt) file:", bg="white") #label2
l2.place(x=10, y=180, height=20, width=200)
l2['font'] = font.Font(size=15)

file_entry = Entry(window, bg="#9EF281") #entry_2
file_entry.place(x=230, y=175, height=30, width=300)
file_entry['font'] = font.Font(size=15)
file_entry['state'] = "disabled"

file_btn = Button(window, bg="yellow", text="Choose File", command=choose_file) #choose file button
file_btn.place(x=345, y=220)

## SECTION 3 : DETECT BUTTON & OUTPUT WINDOW
detect_button = Button(window, bg="green", text="Detect Language", fg="white", command=detect) #detect lang button
detect_button.place(x=750, y=55)
stxt = scrolledtext.ScrolledText(window,
                                      wrap = tk.WORD,
                                      width = 40,
                                      height = 10,
                                      font = ("Times New Roman",
                                              15))
stxt.place(x=650,y=100, height=140, width=300)
stxt['state'] = "disabled"

## SECTION 4 : REFERENCE SECTION FOR LANGUAGE CODES
frame = Frame(window)
frame.place(x=35,y=350,height=260, width=930)

ref_label = Label(window,text="Reference for Language Codes: ",  bg='white', fg='green')
ref_label['font'] = font.Font(size=15)
ref_label.place(x=20, y=300)


# Constructing treeview for displaying codes from csv file in table format in tkinter
with open(".\Related\languages.csv",newline='\n')  as csvfile:  #takes filename of languages.csv from "Related" folder
    data_rows = csv.reader(csvfile)
    tree = ttk.Treeview(frame,column=('col1','col2'), show='headings',height=10)
    tree.column("# 1", anchor=CENTER)
    tree.heading("# 1", text="CODE")
    tree.column("# 2", anchor=CENTER)
    tree.heading("# 2", text="LANGUAGE")

    for row in data_rows:
        tree.insert('', 'end', text="1", values=(row[0],row[1]))
    tree.place(x=0,y=0,height=260, width=930)

window.mainloop()
##------GUI ENDS HERE--------##
