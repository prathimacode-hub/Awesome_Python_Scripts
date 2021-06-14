import random as rd
import time as t
import tkinter as tk

#function to show different symbols
#here it also checks if first card is same as second or not
def show_symbols(i, j):
    global first_card
    global previous_X
    global previous_Y
    buttons[i, j]['text'] = button_symbols[i, j]
    buttons[i, j].update_idletasks()

    if first_card:
        previous_X = i
        previous_Y = j
        first_card = False

    elif previous_X != i or previous_Y != j:
        if buttons[previous_X, previous_Y]['text'] != buttons[i, j]['text']:

            t.sleep(0.5)
            buttons[previous_X, previous_Y]['text'] = ' '
            buttons[i, j]['text'] = ' '
        else:
            buttons[previous_X, previous_Y]['command'] = tk.DISABLED

            buttons[i, j]['command'] = tk.DISABLED
        first_card = True


window = tk.Tk()

window.background = "red"
window.title("Matchmaker by Neel Shah")
window.resizable(width=False, height=False)

first_card = True
previous_X = 0
previous_Y = 0
buttons = {}
button_symbols = {}

symbol_list = [u'\u03B1', u'\u03B2', u'\u03B3', u'\u03B4', u'\u03B5', u'\u03B6',
               u'\u03B7', u'\u03B8', u'\u03BB', u'\u03BC', u'\u03BE', u'\u03BF',
               u'\u03B1', u'\u03B2', u'\u03B3', u'\u03B4', u'\u03B5', u'\u03B6',
               u'\u03B7', u'\u03B8', u'\u03BB', u'\u03BC', u'\u03BE', u'\u03BF']

rd.shuffle(symbol_list)

#designing the grid
for i in range(6):
    for j in range(4):
        button = tk.Button(master=window, command=lambda i=i, j=j: show_symbols(i, j), width=8, height=5, bg='green',
                           fg='red', font=('Helvetica', '20'))
        button.grid(column=i, row=j)
        buttons[i, j] = button
        button_symbols[i, j] = symbol_list.pop()

window.mainloop()