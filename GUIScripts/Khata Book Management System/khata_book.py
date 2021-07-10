# Including required modules

import mysql.connector
from tkinter import * 
import speech_recognition as sr
import pyttsx3 

# assigining the voice commands 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

# function to speak 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
# making the connections towards the mysql 
def connection():
    try:
        con=mysql.connector.connect(user='root',password='4844',host='127.0.0.1',database='kbook')
        mycursor=con.cursor()
        #creating the servers
        mycursor.execute("CREATE TABLE IF NOT EXIST ITEMS (CID INT PRIMARY KEY,COUSTOMER_NAME VARCHAR(25),ITEM1 VARCHAR(20),WORTH1 INT,ITEM2 VARCHAR(20),WORTH2 INT,TOTAL_AMOUNT INT)")
    except:
        print("cannot Connect to database")
    return con
   
 
# function to search records in mysql tables
def Search_Records():
    con=connection()
    cursor=con.cursor()
    CID=e1.get()
    query=("select * from items where CID=%s")  #executive the querry 
    data=(CID,)
    cursor.execute(query,data)
    dasd = cursor.fetchall()
    for x in dasd:
        t1.insert(END,str(x)+"\n")
        speak("Record Found")



 # function to Insert records in mysql tables   
def Insert_Records():
    con=connection()
    cursor=con.cursor()
    CID=e1.get()
    Coustomer_Name=e2.get()
    Item1=e3.get()
    worth1=int(e4.get())
    Item2=e5.get()
    worth2=int(e6.get())
    total_amount=worth1+worth2
    query=("insert into items values(%s,%s,%s,%s,%s,%s,%s)")
    data=(CID,Coustomer_Name,Item1,worth1,Item2,worth2,total_amount)
    cursor.execute(query,data)
    cursor.close()
    t1.insert(END,"ADDED SUCCESSFULLY\n")
    speak("Record Inserted")
    con.commit()
    con.close()

# function to show all  records in mysql tables
def show_money():
    con=connection()
    cur=con.cursor()
    query=("select Coustomer_Name,total_amount from items ")
    cur.execute(query,)
    y=cur.fetchall()
    for x in y:
        t1.insert(END,str(x)+"\n")

    speak(query)
    cur.close()
    con.commit()
    con.close()
    
#Function To delete the records
def delete():
    con=connection()
    cur=con.cursor()
    CID=e1.get()
    query=("delete from items where CID=%s")
    data=(CID,)
    cur.execute(query,data)
    speak("Record Deleted")
    con.commit()
    cur.close()
    con.close()
    t1.insert(END,"Record Deleted \n")
    
    

    

def close():
    sys.exit()

#Starting the UI Work........


root=Tk()
root.title("KHATA BOOK SOFT")
#decalring the variables...
CID=StringVar()
Customer_Name=StringVar()
Item1=StringVar()
worth1=StringVar()
Item2=StringVar()
worth2=StringVar()

#making the labels for fields in UI...........

label1=Label(root,text="Customer ID",font="arial 10 bold")
label1.place(x=0,y=0)

label12=Label(root,text="Customer_Name",font="arial 10 bold")
label12.place(x=0,y=30)

label13=Label(root,text="ITEM1",font="arial 10 bold")
label13.place(x=0,y=60)

label14=Label(root,text="worth1",font="arial 10 bold")
label14.place(x=0,y=90)

label15=Label(root,text="ITEM2",font="arial 10 bold ")
label15.place(x=0,y=120)

label16=Label(root,text="worth2",font="arial 10 bold")
label16.place(x=0,y=150)

# MAking th entry field .........
e1=Entry(root,textvariable=CID,bg="lightblue")
e1.place(x=120,y=0)

e2=Entry(root,textvariable=Customer_Name,bg="lightblue")
e2.place(x=120,y=30)

e3=Entry(root,textvariable=Item1,bg="lightblue")
e3.place(x=120,y=60)

e4=Entry(root,textvariable=worth1,bg="lightblue")
e4.place(x=120,y=90)

e5=Entry(root,textvariable=Item2,bg="lightblue")
e5.place(x=120,y=120)

e6=Entry(root,textvariable=worth2,bg="lightblue")
e6.place(x=120,y=150)


# OUTPUT AREA....................
t1=Text(root,width=80,height=20,bg="green",font="arial 10 bold")
t1.grid(row=9,column=1)

#Buttons That Triggers the Functions............

b1=Button(root,text="Seacrch CUSTOMER",command=Search_Records,width=40,bg="orange",font="arial 10 bold")
b1.grid(row=11,column=0)

b2=Button(root,text="INSERT_RECORDS",command=Insert_Records,width=40,bg="pink",font="arial 10 bold")
b2.grid(row=12,column=0)

b3=Button(root,text="CLOSE",command=close,width=40,bg="Yellow",font="arial 10 bold")
b3.grid(row=14,column=0)

b4=Button(root,text="SHOW ALL REAMAING MONEY",command=show_money,width=40,bg="pink",font="arial 10 bold")
b4.grid(row=10,column=0)

b5=Button(root,text="DELETE RECORDS",command=delete,width=40,bg="orange",font="arial 10 bold")
b5.grid(row=13,column=0)




root.mainloop()
    
