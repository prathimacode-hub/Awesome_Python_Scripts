import tkinter as tk
from tkinter import *
from tkinter import messagebox
import tkinter.font as font
import wikipediaapi
import requests


##_____________INITIALIZE WIKI MODULE________________##
wiki = wikipediaapi.Wikipedia(
            language='en',
            extract_format=wikipediaapi.ExtractFormat.WIKI
        )

##___________BUTTON CALLBACKS______________##
def submit_data():
    entry_data = entry.get()
    if entry_data=="":
        messagebox.showwarning("WARNING !", "Topic Name is Missing !!")
    else:
        wiki_data = wiki.page(entry.get())
        output.delete('1.0',END)
        output.insert(END,wiki_data.text)
        result_lab.configure(text="Result"+" : "+wiki_data.title)
        #output.insert(END,wiki_data.sections)

def clear():
    output.delete('1.0',END)
    result_lab.configure(text="Result")


#______________________________GUI CODE STARTS___________________________________##
#Defining the GUI window
window = Tk()
#set window color
window.configure(bg="white")
#set window title
window.title("Mini Wikipedia")


##ROW0
tk.Label(window,text="Topic", relief=tk.RIDGE, width=30, pady=5, justify=CENTER).grid(row=0,column=0)
entry = tk.Entry(window,bg="white", relief=tk.RIDGE, width=30)
entry['font'] = font.Font(size=12)
entry.grid(row=0,column=2)

##ROW1
result_lab = tk.Label(window, text="Result",bg="white",fg='green', )
result_lab['font'] = font.Font(size = 20)
result_lab.grid(row=1,column=3)

tk.Button(window,text='Quit',width=25,bg="red",fg="white", command = exit).grid(row=1, column=0)
tk.Button(window,text='Submit',width=25,bg="yellow", command = submit_data).grid(row=1, column=2)

##ROW2
tk.Button(window,text='Clear Output',width=25,bg="green", fg="white", command = clear).grid(row=2, column=0)

##ROW3
output = tk.Text(window,height=40)
output.grid(row=3,column=3)

window.resizable('False','True')
window.mainloop()
#_____________________________GUI CODE ENDS______________________________________##

