![](http://ForTheBadge.com/images/badges/made-with-python.svg)
![](https://forthebadge.com/images/badges/built-by-developers.svg)</br>
[![Prettier](https://img.shields.io/badge/Code%20Style-Prettier-red.svg)](https://github.com/prettier/prettier)
![License](https://img.shields.io/badge/License-MIT-red.svg)</br>

## Description: 
- Let's [**look**](https://github.com/Iamtripathisatyam/Awesome_Python_Scripts/blob/main/BasicPythonScripts/Distance%20Finder/distance.py) at a Python script that calculates the distance between two locations.
- It accepts two cities as input and calculates longitude and latitude for them.
- Finally, the result will be displayed in kilometres.

## Procedure to follow: 
```python
      from geopy.geocoders import Nominatim 
      from geopy.distance import geodesic 
```
- Set the user agent where all the data will be fetched using the **Nominatim** function; in our example, it'll be **Google Map**.
- Take the user's input for two cities.
- Now, using **geocode**, retrieve all of the data, including all of the city's details, such as **latitude**, **longitude**, and so on.
- Both cities longitude and latitude should be saved in separate variables.
- Use **geodesic** to determine the city's name based on its longi and lati.
- Finally, in kilometers, display the result.


## Sample Output: 

![hey](https://github.com/Iamtripathisatyam/Awesome_Python_Scripts/blob/main/BasicPythonScripts/Distance%20Finder/Images/output.jpg)
