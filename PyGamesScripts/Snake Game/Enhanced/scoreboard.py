# class to handle scorecard
from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.get_high_score()
        self.color("white")
        self.penup()
        self.update_score()
        self.hideturtle()

#   get and store highest score
    def get_high_score(self):
        with open("high_score.txt", mode="r") as file_score:
            self.high_score = int(file_score.read())

    def set_high_score(self):
        with open("high_score.txt", mode="w") as file_score:
            file_score.write(f"{self.score}")

#   increment score           
    def incr_score(self):
        self.score += 1
        self.update_score()


    def update_score(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 18, "normal"))

#   reset score when game over
    def reset(self):
        if self.score > self.high_score:
            self.set_high_score()
            self.high_score = self.score
        self.score = 0
        self.update_score()
