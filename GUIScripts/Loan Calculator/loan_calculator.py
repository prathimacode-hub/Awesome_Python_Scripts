# Import TKinter Module
from tkinter import *           # (*) Imports whole module

# Create a user defined class named: LoanCalculator which holds it's own
# data members and member functions.

class LoanCalculator:
	def __init__(self):    #Special method in Python Class-Constructor of a Python Class
		window = Tk() #Creates a window to house the calculator bits
		window.title("Loan Calculator") # sets the title
		window.configure(background = "light green")  # sets bg color for window

		# Create input boxes: Label function creates a display box to take input
		# The grid method gives it a table like structure
		#Widgets are centered by default.
		Label(window, font='Helvetica 12 bold',bg ="light green",text="Annual Interest Rate").grid(row=1,column=1, sticky=W)
		Label(window, font='Helvetica 12 bold',bg ="light green",text="Number of Years").grid(row=2,column=1, sticky=W)
		Label(window, font='Helvetica 12 bold',bg ="light green",text="Loan Amount").grid(row=3,column=1, sticky=W)
		Label(window, font='Helvetica 12 bold',bg ="light green", text="Monthly Payment").grid(row=4,column=1, sticky=W)
		Label(window, font='Helvetica 12 bold',bg ="light green",text="Total Payment").grid(row=5,column=1, sticky=W)

		# Create objects: first 3 objects to take inputs using entry() function

		self.annualInterestRateVar = StringVar()
		Entry(window, textvariable=self.annualInterestRateVar,justify=RIGHT).grid(row=1, column=2)

		self.numberofYearsVar = StringVar()
		Entry(window, textvariable=self.numberofYearsVar,justify=RIGHT).grid(row=2, column=2)

		self.loanAmountVar = StringVar()
		Entry(window, textvariable=self.loanAmountVar,justify=RIGHT).grid(row=3, column=2)

		self.monthlyPaymentVar = StringVar()
		lblMonthlyPayment= Label(window,font='Helvetica 12 bold',bg ="light green", textvariable=self.monthlyPaymentVar).grid(row=4,column=2, sticky=E)

		self.totalPaymentVar = StringVar()
		lblTotalPayment= Label(window,font='Helvetica 12 bold',bg ="light green", textvariable=self.totalPaymentVar).grid(row=5,column=2, sticky=E)

		# Create button to calculate payment. When button is clicked it will call the compute payment function

		btComputePayment = Button(window, text="Compute Payment",bg="red",fg="white",font='Helvetica 14 bold', command=self.computePayment).grid(row=6, column=2, sticky=E)
		btClear = Button(window, text="Clear",bg="blue",fg="white",font='Helvetica 14 bold', command=self.delete_all).grid(row=6, column=8, padx=20,pady=20 ,sticky=E)

		window.mainloop()  # The mainloop () function is used to run the application program.

		# Create function to compute total payment

	def computePayment(self):
		monthlyPayment = self.getMonthlyPayment(
			float(self.loanAmountVar.get()),
			float(self.annualInterestRateVar.get())  / 1200 ,
			int(self.numberofYearsVar.get()))


		self.monthlyPaymentVar.set(format(monthlyPayment, '10.2f'))
		totalPayment = float(self.monthlyPaymentVar.get()) * 12 \
		 * int(self.numberofYearsVar.get())

		self.totalPaymentVar.set(format(totalPayment, '10.2f'))


	def getMonthlyPayment(self,loanAmount,monthlyInterestRate,numberofYears):
		monthlyPayment = loanAmount * monthlyInterestRate / (1-1/(1 + monthlyInterestRate)** (numberofYears * 12 ))
		return monthlyPayment


	def delete_all(self) :
		self.monthlyPaymentVar.set("")
		self.loanAmountVar.set("")
		self.annualInterestRateVar.set("")
		self.numberofYearsVar.set("")
		self.totalPaymentVar.set("")




# Call the class to run the program

LoanCalculator()
