import turtle as t    #keyword, module name, keyword, alias name
import random

myrtle = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_spirograph(size_of_gap):                                #size in between each of the circles
    for _ in range(int(360 / size_of_gap)):                      #start the loop (basically we have 360 degrees in a circle) 360/offset so that we can repeat it and we cant have a floating point number
        myrtle.color(random_color())                             #to have different color each time
        myrtle.circle(100)                                       #turtle's circle with radius 100
        myrtle.setheading(myrtle.heading() + size_of_gap)        #setting it to a new heading that is from the current heading basically to change the tilt of my circle

draw_spirograph(5)                                               #with size 5

