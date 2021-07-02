def stepup_pattern(value):
    for i in range(value):# Loop use for creating number of rows
        for j in range(i):  # Loop for printing pattern
            print(" * " , end =" ")  # Printing the patttern
        print("\n")

def stepdown_pattern(value):
    i=value
    while(i>0):# Loop use for creating number of rows
        for j in range(i):  # Loop for printing pattern
            print(" * " , end =" ")  # Printing the patttern
        print("\n")
        i=i-1


def pyramidal_pattern(value):
    space =value- 1  # defining variable for space
    for i in range(0,value):  # Loop use for creating number of rows
        for j in range(0, space): # Loop for creating space
            print(end=" ")  #Providing Space
        space = space - 1   # Decrement of space value
        for j in range(0, i + 1):  # Loop for printing pattern
            print(" * ", end="")   # Printing the patttern
        print("\r")


def main():
    print(" Enter 1 for Stepup Pattern ")
    print(" Enter 2 for Stepdown Pattern ")
    print(" Enter 3 for Pyramidal Pattern ")
    choice=int(input (" "))     #input taking for performing the operation
    value=int(input(" Enter the number of steps "))

    #Condition checking fordiffernent operation.
    if choice == 1:
        stepup_pattern(value)
    elif choice == 2:
        stepdown_pattern(value)
    elif  choice == 3:
        pyramidal_pattern(value)

    condition=int(input(" Enter 1 to continue or else to exit "))
    if condition == 1:  #condition checking for re-executing the program.
        main()   # Recalling main function
    else:
        exit()   #exiting the program


main()  # Calling the main function