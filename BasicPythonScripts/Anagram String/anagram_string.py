#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Script for strings are angram string or not.

string1 = input("enter string-1:")   #user enter string 1 
string2 = input("enter string-2:")   # user enter strung 2

# check length of both string same or not.
if(len(string1) == len(string2)):    
    
    # if length same, sorting both string and check sorting string equal or not.
    if(sorted(string1) == sorted(string2)):   
        print(string1 + " and " + string2 + " are anagram string.")    # if equal then print both string are anagram stirng
    else:
        print(string1 + " and " + string2 + " are not anagram string.") # otherwise print both string are not anagram string
else:
    print(string1 + " and " + string2 + " are not anagram string.") # length not same print both stirng are not anagram string


# In[ ]:




