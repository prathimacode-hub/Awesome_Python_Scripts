# Dr Battery 🔋
## Aim 
To create a Dr Battery a Battery alert notifier for Lappy.
## Purpose
- Dr Battery is continuously monitor your battery level and saves your Lappy from draining and over charging by notifing you:
## Short description
- Battery is one of the important components in our system. We've to protect it from over charging and draining at the same time.
- This code wil let you know when the battery is draining and generates a voice output that ask you to charge.
- Also asks you to unplug if the battery seems to be over charging.
- In the end this will help you to increase the life time of your battery.
- ***Libraries Imported:***
    - `psutil`
    - `time`
    - `pyttsx3`
    - `win10toast`
    - `ToastNotifier`
    - `threading`
## Workflow
- Import all the required libraries i.e., psutil, time, pyttsx3, win10toast, Toast Notifier, threading.
- `psutil`
    - ***Installation:***  `pip install psutil`
    - ***Purpose:*** Used for system monitoring
- `time`
    - ***Installation:***  This Library is part of Python's Standard library no need install separately.
    - ***Purpose:*** Delaying notification
- `pyttsx3`
    - ***Installation:***  `pip install pyttsx3`
    - ***Purpose:*** This is text to speech convertor used here to generate voice notification.
- `win10toast`
    - ***Installation:***  `pip install win10toast`
    - ***Purpose:***  Used for importind `Toast Notifier`. This displays notification.
- `threading`
    - ***Installation:***  `pip install threading`
    - ***Purpose:*** Used to give desktop notification and voice notification at the same time.

## Compilation Steps
- Download the file [Dr_Battery.py](https://github.com/DurgaSai-16/Awesome_Python_Scripts/blob/main/GUIScripts/Dr%20Battery/Dr_Battery.py)
- Run the file [Dr_Battery.py](https://github.com/DurgaSai-16/Awesome_Python_Scripts/blob/main/GUIScripts/Dr%20Battery/Dr_Battery.py)
- Now our Dr Battery starts Monitoring our Lappy. Leave it in the background do your works in Lappy.
- When Lappy goes below 40% then it generates a voice asking you to plug in the charge as well as a notification saying the same. This won't stop until you plug the charger.
- When Lappy goes above 90% then it generates a voice asking you to unplug the charge as well as a notification saying the same. This won't stop until you unplug the charger.
- If you forgot to unplug and it reaches 100% then it generates notification saying battery full please unplug. This won't stop until you plug out the charger from the socket.
-  
## Output
- **Low Battery (<40%)**
![LowBatteryLow](https://user-images.githubusercontent.com/85128689/127781919-8b6e474f-c54a-450b-97f3-a46909d9cd2f.png)

Pathlink: https://github.com/DurgaSai-16/Awesome_Python_Scripts/blob/main/GUIScripts/Dr%20Battery/Images/LowBattery.jpg


- **Over Charged (> 90%)**
![OverCharge](https://user-images.githubusercontent.com/85128689/127782617-71d0b319-325f-467d-82e9-9a6d3274ee06.png)

Pathlink: https://github.com/DurgaSai-16/Awesome_Python_Scripts/blob/main/GUIScripts/Dr%20Battery/Images/Over%20Charged.jpg

- **Fully Charged (100%)**
![Fully Charged](https://user-images.githubusercontent.com/85128689/127782770-b7169c08-ce41-47b9-82a9-f9e3d34d3c85.png)

Pathlink: https://github.com/DurgaSai-16/Awesome_Python_Scripts/blob/main/GUIScripts/Dr%20Battery/Images/Over%20Charged.jpg


## Author:
[NALLANI DURGA SAI](https://github.com/DurgaSai-16)
