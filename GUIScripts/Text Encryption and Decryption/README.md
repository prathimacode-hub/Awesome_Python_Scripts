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

## Short description of packages

<> Tkinter ( Version 8.5 ): Tkinter is a Python binding to the Tk GUI toolkit. It is the standard Python interface to the Tk 			    GUI toolkit, and is Python's de facto standard GUI.Tkinter is included with standard 			    		    Linux, Microsoft Windows and Mac OS X installs of Python. As with most other modern Tk bindings, 			    Tkinter is implemented as a Python wrapper around a complete Tcl interpreter embedded in the 			            Python interpreter. Tkinter calls are translated into Tcl commands, which are fed to this 			    		    embedded interpreter, thus making it possible to mix Python and Tcl in a single application.
			    There are several popular GUI library alternatives available, such as wxPython, PyQt, PySide,    			    Pygame, Pyglet, and PyGTK.

<> Ohawf ( Version 0.0.5 ): Easy OAuth2 authentication for Google services, a package which uses Google API that will access 			    	    your identity by signing into your Gmail id and allows you to authenticate by giving you unique 				    token which you need to pass this token in our app before proceeding further.

<> simple-crypt ( Version 3.1 ): Simple Crypt encrypts and decrypts data. It has two functions, encrypt and decrypt. It uses 				 standard, well-known algorithms, closely following the recommendations here.
				 The established, efficient pycrypto library provides the algorithm implementations (the 		 		         cipher used is AES256).It includes a check (an HMAC with SHA256) to warn when ciphertext 				 data are modified.

## Setup instructions

For importing necessary libraries, you just need to write import just before the package you want to include in your script. For e.g to include numpy module, you have to type "import numpy". 

The most sought after way of writing a Python program is by using a plain text editor. The code written in the Python interactive session is lost once the session is closed, though it allows the user to write a lot of lines of code. On Windows, the files use the .py extension.  

If you are at the beginning of working with Python, you can use editors like PyCharm or Notepad++ which are easy-to-use or any other text editors.

Now you need to create a test script. In order to do that, open your most suited text editor and write the code.
Then save the file in your desktop with the name first_script.py or anything you like. Remember you need to give the .py extension only.

<> Using python command:
The most basic and the easy way to run Python scripts is by using the python command. You need to open a command-line and type the word python followed by the path to your script file, like this: "python first_script.py"
Then you hit the ENTER button from the keyboard and that's it.

However, if you do not get the output, you might want to check your system PATH and the place where you saved your file. If it still doesn’t work, re-install Python in your system and try again.

## Purpose

Let us consider a case where the user sends a text from his phone to his friend. The risk of the data being accessed by a third party is high when the data enters the cloud platform. Hence a new method to secure the messages is to be done by building an algorithm which can give more security and consumes less time. The identity of the user must also be verified by using the authentication before sending any messages.

Due to recent surge in cyber attacks in the past few years, the user data is at risk and could be used for other criminal activities. So there should be a mechanism to secure the data being transferred from one device to other by authenticating user’s identity and converting the messages to a form which could not be decoded easily in one shot.


## Workflow of the Project

In order to complete this project, we first verify the identity of the user before sending the message. We have used ohawf [ Easy OAuth2 authentication for Google services ] package which uses Google API that will access your identity by signing into your Gmail id and allows you to authenticate by giving you unique token which you need to pass this token in our app before proceeding further.

The code also uses the Python Tkinter library, which is very popular for building graphical user interfaces (GUIs) Tkinter is a Python binding to the Tk GUI toolkit. It is the standard Python interface to the Tk GUI toolkit, and is Python's de facto standard GUI.

After required packages loaded successfully, we start by creating our GUI app. We initialize tkinter by creating a root widget, which is a frame/window where we are going to attach our radio buttons and the text bar. There can be only one root widget and it has to be created before any other widgets.

Now we define our Encryption and decryption function. The function basically traverses through the given text character by character. For each character, we convert it according to the algorithm we defined earlier. Then we return the newly generated text. We also create text labels which will show the output after the execution of the function.


## Compilation Steps


Python first compiles your source code (.py file) into a format known as byte code . Compilation is simply a translation step, and byte code is a lower-level, and platform-independent, representation of your source code. Compiled code is usually stored in .pyc files , and is regenerated when the source is updated, or when otherwise necessary. In order to distribute a program to people who already have Python installed, you can ship either the .py files or the .pyc files.

The bytecode (.pyc file) is loaded into the Python runtime and interpreted by a Python Virtual Machine , which is a piece of code that reads each instruction in the bytecode and executes whatever operation is indicated. Byte code compilation is automatic, and the PVM is just part of the Python system that you have installed on your machine. The PVM is always present as part of the Python system , and is the component that truly runs your scripts.


## Output

1. UI output of our project:
2. Typing text and clicking on Encryption to get encrypted text.
3. Clicking on Decryption to get decrypted text.

<p align="center">
  <img width = 500 src="Images/Screenshot (338).png" /><br>
  <img width = 500 src="Images/Screenshot (339).png" /><br>
  <img width = 500 src="Images/Screenshot (340).png" /><br>
</p>





## Author(s): Shivam Ravi



