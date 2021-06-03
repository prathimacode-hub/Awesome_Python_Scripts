# pong
import os
import turtle

wn = turtle.Screen()
wn.title("Ping-Pong by PRAGYA KHANNA")
wn.bgcolor("purple")
wn.setup(width=800, height=600)
wn.tracer(0)  # stops the window from updating
# game runs faster

# prompt user for names
player1 = turtle.textinput("Personal Detail", "Player 1")
player2 = turtle.textinput("Personal Detail", "Player 2")

# turtle.write("hello")

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.penup()
# ball.goto(0, 0)
ball.dx = 0.5
ball.dy = 0.5

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
# pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))
pen.write("{}: 0  {}: 0".format(player1, player2), align="center", font=("Courier", 24, "normal"))


# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard bindings
wn.listen()  # listen for keyboard input
wn.onkeypress(paddle_a_up, "w")  # up when w is pressed
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()  # every time the loop runs it updates the screen

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking

    # Top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    # Left and right
    if ball.xcor() > 350:
        score_a += 1
        pen.clear()
        pen.write("{}: {}  {}: {}".format(player1, score_a, player2, score_b), align="center",
                  font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -350:
        score_b += 1
        pen.clear()
        pen.write("{}: {}  {}: {}".format(player1, score_a, player2, score_b), align="center",
                  font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
        # Paddle and ball collisions
    if ball.xcor() < -340 and paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1
        os.system("afplay bounce.wav&")

    elif ball.xcor() > 340 and paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
        os.system("afplay bounce.wav&")
