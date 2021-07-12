# Import Required Modules

from tkinter import *
from tkinter import messagebox
import os

#------------------------------------------------------------------------------------------------------------------------------------------------

f=open("database_proj",'a+') # File Open

root = Tk() # Create GUI-Window
root.title("Simple Pharmacy Managment System") # Set Title
root.configure(width=1500,height=600,bg='midnightblue')  # Configure the window
var=-1

#------------------------------------------------------------------------------------------------------------------------------------------------

def additem(): # Function to add Items
    global var
    num_lines = 0
    with open("database_proj", 'r') as f10:
        for line in f10:
            num_lines += 1
    var=num_lines-1
    e1= entry1.get()
    e2=entry2.get()
    e3=entry3.get()
    e4=entry4.get()
    e5=entry5.get()
    f.write('{0} {1} {2} {3} {4}\n'.format(str(e1),e2,e3,str(e4),e5))
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)

#------------------------------------------------------------------------------------------------------------------------------------------------

def deleteitem(): # Function to Delete Items
    e1=entry1.get()
    with open(r"database_proj") as f, open(r"database_proj1", "w") as working:
        for line in f:
            if str(e1) not in line:
                working.write(line)
    os.remove(r"database_proj")
    os.rename(r"database_proj1", r"database_proj")
    f.close()
    working.close()
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)

#------------------------------------------------------------------------------------------------------------------------------------------------

def firstitem(): # Function to redirect to First item 
    global var
    var=0
    f.seek(var)
    c=f.readline()
    v=list(c.split(" "))
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    entry1.insert(0,str(v[0]))
    entry2.insert(0,str(v[1]))
    entry3.insert(0,str(v[2]))
    entry4.insert(0,str(v[3]))
    entry5.insert(0,str(v[4]))
    
#------------------------------------------------------------------------------------------------------------------------------------------------

def nextitem(): # Function to move to next item
    global var
    var = var + 1
    f.seek(var)
    try:
        c=f.readlines()
        xyz = c[var]
        v = list(xyz.split(" "))
        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)
        entry4.delete(0, END)
        entry5.delete(0, END)
        entry1.insert(0, str(v[0]))
        entry2.insert(0, str(v[1]))
        entry3.insert(0, str(v[2]))
        entry4.insert(0, str(v[3]))
        entry5.insert(0, str(v[4]))
    except:
        messagebox.showinfo("Title", "SORRY!...NO MORE RECORDS")
        
#------------------------------------------------------------------------------------------------------------------------------------------------

def previousitem():  # Function to move to previous item
        global var
        var=var-1
        f.seek(var)
        try:
            z = f.readlines()
            xyz=z[var]
            v = list(xyz.split(" "))
            entry1.delete(0, END)
            entry2.delete(0, END)
            entry3.delete(0, END)
            entry4.delete(0, END)
            entry5.delete(0, END)

            entry1.insert(0, str(v[0]))
            entry2.insert(0, str(v[1]))
            entry3.insert(0, str(v[2]))
            entry4.insert(0, str(v[3]))
            entry5.insert(0, str(v[4]))
        except:
            messagebox.showinfo("Title", "SORRY!...NO MORE RECORDS")

#------------------------------------------------------------------------------------------------------------------------------------------------

def lastitem(): # Function to move to last item
    global var
    f4=open("database_proj",'r')
    x=f4.read().splitlines()
    last_line= x[-1]
    num_lines = 0
    with open("database_proj", 'r') as f8:
        for line in f8:
            num_lines += 1
    var=num_lines-1
    print(last_line)
    try:
        v = list(last_line.split(" "))
        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)
        entry4.delete(0, END)
        entry5.delete(0, END)

        entry1.insert(0, str(v[0]))
        entry2.insert(0, str(v[1]))
        entry3.insert(0, str(v[2]))
        entry4.insert(0, str(v[3]))
        entry5.insert(0, str(v[4]))
    except:
        messagebox.showinfo("Title", "SORRY!...NO MORE RECORDS")

#------------------------------------------------------------------------------------------------------------------------------------------------

def updateitem(): # Function to update item

    e1 = entry1.get()
    e2 = entry2.get()
    e3 = entry3.get()
    e4 = entry4.get()
    e5 = entry5.get()
    with open(r"database_proj") as f1, open(r"database_proj1", "w") as working:
        for line in f1:
            if str(e1) not in line:
                working.write(line)
            else:
                working.write('{0} {1} {2} {3} {4}'.format(str(e1), e2, e3, str(e4), e5))
    os.remove(r"database_proj")
    
    os.rename(r"database_proj1", r"database_proj")

#------------------------------------------------------------------------------------------------------------------------------------------------

def searchitem(): # Function search item
    i=0
    e11 = entry1.get()
    with open(r"database_proj") as working:
        for line in working:
            i=i+1
            if str(e11) in line:
                break
        try:
            v = list(line.split(" "))
            entry1.delete(0, END)
            entry2.delete(0, END)
            entry3.delete(0, END)
            entry4.delete(0, END)
            entry5.delete(0, END)
            entry1.insert(0, str(v[0]))
            entry2.insert(0, str(v[1]))
            entry3.insert(0, str(v[2]))
            entry4.insert(0, str(v[3]))
            entry5.insert(0, str(v[4]))
        except:
            messagebox.showinfo("Title", "error end of file")
    working.close()

#------------------------------------------------------------------------------------------------------------------------------------------------

def clearitem(): # Function to clear item
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    
#------------------------------------------------------------------------------------------------------------------------------------------------
    
# Create the Label and Entry for Input

label0= Label(root,text="PHARMACY MANAGEMENT SYSTEM ",bg="royalblue",fg="white",font=("Times", 30))

label1=Label(root,text="ENTER ITEM NAME",bg="blueviolet",relief="ridge",fg="white",font=("Times", 12),width=25)
entry1=Entry(root , font=("Times", 12))

label2=Label(root, text="ENTER ITEM PRICE",bd="2",relief="ridge",height="1",bg="blueviolet",fg="white", font=("Times", 12),width=25)
entry2= Entry(root, font=("Times", 12))

label3=Label(root, text="ENTER ITEM QUANTITY",bd="2",relief="ridge",bg="blueviolet",fg="white", font=("Times", 12),width=25)
entry3= Entry(root, font=("Times", 12))

label4=Label(root, text="ENTER ITEM CATEGORY",bd="2",relief="ridge",bg="blueviolet",fg="white", font=("Times", 12),width=25)
entry4= Entry(root, font=("Times", 12))

label5=Label(root, text="ENTER ITEM DISCOUNT",bg="blueviolet",relief="ridge",fg="white", font=("Times", 12),width=25)
entry5= Entry(root, font=("Times", 12))

# Creating Button For 

button1= Button(root, text="ADD ITEM", bg="blueviolet", fg="black", width=20, font=("Times", 12),command=additem)   # Add item
button2= Button(root, text="DELETE ITEM", bg="blueviolet", fg="black", width =20, font=("Times", 12),command=deleteitem)    # Delete Item
button3= Button(root, text="VIEW FIRST ITEM" , bg="blueviolet", fg="black", width =20, font=("Times", 12),command=firstitem)   # View First Item
button4= Button(root, text="VIEW NEXT ITEM" , bg="blueviolet", fg="black", width =20, font=("Times", 12), command=nextitem)   #View Next item
button5= Button(root, text="VIEW PREVIOUS ITEM", bg="blueviolet", fg="black", width =20, font=("Times", 12),command=previousitem)   #View Previous Item
button6= Button(root, text="VIEW LAST ITEM", bg="blueviolet", fg="black", width =20, font=("Times", 12),command=lastitem)   # View Last Item
button7= Button(root, text="UPDATE ITEM", bg="blueviolet", fg="black", width =20, font=("Times", 12),command=updateitem)   # Update Item
button8= Button(root, text="SEARCH ITEM", bg="blueviolet", fg="black", width =20, font=("Times", 12),command=searchitem)   # Search Item
button9= Button(root, text="CLEAR SCREEN", bg="blueviolet", fg="black", width=20, font=("Times", 12),command=clearitem)   # Clear Screen

# Creating the label grid for position

label0.grid(columnspan=6, padx=10, pady=10)
label1.grid(row=1,column=0, sticky=W, padx=10, pady=10)
label2.grid(row=2,column=0, sticky=W, padx=10, pady=10)
label3.grid(row=3,column=0, sticky=W, padx=10, pady=10)
label4.grid(row=4,column=0, sticky=W, padx=10, pady=10)
label5.grid(row=5,column=0, sticky=W, padx=10, pady=10)

# Creating the entry for input grid for position

entry1.grid(row=1,column=1, padx=40, pady=10)
entry2.grid(row=2,column=1, padx=10, pady=10)
entry3.grid(row=3,column=1, padx=10, pady=10)
entry4.grid(row=4,column=1, padx=10, pady=10)
entry5.grid(row=5,column=1, padx=10, pady=10)

# Allign the buttons 

button1.grid(row=1,column=4, padx=40, pady=10)
button2.grid(row=1,column=5, padx=40, pady=10)
button3.grid(row=2,column=4, padx=40, pady=10)
button4.grid(row=2,column=5, padx=40, pady=10)
button5.grid(row=3,column=4, padx=40, pady=10)
button6.grid(row=3,column=5, padx=40, pady=10)
button7.grid(row=4,column=4, padx=40, pady=10)
button8.grid(row=4,column=5, padx=40, pady=10)
button9.grid(row=5,column=5, padx=40, pady=10)

root.mainloop() # Main loop to execute

#------------------------------------------------------------------------------------------------------------------------------------------------
