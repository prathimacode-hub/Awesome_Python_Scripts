import pyautogui
import time

message = 5  #Here message variable stores the no. of times message prints
while message:
    time.sleep(4)
    pyautogui.typewrite("Hello ,How are you?"
                       "What is your today's schedule , I want a meet with you?"
                        "Please reply me as early as possible.")
    time.sleep(2)
    pyautogui.press('enter')
   
