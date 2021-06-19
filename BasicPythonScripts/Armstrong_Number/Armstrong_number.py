
#armstrong number
number=input("Enter the number :- ")
n=len(str(number))

sum=0
#we save the base as 
number=int(number)
local =int(number)

while local > 0 : 
    l_digit=local%10
    sum =sum + l_digit**n
    local//=10 
    
if number==sum:
    print(number,"is an Armstrong Number")
else:
    print(number,"is not an Armstrong Number")
    
