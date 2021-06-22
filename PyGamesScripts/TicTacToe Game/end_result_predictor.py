
# Unscramble Word Game

import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
from PIL import Image, ImageTk


# function defined for guessing the result of given input of TIC TAC TOE board.
def guess_result():
    cntx = 0
    cnto = 0
    cnt_ = 0
    cnt1 = 0
    cnt2 = 0

    board_list = []
    board_00 = var_00.get()
    board_list.append(board_00)
    board_01 = var_01.get()
    board_list.append(board_01)
    board_02 = var_02.get()
    board_list.append(board_02)
    board_10 = var_10.get()
    board_list.append(board_10)
    board_11 = var_11.get()
    board_list.append(board_11)
    board_12 = var_12.get()
    board_list.append(board_12)
    board_20 = var_20.get()
    board_list.append(board_20)
    board_21 = var_21.get()
    board_list.append(board_21)
    board_22 = var_22.get()
    board_list.append(board_22)


    for i in board_list:
        if(i=='X'):
            cntx = cntx + 1
        elif(i=='O'):
            cnto = cnto + 1
        else:
            cnt_ = cnt_ + 1

    if(board_00=='X' and board_01=='X' and board_02=='X'):
        cnt1 = cnt1 + 1
    if (board_10 == 'X' and board_11 == 'X' and board_12 == 'X'):
        cnt1 = cnt1 + 1
    if (board_20 == 'X' and board_21 == 'X' and board_22 == 'X'):
        cnt1 = cnt1 + 1
    if (board_00 == 'X' and board_10 == 'X' and board_20 == 'X'):
        cnt1 = cnt1 + 1
    if (board_01 == 'X' and board_11 == 'X' and board_21 == 'X'):
        cnt1 = cnt1 + 1
    if (board_02 == 'X' and board_12 == 'X' and board_22 == 'X'):
        cnt1 = cnt1 + 1
    if (board_00 == 'X' and board_11 == 'X' and board_22 == 'X'):
        cnt1 = cnt1 + 1
    if (board_02 == 'X' and board_11 == 'X' and board_20 == 'X'):
        cnt1 = cnt1 + 1

    if (board_00 == 'O' and board_01 == 'O' and board_02 == 'O'):
        cnt2 = cnt2 + 1
    if (board_10 == 'O' and board_11 == 'O' and board_12 == 'O'):
        cnt2 = cnt2 + 1
    if (board_20 == 'O' and board_21 == 'O' and board_22 == 'O'):
        cnt2 = cnt2 + 1
    if (board_00 == 'O' and board_10 == 'O' and board_20 == 'O'):
        cnt2 = cnt2 + 1
    if (board_01 == 'O' and board_11 == 'O' and board_21 == 'O'):
        cnt2 = cnt2 + 1
    if (board_02 == 'O' and board_12 == 'O' and board_22 == 'O'):
        cnt2 = cnt2 + 1
    if (board_00 == 'O' and board_11 == 'O' and board_22 == 'O'):
        cnt2 = cnt2 + 1
    if (board_02 == 'O' and board_11 == 'O' and board_20 == 'O'):
        cnt2 = cnt2 + 1

    if(cntx<cnto):
        mbox.showinfo("Prediction", "This Tic Tac Toe board is not reachable.\n\nReason : The no. of X is less than no. of O.")
        return
    if(cntx>cnto+1):
        mbox.showinfo("Prediction", "This Tic Tac Toe board is not reachable.\n\nReason : The difference between the no. of X and the no. of O can never be greater than 1 at any instant, as both X and O have alternate turns.")
        return
    if(cnt1>=1 and cnt2>=1):
        mbox.showinfo("Prediction", "This Tic Tac Toe board is not reachable.\n\nReason : Both X and O can never win.")
        return
    if(cnt1>=1 and cntx==cnto):
        mbox.showinfo("Prediction", "This Tic Tac Toe board is not reachable.\n\nReason : As game starts with X, and if X is winning then the no. of X can never be equal to no. of O.")
        return
    if(cnt2>=1 and cntx>cnto):
        mbox.showinfo("Prediction", "This Tic Tac Toe board is not reachable.\n\nReason : Because if the player with O has won, then no. of X can never ne greater than no. of O.")
        return
    if(cnt1>=1 or cnt2>=1):
        if(cnt1>=1):
            mbox.showinfo("Prediction", "This Tic Tac Toe board is reachable, and the player with X won.\n\nReason : Beacuse there is atleast one complete sequence of 3 X's present in the board.")
            return
        else:
            mbox.showinfo("Prediction", "This Tic Tac Toe board is reachable, and the player with O won.\n\nReason : Beacuse there is atleast one complete sequence of 3 O's present in the board.")
            return
    if(cnt_==0):
        mbox.showinfo("Prediction", "This Tic Tac Toe board is reachable, and the game is drawn.\n\nReason : Since there is no empty cell and also no one either player with X or player with O has won.")
        return
    else:
        mbox.showinfo("Prediction", "This Tic Tac Toe board is reachable, and the game will continue for at least one more move.")
        return


# creating a main window
window = Tk()
window.geometry("1100x750")
window.title("End Result Predictor (TIC-TAC-TOE)")

# for printing the starting label
start1 = tk.Label(text = "TIC-TAC-TOE PREDICTOR", font=("Arial", 50), fg="blue",underline=0) # same way bg
start1.place(x = 80, y = 10)

# image on the main window
path = "Images/board.png"
# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))
# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image = img, anchor = "nw")
# The Pack geometry manager packs widgets in rows or columns.
# panel.pack(side = "top", fill = "both", expand = "no")
panel.place(x = 20, y = 110)

# -----------------------------------------------------------------------------------------------
# creating the OptionMenu at (0,0)
var_00 = tk.StringVar()
# as icon size are really small, we defined the following 7 sizes
choices_00 = ['X','O','   ']
menu_00 = OptionMenu(window, var_00, *choices_00)
menu_00.config(font=("Arial", 50), bg = "brown", fg = "yellow", borderwidth=10)
menu_00["menu"].config(font=("Arial", 30), bg = "light yellow", fg = "brown")
menu_00.place(x=80, y=190)
var_00.set('   ') # size 1 is selected as by default, and we can

# creating the OptionMenu at (0,1)
var_01 = tk.StringVar()
# as icon size are really small, we defined the following 7 sizes
choices_01 = ['X','O','   ']
menu_01 = OptionMenu(window, var_01, *choices_01)
menu_01.config(font=("Arial", 50), bg = "brown", fg = "yellow", borderwidth=10)
menu_01["menu"].config(font=("Arial", 30), bg = "light yellow", fg = "brown")
menu_01.place(x=270, y=190)
var_01.set('   ') # size 1 is selected as by default, and we can

# creating the OptionMenu at (0,2)
var_02 = tk.StringVar()
# as icon size are really small, we defined the following 7 sizes
choices_02 = ['X','O','   ']
menu_02 = OptionMenu(window, var_02, *choices_02)
menu_02.config(font=("Arial", 50), bg = "brown", fg = "yellow", borderwidth=10)
menu_02["menu"].config(font=("Arial", 30), bg = "light yellow", fg = "brown")
menu_02.place(x=460, y=190)
var_02.set('   ') # size 1 is selected as by default, and we can

# creating the OptionMenu at (1,0)
var_10 = tk.StringVar()
# as icon size are really small, we defined the following 7 sizes
choices_10 = ['X','O','   ']
menu_10 = OptionMenu(window, var_10, *choices_10)
menu_10.config(font=("Arial", 50), bg = "brown", fg = "yellow", borderwidth=10)
menu_10["menu"].config(font=("Arial", 30), bg = "light yellow", fg = "brown")
menu_10.place(x=80, y=370)
var_10.set('   ') # size 1 is selected as by default, and we can

# creating the OptionMenu at (1,1)
var_11 = tk.StringVar()
# as icon size are really small, we defined the following 7 sizes
choices_11 = ['X','O','   ']
menu_11 = OptionMenu(window, var_11, *choices_11)
menu_11.config(font=("Arial", 50), bg = "brown", fg = "yellow", borderwidth=10)
menu_11["menu"].config(font=("Arial", 30), bg = "light yellow", fg = "brown")
menu_11.place(x=270, y=370)
var_11.set('   ') # size 1 is selected as by default, and we can

# creating the OptionMenu at (1,2)
var_12 = tk.StringVar()
# as icon size are really small, we defined the following 7 sizes
choices_12 = ['X','O','   ']
menu_12 = OptionMenu(window, var_12, *choices_12)
menu_12.config(font=("Arial", 50), bg = "brown", fg = "yellow", borderwidth=10)
menu_12["menu"].config(font=("Arial", 30), bg = "light yellow", fg = "brown")
menu_12.place(x=460, y=370)
var_12.set('   ') # size 1 is selected as by default, and we can

# creating the OptionMenu at (2,0)
var_20 = tk.StringVar()
# as icon size are really small, we defined the following 7 sizes
choices_20 = ['X','O','   ']
menu_20 = OptionMenu(window, var_20, *choices_20)
menu_20.config(font=("Arial", 50), bg = "brown", fg = "yellow", borderwidth=10)
menu_20["menu"].config(font=("Arial", 30), bg = "light yellow", fg = "brown")
menu_20.place(x=80, y=550)
var_20.set('   ') # size 1 is selected as by default, and we can

# creating the OptionMenu at (2,1)
var_21 = tk.StringVar()
# as icon size are really small, we defined the following 7 sizes
choices_21 = ['X','O','   ']
menu_21 = OptionMenu(window, var_21, *choices_21)
menu_21.config(font=("Arial", 50), bg = "brown", fg = "yellow", borderwidth=10)
menu_21["menu"].config(font=("Arial", 30), bg = "light yellow", fg = "brown")
menu_21.place(x=270, y=550)
var_21.set('   ') # size 1 is selected as by default, and we can

# creating the OptionMenu at (2,2)
var_22 = tk.StringVar()
# as icon size are really small, we defined the following 7 sizes
choices_22 = ['X','O','   ']
menu_22 = OptionMenu(window, var_22, *choices_22)
menu_22.config(font=("Arial", 50), bg = "brown", fg = "yellow", borderwidth=10)
menu_22["menu"].config(font=("Arial", 30), bg = "light yellow", fg = "brown")
menu_22.place(x=460, y=550)
var_22.set('   ') # size 1 is selected as by default, and we can
#--------------------------------------------------------------------------------------------------------

# for defining X, O, and empty spaces
# image X
pathx = "Images/x.jpg"
# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
imgx = ImageTk.PhotoImage(Image.open(pathx))
# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panelx = tk.Label(window, image = imgx, anchor = "nw")
# The Pack geometry manager packs widgets in rows or columns.
# panel.pack(side = "top", fill = "both", expand = "no")
panelx.place(x = 650, y = 150)

xlabel = tk.Label(text = "is X.", font=("Arial", 20), fg="blue") # same way bg
xlabel.place(x = 680, y = 150)

# image O
patho = "Images/o.jpg"
# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
imgo = ImageTk.PhotoImage(Image.open(patho))
# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panelo = tk.Label(window, image = imgo, anchor = "nw")
# The Pack geometry manager packs widgets in rows or columns.
# panel.pack(side = "top", fill = "both", expand = "no")
panelo.place(x = 770, y = 148)

olabel = tk.Label(text = "is O.", font=("Arial", 20), fg="blue") # same way bg
olabel.place(x = 800, y = 148)

# image empty
pathempty = "Images/empty.jpg"
# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
imgempty = ImageTk.PhotoImage(Image.open(pathempty))
# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panelempty = tk.Label(window, image = imgempty, anchor = "nw")
# The Pack geometry manager packs widgets in rows or columns.
# panel.pack(side = "top", fill = "both", expand = "no")
panelempty.place(x = 890, y = 153)

emptylabel = tk.Label(text = "is Empty.", font=("Arial", 20), fg="blue") # same way bg
emptylabel.place(x = 930, y = 150)

# x start label
startlabel = tk.Label(text = "The game starts with X.", font=("Arial", 30), fg="brown") # same way bg
startlabel.place(x = 650, y = 230)

# creating button
guessb = Button(window, text="GUESS",command=guess_result,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
guessb.place(x =800 , y =350 )

# function defined for reseting the board
def reset_board():
    var_00.set('   ')
    var_01.set('   ')
    var_02.set('   ')
    var_10.set('   ')
    var_11.set('   ')
    var_12.set('   ')
    var_20.set('   ')
    var_21.set('   ')
    var_22.set('   ')

# button created for reseting the TIC TAC TOE to all empty cell
resetb = Button(window, text="RESET",command=reset_board,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
resetb.place(x =800 , y =450 )

# function defined to exit from the application
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

# creating exit button
exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 20), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =815 , y =550 )


window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()
