# import random library to use it in this program.
import random

# Variable num generates and stores a random number between 0 to 100.
num = random.randrange(0, 100)
guessCheck = "wrong"
print("--Welcome to Guess The Number Game--")

# Iterate using while loop
while guessCheck == "wrong":
    res = int(input("Please input a number between 0 and 100:"))
    try:
        val = int(res)
    except ValueError:
        print("This is not a valid integer. Please try again!")
        continue
    # Check whether the user input is high or low than the random number generated.
    if val < num:
        print("This is lower than actual number. Please try again!")
    elif val > num:
        print("This is higher than actual number. Please try again!")
    else:
        # Final result will be printed with this message as the user input matches the random number generated
        print("Hurray! you won, this is the correct number.")
        guessCheck = "correct"
print("Thank you for playing Guess The Number. See you again!")
