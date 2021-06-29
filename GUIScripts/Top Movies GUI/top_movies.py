# Import Required Modules

from tkinter import *
from tkinter.ttk import Treeview
from tkinter import ttk
import imdb

#---------------------------------------------------------------------------------------------------------------------------------------------------

# Set window

root = Tk()
root.title("Top Movies List")
root.geometry("600x630+100+20")
root.configure(bg='magenta')

#---------------------------------------------------------------------------------------------------------------------------------------------------

#Set Frame

frame = Frame(root , bg = "white" , relief = GROOVE , borderwidth = 5)
frame.place(x = 50 , y = 100 , width = 500 , height = 500)

#Set Scrollbar

scrollX = Scrollbar(frame , orient = HORIZONTAL)  # For horizontal
scrollX.pack(side = BOTTOM , fill = X)

scrollY = Scrollbar(frame , orient = VERTICAL)   # For Vertical
scrollY.pack(side = RIGHT , fill = Y)

#Set style for display

style = ttk.Style()
style.configure("Treeview.Heading" , font = ("Arial" , 16 , "bold") , foreground = "violet")
style.configure("Treeview" , font = ("times" , 14 , "bold") , bg = "pink" , fg = "black")

# Set header for frame

header = Treeview(frame , columns = ("Sr. No." , "Name") , xscrollcommand = scrollX.set , yscrollcommand = scrollY.set)
header.heading("Sr. No." , text = "Sr. No.")
header.heading("Name" , text = "Name", a='c')
header["show"] = "headings"
header.column("Sr. No." , width = 70)
header.column("Name" , width = 500)
header.pack(fill = BOTH , expand = YES)

# Set scrollbar for frame to see image list

scrollX.config(command = header.xview)  # scroll x view that is horizontal view from header in frame
scrollY.config(command = header.yview)  # scroll y view that is horizontal view from header in frame

header.delete(*header.get_children())

n = IntVar()

combo = ttk.Combobox(root, width=8, textvariable=n, font=('ariel 15 bold'))
combo['values'] = [i for i in range(0,250)]
combo.place(x=375, y=25)

movie = imdb.IMDb()
search = movie.get_top250_movies()

#---------------------------------------------------------------------------------------------------------------------------------------------------

def display():  # To display the movies
        header.delete(*header.get_children())
        for m in range(1, n.get()+1):
                listt = [m , search[m]]
                header.insert("" , END , values = listt)  #tree view data

                
select = Label(text="Select the number from 1 to 249 :", font=("Ariel",15,"bold"), bg ='magenta' ) #Set button for getting number of output movie list
select.place(x=45, y=25)
btn = Button(root,text="Display", bg='black', fg='silver', relief=GROOVE, font=("Ariel",15,"bold"), command=display)
btn.place(x=270, y=55)
root.mainloop() # main loop
