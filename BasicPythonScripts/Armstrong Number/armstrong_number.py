#armstrong number
number=input("Enter the number :- ")             #user input
#storing the order of number in n
n=len(str(number))

sum=0
#changing the data type to int so that we can use it in looping
number=int(number)
local =int(number)

while local > 0 : 
    l_digit=local%10
    sum =sum + l_digit**n
    local//=10 
#CONDITIONAL STATEMENTS    
if number==sum:
    print(number,"is an Armstrong Number")
else:
    print(number,"is not an Armstrong Number")
    
