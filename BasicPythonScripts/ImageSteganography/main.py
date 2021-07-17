from cryptosteganography import CryptoSteganography
import getpass
crypto_steganography = CryptoSteganography('')

# Save the encrypted file inside the image
opt = int(input("1. Encode \t 2. Decode \t 3. Quit :: "))

while opt!=3:
    if opt==1:
        msg = input("Enter the message to be hidden: ")
        key = getpass.getpass("Enter secret key: ")
        img = "E:\github\Awesome_Python_Scripts\BasicPythonScripts\ImageSteganography\img.jpeg"
        crypto_steganography.hide(img, 'output1.png', msg)
        print("Data successfully hidden!")
    else:
        key1 = getpass.getpass("Enter secret key to retrieve the data: ")   # Decryption of data from the image
        if key == key1:
            secret = crypto_steganography.retrieve('output1.png')
            print("Encoded data: ", secret)         # Secret message displayed
        else:
            print("The entered key is INCORRECT")
            print("Please enter the correct secret key")  

    print(" ")
    opt= int(input("1. Encode \t 2. Decode \t 3. Quit :: "))
