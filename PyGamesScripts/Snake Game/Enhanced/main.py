# import class and library
from turtle import Screen  
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# setupping screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# creating snake player from snake class
snake_player = Snake()
food = Food()
scoreboard = Scoreboard()

# listening to keyboard event
screen.listen()
screen.onkey(snake_player.up,"Up")
screen.onkey(snake_player.down,"Down")
screen.onkey(snake_player.left,"Left")
screen.onkey(snake_player.right,"Right")


# check for game status
game_over = False

# to game keep running
while not game_over:
    screen.update()
#     create delay in game
    time.sleep(0.1)
#     calling move function
    snake_player.move()
    
#     check snake eat food
    if snake_player.snakes_bit[0].distance(food) < 15:
        food.refresh()
        scoreboard.incr_score()
        print(snake_player.snakes_bit[0].position() ,"player at")
        print(snake_player.snakes_bit[-1].position() ,"last player at")
        snake_player.extend()

#     detect collision with wall
    if snake_player.snakes_bit[0].xcor() > 280 or snake_player.snakes_bit[0].xcor() < -280 or snake_player.snakes_bit[0].ycor() > 280 or snake_player.snakes_bit[0].ycor() < -280:

        scoreboard.reset()
        snake_player.reset()

#         DETECT COLLISION WITH TAIL
    for bit in snake_player.snakes_bit:
        if bit == snake_player.snakes_bit[0]:
            pass
        elif snake_player.snakes_bit[0].distance(bit) < 10:
            scoreboard.reset()
            snake_player.reset()


screen.exitonclick()
