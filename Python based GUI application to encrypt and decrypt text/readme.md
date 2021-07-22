## Name: SHIVAM RAVI
## PROJECT CODE
##             on
## “Python based GUI application to encrypt and decrypt text”
##   DevIncept Participant
## Issue no: #660
## Contributed to: Awesome_Python_Scripts

## Aim

In this project, I have developed a GUI app that can encrypt and decrypt text.
This includes implementation of Caesar Cipher algorithm to perform the required operations.
The basic working of this app is that the app consists of a text bar where the user
enters the text.There are two options available, either the user can encrypt the text or can decrypt the text. When the user clicks on any one of the option, the operation is performed and the user is presented with the encrypted / decrypted text.


## Purpose

Let us consider a case where the user sends a text from his phone to his friend. The risk of the data being accessed by a third party is high when the data enters the cloud platform. Hence a new method to secure the messages is to be done by building an algorithm which can give more security and consumes less time. The identity of the user must also be verified by using the authentication before sending any messages.

Due to recent surge in cyber attacks in the past few years, the user data is at risk and could be used for other criminal activities. So there should be a mechanism to secure the data being transferred from one device to other by authenticating user’s identity and converting the messages to a form which could not be decoded easily in one shot.


## Workflow of the Project

In order to complete this project, we first verify the identity of the user before sending the message. We have used ohawf [ Easy OAuth2 authentication for Google services ] package which uses Google API that will access your identity by signing into your Gmail id and allows you to authenticate by giving you unique token which you need to pass this token in our app before proceeding further.

The code also uses the Python Tkinter library, which is very popular for building graphical user interfaces (GUIs) Tkinter is a Python binding to the Tk GUI toolkit. It is the standard Python interface to the Tk GUI toolkit, and is Python's de facto standard GUI.

After required packages loaded successfully, we start by creating our GUI app. We initialize tkinter by creating a root widget, which is a frame/window where we are going to attach our radio buttons and the text bar. There can be only one root widget and it has to be created before any other widgets.

Now we define our Encryption and decryption function. The function basically traverses through the given text character by character. For each character, we convert it according to the algorithm we defined earlier. Then we return the newly generated text. We also create text labels which will show the output after the execution of the function.


## Software Requirements:

  <> Jupyter Notebook
  <> Python 3

## Hardware Requirements:

  <> Operating System: Windows 7 above, Ubuntu
  <> RAM : 4GB or above
  <> Processor: Intel core i5 2.40GHz and above

