import random
from tkinter import Tk, Button, END, Entry, mainloop, DISABLED, NORMAL #All the necessary imports
from PIL import Image, ImageTk

root = Tk() #initializing the tkinter module
root.title('Rock Paper Scissors')
root.geometry("675x250")
root.config(bg='#83b576')


#results after Rock Button is clicked
def Rock():
    answer["state"] = NORMAL
    answer.delete(0, END) #deletes the previous results, and shows a new one
    computer = random.choice(['r', 'p', 's'])
    if computer == 'r':
        answer.insert(0,f"Draw, you both chose 'rock' ")
    elif computer == 'p':
        answer.insert(0,f"You lost, computer chose 'paper' defeating you")
    else:
        answer.insert(0,f"You won!!, computer chose 'scissors' losing to you")
    answer["state"] = DISABLED

#results after Rock Button is clicked
def Scissors():
    answer["state"] = NORMAL
    answer.delete(0, END) #deletes the previous results, and shows a new one
    computer = random.choice(['r', 'p', 's'])
    if computer == 's':
        answer.insert(0,f"Draw, you both chose 'scissors'")
    elif computer == 'r':
        answer.insert(0,f"You lost, computer chose 'rock' defeating you")
    else:
        answer.insert(0,f"You won!!, computer chose 'paper' losing to you")
    answer["state"] = DISABLED
    
#results after Rock Button is clicked
def Paper():
    answer["state"] = NORMAL
    answer.delete(0, END) #deletes the previous results, and shows a new one
    computer = random.choice(['r', 'p', 's'])
    if computer == 'p':
        answer.insert(0,f"Draw, you both chose 'paper'")
    elif computer == 's':
        answer.insert(0,f"You lost, computer chose 'scissors' defeating you")
    else:
        answer.insert(0,f"You won!!, computer chose 'rock' losing to you")
    answer["state"] = DISABLED

#buttons, with images using PIL module
Rock_btn = ImageTk.PhotoImage(Image.open('Images/Rock.jpg'))
Scissors_btn = ImageTk.PhotoImage(Image.open('Images/Scissors.jpg'))
Paper_btn = ImageTk.PhotoImage(Image.open('Images/Paper.jpg'))

#positioning of the buttons
Rock_butn = Button(root, image=Rock_btn, command=Rock)
Rock_butn.place(x=75, y=30 )

Paper_butn = Button(root, image=Paper_btn, command = Paper)
Paper_butn.place(x=300, y=25 )

Scissors_butn = Button(root, image=Scissors_btn, command = Scissors)
Scissors_butn.place(x=550, y=25 )

#The results bar, The result of win/loss/draw will show up here
answer = Entry(
    root,
    width=50,
    font=('Courier New', 14),
    state = DISABLED
    )

answer.place(y=200, x=80)

#starts the program
mainloop()
