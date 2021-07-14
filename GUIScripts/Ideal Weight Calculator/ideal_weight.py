import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter import messagebox as mbox

def clear_results():
    bmi_label.configure(text="")
    robinson['state'] = "normal"
    peterson['state'] = "normal"
    miller['state'] = "normal"
    peterson_val = peterson.get()
    miller_val = miller.get()
    robin_val = robinson.get()
    if(peterson_val!="" and robin_val!="" and miller_val!=""):
        peterson.delete(0, END)
        robinson.delete(0, END)
        miller.delete(0, END)
    else:
        pass

def calculate():
    clear_results()  #Calls Clear_Results function to clear any previous contents in results
    p_age = age.get()
    p_height = height_.get()
    p_weight = weight_.get()
    if(p_age == "" or p_height == "" or p_weight == ""):
        mbox.showerror("Input Error","Details are Incomplete !")
    else:
        try:
            p_age = int(p_age)
            p_height = float(p_height)
            p_weight = float(p_weight)

            inch_to_m = p_height*0.0254

            #For printing BMI measures
            bmi = p_weight//(inch_to_m**2)

            if(bmi<18.5):
                bmi_label.configure(text="BMI: "+str(bmi)+"\nYou are underweight", fg="blue")
            elif(18.5<bmi<=25):
                bmi_label.configure(text="BMI: "+str(bmi) + "\nYou are Normal weight", fg="green")
            elif(25<bmi<=30):
                bmi_label.configure(text="BMI: "+str(bmi) + "\nYou are Overweight", fg="orange")
            else:
                bmi_label.configure(text="BMI: "+str(bmi)+"\nYou are Obese", fg="red")


            var_val = var.get() #To check gender selected is Male or Female
            if var_val == 1: #If Male Selected
                peterson_ans = 2.2 * 22 + 3.5 * 22 * (inch_to_m - 1.5 )
                peterson.insert(END, round(peterson_ans,2))
                peterson['state'] = "disabled"

                miller_ans = 56.2 + 1.41 * (p_height - 60)
                miller.insert(END, round(miller_ans,2))
                miller['state'] = "disabled"

                robinson_ans = 52 + 1.9 * (p_height- 60) #(5*bmi)+(bmi/5)*(p_height-60)
                robinson.insert(END, round(robinson_ans,2))
                robinson['state'] = "disabled"
            else:    #If Female Selected
                peterson_ans = 2.2 * 22 + 3.5 * 22 * (inch_to_m - 1.5)
                peterson.insert(END, round(peterson_ans,2))
                peterson['state'] = "disabled"

                miller_ans = 53.1 + 1.36 * (p_height - 60)
                miller.insert(END, round(miller_ans,2))
                miller['state'] = "disabled"

                robinson_ans = 49 + 1.7 * (p_height - 60)
                robinson.insert(END,round(robinson_ans,2))
                robinson['state'] = "disabled"


        except ValueError: #If values entered are non-numeric
            mbox.showerror("Input Error", "Details are Incorrect !")



##----------GUI STARTS----------##
window = tk.Tk()
window.title("Ideal Weight Calculator ❤")
window.config(bg="#cff2f8")
window.geometry("550x700")

age_lab = Label(window,text="AGE:", bg="#cff2f8")
age_lab['font'] = font.Font(size=15)
age_lab.place(x=15, y=40)
age = Entry(window, bg="white")
age['font'] = font.Font(size=15)
age.place(x=180, y=39, height=30, width=300)

gender_lab = Label(window,text="GENDER:", bg="#cff2f8")
gender_lab['font'] = font.Font(size=15)
gender_lab.place(x=15, y=100)
var = IntVar()
male = Radiobutton(window, text="Male", variable=var, value=1, bg="#cff2f8")
male['font'] = font.Font(size=15)
male.place(x=180, y=99)
female = Radiobutton(window, text="Female", variable=var, value=0, bg="#cff2f8")
female['font'] = font.Font(size=15)
female.place(x=300, y=99)

height_lab = Label(window,text="HEIGHT (inch):", bg="#cff2f8")
height_lab['font'] = font.Font(size=15)
height_lab.place(x=15, y=160)
height_ = Entry(window, bg="white")
height_['font'] = font.Font(size=15)
height_.place(x=180, y=159, height=30, width=300)

weight_lab = Label(window, text="WEIGHT (Kg):", bg="#cff2f8")
weight_lab['font'] = font.Font(size=15)
weight_lab.place(x=15, y=220)
weight_ = Entry(window, bg="white")
weight_['font'] = font.Font(size=15)
weight_.place(x=180, y=219, height=30, width=300)

calc = Button(window, text="Calculate", bg="yellow", command=calculate)
calc.place(x=290, y=275)

##------RESULTS ENCLOSED IN LABEL FRAME-------##
result_frame = LabelFrame(window, text="YOUR IDEAL WEIGHT SHOULD BE:", bg = "#cff2f8",bd=5,width=500,height=350)
result_frame.place(x=25, y=320)

peterson_lab = Label(result_frame, text="Peterson", bg="#cff2f8")
peterson_lab['font'] = font.Font(size=15)
peterson_lab.place(x=15, y=20)
peterson = Entry(result_frame, bg="#faa0c0")
peterson['font'] = font.Font(size=15)
peterson['state'] = "disabled"
peterson.place(x=150, y=16, height=30, width=300)

miller_lab = Label(result_frame, text="Miller", bg="#cff2f8")
miller_lab['font'] = font.Font(size=15)
miller_lab.place(x=15, y=80)
miller = Entry(result_frame, bg="#faa0c0")
miller['font'] = font.Font(size=15)
miller['state'] = "disabled"
miller.place(x=150, y=76, height=30, width=300)

robinson_lab = Label(result_frame, text="Robinson", bg="#cff2f8")
robinson_lab['font'] = font.Font(size=15)
robinson_lab.place(x=15, y=140)
robinson = Entry(result_frame, bg="#faa0c0")
robinson['font'] = font.Font(size=15)
robinson['state'] = "disabled"
robinson.place(x=150, y=136, height=30, width=300)

bmi_label = Label(result_frame, text="", fg="black", bg="#cff2f7")
bmi_label['font'] = font.Font(size=20)
bmi_label.place(x=100, y=200)
##------RESULTS FRAME ENDS HERE------##

##-----GUI ENDS HERE-----##

window.mainloop()