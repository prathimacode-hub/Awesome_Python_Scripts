## Rain Alert Notification

## Aim

To take city name, sender's email ID, sender's password, receiver's email ID, API key as input and then emailing the registered user about the 12 hour weather forecast of that city.

## Purpose

We can easily put the code into cloud servers and then it will email us about the 12 hour weather forecast making our lives easy so that we have an idea if it's goind to rain or not.

## Short description of package/script

- The script uses openweathermap.org/api to get weather information and emails the user about the weather forecast of input city.
- Also for accessing full link I have used city_list.json data which contains the latitude and longitude of the input city.
- Libraries : json, requests, smtplib

## Workflow of the Project

- Initally I am taking input city from user. After that I am changing that input city to correct format i.e. first letter of each word has to be capital.
- Then I am taking city data and then looping through that data and then checking if the city is present in the data.
- If the city name is present then I am taking storing its latitude and longitude values.
- Then I am getting data from link : https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}.
- Here "lat" is latitude and "lon" is longitude which depends on city. Also the link requires an API key.
- Now I have access to the data, so then I am finding weather forecast which is present after "main". 
- After that I am sending a message to the registered email ID about 12 hour weather forecast.

## Setup instructions

- First of all, download the city_list.json file and keep it in the same location as python code file.
- For sender, create an account on website : https://openweathermap.org/ and then you'll have deafult API key.
- Sender also has to input the email ID as well as password.
- receiver just need to input email ID. 

## Detailed explanation of script, if needed

Explained above.

## Compilation Steps

After arranging all the things as mentioned in "setup instructions". Just run the code in the IDLE or command prompt and then input all the things mentioned in "setup instructions".

## Author(s)

Varun Kumar
