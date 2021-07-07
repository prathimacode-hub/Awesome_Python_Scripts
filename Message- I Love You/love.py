from turtle import color, back, left, forward, right, exitonclick
import turtle
color("black")
back(450)
color("orange")

# let us start creating the words
left(90)
forward(100)
back(100)
right(90)
color("black")
forward(100)
left(90)
color("orange")
forward(100)
back(100)
right(90)

#we are adjusting the cursor in such a way where in the cursor will write i love you in the given code.

color("orange")
forward(50)
color("black")
forward(50)
color("orange")
forward(50)
back(50)
left(90)
forward(100)
right(90)
forward(50)
right(90)
forward(100)
left(90)
color("black")
forward(100)
color("orange")
left(120)
forward(110)
back(110)
right(60)
forward(110)
back(110)
right(60)
color("black")
forward(100)

# if we observe carefully, there are only two colors, one is black other one is orange.
color("orange")
forward(50)
back(50)
left(90)
forward(100)
right(90)
forward(50)
back(50)
right(90)
forward(50)
left(90)
forward(50)
back(50)
right(90)
forward(50)
left(90)
forward(50)
color("black")
forward(150)
color("orange")
left(90)
forward(50)
left(45)
forward(75)
back(75)
right(90)
forward(75)
back(75)
left(45)

# we are at the middle of the word
back(50)
right(90)
color("black")
forward(100)
color("orange")
forward(50)
back(50)
left(90)
forward(100)
right(90)
forward(50)
right(90)
forward(100)
left(90)
color("black")
forward(100)
color("orange")
back(50)
left(90)
forward(100)
back(100)
right(90)
forward(50)
left(90)
forward(107)
color("black")
pen = turtle.Turtle() 

# we are done with the cursor part.
def curve():
    
    for i in range(200): 
        pen.right(1) 
        pen.forward(1) 

# what if there is a heart in between the 3 words ??
def heart():

#interesting right? now, let us give the points where we need the heart symbol to be visible
    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(250)
    curve()
    pen.left(120)
    curve()
    pen.forward(112)
    pen.end_fill()

heart()

def txt(x="" ):

    pen.up()
    pen.setpos(-70, 60)
    pen.down()
    pen.color('lightgreen')
    pen.write(x, font=("Verdana", 10, ""))


# that's it we are done.
txt()

pen.ht()
exitonclick()
