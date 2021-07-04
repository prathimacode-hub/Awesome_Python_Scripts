
# Taxi Hire Application

# imported necessary library
from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox as ms
import sqlite3 # for database
import tkinter.messagebox as mbox

Item4 = 0
geometry = 0
application = 0

# make database and users (if not exists already) table at programme start up
with sqlite3.connect('Users.db') as db:
    c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL ,password TEXT NOT NULL)')
db.commit()
db.close()

#main Class
class user:
    def __init__(self,master):
        # Window
        self.master = master
        # Some Usefull variables
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        #Create Widgets
        self.widgets()

    # defined functon for handling the login process of user
    def login(self):
        # building database connection
        with sqlite3.connect('Users.db') as db:
            c = db.cursor()

        # Finding user in the database
        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user,[(self.username.get()),(self.password.get())])
        result = c.fetchall()
        if result:
            self.logf.pack_forget()
            self.head['text'] = "Welcome, " + self.username.get()
            self.head.configure(fg="green")
            self.head.pack(fill=X)
            application = travel(root)
            
        else:
            # if user name is not found the we show username not found error
            ms.showerror('Oops!','Username Not Found.')

    # creating account for new user
    def new_user(self):
        # building database connection
        with sqlite3.connect('Users.db') as db:
            c = db.cursor()

        # checking if user already has an account
        find_user = ('SELECT * FROM user WHERE username = ?')
        c.execute(find_user,[(self.username.get())])        
        if c.fetchall():
            ms.showerror('Error!','Username Already Taken!')
        else:
            ms.showinfo('Success!','Account Created!')
            self.log()
        # inserting new user details in database
        insert = 'INSERT INTO user(username,password) VALUES(?,?)'
        c.execute(insert,[(self.n_username.get()),(self.n_password.get())])
        db.commit()

    # for creating variable for login
    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'LOGIN'
        self.logf.pack()
    # for defining variable for creating new account
    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()


    # Adding different widgets
    def widgets(self):

        self.head = Label(self.master,text = 'LOGIN', font=("Arial", 70), fg = "brown")
        self.head.pack()
        self.logf = Frame(self.master)
        Label(self.logf,text = 'Username: ',font = ('',25),pady=50,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.username,bd = 5,font = ('',20)).grid(row=0,column=1)
        Label(self.logf,text = 'Password: ',font = ('',25),pady=50,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.password,bd = 5,font = ('',20),show = '*').grid(row=1,column=1)
        Button(self.logf,text = ' Login ',font = ('',20),padx=5,pady=5,command=self.login, bg = "light green", fg = "blue", borderwidth=3, relief="raised").grid(row=2,column=0)
        Button(self.logf,text = ' Create Account ',font = ('',20),padx=5,pady=5,command=self.cr, bg = "light green", fg = "blue", borderwidth=3, relief="raised").grid(row=2,column=1)
        self.logf.pack()
        #
        self.crf = Frame(self.master,padx =10,pady = 10)
        Label(self.crf,text = 'Username: ',font = ('',25),pady=50,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_username,bd = 5,font = ('',20)).grid(row=0,column=1)
        Label(self.crf,text = 'Password: ',font = ('',25),pady=50,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_password,bd = 5,font = ('',20),show = '*').grid(row=1,column=1)
        Button(self.crf,text = 'Create Account',bd = 3 ,font = ('',20),padx=5,pady=5,command=self.new_user, bg = "light green", fg = "blue", borderwidth=3, relief="raised").grid()
        Button(self.crf,text = 'Go to Login',bd = 3 ,font = ('',20),padx=5,pady=5,command=self.log, bg = "light green", fg = "blue", borderwidth=3, relief="raised").grid(row=2,column=1)


class travel:

    def __init__(self,root):
        self.root = root
        self.root.title("Taxi Booking System")
        self.root.geometry(geometry) 
        self.root.configure(background='white')

        DateofOrder=StringVar()
        DateofOrder.set(time.strftime(" %d / %m / %Y "))
        Receipt_Ref=StringVar()
        PaidTax=StringVar()
        SubTotal=StringVar()
        TotalCost=StringVar()

        var1=IntVar()
        var2=IntVar()
        var3=IntVar()
        var4=IntVar()
        journeyType=IntVar()
        carType=IntVar()
        
        varl1=StringVar()
        varl2=StringVar()
        varl3=StringVar()
        reset_counter=0


        Firstname=StringVar()
        Surname=StringVar()
        Address=StringVar()
        Postcode=StringVar()
        Mobile=StringVar()
        Telephone=StringVar()
        Email=StringVar()

        TaxiTax=StringVar()
        Km=StringVar()
        Travel_Ins=StringVar()
        Luggage=StringVar()
        Receipt=StringVar()


        Standard=StringVar()
        PrimeSedan=StringVar()
        PremiumSedan=StringVar()


        TaxiTax.set("0")
        Km.set("0")
        Travel_Ins.set("0")
        Luggage.set("0")


        Standard.set("0")
        PrimeSedan.set("0")
        PremiumSedan.set("0")

    #==========================================Define Functiom==================================================

        def iExit():
            iExit= ms.askyesno("Exit!","Do you want to exit?")
            if iExit > 0:
                root.destroy()
                return

        def Reset():
            TaxiTax.set("0")
            Km.set("0")
            Travel_Ins.set("0")
            Luggage.set("0")

            Standard.set("0")
            PrimeSedan.set("0")
            PremiumSedan.set("0")

            Firstname.set("")
            Surname.set("")
            Address.set("")
            Postcode.set("")
            Mobile.set("")
            Telephone.set("")
            Email.set("")

            PaidTax.set("")
            SubTotal.set("")
            TotalCost.set("")
            self.txtReceipt1.delete("1.0",END)
            self.txtReceipt2.delete("1.0",END)
            
            var1.set(0)
            var2.set(0)
            var3.set(0)
            var4.set(0)
            journeyType.set(0)
            carType.set(0)
            varl1.set("0")
            varl2.set("0")
            varl3.set("0")

            self.cboPickup.current(0)
            self.cboDrop.current(0)
            self.cboPooling.current(0)

            self.txtTaxiTax.configure(state=DISABLED)
            self.txtKm.configure(state=DISABLED)
            self.txtTravel_Ins.configure(state=DISABLED)
            self.txtLuggage.configure(state=DISABLED)
        
            self.txtStandard.configure(state=DISABLED)
            self.txtPrimeSedan.configure(state=DISABLED)
            self.txtPremiumSedan.configure(state=DISABLED)
            self.reset_counter=1

        def Receiptt():
            if reset_counter == 0 and Firstname.get()!="" and Surname.get()!="" and Address.get()!="" and Postcode.get()!="" and Mobile.get()!="" and Telephone.get()!="" and Email.get()!="":
                self.txtReceipt1.delete("1.0",END)
                self.txtReceipt2.delete("1.0",END)
                x=random.randint(10853,500831)
                randomRef = str(x)
                Receipt_Ref.set(randomRef)

                self.txtReceipt1.insert(END,"Receipt Ref:\n")
                self.txtReceipt2.insert(END, Receipt_Ref.get() + "\n")
                self.txtReceipt1.insert(END,'Date:\n')
                self.txtReceipt2.insert(END, DateofOrder.get() + "\n")
                self.txtReceipt1.insert(END,'Taxi No:\n')
                self.txtReceipt2.insert(END, 'TR ' + Receipt_Ref.get() + " BW\n")
                self.txtReceipt1.insert(END,'Firstname:\n')
                self.txtReceipt2.insert(END, Firstname.get() + "\n")
                self.txtReceipt1.insert(END,'Surname:\n')
                self.txtReceipt2.insert(END, Surname.get() + "\n")
                self.txtReceipt1.insert(END,'Address:\n')
                self.txtReceipt2.insert(END, Address.get() + "\n")
                self.txtReceipt1.insert(END,'Postal Code:\n')
                self.txtReceipt2.insert(END, Postcode.get() + "\n")
                self.txtReceipt1.insert(END,'Telephone:\n')
                self.txtReceipt2.insert(END, Telephone.get() + "\n")
                self.txtReceipt1.insert(END,'Mobile:\n')
                self.txtReceipt2.insert(END, Mobile.get() + "\n")
                self.txtReceipt1.insert(END,'Email:\n')
                self.txtReceipt2.insert(END, Email.get() + "\n")
                self.txtReceipt1.insert(END,'From:\n')
                self.txtReceipt2.insert(END, varl1.get() + "\n")
                self.txtReceipt1.insert(END,'To:\n')
                self.txtReceipt2.insert(END, varl2.get() + "\n")
                self.txtReceipt1.insert(END,'Pooling:\n')
                self.txtReceipt2.insert(END, varl3.get() + "\n")
                self.txtReceipt1.insert(END,'Standard:\n')
                self.txtReceipt2.insert(END, Standard.get() + "\n")
                self.txtReceipt1.insert(END,'Prime Sedan:\n')
                self.txtReceipt2.insert(END, PrimeSedan.get() + "\n")
                self.txtReceipt1.insert(END,'Premium Sedan:\n')
                self.txtReceipt2.insert(END, PremiumSedan.get() + "\n")
                self.txtReceipt1.insert(END,'Paid:\n')
                self.txtReceipt2.insert(END, PaidTax.get() + "\n")
                self.txtReceipt1.insert(END,'SubTotal:\n')
                self.txtReceipt2.insert(END, str(SubTotal.get()) + "\n")
                self.txtReceipt1.insert(END,'Total Cost:\n')
                self.txtReceipt2.insert(END, str(TotalCost.get()))
                
            else:
                self.txtReceipt1.delete("1.0",END)
                self.txtReceipt2.delete("1.0",END)
                self.txtReceipt1.insert(END,"\nNo Input")
                

        def Taxi_Tax():
            global Item1
            if var1.get() == 1:
                self.txtTaxiTax.configure(state = NORMAL)
                Item1=float(50)
                TaxiTax.set("Rs " + str(Item1))
            elif var1.get() == 0:
                self.txtTaxiTax.configure(state=DISABLED)
                TaxiTax.set("0")
                Item1=0

        
        def Kilo():
            if var2.get() == 0:
                self.txtKm.configure(state=DISABLED)
                Km.set("0")
            elif var2.get() == 1 and varl1.get() != "" and varl2.get() != "":
                self.txtKm.configure(state=NORMAL)
                if varl1.get() == "Laxmipura":
                    switch ={"Gorwa": 10,"Panchavati": 8,"Bhayli":6,"Laxmipura": 0}
                    Km.set(switch[varl2.get()])
                elif varl1.get() == "Gorwa":
                    switch ={"Gorwa": 0,"Panchavati": 2,"Bhayli":5,"Laxmipura": 10}
                    Km.set(switch[varl2.get()])
                elif varl1.get() == "Panchavati":
                    switch ={"Gorwa": 2,"Panchavati": 0,"Bhayli":3,"Laxmipura": 8}
                    Km.set(switch[varl2.get()])
                elif varl1.get() == "Bhayli":
                    switch ={"Gorwa": 5,"Panchavati": 3,"Bhayli":0,"Laxmipura": 6}
                    Km.set(switch[varl2.get()])        

        
        def Travelling():
            global Item3
            if var3.get() == 1:
                self.txtTravel_Ins.configure(state = NORMAL)
                Item3=float(10)
                Travel_Ins.set("Rs " + str(Item3))
            elif var3.get() == 0:
                self.txtTravel_Ins.configure(state = DISABLED)
                Travel_Ins.set("0")
                Item3=0

        
        def Lug():
            global Item4
            if (var4.get()==1):
                self.txtLuggage.configure(state = NORMAL)
                Item4=float(30)
                Luggage.set("Rs "+ str(Item4))
            elif var4.get()== 0:
                self.txtLuggage.configure(state = DISABLED)
                Luggage.set("0")
                Item4=0

        
        def selectCar():
            global Item5
            if carType.get() == 1:
                self.txtPrimeSedan.configure(state = DISABLED)
                PrimeSedan.set("0") 
                self.txtPremiumSedan.configure(state = DISABLED)
                PremiumSedan.set("0")
                self.txtStandard.configure(state = NORMAL)
                Item5 = float(8)
                Standard.set("Rs "+ str(Item5))
            elif carType.get() == 2:
                self.txtStandard.configure(state =DISABLED)
                Standard.set("0")
                self.txtPremiumSedan.configure(state = DISABLED)
                PremiumSedan.set("0")
                self.txtPrimeSedan.configure(state = NORMAL)
                Item5 = float(10)
                PrimeSedan.set("Rs "+ str(Item5))
            else:
                self.txtStandard.configure(state =DISABLED)
                Standard.set("0")
                self.txtPrimeSedan.configure(state = DISABLED)
                PrimeSedan.set("0")
                self.txtPremiumSedan.configure(state = NORMAL)
                Item5 = float(15)
                PremiumSedan.set("Rs "+ str(Item5))
                
                       
        def Total_Paid():
            if ((var1.get() == 1 and var2.get() == 1 and var3.get() == 1 or var4.get() == 1) and carType.get() != 0 and journeyType.get() != 0 and (varl1.get() != "" and varl2.get() !="")):
                if journeyType.get()==1:
                    Item2=Km.get()
                    Cost_of_fare = (Item1+(float(Item2)*Item5)+Item3+Item4)

                    Tax = "Rs " + str('%.2f'%((Cost_of_fare) *0.09))
                    ST = "Rs " + str('%.2f'%((Cost_of_fare)))
                    TT = "Rs " + str('%.2f'%(Cost_of_fare+((Cost_of_fare)*0.9)))
                elif journeyType.get()==2:
                    Item2=Km.get()
                    Cost_of_fare = (Item1+(float(Item2)*Item5)*1.5+Item3+Item4)

                    Tax = "Rs " + str('%.2f'%((Cost_of_fare) *0.09))
                    ST = "Rs " + str('%.2f'%((Cost_of_fare)))
                    TT = "Rs " + str('%.2f'%(Cost_of_fare+((Cost_of_fare)*0.9)))
                else:
                    Item2=Km.get()
                    Cost_of_fare = (Item1+(float(Item2)*Item5)*2+Item3+Item4)

                    Tax = "Rs " + str('%.2f'%((Cost_of_fare) *0.09))
                    ST = "Rs " + str('%.2f'%((Cost_of_fare)))
                    TT = "Rs " + str('%.2f'%(Cost_of_fare+((Cost_of_fare)*0.9)))

                PaidTax.set(Tax)
                SubTotal.set(ST)
                TotalCost.set(TT)
            else:
                w = ms.showwarning("Error !","Invalid Input\nPlease try again !!!")

            
        # Main application of taxi hire, where user needs to enter all details
        MainFrame=Frame(self.root)
        MainFrame.pack(fill=BOTH)
        
        Tops = Frame(MainFrame, bd=5, width=1350,relief=RIDGE)
        Tops.pack(side=TOP,fill=BOTH)

        self.lblTitle=Label(Tops,font=('arial',50),text=" Taxi Hire Details")
        self.lblTitle.grid()

        # taking customers details
        CustomerDetailsFrame=LabelFrame(MainFrame, width=1350,height=500,bd=5, pady=5, relief=RIDGE)
        CustomerDetailsFrame.pack(side=BOTTOM,fill=BOTH)

        FrameDetails=Frame(CustomerDetailsFrame, width=880,height=400,bd=5, relief=RIDGE)
        FrameDetails.pack(side=LEFT,fill=BOTH)

        CustomerName=LabelFrame(FrameDetails, width=150,height=250,bd=5, font=('arial',12),text="Customer Name", relief=RIDGE)
        CustomerName.grid(row=0,column=0)

        TravelFrame = LabelFrame(FrameDetails,bd=5, width=300,height=250, font=('arial',12),text="Booking Detail", relief=RIDGE)
        TravelFrame.grid(row=0,column=1)

        Book_Frame=LabelFrame(FrameDetails,width=300,height=150,relief=FLAT)
        Book_Frame.grid(row=1,column=0)

        CostFrame = LabelFrame(FrameDetails,width=150,height=150,bd=5,relief=FLAT)
        CostFrame.grid(row=1,column=1)


        # Adding widgets for receipt
        Receipt_BottonFrame=LabelFrame(CustomerDetailsFrame,bd=5, width=450,height=400, relief=RIDGE)
        Receipt_BottonFrame.pack(side=LEFT,fill=BOTH)

        ReceiptFrame=LabelFrame(Receipt_BottonFrame, width=350,height=300, font=('arial',12),text="Receipt", relief=RIDGE)
        ReceiptFrame.grid(row=0,column=0)

        ButtonFrame=LabelFrame(Receipt_BottonFrame, width=350,height=100, relief=RIDGE)
        ButtonFrame.grid(row=1,column=0)

        # Details about customer details
        self.lblFirstname=Label(CustomerName,font=('arial',14),text="Firstname",bd=5)
        self.lblFirstname.grid(row=0,column=0,sticky=W)
        self.txtFirstname=Entry(CustomerName,font=('arial',14,),textvariable=Firstname,bd=5,insertwidth=2,justify=RIGHT)
        self.txtFirstname.grid(row=0,column=1)


        self.lblSurname=Label(CustomerName,font=('arial',14),text="Surname",bd=5)
        self.lblSurname.grid(row=1,column=0,sticky=W)
        self.txtSurname=Entry(CustomerName,font=('arial',14),textvariable=Surname,bd=5,insertwidth=2,justify=RIGHT)
        self.txtSurname.grid(row=1,column=1,sticky=W)


        self.lblAddress=Label(CustomerName,font=('arial',14),text="Address",bd=5)
        self.lblAddress.grid(row=2,column=0,sticky=W)
        self.txtAddress=Entry(CustomerName,font=('arial',14),textvariable=Address,bd=5,insertwidth=2,justify=RIGHT)
        self.txtAddress.grid(row=2,column=1)


        self.lblPostcode=Label(CustomerName,font=('arial',14),text="Postcode",bd=5)
        self.lblPostcode.grid(row=3,column=0,sticky=W)
        self.txtPostcode=Entry(CustomerName,font=('arial',14),textvariable=Postcode,bd=5,insertwidth=2,justify=RIGHT)
        self.txtPostcode.grid(row=3,column=1)


        self.lblTelephone=Label(CustomerName,font=('arial',14),text="Telephone",bd=5)
        self.lblTelephone.grid(row=4,column=0,sticky=W)
        self.txtTelephone=Entry(CustomerName,font=('arial',14),textvariable=Telephone,bd=5,insertwidth=2,justify=RIGHT)
        self.txtTelephone.grid(row=4,column=1)

        self.lblMobile=Label(CustomerName,font=('arial',14),text="Mobile",bd=5)
        self.lblMobile.grid(row=5,column=0,sticky=W)
        self.txtMobile=Entry(CustomerName,font=('arial',14),textvariable=Mobile,bd=5,insertwidth=2,justify=RIGHT)
        self.txtMobile.grid(row=5,column=1)

        self.lblEmail=Label(CustomerName,font=('arial',14),text="Email",bd=5)
        self.lblEmail.grid(row=6,column=0,sticky=W)
        self.txtEmail=Entry(CustomerName,font=('arial',14),textvariable=Email,bd=5,insertwidth=2,justify=RIGHT)
        self.txtEmail.grid(row=6,column=1)

 
        # for showing Taxi Information
        self.lblPickup=Label(TravelFrame,font=('arial',14),text="Pickup",bd=5)
        self.lblPickup.grid(row=0,column=0,sticky=W)

        self.cboPickup =ttk.Combobox(TravelFrame, textvariable = varl1 , state='readonly', font=('arial',20), width=14)
        self.cboPickup['value']=('','Laxmipura','Bhayli','Panchavati','Gorwa')
        self.cboPickup.current(0)
        self.cboPickup.grid(row=0,column=1)


        self.lblDrop=Label(TravelFrame,font=('arial',14),text="Drop",bd=5)
        self.lblDrop.grid(row=1,column=0,sticky=W)

        self.cboDrop =ttk.Combobox(TravelFrame, textvariable = varl2 , state='readonly', font=('arial',20), width=14)
        self.cboDrop['value']=('','Gorwa','Panchavati','Laxmipura','Bhayli')
        self.cboDrop.current(0)
        self.cboDrop.grid(row=1,column=1)

        self.lblPooling=Label(TravelFrame,font=('arial',14),text="Pooling",bd=5)
        self.lblPooling.grid(row=2,column=0,sticky=W)

        self.cboPooling =ttk.Combobox(TravelFrame, textvariable = varl3 , state='readonly', font=('arial',20), width=14)
        self.cboPooling['value']=('','1','2','3','4')
        self.cboPooling.current(1)
        self.cboPooling.grid(row=2,column=1)


        self.chkTaxiTax=Checkbutton(TravelFrame,text="Taxi Tax(Base Charge) *",variable = var1, onvalue=1, offvalue=0,font=('arial',16),command=Taxi_Tax).grid(row=3, column=0, sticky=W)
        self.txtTaxiTax=Label(TravelFrame,font=('arial',14),textvariable=TaxiTax,bd=5,width=18,bg="white",state= DISABLED,justify=RIGHT,relief=SUNKEN)
        self.txtTaxiTax.grid(row=3,column=1)


        self.chkKm=Checkbutton(TravelFrame,text="Distance(KMs) *",variable = var2, onvalue=1, offvalue=0,font=('arial',16),command=Kilo).grid(row=4, column=0, sticky=W)
        self.txtKm=Label(TravelFrame,font=('arial',14),textvariable=Km,bd=5,width=18,bg="white",state= DISABLED,justify=RIGHT,relief=SUNKEN,highlightthickness=0)
        self.txtKm.grid(row=4,column=1)

        self.chkTravel_Ins=Checkbutton(TravelFrame,text="Travelling Insurance *",variable = var3, onvalue=1, offvalue=0,font=('arial',16),command=Travelling).grid(row=5, column=0, sticky=W)
        self.txtTravel_Ins=Label(TravelFrame,font=('arial',14),textvariable=Travel_Ins,bd=5,width=18,bg="white",state= DISABLED,justify=RIGHT,relief=SUNKEN)
        self.txtTravel_Ins.grid(row=5,column=1)

      
        self.chkLuggage=Checkbutton(TravelFrame,text="Extra Luggage",variable = var4, onvalue=1, offvalue=0,font=('arial',16),command=Lug).grid(row=6, column=0, sticky=W)
        self.txtLuggage=Label(TravelFrame,font=('arial',14),textvariable=Luggage,bd=5,width=18,bg="white",state= DISABLED,justify=RIGHT,relief=SUNKEN)
        self.txtLuggage.grid(row=6,column=1)

        # for showing payment information
        self.lblPaidTax=Label(CostFrame,font=('arial',14),text="Paid Tax\t\t",bd=5)
        self.lblPaidTax.grid(row=0,column=2,sticky=W)
        self.txtPaidTax = Label(CostFrame,font=('arial',14),textvariable=PaidTax,bd=5, width=26, justify=RIGHT,bg="white",relief=SUNKEN)
        self.txtPaidTax.grid(row=0,column=3)
            

        
        self.lblSubTotal=Label(CostFrame,font=('arial',14),text="Sub Total",bd=5)
        self.lblSubTotal.grid(row=1,column=2,sticky=W)
        self.txtSubTotal = Label(CostFrame,font=('arial',14),textvariable=SubTotal,bd=5, width=26, justify=RIGHT,bg="white",relief=SUNKEN)
        self.txtSubTotal.grid(row=1,column=3)



        self.lblTotalCost=Label(CostFrame,font=('arial',14),text="Total Cost",bd=5)
        self.lblTotalCost.grid(row=2,column=2,sticky=W)
        self.txtTotalCost = Label(CostFrame,font=('arial',14),textvariable=TotalCost,bd=5, width=26, justify=RIGHT,bg="white",relief=SUNKEN)
        self.txtTotalCost.grid(row=2,column=3)

        # for showing taxi selection option
        self.chkStandard=Radiobutton(Book_Frame,text="Standard",value=1,variable = carType,font=('arial',14),command=selectCar).grid(row=0, column=0, sticky=W)
        self.txtStandard = Label(Book_Frame,font=('arial',14),width =7,textvariable=Standard,bd=5, state= DISABLED, justify=RIGHT,bg="white",relief=SUNKEN)
        self.txtStandard.grid(row=0,column=1)
        

        self.chkPrimeSedand=Radiobutton(Book_Frame,text="PrimeSedan",value=2,variable = carType,font=('arial',14),command=selectCar).grid(row=1, column=0, sticky=W)
        self.txtPrimeSedan= Label(Book_Frame,font=('arial',14),width =7,textvariable=PrimeSedan,bd=5, state= DISABLED, justify=RIGHT,bg="white",relief=SUNKEN)
        self.txtPrimeSedan.grid(row=1,column=1)
             
       
        self.chkPremiumSedan = Radiobutton(Book_Frame,text="PremiumSedan",value=3,variable = carType,font=('arial',14),command=selectCar).grid(row=2, column=0)
        self.txtPremiumSedan = Label(Book_Frame,font=('arial',14),width =7,textvariable=PremiumSedan,bd=5, state= DISABLED, justify=RIGHT,bg="white",relief=SUNKEN)
        self.txtPremiumSedan.grid(row=2,column=1)

        self.chkSingle =Radiobutton(Book_Frame,text="Single",value=1,variable = journeyType,font=('arial',14)).grid(row=0, column=2, sticky=W)
        self.chkReturn =Radiobutton(Book_Frame,text="Return",value=2,variable = journeyType,font=('arial',14)).grid(row=1, column=2, sticky=W)
        self.chkSpecialsNeeds =Radiobutton(Book_Frame,text="SpecialNeeds",value=3,variable = journeyType,font=('arial',14)).grid(row=2, column=2, sticky=W)

        # for receipt
        self.txtReceipt1 = Text(ReceiptFrame,width = 22, height = 21,font=('arial',10),borderwidth=0)
        self.txtReceipt1.grid(row=0,column=0,columnspan=2)
        self.txtReceipt2 = Text(ReceiptFrame,width = 22, height = 21,font=('arial',10),borderwidth=0)
        self.txtReceipt2.grid(row=0,column=2,columnspan=2)

        # for showing button below receipt
        self.btnTotal = Button(ButtonFrame,padx=18,bd=7,font=('arial',11),width = 2,text='Total',command=Total_Paid).grid(row=0,column=0)
        self.btnReceipt = Button(ButtonFrame,padx=18,bd=7,font=('arial',11),width = 2,text='Receipt',command=Receiptt).grid(row=0,column=1)
        self.btnReset = Button(ButtonFrame,padx=18,bd=7,font=('arial',11),width = 2,text='Reset',command=Reset).grid(row=0,column=2)
        self.btnExit = Button(ButtonFrame,padx=18,bd=7,font=('arial',11),width = 2,text='Exit', command=iExit).grid(row=0,column=3)
        


if __name__=='__main__':

    root1 = Tk()
    root1.geometry("1000x700")
    root1.title("Taxi Hire Application")
    c1 = Canvas(root1, width=1000, height=700, bg = "white")  # blue
    c1.pack()
    p1 = PhotoImage(file='Images/taxi.gif')
    c1.create_image(120, 120, image=p1, anchor="nw")
    # w1 = Canvas(self.master)
    # w1.p1 = p1

    top1 =Label(root1, text='TAXI  HIRE', font=("Arial", 50), fg="magenta", bg = "white")
    top1.place(x=330, y=10)

    def root1_des():
        root1.destroy()

    def help_desk():
        mbox.showinfo("Taxi Help", "How to use this application :\n\n1.)  First on the starting page of application, user need to click on the START button to enter the LOGIN/CREATE ACCOUNT page.\n\n2.)  Here user needs to create a new account is he/she doesn't already have an account.\n\n3.)  If User already has an account in Taxi Hire Appplication, then he/she just need to LOGIN using Username and Password.\n\n4.)  After User Login is sucessfull, then user will be directed to the main application window.\n\n5.)  Now here user needs to enter his details like FirstName, SurName, Address, PostCode, Telephone, Mobile No., Email Id. Also user needs to select with which feature he/she want to go like, Strandard, or Prime Sedan or Premium Sedan. And how he/she wants to go, like Single, Return or with special needs.\n\n6.)  After selecting these details, now user needs to select the starting and destination address of his/her route.\n\n7.)  After selcting all thses details, when user clicks on the TOTAL button, he/she, will be able to see the total price he/she needs to pay.\n\n8.)  User will also be able to see the receipt for that particular route.\n\n9.)  Also there is RESET button, clicking on which user can reset the details entered.")

    def exit_win1():
        if mbox.askokcancel("Exit", "Do you want to exit?"):
            root1.destroy()
            return

    # Creating Help Button
    Button(root1, text="HELP", command=help_desk, font=("Arial", 20), bg="orange", fg="blue", borderwidth=3,relief="raised").place(x=200, y=550)

    # Creating Start Button
    Button(root1, text="START", command=root1_des, font=("Arial", 20), bg="light green", fg="blue",borderwidth=3, relief="raised").place(x=440, y=550)

    # Creating Exit Button
    Button(root1, text="EXIT", command=exit_win1, font=("Arial", 20), bg="red", fg="blue", borderwidth=3,relief="raised").place(x=700, y=550)

    bottom1 = Label(root1, text='⭐🌟 Have A Happy And Safe Trip 🌟⭐', font=("Arial", 30), fg="blue", bg="white")
    bottom1.place(x=150, y=630)

    root1.protocol("WM_DELETE_WINDOW", exit_win1)
    root1.mainloop()


    root = Tk()

    w = 1280
    h = 650
    geometry="%dx%d+%d+%d"%(w,h,0,0)

    def exit_win():
        if mbox.askokcancel("Exit", "Do you want to exit?"):
            root.destroy()

    root.geometry("1000x700+320+200")
    root.title('Login Form')
    application = user(root)
    root.protocol("WM_DELETE_WINDOW", exit_win)
    root.mainloop()
    
