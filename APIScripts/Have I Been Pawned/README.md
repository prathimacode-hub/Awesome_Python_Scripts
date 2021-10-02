# Are You Pawned!

## Aim
A user can check there password pawned or not and how many times it pawned. This python script uses "**haveibeenpwned API V3**"  

## Installation

No packages or modules to be install :)

## Setup Instructions

1. Have Python 3.x setup in the system 
2. Run the code using the command

    ```
      python are_you_pawned.py
    ```
   and obtain the Output

## Source
### [API Documentation](https://haveibeenpwned.com/API/v3)
#### Example API request : 
`https://api.pwnedpasswords.com/range/{first 5 hash chars}`

Your password is converted to hash SHA-1 and only first 5 character of hash are send as params
##  Workflow of the Program
1. The python script will be asking user to input the password
2. While typing the script will not show the character it will just masked the password character
3. After typing password ,press enter and obtain the output.

**program asking for input**
```bash
Password:
```
**if your password is pwned! this output will be shown**
```bash
Oh No - pwned! This Password has been seen 4 times before
```
**Not pwned!**
```bash
Good news — no pwnage found!
```
## Disclaimer
This password wasn't found in any of the Pwned Passwords loaded into "**haveibeenpwned Datasets**". That doesn't necessarily mean it's a good password, merely that it's not indexed in the database of "**haveibeenpwned**".All data is fetch from the API through GET request.
## Author
Rushi Patel :)
