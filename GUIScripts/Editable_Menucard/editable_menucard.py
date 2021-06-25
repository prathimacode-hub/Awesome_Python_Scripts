#######################################################################################################################
#Importing
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
from tkinter import ttk
#######################################################################################################################

#=======Colorcodes=====================================================================================================
WHITE='#ffffff'
BLACK='#000000'
YELLOW_O='#ae9c84'
RED='#ff0000'

#======================================================================================================================
#========Class Definitions=============================================================================================

#Class for dealing with the menu items

class Menu(object):
    def __init__(self,items,customer,customerOrder):
        #====
        self.type1=None
        self.name=None
        self.price=None
        self.desc=None
        self.items=items
        self.id_no=None

        self.orderListC=[]

        self.countA=0
        self.countA1=0
        
        self.username_var=StringVar()
        self.id_var=StringVar()
        self.usernameOrder=StringVar()
        self.itemnameA=StringVar()
        self.itemnameA.set("")
        self.itemname=StringVar()
        self.itemname.set("")
        
        self.type1_var=StringVar()
        self.price_var=StringVar()
        self.itemnamevar=StringVar()
        self.status=StringVar()
        self.qty=StringVar()
        self.cost=StringVar()
        

        
        self.cost.set("0")
        self.customer=customer
        self.customerOrder=customerOrder

    

#========Functions ====================================

#-----------------------------------------------------------------------------------------------------------------------------------------------

##    Background Functions directly making value changes 
##    to the list provided. Checks Error with the input.
    def Add_Item(self):
        if (self.day.get() != '') and (self.type1.get() != '') and (self.name.get() != '') and (self.price.get() != '') and (self.desc.get() != '') and (self.id_no.get() != ''): 
            item=[]
            item.append(self.type1.get())
            item.append(self.name.get())
            item.append(self.price.get())
            item.append(self.desc.get())
            item.append(self.id_no.get())
            item.append(self.day.get())

            self.items.append(item)
            print(self.items)
            self.DashboardA_draw()

        else:
            messagebox.showerror('Error','All fields are Required!',parent=self.root)

    def Remove_Item(self):
        if (self.day.get() != '') and (self.type1.get() != '') and (self.name.get() != '') and (self.price.get() != '') and (self.desc.get() != '') and (self.id_no.get() != ''):
            flag=0
            for i in range(len(self.items)):
                if (self.items[i][4]==self.id_no.get()) and (self.day.get()==self.items[i][5]) and (self.type1.get()==self.items[i][0]) and (self.price.get()==self.items[i][2]) and (self.desc.get()==self.items[i][3]) and (self.name.get()==self.items[i][1]):
                    flag=1
                    print(self.items)
                    break
                
            if flag==1:
                #print(self.items)
                del self.items[i]
                self.DashboardA_draw()
            else:
                    messagebox.showerror('Error','Item not found',parent=self.root)
                    #print('Item: {} is not found'.format(self.id_no.get()))
            

        else:
            messagebox.showerror('Error','All fields are Required!',parent=self.root)


    def Change_Price(self):
        if (self.day.get() != '') and (self.type1.get() != '') and (self.name.get() != '') and (self.price.get() != '') and (self.desc.get() != '') and (self.id_no.get() != ''):
            flag=0
            for i in range(len(self.items)):
                if (self.items[i][4]==self.id_no.get()) and (self.day.get()==self.items[i][5]) and (self.type1.get()==self.items[i][0]) and (self.desc.get()==self.items[i][3]) and (self.name.get()==self.items[i][1]):
                    flag=1
                    break
                    
            if flag==1:
                self.items[i][2]=self.price.get()
                #print(self.items)
                self.DashboardA_draw()
            else:
                messagebox.showerror('Error','Item not found',parent=self.root)
                    #print('Item: {} is not found'.format(self.id_no.get()))

                

        else:
            messagebox.showerror('Error','All fields are Required!',parent=self.root)


    def Change_Desc(self):
        if (self.day.get() != '') and (self.type1.get() != '') and (self.name.get() != '') and (self.price.get() != '') and (self.desc.get() != '') and (self.id_no.get() != ''):
            flag=0
            for i in range(len(self.items)):
                if (self.items[i][4]==self.id_no.get()) and (self.day.get()==self.items[i][5]) and (self.type1.get()==self.items[i][0]) and (self.price.get()==self.items[i][2]) and (self.name.get()==self.items[i][1]):
                    flag=1
                    #self.items[i][3]=self.desc.get()
                    break
                    
            if flag==1:
                self.items[i][3]=self.desc.get()
                #print(self.items)
                self.DashboardA_draw()
            else:
                messagebox.showerror('Error','Item not found',parent=self.root)
                #print('Item: {} is not found'.format(self.id_no.get()))

                

        else:
            messagebox.showerror('Error','All fields are Required!',parent=self.root)

#------------------------------------------------------------------------------------------------------------------------------------------------

#################################################################################################################################################

#------------------------------------------------------------------------------------------------------------------------------------------------

#Class for the Design of the Display.

class basicFormat(Menu):
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def __init__(self,root,items,customer,customerOrder):
        super().__init__(items,customer,customerOrder)
        #---------------------------------------------------------------------
        #Setting up of root
        self.root=root
        self.root.title("Restaurant")
        self.root.geometry('1000x773+400+0')
        self.root.resizable(False,False)
        #====BG Img========
        self.bg=ImageTk.PhotoImage(file="Images/bg_img.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        #---------------------------------------------------------------------

        #====Title Design=====================================================
        Frame_title=Frame(self.root,bg=BLACK)
        Frame_title.place(x=350,y=100,height=80,width=600)
        title=Label(Frame_title,text='Your Restaurant Name',font=("times new roman",35,"bold"),bg=BLACK,fg='#ae9c84').place(x=40,y=10)

        #====List of Days Design==============================================
        Frame_listofdays=Frame(self.root,bg=BLACK)
        Frame_listofdays.place(x=333,y=290,height=40,width=665)
        
        #====Buttons for days of the week======================================
        Btn_mon=Button(Frame_listofdays,cursor='hand2',command=self.MonDraw_menu,text='Monday',fg=BLACK,bg=YELLOW_O,font=("times new roman",10)).place(x=5.5,y=5,height=30,width=90)
        Btn_tue=Button(Frame_listofdays,cursor='hand2',command=self.TueDraw_menu,text='Tuesday',fg=BLACK,bg=YELLOW_O,font=("times new roman",10)).place(x=99.5,y=5,height=30,width=90)
        Btn_wed=Button(Frame_listofdays,cursor='hand2',command=self.WedDraw_menu,text='Wednesday',fg=BLACK,bg=YELLOW_O,font=("times new roman",10)).place(x=193.5,y=5,height=30,width=90)
        Btn_thu=Button(Frame_listofdays,cursor='hand2',command=self.ThuDraw_menu,text='Thursday',fg=BLACK,bg=YELLOW_O,font=("times new roman",10)).place(x=287.5,y=5,height=30,width=90)
        Btn_fri=Button(Frame_listofdays,cursor='hand2',command=self.FriDraw_menu,text='Friday',fg=BLACK,bg=YELLOW_O,font=("times new roman",10)).place(x=381.5,y=5,height=30,width=90)
        Btn_sat=Button(Frame_listofdays,cursor='hand2',command=self.SatDraw_menu,text='Saturday',fg=BLACK,bg=YELLOW_O,font=("times new roman",10)).place(x=475.5,y=5,height=30,width=90)
        Btn_sun=Button(Frame_listofdays,cursor='hand2',command=self.SunDraw_menu,text='Sunday',fg=BLACK,bg=YELLOW_O,font=("times new roman",10)).place(x=569.5,y=5,height=30,width=90)

        #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
##        Frame definitions for the sides with
##        regular changes. Left Side Frame for
##        buttons and Working frame placed at centre
##        where display happens.
        #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        #====Working Frame====
        self.Frame_work=Frame(self.root,bg=BLACK)
        self.Frame_work.place(x=340,y=360,height=403,width=653)
        
        #====Buttons Frame Left====
        self.Frame_btn=Frame(self.root,bg=BLACK)
        self.Frame_btn.place(x=0,y=0,height=1000,width=330)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def Draw_menu(self):
        self.clear_workframe()
        #===Treeview Display of Menu items to both Admin and Customer========================================================================================================
        self.tv=ttk.Treeview(self.Frame_work)
        self.tv['columns']=('ID','Itemname','Price','Description','Type')
        self.tv.column('#0',width=0,stretch=NO)
        self.tv.column('ID',anchor=CENTER,width=40)
        self.tv.column('Itemname',anchor=CENTER,width=110)
        self.tv.column('Price',anchor=CENTER,width=50)
        self.tv.column('Description',anchor=CENTER,width=380)
        self.tv.column('Type',anchor=CENTER,width=70)

        self.tv.heading('#0',text='',anchor=CENTER)
        self.tv.heading('ID',text='ID',anchor=CENTER)
        self.tv.heading('Itemname',text='Itemname',anchor=CENTER)
        self.tv.heading('Price',text='Price',anchor=CENTER)
        self.tv.heading('Description',text='Description',anchor=CENTER)
        self.tv.heading('Type',text='Type',anchor=CENTER)

        self.tv.pack()

        

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #===Functions to clear previous screens======

    def clear_workframe(self):
        for widgets in self.Frame_work.winfo_children():
            widgets.destroy()

    def clear_btnframe(self):
        for widgets in self.Frame_btn.winfo_children():
            widgets.destroy()
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

###################################################################################################################################################################################

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            
##Class for the Design of Display after users
##have logged-in.

class afterLogin(basicFormat):
    def __init__(self,root,items,customer,customerOrder):
        super().__init__(root,items,customer,customerOrder)
        self.Home_page()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def Afterlogin_page(self):

##    Function for the design of basic
##    page after login. User distinction
##    not made yet.
        self.clear_btnframe()
        
        #====User Icon set-up========================================================================================================================================================

        self.use=PhotoImage(file="Images/user.png")
        self.use_img=Label(self.Frame_btn,image=self.use).place(x=100,y=100)

        #====Username Display on the left============================================================================================================================================

        Frame_user=Frame(self.Frame_btn,bg=BLACK)
        Frame_user.place(x=70,y=290,height=40,width=200)
        
        lbl_user=Label(Frame_user,text=self.customer[self.tu][0],font=("times new roman",20),bg=BLACK,fg=YELLOW_O).place(x=40,y=0)

        #====Home Button====================================================================================================================================================================

        Frame_home=Frame(self.Frame_btn,bg=BLACK)
        Frame_home.place(x=70,y=360,height=40,width=200)
    
        Btn_home=Button(Frame_home,text='Home',cursor='hand2',command=self.MonDraw_menu,fg=YELLOW_O,bg=BLACK,font=("times new roman",20)).place(x=0,y=0,height=40,width=200)

        #====Dashboard Button========================================================================================================================================================
        Frame_dashboard=Frame(self.Frame_btn,bg=BLACK)
        Frame_dashboard.place(x=70,y=430,height=40,width=200)
        Btn_dashboard=Button(Frame_dashboard,text='Dashboard',cursor='hand2',command=self.Dashboard_draw,fg=YELLOW_O,bg=BLACK,font=("times new roman",20)).place(x=0,y=0,height=40,width=200)

        #====Orders Button======================================================================================================================================================
        Frame_orders=Frame(self.Frame_btn,bg=BLACK)
        Frame_orders.place(x=70,y=500,height=40,width=200)
        Btn_orders=Button(Frame_orders,text='Orders',cursor='hand2',command=self.Orders_draw,fg=YELLOW_O,bg=BLACK,font=("times new roman",20)).place(x=0,y=0,height=40,width=200)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        #==== After Login calling of the functions a/c to user when Left Hand Buttons pressed=====

    def HomeA_page(self):
        #Function for the Home page of Admin
        self.MonDraw_menu()
        self.Afterlogin_page()

    def Dashboard_draw(self):
        #Function for Dashboard
        if self.tu=='Admin':
            self.DashboardA_draw()
        else:
            self.DashboardC_draw()

    def Orders_draw(self):
        #Function for Orders Page
        if self.tu=='Admin':
            self.OrdersA_draw()
        else:
            self.OrdersC_draw()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------       
        #=====Dashboard of Admin Design=================================================================================================================================================
    def DashboardA_draw(self):
        self.clear_workframe()
        
        Frame_add=Frame(self.Frame_work,bg=YELLOW_O)
        Frame_add.place(x=20,y=0,height=40,width=600)
        lbl_add=Label(Frame_add,text='Add Item',font=('times new roman',20),bg=YELLOW_O,fg=BLACK).place(x=10,y=0,height=40,width=100)
        Btn_add=Button(Frame_add,cursor='hand2',command=self.AddItem,text='Add Item',bg=WHITE,fg=BLACK,font=('times new roman',12)).place(x=400,y=5,height=20,width=100)

        Frame_remove=Frame(self.Frame_work,bg=YELLOW_O)
        Frame_remove.place(x=20,y=60,height=40,width=600)
        lbl_remove=Label(Frame_remove,text='Remove Item',font=('times new roman',20),bg=YELLOW_O,fg=BLACK).place(x=10,y=0,height=40,width=148)
        Btn_remove=Button(Frame_remove,cursor='hand2',command=self.RemoveItem,text='Remove Item',bg=WHITE,fg=BLACK,font=('times new roman',12)).place(x=400,y=5,height=20,width=100)

        Frame_changeprice=Frame(self.Frame_work,bg=YELLOW_O)
        Frame_changeprice.place(x=20,y=120,height=40,width=600)
        lbl_changeprice=Label(Frame_changeprice,text='Change Price',font=('times new roman',20),bg=YELLOW_O,fg=BLACK).place(x=10,y=0,height=40,width=148)
        Btn_changeprice=Button(Frame_changeprice,cursor='hand2',command=self.ChangePrice,text='Change Price',bg=WHITE,fg=BLACK,font=('times new roman',12)).place(x=400,y=5,height=20,width=140)

        Frame_changedesc=Frame(self.Frame_work,bg=YELLOW_O)
        Frame_changedesc.place(x=20,y=180,height=40,width=600)
        lbl_changedesc=Label(Frame_changedesc,text='Change Description',font=('times new roman',20),bg=YELLOW_O,fg=BLACK).place(x=10,y=0,height=40,width=250)
        Btn_changedesc=Button(Frame_changedesc,cursor='hand2',command=self.ChangeDescription,text='Change Description',bg=WHITE,fg=BLACK,font=('times new roman',12)).place(x=400,y=5,height=20,width=140)

        Frame_Alogout=Frame(self.Frame_work,bg=YELLOW_O)
        Frame_Alogout.place(x=20,y=240,height=40,width=600)
        Btn_Alogout=Button(Frame_Alogout,cursor='hand2',command=self.Home_page,text='Logout',bg=WHITE,fg=BLACK,font=('times new roman',12)).place(x=10,y=5,height=30,width=150)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        #=======Layout Design of Functions present on Dashboard of Admin======================================================================================================================

##    This function is to set up the layout of
##    pages following the functions present
##    on the dashboard of the Admin

        
    def DashboardA_layout_draw(self):
        self.clear_workframe()

        Frame_day=Frame(self.Frame_work,bg=YELLOW_O)
        Frame_day.place(x=20,y=0,height=40,width=600)
        lbl_day=Label(Frame_day,text='Day',font=('times new roman',20),bg=YELLOW_O,fg=BLACK).place(x=10,y=0,height=40,width=100)
        self.day=Entry(Frame_day,font=("times new roman",12),bg='lightgray')
        self.day.place(x=400,y=5,height=20,width=140)
        
        

        Frame_type1=Frame(self.Frame_work,bg=YELLOW_O)
        Frame_type1.place(x=20,y=60,height=40,width=600)
        lbl_type1=Label(Frame_type1,text='Type',font=('times new roman',20),bg=YELLOW_O,fg=BLACK).place(x=10,y=0,height=40,width=100)
        self.type1=Entry(Frame_type1,font=("times new roman",12),bg='lightgray')
        self.type1.place(x=400,y=5,height=20,width=140)

        Frame_name=Frame(self.Frame_work,bg=YELLOW_O)
        Frame_name.place(x=20,y=120,height=40,width=600)
        lbl_name=Label(Frame_name,text='Name',font=('times new roman',20),bg=YELLOW_O,fg=BLACK).place(x=10,y=0,height=40,width=100)
        self.name=Entry(Frame_name,font=("times new roman",12),bg='lightgray')
        self.name.place(x=400,y=5,height=20,width=140)


        Frame_price=Frame(self.Frame_work,bg=YELLOW_O)
        Frame_price.place(x=20,y=180,height=40,width=600)
        lbl_price=Label(Frame_price,text='Price',font=('times new roman',20),bg=YELLOW_O,fg=BLACK).place(x=10,y=0,height=40,width=100)
        self.price=Entry(Frame_price,font=("times new roman",12),bg='lightgray')
        self.price.place(x=400,y=5,height=20,width=140)


        Frame_desc=Frame(self.Frame_work,bg=YELLOW_O)
        Frame_desc.place(x=20,y=240,height=40,width=600)
        lbl_desc=Label(Frame_desc,text='Description',font=('times new roman',20),bg=YELLOW_O,fg=BLACK).place(x=10,y=0,height=40,width=150)
        self.desc=Entry(Frame_desc,font=("times new roman",12),bg='lightgray')
        self.desc.place(x=400,y=5,height=20,width=140)


        Frame_id_no=Frame(self.Frame_work,bg=YELLOW_O)
        Frame_id_no.place(x=20,y=300,height=40,width=600)
        lbl_id_no=Label(Frame_id_no,text='ID no.',font=('times new roman',20),bg=YELLOW_O,fg=BLACK).place(x=10,y=0,height=40,width=100)
        self.id_no=Entry(Frame_id_no,font=("times new roman",12),bg='lightgray')
        self.id_no.place(x=400,y=5,height=20,width=140)
        
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        

    #======Functions Combining DIsplay and functionality of Admin's Dashboard============================================================================================================    

    def AddItem(self):
        self.DashboardA_layout_draw()
        btn_submit=Button(self.Frame_work,cursor='hand2',command=self.Add_Item,text='Submit',bg="red",fg=WHITE,font=('times new roman',12)).place(x=200,y=350,height=30,width=150)       

    def RemoveItem(self):
        self.DashboardA_layout_draw()
        btn_submit=Button(self.Frame_work,cursor='hand2',command=self.Remove_Item,text='Submit',bg="red",fg=WHITE,font=('times new roman',12)).place(x=200,y=350,height=30,width=150)
        
    def ChangePrice(self):
        self.DashboardA_layout_draw()
        btn_submit=Button(self.Frame_work,cursor='hand2',command=self.Change_Price,text='Submit',bg="red",fg=WHITE,font=('times new roman',12)).place(x=200,y=350,height=30,width=150)
        
    def ChangeDescription(self):
        self.DashboardA_layout_draw()
        btn_submit=Button(self.Frame_work,cursor='hand2',command=self.Change_Desc,text='Submit',bg="red",fg=WHITE,font=('times new roman',12)).place(x=200,y=350,height=30,width=150)

        
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        

    #=====Orders Page of Admin============================================================================================================================================================
    def OrdersA_draw(self):
        self.clear_workframe()

        #=======Order Display List===============
        self.Atv=ttk.Treeview(self.Frame_work)
        self.Atv['columns']=('ID','Username','Itemname','Qty','Cost','Status')
        self.Atv.column('#0',width=0,stretch=NO)
        self.Atv.column('ID',anchor=CENTER,width=50)
        self.Atv.column('Username',anchor=CENTER,width=140)
        self.Atv.column('Itemname',anchor=CENTER,width=140)
        self.Atv.column('Qty',anchor=CENTER,width=90)
        self.Atv.column('Cost',anchor=CENTER,width=100)
        self.Atv.column('Status',anchor=CENTER,width=100)

        self.Atv.heading('#0',text='',anchor=CENTER)
        self.Atv.heading('ID',text='ID',anchor=CENTER)
        self.Atv.heading('Username',text='Username',anchor=CENTER)
        self.Atv.heading('Itemname',text='Itemname',anchor=CENTER)
        self.Atv.heading('Qty',text='Qty',anchor=CENTER)
        self.Atv.heading('Cost',text='Cost',anchor=CENTER)
        self.Atv.heading('Status',text='Status',anchor=CENTER)
        self.Atv.pack()

        for item in (self.orderListC):
            self.Atv.insert(parent='',index='end',iid=self.countA,text='',values=(item))
            self.Atv.pack()
            self.countA+=1





        
        #=======Admin Order Status Counter===============================================================================================================================================================
        lbl_order=Label(self.Frame_work,text='Enter to update the status of Ordered Items here:',font=('times new roman',12),bg=YELLOW_O,fg=BLACK).place(x=0,y=290,height=20,width=660)

        Frame_Aid=Frame(self.Frame_work,bg=WHITE)
        Frame_Aid.place(x=0,y=320,height=80,width=70)
        lbl_Aid=Label(Frame_Aid,text='ID here:',font=('times new roman',12),bg=YELLOW_O,fg=BLACK).place(x=0,y=0,height=20,width=70)
        self.txt_id=Entry(Frame_Aid,textvariable=self.id_var,font=("times new roman",18),bg='lightgray')
        self.txt_id.place(x=10,y=35,height=30,width=50)

        Frame_Ausername=Frame(self.Frame_work,bg=WHITE)
        Frame_Ausername.place(x=72,y=320,height=80,width=200)
        lbl_Ausername=Label(Frame_Ausername,text='Username here:',font=('times new roman',12),bg=YELLOW_O,fg=BLACK).place(x=0,y=0,height=20,width=200)
        self.user_key=Entry(Frame_Ausername,textvariable=self.usernameOrder,font=("times new roman",18),bg='lightgray')
        self.user_key.place(x=10,y=35,height=30,width=180)

        Frame_Aitemname=Frame(self.Frame_work,bg=WHITE)
        Frame_Aitemname.place(x=274,y=320,height=80,width=232)
        lbl_Aitemname=Label(Frame_Aitemname,text='Item name here:',font=('times new roman',12),bg=YELLOW_O,fg=BLACK).place(x=0,y=0,height=20,width=232)
        lbl_AitemnameOrder=Label(Frame_Aitemname,textvariable=self.itemnameA,font=('times new roman',12),bg=WHITE,fg=BLACK).place(x=0,y=25,height=20,width=232)

        Frame_Astatus=Frame(self.Frame_work,bg=WHITE)
        Frame_Astatus.place(x=508,y=320,height=80,width=142)
        lbl_Astatus=Label(Frame_Astatus,text='Status:',font=('times new roman',12),bg=YELLOW_O,fg=BLACK).place(x=0,y=0,height=20,width=142)

        self.stat_val=StringVar()
        self.stat_val.set("Preparing")

        Btn_status=Button(Frame_Astatus,cursor='hand2',command=self.change_statusA,text='Complete',bg=WHITE,fg=BLACK,font=('times new roman',12)).place(x=30,y=30,height=20,width=100)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#==============Admin Order Counter Functionality============================================================================================================================================
##Checking of Entries at Admin Order COunter
##for errors. Updating status and display list.
##Removing Delivered items. Updating the List of orders

    def change_statusA(self):
        if (self.usernameOrder.get()!='') and (self.txt_id.get() != ''):
            self.stat_val.set('Delivered')
            self.status.set('Delivered')
            self.user_comp=self.usernameOrder.get()
            self.disid=self.id_var.get()

            for item in self.orderListC:
                if item[1]==self.user_comp:
                    item1=list(item)
                    self.orderListC.remove(item)
                    item1[5]='Delivered'
                    item=tuple(item1)
                    self.orderListC.append(item)
                    print(self.orderListC)
                
            for i in range(len(self.items)):
                if self.items[i][4]==self.disid:
                    self.itemnameA.set(self.items[i][1])
                    print(self.itemnameA)
            self.customerOrder[self.user_comp].remove(self.disid)
            self.OrdersA_draw()

        else:
            messagebox.showerror('Error','All fields are required!',parent=self.root)
                
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


        #=======Home Page Before Login===========================================================================================================================================
    def Home_page(self):
        self.clear_workframe()
        self.clear_btnframe()

        #==Login Button Placement================================================================================================================================================
        Frame_beforelogin=Frame(self.Frame_btn,bg=WHITE)
        Frame_beforelogin.place(x=70,y=120,height=40,width=200)
        Btn_beforelogin=Button(Frame_beforelogin,cursor='hand2',command=self.Login_page_draw,text='Login',fg=YELLOW_O,bg=BLACK,font=("times new roman",20)).place(x=0,y=0,height=40,width=200)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        #======Login/Register Page Layout Draw==========================================================================================================================================
    def Login_page_draw(self):

        #===Delete previous widgets===
        self.clear_workframe()
        
        #==Register Counter Layout Draw==================================================================================================================================================
        Frame_register=Frame(self.Frame_work,bg=WHITE)
        Frame_register.place(x=10,y=2,height=400,width=315)

        lbl_register=Label(Frame_register,text='Register: ',font=("times new roman",20,'bold'),bg=WHITE,fg=BLACK).place(x=10,y=10,height=40,width=120)
        lbl_Remail=Label(Frame_register,text='E-mail ID',font=("Goudy old style",12),bg=WHITE,fg=BLACK).place(x=0,y=60,height=20,width=100)

        self.txt_Remail=Entry(Frame_register,font=("times new roman",12),bg='lightgray')
        self.txt_Remail.place(x=10,y=100,height=20,width=300)

        lbl_Rusername=Label(Frame_register,text='Username',font=("Goudy old style",12),bg=WHITE,fg=BLACK).place(x=0,y=130,height=20,width=100)
        self.txt_Rusername=Entry(Frame_register,font=("times new roman",12),bg='lightgray')
        self.txt_Rusername.place(x=10,y=160,height=20,width=300)

        lbl_Rpassword=Label(Frame_register,text='Password',font=("Goudy old style",12),bg=WHITE,fg=BLACK).place(x=0,y=190,height=20,width=100)
        self.txt_Rpassword=Entry(Frame_register,show="*",font=("times new roman",12),bg='lightgray')
        self.txt_Rpassword.place(x=10,y=220,height=20,width=300)

        Btn_register=Button(Frame_register,command=self.Register_function,cursor="hand2",text='Register',bg='red',fg=WHITE,font=('times new roman',20)).place(x=10,y=270,height=40,width=100)

        #==Login Counter Layout Draw====================================================================================================================================================
        Frame_login=Frame(self.Frame_work,bg=WHITE)
        Frame_login.place(x=330,y=2,height=400,width=315)

        lbl_login=Label(Frame_login,text='Login: ',font=("times new roman",20,'bold'),bg=WHITE,fg=BLACK).place(x=0,y=10,height=40,width=120)
        lbl_username=Label(Frame_login,text='Username',font=("Goudy old style",18),bg=WHITE,fg=BLACK).place(x=0,y=80,height=40,width=120)

        self.txt_username=Entry(Frame_login,textvariable=self.username_var,font=("times new roman",18),bg='lightgray')
        self.txt_username.place(x=10,y=120,height=40,width=300)
        

        lbl_password=Label(Frame_login,text='Password',font=("Goudy old style",18),bg=WHITE,fg=BLACK).place(x=0,y=170,height=40,width=100)
        self.txt_password=Entry(Frame_login,show="*",font=("times new roman",18),bg='lightgray')
        self.txt_password.place(x=10,y=210,height=40,width=300)

        Btn_login=Button(Frame_login,command=self.Login_function,cursor="hand2",text='Login',bg='red',fg=WHITE,font=('times new roman',20)).place(x=10,y=270,height=40,width=100)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #=====Creating/Updating Userlist======================================================================================================================================================
    def Userlist_Add(self):
        self.customer[self.txt_Rusername.get()]=[self.txt_Rusername.get(),self.txt_Rpassword.get(),self.txt_Remail.get()]
        self.customerOrder[self.txt_Rusername.get()]=[self.txt_Rusername.get()]

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
        
    #=====Adding functionality==============================================================================================================================================================
##Function to add functionality to Login button.
##Checks for input fields error.
##Calling of home page of customer or Admin
##depending upon the Login username.

    def Login_function(self):
        self.tu=self.username_var.get()
        print(self.tu)
        
        if self.txt_password.get()=="" or self.txt_username.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
            print(1)
            self.Login_page_draw()
            
        elif (self.txt_username.get() in self.customer) and (self.txt_password.get()!= self.customer[self.txt_username.get()][1]) :
            messagebox.showerror("Error","Invalid Username/Password",parent=self.root)
            print(2)
            self.Login_page_draw()
        elif (self.txt_username.get() not in self.customer) :
            messagebox.showerror("Error","Invalid Username/Password",parent=self.root)
            print(2)
            self.Login_page_draw()
        elif (self.txt_username.get() in self.customer) and (self.txt_password.get()== self.customer[self.txt_username.get()][1]):
            messagebox.showinfo("Welcome",f"Welcome{self.txt_username.get()}")
            if self.txt_username.get()=="Admin":
                self.HomeA_page()
            else:
                self.HomeC_page()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #======Adding Functionality to Register===============================================================================================================================================

            

    def Register_function(self):
        if self.txt_Rpassword.get()=="" or self.txt_Rusername.get()=="" or self.txt_Remail.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
            self.Login_page_draw()
            print(1)
        elif self.txt_Rusername.get() in self.customer:
            messagebox.showerror("Error","Already has an account",parent=self.root)
            self.Login_page_draw()
            print(2)
            
        else:
            messagebox.showinfo("Welcome",f"Welcome{self.txt_Rusername.get()} \n PLease Login again")
            self.Userlist_Add()
            self.Login_page_draw()
            print(self.customerOrder)
            print(3)
            print(self.customer)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

###########################################################################################################################################################################################

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #======Customer Functions Defintions===================================================================================================================================================

    #======Home Page of Customer===========================================================================================================================================================
    def HomeC_page(self):
        self.MonDraw_menu()
        self.Afterlogin_page()
        
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #======Dashboard of Customer Layout Draw===============================================================================================================================================
    def DashboardC_draw(self):
        self.clear_workframe()

        Frame_displayuser=Frame(self.Frame_work,bg=YELLOW_O)
        Frame_displayuser.place(x=20,y=0,height=40,width=600)
        lbl_displayuser=Label(Frame_displayuser,text=self.customer[self.tu][0],font=('times new roman',12),bg=YELLOW_O,fg=BLACK).place(x=0,y=0,height=40,width=130)

        Frame_displayemail=Frame(self.Frame_work,bg=YELLOW_O)
        Frame_displayemail.place(x=20,y=50,height=40,width=600)
        lbl_displayemail=Label(Frame_displayemail,text=self.customer[self.tu][2],font=('times new roman',12),bg=YELLOW_O,fg=BLACK).place(x=0,y=0,height=40,width=150)

        Frame_logout=Frame(self.Frame_work,bg=YELLOW_O)
        Frame_logout.place(x=20,y=100,height=40,width=600)
        Btn_logout=Button(Frame_logout,cursor='hand2',command=self.Home_page,text='Logout',bg=WHITE,fg=BLACK,font=('times new roman',12)).place(x=10,y=5,height=30,width=150)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #=======Orders Page of Customer Layout Draw===========================================================================================================================================
    def OrdersC_draw(self):
        self.clear_workframe()

        #=======Order Display List==========================================================================================================================================================
        self.Ctv=ttk.Treeview(self.Frame_work)
        self.Ctv['columns']=('ID','Username','Itemname','Qty','Cost','Status')
        self.Ctv.column('#0',width=0,stretch=NO)
        self.Ctv.column('ID',anchor=CENTER,width=50)
        self.Ctv.column('Username',anchor=CENTER,width=140)
        self.Ctv.column('Itemname',anchor=CENTER,width=140)
        self.Ctv.column('Qty',anchor=CENTER,width=90)
        self.Ctv.column('Cost',anchor=CENTER,width=100)
        self.Ctv.column('Status',anchor=CENTER,width=100)

        self.Ctv.heading('#0',text='',anchor=CENTER)
        self.Ctv.heading('ID',text='ID',anchor=CENTER)
        self.Ctv.heading('Username',text='Username',anchor=CENTER)
        self.Ctv.heading('Itemname',text='Itemname',anchor=CENTER)
        self.Ctv.heading('Qty',text='Qty',anchor=CENTER)
        self.Ctv.heading('Cost',text='Cost',anchor=CENTER)
        self.Ctv.heading('Status',text='Status',anchor=CENTER)
        self.Ctv.pack()

        for item in self.orderListC:
            if item[1]==self.tu:
                self.countA1+=1
                self.Ctv.insert(parent='',index='end',iid=self.countA1,text='',values=item)
                self.Ctv.pack()
        




        #=============Customer Order Counter Draw=========================================================================================================================================================
        lbl_order=Label(self.Frame_work,text='Enter details to Order Item here:',font=('times new roman',12),bg=YELLOW_O,fg=BLACK).place(x=0,y=290,height=20,width=660)
        
        Frame_id=Frame(self.Frame_work,bg=WHITE)
        Frame_id.place(x=0,y=320,height=80,width=100)
        lbl_id=Label(Frame_id,text='ID here:',font=('times new roman',12),bg=YELLOW_O,fg=BLACK).place(x=0,y=0,height=20,width=100)
        self.txt_id=Entry(Frame_id,textvariable=self.id_var,font=("times new roman",18),bg='lightgray')
        self.txt_id.place(x=30,y=35,height=30,width=50)
        
        Frame_itemname=Frame(self.Frame_work,bg=WHITE)
        Frame_itemname.place(x=102,y=320,height=80,width=200)
        lbl_itemname=Label(Frame_itemname,text='Itemname:',font=('times new roman',12),bg=YELLOW_O,fg=BLACK).place(x=0,y=0,height=20,width=200)

        Frame_qty=Frame(self.Frame_work,bg=WHITE)
        Frame_qty.place(x=304,y=320,height=80,width=100)
        lbl_qty=Label(Frame_qty,text='Qty:',font=('times new roman',12),bg=YELLOW_O,fg=BLACK).place(x=0,y=0,height=20,width=100)

        Frame_cost=Frame(self.Frame_work,bg=WHITE)
        Frame_cost.place(x=406,y=320,height=80,width=100)
        lbl_cost=Label(Frame_cost,text='Cost:',font=('times new roman',12),bg=YELLOW_O,fg=BLACK).place(x=0,y=0,height=20,width=100)

        Frame_status=Frame(self.Frame_work,bg=WHITE)
        Frame_status.place(x=508,y=320,height=80,width=145)
        lbl_statushead=Label(Frame_status,text='Status:',font=('times new roman',12),bg=YELLOW_O,fg=BLACK).place(x=0,y=0,height=20,width=145)

        lbl_disitemname=Label(Frame_itemname,textvariable=self.itemname,font=('times new roman',12),bg=WHITE,fg=BLACK).place(x=0,y=35,height=30,width=140)
        self.txt_disqty=Entry(Frame_qty,textvariable=self.qty,font=('times new roman',12),bg='lightgrey',fg=BLACK).place(x=30,y=35,height=30,width=40)
        lbl_discost=Label(Frame_cost,textvariable=self.cost,font=('times new roman',12),bg=WHITE,fg=BLACK).place(x=0,y=35,height=30,width=140)

        
        self.status.set('Click To order')
        lbl_status=Label(Frame_status,textvariable=self.status,font=('times new roman',12),bg=WHITE,fg=BLACK).place(x=0,y=27,height=30,width=140)
    
        Btn_submit=Button(Frame_status,cursor='hand2',command=self.Display_statusC,text='Order',bg=WHITE,fg=BLACK,font=('times new roman',10)).place(x=20,y=50,height=30,width=100)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#============Adding Functionality to submit button of order counter=========================================================================================================================

##Checking of Input field errors.
##Adding to the Orderlist.
##Adding items to the Display.
##Sending info to the Admin.

    def Display_statusC(self):
        if (self.id_var.get() != '') and (self.qty.get() != ''):
            self.ordersubListC=[]
            self.status.set('Preparing')
            self.status1='Preparing'
            self.disid=self.id_var.get()
            
            self.disqty=self.qty.get()
            self.send_username=self.username_var.get()
            
            for i in range(len(self.items)):
                if self.items[i][4]==self.disid:
                    
                    self.itemname.set(self.items[i][1])
                    self.cost1=int(self.disqty)*int(self.items[i][2])
                    self.cost.set(str(self.cost1))
                    self.customerOrder[self.tu].append(self.disid)
                    #self.ordersubListC.clear()
                    self.row=(self.items[i][4],self.send_username,self.items[i][1],self.disqty,self.cost1,self.status1)
                    self.ordersubListC.append(self.row)
                    self.orderListC.append(self.row)

            self.OrdersC_draw()

        else:
            messagebox.showerror('Error','All fields are required!',parent=self.root)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
###########################################################################################################################################################################################
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def MonDraw_menu(self):
        self.Draw_menu()
        for i in range(len(self.items)):
            if self.items[i][5]=='Monday':
                self.tv.insert(parent='',index=i,iid=i,text='',values=(self.items[i][4],self.items[i][1],self.items[i][2],self.items[i][3],self.items[i][0]))
                self.tv.pack()

    def TueDraw_menu(self):
        self.Draw_menu()
        for i in range(len(self.items)):
            if self.items[i][5]=='Tuesday':
                self.tv.insert(parent='',index=i,iid=i,text='',values=(self.items[i][4],self.items[i][1],self.items[i][2],self.items[i][3],self.items[i][0]))
                self.tv.pack()

    

    def WedDraw_menu(self):
        self.Draw_menu()
        for i in range(len(self.items)):
            if self.items[i][5]=='Wednesday':
                self.tv.insert(parent='',index=i,iid=i,text='',values=(self.items[i][4],self.items[i][1],self.items[i][2],self.items[i][3],self.items[i][0]))
                self.tv.pack()

    

    def ThuDraw_menu(self):
        self.Draw_menu()
        for i in range(len(self.items)):
            if self.items[i][5]=='Thursday':
                self.tv.insert(parent='',index=i,iid=i,text='',values=(self.items[i][4],self.items[i][1],self.items[i][2],self.items[i][3],self.items[i][0]))
                self.tv.pack()

    

    def FriDraw_menu(self):
        self.Draw_menu()
        for i in range(len(self.items)):
            if self.items[i][5]=='Friday':
                self.tv.insert(parent='',index=i,iid=i,text='',values=(self.items[i][4],self.items[i][1],self.items[i][2],self.items[i][3],self.items[i][0]))
                self.tv.pack()

    

    def SatDraw_menu(self):
        self.Draw_menu()
        for i in range(len(self.items)):
            if self.items[i][5]=='Saturday':
                self.tv.insert(parent='',index=i,iid=i,text='',values=(self.items[i][4],self.items[i][1],self.items[i][2],self.items[i][3],self.items[i][0]))
                self.tv.pack()

    

    def SunDraw_menu(self):
        self.Draw_menu()
        for i in range(len(self.items)):
            if self.items[i][5]=='Sunday':
                self.tv.insert(parent='',index=i,iid=i,text='',values=(self.items[i][4],self.items[i][1],self.items[i][2],self.items[i][3],self.items[i][0]))
                self.tv.pack()

    


            
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

############################################################################################################################################################################################

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#===========================================================================================================================================================================================
#==========================Values===========================================================================================================================================================
#==========================================================================================================================================================================================
items=[['breakfast','Poha','100','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent nec. ','1','Monday'],
       ['breakfast','Pao Bhaji','300','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent nec. ','2','Monday'],
       ['lunch','Chana Kulcha','500','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent nec. ','3','Monday'],
       ['lunch','Masala Bhindi','400','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent nec. ','4','Tuesday'],
       ['lunch','Dal Makhni','460','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent nec. ','5','Tuesday'],
       ['dinner','Dum Aloo','350','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent nec. ','6','Tuesday'],
       ['dinner','Lemon Chicken','700','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent nec. ','7','Wednesday'],
       ['breakfast','Poha','100','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent nec. ','8','Wednesday'],
       ['breakfast','Pao Bhaji','300','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent nec. ','9','Wednesday'],
       ['lunch','Chana Kulcha','500','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent nec. ','10','Thursday'],
       ['lunch','Masala Bhindi','400','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent nec. ','11','Thursday'],
       ['lunch','Dal Makhni','460','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent nec. ','12','Thursday'],
       ['dinner','Dum Aloo','350','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent nec. ','13','Friday'],
       ['dinner','Lemon Chicken','700','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent nec. ','14','Friday'],
       ['breakfast','Poha','100','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent nec. ','15','Friday'],
       ['breakfast','Pao Bhaji','300','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent nec. ','16','Saturday'],
       ['lunch','Chana Kulcha','500','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent nec. ','17','Saturday'],
       ['lunch','Masala Bhindi','400','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent nec. ','18','Saturday'],
       ['lunch','Dal Makhni','460','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent nec. ','19','Sunday'],
       ['dinner','Dum Aloo','350','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent nec. ','20','Sunday'],
       ['dinner','Lemon Chicken','700','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent nec. ','21','Sunday'],
       ['breakfast','Dosa','100','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent nec. ','22','Monday'],
       ['breakfast','Veg Kolhapuri','300','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent nec. ','23','Tuesday'],
       ['lunch','Chana Bhatura','500','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent nec. ','24','Wednesday'],
       ['lunch','Masala Veg','400','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent nec. ','25','Thursday'],
       ['lunch','Dal Fry','460','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent nec. ','26','Friday'],
       ['dinner','Dum Biryani','350','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent nec. ','27','Saturday'],
       ['dinner','Chicken 65','700','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent nec. ','28','Sunday'],
       ['breakfast','Dosa','100','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent nec. ','29','Tuesday'],
       ['breakfast','Veg Kolhapuri','300','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent nec. ','30','Wednesday'],
       ['lunch','Chana Bhatura','500','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent nec. ','31','Friday'],
       ['lunch','Masala Veg','400','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent nec. ','32','Monday'],
       ['lunch','Dal Fry','460','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent nec. ','33','Sunday'],
       ['dinner','Dum Biryani','350','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent nec. ','34','Thursday'],
       ['dinner','Chicken 65','700','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent nec. ','35','Saturday']
       ]
customer={'Admin':['Admin','123456','admin@xyz.com'],
                       'User1':['User1','User1234','user1@xyz.com'],
                       'User2':['User2','User234','user2@xyz.com'],
                       'User3':['User3','User34','user3@xyz.com']}

customerOrder={'User1':['User1'],'User2':['User2']}




root=Tk()

obj=afterLogin(root,items,customer,customerOrder)
root.mainloop()
