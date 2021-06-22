from turtle import Turtle, Screen
import random

is_race_on = False  
screen = Screen() #setting screen
screen.title("Turtle Race") #setting title of the game
screen.setup(width=1000, height=700)  #setting screen height
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ") #taking user input to take the bet
colors = ["red", "orange", "yellow", "green", "blue","black"]  #defined colors

y_positions = [-100, -70, -40, -10, 20, 50]  #setting initial position of the turtles y axis
all_turtles = []  #empty list to saving the turtles


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle") #creating turtle shape to turtle        
    new_turtle.penup()              #pen_up for not to draw line in time of moving 
    new_turtle.color(colors[turtle_index])  #setting colors
    new_turtle.goto(x=-450, y=y_positions[turtle_index])  #placing the turtles to positions only y cordinate will be change
    all_turtles.append(new_turtle)  #saving the turtles to the all_turtles list

if user_bet in colors:     #if user_bet's color is there then it will start
    is_race_on = True
else:
    print("Choose correct color!")      

while is_race_on:                #entering to loop for turtles move
    for turtle in all_turtles:    #for all the turtles in all_turtles
        
        if turtle.xcor() > 480:           #480 is the end point for turtles race (finish line)
            is_race_on = False          #ending the race so is_race_on=false
            winning_color = turtle.pencolor()   #getting the turtl's color by using (.pencolor)
            if winning_color == user_bet: #checking if user won or not
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        #Make each turtle move a random amount.
        rand_distance = random.randint(0, 10)    #this will determine turtles  random distance from value is set to (0,10) so the turtles will keep forward randomly
        turtle.forward(rand_distance)        #this (.forward)functiom used to make the turtle go forward according to random distance

screen.exitonclick() #this is inbuilt funcyion of turtle library which will keep hold to screen unless  screen will off when you run the programm in a blink