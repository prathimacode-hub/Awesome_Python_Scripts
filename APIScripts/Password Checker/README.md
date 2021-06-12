# Password Checker
## Short Description:
**Imported Libraries:**
- requests
- hashlib
- sys


**Purpose:**
It's an actual tool that I use day to day for security reasons, not just any silly dumb password checker. This is legitimately going to be the most secure way for you to check if your password has been ever pawned or been under hacker radars.


**Steps Taken:**
- Used a paid API of https://haveibeenpwned.com/
- Implemented SHA1 algorithm for hashing and security
- Used Sys module to directly run from CLI
- Returned the number of times a password keyword has been compromised as output and displayed a safe message for the keywords that were not pawned.

------------
## Setup Instructions:
1. Open Command Line terminal
2. Type the command: 'python password-checker.py {your password}'
3. Hit Enter and see the magic!!

------------

## Output:
![Sample Output](/Images/Output.png)


------------

## Author:
RISHAV KUMAR
