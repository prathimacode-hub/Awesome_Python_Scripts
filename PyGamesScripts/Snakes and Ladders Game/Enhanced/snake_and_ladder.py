# Import required modules

from tkinter import *
import tkinter.simpledialog
import threading

# try to load PIL (Pillow) module if it is available and drop an error if it is not available
try:
    from PIL import ImageTk, Image
    
except:
    print("Python PIL package not found. Please install it to be able load images correctly.")
    
import random
import re

#-----------------------------------------------------------------------------------------------------------------------------------------------------

dice_num = 0

SNAKE_HOLES = [98,78,81,74,62,58,48, 44, 39, 34, 28, 13] # Assign array for snake holes colors in labels

LADDER_BRIDGES = [3, 8, 6, 26, 14, 22, 32, 49,54,64,76,83,86,95] # Assign array for ladder bridges colors in labels

player_1_pos = 0 # set current position

player_moves = 0 # count player moves

player_bites = 0 # count snake bites

player_climb = 0 # count ladder climbs

player_name = "" # player name variable

time_elapsed = 0 # Time holder

p=""

#-----------------------------------------------------------------------------------------------------------------------------------------------------

def randomColor():
    global PlayerMovesLabel
    COLORS = ['red', 'blue', 'yellow', 'pink', 'lightblue', 'steel blue', 'turquoise', 'sandy brown', 'purple',
              'violet red', 'violet', 'maroon', 'tomato', 'orange', 'green yellow','indigo']
    randomColor = random.randint(0, len(COLORS))
    PlayerMovesLabel.config(bg=COLORS[randomColor])


def colorCycle():
    global PlayerMovesLabel, time_elapsed
    # put it inside try, so that if in middle of color switching, main thread is closed, it don't crash
    try:
        
        mytimer = threading.Timer(0.2, colorCycle) # assign our timer
        
        mytimer.daemon = True # link timer to main thread, so that if main thread is closed, timer get stopped
        
        mytimer.start() # start timer

        
        if player_1_pos == 100: # if player is in position 50, start the cycle
            randomColor()
        else:
            
            PlayerMovesLabel.config(bg='cyan') # otherwise keep background white

        time_elapsed = time_elapsed + 1
    except:
        # if error, do nothing. error means program has been exited but thread is running for one more last time.
        return

#-----------------------------------------------------------------------------------------------------------------------------------------------------

def movePlayer():
    # define our global variables so that function can access variables outside of its scope
    global player_1_pos
    global dice_num
    global player_moves
    global player_bites
    global player_climb
    global grid_array
    global PlayerMovesLabel
    global diceRollLabel
    global time_elapsed

    # If player reach goal, reset the counter and colors
    if player_1_pos == 100:
        player_1_pos = 0
        player_moves = 0
        player_1_pos = 0
        player_bites = 0
        player_climb = 0
        grid_array[100 - 1].config(bg="white")
        time_elapsed = 0

    # get our old and new player positions
    old_player_pos = player_1_pos
    new_player_pos = player_1_pos + dice_num

    # if there is snake bite or ladder climb, show feedback message
    additional_message = ""

    # code to take care when move is more than 50
    if new_player_pos > 100:
        new_player_pos = 100 - (new_player_pos - 100)

    # detect if player go to snake hole
    # enumerate snake holes to get their Index ID and
    # go through list of snake holes
    for idx, val in enumerate(SNAKE_HOLES):
        # in our array, first value (even index number) is snake head, and second value (odd index number) is snake tail, detect head
        if idx % 2 == 0:
            
            if new_player_pos == SNAKE_HOLES[idx]: # if it is head, and player is on head
                
                new_player_pos = SNAKE_HOLES[idx + 1] # move player to tail number
                
                player_bites = player_bites + 1 # Update player bites counter
                additional_message = "Bitten | "

    # detect if player go to ladder bottom
    # enumerate ladder bridges to get their Index ID and
    # go through list of ladders
    for idx, val in enumerate(LADDER_BRIDGES):
        # in our array, first value (even index number) is ladder bottom, and second value (odd index number) is ladder top, detect bottom
        if idx % 2 == 0:
            
            if new_player_pos == LADDER_BRIDGES[idx]:  # if it is ladder bottom, and player is on bottom of ladder
                # climb the ladder!
                new_player_pos = LADDER_BRIDGES[idx + 1]
                # Update player climb counter
                player_climb = player_climb + 1
                additional_message = "Climb | "

   
    if old_player_pos > 0:   # change old position to white
        grid_array[old_player_pos - 1].config(bg="white")

    
    grid_array[new_player_pos - 1].config(bg="yellow") # change new position to yellow

    
    player_1_pos = new_player_pos  # apply change to player position variable
    player_moves = player_moves + 1

    if player_1_pos == 100:
        PlayerMovesLabel['text'] = "*WON* Move: " + str(player_moves) + ", Bite: " + str(player_bites) + ", Climb:" + str(player_climb) + " *WON*"
        tkinter.messagebox.showinfo("*WON*",
                                    player_name + " Won the game in " + str(player_moves) + " moves during " + str(int(time_elapsed / 5)) + " seconds!")
    else:
        PlayerMovesLabel['text'] = additional_message + "Move: " + str(player_moves) + ", Bite: " + str(player_bites) + ", Climb:" + str(player_climb)

#-----------------------------------------------------------------------------------------------------------------------------------------------------

# function when Roll button is clicked
def rollTheDice():
    global dice_num
    global diceRollLabel
    
    # get a random number between 1 to 6
    dice_num = random.randint(1, 6)
    
    # write number into label
    diceRollLabel['text'] = player_name + " Rolled: " + str(dice_num)
    
    # move the player!
    movePlayer()

#-----------------------------------------------------------------------------------------------------------------------------------------------------

def createGUI():
    global grid_array
    global PlayerMovesLabel
    global diceRollLabel
    global diceWindow
    global player_name
    global p
    pattern=r".*"

    # create diceWindow
    diceWindow = Tk()

    # Set title for diceWindow
    diceWindow.title("SNAKE & LADDERS")
    
    # Make window not resizable
    diceWindow.resizable(width=False, height=False)
    diceWindow.config(bg='white')
    
    # otherwise just show a label
    RevertLogoImage = Label(diceWindow, text="Snake & Ladder", bg='white', font=("Arial", 30))
    RevertLogoImage.grid(row=0, column=1, columnspan=10)
    
    # create moves indicator label
    PlayerMovesLabel = Label(diceWindow, text="Please enter your name in popup window", bg='white')
    PlayerMovesLabel.grid(row=1, column=1, columnspan=10)

    # Create button for GUI
    btnRoll = Button(diceWindow, text="Roll", command=rollTheDice, width=30)
    
    # show it on screen
    btnRoll.grid(row=3, column=1, columnspan=10)

    # create our board interface define out array of labels first
    grid_array = []
    for y in range(0, 10):
        for x in range(0, 10):
            array_num = ((x + 1) + (y * 10))
            grid_array.append(Label(diceWindow, borderwidth=8, text=array_num))

            # get x and y and put them into new variable to avoid editing original x/y variables which can cause infinite loop
            xx = x
            yy = y

            
            yy = abs(yy - 10) # a simple control to make board-like numbers to position correctly
            
            if not yy % 2: # reverse the numbers if it is not even row
                xx = abs(xx - 9)

            grid_array[array_num - 1].grid(row=(yy + 1) + 4, column=(xx + 1))            
            grid_array[array_num - 1].config(bg='white') # fix problem with windows OS that don't show labels in white color by default
            
            if array_num in SNAKE_HOLES: # take care of snake holes, apply custom colors
                
                if SNAKE_HOLES.index(array_num) % 2 == 0: # if it is even index number, means it is snake head
                    grid_array[array_num - 1].config(fg="red")  # red is for snake head
                    
                else:
                    grid_array[array_num - 1].config(fg="orange") # orange is for snake tail

           
            if array_num in LADDER_BRIDGES:  # take care of ladder bridges, apply custom colors
                
                if LADDER_BRIDGES.index(array_num) % 2 == 0: # if it is even index number, it means it is ladder bottom
                    grid_array[array_num - 1].config(fg="blue")  # blue is ladder bottom
                    
                else:
                    grid_array[array_num - 1].config(fg="lightblue") # blue is ladder top
   
    colorCycle()  # initialize timer

   
    if re.match(pattern,player_name):  # If user cancel promptbox dialog or left name empty, ask again
        p=player_name
        player_name = tkinter.simpledialog.askstring("Player Name", "Please enter your name: ")
        PlayerMovesLabel['text'] = '- Waiting for first Roll -'


    
    diceRollLabel = Label(diceWindow, bg="white", text="Welcome " + player_name + ", Please roll your dice!") # create introduction label
    diceRollLabel.grid(row=2, column=1, columnspan=10)

    
    diceWindow.mainloop() # Establish the window



GUI = threading.Thread(target=createGUI()) # create GUI to start things up
GUI.start()
q=player_moves
Process = threading.Thread(target=createGUI())
Process.start()
w=player_moves

GUI.join()
Process.join()

#-----------------------------------------------------------------------------------------------------------------------------------------------------

if q<w:
    tkinter.messagebox.showinfo("*WON*",  p + " Won the game by " + str(w-q) + " moves")
else:
    tkinter.messagebox.showinfo("*WON*",  player_name + " Won the game by " + str(q-w) + " moves")
