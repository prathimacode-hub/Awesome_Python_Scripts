import tkinter
#importing tkinter

root = tkinter.Tk()

root.configure(bg='lightblue')

root.title("Calculator")

expression = ""

# Creating functions
def add(value):
    global expression
    expression += value
    label_result.config(text=expression)
    
def clear():
    global expression
    expression = ""
    label_result.config(text=expression)
    
def calculate():
    global expression
    result = ""
    if expression != "":
        try:
            result = eval(expression)
        except:
            result = "error"
            expression = ""
    label_result.config(text=result)
            
# Creating GUI

#adding the name hello in the row 1 and column 0 line.

label_result = tkinter.Label(root, text="hello")
label_result.grid(row=1, column=0, columnspan=6)

#created the layout for the calculator app

but_1 = tkinter.Button(root, text="1", command=lambda: add("1"),bg='blue', fg='white')

but_1.grid(row=2, column=0)

but_2 = tkinter.Button(root, text="2", command=lambda: add("2"),bg='blue', fg='white')
but_2.grid(row=2, column=1)

but_3 = tkinter.Button(root, text="3", command=lambda: add("3"),bg='blue', fg='white')
but_3.grid(row=2, column=2)

but_divide = tkinter.Button(root, text="/", command=lambda: add("/"),bg='blue', fg='white')
but_divide.grid(row=2, column=3)


but_4 = tkinter.Button(root, text="4", command=lambda: add("4"),bg='blue', fg='white')
but_4.grid(row=4, column=0)

but_5 = tkinter.Button(root, text="5", command=lambda: add("5"),bg='blue', fg='white')
but_5.grid(row=4, column=1)

but_6 = tkinter.Button(root, text="6", command=lambda: add("6"),bg='blue', fg='white')
but_6.grid(row=4, column=2)

but_mul = tkinter.Button(root, text="*", command=lambda: add("*"),bg='blue', fg='white')
but_mul.grid(row=4, column=3)

but_7 = tkinter.Button(root, text="7", command=lambda: add("7"),bg='blue', fg='white')
but_7.grid(row=6, column=0)

button_8 = tkinter.Button(root, text="8", command=lambda: add("8"),bg='blue', fg='white')
button_8.grid(row=6, column=1)

button_9 = tkinter.Button(root, text="9", command=lambda: add("9"),bg='blue', fg='white')
button_9.grid(row=6, column=2)

button_sub = tkinter.Button(root, text="-", command=lambda: add("-"),bg='blue', fg='white')
button_sub.grid(row=6, column=3)

button_clear = tkinter.Button(root, text="C", command=lambda: clear())
button_clear.grid(row=7, column=0)

button_0 = tkinter.Button(root, text="0", command=lambda: add("0"),bg='blue', fg='white')
button_0.grid(row=7, column=1)

but_dot = tkinter.Button(root, text=".", command=lambda: add("."),bg='blue', fg='white')
but_dot.grid(row=7, column=2)

but_add = tkinter.Button(root, text="+", command=lambda: add("+"),bg='blue', fg='white')
but_add.grid(row=7, column=3)

but_equals = tkinter.Button(root, text="=", width=16, command=lambda: calculate())
but_equals.grid(row=9, column=0, columnspan=4)
#completed creating GUI design for python.

root.mainloop()
