from tkinter import *
#making the output grid
window = Tk()
window.geometry("800x700")

#function for different products
def calculate():
	paneer_tikka = e1.get()
	fried_rice = e2.get()
	chowmein = e3.get()
	chilli_potato = e4.get()
	total = ((int(paneer_tikka)*150)+ (int(fried_rice)*120)+ (int(chowmein)*180)+ (int(chilli_potato)*200))
	label12 = Label(window,text=total,font="times 25 bold")
	label12.place(x=200,y=440)

#adjusting all the labels and aligning them properly
label6 = Label(window, text="Hotel Bill",font="times 30 bold")
label6.place(x=180, y=20)

#---------menu option ------

label1 = Label(window, text="MENU", font="times 28 bold")
label1.place(x=550, y=70)

label2 = Label(window,text="Paneer Tikka          Rs.150",font="times 20 bold")
label2.place(x=450, y=120)

label3 = Label(window,text="Fried Rice               Rs.120",font="times 20 bold")
label3.place(x=450, y=150)

label4 = Label(window,text="Chowmein               Rs.180",font="times 20 bold")
label4.place(x=450, y=180)

label5 = Label(window,text="Chilli Potato           Rs.200",font="times 20 bold")
label5.place(x=450, y=210)

label7 = Label(window, text="Select the items", font="times 20 bold")
label7.place(x=80, y=90)

label8 = Label(window, text="Paneer Tikka", font="times 18")
label8.place(x=20,y=140)

e1 = Entry(window)
e1.place(x=20,y=180)

label9 = Label(window, text="Fried Rice", font="times 18")
label9.place(x=250,y=140)

e2 = Entry(window)
e2.place(x=250,y=180)


label10 = Label(window, text="Chowmein", font="times 18")
label10.place(x=20,y=220)

e3 = Entry(window)
e3.place(x=20,y=250)

label11= Label(window, text="Chilli Potato", font="times 18")
label11.place(x=250,y=215)

e4 = Entry(window)
e4.place(x=250,y=250)

b2 = Button(window, text="BILL",font="times 20 bold",width=20,command=calculate)
b2.place(x=100, y=350)

window.mainloop()