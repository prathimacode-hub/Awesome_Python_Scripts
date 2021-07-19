# Password Validator

# Purpose

To verify each password entered by user

# Short description of script

This program validates passwords to match specific rules. A valid password is one that conforms to the following rules:
- Minimum length is 6;
- Maximum length is 12;
- Contains at least an uppercase letter or a lowercase letter
- Contains at least a number;
- Contains at least a special character (such as @,+,£,$,%,*^,etc);
- Doesn't contain space(s).

The libary used in this program is string. The string module contains a number of functions to process standard Python strings:
- string.ascii_letters is used to verify that either an uppercase or lowercase letter is present in the user's password 
- string.digits is used to verify that at least a number is present in the user's password
- string.punctuation is used to verify that punctuation(s) is presnt in the user's password

# Workflow of program

+ The user is asked to enter a password that conforms to some displayed rules;
+ the password is then checked to ensure that all rules were met.

# Setup instructions

To run the script, open a terminal in the folder where your script is located and run the following command :

`python PASSWORD_VALIDATOR.py`

# Sample use of the script

![alt text](https://github.com/Mannuel25/Awesome_Python_Scripts/blob/main/BasicPythonScripts/Password%20Validator/screenshot_1.png)

![alt text](https://github.com/Mannuel25/Awesome_Python_Scripts/blob/main/BasicPythonScripts/Password%20Validator/screenshot_2.png)

![alt text](https://github.com/Mannuel25/Awesome_Python_Scripts/blob/main/BasicPythonScripts/Password%20Validator/screenshot_3.png)

# Author's name

[Tanimowo Emmanuel](https://github.com/Mannuel25)
