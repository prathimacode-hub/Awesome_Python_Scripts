# File Encryptor and Decryptor

## Aim :

- To successfully encrypt sensitive files with a password.
- To decrypt them later with the password set by the encryptor.
- Do all the steps mentioned above, right from the terminal.

## Purpose :

The purpose of the script is to encrypt sensitive files from the terminal to achieve better security.

## Short description of package/script :

- The script lets you encrypt or decrypt a file.
- To do so, we use the [pycryptodome](https://pycryptodome.readthedocs.io/en/latest/) library.
- The user passes the function and also the file on which the same is to be performed.
- Once the parameters are passed, a password is required to encrypt or decrypt a file (set by the encryptor)
- All passwords are hidden with asterisk using the [pwinput](https://github.com/asweigart/pwinput) library.

## Workflow of the Project :

- When the script is run, it expects few parameters to be passed : function [```-e/-d```] and filename.
- Once the function and filename is defined, the script expects the user to input the password.
- The password along with the filename is passed on to the respective function [```encrypt()/decrypt()```]
- The encrypt function traces the file's path and creates an encrypted file with the password that was passed.
- The encrypted file is stored in the "encrypted" folder which is used by the decrypt function to trace the file.
- Decrypt function checks the input password and the password set earlier and stores the decrypted file in the decrypted folder.

## Setup instructions :

- Install required libraries : ```pip install -r requirements.txt```
- Place your file in the original folder for the script to work on it.
- Encrypt your file : ```python file_encryptor_decryptor.py -e file.extension```
- Decrypt encrypted file : ```python file_encryptor_decryptor.py -d enc-file.extension```

## Output :

![Sample Results](https://i.imgur.com/SgERi2K.png)

## Author(s) :

- [Piyush Mohan](https://github.com/piyushmohan01)
