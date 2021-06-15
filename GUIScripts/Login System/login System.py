from tkinter import *
import tkinter.messagebox as tsmg

root=Tk()
#Taking input from user
def check():
    a=uname.get()
    b=pwd.get()
    c=cpwd.get()
    mix=a+"-"+b+"-"+c
    #  Instead of Login.txt you should write your file name.
    with open("Login.txt","r") as fi:
        d=fi.readlines()
    if b==c:
        if str(mix) in str(d):
            tsmg.showinfo("Welcome",f"Hello {a}, You Have SuccessFully Logged In")
        else:
            tsmg.showerror("Error","No User Found, Please Sign-Up First")
    else:
        tsmg.showerror("Error","Both Password Are Different")
    uname.set("")
    pwd.set("")
    cpwd.set("")
# This function save the data in login.txt file entered by the user
def save():
    a=uname.get()
    b=pwd.get()
    c=cpwd.get()
    mix=a+"-"+b+"-"+c
    if a!="" and b!="" and c!="" :
        with open("Login.txt","r") as fi:
            d=fi.readlines()
        if str(mix) in str(d):
            tsmg.showerror("Error","You Already Have An Account, Please Login")
            uname.set("")
            pwd.set("")
            cpwd.set("")
        elif str(a) in str(d):
            tsmg.showerror("Error","Username Already Exist")
            uname.set("")
            pwd.set("")
            cpwd.set("")
        else:
            if b==c:
                with open("Login.txt","a") as f:
                    f.write(f"{a}-{b}-{c}\n")
                tsmg.showinfo("Success","Your Account Has Been Created")
                uname.set("")
                pwd.set("")
                cpwd.set("")
            else:
                tsmg.showerror("Error","Both Password Are Different")   
                uname.set("")
                pwd.set("")
                cpwd.set("") 

uname=StringVar()
pwd=StringVar()
cpwd=StringVar()

#Heading title of the front page
root.geometry("700x500")
root.title("Welcome To My Page")

f=Frame(root)
Label(f,text="Login To Continue",font="SegoeUI 18 bold",pady=10).pack()
f.pack()

f=Frame(root)
Label(f,text="Username",font="SegoeUI 14 bold",pady=5).pack()
e1=Entry(f,textvariable=uname,font="SegoeUI 14 bold",borderwidth=5,relief=SUNKEN).pack(padx=5,pady=5)
Label(f,text="Password",font="SegoeUI 14 bold",pady=5).pack()
e2=Entry(f,textvariable=pwd,font="SegoeUI 14 bold",borderwidth=5,relief=SUNKEN).pack(padx=5,pady=5)
l1=Label(f,text="Conform-Password",font="SegoeUI 14 bold",pady=5).pack()
e3=Entry(f,textvariable=cpwd,font="SegoeUI 14 bold",borderwidth=5,relief=SUNKEN).pack(padx=5,pady=5)
f.pack()

f=Frame(root)
b1=Button(f,text="Login",font="SegoeUI 10 bold",command=check).pack(side=LEFT,pady=10,padx=10)
b2=Button(f,text="Sign-Up",font="SegoeUI 10 bold",command=save).pack(side=LEFT,pady=10,padx=10)
f.pack()

f=Frame(root)
Label(f,text="Don't Have An Account Then Sign-Up",font="SegoeUI 14 bold",pady=5).pack()
f.pack()

root.mainloop()
