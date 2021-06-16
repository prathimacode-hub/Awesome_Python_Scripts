#from the forex-python module import CurrencyRates and CurrencyCodes to perform the tasks required
from forex_python.converter import CurrencyRates, CurrencyCodes

#create objects for the imported packages
rates = CurrencyRates()

codes = CurrencyCodes()

#Declare the functions according the task


def exchange_rate():
    #This function helps you to calculate exchange rates between given currencies
     c1 = input("Enter country code one (from): ").upper()
     c2 = input("Enter country code two (to): ").upper()
     print(rates.get_rate(c1, c2))

def conversion():
    #This function helps you in coversion between given currencies for a given amount

     t1 = input("Enter country code one (from): ").upper()
     t2 = input("Enter country code two (to): ").upper()
     t3 = int(input("Enter the amount of currency in " + t1 + " :"))

     print(rates.convert(t1, t2, t3))

def other():
    #This function helps you in providing info about the currency codes and currency names
    #when user gives currency code as input

     s1 = input("Type sym for symbols or name for currency name: ")
     if s1 == 'sym':
        s2 = input("Enter the currency code of the country: ").upper()
        print(codes.get_symbol(s2))
     elif s1 == 'name':
        s3 = input("Enter the currency name: ").upper()
        print(codes.get_currency_name(s3))

while True:   #This line allows us to ask the user for input until valid response is given

    purpose = input("Type 'r' if you wish to know the rate of currency, 'c' for converting currency or 's' for alternate information: ")

    try:
         if purpose == 'r':
            exchange_rate()  #Calls exchange_rate function if user's response is 'r'
         elif purpose == 'c':
            conversion()     #Calls conversion function if user's response is 'c'
         elif purpose == 's':
            other()          #Calls other function if user's response is 's'

            break   #breaks from the loop if user gives suitable input

         print("Enter only r,c or s")  #this statement is printed if wrong response is given

    except:
         continue   #continues until suitable response is given
