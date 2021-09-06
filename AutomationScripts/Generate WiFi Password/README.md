# Generate WiFi Password and Send to Specified Email Address


## Aim

The aim of this project to create a program that can extract all the WiFi names with their passwords from any particular PC, Laptop, etc.

## Short description of package/script

- Basically this program extracts all the passwords of all the WiFi that is currently connected and all previous connected WiFi. 
- It collects names of all the WiFi as in SSIDs and their passwords and sends them to the Specified email address.

* Note: The sender's email address must set to allow less secure apps, if you are using Gmail.

## Workflow of the Project

- First this program will run a command in command prompt to view all WiFi profiles.
- Then it will extract SSIDs of each of the WiFi profile.
- After that it will check if the selected SSID has a password or else it will ignore that SSID if no password is found as it's open WiFi or WiFi which is not connected.
- Then after formating them as in "WiFi_Name: Password", it will send it to the specified email address.


## Setup instructions

- You just need to install some of the libraries of python and you can run this program.
- All the libraries are mentioned in requirements.txt


# Screenshot of Output
<p align="center"><img src="https://github.com/shubhdholakiya/Awesome_Python_Scripts/blob/a4bb7774583b694204cf98b321d678949b67bda4/AutomationScripts/Generate%20WiFi%20Password/Images/Mail%20Sent%20from%20Dummy%20Email%20Address.JPG">"</p>
<br>

<p align="center"><img src="https://github.com/shubhdholakiya/Awesome_Python_Scripts/blob/a4bb7774583b694204cf98b321d678949b67bda4/AutomationScripts/Generate%20WiFi%20Password/Images/Mail%20Received.jpg">"</p>
<br>

## Author(s)

Shubh Dholakiya
