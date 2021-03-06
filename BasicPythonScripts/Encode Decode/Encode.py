from tkinter import Tk
from tkinter import Label
from tkinter import BOTTOM
from tkinter import StringVar
from tkinter import Entry
from tkinter import Button
import base64

# Lets first initialize window 
root = Tk()
root.geometry('500x500')
root.resizable(0, 0)

#  This is the title of the window
root.title("Encode Decode")

# LETS label
Label(root, text='ENCODE DECODE', font='arial 20 bold').pack()
Label(root, text='Made with code :)', font='arial 20 bold').pack(side=BOTTOM)

# LETS DEFINE VARIABLES
Text = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()


# This is function to encode
def Encode(key, message):
    """Encode the message."""
    enc = []
    for i in enumerate(message):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


# This is function to decode
def Decode(key, message):
    """Decode the message."""
    dec = []
    message = base64.urlsafe_b64decode(message).decode()
    for i in enumerate(message):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i]) - ord(key_c)) % 256))
    return "".join(dec)


# this is the function to set mode
def Mode():
    """Take the key."""
    if mode.get() == 'e':
        Result.set(Encode(private_key.get(), Text.get()))
    elif mode.get() == 'd':
        Result.set(Decode(private_key.get(), Text.get()))
    else:
        Result.set('Invalid one')


# Function to exit window
def Exit():
    """Exit ."""
    root.destroy()


# Function to reset
def Reset():
    """Reset"""
    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")


Label(
    root, font='arial 12 bold', text='type the message'
).place(x=60, y=60)
Entry(
    root, font='arial 10', textvariable=Text, bg='ghost white'
).place(x=290, y=60)


# key
Label(root, font='arial 12 bold', text='KEY').place(x=60, y=90)
Entry(
    root, font='arial 10', textvariable=private_key , bg='ghost white'
).place(x=290, y=90)

# setting the mode
Label(
    root, font='arial 12 bold', text='MODE(e-encode, d-decode)'
).place(x=60, y=120)
Entry(
    root, font='arial 10', textvariable=mode , bg='ghost white'
).place(x=290, y=120)

# result
Entry(
     root, font='arial 10 bold', textvariable=Result, bg='ghost white'
).place(x=290, y=150)

# this is the result button
Button(
    root, font='arial 10 bold', text='OUTPUT', padx=2, bg='Lightpink', command=Mode
).place(x=60, y=150)

# this is reset button
Button(
    root, font='anson', text='RESET', width=6, command=Reset, bg='pink', padx=2
).place(x=80, y=190)

# lets exit the button
Button(
    root, font='anson', text='EXIT', width=6, command=Exit, bg='yellow', padx=2, pady=2
).place(x=180, y=190)
root.mainloop()
