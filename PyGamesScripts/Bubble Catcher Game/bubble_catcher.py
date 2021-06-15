
'''

MODULE IMPORTED :
1.) from intertools imported cycle , to create the bubbkes in cycle
2.) form random imported randrange , to create some randomness on the bubble coming from the top
3.) from tkinter imported Tk , Canvas , messagebox , font , which we used to create gui window and adding styles to it

FUNCTION DEFINED :
1.) create_bubbles() - creates the shape and size of bubble which are dropping from top
2.) move_bubbles() - defined to move the bubble to the downward direction
3.) bubble_dropped(bubble) - defined to drop the bubble from top positon
4.) lose_a_life() - defined to decrease the lives of the player by one if player fails to catch the bubble
5.) catch_check() - defined to check if the player has caught the bubble or not
6.) increase_score(points) - if bubbles is caught bu the player, then this function increases the score by 10 points
7.) move_left(event) - defined to make the catcher to be moved left
8.) move_right(event) - defined to make the catcher to be moved right

'''

from itertools import cycle # we require this library to get different color of bubbles
from random import randrange
from tkinter import Tk , Canvas , messagebox , font
from PIL import ImageTk

canvas_width = 750
canvas_height = 430

frame = Tk() # frame created named win
frame.title("Bubble Catcher")
c = Canvas(frame , width = canvas_width ,  height = canvas_height , background = 'gray')
# c.create_rectangle(-5, canvas_height - 100 , canvas_width + 5 , canvas_height + 5 , fill='sea green', width=0)
# c.create_polygon(-80,-80,120,120,fill='orange' , width=0)

image = ImageTk.PhotoImage(file = "images/bgimage.jpg")
c.create_image(380, 215, image = image)
c.pack()

# creafed list of all th possible color for bubbles
color_cycle = cycle(['light blue' , 'light pink' , 'light yellow','light green' , 'red', 'blue' , 'green','black'])

# defining all the variables needed for bubble
bubble_width = 45
bubble_height = 55
bubble_score = 10 # on catching each bubble, how much increment will be there
bubble_speed = 100
bubble_interval = 4000
difficulty_factor = 0.95

# defining all the variables needed for catcher
catcher_color = 'red'
catcher_width = 100
catcher_height = 80
catcher_start_x = canvas_width / 2 - catcher_width / 2
catcher_start_y = canvas_height -catcher_height - 20
catcher_start_x2 = catcher_start_x + catcher_width
catcher_start_y2 = catcher_start_y + catcher_height

# created a catcher in shape of arc to catch the bubble
catcher = c.create_arc(catcher_start_x ,catcher_start_y ,catcher_start_x2,catcher_start_y2 , start=200 , extent = 140 , style='arc' , outline=catcher_color , width=10)

# variable defined for storing score, initialized with 0
score = 0
# created text for score
score_text = c.create_text(10,10,anchor='nw' , font=('Arial',28,'bold'),fill='darkgreen',text='SCORE : ' + str(score))

# added variable lives_remaning, to gives the players the specific no lives
lives_remaning = 3
# created text for lives
lives_text = c.create_text(canvas_width-10,10,anchor='ne' , font=('Arial',28,'bold'),fill='darkgreen',text='LIVES : ' + str(lives_remaning))

# list created to store the bubbles
bubbles = []

# function defined to create bubbles
def create_bubbles():
    x = randrange(10,740) # randrange function is used from module random, to generate randomness
    y = 40
    new_bubble = c.create_oval(x,y,x+bubble_width,y+bubble_height,fill=next(color_cycle),width=0)
    bubbles.append(new_bubble)
    frame.after(bubble_interval,create_bubbles)

# function defined to move the bubbles
def move_bubbles():
    for bubble in bubbles:
        (bubble_x,bubble_y,bubble_x2,bubble_y2) = c.coords(bubble)
        c.move(bubble,0,10)
        if bubble_y2 > canvas_height:
            bubble_dropped(bubble)
    frame.after(bubble_speed,move_bubbles)

# function defined to drop the bubble from the top position
def bubble_dropped(bubble):
    bubbles.remove(bubble)
    c.delete(bubble)
    lose_a_life()
    if lives_remaning == 0: # if ives = 0, then we show gameover dialog box
        messagebox.showinfo('GAME OVER!' , 'Final Score : ' + str(score) + '\nBubble Caught : ' + str(int(score/10)));
        frame.destroy()

# function defined to notify the player that he loses one life when unable to catch the bubble
def lose_a_life():
    global lives_remaning
    lives_remaning -= 1
    c.itemconfigure(lives_text , text='LIVES : ' + str(lives_remaning))

# function defined to check whether player has catched the bubble or not
def catch_check():
    (catcher_x,catcher_y,catcher_x2,catcher_y2) = c.coords(catcher)
    for bubble in bubbles:
        (bubble_x,bubble_y,bubble_x2,bubble_y2) = c.coords(bubble)
        if catcher_x < bubble_x and bubble_x2  < catcher_x2 and catcher_y2 - bubble_y2 < 40:
            bubbles.remove(bubble)
            c.delete(bubble)
            increase_score(bubble_score)
    frame.after(100,catch_check)

# funtion defined to increase the score whenever player catches a bubble
def increase_score(points):
    global score , bubble_speed , bubble_interval
    score += points
    bubble_speed = int(bubble_speed * difficulty_factor)
    bubble_interval = int(bubble_interval * difficulty_factor)
    c.itemconfigure(score_text , text='SCORE : ' + str(score))

# function defined to make the player move the catcher to left
def move_left(event):
    (x1,y1,x2,y2) = c.coords(catcher)
    if x1 > 0:
        c.move(catcher,-20,0)

# function defined to make the player move the catcher to right
def move_right(event):
    (x1,y1,x2,y2) = c.coords(catcher)
    if x2 < canvas_width:
        c.move(catcher,20,0)

# bounding the movement of the catcher so that it can be moved within the width of gui window
c.bind('<Left>' , move_left)
c.bind('<Right>' , move_right)
c.focus_set()

frame.after(1000,create_bubbles)
frame.after(1000,move_bubbles)
frame.after(1000,catch_check)

frame.mainloop()
