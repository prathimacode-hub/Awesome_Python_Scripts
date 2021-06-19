

from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import tkinter.messagebox as mbox # for displaying the dialog box
import pyglet

#Create splash screen
animation=pyglet.image.load_animation('Images/splash.gif')
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

pyglet.clock.schedule_once(close,5.0)

pyglet.app.run()

# Main Window & Configuration
window = tk.Tk() # created a tkinter gui window frame
window.title("ZODIAC SIGNS") # title given is "DICTIONARY"
window.geometry('1000x700')

# defined exit_win function, to show a exit dialog box when tried to exit
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

# to reset the value
def set_dob():
    if mbox.askokcancel("Reset", "Do you want to reset?"):
        date_var.set(1)
        month_var.set(1)
        year_var.set("Non Leap")


def get_zodiac_sign():
    date = date_var.get()
    month = month_var.get()
    year = year_var.get()

    valid = True
    if(year=='Leap'):
        if(month==2 and date>29) or (month==4 and date>30) or (month==6 and date>30) or (month==8 and date>30) or (month==9 and date>30) or (month==11 and date>30):
            valid = False
    else:
        if (month == 2 and date > 28) or (month == 4 and date > 30) or (month == 6 and date > 30) or (month == 8 and date > 30) or (month == 9 and date > 30) or (month == 11 and date > 30):
            valid = False


    if(valid):
        path=''
        if(month==3 and date>=21) or (month==4 and date<=19):
            path = 'Images/aries.gif'
            f1 = Frame(window, width=1000, height=700)
            f1.propagate(0)
            f1.pack(side='top')

            c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
            c1.pack()
            p1 = PhotoImage(file=path)
            c1.create_image(400, 10, image=p1, anchor="nw")
            w1 = Canvas(window)
            w1.p1 = p1

            zodiac_name = Label(f1, text='ARIES', font=("Arial", 35),fg="magenta")
            zodiac_name.place(x=50, y=150)

            info = "ARIES : The Ram -- March 21 - April 19\n  Those born under the Aries zodiac sign often have an exciting and enthusiastic energy. They often seek new and challenging adventures that can push their limits. They are driven, ambitious and curious, and aries tends to have a strong sense of justice. They love competition, in all its forms. They are generally quite optimistic, and they love being placed in leadership positions."
            zodiac_info = tk.Text(f1, height=10, width=80, font=("Arial", 15), bg="light yellow", fg="brown",borderwidth=3, relief="solid")
            zodiac_info.place(x=50, y = 430)
            zodiac_info.insert(END, info)

        elif (month == 4 and date >= 20) or (month == 5 and date <= 20):
            path = 'Images/taurus.gif'
            f1 = Frame(window, width=1000, height=700)
            f1.propagate(0)
            f1.pack(side='top')

            c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
            c1.pack()
            p1 = PhotoImage(file=path)
            c1.create_image(400, 10, image=p1, anchor="nw")
            w1 = Canvas(window)
            w1.p1 = p1

            zodiac_name = Label(f1, text='TAURUS', font=("Arial", 35), fg="magenta")
            zodiac_name.place(x=50, y=150)

            info = "TAURUS : The Bull -- April 20 - May 20\n  People born under the Taurus zodiac sign are often incredibly dedicated, reliable and dependable. Above all things, they value their sense of security and stability.  After Aries brings its fiery energy, it is Taurus that lays down the foundations and follows through. They tend to be rather stubborn and dislike change. When they settle with a routine that they like, it can take much effort to get them to change. "
            zodiac_info = tk.Text(f1, height=10, width=80, font=("Arial", 15), bg="light yellow", fg="brown",
                                  borderwidth=3, relief="solid")
            zodiac_info.place(x=50, y=430)
            zodiac_info.insert(END, info)

        elif (month == 5 and date >= 21) or (month == 6 and date <= 20):
            path = 'Images/gemini.gif'
            f1 = Frame(window, width=1000, height=700)
            f1.propagate(0)
            f1.pack(side='top')

            c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
            c1.pack()
            p1 = PhotoImage(file=path)
            c1.create_image(400, 10, image=p1, anchor="nw")
            w1 = Canvas(window)
            w1.p1 = p1

            zodiac_name = Label(f1, text='GEMINI', font=("Arial", 35), fg="magenta")
            zodiac_name.place(x=50, y=150)

            info = "GEMINI : The Twins -- May 21 - June 20\n  Those born under the Gemini zodiac sign enjoy socializing and love surrounding themselves with people. They are ruled by the planet Mercury, and so they are never happier than when they are sharing their ideas and communicating with the people around them. They enjoy chit-chat and tend to have expression and communication very high on their list of priorities. Sometimes their love for sharing themselves with others, and their never-ending list of ideas can make them seem nervous, excited, and sometimes even manic."
            zodiac_info = tk.Text(f1, height=10, width=80, font=("Arial", 15), bg="light yellow", fg="brown",
                                  borderwidth=3, relief="solid")
            zodiac_info.place(x=50, y=430)
            zodiac_info.insert(END, info)

        elif (month == 6 and date >= 21) or (month == 7 and date <= 22):
            path = 'Images/cancer.gif'
            f1 = Frame(window, width=1000, height=700)
            f1.propagate(0)
            f1.pack(side='top')

            c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
            c1.pack()
            p1 = PhotoImage(file=path)
            c1.create_image(400, 10, image=p1, anchor="nw")
            w1 = Canvas(window)
            w1.p1 = p1

            zodiac_name = Label(f1, text='CANCER', font=("Arial", 35), fg="magenta")
            zodiac_name.place(x=50, y=150)

            info = "CANCER : The Crab -- June 21 - July 22\n  Those born under the zodiac sign Cancer need to be needed. They have an great desire to feel loved and appreciated in every part of their lives. This is needed so that they can develop a sense of security and identity. To the Cancer zodiac sign, their sense of home is very important to their feeling of safety and comfort. They find it rather difficult to achieve unless they feel safe in their home. They are talented at developing home environments for people that are close to them - in both an emotional and physical sense. "
            zodiac_info = tk.Text(f1, height=10, width=80, font=("Arial", 15), bg="light yellow", fg="brown",
                                  borderwidth=3, relief="solid")
            zodiac_info.place(x=50, y=430)
            zodiac_info.insert(END, info)

        elif (month == 7 and date >= 23) or (month == 8 and date <= 22):
            path = 'Images/leo.gif'
            f1 = Frame(window, width=1000, height=700)
            f1.propagate(0)
            f1.pack(side='top')

            c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
            c1.pack()
            p1 = PhotoImage(file=path)
            c1.create_image(400, 10, image=p1, anchor="nw")
            w1 = Canvas(window)
            w1.p1 = p1

            zodiac_name = Label(f1, text='LEO', font=("Arial", 35), fg="magenta")
            zodiac_name.place(x=50, y=150)

            info = "LEO : The Lion -- July 23 - August 22\n  Leos tend to have almost a royal air about them. Their planetary ruler is the Sun, and so they are talented at bringing warmth, life and light into the relationships that are important to them. Many Leos will have a large group of friends that adore them. They have a kind of natural charisma which often makes other signs gravitate towards them. Like their planetary ruler, Leos love to be at the center of attention and they deeply appreciate compliments and even flattery. Their happy and outgoing attitude towards life makes them pleasurable to be around. "
            zodiac_info = tk.Text(f1, height=10, width=80, font=("Arial", 15), bg="light yellow", fg="brown",
                                  borderwidth=3, relief="solid")
            zodiac_info.place(x=50, y=430)
            zodiac_info.insert(END, info)

        elif (month == 8 and date >= 23) or (month == 9 and date <= 22):
            path = 'Images/virgo.gif'
            f1 = Frame(window, width=1000, height=700)
            f1.propagate(0)
            f1.pack(side='top')

            c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
            c1.pack()
            p1 = PhotoImage(file=path)
            c1.create_image(400, 10, image=p1, anchor="nw")
            w1 = Canvas(window)
            w1.p1 = p1

            zodiac_name = Label(f1, text='VIRGO', font=("Arial", 35), fg="magenta")
            zodiac_name.place(x=50, y=150)

            info = "VIRGO : The Virgin -- August 23 - September 22\n  Those born under the Virgo zodiac sign have capable, organized and analytical minds, which often makes them a pleasure to chat with. Even when they have rather fantastic stories, the charming way they tell them can make those stories convincing. Virgos are curious people, and they have a natural gift for research - whether it comes to assignments, or even people. They also often have great memory and a talent for intuition. They make for excellent team members in both work and social situations. They love to collaborate, although their sometimes critical nature can annoy others when those criticisms are not understood."
            zodiac_info = tk.Text(f1, height=10, width=80, font=("Arial", 15), bg="light yellow", fg="brown",
                                  borderwidth=3, relief="solid")
            zodiac_info.place(x=50, y=430)
            zodiac_info.insert(END, info)

        elif (month == 9 and date >= 23) or (month == 10 and date <= 22):
            path = 'Images/libra.gif'
            f1 = Frame(window, width=1000, height=700)
            f1.propagate(0)
            f1.pack(side='top')

            c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
            c1.pack()
            p1 = PhotoImage(file=path)
            c1.create_image(400, 10, image=p1, anchor="nw")
            w1 = Canvas(window)
            w1.p1 = p1

            zodiac_name = Label(f1, text='LIBRA', font=("Arial", 35), fg="magenta")
            zodiac_name.place(x=50, y=150)

            info = "LIBRA : The Scales -- September 23 - October 22\n  The zodiac sign Libra is thrives when their needs of balance, justice, and stability are met. They are charming creatures that somehow always surround themselves with a sense of beauty and harmony. Admittedly, some of them can go to extremes searching for that harmony - which can make their situations unreasonable or unhealthy. Their ruling planet is Venus meaning that Libras are nurturing, caring, and they can make great defenders of the downtrodden. Sometimes, they can be shy if they find difficulties in coming out of their shell and letting their guard down. Despite their more introverted side they still love a good debate."
            zodiac_info = tk.Text(f1, height=10, width=80, font=("Arial", 15), bg="light yellow", fg="brown",
                                  borderwidth=3, relief="solid")
            zodiac_info.place(x=50, y=430)
            zodiac_info.insert(END, info)

        elif (month == 10 and date >= 23) or (month == 11 and date <= 21):
            path = 'Images/scorpio.gif'
            f1 = Frame(window, width=1000, height=700)
            f1.propagate(0)
            f1.pack(side='top')

            c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
            c1.pack()
            p1 = PhotoImage(file=path)
            c1.create_image(400, 10, image=p1, anchor="nw")
            w1 = Canvas(window)
            w1.p1 = p1

            zodiac_name = Label(f1, text='SCORPIO', font=("Arial", 35), fg="magenta")
            zodiac_name.place(x=50, y=150)

            info = "SCORPIO : The Scorpion -- October 23 - November 21\n  Unfortunately, those born under the Scorpio zodiac sign are often misunderstood. They are quite bold, with intense personalities and feelings that hide underneath their cool exterior. They are capable people that can complete great and massive projects with control and confidence. Their intensity when approaching a situation means that they can surmount almost all obstacles if they can truly put their mind to the task. Many Scorpios have an unshakable focus when they need to call on it. However, they are often secretive, seeming withdrawn and uninterested, when they are actually keenly observing."
            zodiac_info = tk.Text(f1, height=10, width=80, font=("Arial", 15), bg="light yellow", fg="brown",
                                  borderwidth=3, relief="solid")
            zodiac_info.place(x=50, y=430)
            zodiac_info.insert(END, info)

        elif (month == 11 and date >= 22) or (month == 12 and date <= 21):
            path = 'Images/sagittarius.gif'
            f1 = Frame(window, width=1000, height=700)
            f1.propagate(0)
            f1.pack(side='top')

            c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
            c1.pack()
            p1 = PhotoImage(file=path)
            c1.create_image(400, 10, image=p1, anchor="nw")
            w1 = Canvas(window)
            w1.p1 = p1

            zodiac_name = Label(f1, text='SAGITTARIUS', font=("Arial", 35), fg="magenta")
            zodiac_name.place(x=50, y=150)

            info = "SAGITTARIUS : The Centaur -- November 22 - December 21\n  The Sagittarius zodiac sign often gains the reputation of the philosopher among their fellow zodiac signs. They do have a great ability to focus, but this may be surprising since many of them love exploring and wandering the world, tasting all the pleasures of life. From an early age, they must learn how to channel their energy or else they risk stretching themselves out too thin going in too many directions. They often are hasty individuals and lack patience. When they encounter failure they can sometimes make a sudden comeback, much to the surprise of others. While they are loyal friends, they may find it hard to commit as this can run counter to their desire for freedom and expansion. "
            zodiac_info = tk.Text(f1, height=10, width=80, font=("Arial", 15), bg="light yellow", fg="brown",
                                  borderwidth=3, relief="solid")
            zodiac_info.place(x=50, y=430)
            zodiac_info.insert(END, info)

        elif (month == 12 and date >= 22) or (month == 1 and date <= 19):
            path = 'Images/capricorn.gif'
            f1 = Frame(window, width=1000, height=700)
            f1.propagate(0)
            f1.pack(side='top')

            c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
            c1.pack()
            p1 = PhotoImage(file=path)
            c1.create_image(400, 10, image=p1, anchor="nw")
            w1 = Canvas(window)
            w1.p1 = p1

            zodiac_name = Label(f1, text='CAPRICORN', font=("Arial", 35), fg="magenta")
            zodiac_name.place(x=50, y=150)

            info = "CAPRICORN : The Goat -- December 22 - January 19\n  Those born under the Capricorn zodiac sign are talented at applying their keen intelligence and ambition to practical matters.  Stability and order are important to them - and this makes them good organizers. Their goals are often lofty, and they achieve them slowly - but purposefully, and systematically. They are gifted with a sharp intuition, although they can be rather secretive about what they perceive. They are patient with themselves - they have confidence that they can accomplish all their goals if they follow their step-by-step plan. They are responsible people that often take the heavy burden of others - whether willingly, or just because they are so capable. However, they find it difficult to share their own troubles and can struggle with depression if they don't learn how to express their feelings. "
            zodiac_info = tk.Text(f1, height=10, width=80, font=("Arial", 15), bg="light yellow", fg="brown",
                                  borderwidth=3, relief="solid")
            zodiac_info.place(x=50, y=430)
            zodiac_info.insert(END, info)

        elif (month == 1 and date >= 20) or (month == 2 and date <= 18):
            path = 'Images/aquarius.gif'
            f1 = Frame(window, width=1000, height=700)
            f1.propagate(0)
            f1.pack(side='top')

            c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
            c1.pack()
            p1 = PhotoImage(file=path)
            c1.create_image(400, 10, image=p1, anchor="nw")
            w1 = Canvas(window)
            w1.p1 = p1

            zodiac_name = Label(f1, text='AQUARIUS', font=("Arial", 35), fg="magenta")
            zodiac_name.place(x=50, y=150)

            info = "AQUARIUS : The Water Bearer -- January 20 - February 18\n  Aquarius often comes off as an oddball - they have quirky personalities and quietly go about accomplishing their goals in quiet, and unorthodox ways. Oftentimes, just because Aquarius chooses to take the path less traveled, the results of their eccentric methods are surprisingly effective. They are the humanitarians of the zodiac, taking up banners for the greater good of humanity. Many of them are also easy going and their peculiarity alongside their curious nature make them fast friendships. Sometimes, if they don't strive to motivate themselves, they can succumb to laziness. Many are often gifted with a strong sense of art and poetry."
            zodiac_info = tk.Text(f1, height=10, width=80, font=("Arial", 15), bg="light yellow", fg="brown",
                                  borderwidth=3, relief="solid")
            zodiac_info.place(x=50, y=430)
            zodiac_info.insert(END, info)

        elif (month == 2 and date >= 19) or (month == 3 and date <= 20):
            path = 'Images/pisces.gif'
            f1 = Frame(window, width=1000, height=700)
            f1.propagate(0)
            f1.pack(side='top')

            c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
            c1.pack()
            p1 = PhotoImage(file=path)
            c1.create_image(400, 10, image=p1, anchor="nw")
            w1 = Canvas(window)
            w1.p1 = p1

            zodiac_name = Label(f1, text='PISCES', font=("Arial", 35), fg="magenta")
            zodiac_name.place(x=50, y=150)

            info = "PISCES : The Fish -- February 19 - March 20\n  The Pisces zodiac sign are the dreamers and mystics of the zodiac - but you may never know it. Many of them have extremely vivid inner lives - filled with fantasy, magic and wonder. They may find it hard to express that inner life, meaning that many of them are introverts. They are honest, compassionate, and trustworthy but they can sometimes take it too far and be rather gullible. Because of that they can be taken advantage of. Beneath their quiet exterior, Pisces has an intense determination, which helps them transcend any obstacles that come their way."
            zodiac_info = tk.Text(f1, height=10, width=80, font=("Arial", 15), bg="light yellow", fg="brown",
                                  borderwidth=3, relief="solid")
            zodiac_info.place(x=50, y=430)
            zodiac_info.insert(END, info)
    else:
        mbox.showerror("Error", "You have entered invalid D.O.B.")



# starting label
start1 = Label(window, text='ZODIAC SIGNS', font=("Arial", 35),fg="magenta",underline=0)
start1.place(x=350,y=10)

# image on the main window
path = "Images/zodiac.jpg"
# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))
# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image = img)
# The Pack geometry manager packs widgets in rows or columns.
# panel.pack(side = "top", fill = "both", expand = "no")
panel.place(x = 260, y = 80)

# starting label
dob = Label(window, text='Choose Date and Month of your D.O.B.', font=("Arial", 25),fg="brown")
dob.place(x=200,y=380)

# Creating a label for drop down menu date --------------------------------
date_lbl = Label(window, text='Date :', font=("Arial", 25),fg="brown")
date_lbl.place(x=120,y=450)
# siz_lbl.grid(row=1, column=0, pady=10)

# creating the drop down menu button
date_var = tk.IntVar()
# as icon size are really small, we defined the following 7 sizes
date_choices = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
date_menu = OptionMenu(window, date_var, *date_choices)
date_menu.config(font=("Arial", 15), bg = "light green", fg = "blue", borderwidth=3)
date_menu["menu"].config(font=("Arial", 10), bg = "light yellow", fg = "blue")
date_menu.place(x=220, y=450)
date_var.set(1) # size 1 is selected as by default, and we can

# Creating a label for drop down menu month ----------------------------------------------
month_lbl = Label(window, text='Month :', font=("Arial", 25),fg="brown")
month_lbl.place(x=370,y=450)

# creating the drop down menu button
month_var = tk.IntVar()
# as icon size are really small, we defined the following 7 sizes
month_choices = [1,2,3,4,5,6,7,8,9,10,11,12]
month_menu = OptionMenu(window, month_var, *month_choices)
month_menu.config(font=("Arial", 15), bg = "light green", fg = "blue", borderwidth=3)
month_menu["menu"].config(font=("Arial", 10), bg = "light yellow", fg = "blue")
month_menu.place(x=490, y=450)
month_var.set(1) # size 1 is selected as by default, and we can

# Creating a label for drop down menu year ----------------------------------------------
month_lbl = Label(window, text='Year :', font=("Arial", 25),fg="brown")
month_lbl.place(x=620,y=450)

# creating the drop down menu button
year_var = tk.StringVar()
# as icon size are really small, we defined the following 7 sizes
year_choices = ["Leap","Non Leap"]
year_menu = OptionMenu(window, year_var, *year_choices)
year_menu.config(font=("Arial", 15), bg = "light green", fg = "blue", borderwidth=3)
year_menu["menu"].config(font=("Arial", 15), bg = "light yellow", fg = "blue")
year_menu.place(x=720, y=450)
year_var.set("Non Leap") # size 1 is selected as by default, and we can


# button to get the zodiac
zbutton = Button(window,text="ZODIAC",command= get_zodiac_sign,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
zbutton.place(x = 200, y = 550)

# button to reset
resetb = Button(window,text="RESET",command= set_dob,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
resetb.place(x = 430, y = 550)

# button to exit
resetb = Button(window,text="EXIT",command= exit_win,font=("Arial", 20), bg = "red", fg = "blue", borderwidth=3, relief="raised")
resetb.place(x = 650, y = 550)

window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()

