import randfacts
s=1
n = int(input('How many interesting facts yo need???\n'))

for i in range(n):
    x = randfacts.getFact(True)
    print(f'{s}..{x}')
    s=s+1
