#importing necessary modules
from tkinter import *

# function for addition
def add(a,b):
    return a + b

#function for subraction
def sub(a,b):
    return a - b

#function for multiplication
def mul(a,b):
    return a * b

#function for division
def div(a,b):
    return a / b

#functtion for Modulus
def mod(a,b):
    return a % b

# function to find LCM
def lcm(a,b):
    L = a if a>b else b
    while L <= a*b:
        if L%a == 0 and L%b == 0:
            return L
        L+=1

# function to find HCF
def hcf(a,b):
    H = a if a<b else b
    while H >= 1:
        if a%H == 0 and b%H == 0:
            return H
        H-=1

# extracting the values of a and b from Text
def extraxt_from_text(text):
    l = []
    for t in text.split(' '):  #splitting using whitespace
        try:
            l.append(float(t))     #converting the values entered into float
        except ValueError:
            pass
    return l


# Function for calculation
def calculate():
    #getting user input
    text = textin.get()
    #splitting the words
    for word in text.split(' '):

        #converting the splitted words to uppercase and check whether they match with keys of Operations Dictionary
        if word.upper() in operations.keys():
            try:
                l = extraxt_from_text(text)   #splitting the text and storing in the array
                r = operations[word.upper()](l[0] , l[1])    #Here we are finding the relevant operation from dict and passing the values for calculation
                list.delete(0,END)     #removing the inputs
                list.insert(END,r)      #inserting the output value
            except:                         #To handle error
                list.delete(0,END)
                list.insert(END,'something went wrong please enter again')
            finally:
                break
        elif word.upper() not in operations.keys():    #To handle wrong input
            list.delete(0,END)
            list.insert(END,'something went wrong please enter again')

# Creating the dictionary of operations
operations = {'ADD':add , 'ADDITION':add , 'SUM':add , 'PLUS':add ,
                'SUB':sub , 'DIFFERENCE':sub , 'MINUS':sub , 'SUBTRACT':sub,
                 'LCM':lcm , 'HCF':hcf , 'PRODUCT':mul , 'MULTIPLICATION':mul,
                 'MULTIPLY':mul , 'DIVISION':div , 'DIV':div ,'DIVIDE':div, 'MOD':mod ,
                  'REMAINDER':mod , 'MODULUS':mod}

#setting and configuring window size color and name
win = Tk()
win.geometry('500x300')
win.title('Smart Calculator')
win.configure(bg='lightskyblue')


# Giving labels to texts in the window
l1 = Label(win , text='I am a smart calculator',width=20 , padx=3)
l1.place(x=150,y=10)
l2 = Label(win , text='How can i help you' , padx=3)
l2.place(x=176,y=130)

# Input area for entering the text (user input)
textin = StringVar()
e1 = Entry(win , width=30 , textvariable = textin)
e1.place(x=100,y=160)

#button to calculate
b1 = Button(win , text='Just this' ,command=calculate)
b1.place(x=210,y=200)

#Displaying the output here
list = Listbox(win,width=20,height=3)
list.place(x=150,y=230)

