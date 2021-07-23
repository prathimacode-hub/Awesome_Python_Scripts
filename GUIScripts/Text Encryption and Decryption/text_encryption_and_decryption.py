

# # Name: SHIVAM RAVI
# ## PROJECT CODE
# ##             on
# ## “Python based GUI application to encrypt and decrypt text”
# ##   DevIncept Participant
# ## Issue no: #660
# ## Contributed to : Awesome_Python_Scripts

#  Importing required libraries


import tkinter as tk
import tkinter.font as tkfont
from tkinter import *
from tkinter.ttk import *


# Importing ohawf [ Easy OAuth2 authentication for Google services ]  package for authentication purpose

import ohawf


# Creating a credentials object so that you will immediately receive a link for the Web-based Google OAuth2 login prompt. This will identify yours identity before sending any message to other

credentials = ohawf.Credentials().get()
print("Authenticaton Successful!! You are good to go for instant messaging")


# We are using tkinter as a frontend part of this projet. This framework provides Python users with a simple way to create GUI elements using the widgets found in the Tk toolkit. Tk widgets can be used to construct buttons, menus, data fields, etc.

root = tk.Tk()


# For changing the title of the title bar 
root.title("Text Encryptor-Decryptor")

# To set the dimensions of the window
root.geometry("400x500") # width x height
# To set whether we can resize the window or not.The below line doesn't allow the resizing of the window.
root.resizable(width=FALSE, height=FALSE)


# Creating a canvas 
canvas = tk.Canvas(root,height = 500, width=400, bg="MediumPurple1")
# Attaching the canvas
canvas.pack()


# Set the family,size and style of the font
bold_font = tkfont.Font(family="Helvetica",size=12,weight="bold")



# Creating a label with a text and attaching it to the root
label1 = tk.Label(root,text= "Enter the Text",width=20,bg="MediumPurple1")
# adding the font features to the label
label1.config(font=bold_font)
# placing the label in the canvas
canvas.create_window(200,100,window=label1)


# Text Area 
user_text = tk.Entry(root)
canvas.create_window(200,150,window=user_text)


# Creating a label with a text and attaching it to the root
label2=tk.Label(root,text="Choose an Operation",width=25,bg="MediumPurple1")
# adding the font features to the label
label2.config(font=bold_font)
# placing the label in the canvas
canvas.create_window(200,200,window=label2)


# Tkinter Variable 
v = tk.IntVar()


# Defined a function choice
def choice():
  # Retrieve the value of the radio button
    x = v.get()
  # Performs Encryption if the value is 1 else performs Decryption.
    if(x==1):
        encryption()
    elif(x==2):
        decryption()



# Defined a function Encryption
def encryption():
  # Get the user entered text to get function and store it in a variable plain_text
    plain_text = user_text.get()
  # To store the result   
    cipher_text = ""
  # Number of shift to be performed. For Caesar Cipher it's 3
    key = 3
  # traversing the text
    for i in range(len(plain_text)):
        letter = plain_text[i]
  # UpperCase Condition
        if(letter.isupper()):
            cipher_text+=chr((ord(letter)+key-65)%26+65)
        else:
  # LowerCase Condition
            cipher_text+=chr((ord(letter)+key-97)%26+97)
  # Creating a label with a text and attaching it to the root       
    label3 =tk.Label(root,text=cipher_text,width=20,bg="light yellow")
  # adding the font features to the label
    label3.config(font=bold_font)
  # placing the label in the canvas
    canvas.create_window(200,350,window=label3)


# Defined a function Decryption
def decryption():
  # Get the user entered text to get function and store it in a varaible cipher_text
    cipher_text = user_text.get()
  # To store the result
    plain_text = ""
  # Number of shifts to be performed. For Caesar Cipher it's 3.
    key = 3
  # Traversing the text
    for i in range(len(cipher_text)):
        letter = cipher_text[i]
  # Uppercase condition
        if(letter.isupper()):
            plain_text+=chr((ord(letter)-key-65)%26+65)
        else:
  # Lowercase condition
            plain_text+=chr((ord(letter)-key-97)%26+97) 
  # Creating a label with a text and attaching it to the root
    label4 =tk.Label(root,text=plain_text,width=20,bg="light yellow")
  # Adding the font features to the label
    label4.config(font=bold_font)
  # Placing the label in the canvas
    canvas.create_window(200,350,window=label4)


# Radio Button for Encryption 
label5=tk.Radiobutton(root, text="Encryption",padx = 20, variable=v, value=1,command=choice,bg="light yellow")
label5.config(font=bold_font)
canvas.create_window(100,250,window=label5)
# Radio Button for Decryption
label6=tk.Radiobutton(root, text="Decryption",padx = 20, variable=v, value=2,command=choice,bg="light yellow")
label6.config(font=bold_font)
canvas.create_window(300,250,window=label6)


# Creating a label with a text and attaching it to the root
label7 =tk.Label(root,text="Converted Text ",width=20,bg="MediumPurple1")
# adding the font features to the label
label7.config(font=bold_font)
# placing the label in the canvas
canvas.create_window(200,300,window=label7)



root.mainloop()






