import hashlib
import getpass
import requests

#Get Masked User Password
#password = getpass.getpass()

#Uncomment this to not masked the password
password = input('Password:')

#Making Password text into Hash SHA-1
HASH_SHA1 = hashlib.sha1(str(password).encode('utf-8'))
hash = HASH_SHA1.hexdigest()

#Making a request
URL = "https://api.pwnedpasswords.com/range/{}".format(hash[0:5])
r = requests.get(url=URL)
data = list(str(r.text).split('\n'))

#We can modify this to better Searching alogrithms
bool_pwned = False
for i in data:
    tranform_data = str(i).replace("\r","").split(":")
    if hash.upper()[5::] == tranform_data[0]:
        bool_pwned = True
        break

if bool_pwned:
    print("\nOh No - pwned! This Password has been seen {} times before\n".format(tranform_data[1]))
else:
    print("\nGood news — no pwnage found!\n")

