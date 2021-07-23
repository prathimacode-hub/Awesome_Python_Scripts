# snake player class
from turtle import Turtle

MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.snakes_bit = []
        self.create_snake()

    def create_snake(self):
        for i in range(3):
            snake = Turtle(shape="square")
            snake.color("white")
            snake.penup()
            snake.goto(x=-20 * i, y=0)
            self.snakes_bit.append(snake)
    
#     reset snake player when game over
    def reset(self):
        for bit in self.snakes_bit:
            bit.goto(1000,1000)
        self.snakes_bit.clear()

        self.create_snake()

    
    def move(self):
        for current in range(len(self.snakes_bit) - 1, 0, -1):
            new_x = self.snakes_bit[current - 1].xcor()
            new_y = self.snakes_bit[current - 1].ycor()
            self.snakes_bit[current].goto(new_x, new_y)
        self.snakes_bit[0].forward(MOVE_DISTANCE)

#   extend player when rat food
    def extend(self):
        #     add new bit
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.goto(self.snakes_bit[-1].position())
        print("adding at",self.snakes_bit[-1].position())
        self.snakes_bit.append(snake)

#   handle movement
    def up(self):
        if self.snakes_bit[0].heading() != 270:
            self.snakes_bit[0].setheading(90)

    def down(self):
        if self.snakes_bit[0].heading() != 90:
            self.snakes_bit[0].setheading(270)

    def left(self):
        if self.snakes_bit[0].heading() != 0:
            self.snakes_bit[0].setheading(180)

    def right(self):
        if self.snakes_bit[0].heading() != 180:
            self.snakes_bit[0].setheading(0)
