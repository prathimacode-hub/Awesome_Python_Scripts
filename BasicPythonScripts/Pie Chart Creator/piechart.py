# Import libraries
from matplotlib import pyplot as plt
#import numpy as np

lst=[]
# Creating dataset
n = int(input("Enter the number of elements you want in pie chart: "))

# iterating till the range
print("Enter the data headings you want in pie chart: ")
for i in range(0, n):
	ele = (input())
	lst.append(ele)

lst1=[]
# Creating dataset
# iterating till the range
print("Enter the values in number for the data: ")
for i in range(0, n):
	ele1 = int(input())
	lst1.append(ele1)

print("Your pie chart is ready!!")
# Creating plot
fig = plt.figure(figsize =(10, 7))
plt.pie(lst1, labels = lst)

# show plot
plt.show()
