#The logic of the game is that the turns will keep increasing as
#you press the space bar, and it will reduce its speed and
#stop at a point where you stop pressing the space bar.

from distutils.core import setup
from turtle import *
state = {'turn': 0}
#definning the spinner
def spinner():
    clear()
    angle = state['turn']/10
    right(angle)
    forward(100)
    dot(120, 'red')
    back(100)
    right(120)
    forward(100)
    dot(120, 'brown')
    back(100)
    right(120)
    forward(100)
    dot(120, 'orange')
    back(100)
    right(120)
    update()
#creating the animation
def animate():
    if state['turn']>0:
        state['turn']-=1

    spinner()
    ontimer(animate, 20)
def flick():
    state['turn']+=10

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
width(20)
onkey(flick, 'space')
listen()
animate()
done()