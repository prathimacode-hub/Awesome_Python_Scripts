from tkinter import *
import random

houses = ["Slytherin", "Gryffindor", "Hufflepuff", "Ravenclaw"] #list of houses

def pickHouse():#funcion to pick a house randomly
    hat.configure(text=(random.choice(houses)))

root = Tk()   #initializes a blank 'root' window
root.title("Sorting hat Game")  #sets the title of window 
root.geometry("700x100")  #sets the dimensions of window

#creates a label 'hat' 
hat = Label(root,text="This game selects a house for you. So click on the button",bg="purple",fg="yellow",font=("Calibri",18,"bold"))
hat.pack() #adds 'hat' label onto 'root' window

#creates a button
button = Button(root, text="Choose a House" , bd='5', bg="yellow", fg="red", font="andalus", activebackground="#34A2FE", activeforeground="black", justify="left", highlightcolor="purple", relief="groove",  command=pickHouse)
button.pack()#adds a button named 'Choose a House' on 'root' window

root.mainloop() #holds the window
