# Koala Speed Clicker

import turtle
from threading import Timer

# set up the screen
t = turtle.Screen()
t.setup(1000, 589)

# set title and background picture
t.title("Speed Clicker Game")
t.bgpic("background1.gif")

# insert image
t.register_shape("koala.gif")
koala = turtle.Turtle()
koala.shape("koala.gif")
koala.speed(0)

# set up the pen or text
pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0, -250)
pen.write(f"Spam click the koala within 5 seconds", align="center", font=("Comic Sans MS", 30, "bold"))

# create a placeholder for number of clicks
clicks = 0


# function to increment the number of clicks
def clicked(x, y):
    global clicks
    clicks += 1
    pen.clear()
    pen.write(f"Koala clicks: {clicks}", align="center", font=("Comic Sans MS", 30, "bold"))


# function to display the total of clicks
def finish():
    global clicks
    koala.speed(0)
    pen.clear()
    if clicks >= 10:
        pen.write(f"Wow, so fast! Total click(s): {clicks}\n Click to Exit", align="center",
                  font=("Comic Sans MS", 30, "bold"))
        t.onscreenclick(end)

    elif clicks < 10:
        pen.write(f"Oof, too slow! Total click(s): {clicks}\n Click to Exit", align="center",
                  font=("Comic Sans MS", 30, "bold"))
        t.onscreenclick(end)


# function to exit or quit the program
def end(x, y):
    quit()


koala.onclick(clicked)  # on click listener
s = Timer(5.0, finish)  # set timer to 5 seconds
s.start()               # start the timer
t.mainloop()            # loop or keep the GUI window
