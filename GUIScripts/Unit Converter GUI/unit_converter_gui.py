from tkinter import *
# Creating a GUI Window
window = Tk()
#funtion for the gui grid
def from_kg():
    gram = float(e2_value.get())*1000
    pound = float(e2_value.get())*2.20462
    ounce = float(e2_value.get())*35.274
    t1.delete("1.0",END)
    t1.insert(END, gram)
    t2.delete("1.0", END)
    t2.insert(END, pound)
    t3.delete("1.0", END)
    t3.insert(END, ounce)
#input button
e1 = Label(window, text="Input the weight in KG")
e2_value = StringVar()
e2 = Entry(window, textvariable=e2_value)
e3 = Label(window, text="Gram")
e4 = Label(window, text="Pound")
e5 = Label(window, text="Ounce")
#proper formatting of input text area
t1 = Text(window, height=5, width=30,bg='lightpink')
t2 = Text(window, height=5, width=30,bg='lightgreen')
t3 = Text(window, height=5, width=30,bg='lightblue')

b1 = Button(window, text="Convert", command=from_kg)
#giving the proper position for each button and text area
e1.grid(row=0, column=0)
e2.grid(row=0, column=1)
e3.grid(row=1, column=0)
e4.grid(row=1, column=1)
e5.grid(row=1, column=2)
t1.grid(row=2, column=0)
t2.grid(row=2, column=1)
t3.grid(row=2, column=2)
b1.grid(row=0, column=2)

window.mainloop()

"""
For reference
1 milligram = 0.001 gram
1 centigram = 0.01 gram
1 decigram = 0.1 gram
1 kilogram = 1000 grams
1 gram = 1000 milligrams
1 ton = 2000 pounds
1 pound = 16 ounces
"""