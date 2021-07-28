#!/usr/bin/env python
# coding: utf-8

# In[22]:


# Program to check user entered number is Peterson number or not.

'''A number is said to be a Peterson number if the sum of factorials of each digit of the number is equal to the number itself.
Peterson Numbers: 1, 2, 145, 40585, ... '''

number = int(input("number = "))   # take the input from user
num = number
sum = 0
factorial = [1,1,2,6,24,120,720,5040,40320,362880]     # factotrial of 0 to 9 number

while(num > 0):
    rem = num % 10     # spilt the number in digit
    sum += factorial[rem]     # add with factorial of remainder
    num //= 10            # divide the number

if(sum == number):              # check sum and number is equal or not
    print(str(number) + " is a peterson number")
else:
    print(str(number) + " is not a peterson number")

