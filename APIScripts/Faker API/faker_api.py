#Importing required libraries
import fakerapi
import json
import requests

'''
Faker Library is used to create fake data 
In it's syntax , Every resource accepts 3 common GET parameters:
_locale
_quantity
_seed


_Locale : This parameter means the language of the API response we want to get and accept the locale format "en_EN". 
For example: https://fakerapi.it/api/v1/persons?_locale=en_EN . This example returns people with English names.

_quantity : This parameter means the number of rows we want to obtain and accept only integers.
If you request more than 1000 rows (maximum) the system will return 1000 rows anyway.
Default Value : 10
Min: 1 - Max: 1000
Example : https://fakerapi.it/api/v1/addresses?_quantity=5 This example returns 5 Addresses

_seed : This parameter accept an integer and allows to get always the same results. 
So, executing the same request with _seed parameter set to the same value (ex. 12345) the results will never change.
Default Value : null
Example : https://fakerapi.it/api/v1/companies?_seed=12456

'''

#Now we will go through the basic example and discover some of the options Faker provides us to generate random data for

response = requests.get('https://fakerapi.it/api/v1/addresses?_quantity=5')
print(response.status_code)
#To check whether API call is successful(200) or not(404)

print(response.text) 
# To access all the content of the website

print(response.url) 
# print(response.url) # url of the website to which we made our API call

print("\n\n")
python_data = json.loads(response.text) # Converting json data to python data
# print(type(python_data)) 
for key in python_data.keys():
    print(f'{key} : {python_data[key]}') # Calling the whole data from the API

# In this example 5 Addresses were printed , apart from addresses we will see some other options Faker provides us with.

#Example 1 : Credit Cards 
response = requests.get('https://fakerapi.it/api/v1/credit_cards?_quantity=3')
print("\n\n")
python_data = json.loads(response.text) # Converting json data to python data
# print(type(python_data)) 
for key in python_data.keys():
    print(f'{key} : {python_data[key]}') 

#In this example we got details of 3 fake credit cards

#Example 2 : Places
response = requests.get('https://fakerapi.it/api/v1/places?_quantity=1')
print("\n\n")
python_data = json.loads(response.text) # Converting json data to python data
# print(type(python_data)) 
for key in python_data.keys():
    print(f'{key} : {python_data[key]}')
# In this example we are generating fake data for any random place with position of their longitude and longitude

#Example 3 : Persons
response = requests.get('https://fakerapi.it/api/v1/users?_quantity=7&_gender=female')
print("\n\n")
python_data = json.loads(response.text) # Converting json data to python data
# print(type(python_data)) 
for key in python_data.keys():
    print(f'{key} : {python_data[key]}')
# In this data of 7 random females are generated , with their firstname, lastname,email,etc.