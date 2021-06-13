# Import the following modules.

from tkinter import*
import mysql.connector
from functools import partial

# To connect the Database.

mydb=mysql.connector.connect(
			host="localhost",
			user="root",
			passwd="password",
			database="Name of the Database"
		)

# To insert the data into the Database.

def insert(Date,Earnings,Exercise,Study,Diet,Python):
	var_Date=Date.get()
	var_Earnings=Earnings.get()
	var_Exercise=Exercise.get()
	var_Study=Study.get()
	var_Diet=Diet.get()
	var_Python=Python.get()
	
	mycursor= mydb.cursor()
	mycursor.execute("CREATE TABLE IF NOT EXISTS Routine (id INT AUTO_INCREMENT PRIMARY KEY, Date VARCHAR(255), Earnings VARCHAR(255), Exercise VARCHAR(255), Study VARCHAR(255),Diet VARCHAR(255), Python VARCHAR(255))")
	sql="INSERT INTO Routine (Date,Earnings,Exercise,Study,Diet,Python) VALUES (%s,%s,%s,%s,%s,%s)"
	val=(var_Date,var_Earnings,var_Exercise,var_Study,var_Diet,var_Python)
	myresult=mycursor.execute(sql,val)
	mydb.commit()

	return myresult

# To view all the data in the Listbox.

def view():
	
	mycursor= mydb.cursor()
	mycursor.execute("SELECT * FROM Routine")
	myresult=mycursor.fetchall()
	mydb.commit()
	
	return myresult

# To delete a particular row from the Database.

def delete(id):
	
	mycursor= mydb.cursor()
	sql=("DELETE FROM Routine where id=%s")
	val=(id,)
	mycursor.execute(sql,val)
	mydb.commit()
	return

# To search data based on particular input.

def search(Date='',Earnings='',Exercise='',Study='',Diet='',Python=''):
	var_Date=Date.get()
	var_Earnings=Earnings.get()
	var_Exercise=Exercise.get()
	var_Study=Study.get()
	var_Diet=Diet.get()
	var_Python=Python.get()
	
	mycursor= mydb.cursor()
	sql=("SELECT * FROM Routine where Date=%s or Earnings=%s or Exercise=%s or Study=%s or Diet=%s or Python=%s")
	val=(var_Date,var_Earnings,var_Exercise,var_Study,var_Diet,var_Python)
	mycursor.execute(sql,val)
	myresult=mycursor.fetchall()
	mydb.commit()
	return myresult

def view_command():
	list.delete(0,END)
	for row in view():
		list.insert(END,row)
	return

def search_command():
	list.delete(0,END)
	for row in search():
		list.insert(END,row)
	return

def add_command(Date,Earnings,Exercise,Study,Diet,Python):
	insert(Date,Earnings,Exercise,Study,Diet,Python)
	list.delete(0,END)
	list.insert(END,(Date.get(),Earnings.get(),Exercise.get(),Study.get(),Diet.get(),Python.get()))
	return

def get_selected_row(event):
	global selected_row
	index=list.curselection()[0]
	selected_row=list.get(index)
	return
	

def delete_command():
	delete(selected_row[0])
	return

# Creating Window.

win=Tk()

# Adding title to the Window.

win.title("MY ROUTINE DATABASE SYSTEM")

# Adding Labels.

Date_Label=Label(win,text='Date')
Date_Label.grid(row=0,column=0)
Earnings_Label=Label(win,text='Earnings')
Earnings_Label.grid(row=0,column=2)
Exercise_Label=Label(win,text='Exercise')
Exercise_Label.grid(row=1,column=0)
Study_Label=Label(win,text='Study')
Study_Label.grid(row=1,column=2)
Diet_Label=Label(win,text='Diet')
Diet_Label.grid(row=2,column=0)
Python_Label=Label(win,text='Python')
Python_Label.grid(row=2,column=2)

# Creating Entries for user.

date_text=StringVar()
Date_Entry=Entry(win,textvariable=date_text,bd=3)
Date_Entry.grid(row=0,column=1)

earnings_text=StringVar()
Earnings_Entry=Entry(win,textvariable=earnings_text,bd=3)
Earnings_Entry.grid(row=1,column=1)

exercise_text=StringVar()
Exercise_Entry=Entry(win,textvariable=exercise_text,bd=3)
Exercise_Entry.grid(row=2,column=1)

study_text=StringVar()
Study_Entry=Entry(win,textvariable=study_text,bd=3)
Study_Entry.grid(row=0,column=3)

diet_text=StringVar()
Diet_Entry=Entry(win,textvariable=diet_text,bd=3)
Diet_Entry.grid(row=1,column=3)

python_text=StringVar()
Python_Entry=Entry(win,textvariable=python_text,bd=3)
Python_Entry.grid(row=2,column=3)

l=Label(win)
l.grid(row=3,column=0)

list=Listbox(win,height=8,width=35,bd=5)
list.grid(row=4,column=0,rowspan=9,columnspan=2)

sb=Label(win)
sb.grid(row=4,column=2,rowspan=9)

list.bind('<<ListboxSelect>>',get_selected_row)

add_command=partial(add_command,date_text,earnings_text,exercise_text,study_text,diet_text,python_text)
search=partial(search,date_text,earnings_text,exercise_text,study_text,diet_text,python_text)


# Creating Buttons.

Add_Button=Button(win,text='ADD',width=12,pady=5,command=add_command)
Add_Button.grid(row=4,column=3)
Search_Button=Button(win,text='Search',width=12,pady=5,command=search_command)
Search_Button.grid(row=5,column=3)
Delete_Button=Button(win,text='Delete row',width=12,pady=5,command=delete_command)
Delete_Button.grid(row=6,column=3)
View_Button=Button(win,text='View all',width=12,pady=5,command=view_command)
View_Button.grid(row=7,column=3)
Close_Button=Button(win,text='Close',width=12,pady=5,command=win.destroy)
Close_Button.grid(row=8,column=3)

win.mainloop()