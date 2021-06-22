from tkinter import *
from tkinter import messagebox
import tkinter.messagebox as mbox
import pyglet

#Added Splash Screen
animation=pyglet.image.load_animation('Media/BMI_Splash Screen.gif')
animSprite=pyglet.sprite.Sprite(animation)
w=animSprite.width
h=animSprite.height

win=pyglet.window.Window(width=w,height=h,style='borderless')
win.set_location(200,100)

r,g,b,alpha=0.5,0.5,0.8,0.5
pyglet.gl.glClearColor(r,g,b,alpha)
@win.event

def on_draw():
	win.clear()
	animSprite.draw()

def close(event):
	win.close()
#Splash screen timer
pyglet.clock.schedule_once(close,4.0)

pyglet.app.run()

#Reset button functioning
def reset_entry():
    age_tf.delete(0,'end')
    height_tf.delete(0,'end')
    weight_tf.delete(0,'end')

#BMI calculation
def calculate_bmi():
    kg=int(weight_tf.get())
    m=int(height_tf.get())/100
    bmi=kg/(m*m)
    bmi=round(bmi,1)
    bmi_index(bmi)

def bmi_index(bmi):
    if bmi<18.5:
        messagebox.showinfo('BMI Ratio',f'BMI={bmi} is Underweight')
    elif (bmi>18.5) and (bmi<24.9):
        messagebox.showinfo('BMI Ratio', f'BMI = {bmi} is Normal')
    elif (bmi > 24.9) and (bmi < 29.9):
        messagebox.showinfo('BMI Ratio', f'BMI = {bmi} is Overweight')
    elif (bmi > 29.9):
        messagebox.showinfo('BMI Ratio', f'BMI = {bmi} is Obesity')
    else:
        messagebox.showerror('BMI Ratio', 'Something went wrong!')

root=Tk()
#Title for main window
root.title('BMI Calculator')
root.geometry('700x500')
#Background colour of the main screen
root.config(bg='cyan')
#Dimensions of the screen
root.maxsize(700,500)
root.minsize(700,500)
#Disabled the maximsize/minimise button. 
root.resizable(0,0)
#Font styles for complete program
font1=("Times",14,"bold")
font2=("Times",14)

#Added the logo to application
l=PhotoImage(file="Media/BMI Calculator_logo.gif")
root.iconphoto(False,l)

var=IntVar()

#Designing of the screen by adding buttons entry,boxes,creating a frame.
frame=Frame(root,padx=100,pady=100)
frame.pack(expand=True)

age_lb = Label(frame,text="Enter your age ",font=font1)
age_lb.grid(row=1, column=1)

age_tf = Entry(frame,font=font1,bd=3)
age_tf.grid(row=1, column=2, pady=10)

gen_lb = Label(frame,text='Select Gender',font=font1)
gen_lb.grid(row=2, column=1)

frame2 = Frame(frame)
frame2.grid(row=2, column=2, pady=10)

male_rb = Radiobutton(frame2,text='Male',variable=var,value=1,font=font1,background="light grey",padx=5)
male_rb.pack(side=LEFT)

female_rb = Radiobutton(frame2,text='Female',variable=var,value=2,font=font1,background="light grey",padx=5)
female_rb.pack(side=RIGHT)

height_lb = Label(frame,text="Enter Height (in cm) ",font=font1)
height_lb.grid(row=3, column=1)

weight_lb = Label(frame,text="Enter Weight (in kg) ",font=font1)
weight_lb.grid(row=4, column=1)

height_tf = Entry(frame,font=font1,bd=3)
height_tf.grid(row=3, column=2, pady=10)

weight_tf = Entry(frame,font=font1,bd=3)
weight_tf.grid(row=4, column=2, pady=10)

frame3 = Frame(frame)
frame3.grid(row=5, columnspan=3, pady=20)

#For HoverButton so that as the cursor comes over the button the button changes it's colour to light blue.
def on_entercal(c):
    cal_btn.config(background="light blue",foreground="black")

def on_leavecal(c):
    cal_btn.config(background="SystemButtonFace",foreground="black")

cal_btn = Button(frame3,text='Calculate',command=calculate_bmi,font=font2)
cal_btn.pack(side=LEFT,padx=7)

cal_btn.bind('<Enter>',on_entercal)
cal_btn.bind('<Leave>',on_leavecal)

#For HoverButton so that as the cursor comes over the button the button changes it's colour to light blue.
def on_enterreset(r):
    reset_btn.config(background="light blue",foreground="black")

def on_leavereset(r):
    reset_btn.config(background="SystemButtonFace",foreground="black")

reset_btn = Button(frame3,text='Reset',command=reset_entry,font=font2)
reset_btn.pack(side=LEFT,padx=7)

reset_btn.bind('<Enter>',on_enterreset)
reset_btn.bind('<Leave>',on_leavereset)

def end():
    root.destroy()

#Pop-Up for exit Screen
def exit_win():
    ans=mbox.askyesno("Exit","Are you sure?")
    if(ans):
        root.destroy()

#For HoverButton so that as the cursor comes over the button the button changes it's colour to light blue.
def on_enterexit(e):
    exit_btn.config(background="light blue",foreground="black")

def on_leaveexit(e):
    exit_btn.config(background="SystemButtonFace",foreground="black")

exit_btn = Button(frame3,text='Exit',command=end,font=font2)
exit_btn = Button(frame3,text='Exit',command=exit_win,font=font2)
exit_btn.pack(side=RIGHT,padx=7)

exit_btn.bind('<Enter>',on_enterexit)
exit_btn.bind('<Leave>',on_leaveexit)

root.mainloop()
