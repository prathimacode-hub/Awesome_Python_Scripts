def roman_number(num):
    if num > 3999:
        print("enter number less than 3999")
        return
    #take 2 list symbol and value symbol having roman of each integer in list value
    value = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    symbol = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    roman = ""
    i=0
    while num>0:
        #then we have to check the the range of value
        #divide the number with all values starting from zero
        div = num//value[i]
        #mod to get part of number
        num = num%value[i]
        while div:
            roman = roman+symbol[i]
            #loop goes till div become zero
            div = div-1
        i=i+1
    return roman

num = int(input("enter an integer number:  "))
print(f" Roman Numeral of {num} is {roman_number(num)}")