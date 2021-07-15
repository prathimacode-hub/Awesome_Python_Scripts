# Family Key Logger

## Aim

The main aim of this project is to create a family keylogger.

## Purpose

The purpose of this script is to run in the background and log whatever the user is typing through the keyboard input. 

## Short description of package/script

This key logger is a python based script which logs and stores key-strokes. The key-strokes are then saved on the hard-drive in a text file. 
<br>
It can be ethically used by parents to track what their children are doing on the internet. Key loggers are used in corporations where employers track and keep a log of what their employees are doing.

## Workflow of the Project
 
- We have installed and used the 'pynput' module to get and track the input from the keyboard. 
- We have installed and used the 'win10toast' module to get the ToastNotifier for Windows 10.
- Just run the script through the terminal.
- You will see a notification saying - "A family keylogger has started to work" which tells that the script has started to work.


## Setup instructions
- You should have 'pynput' module in your system. If you don't have just install it through the terminal using the following command 
   ```sh
   pip install pynput
   ```
 - You should have 'win10toast' module in your system. If you don't have just install it through the terminal using the following command 
   ```sh
   pip install win10toast
   ```
 - Finally to run this script in the background of your computer, open the terminal and type-in the below mentioned command 
    ```sh
   python key_logger.py
   ```

## Compilation Steps

- Open the python script code in any of your ide. 
- Follow the above mentioned Setup Instructions. 
- Debug and Run your code


## Output

<img src="Images/Screenshot%20(368).png" width = "720" height = "480">


## Author

Name of author : [Dhruv Mehta](https://github.com/Dhruv-194)


## Disclaimers, if any

- Never use this script for wrong purposes, that is to track someone without their knowledge.
- To test and make this script work you need to turn off your antivirus and windows defender otherwise the script will be flagged as malicious software and you will not be able to work/run it.
- If you want to stop the script from running in the background then just open the task manager and close the python module in it.


