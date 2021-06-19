import tkinter
from tkinter import *
#importing tkinter
#Added splash screen
import pyglet

animation=pyglet.image.load_animation('Media/Splash Screen_Calculator App.gif')
animSprite=pyglet.sprite.Sprite(animation)
w=animSprite.width
h=animSprite.height
win=pyglet.window.Window(width=w,height=h,style='borderless')
win.set_location(100,100)

r,g,b,alpha=0.5,0.5,0.8,0.5
pyglet.gl.glClearColor(r,g,b,alpha)
@win.event

def on_draw():
	win.clear()
	animSprite.draw()

def close(event):
	win.close()

pyglet.clock.schedule_once(close,5.0)

pyglet.app.run()

root = tkinter.Tk()
root.maxsize(300,400)
root.minsize(300,400)
root.configure(bg='lightblue')

root.title("Calculator")
#Added Logo in Title Bar
l=PhotoImage(file='Media/Logo_CalculatorApp.gif')
root.iconphoto(False,l)

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

label_result = tkinter.Label(root, text="hello",height=3,width=30)
label_result.grid(row=1, column=0, columnspan=6,padx=5,pady=5)

#created the layout for the calculator app

but_1 = tkinter.Button(root, text="1", command=lambda: add("1"),bg='blue', fg='white',height=3,width=5)

but_1.grid(row=2, column=0,padx=15,pady=5)

but_2 = tkinter.Button(root, text="2", command=lambda: add("2"),bg='blue', fg='white',height=3,width=5)
but_2.grid(row=2, column=1,padx=15,pady=5)

but_3 = tkinter.Button(root, text="3", command=lambda: add("3"),bg='blue', fg='white',height=3,width=5)
but_3.grid(row=2, column=2,padx=15,pady=5)

but_divide = tkinter.Button(root, text="/", command=lambda: add("/"),bg='blue', fg='white',height=3,width=5)
but_divide.grid(row=2, column=3,padx=15,pady=5)

but_4 = tkinter.Button(root, text="4", command=lambda: add("4"),bg='blue', fg='white',height=3,width=5)
but_4.grid(row=4, column=0,padx=15,pady=5)

but_5 = tkinter.Button(root, text="5", command=lambda: add("5"),bg='blue', fg='white',height=3,width=5)
but_5.grid(row=4, column=1,padx=15,pady=5)

but_6 = tkinter.Button(root, text="6", command=lambda: add("6"),bg='blue', fg='white',height=3,width=5)
but_6.grid(row=4, column=2,padx=15,pady=5)

but_mul = tkinter.Button(root, text="*", command=lambda: add("*"),bg='blue', fg='white',height=3,width=5)
but_mul.grid(row=4, column=3,padx=15,pady=5)

but_7 = tkinter.Button(root, text="7", command=lambda: add("7"),bg='blue', fg='white',height=3,width=5)
but_7.grid(row=6, column=0,padx=15,pady=5)

button_8 = tkinter.Button(root, text="8", command=lambda: add("8"),bg='blue', fg='white',height=3,width=5)
button_8.grid(row=6, column=1,padx=15,pady=5)

button_9 = tkinter.Button(root, text="9", command=lambda: add("9"),bg='blue', fg='white',height=3,width=5)
button_9.grid(row=6, column=2,padx=15,pady=5)

button_sub = tkinter.Button(root, text="-", command=lambda: add("-"),bg='blue', fg='white',height=3,width=5)
button_sub.grid(row=6, column=3,padx=15,pady=5)

button_clear = tkinter.Button(root, text="C", command=lambda: clear(),height=3,width=5)
button_clear.grid(row=7, column=0,padx=15,pady=5)

button_0 = tkinter.Button(root, text="0", command=lambda: add("0"),bg='blue', fg='white',height=3,width=5)
button_0.grid(row=7, column=1,padx=15,pady=5)

but_dot = tkinter.Button(root, text=".", command=lambda: add("."),bg='blue', fg='white',height=3,width=5)
but_dot.grid(row=7, column=2,padx=15,pady=5)

but_add = tkinter.Button(root, text="+", command=lambda: add("+"),bg='blue', fg='white',height=3,width=5)
but_add.grid(row=7, column=3,padx=15,pady=5)

but_equals = tkinter.Button(root, text="=", width=26, command=lambda: calculate())
but_equals.grid(row=9, column=0, columnspan=4,pady=10)
#completed creating GUI design for python.

root.mainloop()
