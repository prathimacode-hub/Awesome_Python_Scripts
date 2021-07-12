# Import Required modules

import os
import pickle


# Create List

details_list=[]
l2=[]
G = []

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

def file_save(): # Function to save a file
    NAME_PRO = details_list[0]
    ADDRESS_PRO = details_list[1]
    MOBILE_NO_PRO = details_list[2]
    ROOM_NO_PRO = details_list[3]
    PRICE_PRO = details_list[4]
    f = open("hotel.dat", "ab")
    a=save(NAME_PRO,ADDRESS_PRO,MOBILE_NO_PRO,ROOM_NO_PRO,PRICE_PRO)
    pickle.dump(a,f,protocol=2)
    f.close()
    restart_program()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

def restart_program(): # Function to restart program
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------


class save:  # Save Class Starts
    def __init__(self, NAME_PRO, ADDRESS_PRO, MOBILE_NO_PRO, ROOM_NO_PRO, PRICE_PRO):
        self.name=NAME_PRO
        self.address=ADDRESS_PRO
        self.mobile_no=MOBILE_NO_PRO
        self.room_no=ROOM_NO_PRO
        self.price=PRICE_PRO
        print(self.name,self.address,self.mobile_no,self.room_no,self.price)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

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



#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

class HOTEL_MANGMENT_checkin: # Class for Check-in list
    def __init__(self):
        root = Tk() # Set new Window
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#ffffff' # X11 color: 'white'
        _ana1color = '#ffffff' # X11 color: 'white'
        _ana2color = '#ffffff' # X11 color: 'white'
        font11 = "-family {Segoe UI} -size 17 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font14 = "-family {Times New Roman} -size 16 -weight bold " \
                 "-slant roman -underline 0 -overstrike 0"
        
    #----------------------------------------------------------------------------------------------------------------------------------------------------------
        
        root.geometry("780x541+504+123") # Setting size of Window
        root.title("HOTEL MANAGEMENT")
        root.configure(background="#ffffff")
        root.configure(highlightbackground="#ffffff")
        root.configure(highlightcolor="black")

    #----------------------------------------------------------------------------------------------------------------------------------------------------------

        self.Labelframe1 = LabelFrame(root) # Set a Label Frame for List
        self.Labelframe1.place(relx=0.01, rely=0.04, relheight=0.95, relwidth=0.97)
        self.Labelframe1.configure(relief=GROOVE)
        self.Labelframe1.configure(font=font11)
        self.Labelframe1.configure(foreground="black")
        self.Labelframe1.configure(text='''LIST OF ALL GUEST''')
        self.Labelframe1.configure(background="#ffffff")
        self.Labelframe1.configure(highlightbackground="#ffffff")
        self.Labelframe1.configure(highlightcolor="black")
        self.Labelframe1.configure(width=760)

    #----------------------------------------------------------------------------------------------------------------------------------------------------------

        self.Frame1 = Frame(self.Labelframe1)
        self.Frame1.place(relx=0.03, rely=0.1, relheight=0.86, relwidth=0.47, y=-31, h=15)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#ffffff")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=355)

    #----------------------------------------------------------------------------------------------------------------------------------------------------------
        
        self.Label1 = Label(self.Frame1) # Label for names
        self.Label1.place(relx=0.28, rely=0.02, height=37, width=117)
        self.Label1.configure(activebackground="#ffffff")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font11)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#ffffff")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''NAMES''')

    #----------------------------------------------------------------------------------------------------------------------------------------------------------

        self.Text1 = Text(self.Frame1) # Heading Text
        self.Text1.place(relx=0.06, rely=0.16, relheight=0.8, relwidth=0.88)
        self.Text1.configure(background="white")
        self.Text1.configure(font=font14)
        self.Text1.configure(foreground="#000000")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(width=314)
        self.Text1.configure(wrap=WORD)

    #----------------------------------------------------------------------------------------------------------------------------------------------------------

        self.Frame2 = Frame(self.Labelframe1) # Setframe to show details
        self.Frame2.place(relx=0.51, rely=0.1, relheight=0.86, relwidth=0.47, y=-31, h=15)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(background="#d9d9d9")
        self.Frame2.configure(highlightbackground="#ffffff")
        self.Frame2.configure(highlightcolor="black")
        self.Frame2.configure(width=355)
        
    #----------------------------------------------------------------------------------------------------------------------------------------------------------
        
        self.Label2 = Label(self.Frame2) # Label foe Room number
        self.Label2.place(relx=0.37, rely=0.02, height=44, width=152)
        self.Label2.configure(activebackground="#ffffff")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font11)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#ffffff")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''ROOM NO.''')

    #----------------------------------------------------------------------------------------------------------------------------------------------------------

        self.Text2 = Text(self.Frame2)
        self.Text2.place(relx=0.06, rely=0.16, relheight=0.8, relwidth=0.88)
        self.Text2.configure(background="white")
        self.Text2.configure(font=font14)
        self.Text2.configure(foreground="black")
        self.Text2.configure(highlightbackground="#d9d9d9")
        self.Text2.configure(highlightcolor="black")
        self.Text2.configure(insertbackground="black")
        self.Text2.configure(selectbackground="#c4c4c4")
        self.Text2.configure(selectforeground="black")
        self.Text2.configure(width=314)
        self.Text2.configure(wrap=WORD)
        for i in range(0,len(G)):
            s=str(l2[i])
            h=str(G[i])
            self.Text1.insert(INSERT,s+"\n")
            self.Text2.insert(INSERT,h+"\n")


        root.mainloop() # Main loop


#------------------------------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    f2 = open("hotel.dat", "rb")
    try:
        while True:
            s = pickle.load(f2)
            k = s.room_no
            o = s.name.upper()
            l2.append(o)

            G.append(k)
            continue

    except EOFError:
        pass
    f2.close()
    hotel=HOTEL_MANGMENT_checkin()
