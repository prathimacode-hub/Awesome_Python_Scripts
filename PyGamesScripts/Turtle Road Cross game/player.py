from turtle import Turtle

STARTING_POSITION = (-60, -270)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.start_pos()

    def start_pos(self):
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def moveup(self):
        newy= self.ycor()+ MOVE_DISTANCE
        self.goto(self.xcor(), newy)   

