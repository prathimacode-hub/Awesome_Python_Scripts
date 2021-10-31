# Faker API (Fake Data Generator)

## AIM
To randomly generate fake data for further application

## Purpose
To generate fake data for Data Science purposes or testing purposes [FAKER API](https://fakerapi.it/en)  
We can generate fake data related to:
 - Address , which includes the street address , city , district, pincode ,etc.
 - People , whether male or female , with the inclusion of first name , last name , email id ,etc.
 - Credit Card Information , all the factors related to credit cards , like card no . , cvv,card holder name ,etc.
 - Location , which includes the latitude and longitude of the location
 - Companies : with their name , email address,contact no , location , etc.
 <br>
 and many more ...

## Short description of package/script
 Libraries used in this project are:<br>
  - ```requests```:- To get an API call from the website. <br>
  - ```json```:- To convert the json data that we got from API to python data.
  - ```fakerapi```:- To call in the Faker package to generate fake data

## Workflow of the Project
This project follows the following steps:<br>
 - Importing relevant libraries
 - Making an API call
 - Converting json data to python data
 - Accessing the python data to show the records.

## Setup Instructions
In order to run this code in your system, one needs to make sure that relevant libraries are installed, use the following commands for installation:
 - ```pip install requests```<br>
 - ```pip install json```

## Outputs
<br>
 ![image](https://user-images.githubusercontent.com/74582422/139575631-7ea06e9e-4159-4cff-a9e6-5755f322a6d2.png)
Request call getting 200 means API call successfull <br>
![image](https://user-images.githubusercontent.com/74582422/139575666-698309f4-2f46-4812-bf81-f0141aa6bc37.png)
Fake Address Generation eg <br>
![image](https://user-images.githubusercontent.com/74582422/139575688-d74084e4-067d-43c4-9185-2c206dc276c3.png)
Fake credit card details generated <br>
![image](https://user-images.githubusercontent.com/74582422/139575702-3038ae81-b8e7-44df-ad72-8d708be3d278.png)
Fake location generation <br>
![image](https://user-images.githubusercontent.com/74582422/139575726-e69dd5e4-fd92-4d19-a9b8-d8464590aaba.png)
Fake People generation <br>


## Author
 [Shiwansh Raj](https://github.com/photon149)
