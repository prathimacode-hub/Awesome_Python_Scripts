import pyautogui
import time

message = 5  #Here message variable stores the no. of times message prints
while message:
    time.sleep(4)
    pyautogui.typewrite("Hello ,How are you?")
    time.sleep(2)
    pyautogui.press('enter')
   