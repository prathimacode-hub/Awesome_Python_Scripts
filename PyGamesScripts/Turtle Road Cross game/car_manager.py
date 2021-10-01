from turtle import Turtle
import random
COLORS = ["firebrick", "orange", "yellow", "white", "blue", "purple", "cornflower blue", "deep pink"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager():
    def __init__(self):
        self.allcars=[]
        self.carspeed = STARTING_MOVE_DISTANCE

    def create_car(self):  
        random_chance= random.randint(1,6)
        if random_chance ==1:
            newcar= Turtle()
            newcar.shape("square")
            newcar.shapesize(1,2)
            newcar.penup()
            newcar.color(random.choice(COLORS))
            random_y = random.randint(-215, 215)
            newcar.goto(300, random_y)
            self.allcars.append(newcar)

    def move_cars(self):
        for car in self.allcars:
            car.backward(self.carspeed)

    def level_up(self):
        self.carspeed += MOVE_INCREMENT
