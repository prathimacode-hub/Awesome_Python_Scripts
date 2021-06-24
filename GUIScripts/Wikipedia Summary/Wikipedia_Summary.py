from tkinter import *
from tkinter.scrolledtext import ScrolledText
import wikipedia as wiki

def search():
    search_data = ent.get()
    data = wiki.summary(search_data)
    #delete current data
    ent.set('')
    text.delete(0.0,END)
    #INSERT DATA
    search_lbl['text'] = 'Topic to be search given by user is....{}'.format(search_data)
    text.insert(0.0,data)

root = Tk()

#adding icon
p1 = PhotoImage(file = r'C:\Users\HP\Downloads\wiki.png')
root.iconphoto(False, p1)
#giving title to gui
root.title('Wikipedia Summary')
root.geometry('500x680')
root.configure(bg='white')

ent = StringVar()

search_entry = Entry(root,font=('arial',15),bd=2,relief=RIDGE,textvariable=ent)
search_entry.place(x=15,y=11,height=32,width=350)

search_lbl = Label(root,text='Topic to be search given by user is....',font=('arial',12,'bold'),bg='white')
search_lbl.place(x=15,y=65)

text = ScrolledText(root,font=('times',18),bd=4,relief=SUNKEN,wrap = WORD)
text.place(x=15,y=100,height=480,width=480)

search_btn = Button(root,text='search',font=('arial',12,'bold'),width=10,command=search)
search_btn.place(x=380,y=11)

clear_btn = Button(root,text='Clear',font=('arial',12,'bold'),width=10,command=lambda :text.delete(0.0,END))
clear_btn.place(x=105,y=590)

exit_btn = Button(root,text='Exit',font=('arial',12,'bold'),width=10,command=root.quit)
exit_btn.place(x=220,y=590)


root.mainloop()