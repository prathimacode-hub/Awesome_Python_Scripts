# COWIN API

COWIN is a cloud-based IT solution for planning, implementation, monitoring, and evaluation of Covid-19 vaccination in India.

<br>

The COWIN public API can be used to obtain the details of vaccination sessions available.
<br>

The API can be used 
- to get available vaccination sessions on a specific date in a given pincode.
- to get available vaccination sessions on a specific date in a given district.
- to get available vaccination sessions for 7 days from a specific date in a given pincode.
- to get available vaccination sessions for 7 days from a specific date in a given district.

<br>    

# Source  
### https://apisetu.gov.in/public/api/cowin 

<br>  

### Example API Request: 
### https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/[GET/POST method]?options={options}

<br>

# Setup Instructions

1. Have Python 3.x setup in the system
2. Install the necessary packages 
3. Run the code using the command

    ```
      python cowin_api.py
    ```
   and obtain the Output

<br> 

# Workflow of the Program

1. Choose the option to obtain details of vaccination sessions
2. Entering wrong option prompts the user to enter the right option
3. Enter the date in proper format 
4. Enter PINCODE or District ID according to the option entered
5. Obtain the Output

<br> 

# Output

<img src="Images/img3.gif">