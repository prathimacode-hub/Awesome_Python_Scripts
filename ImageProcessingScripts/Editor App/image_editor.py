# import required modules

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename,asksaveasfilename
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps
import os

#------------------------------------------------------------------------------------------------------------------------------------------

# contrast border thumbnail

root = Tk()
root.title("Rammya's Image Editor")  # name for the window
root.geometry("700x640")   # set size of window
root.configure(bg='magenta')  # background color

#-------------------------------------------------------------------------------------------------------------------------------------------

# create functions

def selected():   # function to select image
    global img_path, img
    img_path = filedialog.askopenfilename(initialdir=os.getcwd())  # path file
    img = Image.open(img_path) # open the file
    img.thumbnail((350, 350))
    #imgg = img.filter(ImageFilter.BoxBlur(0))
    img1 = ImageTk.PhotoImage(img) 
    canvas2.create_image(300, 210, image=img1)  # set image in canvas
    canvas2.image=img1

#-------------------------------------------------------------------------------------------------------------------------------------------
    
def blur(event):  # function to blur the image
    global img_path, img1, imgg
    for m in range(0, v1.get()+1):
            img = Image.open(img_path) 
            img.thumbnail((350, 350))
            imgg = img.filter(ImageFilter.BoxBlur(m))
            img1 = ImageTk.PhotoImage(imgg) 
            canvas2.create_image(300, 210, image=img1)
            canvas2.image=img1
#-------------------------------------------------------------------------------------------------------------------------------------------
            
def brightness(event): # function to brightness the image
    global img_path, img2, img3
    for m in range(0, v2.get()+1):
            img = Image.open(img_path)
            img.thumbnail((350, 350))
            imgg = ImageEnhance.Brightness(img)
            img2 = imgg.enhance(m)
            img3 = ImageTk.PhotoImage(img2)
            canvas2.create_image(300, 210, image=img3)
            canvas2.image=img3

#-------------------------------------------------------------------------------------------------------------------------------------------

def contrast(event): # function to contrast the image
    global img_path, img4, img5
    for m in range(0, v3.get()+1):
            img = Image.open(img_path)
            img.thumbnail((350, 350))
            imgg = ImageEnhance.Contrast(img)
            img4 = imgg.enhance(m)
            img5 = ImageTk.PhotoImage(img4)
            canvas2.create_image(300, 210, image=img5)
            canvas2.image=img5

#-------------------------------------------------------------------------------------------------------------------------------------------

def rotate_image(event):  # function to rotate the image
        global img_path, img6, img7
        img = Image.open(img_path)
        img.thumbnail((350, 350))
        img6 = img.rotate(int(rotate_combo.get()))
        img7 = ImageTk.PhotoImage(img6)
        canvas2.create_image(300, 210, image=img7)
        canvas2.image=img7

#-------------------------------------------------------------------------------------------------------------------------------------------
        
def flip_image(event):  # function to flip flop the image
        global img_path, img8, img9
        img = Image.open(img_path)
        img.thumbnail((350, 350))
        if flip_combo.get() == "FLIP LEFT TO RIGHT":
            img8 = img.transpose(Image.FLIP_LEFT_RIGHT)
        elif flip_combo.get() == "FLIP TOP TO BOTTOM":
            img8 = img.transpose(Image.FLIP_TOP_BOTTOM)
        img9 = ImageTk.PhotoImage(img8)
        canvas2.create_image(300, 210, image=img9)
        canvas2.image=img9

#-------------------------------------------------------------------------------------------------------------------------------------------

def image_border(event):  # function to add border the image
    global img_path, img10, img11
    img = Image.open(img_path)
    img.thumbnail((350, 350))
    img10 = ImageOps.expand(img, border=int(border_combo.get()), fill=95)
    img11 = ImageTk.PhotoImage(img10)
    canvas2.create_image(300, 210, image=img11)
    canvas2.image=img11    
img1 = None
img3 = None
img5 = None
img7 = None
img9 = None
img11 = None

#-------------------------------------------------------------------------------------------------------------------------------------------

def save():  # save the file
    global img_path, imgg, img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11
    #file=None
    ext = img_path.split(".")[-1]
    file=asksaveasfilename(defaultextension =f".{ext}",filetypes=[("All Files","*.*"),("PNG file","*.png"),("jpg file","*.jpg")])
    if file:  # choose the image file to save
            if canvas2.image==img1:
                imgg.save(file)
            elif canvas2.image==img3:
                img2.save(file)
            elif canvas2.image==img5:
                img4.save(file)
            elif canvas2.image==img7:
                img6.save(file)
            elif canvas2.image==img9:
                img8.save(file)
            elif canvas2.image==img11:
                img10.save(file)

#-------------------------------------------------------------------------------------------------------------------------------------------

# create labels, scales and comboboxes

blu = Label(root, text="BLUR ", font=("arial 15 bold"), width=9, anchor='e', bg = 'magenta') 
blu.place(x=15, y=8)
v1 = IntVar()
scale1 = ttk.Scale(root, from_=0, to=10, variable=v1, orient=HORIZONTAL, command=blur) # set the scale for blur
scale1.place(x=150, y=10)

#-------------------------------------------------------------------------------------------------------------------------------------------


bright = Label(root, text="BRIGHTNESS ", font=("arial 15 bold"), bg = 'magenta')  
bright.place(x=8, y=50)
v2 = IntVar()   
scale2 = ttk.Scale(root, from_=0, to=10, variable=v2, orient=HORIZONTAL, command=brightness) # set the scale for brightness
scale2.place(x=150, y=55)

#-------------------------------------------------------------------------------------------------------------------------------------------

contrast = Label(root, text="CONTRAST ", font=("arial 15 bold"),  bg = 'magenta')
contrast.place(x=35, y=92)
v3 = IntVar()   
scale3 = ttk.Scale(root, from_=0, to=10, variable=v3, orient=HORIZONTAL, command=contrast) # set the scale for contrast
scale3.place(x=150, y=100)

#-------------------------------------------------------------------------------------------------------------------------------------------

rotate = Label(root, text="ROTATE ", font=("arial 15 bold"),  bg = 'magenta')
rotate.place(x=370, y=8)
values = [0, 90, 180, 270, 360]   # values for rotate the image by angle
rotate_combo = ttk.Combobox(root, values=values, font=('verdana 10 bold'))
rotate_combo.place(x=460, y=15)
rotate_combo.bind("<<ComboboxSelected>>", rotate_image)

#-------------------------------------------------------------------------------------------------------------------------------------------

flip = Label(root, text="FLIP ", font=("arial 15 bold"),  bg = 'magenta')
flip.place(x=400, y=50)
values1 = ["FLIP LEFT TO RIGHT", "FLIP TOP TO BOTTOM"]  # choosing option for the flip
flip_combo = ttk.Combobox(root, values=values1, font=('verdana 10 bold'))
flip_combo.place(x=460, y=57)
flip_combo.bind("<<ComboboxSelected>>", flip_image)

#-------------------------------------------------------------------------------------------------------------------------------------------

border = Label(root, text="ADD BORDER ", font=("arial 15 bold"),  bg = 'magenta')
border.place(x=320, y=92)
values2 = [i for i in range(10, 45, 5)]  # adding border width to choose
border_combo = ttk.Combobox(root, values=values2, font=("verdana 10 bold"))
border_combo.place(x=460, y=99)
border_combo.bind("<<ComboboxSelected>>", image_border)

#-------------------------------------------------------------------------------------------------------------------------------------------

# create canvas to display image
canvas2 = Canvas(root, width="600", height="420", relief=RIDGE, bd=2)
canvas2.place(x=15, y=150)

#-------------------------------------------------------------------------------------------------------------------------------------------

# create buttons
btn1 = Button(root, text="SELECT IMAGE", bg='black', fg='white', font=('verdana 10 bold'), relief=GROOVE, command=selected) # button for select image
btn1.place(x=100, y=595)
btn2 = Button(root, text="SAVE", width=12, bg='black', fg='white', font=('verdana 10 bold'), relief=GROOVE, command=save) # button for save
btn2.place(x=280, y=595)
btn3 = Button(root, text="EXIT", width=12, bg='black', fg='white', font=('verdana 10 bold'), relief=GROOVE, command=root.destroy) # button for exit
btn3.place(x=460, y=595)
root.mainloop()
