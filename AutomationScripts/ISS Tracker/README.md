## Description: 
[**Here**](https://github.com/Aditya8821/Awesome_Python_Scripts/blob/main/AutomationScripts/ISS%20Tracker/iss_tracker.py) is Python Script which tracks the current location of ISS(International Space Station)
and then map location.
This displays the current location of ISS along with onboarded crew names. It works by use of API, it takes the current location of ISS in form of latitude and longitude and then locates that value onto the map. It takes the value from the website at very 5 sec and then updates the value of lati. and long. and thus also moves the ISS icon on the map. The movement visible is very little but you can notice that movement in the gif below.
This is possible by using some of the modules of python like JSON, Urllib.requests, Webbrowser, Geocoder etc. Numerous functions are used to create thsi script.
Some of the modules are listed below.

## Purpose:
This script helps to get the information about ISS that is revolving over the earth gravitational field. It helps us to know the names of onboarded crew inside it along with the current real time location in form of latitude and longitude. Then using that lat and long we have mapped that particular location in the map.

- **JSON:**
This JSOn module is used to decode a JSON document from a string that may have extraneous data at the end.

- **Urllib.requests:**
It offers a very simple interface, in the form of the urlopen function. This is capable of fetching URLs using a variety of different protocols.

- **Webbrowser**
This webbrowser module allows to open the web browser from a python script By simply calling the open() function of the module.

- **Geocoder**
Geocoder is a simple and consistent geocoding library written in Python. Dealing with multiple different geocoding provider.

## Procedure to follow: 
- pip install json
- pip install turtle
- pip install geocoder
- pip install requests
- pip install time
- store api link in url variable
- extract required data from that url and display that in txt form.
- Use latitude and longitude real time value from extracted data and keep on update the location of ISS on map in every 5 sec.

## Sample Output Crew Info:
<p align="center"><img src="https://github.com/Aditya8821/Awesome_Python_Scripts/blob/main/AutomationScripts/ISS%20Tracker/Images%20%26%20Video/iss%20crew%20info.png"></p>

## Sample Output ISS Location:
<p align="center"><img src="https://github.com/Aditya8821/Awesome_Python_Scripts/blob/main/AutomationScripts/ISS%20Tracker/Images%20%26%20Video/iss%20location%20map.png"></p>

## Sample Output Video ISS Moving:
<p align="center"><img src="https://github.com/Aditya8821/Awesome_Python_Scripts/blob/main/AutomationScripts/ISS%20Tracker/Images%20%26%20Video/iss%20live%20video.gif"></p>

For any queries please contact?
- [**LinkedIn**](https://www.linkedin.com/in/aditya-trivedi-032090164/)
