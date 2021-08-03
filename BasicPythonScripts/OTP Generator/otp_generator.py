# Write down script for generating 6 digits OTP(One Time Password).

import random as r      # import random library

otp = ""
for i in range(1 , 7):     # generating otp
    otp += str(r.randint(0 , 9))       #generating 6 digit otp using randint function

print("One Time Password(OTP) is",otp)    # print the OTP