## Description:
- My project works on displaying Current Time Stamps
- To create Current time stamps using python, we will need to import two Python modules one for creating GUI and another to get year data.
- **Pendulum**, Pendulum is one of the libraries in python which provides easily manages complex date manipulations better than native DateTime instances. It also manages timezones.
- And for the speaking purpose, we will use **pyttsx3**.

## Procedure: 
```python
import pendulum
import pyttsx3  
```
- First after importing modules.
- After that we will make a function **speak()** in which we will set the rate of speaking and the type of voice.
- Then we will take input from user for which year you want to display the calendar.
- After that in code section we will first use **pendulum.now()** which will tell the current date and time of that zone.
- After displaying it, a bot voice will ask you to enter a location which is evaluated in try and except block.

## Sample Output:
![LGM](https://github.com/AmitGupta700/Awesome_Python_Scripts/blob/main/AutomationScripts/Current%20Time%20Stamps/Images/Output.png)

## For any query please contact:
<a href="https://www.linkedin.com/in/amit-gupta-681206191/">LinkedIn</a>
