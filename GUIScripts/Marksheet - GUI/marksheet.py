# Import tkinter as tk
import tkinter as tk

#------------------------------------------------------------------------------------------------------------------------------------------------------

# creating a new tkinter window
root = tk.Tk()
root.title("MARKSHEET")  # assigning a title
root.geometry("500x250")   # specifying geometry for window size
root.configure(bg='magenta')

#------------------------------------------------------------------------------------------------------------------------------------------------------

# declaring objects for entering data
e1 = tk.Entry(root)
e2 = tk.Entry(root)
e3 = tk.Entry(root)
e4 = tk.Entry(root)
e5 = tk.Entry(root)
e6 = tk.Entry(root)
e7 = tk.Entry(root)

#------------------------------------------------------------------------------------------------------------------------------------------------------


# function to display the total subject
# credits total credits and SGPA according to grades entered
def display():
	
	# Variable to store total marks
	tot=0
	
	# 10*number of subject credits
	# give total credits for grade A
	if e4.get() == "A":
		
		# grid method is used for placing
		# the widgets at respective positions
		# in table like structure .
		tk.Label(root, text ="40" , bg='magenta').grid(row=3, column=4)
		tot += 40
		
	# 9*number of subject credits give
	# total credits for grade B
	if e4.get() == "B":
		tk.Label(root, text ="36" , bg='magenta').grid(row=3, column=4)
		tot += 36
		
	# 8*number of subject credits give
	# total credits for grade C
	if e4.get() == "C":
		tk.Label(root, text ="32" , bg='magenta').grid(row=3, column=4)
		tot += 32
		
	# 7*number of subject credits
	# give total credits for grade D
	if e4.get() == "D":
		tk.Label(root, text ="28" , bg='magenta').grid(row=3, column=4)
		tot += 28
		
	# 6*number of subject credits give
	# total credits for grade P
	if e4.get() == "P":
		tk.Label(root, text ="24" , bg='magenta').grid(row=3, column=4)
		tot += 24
		
	# 0*number of subject credits give
	# total credits for grade F
	if e4.get() == "F":
		tk.Label(root, text ="0" , bg='magenta').grid(row=3, column=4)
		tot += 0


	# Similarly doing with other objects
	if e5.get() == "A":
		tk.Label(root, text ="40" , bg='magenta').grid(row=4, column=4)
		tot += 40
	if e5.get() == "B":
		tk.Label(root, text ="36" , bg='magenta').grid(row=4, column=4)
		tot += 36
	if e5.get() == "C":
		tk.Label(root, text ="32").grid(row=4, column=4)
		tot += 32
	if e5.get() == "D":
		tk.Label(root, text ="28" , bg='magenta').grid(row=4, column=4)
		tot += 28
	if e5.get() == "P":
		tk.Label(root, text ="28" , bg='magenta').grid(row=4, column=4)
		tot += 24
	if e5.get() == "F":
		tk.Label(root, text ="0" , bg='magenta').grid(row=4, column=4)
		tot += 0
	
	

	if e6.get() == "A":
		tk.Label(root, text ="30" , bg='magenta').grid(row=5, column=4)
		tot += 30
	if e6.get() == "B":
		tk.Label(root, text ="27" , bg='magenta').grid(row=5, column=4)
		tot += 27
	if e6.get() == "C":
		tk.Label(root, text ="24" , bg='magenta').grid(row=5, column=4)
		tot += 24
	if e6.get() == "D":
		tk.Label(root, text ="21" , bg='magenta').grid(row=5, column=4)
		tot += 21
	if e6.get() == "P":
		tk.Label(root, text ="28" , bg='magenta').grid(row=5, column=4)
		tot += 24
	if e6.get() == "F":
		tk.Label(root, text ="0" , bg='magenta').grid(row=5, column=4)
		tot += 0




	if e7.get() == "A":
		tk.Label(root, text ="40" , bg='magenta').grid(row=6, column=4)
		tot += 40
	if e7.get() == "B":
		tk.Label(root, text ="36" , bg='magenta').grid(row=6, column=4)
		tot += 36
	if e7.get() == "C":
		tk.Label(root, text ="32" , bg='magenta').grid(row=6, column=4)
		tot += 32
	if e7.get() == "D":
		tk.Label(root, text ="28" , bg='magenta').grid(row=6, column=4)
		tot += 28
	if e7.get() == "P":
		tk.Label(root, text ="28" , bg='magenta').grid(row=6, column=4)
		tot += 24
	if e7.get() == "F":
		tk.Label(root, text ="0" , bg='magenta').grid(row=6, column=4)
		tot += 0


	# to display total credits
	tk.Label(root, text=str(tot) , bg='magenta').grid(row=7, column=4)
	
	# to display SGPA
	tk.Label(root, text=str(tot/15) , bg='magenta').grid(row=8, column=4)

	
# end of display function

#------------------------------------------------------------------------------------------------------------------------------------------------------

# label to enter name
tk.Label(root, text="Name" , bg='magenta').grid(row=0, column=0)

# label for registration number
tk.Label(root, text="Reg.No" , bg='magenta').grid(row=0, column=3)

# label for roll Number
tk.Label(root, text="Roll.No" , bg='magenta').grid(row=1, column=0)

# labels for serial numbers
tk.Label(root, text="Srl.No" , bg='magenta').grid(row=2, column=0)
tk.Label(root, text="1" , bg='magenta').grid(row=3, column=0)
tk.Label(root, text="2" , bg='magenta').grid(row=4, column=0)
tk.Label(root, text="3" , bg='magenta').grid(row=5, column=0)
tk.Label(root, text="4" , bg='magenta').grid(row=6, column=0)

#------------------------------------------------------------------------------------------------------------------------------------------------------


tk.Label(root, text="Subject"  , bg='magenta').grid(row=2, column=1)  # labels for subject codes
tk.Label(root, text="MA 8591" , bg='magenta').grid(row=3, column=1)
tk.Label(root, text="EC 8501" , bg='magenta').grid(row=4, column=1)
tk.Label(root, text="EC 8591" , bg='magenta').grid(row=5, column=1)
tk.Label(root, text="CS 8512" , bg='magenta').grid(row=6, column=1)

	

tk.Label(root, text="Grade" , bg='magenta').grid(row=2, column=2)  # label for grades
e4.grid(row=3, column=2)
e5.grid(row=4, column=2)
e6.grid(row=5, column=2)
e7.grid(row=6, column=2)



tk.Label(root, text="Sub Credit" , bg='magenta').grid(row=2, column=3)  # labels for subject credits
tk.Label(root, text="4" , bg='magenta').grid(row=3, column=3)
tk.Label(root, text="4" , bg='magenta').grid(row=4, column=3)
tk.Label(root, text="3" , bg='magenta').grid(row=5, column=3)
tk.Label(root, text="4" , bg='magenta').grid(row=6, column=3)

tk.Label(root, text="Credit obtained" , bg='magenta').grid(row=2, column=4)


e1=tk.Entry(root)  # taking entries of name, reg, roll number respectively
e2=tk.Entry(root)
e3=tk.Entry(root)

e1.grid(row=0, column=1)  # organizing them in th e grid
e2.grid(row=0, column=4)
e3.grid(row=1, column=1)


button1=tk.Button(root, text="submit", bg="green", command=display) # button to display all the calculated credit scores and sgpa
button1.grid(row=8, column=1)

tk.Label(root, text="Total credit", bg='magenta').grid(row=7, column=3)
tk.Label(root, text="SGPA" , bg='magenta').grid(row=8, column=3)
	
root.mainloop()

