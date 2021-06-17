# importing all necessary libraries
from tkinter import *
import tkinter.messagebox
tk = Tk()
tk.title("Tic Tac Toe Game")

pa = StringVar()
playerb = StringVar()
p1 = StringVar()
p2 = StringVar()

player1_name = Entry(tk, textvariable=p1, bd=5)
player1_name.grid(row=1, column=1, columnspan=8)
player2_name = Entry(tk, textvariable=p2, bd=5)
player2_name.grid(row=2, column=1, columnspan=8)

bclick = True
flag = 0

def disableButton():
    b1.configure(state=DISABLED)
    b2.configure(state=DISABLED)
    b3.configure(state=DISABLED)
    b4.configure(state=DISABLED)
    b5.configure(state=DISABLED)
    b6.configure(state=DISABLED)
    b7.configure(state=DISABLED)
    b8.configure(state=DISABLED)
    b9.configure(state=DISABLED)



def btnClick(buttons):
    global bclick, flag, player2_name, player1_name, player, pa
    if buttons["text"] == " " and bclick == True:
        buttons["text"] = "X"
        bclick = False
        player = p2.get() + " Wins!"
        pa = p1.get() + " Wins!"
        checkForWin()
        flag += 1


    elif buttons["text"] == " " and bclick == False:
        buttons["text"] = "O"
        bclick = True
        checkForWin()
        flag += 1
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")

#Checks for victory or Draw
def checkForWin():
    if (b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X' or
        b4['text'] == 'X' and b5['text'] == 'X' and b6['text'] == 'X' or
        b7['text'] == 'X' and b8['text'] == 'X' and b9['text'] == 'X' or
        b1['text'] == 'X' and b5['text'] == 'X' and b9['text'] == 'X' or
        b3['text'] == 'X' and b5['text'] == 'X' and b7['text'] == 'X' or
        b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X' or
        b1['text'] == 'X' and b4['text'] == 'X' and b7['text'] == 'X' or
        b2['text'] == 'X' and b5['text'] == 'X' and b8['text'] == 'X' or
        b7['text'] == 'X' and b6['text'] == 'X' and b9['text'] == 'X'):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", pa)

    elif(flag == 8):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")

    elif (b1['text'] == 'O' and b2['text'] == 'O' and b3['text'] == 'O' or
          b4['text'] == 'O' and b5['text'] == 'O' and b6['text'] == 'O' or
          b7['text'] == 'O' and b8['text'] == 'O' and b9['text'] == 'O' or
          b1['text'] == 'O' and b5['text'] == 'O' and b9['text'] == 'O' or
          b3['text'] == 'O' and b5['text'] == 'O' and b7['text'] == 'O' or
          b1['text'] == 'O' and b2['text'] == 'O' and b3['text'] == 'O' or
          b1['text'] == 'O' and b4['text'] == 'O' and b7['text'] == 'O' or
          b2['text'] == 'O' and b5['text'] == 'O' and b8['text'] == 'O' or
          b7['text'] == 'O' and b6['text'] == 'O' and b9['text'] == 'O'):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", player)

#main function
buttons = StringVar()

label = Label( tk, text="Player 1:", font='Helvetica', bg='yellow', fg='black', height=1, width=8)
label.grid(row=1, column=0)


label = Label( tk, text="Player 2:", font='Helvetica', bg='yellow', fg='black', height=1, width=8)
label.grid(row=2, column=0)

b1 = Button(tk, text=" ", font='Helvetica', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(b1))
b1.grid(row=3, column=0)

b2 = Button(tk, text=' ', font='Helvetica', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(b2))
b2.grid(row=3, column=1)

b3 = Button(tk, text=' ',font='Helvetica', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(b3))
b3.grid(row=3, column=2)

b4 = Button(tk, text=' ', font='Helvetica', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(b4))
b4.grid(row=4, column=0)

b5 = Button(tk, text=' ', font='Helvetica', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(b5))
b5.grid(row=4, column=1)

b6 = Button(tk, text=' ', font='Helvetica', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(b6))
b6.grid(row=4, column=2)

b7 = Button(tk, text=' ', font='Helvetica', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(b7))
b7.grid(row=5, column=0)

b8 = Button(tk, text=' ', font='Helvetica', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(b8))
b8.grid(row=5, column=1)

b9 = Button(tk, text=' ', font='Helvetica', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(b9))
b9.grid(row=5, column=2)

tk.mainloop()