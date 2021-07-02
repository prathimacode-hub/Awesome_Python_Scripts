
# imported necessary library
import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
from tkinter import filedialog
import os

root = Tk()
root.geometry('1000x700')
root.title('Text Editor')

# function of popup event
def popup(event):
    cmenu.tk_popup(event.x_root, event.y_root, 0)

# theme choice
def theme():
        global bgc,fgc
        val = themechoice.get()
        clrs = clrschms.get(val)
        fgc, bgc = clrs.split('.')
        fgc, bgc = '#'+fgc, '#'+bgc
        textPad.config(bg=bgc, fg=fgc)

# function for showing info bar
def show_info_bar():
    val = showinbar.get()
    if val:
        infobar.pack(expand=NO, fill=None, side=RIGHT, anchor='se')
    elif not val:
        infobar.pack_forget()

# function defined for updating line number
def update_line_number(event=None):
    txt = ''
    if showln.get(): 
        endline, endcolumn = textPad.index('end-1c').split('.')
        txt = '\n'.join(map(str, range(1, int(endline))))
    lnlabel.config(text=txt, anchor='nw')  # , font=("Arial", 20) ------------------------------------------------------
    currline, curcolumn = textPad.index("insert").split('.')
    infobar.config(text='Line: %s | Column: %s'  %(currline,curcolumn) )

# function for highlighting thr current line
def highlight_line(interval=100):
    textPad.tag_remove("active_line", 1.0, "end")
    textPad.tag_add("active_line", "insert linestart", "insert lineend+1c")
    textPad.after(interval, toggle_highlight)

# function to remove the highlight
def undo_highlight():
    textPad.tag_remove("active_line", 1.0, "end")


def toggle_highlight(event=None):
    val = hltln.get()
    undo_highlight() if not val else highlight_line()

# function defined to show the about message
def about():
    mbox.showinfo("About", "A Simple Text Editor using tkinter GUI")

# function for showing message for help
def help_box(event=None):
    mbox.showinfo("Help", "For help email to aakashrajak02@gmail.com", icon='question')

# function for exiting the editor
def exit_editor():
    if mbox.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()
root.protocol('WM_DELETE_WINDOW',exit_editor)


# demo of indexing and tagging features of text widget
def select_all(event=None):   
    textPad.tag_add('sel', '1.0', 'end')

# function for finding
def on_find(event=None):
    t2 = Toplevel(root)
    t2.title('Find')
    t2.geometry('300x65+200+250')
    t2.transient(root)
    Label(t2,text="Find All:").grid(row=0, column=0, pady=4, sticky='e')
    v=StringVar()
    e = Entry(t2, width=25, textvariable=v)
    e.grid(row=0, column=1, padx=2, pady=4, sticky='we')
    c=IntVar()
    Checkbutton(t2, text='Ignore Case', variable=c).grid(row=1, column=1, sticky='e', padx=2, pady=2)
    Button(t2, text='Find All', underline=0, command=lambda:search_for(v.get(), c.get(), textPad, t2, e)).grid(row=0, column=2, sticky='e'+'w', padx=2, pady=4)
    def close_search():
        textPad.tag_remove('match', '1.0', END)
        t2.destroy()
    t2.protocol('WM_DELETE_WINDOW', close_search)


def search_for(needle,cssnstv, textPad, t2,e) :
        textPad.tag_remove('match', '1.0', END)
        count =0
        if needle:
                pos = '1.0'
                while True:
                    pos = textPad.search(needle, pos, nocase=cssnstv, stopindex=END)
                    if not pos: break
                    lastpos = '%s+%dc' % (pos, len(needle))
                    textPad.tag_add('match', pos, lastpos)
                    count += 1
                    pos = lastpos
                textPad.tag_config('match', foreground='red', background='yellow')
        e.focus_set()
        t2.title('%d matches found' %count)

# function for undoing the event
def undo():
    textPad.event_generate("<<Undo>>")
    update_line_number()

# function for redoing the event
def redo():
    textPad.event_generate("<<Redo>>")
    update_line_number()

# function for cutting
def cut():
    textPad.event_generate("<<Cut>>")
    update_line_number()

# function for copying
def copy():
    textPad.event_generate("<<Copy>>")
    update_line_number()

# function for pasting
def paste():
    textPad.event_generate("<<Paste>>")
    update_line_number()

# function for creating new file
def new_file(event=None):
    global filename
    filename = None
    root.title("Untitled - Tkeditor")
    textPad.delete(1.0, END)
    update_line_number()

# function to open existing file from local system
def open_file(event=None):
    global filename
    filename = filedialog.askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if filename == "": # If no file chosen.
        filename = None # Absence of file.
    else:
        root.title(os.path.basename(filename) + " - Tkeditor") # Returning the basename of 'file'
        textPad.delete(1.0,END)         
        fh = open(filename,"r")        
        textPad.insert(1.0,fh.read()) 
        fh.close()
    update_line_number()

# function to save file
def save(event=None):
    global filename
    try:
        f = open(filename, 'w')
        letter = textPad.get(1.0, 'end')
        f.write(letter)
        f.close()
    except:
        save_as()

# function for save as button
def save_as():
    try:
        # Getting a filename to save the file.
        f = tkFileDialog.asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        fh = open(f, 'w')           
        global filename
        filename = f
        textoutput = textPad.get(1.0, END)
        fh.write(textoutput)              
        fh.close()                
        root.title(os.path.basename(f) + " - Tkeditor") # Setting the title of the root widget.
    except:
        pass

# defining icons for compund menu demonstration
newicon = PhotoImage(file='Images/new_file.gif')
openicon = PhotoImage(file='Images/open_file.gif')
saveicon = PhotoImage(file='Images/Save.gif')
cuticon = PhotoImage(file='Images/Cut.gif')
copyicon = PhotoImage(file='Images/Copy.gif')
pasteicon = PhotoImage(file='Images/Paste.gif')
undoicon = PhotoImage(file='Images/Undo.gif')
redoicon = PhotoImage(file='Images/Redo.gif')

#Define a menu bar
menubar = Menu(root)

#File menu
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", accelerator='Ctrl+N', compound=LEFT, image=newicon, underline=0, command=new_file)
filemenu.add_command(label="Open", accelerator='Ctrl+O', compound=LEFT, image=openicon, underline=0, command=open_file)
filemenu.add_command(label="Save", accelerator='Ctrl+S', compound=LEFT, image=saveicon, underline=0, command=save)
filemenu.add_command(label="Save as", accelerator='Shift+Ctrl+S', command=save_as)
filemenu.add_separator()
filemenu.add_command(label="Exit", accelerator='Alt+F4', command=exit_editor)
menubar.add_cascade(label="File", menu=filemenu) 

#Edit menu
editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Undo", compound=LEFT, image=undoicon, accelerator='Ctrl+Z', command=undo)
editmenu.add_command(label="Redo", compound=LEFT, image=redoicon, accelerator='Ctrl+Y', command=redo)
editmenu.add_separator()
editmenu.add_command(label="Cut", compound=LEFT, image=cuticon, accelerator='Ctrl+X', command=cut)
editmenu.add_command(label="Copy", compound=LEFT, image=copyicon, accelerator='Ctrl+C', command=copy)
editmenu.add_command(labe="Paste", compound=LEFT, image=pasteicon, accelerator='Ctrl+V', command=paste)
editmenu.add_separator()
editmenu.add_command(label="Find", underline=0, accelerator='Ctrl+F', command=on_find)
editmenu.add_separator()
editmenu.add_command(label="Select All", accelerator='Ctrl+A', underline=7, command=select_all)

#View menu
viewmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="View", menu=viewmenu)
showln = IntVar()
showln.set(1)
viewmenu.add_checkbutton(label="Show Line Number", variable=showln)
showinbar = IntVar()
showinbar.set(1)
viewmenu.add_checkbutton(label="Show Info Bar at Bottom", variable=showinbar, command=show_info_bar)
hltln = IntVar()
viewmenu.add_checkbutton(label="Highlight Current Line", variable=hltln, command=toggle_highlight)
themesmenu = Menu(viewmenu, tearoff=0)
viewmenu.add_cascade(label="Themes", menu=themesmenu)

#we define a color scheme dictionary containg name and color code as key value pair
clrschms = { '1. Default White': '000000.FFFFFF', '2. Greygarious Grey':'83406A.D1D4D1','3. Lovely Lavender':'202B4B.E1E1FF' , '4. Aquamarine': '5B8340.D1E7E0','5. Bold Beige': '4B4620.FFF0E1','6. Cobalt Blue':'ffffBB.3333aa','7. Olive Green': 'D1E7E0.5B8340',}
themechoice= StringVar()
themechoice.set('1. Default White')
for k in sorted(clrschms):
    themesmenu.add_radiobutton(label=k, variable=themechoice, command=theme)

#About menu
aboutmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="About", menu=aboutmenu)
aboutmenu.add_command(label="About", command=about)
aboutmenu.add_command(label="Help", command=help_box)

root.config(menu=menubar)

#shortcut bar and line number 
shortcutbar = Frame(root, height=25)
icons = ['new_file', 'open_file', 'save', 'cut', 'copy', 'paste', 'undo', 'redo', 'on_find', 'about']
for i, icon in enumerate(icons):
    tbicon = PhotoImage(file='Images/'+icon+'.gif')
    cmd = eval(icon)
    toolbar = Button(shortcutbar, image=tbicon,  command=cmd)
    toolbar.image = tbicon  #http://effbot.org/tkinterbook/photoimage.htm
    toolbar.pack(side=LEFT)
shortcutbar.pack(expand=NO, fill=X)

lnlabel = Label(root,  width=2,  bg = 'antique white')
lnlabel.pack(side=LEFT, fill=Y)

#Text widget and scrollbar widget
#####################################
textPad = Text(root, undo=True)
textPad.pack(expand=YES, fill=BOTH)
scroll=Scrollbar(textPad)
textPad.configure(yscrollcommand=scroll.set)
scroll.config(command=textPad.yview)
scroll.pack(side=RIGHT, fill=Y)

#Info Bar
infobar = Label(textPad, text='Line: 1 | Column:0')
infobar.pack(expand=NO, fill=None, side=RIGHT, anchor='se')


#context popup menu
cmenu = Menu(textPad,tearoff=0)
for i in ('cut', 'copy', 'paste', 'undo', 'redo'):
    cmd = eval(i)
    cmenu.add_command(label=i, compound=LEFT, command=cmd)  
cmenu.add_separator()
cmenu.add_command(label='Select All', underline=7, command=select_all)
textPad.bind("<Button-3>", popup)

#################################################
#Add events
#Binding events
textPad.bind('<Control-N>', new_file)
textPad.bind('<Control-n>', new_file)
textPad.bind('<Control-O>', open_file)
textPad.bind('<Control-o>', open_file)
textPad.bind('<Control-S>', save)
textPad.bind('<Control-s>', save)
textPad.bind('<Control-A>', select_all)
textPad.bind('<Control-a>', select_all)
textPad.bind('<Control-f>', on_find)
textPad.bind('<Control-F>', on_find)
textPad.bind('<KeyPress-F1>', help_box)

textPad.bind("<Any-KeyPress>", update_line_number)
textPad.tag_configure("active_line", background="ivory2")
root.mainloop()