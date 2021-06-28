# A python script to convert string to it's ASCII value
print("Enter a String: ", end="") 
# end="" to make sure it take input from same line 
text = input()
textlength = len(text)
for char in text:
    ascii = ord(char)
    print(char, "\t", ascii)