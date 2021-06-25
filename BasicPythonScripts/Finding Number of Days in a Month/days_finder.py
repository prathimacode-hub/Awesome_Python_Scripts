# This code will be used to find out the Numbers of day in a month.
print("  -- This code is used to find the Number of days in a Month--   ")
days_finder.py
import datetime


def days_finder(month_number, year):  #defining the functon to find the number of days in a month
    leap = 0   #assigning value
    print(month_number)
    list_31 = [1, 3, 5, 7, 8, 10, 12]  # Listing Out  month number having 31 days
    list_30 = [4, 6, 9, 11]  # Listing Out  month number having 31 days
    if year % 4 == 0:   # Condition checking for leap year
        leap = 1
    if month_number in list_30:   # Condition check for 30 days
        number_of_days = 30
    elif month_number in list_31:   # Condition checking for 31 days
        number_of_days = 31
    else:                           #Condition checking for 28 days
        number_of_days = 28 + leap  # if month is feb and its leap year than leap + 1 so it will become 29 days
    return number_of_days


def main():                       #  main function
    year = int(input("Enter the year "))          # user input (year ) 
    month_number = (input(' Enter the Name of Month '))   #user input (month)
    datetime_object = datetime.datetime.strptime(month_number, "%m") # calling datetime libray for month finding

    month_name = datetime_object.strftime("%B")    # This Section will give month name as output 
    month_number = int(month_number)

    print("The Number of days in ",month_name ," is " ,days_finder(month_number, year))

    choice=int(input("Enter 1 to Continue or else to exit "))
    if choice == 1:
        main()
    else:
        exit


main()

