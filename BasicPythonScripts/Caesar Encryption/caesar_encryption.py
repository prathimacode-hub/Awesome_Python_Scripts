import string

plain_text = "ebiil tloia"
shift = 3 #this is the number by which the alphabets are shifted

alphabet = string.ascii_lowercase
shifted = alphabet[shift:]+alphabet[:shift]
table = str.maketrans(alphabet, shifted)

encrypted = plain_text.translate(table)

print(encrypted)