
# Initial Imports
import subprocess
import pyautogui
import time
import pandas as pd
from datetime import datetime


# Sign in method for the bot to sign in to zoom app
def sign_in_zoom(meetingid, pswd):
    #Opens up the zoom app
    #change the path specific to your computer
    
    #If on windows use below line for opening zoom
    #subprocess.call('C:\\myprogram.exe')
    
    #If on mac / Linux use below line for opening zoom
    subprocess.call(["/usr/bin/open", "/Applications/zoom.us.app"])

    time.sleep(10)
    
    #clicks the join button
    joining_btn = pyautogui.locateCenterOnScreen('join_button.png')
    pyautogui.moveTo(joining_btn)
    pyautogui.click()

    # Type the meeting ID
    meet_id =  pyautogui.locateCenterOnScreen('meeting_id_button.png')
    pyautogui.moveTo(meet_id)
    pyautogui.click()
    pyautogui.write(meetingid)

    # Disables both the camera and the mic
    media_btn = pyautogui.locateAllOnScreen('media_btn.png')
    for btn in media_btn:
        pyautogui.moveTo(btn)
        pyautogui.click()
        time.sleep(2)

    # Hits the join button
    joining_btn = pyautogui.locateCenterOnScreen('joining_btn.png')
    pyautogui.moveTo(joining_btn)
    pyautogui.click()
    
    time.sleep(5)
    #Types the password and hits enter
    meet_password_btn = pyautogui.locateCenterOnScreen('meeting_pswd.png')
    pyautogui.moveTo(meet_password_btn)
    pyautogui.click()
    pyautogui.write(pswd)
    pyautogui.press('enter')

# Reading the file
df = pd.read_csv('timings.csv')

while True:
    # checking of the current time exists in our csv file
    now = datetime.now().strftime("%H:%M")
    if now in str(df['timings']):

       row = df.loc[df['timings'] == now]
       m_id = str(row.iloc[0,1])
       m_pswd = str(row.iloc[0,2])

       sign_in_zoom(m_id, m_pswd)
       time.sleep(40)
       print('signed in')
