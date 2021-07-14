################################### Helper classes ###################################
# File Name: myMethods.py
# Date: 14-july-2021
# Author: Victor Swaroop ( @GVictorsd )
#
# This file contains some helper class definations
# for use in the main script
#
#######################################################################################

class Box:
    '''
    requires a list containing dimensions of the box
    [left, right, bottom, top]
    '''
    def __init__(this, dim):
        this.__dim = dim

    # getters
    def left(this):
        return this.__dim[0]
    def right(this):
        return this.__dim[1]
    def bottom(this):
        return this.__dim[2]
    def top(this):
        return this.__dim[3]

class Body:
    '''
    class defining each ball object
    '''
    def __init__(this, mass, radius, position, velocity, accl):
        # initialize object variables
        this.__mass = mass
        this.__radius = radius
        this.__position = position
        this.__velocity = velocity
        this.__accl = accl

    # getters and setters
    def position(this):
        return this.__position
    def velocity(this):
        return this.__velocity
    def accl(this):
        return this.__accl
    def radius(this):
        return this.__radius
    def mass(this):
        return this.__mass
    def setVelocity(this, velocity):
        this.__velocity = velocity


    def update(this, box, dt=0.1):
        # update metrics even if collision was detected
        # with the box
        this.__velocity[0] = this.__velocity[0] + this.__accl[0]*dt
        this.__velocity[1] = this.__velocity[1] + this.__accl[1]*dt
        this.__position[0] = this.__position[0] + this.__velocity[0]*dt
        this.__position[1] = this.__position[1] + this.__velocity[1]*dt
        this.BoxCollision(box)
        return this.__position


    def BoxCollision(this, box):
        '''
         Detect and handle collision with the box
        '''
        if(this.__position[0]-this.__radius <= box.left()
                or this.__position[0]+this.__radius >= box.right()):
            # if collision with left and right walls:
            this.__velocity[0] = -this.__velocity[0]

        if(this.__position[1]-this.__radius <= box.bottom()
                or this.__position[1]+this.__radius >= box.top()):
            # if collision with bottom and top
            this.__velocity[1] = -this.__velocity[1]


    def BallCollision(this, ball):
        '''
        Detect and handle Collision with other ball
        requires other Body object as parameter
        '''
        # normal vector
        un = []
        un.append(this.position()[0] - ball.position()[0])
        un.append(this.position()[1] - ball.position()[1])

        # unit vectors(normal and tangent)
        mod = pow(un[0]*un[0] + un[1]*un[1] ,0.5)
        un[0] = un[0]/mod
        un[1] = un[1]/mod
        ut = [-un[1], un[0]]

        # initial tangent and normal velocity components
        u1n = this.__dot(un, this.velocity())
        u1t = this.__dot(ut, this.velocity())
        u2n = this.__dot(un, ball.velocity())
        u2t = this.__dot(ut, ball.velocity())

        # final velocity components(scalars)
        v1t = u1t
        v2t = u2t
        v1n = u1n*(this.mass()-ball.mass()) + 2*ball.mass()*u2n / (this.mass() + ball.mass())
        v2n = u2n*(ball.mass()-this.mass()) + 2*this.mass()*u1n / (this.mass() + ball.mass())

        # final velocity components(vectors)
        v1n = [v1n*un[0], v1n*un[1]]
        v1t = [v1t*ut[0], v1t*ut[1]]
        v2n = [v2n*un[0], v2n*un[1]]
        v2t = [v2t*ut[0], v2t*ut[1]]

        # final velocities
        v1 = [v1n[0]+v1t[0], v1n[1]+v1t[1]]
        v2 = [v2n[0]+v2t[0], v2n[1]+v2t[1]]
        this.setVelocity(v1) # update velocity of each object
        ball.setVelocity(v2)

    def __dot(this, a, b):
        '''
        return dot product of two vectors
        '''
        return a[0]*b[0] + a[1]*b[1]
      
