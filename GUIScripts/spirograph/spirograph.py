import turtle as t
import random

myrtle = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        myrtle.color(random_color())
        myrtle.circle(100)
        myrtle.setheading(myrtle.heading() + size_of_gap)

draw_spirograph(5)

