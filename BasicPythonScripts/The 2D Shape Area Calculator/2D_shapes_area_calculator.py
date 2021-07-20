from math import pi #Pi is imported from Math Library imported
print("Please choose one of the following option to find Areas of 2D shape: \n1.Circle \n2.Triangle \n3.Square \n4.Rectangle \n5.Parallelogram \n6.Trapezium \n7.Ellipse")
i = int(input("Option:")) #Choose any one option
if i == 1: #Circle
    r = float(input("radius: "))
    print("Area of the circle:",pi*r*r) #Formula to find area of circle
elif i== 2: #Triangle
    print("Choose a method: \n1.Using Herons Formula \n2.Base and Height")
    j = int(input("Method:"))
    if j ==1: #Method 1
        a = float(input('a: '))
        b = float(input('b: '))
        c = float(input('c: '))
        s = (a + b + c) / 2 #Heron's Formula
        print('Area of the triangle:',(s * (s - a) * (s - b) * (s - c)) ** 0.5)  #Formula to find area of Triangle

    elif j == 2: #Method 2
        b = float(input('b: '))
        h = float(input('h: '))
        print("Area of the triangle:",0.5*b*h)  #Formula to find area of Triangle

elif i == 3: #Square
    a = float(input('a:'))
    print("Area of the Square:",a*a)  #Formula to find area of Square

elif i == 4: #Rectangle
    l = float(input("l: "))
    b = float(input("b:"))
    print("Area of Rectangle:",l*b)  #Formula to find area of Rectangle

elif i == 5: #Parallelogram
    b = float(input('b: '))
    h = float(input('h: '))
    print("Area of the Parallelogram:",b*h)  #Formula to find area of Parallelogram

elif i == 6: #Trapezium
    a = float(input('a: '))
    b = float(input('b: '))
    h = float(input('h: '))
    print("Area of the Trapezium:",(0.5*(a+b))*h)  #Formula to find area of Trapezium

elif i == 7: #Ellipse
    a = float(input('a: '))
    b = float(input('b: '))
    print("Area of Ellipse:",pi*a*b) #Formula to find area of Ellipse

else:
    print("Invalid Option")
