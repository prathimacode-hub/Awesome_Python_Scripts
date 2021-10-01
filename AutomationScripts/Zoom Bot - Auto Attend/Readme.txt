
## Zoom Auto attend Bot :

This Bot Requires the Timings csv file which contains meetingId,Time and password for zoom account.
Then this bot logs into the account and attends the meeting




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