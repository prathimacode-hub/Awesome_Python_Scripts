#take user input here
# The Amount of money you have -----
money = int(input('Enter amount of money you have : ')) 

# The Price of each chocolate -----
price = int(input('Enter price of each chocolate : '))  

# Number of wrapper, in exchange of which you will get the chocolates -----
wrappers = int(input('Enter for how many wrappers, shopkeeper gives you chocolates : ')) 

#Number of chocolates you will get in exchange of wrappers -----
choco_wrapper = int(input('Enter how many chocolates , will shopkeeper gives you for given number of wrappers : '))

# The Algorithm 
chocolates = money//price          # Number of chocolates you will get with your money and price of chocolates
number_of_wrappers = money//price  # Number of wrappers when you will buy chocolates

# Calculation for Extra chocolates in exchange of wrappers -----
while number_of_wrappers//wrappers!=0:
    chocolates = chocolates + ((number_of_wrappers//wrappers)*choco_wrapper)
    number_of_wrappers = ((number_of_wrappers//wrappers)*choco_wrapper) + (number_of_wrappers%wrappers)

# Finally you get Extra Chocolates : 

print('---------------------------------------------------------------------------------------------------------')
print('Yay you got',chocolates,'Chocolates 🍫🍫 . Enjoy')