from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level =1
        self.goto(-290, 230)
        self.update_scoreboard()
        

    def increase_level(self) :
        self.level+=1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.color("black")
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font= FONT)    