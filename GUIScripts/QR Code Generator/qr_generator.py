import pyqrcode
import png
from tkinter import *
from PIL import ImageTk, Image

# Function to get the data from the input field and export it to png format
def get_code():
    data_var = data.get()
    qr = pyqrcode.create(str(data_var))
    qr.png('code.png', scale=6)

 
# Basic GUI setup, title and dimensions are set
base = Tk()
base.geometry("400x200")
base.title("QR Code Generator")

# variable to store the input value from the user
data = StringVar()

# Field to get the input from the user
data_entry = Entry(textvariable=data, width="30")
data_entry.place(x=80,y=50)

# button takes get_code() function as 'command' to call it once the button is clicked 
button = Button(base,text="Get Code",command=get_code,width="30",height="2",bg="grey")
button.place(x=80,y=100)

# Keep running the gui window
base.mainloop()
