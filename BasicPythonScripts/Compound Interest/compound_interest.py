# Calculating Compound interest

print('How many years will you be saving?') 
years = int(input('Enter years: '))

print('\nHow much money is currently in your account?') 
principal = float(input('Enter current amount in account: '))

print('\nHow much money do you plan on invest in monthly?') 
monthly_invest = float(input('Enter amount: '))

print('\nWhat do you estimate will be the yearly interest of this investment?') 
interest=float (input('Enter interest in decimal numbers (e.g. 10% = 0.1): '))

print(' ')

# We are simply multiplying the Monthly investment to 1 Year(12 Month)
monthly_invest = monthly_invest * 12
final_amount = 0

#Using loop we want to calculate the CI per year till the saving year is reached by the user.
for i in range(0, years):
    if final_amount == 0:
        final_amount = principal
    #Here we Calculate the amount which is (monthly_invest) * (1 + interest) which gives and amount per year
    final_amount = (final_amount + monthly_invest) * (1 + interest)
    
print('This is how much money you would have in your account after {} years: '.format(years) + str(final_amount))
