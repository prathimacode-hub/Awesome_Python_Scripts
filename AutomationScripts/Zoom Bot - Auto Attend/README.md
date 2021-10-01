
## What are Bots?
Bots are software programs that combine requests, which are typically provided as text, with contextual data, such as geolocation and payment information, to appropriately handle the request and respond. Bots are often also called "chatbots", "assistants" or "agents."


## Zoom Auto attend Bot:

This Bot Requires the Timings csv file which contains meetingId,Time and password for zoom account.
Then this bot logs into the account and attends the meeting

## Steps Included :
* Opens up the zoom app
* clicks the join button
* Type the meeting ID
* Disables both the camera and the mic
* Hits the join button
* Types the password and hits enter
   
## Setup instructions

**Requirements:** python-3.8.6

* Clone the GitHub repo
```
git clone https://github.com/Anish-Malla/Zoom-Automation-Python
```
* cd into the directory
* Install required libraries
```
pip3 install pandas
```
* Follow the instructions specific to your OS for downloading pyautogui
```
https://pyautogui.readthedocs.io/en/latest/install.html
```
* Update the timings.csv with the time of the meeting, meeting id and password, do not add any unnecessary spaces. (Do not open the csv using excel as it changes the formatting)

**Note: windows users**

The code to open zoom is different for windows, this is shown in the main.py file make the changes accordingly.
