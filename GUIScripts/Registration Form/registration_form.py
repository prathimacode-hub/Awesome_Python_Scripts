from tkinter import*
root=Tk()
root.geometry("500x300")
def getvals():
    print("\nAccepted\n")
#heading
Label(root,text="Registration Form",font="ar 15 bold").grid(row=0,column=3)     
#field name
name=Label(root,text="Name")
phone=Label(root,text="Phone")
gender=Label(root,text="Gender")
EmailId=Label(root,text="EmailId")
password=Label(root,text="Password")
#packing field
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
EmailId.grid(row=4,column=2)
password.grid(row=5,column=2)
#variable for storing data
namevalue=StringVar
phonevalue=StringVar
gendervalue=StringVar
EmailIdvalue=StringVar
passwordvalue=StringVar
checkvalue=IntVar
#creating entry field
nameentry=Entry(root,textvariable=namevalue)
phoneentry=Entry(root,textvariable=phonevalue)
genderentry=Entry(root,textvariable=gendervalue)
passwordentry=Entry(root,textvariable=passwordvalue)
EmailIdentry=Entry(root,textvariable=EmailIdvalue)
#packing entry fields
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
EmailIdentry.grid(row=4,column=3)
passwordentry.grid(row=5,column=3)
#creating checkbox
checkbtn=Checkbutton(text="remember me?",variable=checkvalue)
checkbtn.grid(row=6,column=3)
#submit button
Button(text="Submit",command=getvals).grid(row=7,column=3)
root.mainloop()
