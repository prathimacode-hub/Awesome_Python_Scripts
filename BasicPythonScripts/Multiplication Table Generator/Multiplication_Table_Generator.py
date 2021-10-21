def table (num):
    for mult in range(1,11):    
        print(str(num) + " X " + str(mult) + " = " + str(num * mult))
        mult += 1

count = int(input("Enter the number for which you want table: "))
table(count)