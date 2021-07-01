#Password Generator Project

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?")) 
nr_symbols = int(input(f"How many symbols would you like?"))
nr_numbers = int(input(f"How many numbers would you like?"))

for pwd in range(0,nr_letters):
      pwd = print(f"{random.choice(letters)}",end="")

for pwd in range(0,nr_symbols):
      pwd = print(f"{random.choice(symbols)}",end="")

for pwd in range(0,nr_numbers):
      pwd = print(f"{random.choice(numbers)}",end="")

print("\n")

if nr_letters>5 and nr_numbers>3 and nr_symbols>3:
      print("Awesome!, you got a high level password")
else:
      print("Good!, you got your password but try to make it high level password")