import turtle                    #Importing turtlr libray
star=turtle.Turtle()  
star.begin_fill()               #It define the starting area , is used to fill the area.
star.fillcolor("yellow")
star.speed(1)                   #This function is used to change the speed
ashu = turtle.Screen()          
ashu.bgcolor("Black")           # It is used to change the background colour 
star.circle(100,steps=3)
star.color("white","yellow")     # this is used to change the colour of curser anf filling colour respectively.
star.circle(100,steps=3)
star.up()                        # It used to up the curse due to which which can change the position which drawing the line .
star.goto(0,1.762*100)           #It is used to change the location 
star.down()                      # This is used to normalize the curser. Now any moment can easily forward or backward will draw a line .
star.fillcolor("yellow")
star.circle(-100,steps=3)       #This is used to drwa circle .It takes 3 arguments radius,extend and steps. Steps divide shape into equals part . Extend is used to divied the part of circle in degree
star.end_fill()   #Upto which filling will be done.
