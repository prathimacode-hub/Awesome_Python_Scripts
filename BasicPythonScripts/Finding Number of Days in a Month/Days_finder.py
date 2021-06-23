# This code will be used to find out the Numbers of day in a month.
print("  -- This code is used to find the Number of days in a Month--   ")

import datetime


def days_finder(month_number, year):
    leap = 0
    print(month_number)
    list_31 = [1, 3, 5, 7, 8, 10, 12]
    list_30 = [4, 6, 9, 11]
    if year % 4 == 0:
        leap = 1
    if month_number in list_30:
        number_of_days = 30
    elif month_number in list_31:
        number_of_days = 31
    else:
        number_of_days = 28 + leap
    return number_of_days


def main():
    year = int(input("Enter the year "))
    month_number = (input(' Enter the Name of Month '))
    datetime_object = datetime.datetime.strptime(month_number, "%m")

    month_name = datetime_object.strftime("%B")

    print("Month Number ", month_number)
    month_number = int(month_number)

    print("The Number of days in ", days_finder(month_number, year))

    choice=int(input("Enter 1 to Continue or else to exit "))
    if choice == 1:
        main()
    else:
        exit


main()

