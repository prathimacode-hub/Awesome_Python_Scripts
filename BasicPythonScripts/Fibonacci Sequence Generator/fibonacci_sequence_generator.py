#code of the program
#fibonacci series

n=int(input("No. of terms :-" ))

#1st two terms are predefined
a1=0
a2=1
i=0

#applying conditions for correct results
if n<=0:
    print("Enter the terms > 0 ")
elif n==1:
    print(a1)
else:

    #using loops
    print("FIBONACCI SERIES :-")  #generating the series 
    while i<=n:
        print(a1)
        a=a1+a2
        a1=a2
        a2=a
        i+=1
        
