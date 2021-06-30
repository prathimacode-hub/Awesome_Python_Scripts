import random as r
# Points assigned to each letter of the alphabet
POINTS = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
score1 = score2 = 0
# Gives a random letter to the user to start with
print("Enter a word starting with the letter "+ chr(r.randint(65, 90)))
# Get input words from both players
word1 = input("Player 1:")
word2 = input("Player 2:")

# Calculating the score of Player1
# Points given to each letter are irrespective of the case
for i in word1:
    if word1.isupper():
        score1 += POINTS[ord(i) - ord('A')] #ord returns the ASCII value of the letter
    elif word1.islower():
        score1 += POINTS[ord(i) - ord('a')]
#Claculating the score of Player2       
for i in word2:
    if word2.isupper():
        score2 += POINTS[ord(i) - ord('A')] #ord returns the ASCII value of the letter
    elif word2.islower():
        score2 += POINTS[ord(i) - ord('a')]
    
#Prints the winner
if score1 > score2:
    print("Player 1 wins!")
elif score1 < score2 :
    print("Player 2 wins!\n")
elif score1 == score2:
    print("Tie!\n")



    

