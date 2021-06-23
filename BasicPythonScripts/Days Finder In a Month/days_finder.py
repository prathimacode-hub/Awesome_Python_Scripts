# This code will be used to find out the Numbers of day in a month.
print("  -- This code is used to find the Number of days in a Month--   ")

import datetime #importing libray


def days_finder(month_number, year): #defining function to find the number of days

    leap = 0
    list_31 = [1, 3, 5, 7, 8, 10, 12] #Defining list
    list_30 = [4, 6, 9, 11] #Defining list
    if year % 4 == 0: #Condition check for Leap Year
        leap = 1
    if month_number in list_30:  #Condition check for Number of days
        number_of_days = 30
    elif month_number in list_31: #Condition check for Number of days
        number_of_days = 31
    else:
        number_of_days = 28 + leap #Condition check for Number of days
    return number_of_days


def main():
    year = int(input("Enter the year "))  # User defining value
    month_number = (input(' Enter the Name of Month '))  # User defining value
    datetime_object = datetime.datetime.strptime(month_number, "%m")
    month_name = datetime_object.strftime("%B")
    month_number = int(month_number)  #Converting str to int

    print("The Number of days in ", days_finder(month_number, year))

    choice=int(input("Enter 1 to Continue or else to exit "))  #Choice Selection
    if choice == 1:
        main()
    else:
        exit


main()

