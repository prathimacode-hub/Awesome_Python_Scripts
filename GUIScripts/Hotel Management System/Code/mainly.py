#Import Modules and py code

import os
from subprocess import call

import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
def click_checkinn():
    call(["python", "checkin_gui.py"])  # Import the checkin_gui Python Code
def click_list():
    call(["python", "list_gui.py"])  # Import the list_gui Python code
def click_checkout():
    call(["python", "checkout_gui.py"]) # Import the checkout_gui Python code
def click_getinfo():
    call(["python","getinfo_gui.py"])  # Import the getinfo_gui Python code


#-------------------------------------------------------------------------------------------------------------------------------------------

class HOTEL_MANAGEMENT:
    def __init__(self):
        root = Tk()
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#306998'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#ffffff' # X11 color: 'white'
        _ana1color = '#ffffff' # X11 color: 'white'
        _ana2color = '#ffffff' # X11 color: 'white'
        font14 = "-family {Segoe UI} -size 15 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font16 = "-family {Swis721 BlkCn BT} -size 40 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        root.geometry("953x739+540+110")  # Setting the size for Application
        root.title("HOTEL MANAGEMENT")   # Title for Application
        root.configure(background="#306998")  # Set background
        root.configure(highlightbackground="#306998")  # Set hilight background
        root.configure(highlightcolor="black") # Set hilight color

     #---------------------------------------------------------------------------------------------------------------------------------

        self.menubar = Menu(root,font=font9,bg=_bgcolor,fg=_fgcolor) # Set Menubar
        root.configure(menu = self.menubar)

     #---------------------------------------------------------------------------------------------------------------------------------

        self.Frame1 = Frame(root) # Set frame for list of buttons
        self.Frame1.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#4b8bbe")
        self.Frame1.configure(highlightbackground="#4b8bbe")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=925)
        
     #---------------------------------------------------------------------------------------------------------------------------------
        
        self.Message6 = Message(self.Frame1) # Text Welcome Messaging
        self.Message6.place(relx=0.09, rely=0.01, relheight=0.15, relwidth=0.86)
        self.Message6.configure(background="#4b8bbe")
        self.Message6.configure(font=font16)
        self.Message6.configure(foreground="#000000")
        self.Message6.configure(highlightbackground="#d9d9d9")
        self.Message6.configure(highlightcolor="black")
        self.Message6.configure(text='''WELCOME''')
        self.Message6.configure(width=791)
        
     #---------------------------------------------------------------------------------------------------------------------------------
        
        self.Button2 = Button(self.Frame1) # Set Button - 1 for Check - Inn 
        self.Button2.place(relx=0.18, rely=0.17, height=103, width=566)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#4b8bbe")
        self.Button2.configure(disabledforeground="#bfbfbf")
        self.Button2.configure(font=font14)
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''1.CHECK INN''')
        self.Button2.configure(width=566)
        self.Button2.configure(command=click_checkinn)
        
     #---------------------------------------------------------------------------------------------------------------------------------
        
        self.Button3 = Button(self.Frame1) # Set Button - 2 for Showing Guest List Name 
        self.Button3.place(relx=0.18, rely=0.33, height=93, width=566)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#4b8bbe")
        self.Button3.configure(disabledforeground="#bfbfbf")
        self.Button3.configure(font=font14)
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''2.SHOW GUEST LIST''')
        self.Button3.configure(width=566)
        self.Button3.configure(command=click_list)
        
     #---------------------------------------------------------------------------------------------------------------------------------
        
        self.Button4 = Button(self.Frame1) # Set Button - 3 for Check - Out 
        self.Button4.place(relx=0.18, rely=0.47, height=93, width=566)
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#4b8bbe")
        self.Button4.configure(disabledforeground="#bfbfbf")
        self.Button4.configure(font=font14)
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''3.CHECK OUT''')
        self.Button4.configure(width=566)
        self.Button4.configure(command=click_checkout)
        
     #---------------------------------------------------------------------------------------------------------------------------------
        
        self.Button5 = Button(self.Frame1) # Set Button - 4 for Getting Info of any Guest 
        self.Button5.place(relx=0.18, rely=0.61, height=103, width=566)
        self.Button5.configure(activebackground="#d9d9d9")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#4b8bbe")
        self.Button5.configure(disabledforeground="#bfbfbf")
        self.Button5.configure(font=font14)
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''4.GET INFO OF ANY GUEST''')
        self.Button5.configure(width=566)
        self.Button5.configure(command=click_getinfo)
        
     #---------------------------------------------------------------------------------------------------------------------------------
        
        self.Button6 = Button(self.Frame1) # Set Button - 5 for Exit the Application
        self.Button6.place(relx=0.18, rely=0.77, height=103, width=566)
        self.Button6.configure(activebackground="#d9d9d9")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="#4b8bbe")
        self.Button6.configure(disabledforeground="#bfbfbf")
        self.Button6.configure(font=font14)
        self.Button6.configure(foreground="#000000")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(pady="0")
        self.Button6.configure(text='''5.EXIT''')
        self.Button6.configure(width=566)
        self.Button6.configure(command=quit)
       
#-------------------------------------------------------------------------------------------------------------------------------------------

        root.mainloop()

if __name__ == '__main__':
    GUUEST=HOTEL_MANAGEMENT()


