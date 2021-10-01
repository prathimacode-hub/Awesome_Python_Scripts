import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgpic("bg.png")
screen.title("Cross the road!")
screen.tracer(0)
playert= Player()
car= CarManager()
scoreboard= Scoreboard()
screen.listen()
screen.onkeypress(playert.moveup,"Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_cars()

    #detect collision with car
    for c in car.allcars:
        if c.distance(playert) < 25:
            game_is_on= False
            scoreboard.game_over()
    #detect successful reach to end line
    if playert.ycor() >= 260:
        playert.start_pos()
        car.level_up()
        scoreboard.increase_level()
        


screen.exitonclick()