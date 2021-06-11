#This is basic Alarm Clock program.<br>

**Modules used in Alarm Clock project**<br>
#1 time<br>
written as : import time<br>
#This module provides various time-related functions.<br>
<br> 

along with time module localtime() method of Time module also used.
#localtime()<br>
function takes the number of seconds passed since epoch{Period} as an argument and returns struct_time in local time.<br>
<br>
In the project **time.localtime().tm_hour** convert seconds into current local hours.<br>
<br>
Also, convert **time.localtime().tm_min** convert seconds into current local minutes.<br> 
<br>
#2 playsound
**play sound in Python**
<br>
It requires one argument - the path to the file with the sound you’d like to play. This may be a local file, or a URL. In the project I use local file.<br>
<br>
**for playing sound in alarm clock.py**<br>
steps need to be followed 
<br>
#Step 1: install playsound module by writing pip install playsound in WindowsPowerShell.<br>
<br>
#Step 2: import playsound module in Alarm_clock.py by writing **from playsound import playsound**<br>
<br>
#Step 3: Download alarm ringtone using link "https://freetone.org/ringtones/melodies/alarm_clock_nice-10516"<br>
<br>
#Step 4: In the line 14 of the code where playsound is written:
                 playsound(r'here you need to write the path where the above ringtone is downloaded')<br>
         for example:   *****playsound(r'C:\Users\HP\Downloads\13767_nice_larm_clock.mp3')*****<br>
<br>
## Program is now ready to go with sound <br>

<br>
Alarm will ring at your given time setting.<br>
<br>
**Working of Program**<br>

This script is the basic program using time module of Python<br>
when you input hours and minutues for alarm to ring at that respective time alarm will ring<br>
<br>
##This script is the basic program using **time** module of python<br>
<br>
***Screenshot of the output:***
<p align="center"><img src="https://github.com/prathimacode-hub/Awesome_Python_Scripts/blob/main/BasicPythonScripts/Alarm%20Clock/Images/Screenshot.png?raw=true">"</p>
<br>
Name of Author: Pratima Kushwaha


