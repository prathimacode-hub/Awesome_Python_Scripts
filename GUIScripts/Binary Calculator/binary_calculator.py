from tkinter import *
window = Tk()
window.title("Standard Binary Calculator")
window.resizable(0, 0)

#lets create binary digits for more clear to calculator
def f1():
    s = e1_val.get()
    e1.delete(first=0, last=len(s))
def f2():
    s = e1_val.get()
    e1.insert(END, "1")
def f3():
    s = e1_val.get()
    e1.insert(END, "0")

#this loop is for the -, +, / and * operators so that whenever the user is giving the below operations, it will work accordingly.
def f4():
    x = 0
    s = e1_val.get()
    for i in range(0, len(s)):
        if s[i] == '/' or s[i] == 'X' or s[i] == '+' or s[i] == '-':
            a = s[0:i]
            b = s[i + 1:len(s)]
            if s[i] == '-':
                x = sub(int(a), int(b))
            elif s[i] == '/':
                x = int(int(a) / int(b))
            elif s[i] == 'X':
                x = int(int(a) * int(b))
            elif s[i] == '+':
                x = int(add(int(a), int(b)))

    e1.delete(first=0, last=len(s))
    e1.insert(END, "")
    e1.insert(END, str(x))

#this is for dividing the two binary numbers.
def bin_to_dec(n):
    num = n
    dec_value = 0
    base = 1
    temp = num
    while (temp):
        last_digit = temp % 10
        temp = int(temp / 10)

        dec_value += last_digit * base
        base = base * 2
    return dec_value

#now, will add the two binary numbers.
def add(x, y):
    a = bin_to_dec(x)
    b = bin_to_dec(y)
    c = a + b
    d = bin(c).replace("0b", "")
    return d

#this is for - operation for two binary numbers.
def sub(x, y):
    a = bin_to_dec(x)
    b = bin_to_dec(y)
    c = a - b
    d = bin(c).replace("0b", "")
    return d

#this is for function run
def f5():
    x = 0
    s = e1_val.get()
    flag = 1
    
    #from the operations :  -, +, * or / if the operation is `+` then do the work or else end the loop.
    for i in range(0, len(s)):
        if s[i] == '/' or s[i] == 'X' or s[i] == '+' or s[i] == '-':
            flag = 0
            a = s[0:i]
            b = s[i + 1:len(s)]
            if s[i] == '-':
                x = sub(int(a), int(b))
            elif s[i] == '/':
                x = int(int(a) / int(b))
            elif s[i] == 'X':
                x = int(int(a) * int(b))
            elif s[i] == '+':
                x = int(add(int(a), int(b)))
    if flag == 0:
        e1.delete(first=0, last=len(s))
        e1.insert(END, str(x))
    e1.insert(END, "+")

#from the operations :  -, +, * or / if the operation is `-` then do the work or else end the loop.
def f6():
    x = 0
    s = e1_val.get()
    flag = 1
    for i in range(0, len(s)):
        if s[i] == '/' or s[i] == 'X' or s[i] == '+' or s[i] == '-':
            flag = 0
            a = s[0:i]
            b = s[i + 1:len(s)]
            if s[i] == '-':
                x = sub(int(a), int(b))
            elif s[i] == '/':
                x = int(int(a) / int(b))
            elif s[i] == 'X':
                x = int(int(a) * int(b))
            elif s[i] == '+':
                x = int(add(int(a), int(b)))
    if flag == 0:
        e1.delete(first=0, last=len(s))
        e1.insert(END, str(x))
    e1.insert(END, "-")

#from the operations :  -, +, * or / if the operation is `/` then do the work or else end the loop.
def f7():
    x = 0
    s = e1_val.get()
    flag = 1
    for i in range(0, len(s)):
        if s[i] == '/' or s[i] == 'X' or s[i] == '+' or s[i] == '-':
            flag = 0
            a = s[0:i]
            b = s[i + 1:len(s)]
            if s[i] == '-':
                x = sub(int(a), int(b))
            elif s[i] == '/':
                x = int(int(a) / int(b))
            elif s[i] == 'X':
                x = int(int(a) * int(b))
            elif s[i] == '+':
                x = int(add(int(a), int(b)))
    if flag == 0:
        e1.delete(first=0, last=len(s))
        e1.insert(END, str(x))
    e1.insert(END, "/")

#from the operations :  -, +, * or / if the operation is `*` then do the work or else end the loop.
def f8():
    x = 0
    s = e1_val.get()
    flag = 1
    for i in range(0, len(s)):
        if s[i] == '/' or s[i] == 'X' or s[i] == '+' or s[i] == '-':
            flag = 0
            a = s[0:i]
            b = s[i + 1:len(s)]
            if s[i] == '-':
                x = sub(int(a), int(b))
            elif s[i] == '/':
                x = int(int(a) / int(b))
            elif s[i] == 'X':
                x = int(int(a) * int(b))
            elif s[i] == '+':
                x = int(add(int(a), int(b)))
    if flag == 0:
        e1.delete(first=0, last=len(s))
        e1.insert(END, str(x))
    e1.insert(END, "X")

#creating gui for the calculator .

#firstly, creating a space
e1_val = StringVar()
e1 = Entry(window, textvariable=e1_val, width=50)
e1.grid(row=0, column=0, columnspan=4)

# adding the buttons will give colours to the calculator. 
b1 = Button(window, text="1", width=8, height=2, command=f2,bg='lightblue', fg='white')
b1.grid(row=1, column=0)

b0 = Button(window, text="0", width=8, height=2, command=f3,bg='lightblue', fg='white')
b0.grid(row=1, column=1)

clear = Button(window, text="C", width=8, height=2, command=f1,bg='lightblue', fg='white')
clear.grid(row=1, column=2)

beq = Button(window, text="=", width=8, height=2, command=f4,bg='lightpink', fg='white')
beq.grid(row=1, column=3)

badd = Button(window, text="+", width=8, height=2, command=f5,bg='lightblue', fg='white')
badd.grid(row=2, column=0)

bsub = Button(window, text="-", width=8, height=2, command=f6,bg='lightblue', fg='white')
bsub.grid(row=2, column=1)

bmul = Button(window, text="X", width=8, height=2, command=f8,bg='lightblue', fg='white')
bmul.grid(row=2, column=2)

bdiv = Button(window, text="/", width=8, height=2, command=f7,bg='lightpink', fg='white')
bdiv.grid(row=2, column=3)

#ending the loop and it will run until it is false.
window.mainloop()
