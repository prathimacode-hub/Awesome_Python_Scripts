# An Automation script to automatically join a scheduled google-meet meeting at a specific time without manual labour.

# importing the required python packages
import pyautogui
import webbrowser
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

print("THIS IS A PROGRAM FOR GMEET AUTOMATION\nThis PROGRAM WILL HELP YOU TO JOIN YOUR CLASSES ON TIME\nTHANKS TO SANSKAR DWIVEDI FOR MAKING THIS\n\n")

now = datetime.now()
current_day = now.strftime("%H:%M/%A")
print(current_day)



            
while True:
    now = datetime.now()  # check the current system time
    day=now.strftime("%A")
    justtime=int(now.strftime("%H%M"))
    print(justtime)
    s=now.strftime("%S")
    se=int(s) 
    
    while(940<=justtime):
        #MATHS SHEDULE
        if(day=="Monday" and 955<=justtime<=1050 or day=="Wednesday" and 955<=justtime<=1050 or day=="Thursday" and 1055<=justtime<=1250 or day=="Friday" and 1255<=justtime<=1250):
            pyautogui.prompt(text="YOU ARE JOINING TO MATHS CLASS HOPE YOU COMPLETED THE PREVIOUS STUFFS")
            time.sleep(2)
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open_new("https://meet.google.com/weg-kaez-ytb")
            
            
            time.sleep(5)
            pyautogui.click(659, 960)
            time.sleep(5)
            pyautogui.hotkey('ctrl','d')
            time.sleep(5)
            pyautogui.click(1425, 720)
            time.sleep(2500)
            break
        #BEE SHEDULE
        if(day=="Monday" and 1055<=justtime<=1150 or day=="Thursday" and 1155<=justtime<=1250 or day=="Friday" and 1055<=justtime<=1150):
            print("YOU ARE JOINING TO BEE CLASS HOPE YOU COMPLETED THE PREVIOUS STUFF")
           
            time.sleep(2)
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open_new("https://meet.google.com/pex-ktrx-qrk")
            time.sleep(5)
            pyautogui.click(659, 960)
            time.sleep(5)
            pyautogui.hotkey('ctrl','d')
            time.sleep(5)
            pyautogui.click(1425, 720)
            time.sleep(2500)

            
        #CHEMISTRY SHEDULE
        if(day=="Monday" and 1155<=justtime<=1250 or day=="Tuesday" and 955<=justtime<=1050 or day=="Wednesday" and 1155<=justtime<=1250):
            
            print("YOU ARE JOINING TO CHEMISTRY CLASS HOPE YOU COMPLETED THE PREVIOUS STUFF")
            time.sleep(2)
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open_new("https://meet.google.com/sbp-urci-ibv")
            time.sleep(5)
            pyautogui.click(659, 960)
            time.sleep(5)
            pyautogui.hotkey('ctrl','d')
            time.sleep(5)
            pyautogui.click(1425, 720)
            time.sleep(2500)
            break
        #ECOLOGY SHEDULE
        if(day=="Tuesday" and 1155<=justtime<=1250 or day=="Wednesday" and 1055<=justtime<=1150 or day=="Thursday" and 940<=justtime<=1050 ):
            
            print("YOU ARE JOINING TO ECOLOGY CLASS HOPE YOU COMPLETED THE PREVIOUS STUFFS")
            
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open_new("https://meet.google.com/vhg-ptym-znf")
            time.sleep(5)
            pyautogui.click(659, 960)
            time.sleep(5)
            pyautogui.hotkey('ctrl','d')
            time.sleep(5)
            pyautogui.click(1425, 720)
            time.sleep(2500)
            break
        
        #IWT SHEDULE
        if(day=="Tuesday" and 1050<=justtime<=1150 or  day=="Friday" and 955<=justtime<=1050 ):
            print("YOU ARE JOINING TO MATHS CLASS HOPE YOU COMPLETED THE PREVIOUS STUFFS")
            time.sleep(2)
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open_new("https://meet.google.com/aed-dnej-jta")
            time.sleep(5)
            pyautogui.click(659, 960)
            time.sleep(5)
            pyautogui.hotkey('ctrl','d')
            time.sleep(5)
            pyautogui.click(1425, 720)
            time.sleep(2500)
            break

        if(justtime>1500):
            
            pyautogui.alert(text='classes are over you are joining to test class ',button='ok')
            time.sleep(2)
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open_new("https://meet.google.com/dqy-tgte-vco")
            time.sleep(5)
            pyautogui.click(659, 960)
            time.sleep(5)
            pyautogui.hotkey('ctrl','d')
            time.sleep(5)
            pyautogui.click(1425, 720)
            time.sleep(2500)
            break

            quit()
            break

        
    time.sleep(60-se)

    
        
    



        
 
        
        
        
    
        
    

