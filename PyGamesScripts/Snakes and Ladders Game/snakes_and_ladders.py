# importing Image module from Python Imaging Library
from PIL import Image
# importing random module to generate random numbers from 1 to 6 on the dice
import random
# the maximum value on the board above is end
end = 30

# displayBoard() function


def displayBoard():
    img = Image.open(
        "Snakes and Ladders Game/Images/snakes-and-ladders.jpg")
    # To view the image, we need to call the show() function in Image module
    img.show()

# play() function


def play():
    # taking players names as input
    p1_name = input("player1, please enter your name:")
    p2_name = input("player2, please enter your name:")
    # Setting the initial scores of players and number of turns to zero
    # player1 score pp1=0
    pp1 = 0
    # player2 score pp2=0
    pp2 = 0
    # number of turns turn=0
    turn = 0
    while(1):
        # if the number of turns is even, it's player1's turn
        if turn % 2 == 0:
            print(p1_name, ",It's your turn")
            # asking player1 if he wants to continue or quit
            c = int(input("press 1 to continue, 0 to quit: "))
            # Displaying scores and a thank you message if he wants to quit
            if(c == 0):
                print(p1_name, ' ,you scored ', pp1)
                print(p2_name, ' ,you scored ', pp2)
                if(pp1 > pp2):
                    print(p1_name, " is leading by ", (pp1-pp2), " points.")
                else:
                    print(p2_name, " is leading by ", (pp2-pp1), " points.")
                    print("Quitting the game, Thanks for playing.")
                    break
            # else, the program generates a random number from 1 to 6
            # representing a dice is rolled, using randint() function
            dice = random.randint(1, 6)
            print("Dice showed: ", dice)
            # adding the dice points to the player1's score
            pp1 = pp1+dice
            # checking if there is any ladder at the player1's position
            pp1 = checkLadder(pp1)
            # checking if there is any snake at the player1's position
            pp1 = checkSnake(pp1)
            # if the player1's score is exceeding the maximum number on the board,
            # set it to maximum
            if pp1 > end:
                pp1 = end
            print(p1_name, " ,Your score is ", pp1)
            # checking if player1 reached the end of the board
            # if he reached the end, declare player1 as winner! and exit the game
            if(reachedEnd(pp1)):
                print(p1_name, " won by ", (pp1-pp2), " points")
                print("Congratulations! ", p1_name)
                print("Quitting the game, Thanks for playing.")
                break
        else:
            # if the number of turns is odd, it's player2's turn
            print(p2_name, ",It's your turn")
            # asking player2 if he wants to continue or quit
            c = int(input("press 1 to continue, 0 to quit: "))
            # Displaying scores and a thank you message if he wants to quit
            if(c == 0):
                print(p1_name, ' ,you scored ', pp1)
                print(p2_name, ' ,you scored ', pp2)
                if(pp1 > pp2):
                    print(p1_name, " is leading by ", (pp1-pp2), " points.")
                else:
                    print(p2_name, " is leading by ", (pp2-pp1), " points.")
                    print("Quitting the game, Thanks for playing.")
                    break
            # else, the program generates a random number from 1 to 6
            # representing a dice is rolled, using randint() function
            dice = random.randint(1, 6)
            print("Dice showed: ", dice)
            # adding the dice points to the player2's score
            pp2 = pp2+dice
            # checking if there is any ladder at the player2's position
            pp2 = checkLadder(pp2)
            # checking if there is any snake at the player2's position
            pp2 = checkSnake(pp2)
            # if the player2's score is exceeding the maximum number on the board,
            # set it to maximum
            if pp2 > end:
                pp2 = end
            print(p2_name, " ,Your score is ", pp2)
            # checking if player2 reached the end of the board
            # if he reached the end, declare player2 as winner! and exit the game
            if(reachedEnd(pp2)):
                print(p2_name, " won by ", (pp2-pp1), " points")
                print("Congratulations! ", p2_name)
                print("Quitting the game, Thanks for playing.")
                break
        # don't forget to increment the number of turns everytime.
        turn += 1


# checkLadder() function
def checkLadder(points):
    # if player achieves a score of either of the scores among 3, 5, 11, 20
    # he could climb a ladder
    # points are the player scores
    if points == 3:
        print("Hurray ! Ladder")
        return 22
    elif points == 5:
        print("Hurray ! Ladder")
        return 8
    elif points == 11:
        print("Hurray ! Ladder")
        return 26
    elif points == 20:
        print("Hurray ! Ladder")
        return 29
    else:
        return points


# checkSnake() function
def checkSnake(points):
    # points are the scores of players
    # if the player reaches either of the scores as 17, 19, 21, 27
    # a snake is encountered and score is decreased
    if points == 17:
        print("Oops ! Snake")
        return 4
    elif points == 19:
        print("Oops ! Snake")
        return 7
    elif points == 21:
        print("Oops ! Snake")
        return 9
    elif points == 27:
        print("Oops ! Snake")
        return 1
    else:
        return points


# reachedEnd method
def reachedEnd(points):
    if points == end:
        return True
    else:
        return False


# calling displayBoard() and play() functions
displayBoard()

play()
