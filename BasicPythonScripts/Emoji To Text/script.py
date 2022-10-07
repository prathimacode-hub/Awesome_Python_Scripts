import unicodedata

# Get the emoji from user input as a string
em = input('Enter Emoji : ')

# return the encoded name of the emoji from the metadata
print(unicodedata.name(em[0]))
