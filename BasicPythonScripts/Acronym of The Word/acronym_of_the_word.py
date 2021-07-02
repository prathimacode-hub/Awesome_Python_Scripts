def solve(s):
   tokens=s.split(" ")
   string=""
   for word in tokens:
      if (word != "and" ):
         string += str(word[0])
   return string.upper()

print("Don't use special symbols like & ")
k=input("Enter the word whose acronym you want: ")
print("Acronym is:",solve(k))
