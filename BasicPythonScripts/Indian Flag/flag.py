import turtle    # Calling Library
flag = turtle.Turtle()
flag.speed(1)    # changing speed
flag.up()
flag.goto(-200,-300)  # changing curser position 
flag.down()
flag.left(90)
flag.begin_fill()    
flag.fillcolor("black")  #chocing color
for i in range(2):
    flag.forward(600)
    flag.right(90)
    flag.forward(10)
    flag.right(90)
flag.end_fill()
flag.right(90)
flag.forward(10)
flag.left(90)
flag.forward(580)
flag.right(90)

# Orange Section of flag
flag.begin_fill()
flag.fillcolor("orange")
flag.forward(200)
flag.right(90)
flag.forward(30)
flag.right(90)
flag.forward(200)
flag.end_fill()

flag.backward(200)
flag.left(90)

# White Section of flag
flag.forward(30)
flag.right(90)
flag.forward(200)

flag.backward(200)
flag.left(90)

# Green section
flag.begin_fill()
flag.fillcolor("Green")
flag.forward(30)
flag.right(90)
flag.forward(200)
flag.right(90)
flag.forward(30)
flag.end_fill()

flag.right(90)
flag.forward(100)
flag.color("#000080")
flag.circle(15)

flag.penup()
flag.left(90)
flag.forward(15)
flag.pendown()

# Drawing 24 spokes.
for i in range (24):
    flag.forward(15)
    flag.backward(15)
    flag.left(15)








