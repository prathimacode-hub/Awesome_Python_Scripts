import random
from tkinter import Tk, Button, END, Entry, mainloop, DISABLED, NORMAL
from PIL import Image, ImageTk

root = Tk()
root.title('Rock Paper Scissors')
root.geometry("675x250")
root.config(bg='#83b576')

#results
def Rock():
    answer["state"] = NORMAL
    answer.delete(0, END)
    computer = random.choice(['r', 'p', 's'])
    if computer == 'r':
        answer.insert(0,f"Draw, you both chose 'rock' ")
    elif computer == 'p':
        answer.insert(0,f"You lost, computer chose 'paper' defeating you")
    else:
        answer.insert(0,f"You won!!, computer chose 'scissors' losing to you")
    answer["state"] = DISABLED

def Scissors():
    answer["state"] = NORMAL
    answer.delete(0, END)
    computer = random.choice(['r', 'p', 's'])
    if computer == 's':
        answer.insert(0,f"Draw, you both chose 'scissors'")
    elif computer == 'r':
        answer.insert(0,f"You lost, computer chose 'rock' defeating you")
    else:
        answer.insert(0,f"You won!!, computer chose 'paper' losing to you")
    answer["state"] = DISABLED

def Paper():
    answer["state"] = NORMAL
    answer.delete(0, END)
    computer = random.choice(['r', 'p', 's'])
    if computer == 'p':
        answer.insert(0,f"Draw, you both chose 'paper'")
    elif computer == 's':
        answer.insert(0,f"You lost, computer chose 'scissors' defeating you")
    else:
        answer.insert(0,f"You won!!, computer chose 'rock' losing to you")
    answer["state"] = DISABLED

#buttons
Rock_btn = ImageTk.PhotoImage(Image.open('Images/Rock.jpg'))
Scissors_btn = ImageTk.PhotoImage(Image.open('Images/Scissors.jpg'))
Paper_btn = ImageTk.PhotoImage(Image.open('Images/Paper.jpg'))


Rock_butn = Button(root, image=Rock_btn, command=Rock)
Rock_butn.place(x=75, y=30 )

Paper_butn = Button(root, image=Paper_btn, command = Paper)
Paper_butn.place(x=300, y=25 )

Scissors_butn = Button(root, image=Scissors_btn, command = Scissors)
Scissors_butn.place(x=550, y=25 )


answer = Entry(
    root,
    width=50,
    font=('Courier New', 14),
    state = DISABLED
    )

answer.place(y=200, x=80)

mainloop()