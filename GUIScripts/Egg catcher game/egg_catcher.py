
#import the necessary modules
from itertools import cycle
from random import randrange
from tkinter import Tk , Canvas , messagebox , font

#set the width and height of the canvas
canvas_width = 800
canvas_height = 400

#set the interface
win = Tk()
#passing the attributes to canvas
c = Canvas(win , width = canvas_width ,  height = canvas_height , background = 'deep sky blue')

#creating shapes (rectangle for grass and oval for sun) and setting the attributes
c.create_rectangle(-5, canvas_height - 100 , canvas_width + 5 , canvas_height + 5 , fill='sea green', width=0)
c.create_oval(-80,-80,120,120,fill='orange' , width=0)
c.pack()

# creating the list of colors for eggs
color_cycle = cycle(['light blue' , 'light pink' , 'light yellow','light green' , 'red', 'blue' , 'green','black'])

#setting the width,height,score,speed etc.. for the falling egg
egg_width = 45
egg_height = 55
egg_score = 10
egg_speed = 500
egg_interval = 4000
difficulty_factor = 0.95

#setting the color,width,height,start positions etc.. for the egg catcher
catcher_color = 'blue'
catcher_width = 100
catcher_height = 100
catcher_start_x = canvas_width / 2 - catcher_width / 2
catcher_start_y = canvas_height -catcher_height - 20
catcher_start_x2 = catcher_start_x + catcher_width
catcher_start_y2 = catcher_start_y + catcher_height

#creating the catcher in arc shape and passing the attributes
catcher = c.create_arc(catcher_start_x ,catcher_start_y ,catcher_start_x2,catcher_start_y2 , start=200 , extent = 140 , style='arc' , outline=catcher_color , width=3)

#initialize score and create text for displaying score
score = 0
score_text = c.create_text(10,10,anchor='nw' , font=('Arial',18,'bold'),fill='darkblue',text='Score : ' + str(score))


#initialize lives and create text for displaying lives
lives_remaning = 3
lives_text = c.create_text(canvas_width-10,10,anchor='ne' , font=('Arial',18,'bold'),fill='darkblue',text='Lives : ' + str(lives_remaning))

#creating list for eggs
eggs = []

#function to create eggs for a particular interval of time at different positions
def create_eggs():
    x = randrange(10,740)
    y = 40
    new_egg = c.create_oval(x,y,x+egg_width,y+egg_height,fill=next(color_cycle),width=0)
    eggs.append(new_egg)
    win.after(egg_interval,create_eggs)

#This function is to make the eggs move(fall from top)
def move_eggs():
    for egg in eggs:
        (egg_x,egg_y,egg_x2,egg_y2) = c.coords(egg)
        c.move(egg,0,10)
        if egg_y2 > canvas_height:
            egg_dropped(egg)
    win.after(egg_speed,move_eggs)


#if a egg is dropped then remove it from the list and reduce the life
def egg_dropped(egg):
    eggs.remove(egg)
    c.delete(egg)
    lose_a_life()
    #if lives is 0 show game over
    if lives_remaning == 0:
        messagebox.showinfo('GAME OVER!' , 'Final Score : ' + str(score))
        win.destroy()

#fuction for reducing lives score
def lose_a_life():
    global lives_remaning
    lives_remaning -= 1
    c.itemconfigure(lives_text , text='Lives : ' + str(lives_remaning))

#function to check whether the egg is catched
def catch_check():
    (catcher_x,catcher_y,catcher_x2,catcher_y2) = c.coords(catcher)
    for egg in eggs:
        (egg_x,egg_y,egg_x2,egg_y2) = c.coords(egg)
        #checks whether the egg falls within the boundary of the catcher
        if catcher_x < egg_x and egg_x2  < catcher_x2 and catcher_y2 - egg_y2 < 40:
            eggs.remove(egg)
            c.delete(egg)
            increase_score(egg_score)  #if yes increase the score
    win.after(100,catch_check)

#function for increasing the points speed and interval
def increase_score(points):
    global score , egg_speed , egg_interval
    score += points
    egg_speed = int(egg_speed * difficulty_factor)
    egg_interval = int(egg_interval * difficulty_factor)
    c.itemconfigure(score_text , text='Score : ' + str(score))


#imagine start=0 end=canvas-width
#function to move the egg catcher left
def move_left(event):
    (x1,y1,x2,y2) = c.coords(catcher)
    #catcher can be moved left only if the x-cordinate is greater than 0
    if x1 > 0:
        c.move(catcher,-20,0) 

#function to move the egg catcher right
def move_right(event):
    (x1,y1,x2,y2) = c.coords(catcher)
    #catcher can be moved right only if the x-cordinate is lesser than canvas width
    if x2 < canvas_width:
        c.move(catcher,20,0)

#setting the keyboard keys for moving catcher left and right
c.bind('<Left>' , move_left)
c.bind('<Right>' , move_right)
c.focus_set()

#for every 1000 milliseconds these functions are performed
win.after(1000,create_eggs)
win.after(1000,move_eggs)
win.after(1000,catch_check)


