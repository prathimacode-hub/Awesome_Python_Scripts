import webbrowser
from tkinter import *
import urllib.request
from tkinter.colorchooser import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import re

#Setting structure of the browser window and variable declarations.
root = Tk()
root.wm_title("CosmoNet web Browser ")
root.iconbitmap('favicon.ico')
url1='http://www.gmail.com'
url2='http://www.yahoomail.com'
url3='http://www.youtube.com'
url4='http://www.facebook.com'
url5='http://www.github.com'
url6='http://www.linkedin.com'
url7='http://www.firefox.com'
url8='http://www.bing.com'
url9='http://www.yahoo.com'

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)


frame=Frame(root)
frame.pack(side=BOTTOM)
b1=ttk.Button(frame, command=lambda aurl=url7:OpenUrl(aurl))
b1.pack(side=LEFT)
m1=PhotoImage(file="firefox.png")
b1.config(image=m1)
tm1=m1.subsample(3,3)
b1.config(image=tm1)
b2=ttk.Button(frame, command=lambda aurl=url8:OpenUrl(aurl))
b2.pack(side=LEFT)
m2=PhotoImage(file="bing.png")
b2.config(image=m2)
tm2=m2.subsample(6,6)
b2.config(image=tm2)
b3=ttk.Button(frame, command=lambda aurl=url9:OpenUrl(aurl))
b3.pack(side=LEFT)
m3=PhotoImage(file="y.png")
b3.config(image=m3)
tm3=m3.subsample(6,6)
b3.config(image=tm3)
Label(root,text='Quick Links : ',font=("Helvetica",16)).pack(side=BOTTOM)

#This is used to open the apps specified in menu bar in our default browser. 
def OpenUrl(url):
    webbrowser.open_new(url)

#This is used to open the color dialog box under Settings tab.
def getColor():
    color = askcolor()

#This  is used to open the downloads folder under downloads tab.
def callback():
    name= askopenfilename() 


#The following functions are used to clear display area and URL field when back button is clicked.
def clear_text():
    text.delete(1.0,'end')
   
    
    
def clear_entry():
    e1.delete(0,'end')
    

def sequence(*functions):
    def func(*args, **kwargs):
        return_value = None
        for function in functions:
            return_value = function(*args, **kwargs)
        return return_value
    return func

"""As soon as Go button is clicked, the data recieved from the server in form of html code is parsed and displayed
   in the text display area."""
#go button
def go():
    lbl.config(image='')
    url=e1.get()
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    respData = resp.read()
    initial = str(respData)[2:-1]
    lines = initial.split('\\n')
    text.insert(INSERT, lines)
    back.config(relief=RAISED)


    
    
#menubar
menu=Menu(root)
root.config(menu=menu)
subMenu=Menu(menu)
menu.add_cascade(label="Apps",menu=subMenu)
subMenu.add_command(label="Gmail", command=lambda aurl=url1:OpenUrl(aurl))
subMenu.add_command(label="Y! Mail", command=lambda aurl=url2:OpenUrl(aurl))
subMenu.add_command(label="Youtube", command=lambda aurl=url3:OpenUrl(aurl))
subMenu.add_command(label="Facebook", command=lambda aurl=url4:OpenUrl(aurl))
subMenu.add_command(label="Github", command=lambda aurl=url5:OpenUrl(aurl))
subMenu.add_command(label="LinkedIn", command=lambda aurl=url6:OpenUrl(aurl))
subMenu.add_separator()
editMenu=Menu(menu)
menu.add_cascade(label="Settings",menu=editMenu)
editMenu.add_command(label="Themes and Colors", command=getColor)
editMenu.add_command(label="History")
editMenu.add_command(label="Connect account...")
editMenu.add_command(label="Exit", command=root.quit)
editMenu=Menu(menu)
menu.add_cascade(label="Bookmarks",menu=editMenu)
editMenu.add_command(label="View")
editMenu.add_command(label="Add bookmark")
editMenu=Menu(menu)
menu.add_cascade(label="Tools",menu=editMenu)
editMenu.add_command(label="Inspect Element")
editMenu.add_command(label="Manage Extensions")
editMenu.add_command(label="Developer Tools")
editMenu=Menu(menu)
menu.add_cascade(label="Downloads",menu=editMenu)
editMenu.add_command(label="Open Downloads Folder", command=callback)
#Buttons and field
    #declaration
itiger=PhotoImage(file="cosmo.png")
tiger= Label(root, image=itiger )
back= Button(root, relief=SUNKEN, command=sequence(clear_entry, clear_text))
iback=PhotoImage(file="back.gif")
back.config(image=iback)
fwd= Button(root, relief=SUNKEN)
ifwd=PhotoImage(file="fwd.gif")
fwd.config(image=ifwd)
refresh=Button(root)
irel=PhotoImage(file="refresh.gif")
refresh.config(image=irel)
stop=Button(root)
istop=PhotoImage(file="close.gif")
stop.config(image=istop)
l1= Label(root, text="URL:")
e1= Entry(root, font=("Helvetica",12))
go=Button(root, text="Go", command = go)
text = Text(root, bd=4, yscrollcommand=scrollbar.set)
scrollbar.config(command=text.yview)


#placement of widgets
tiger.place(x=10, y=10, height= 80, width=100)
back.place(x=120, y=30, height=30, width= 40)
fwd.place(x=170, y=30, height= 30, width= 40)
refresh.place(x=220, y=30, height= 30, width= 30)
l1.place(x=260, y=30, height= 30, width=50)
e1.place(x=300, y=30, height= 30, width= 900)
stop.place(x=1200, y=30, height= 30, width= 30)
go.place(x=1250, y=30, height=30, width= 40)
text.place(x=10, y=100, height=510, width= 1320)
im=PhotoImage(file="im.png")
lbl=Label(text, image=im)
lbl.pack()

root.mainloop()
