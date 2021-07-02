#importing randfacts module of python
import randfacts
s=1
#variable n define how many facts needed
n = int(input('How many interesting facts yo need???\n'))

#for loop which give random facts simultaneously
for i in range(n):
    x = randfacts.getFact(True)
    print(f'{s}..{x}')
    s=s+1
