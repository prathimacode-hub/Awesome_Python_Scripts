#################################### Main Script ###############################
# File Name: collision_detection.py
# Date: 14-july-2021
# Author: Victor Swaroop ( @GVictorsd )
#
# This Script contains the main code for the project
#
#################################################################################

import turtle
from Related.myMethods import *

# initialize necessary objects
box = Box([-200, 200, -200, 200])
body1 = Body(2, 20, [50,50], [20,10], [0,-4])
body2 = Body(1, 10, [20,10], [11,5], [0,-4])

# define the turtles
t1 = turtle.Turtle()
t2 = turtle.Turtle()

# draw the container
t1.speed(1)
t1.penup()
t1.goto(box.left(), box.bottom())
t1.pendown()
t1.goto(box.left(), box.top())
t1.goto(box.right(), box.top())
t1.goto(box.right(), box.bottom())
t1.goto(box.left(), box.bottom())

# set turtle to correct shape and size
CURSOR_SIZE = 20
t1.shape('circle')
t1.shapesize(2*body1.radius()/CURSOR_SIZE)
t2.shape('circle')
t2.shapesize(2*body2.radius()/CURSOR_SIZE)
t1.penup()
t2.penup()

while(True):
    # get present position coordinates
    p = body1.position()
    q = body2.position()
    # distance between the centers c1c2
    dist = pow(pow(p[0]-q[0],2) + pow(p[1]-q[1],2), 0.5) 
    if(dist <= body1.radius()+body2.radius()):
        # if c1c2 <= r1+r2  //if balls collide, handle it:
        body1.BallCollision(body2)

    # get updated coordinates
    pos1 = body1.update(box)
    pos2 = body2.update(box)
    # and draw the new frame
    t1.goto(pos1[0], pos1[1])
    t2.goto(pos2[0], pos2[1])


