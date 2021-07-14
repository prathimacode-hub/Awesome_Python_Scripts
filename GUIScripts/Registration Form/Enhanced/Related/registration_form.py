#!/usr/bin/env python
# coding: utf-8

# # SET-3
# ### Database connectivity using sqlite3 for for Form creation
# **DONE BY:
# <br>Thejaswin.S
# <br>RA1911026010029
# <br>CSE-AIML K1**

# ### Image of form

# In[3]:


from IPython.display import Image
Image(filename='../Images/2.png') 


# ### After pressing submit button user will get notified whether response is saved successfully or not

# In[16]:


from IPython.display import Image
Image(filename='../Images/msgbox.png') 


# ### After submit button is pressed the form is reset for next response submission

# In[4]:


from IPython.display import Image
Image(filename='./Images/1.png') 


# ### The data entered in form is stored in Database in theja.db file

# In[19]:


from IPython.display import Image
Image(filename='../Images/sql.png') 


# In[1]:



#from openpyxl import *        
from tkinter import *
from tkinter import messagebox 
import sqlite3
my_conn = sqlite3.connect('theja.db')
print("Connected to database successfully")
0
def deleteall0029():
    name_entry.delete(0,END)
    name_entry.insert(0,"ENTER PLATE NUM")
    name_entry01.delete(0,END)
    name_entry1.delete(0,END)
    name_entry3.delete(0,END)
    name_entry4.delete(0,END)
    name_entry5.delete(0,END)
    name_entry6.delete(0,END)
    name_entry7.delete(0,END)
    name_entry8.delete(0,END)
    name_entry9.delete(0,END)
    name_entry10.delete(0,END)
    name_entry11.delete(0,END)
    name_entry12.delete(0,END)
    name_entry13.delete(0,END)
    name_entry14.delete(0,END)
    name_entry15.delete(0,END)
    name_entry16.delete(0,END)
    name_entry17.delete(0,END)
    name_entry018.delete(0,END)
    name_entry18.delete(0,END)
    name_entry19.delete(0,END)
    name_entry20.delete(0,END)
    name_entry21.delete(0,END)
    name_entry22.delete(0,END)
    name_entry23.delete(0,END)
    name_entry24.delete(0,END)
    messagebox.showinfo("showinfo", "Response is saved successfully")
       
def disp0029():
    my_w = Tk()
    my_w.geometry("1500x500") 
    my_w.title('car')
    r_set=my_conn.execute('''SELECT * from student LIMIT 0,10''');
    i=0 # row value inside the loop 
    for student in r_set: 
        for j in range(len(student)):
            e = Entry(my_w, width=9, fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, student[j])
        i=i+1  
    my_w.mainloop()

root0029=Tk()
root0029.geometry('910x640')
root0029.title("Digital Form")
root0029.configure(bg='white')
reg_info = Label(root0029,text = "REGISTRATION INFORMATION",width='910',font= ("ariel",11,"bold"),fg = "black",bg='lightgrey')
reg_info.place(x=470,y=12,anchor='center')
reg_period=Label(root0029,text="Registration Period: ",font=("ariel",11,"bold"),bg='white')
reg_period.place(x=0,y=25)

list0029 = ['One Year','Two Years', 'Three Years']
c = StringVar(root0029)
c.set('Select One')
droplist0029 = OptionMenu(root0029,c,*list0029)
droplist0029.config(width = 20)
droplist0029.place(x =240,y=25)
lab1=Label(root0029,text="(not available for vehicles subject to emissions testing)",font=("ariel",8,"bold"),bg='white')
lab1.place(x=595,y=45)

reg_period=Label(root0029,text="Registration Type: ",font=("ariel",11,"bold"),bg='white')
reg_period.place(x=0,y=60)
reg_period=Label(root0029,text="(check one)",font=("ariel",9),bg='white')
reg_period.place(x=135,y=60)
list00291 = ['Original','Renewal', 'Private','Reissue (plates and decals)','Reissue (Decals Only)','Rental vehicle','Ridesharing(Vanpool)']
d = StringVar(root0029)
d.set('Select ')
droplist0029 = OptionMenu(root0029,d,*list00291)
droplist0029.config(width = 25)
droplist0029.place(x =240,y=60)

label0001=Label(root0029,text='Transfer license plate number: ', font=('calibre',9,'normal'), bg='white')
label0001.place(x=0,y=90)
name_var=StringVar()
name=name_var.get()
name_entry = Entry(root0029,width='15',textvariable = name_var, font=('calibre',9,'normal'),bg='lightblue')
name_entry.insert(0,"ENTER PLATE NUM")
name_entry.place(x=200,y=95)
def clear_search0029(event):
    name_entry.delete(0, END)
name_entry.bind("<Button-1>", clear_search0029)
label111=Label(root0029,text='(Cannot exceed 16 passengers including driver)  Seating capacity',font=('calibre',9,'normal'), bg='white')
label111.place(x=0,y=120)
seat_var=StringVar()
seat=seat_var.get()
name_entry01 = Entry(root0029,width='5',textvariable = seat_var, font=('calibre',10,'normal'),bg='lightblue')
name_entry01.place(x=400,y=120)
v13=IntVar()
v14=IntVar()
label0002=Label(root0029,text='Amateur Radio Operator call letters- Specify letters:', font=('calibre',9,'normal'), bg='white')
label0002.place(x=0,y=150)
ama=StringVar()
amateur=ama.get()
name_entry1 = Entry(root0029,width='10',textvariable = ama, font=('calibre',10,'normal'),bg='lightblue')
name_entry1.place(x=300,y=150)
def clear_search0029(event):
    name_entry2.delete(0, END)
reg_info = Label(root0029,text = "OWNER INFORMATION",width='910',font= ("ariel",11,"bold"),fg = "black",bg='lightgrey')
reg_info.place(x=470,y=200,anchor='center')
v15=IntVar()
v16=IntVar()
owner=Label(root0029,text="OWNER'S FULL LEGAL NAME OR BUSINESS NAME:",font=("ariel",9),bg='white')
owner.place(x=0,y=215)
name_var3=StringVar()
name3=name_var3.get()
name_entry3 = Entry(root0029,width='20',textvariable = name_var3, font=('calibre',9,'normal'),bg='lightblue')
name_entry3.place(x=295,y=215)

number=Label(root0029,text="TELEPHONE NUMBER:",font=("ariel",9),bg='white')
number.place(x=430,y=215)
name_var4=StringVar()
name4=name_var4.get()
name_entry4 = Entry(root0029,width='10',textvariable = name_var4, font=('calibre',9,'normal'),bg='lightblue')
name_entry4.place(x=570,y=215)

dmv=Label(root0029,text="DMV CUSTOMER NUMBER/FEIN/SSN",font=("ariel",9),bg='white')
dmv.place(x=670,y=215)
name_var5=StringVar()
name5=name_var5.get()
name_entry5 = Entry(root0029,width='30',textvariable = name_var5, font=('calibre',9,'normal'),bg='lightblue')
name_entry5.place(x=670,y=235)

coowner=Label(root0029,text="CO OWNER'S FULL LEGAL NAME:",font=("ariel",9),bg='white')
coowner.place(x=0,y=260)
name_var6=StringVar()
name6=name_var6.get()
name_entry6 = Entry(root0029,width='35',textvariable = name_var6, font=('calibre',9,'normal'),bg='lightblue')
name_entry6.place(x=200,y=260)

number1=Label(root0029,text="TELEPHONE NUMBER:",font=("ariel",9),bg='white')
number1.place(x=430,y=260)
name_var7=StringVar()
name7=name_var7.get()
name_entry7 = Entry(root0029,width='10',textvariable = name_var7, font=('calibre',9,'normal'),bg='lightblue')
name_entry7.place(x=570,y=260)

dmv1=Label(root0029,text="DMV CUSTOMER NUMBER/FEIN/SSN",font=("ariel",9),bg='white')
dmv1.place(x=670,y=260)
name_var8=StringVar()
name8=name_var8.get()
name_entry8 = Entry(root0029,width='30',textvariable = name_var8, font=('calibre',9,'normal'),bg='lightblue')
name_entry8.place(x=670,y=280)

resi=Label(root0029,text="RESIDENCE/BUSINESS JURISDICTION",font=("ariel",9),bg='white')
resi.place(x=670,y=300)
name_var9=StringVar()
name9=name_var9.get()
name_entry9 = Entry(root0029,width='30',textvariable = name_var9, font=('calibre',9,'normal'),bg='lightblue')
name_entry9.place(x=670,y=320)

note=Label(root0029,text="NOTE: owners must provide their residence/home/business address where requested, this address",font=("ariel",9),bg='white')
note.place(x=0,y=300)
note1=Label(root0029,text="cannot be a P.O. box . You must complete your ISD-01 if you would like your address updated.",font=("ariel",9),bg='white')
note1.place(x=0,y=315)

resi1=Label(root0029,text="OWNER'S RESIDENCE/HOME/BUSINESS ADDRESS:",font=("ariel",9),bg='white')
resi1.place(x=0,y=350)
name_var10=StringVar()
name10=name_var10.get()
name_entry10 = Entry(root0029,width='45',textvariable = name_var10, font=('calibre',9,'normal'),bg='lightblue')
name_entry10.place(x=0,y=370)

city=Label(root0029,text="CITY:",font=("ariel",9),bg='white')
city.place(x=370,y=350)
name_var11=StringVar()
name11=name_var11.get()
name_entry11 = Entry(root0029,width='15',textvariable = name_var11, font=('calibre',9,'normal'),bg='lightblue')
name_entry11.place(x=410,y=350)

state=Label(root0029,text="STATE:",font=("ariel",9),bg='white')
state.place(x=530,y=350)
name_var12=StringVar()
name12=name_var12.get()
name_entry12 = Entry(root0029,width='15',textvariable = name_var12, font=('calibre',9,'normal'),bg='lightblue')
name_entry12.place(x=580,y=350)

zipc=Label(root0029,text="ZIP CODE:",font=("ariel",9),bg='white')
zipc.place(x=715,y=350)
name_var13=StringVar()
name13=name_var13.get()
name_entry13 = Entry(root0029,width='7',textvariable = name_var13, font=('calibre',9,'normal'),bg='lightblue')
name_entry13.place(x=780,y=350)

resi2=Label(root0029,text="CO OWNER'S RESIDENCE/HOME/BUSINESS ADDRESS:",font=("ariel",9),bg='white')
resi2.place(x=0,y=390)
name_var14=StringVar()
name14=name_var14.get()
name_entry14 = Entry(root0029,width='45',textvariable = name_var14, font=('calibre',9,'normal'),bg='lightblue')
name_entry14.place(x=0,y=410)

city=Label(root0029,text="CITY:",font=("ariel",9),bg='white')
city.place(x=370,y=390)
name_var15=StringVar()
name15=name_var15.get()
name_entry15 = Entry(root0029,width='15',textvariable = name_var15, font=('calibre',9,'normal'),bg='lightblue')
name_entry15.place(x=410,y=390)

state=Label(root0029,text="STATE:",font=("ariel",9),bg='white')
state.place(x=530,y=390)
name_var16=StringVar()
name16=name_var16.get()
name_entry16 = Entry(root0029,width='15',textvariable = name_var16, font=('calibre',9,'normal'),bg='lightblue')
name_entry16.place(x=580,y=390)

zipc=Label(root0029,text="ZIP CODE:",font=("ariel",9),bg='white')
zipc.place(x=715,y=390)
name_var17=StringVar()
name17=name_var17.get()
name_entry17 = Entry(root0029,width='7',textvariable = name_var17, font=('calibre',9,'normal'),bg='lightblue')
name_entry17.place(x=780,y=390)

owe=Label(root0029,text="OWNER EMAIL ADDRESS:",font=("ariel",9),bg='white')
owe.place(x=0,y=435)
name_var018=StringVar()
name018=name_var018.get()
name_entry018 = Entry(root0029,width='30',textvariable = name_var018, font=('calibre',9,'normal'),bg='lightblue')
name_entry018.place(x=160,y=435)

owe=Label(root0029,text="CO-OWNER EMAIL ADDRESS:",font=("ariel",9),bg='white')
owe.place(x=420,y=435)
name_var18=StringVar()
name18=name_var18.get()
name_entry18 = Entry(root0029,width='30',textvariable = name_var18, font=('calibre',9,'normal'),bg='lightblue')
name_entry18.place(x=600,y=435)

add_info = Label(root0029,text = "REGISTRATION INFORMATION",width='910',font= ("ariel",11,"bold"),fg = "black",bg='lightgrey')
add_info.place(x=470,y=475,anchor='center')

owe=Label(root0029,text="LOCATION WHERE VEHICLE IS PRINCIPALLY GARAGED:",font=("ariel",9),bg='white')
owe.place(x=0,y=490)
Label00=Label(root0029,text='CITY/COUNTRY/TOWN OF',font=("ariel",9),bg='white' )
Label00.place(x=0,y=510)
name_var19=StringVar()
name19=name_var19.get()
name_entry19 = Entry(root0029,width='15',textvariable = name_var19, font=('calibre',9,'normal'),bg='lightblue')
name_entry19.place(x=175,y=512)
loc=Label(root0029,text="IF NEW LOCATION ENTER DATE CHANGED:",font=("ariel",9),bg='white')
loc.place(x=360,y=490)
name_var20=StringVar()
name20=name_var20.get()
name_entry20 = Entry(root0029,width='15',textvariable = name_var20, font=('calibre',9,'normal'),bg='lightblue')
name_entry20.place(x=500,y=512)
ser=Label(root0029,text="Are any of the owners/lessees on active",font=("ariel",9),bg='white')
ser.place(x=660,y=490)
ser1=Label(root0029,text="military duty or services?",font=("ariel",9),bg='white')
ser1.place(x=660,y=510)
v20=IntVar()
v21=IntVar()
v22=IntVar()

radio_v = StringVar()
radio_v.set('No')
r1 = Radiobutton(root0029, text='yes', variable=radio_v, value='Yes')
r1.place(x=800,y=510)

r2 = Radiobutton(root0029, text='no', variable=radio_v, value='No')
r2.place(x=850,y=510)
ene=Label(root0029,text="IF YOU WOULD LIKE YOUR REGISTRATION RENEWALS SENT TO AN ADDRESS OTHER THAN YOUR RESIDENCE/BUSINESS ADDRESS. ENTER IT BELOW",font=("ariel",9),bg='white')
ene.place(x=0,y=535)
mail=Label(root0029,text="REGISTRATION MAILING ADDRESS-OPTIONAL",font=("ariel",9),bg='white')
mail.place(x=0,y=558)
name_var21=StringVar()
name21=name_var21.get()
name_entry21 = Entry(root0029,width='20',textvariable = name_var21, font=('calibre',9,'normal'),bg='lightblue')
name_entry21.place(x=270,y=558)
cit=Label(root0029,text="CITY",font=("ariel",9),bg='white')
cit.place(x=440,y=558)
name_var22=StringVar()
name22=name_var22.get()
name_entry22 = Entry(root0029,width='12',textvariable = name_var22, font=('calibre',9,'normal'),bg='lightblue')
name_entry22.place(x=475,y=558)

sta=Label(root0029,text="STATE",font=("ariel",9),bg='white')
sta.place(x=590,y=558)
name_var23=StringVar()
name23=name_var23.get()
name_entry23 = Entry(root0029,width='12',textvariable = name_var23, font=('calibre',9,'normal'),bg='lightblue')
name_entry23.place(x=635,y=558)

zi=Label(root0029,text="ZIP CODE",font=("ariel",9),bg='white')
zi.place(x=730,y=558)
name_var24=StringVar()
name24=name_var24.get()
name_entry24 = Entry(root0029,width='8',textvariable = name_var24, font=('calibre',9,'normal'),bg='lightblue')
name_entry24.place(x=795,y=558)

  

def adddata0029():
    flag_validation=True
    regperiod=c.get()
    regtype=d.get()
    platenum=name_entry.get()
    seatcap=name_entry01.get()
    amateur=name_entry1.get()
    oname=name_entry3.get()
    otel=name_entry4.get()
    ossn=name_entry5.get()
    coname=name_entry6.get()
    cotel=name_entry7.get()
    cossn=name_entry8.get()
    resid=name_entry9.get()
    oresid=name_entry10.get()
    ocity=name_entry11.get()
    ostate=name_entry12.get()
    ozip=name_entry13.get()
    coresid=name_entry14.get()
    cocity=name_entry15.get()
    costate=name_entry16.get()
    cozip=name_entry17.get()
    omail=name_entry018.get()
    comail=name_entry18.get()
    cit=name_entry19.get()
    date=name_entry20.get()
    milser=radio_v.get()
    regmail=name_entry21.get()
    city=name_entry22.get()
    state=name_entry23.get()
    zip1=name_entry24.get()
    if(flag_validation):
        my_str.set("Adding data...")
        try:
           
            my_data=(None,regperiod,regtype,platenum,seatcap,amateur,oname,otel,ossn,coname,cotel,cossn,resid,
                     oresid,ocity,ostate,ozip,coresid,cocity,costate,cozip,omail,comail,cit,date,milser,regmail,city,state,zip1)
            my_query="INSERT INTO student values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
            my_conn.execute(my_query,my_data)
            my_conn.commit()
            x=my_conn.execute('''select last_insert_rowid()''')
            id=x.fetchone()
            l5.config(fg='green') # foreground color 
            l5.config(bg='white') # background color 
            my_str.set("ID:" + str(id[0]))       
            deleteall0029()
        except sqlite3.Error as my_error:
            l5.config(fg='red')   # foreground color
            l5.config(bg='yellow') # background color
            print(my_error)
            my_str.set(my_error)        
        
    else:
        #l5.grid() 
        l5.config(fg='red')   # foreground color
        l5.config(bg='yellow') # background color
        my_str.set("check inputs.")
        #l5.after(3000, lambda: l5.grid_remove() )
submit=Button(text="SUBMIT",fg='blue',bg='lightgreen',font=('calibre',13,'bold'),width='10',command=adddata0029)
submit.place(x=300,y=600)
display=Button(text="DISPLAY",fg='blue',bg='lightgreen',font=('calibre',13,'bold'),width='10',command=disp0029)
display.place(x=500,y=600)
my_str = StringVar()
l5 = Label(root0029,textvariable=my_str, width=10 )  
l5.place(x=700,y=105) 
my_str.set("Output")        
root0029.mainloop()
my_conn.close()


# In[17]:


try:
    my_conn.execute('''
        CREATE TABLE IF NOT EXISTS student(id integer primary key, 
                      regperiod varchar(255), 
                      regtype varchar(255),
                      platenum varchar(255),
                      seatcap varchar(255),
                      amateur varchar(255),
                      oname varchar(255),
                      otel varchar(255),
                      ossn varchar(255),
                      coname varchar(255),
                      cotel varchar(255),
                      cossn varchar(255),
                      resid varchar(255),
                      oresid varchar(255),
                      ocity varchar(255),
                      ostate varchar(255),
                      ozip varchar(255),
                      coresid varchar(255),
                      cocity varchar(255),
                      costate varchar(255),
                      cozip varchar(255),
                      omail varchar(255),
                      comail varchar(255),
                      cit varchar(255),
                      date varchar(255),
                      milser varchar(255),
                      regmail varchar(255),
                      city varchar(255),
                      state varchar(255),
                      zip1 varchar(255)
                      );''')
    my_conn.commit()
    print("Table created successfully")
except sqlite3.Error as my_error:
    print("error: ",my_error)


# In[20]:


import sqlite3
my_conn = sqlite3.connect('theja.db')
import tkinter  as tk 
from tkinter import * 
my_w = tk.Tk()
my_w.geometry("1500x500") 
my_w.title('car')
r_set=my_conn.execute('''SELECT * from student LIMIT 0,10''');
i=0 # row value inside the loop 
for student in r_set: 
    for j in range(len(student)):
        e = Entry(my_w, width=9, fg='blue') 
        e.grid(row=i, column=j) 
        e.insert(END, student[j])
    i=i+1  
my_w.mainloop()


# In[132]:





# In[ ]:




