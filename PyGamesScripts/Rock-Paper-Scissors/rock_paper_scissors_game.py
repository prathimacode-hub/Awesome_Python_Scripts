import random


def rock_paper_scissor(userPoint, comPoint, chances):
    # This while loop continue to till chances is leaser than 
    while(chances < 10):
        randomChoice = random.choice(lst)
        userGuess = str(input("Rock, Paper, scissors:\n"))
        # Computer wins condition
        if userGuess.lower() == "r" and randomChoice == "paper":
            print(f"Computer win!\n{'-'*46}\n")
            comPoint += 1
            chances += 1
        elif userGuess.lower() == "p" and randomChoice == "scissors":
            print(f"Computer win!\n{'-'*46}\n")
            comPoint += 1
            chances += 1
        elif userGuess.lower() == "s" and randomChoice == "rock":
            print(f"Computer win!\n{'-'*46}\n")
            comPoint += 1
            chances += 1
        # User wins condition
        elif randomChoice == "rock" and userGuess.lower() == "p":
            print(f"You win!\n{'-'*46}\n")
            userPoint += 1
            chances += 1
        elif randomChoice == "paper" and userGuess.lower() == "s":
            print(f"You win!\n{'-'*46}\n")
            userPoint += 1
            chances += 1
        elif randomChoice == "scissors" and userGuess.lower() == "r":
            print(f"You win!\n{'-'*46}\n")
            userPoint += 1
            chances += 1
        # Draw situation
        elif (randomChoice == "rock" and userGuess == "r") or (randomChoice == "paper" and userGuess == "p") or (randomChoice == "scissors" and userGuess == "s"):
            print(f"It's a tie!\n{'-'*46}\n")
            chances += 1

    if userPoint > comPoint:
        print(
            f"#. User Point is: {userPoint}\n#. Computer Point is: {comPoint}\n")
        print(f"You won!! this game.")
    elif comPoint > userPoint:
        print(
            f"#. User Point is: {userPoint}\n#. Computer Point is: {comPoint}\n")
        print(f"Computer won!! this game.\n")
    else:
        print(
            f"#. User Point is: {userPoint}\n#. Computer Point is: {comPoint}\n")
        print("#. It's tie!")


if __name__ == "__main__":
    # This loop is for if user wants to play again or wants to exit the game
    while(True):
        print("1. Press 'r' for rock\n2. Press 'p' for paper\n3. Press 's' forscissors\n")
        lst = ["rock", "paper", "scissors"]
        chances = 0
        comPoint = 0
        userPoint = 0
        rock_paper_scissor(userPoint, comPoint, chances)

        ask = input("Press any key to continue and e to exit:\n")
        if ask.lower() == 'e':
            break
