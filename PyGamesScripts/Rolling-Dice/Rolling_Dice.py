import random
die1 = int(input("Enter a value from 1 to 6:"))

die2 = int(input("Enter a value from 1 to 6:"))

print(die1, die2)

print(die1 + die2)

if (die1 + die2) %2==0:
  print("You win!")
    
else:
  print("you lost")
   