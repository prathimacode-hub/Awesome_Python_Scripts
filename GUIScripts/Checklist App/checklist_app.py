from tkinter import *
from tkinter import messagebox
#Define the root window
root=Tk()
root.title("My Checklist App")
root.geometry("400x400")
root.resizable(0,0)


#setting up app theme - font and colours
myFont=("Times New Roman",12)
rootColour = "#3b5998"
buttonColour = "#f7f7f7"

#changing root bg
root.config(bg=rootColour)

#FUNCTIONS
#ADD ITEM FUNCTION
def addItem():
    if listEntry.get() == "":
        messagebox.showinfo("Illegal Entry","Cannot Enter Blank Items")
    else:
        listBox.insert(END,listEntry.get())
        listEntry.delete(0,END)
#REMOVE ITEM FUNCTION
def removeItem():
    listBox.delete(ANCHOR)
#CLEAR LIST FUNCTION
def clearList():
    listBox.delete(0,END)

#SAVE LIST FUNCTION
def saveList():
    with open('checklist.txt','w') as f:
        toSaveList = listBox.get(0,END)
        #print(toSaveList)
        for element in toSaveList:
            if element.endswith("\n"):
                f.write(element)
            else:
                f.write(element+"\n")

#READING FROM FILE WHEN ALL REOPENS
def openList():
    try:
        with open('checklist.txt','r') as f:
            for line in f:
                listBox.insert(END,line)
    except:
        return

#defining the layout of the app

#FRAMES LAYOUT
inputFrame = Frame(root,bg=rootColour)
outputFrame = Frame(root,bg=rootColour)
buttonFrame = Frame(root,bg=rootColour)
inputFrame.pack()
outputFrame.pack()
buttonFrame.pack()

#LAYOUT OF INPUT FRAME ELEMENTS
listEntry = Entry(inputFrame,width=35,borderwidth=3,font=myFont)
listAddButton = Button(inputFrame,text="Add Item",borderwidth=2,font=myFont,bg=buttonColour,command=addItem)
listEntry.grid(row=0,column=0,padx=5,pady=5)
listAddButton.grid(row=0,column=1,padx=5,pady=5,ipadx=5)

#LAYOUT OF OUTPUT FRAME
#Add scrollbar
scrollBar=Scrollbar(outputFrame)
listBox = Listbox(outputFrame,height=15,width=45,borderwidth=3,font=myFont,yscrollcommand=scrollBar.set)
scrollBar.config(command=listBox.yview )
listBox.grid(row=0,column=0)
scrollBar.grid(row=0,column=1,sticky="NS")


#LAYOUT OF BUTTON FRAME
listRemoveButton = Button(buttonFrame,text="Remove Item",borderwidth=2,font=myFont,bg=buttonColour,command=removeItem)
listClearButton = Button(buttonFrame,text="Clear List",borderwidth=2,font=myFont,bg=buttonColour,command=clearList)
saveButton = Button(buttonFrame,text="Save",borderwidth=2,font=myFont,bg=buttonColour,command=saveList)
quitButton = Button(buttonFrame,text="Quit",command=root.destroy,borderwidth=2,font=myFont,bg=buttonColour)
listRemoveButton.grid(row=0,column=0,padx=2,pady=10)
listClearButton.grid(row=0,column=1,padx=2,pady=10,ipadx=10)
saveButton.grid(row=0,column=2,padx=2,pady=10,ipadx=15)
quitButton.grid(row=0,column=30,padx=2,pady=10,ipadx=15)

















openList()
root.mainloop()
